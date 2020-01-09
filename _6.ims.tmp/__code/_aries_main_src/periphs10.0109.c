
// *****************************************************
// Dependencies
// *****************************************************
#include "periphs.h"
#include "sleep.h"
#include "main.h"
//#include "xuartps.h"

//----------------------------------JACKY ADD-------------------------------
/***************************** Include Files ********************************/

#include "xparameters.h"
#include "xgpio.h"
#include "stdio.h"
#include "xstatus.h"
#include "xil_printf.h"
//---------------------------------------------------------------------------
//---------------------------------------JACKY ADD-----------------------------
#ifdef XPAR_INTC_0_DEVICE_ID
 #define INTC_DEVICE_ID	XPAR_INTC_0_DEVICE_ID
 #define INTC		XIntc
 #define INTC_HANDLER	XIntc_InterruptHandler
#else
 #define INTC_DEVICE_ID	XPAR_SCUGIC_SINGLE_DEVICE_ID
 #define INTC		XScuGic
 #define INTC_HANDLER	XScuGic_InterruptHandler
#endif /* XPAR_INTC_0_DEVICE_ID */

/************************** Function Prototypes ******************************/
void GpioHandler(void *CallBackRef);

int GpioIntrExample(INTC *IntcInstancePtr, XGpio *InstancePtr,
			u16 DeviceId, u16 IntrId,
			u16 IntrMask);

int GpioSetupIntrSystem(INTC *IntcInstancePtr, XGpio *InstancePtr,
			u16 DeviceId, u16 IntrId, u16 IntrMask);

void GpioDisableIntr(INTC *IntcInstancePtr, XGpio *InstancePtr,
			u16 IntrId, u16 IntrMask);

/************************** Function Prototypes ****************************/

int GpioOutputExample(u16 DeviceId, u32 GpioWidth, u8 FrameReadyCount);

int GpioOutput_graylevel_axis_Write(u16 DeviceId, u32 graylevel_axis_Write_left_top, u32 graylevel_axis_Write_right_down);//JACKY2020
int gray_monitor();//JACKY2020
int get_gray_value(u32 x_st, u32 y_st, u32 W, u32 H);

int GpioInputExample(u16 DeviceId, u32 *DataRead);
int GpioInput_Total_calc_Graylevel(u16 DeviceId, u32 *DataReadLW, u32 *DataReadSW);//JACKY2020

void GpioDriverHandler(void *CallBackRef);


/************************** Variable Definitions **************************/

/*
 * The following are declared globally so they are zeroed and so they are
 * easily accessible from a debugger
 */
XGpio GpioOutput; /* The driver instance for GPIO Device configured as O/P */
XGpio GpioInput;  /* The driver instance for GPIO Device configured as I/P */
/************************** Variable Definitions *****************************/

/*
 * The following are declared globally so they are zeroed and so they are
 * easily accessible from a debugger
 */
XGpio Gpio; /* The Instance of the GPIO Driver */

INTC Intc; /* The Instance of the Interrupt Controller Driver */


static u16 GlobalIntrMask; /* GPIO channel mask that is needed by
			    * the Interrupt Handler */

static volatile u32 IntrFlag; /* Interrupt Handler Flag */
//------------------------------------------------------------------------------
#define LSW 100 //% of 640x480
#define SSW 50  //% of 640x480
#define CENTER 0x014000F0

#define LOCK_MONITOR 1
#define DMA_DEVICE_ID 			XPAR_XDMAPS_1_DEVICE_ID
uint32_t g_procedure_started = STOP;


// *****************************************************
// Private data
// *****************************************************

// Subcore instantiations
//static XGpio         vid_mux_sel_gpio_inst;
static XGpioPs		 ps_gpio_inst;
static XGpio         lock_monitor_inst;
static XScuGic		 scugic_inst;
static XScuTimer     scutimer_inst;
static XGpio         NFrameReady_inst;
static XUartPs		 psuart0_inst;
static vid_io_intf_t vid_io_camera_inst;
static vid_io_intf_t vid_io_camera_freeze_inst;
static vid_io_intf_t vid_io_GUI_inst;
//static XVtc          vtd_inst;
//static XV_tpg        tpg_old_inst;
static XV_tpg        tpg_GUI_inst;
static XVprocSs      scaler_camera_inst;
static XVprocSs      scaler_camera_freeze_inst;
static XAxiVdma      vdma_camera_inst;
static XAxiVdma      vdma_camera_freeze_inst;
static XAxiVdma      vdma_GUI_inst;
static XV_Mix_l2	 vid_output_mixer_l2_inst;
static XVtc          vtg_inst_0;
static XVtc          vtg_inst_1;
static XUsbPs		 psusb0_inst;
static XDmaPs		 psdma0_inst;

static XUartPs_Config *g_psuart1_config = 0;
//XVidC_VideoStream VidStream;

// *****************************************************
// Private functions
// *****************************************************

// init_drivers() - Initialize drivers for remaining peripherals
//                  and set them to a known power-on state.
//   - p_periphs_inst             - Pointer to object to work on
//   - vid_mux_sel_gpio_device_id - Device ID for GPIO controlling the output video mux
//   - vtd_device_id              - Device ID for Video Timing Detector
//   - tpg_old_device_id          - Device ID for Test Pattern Generator that drives the old Scaler
//   - tpg_new_device_id          - Device ID for Test Pattern Generator that drives the new VPSS-based Scaler
//   - scaler_old_device_id       - Device ID for Scaler v8.1 instance
//   - scaler_new_device_id       - Device ID for VPSS v1.0 Scaler instance
//   - vtg_device_id_0            - Device ID for Video Timing Generator
//   - vtg_device_id_1            - Device ID for Video Timing Generator
//   - return                     - Function status return value (see above)
static int init_drivers
(
	periphs_t*   p_periphs_inst,
	unsigned int ps_gpio_device_id,
	unsigned int video_lock_device_id,
	unsigned int scugic_device_id,
	unsigned int scutimer_device_id,
	unsigned int NFrameReady_device_id,//JACKY1212
	unsigned int psuart0_device_id,
	//unsigned int vid_mux_sel_gpio_device_id,
	//unsigned int vtd_device_id,
	//unsigned int tpg_old_device_id,
	unsigned int tpg_GUI_device_id,
	//unsigned int scaler_camera_device_id,
	unsigned int YUV422toRGB_device_id,//JACKY XPAR_XVPROCSS_0_DEVICE_ID
	unsigned int scaler_camera_freeze_device_id,
	unsigned int vdma_camera_device_id,
	unsigned int vdma_camera_freeze_device_id,
	//unsigned int vdma_GUI_device_id,
	unsigned int vid_output_mixer_device_id,
	unsigned int vtg_device_id_0,
	unsigned int vtg_device_id_1,
	unsigned int psusb0_device_id

)
{
	// Local variables
	int              status         = 0;
	//XGpio_Config*    p_gpio_cfg;
	XGpioPs_Config*	 p_ps_gpio_cfg;
	XGpio_Config*    p_lock_monitor_cfg;
	XScuGic_Config*  p_scugic_cfg;
	XScuTimer_Config* p_scutimer_cfg;
	XGpio_Config* 	p_NFrameReady_cfg;	//JACKY1212
	XUartPs_Config*	 p_psuart0_cfg;
	//XVtc_Config*     p_vtd_cfg;
	XV_tpg_Config*   p_tpg_GUI_cfg;
	//XVprocSs_Config* p_vpss_camera_cfg;
	XVprocSs_Config* p_vpss_camera_YUV422toRGB_cfg;
	XVprocSs_Config* p_vpss_camera_freeze_cfg;
	XAxiVdma_Config* p_vdma_camera_cfg;
	XAxiVdma_Config* p_vdma_camera_freeze_cfg;
	//XAxiVdma_Config* p_vdma_GUI_cfg;
	XVtc_Config*     p_vtg_cfg_0;
	XVtc_Config*     p_vtg_cfg_1;
	XUsbPs_Config*   p_psusb0_cfg;
	
	// Initialize GPIO drivers
//	xil_printf("Initializing GPIO for output video mux.\n\r");
//	p_gpio_cfg = XGpio_LookupConfig(vid_mux_sel_gpio_device_id);
//	if (p_gpio_cfg == NULL)
//	{
//		xil_printf("ERROR! Failed to find GPIO for output video mux.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
//
//	status = XGpio_Initialize(p_periphs_inst->p_vid_mux_sel_gpio_inst, vid_mux_sel_gpio_device_id);
//	if (status != XST_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to initialize the GPIO for output video mux.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}

	// Initialize VTD drivers
//	xil_printf("Initializing VTD.\n\r");
//	p_vtd_cfg = XVtc_LookupConfig(vtd_device_id);
//	if (p_vtd_cfg == NULL)
//	{
//		xil_printf("ERROR! Failed to find VTD.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
//
//	if (periphs_get_fmc_status(p_periphs_inst)) // This function will hang if FMC card is not present. This is because the VTD needs an input video clock to access registers and this function asserts soft reset which causes a hang on AXI Lite interface.
//	{
//		status = XVtc_CfgInitialize(p_periphs_inst->p_vtd_inst, p_vtd_cfg, p_vtd_cfg->BaseAddress);
//		if (status != XST_SUCCESS)
//		{
//			xil_printf("ERROR! Failed to initialize the VTD.\n\r");
//			return PERIPHS_ERROR_UNKNOWN;
//		}
//	}


	xil_printf("\n\rdavid1101: %s:%s(%d) ST\r\n", __FILE__, __func__, __LINE__);

	// Initialize PS GPIO drivers
	xil_printf("Initializing PS GPIO.\n\r");
	p_ps_gpio_cfg = XGpioPs_LookupConfig(ps_gpio_device_id);
	if (p_ps_gpio_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find PS GPIO.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	status = XGpioPs_CfgInitialize(p_periphs_inst->p_ps_gpio_inst, p_ps_gpio_cfg, p_ps_gpio_cfg->BaseAddr);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize the PS GPIO.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	// Initialize Video lock monitor (GPIO) drivers
	xil_printf("Initializing video lock monitor GPIO. video_lock_device_id = %d\n\r", video_lock_device_id);
	p_lock_monitor_cfg = XGpio_LookupConfig(video_lock_device_id);
	if (p_lock_monitor_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find video lock monitor.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	status = XGpio_Initialize(p_periphs_inst->p_lock_monitor_inst, video_lock_device_id);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize the video lock monitor.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	// Initialize the interrupt controller
	xil_printf("=========================XScuGic_LookupConfig DeviceId=%d\n\r", scugic_device_id);
	p_scugic_cfg = XScuGic_LookupConfig(scugic_device_id);
	if (NULL == p_scugic_cfg) {
		xil_printf("ERROR! Failed to find scugic.\n\r");
		return XST_FAILURE;
	}

	status = XScuGic_CfgInitialize(p_periphs_inst->p_scugic_inst, p_scugic_cfg, p_scugic_cfg->CpuBaseAddress);
	if (status != XST_SUCCESS) {
		xil_printf("ERROR! Failed to initialize scugic.\n\r");
		return XST_FAILURE;
	}

	// Initialize the CPU private timer
	p_scutimer_cfg = XScuTimer_LookupConfig(scutimer_device_id);
	if (NULL == p_scutimer_cfg) {
		xil_printf("ERROR! Failed to find scutimer.\n\r");
		return XST_FAILURE;
	}

	xil_printf("david1106: %s:%s(%d) XScuTimer id = %d base = 0x%08x\r\n", __FILE__, __func__, __LINE__, scutimer_device_id, p_scutimer_cfg->BaseAddr);

	status = XScuTimer_CfgInitialize(p_periphs_inst->p_scutimer_inst, p_scutimer_cfg, p_scutimer_cfg->BaseAddr);
	if (status != XST_SUCCESS) {
		xil_printf("ERROR! Failed to initialize scutimer.\n\r");
		return XST_FAILURE;
	}

	//Initialize the AXI_GPIO of p_NFrameReady_cfg
	/*xil_printf("=========================XScuGic_LookupConfig DeviceId=%d\n\r", XPAR_PS7_SCUGIC_0_DEVICE_ID);
	p_NFrameReady_cfg = XScuGic_LookupConfig(XPAR_PS7_SCUGIC_0_DEVICE_ID);
	if (NULL == p_NFrameReady_cfg) {
		return XST_FAILURE;
	}

	status = XScuGic_CfgInitialize(p_periphs_inst->NFrameReady_inst, p_NFrameReady_cfg,
				       GicConfig->CpuBaseAddress);
	xil_printf("=====XScuGic_CfgInitialize: GicConfig=%8x, GicConfig->CpuBaseAddress=%8x=====\n\r", GicConfig, GicConfig->CpuBaseAddress);
	if (status != XST_SUCCESS) {
		return XST_FAILURE;
	}*/
    {
        //-------------------------------------------JACKY121212--------------------------------------------
    	   #define GPIO_CHANNEL1 1
    	   #define GPIO_CHANNEL2 2
    	   static XGpio video_path_camera_in_CDR_VIdeo_In_AXI4_rdy_CDR_Registers_axi_gpio_NFrameReady_Gpio;
    	//-------------------------------------------------------------------------------------------------
    	   status = XGpio_Initialize(&video_path_camera_in_CDR_VIdeo_In_AXI4_rdy_CDR_Registers_axi_gpio_NFrameReady_Gpio, XPAR_VIDEO_PATH_CAMERA_IN_CDR_VIDEO_IN_AXI4_RDY_CDR_REGISTERS_AXI_GPIO_NFRAMESREADY_DEVICE_ID);
			if (status != XST_SUCCESS) {
				return XST_FAILURE;
			}

			//Bock scutimer_IntrHandler JACKY1126
			status = GpioSetupIntrSystem(&scugic_inst, &video_path_camera_in_CDR_VIdeo_In_AXI4_rdy_CDR_Registers_axi_gpio_NFrameReady_Gpio, XPAR_VIDEO_PATH_CAMERA_IN_CDR_VIDEO_IN_AXI4_RDY_CDR_REGISTERS_AXI_GPIO_NFRAMESREADY_DEVICE_ID,
					XPAR_FABRIC_VIDEO_PATH_CAMERA_IN_CDR_VIDEO_IN_AXI4_RDY_CDR_REGISTERS_AXI_GPIO_NFRAMESREADY_IP2INTC_IRPT_INTR, GPIO_CHANNEL1);
			if (status != XST_SUCCESS) {
				return XST_FAILURE;
			}
    }


	// Initialize the UART driver so that it's ready to use
	p_psuart0_cfg = XUartPs_LookupConfig(psuart0_device_id);
	if (NULL == p_psuart0_cfg) {
		xil_printf("ERROR! Failed to find psuart0.\n\r");
		return XST_FAILURE;
	}

	status = XUartPs_CfgInitialize(p_periphs_inst->p_psuart0_inst, p_psuart0_cfg,p_psuart0_cfg->BaseAddress);
	if (status != XST_SUCCESS) {
		xil_printf("ERROR! Failed to initialize psuart0.\n\r");
		return XST_FAILURE;
	}

	// Get psuart1 config
	g_psuart1_config = XUartPs_LookupConfig(XPAR_PS7_UART_1_DEVICE_ID);

	if (NULL == g_psuart1_config) {
		xil_printf("ERROR! Failed to find psuart0.\n\r");
		return XST_FAILURE;
	}

	// Initialize GUI TPG drivers
	xil_printf("Initializing GUI TPG.\n\r");
	p_tpg_GUI_cfg = XV_tpg_LookupConfig(tpg_GUI_device_id);
	if (p_tpg_GUI_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find GUI TPG.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	status = XV_tpg_CfgInitialize(p_periphs_inst->p_tpg_GUI_inst, p_tpg_GUI_cfg, p_tpg_GUI_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize the GUI TPG.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	// Initialize Scaler drivers
//	xil_printf("Initializing Camera Scaler.\n\r");
//	p_vpss_camera_cfg = XVprocSs_LookupConfig(scaler_camera_device_id);
//	if (p_vpss_camera_cfg == NULL)
//	{
//		xil_printf("ERROR! Failed to find Camera scaler.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
//	status = XVprocSs_CfgInitialize(p_periphs_inst->p_scaler_camera_inst, p_vpss_camera_cfg, p_vpss_camera_cfg->BaseAddress);
//	if (status != XST_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to initialize Camera scaler.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
	//---------------------------------------------------------JACKYSTART-------------------------------------------------------------------------------------
	YUV422toRGB_device_id=1;
	xil_printf("Initializing Camera CSC VPSS. YUV422toRGB_device_id = %d\n\r", YUV422toRGB_device_id);
	p_vpss_camera_YUV422toRGB_cfg = XVprocSs_LookupConfig(YUV422toRGB_device_id);
	if (p_vpss_camera_YUV422toRGB_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find Camera CSC VPSS.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("Initializing Camera CSC VPSS.base_addr = 0x%08x\n\r", p_vpss_camera_YUV422toRGB_cfg->BaseAddress);
	status = XVprocSs_CfgInitialize(p_periphs_inst->p_scaler_camera_inst, p_vpss_camera_YUV422toRGB_cfg, p_vpss_camera_YUV422toRGB_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize Camera CSC VPSS.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	//---------------------------------------------------------JACKYEND-------------------------------------------------------------------------------------

	xil_printf("Initializing Camera Freeze Scaler.scaler_camera_freeze_device_id = %d\n\r", scaler_camera_freeze_device_id);
	p_vpss_camera_freeze_cfg = XVprocSs_LookupConfig(scaler_camera_freeze_device_id);
	if (p_vpss_camera_freeze_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find Camera Freeze scaler.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("Initializing Camera Freeze Scaler.base_addr = 0x%08x\n\r", p_vpss_camera_freeze_cfg->BaseAddress);
	status = XVprocSs_CfgInitialize(p_periphs_inst->p_scaler_camera_freeze_inst, p_vpss_camera_freeze_cfg, p_vpss_camera_freeze_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize Camera Freeze scaler.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	// Initialize VDMA drivers
	xil_printf("\n\rInitializing Camera VDMA. id = %d\n\r", vdma_camera_device_id);
	p_vdma_camera_cfg = XAxiVdma_LookupConfig(vdma_camera_device_id);
	if (p_vdma_camera_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find Camera VDMA.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	status = XAxiVdma_CfgInitialize(p_periphs_inst->p_vdma_camera_inst, p_vdma_camera_cfg, p_vdma_camera_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize the Camera VDMA.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	xil_printf("\n\rInitializing Camera Freeze VDMA. id = %d\n\r", vdma_camera_freeze_device_id);
	p_vdma_camera_freeze_cfg = XAxiVdma_LookupConfig(vdma_camera_freeze_device_id);
	if (p_vdma_camera_freeze_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find Camera Freeze VDMA.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	status = XAxiVdma_CfgInitialize(p_periphs_inst->p_vdma_camera_freeze_inst, p_vdma_camera_freeze_cfg, p_vdma_camera_freeze_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize the Camera Freeze VDMA.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("\n\r");
	
//	xil_printf("Initializing GUI VDMA.\n\r");
//	p_vdma_GUI_cfg = XAxiVdma_LookupConfig(vdma_GUI_device_id);
//	if (p_vdma_GUI_cfg == NULL)
//	{
//		xil_printf("ERROR! Failed to find GUI VDMA.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
//	status = XAxiVdma_CfgInitialize(p_periphs_inst->p_vdma_GUI_inst, p_vdma_GUI_cfg, p_vdma_GUI_cfg->BaseAddress);
//	if (status != XST_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to initialize the GUI VDMA.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
	
	// Initialize Video Mixer driver
	xil_printf("\n\rdavid1023: %s:%s(%d) ST Initializing Video Mixer.\r\n",__FILE__,__func__,__LINE__);
	xil_printf("Initializing Video Mixer. vid_output_mixer_device_id = %d\n\r", vid_output_mixer_device_id);
	status  = XVMix_Initialize(p_periphs_inst->p_vid_output_mixer_l2_inst, vid_output_mixer_device_id);
	if(status != XST_SUCCESS) {
	  xil_printf("ERR:: Mixer device not found\r\n");
	  return(XST_FAILURE);
	}
	xil_printf("Initializing Video Mixer. OK\n\r");
	
	xil_printf("david1105: %s:%s(%d) NumLayers = %d\r\n", __FILE__, __func__, __LINE__, p_periphs_inst->p_vid_output_mixer_l2_inst->Mix.Config.NumLayers);

	xil_printf("\n\r\n\rdavid1023: %s:%s(%d) ST Initializing VTG_0.\r\n",__FILE__,__func__,__LINE__);
	// Initialize VTG drivers Device 0
	xil_printf("Initializing VTG_0. vtg_device_id_0 = %d, for TFP410\n\r", vtg_device_id_0);
	p_vtg_cfg_0 = XVtc_LookupConfig(vtg_device_id_0);
	if (p_vtg_cfg_0 == NULL)
	{
		xil_printf("ERROR! Failed to find VTG_0.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	status = XVtc_CfgInitialize(p_periphs_inst->p_vtg_inst_0, p_vtg_cfg_0, p_vtg_cfg_0->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize the VTG_0.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	xil_printf("\n\rdavid1023: %s:%s(%d) ST Initializing VTG_1.\r\n",__FILE__,__func__,__LINE__);
	// Initialize VTG drivers Device 1
	xil_printf("Initializing VTG_1. vtg_device_id_1 = %d, for CH7038\n\r", vtg_device_id_1);
	p_vtg_cfg_1 = XVtc_LookupConfig(vtg_device_id_1);
	if (p_vtg_cfg_1 == NULL)
	{
		xil_printf("ERROR! Failed to find VTG_1.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("david1029: %s:%s(%d) BaseAddr = 0x%08x\r\n", __FILE__, __func__, __LINE__, p_vtg_cfg_1->BaseAddress);
	status = XVtc_CfgInitialize(p_periphs_inst->p_vtg_inst_1, p_vtg_cfg_1, p_vtg_cfg_1->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize the VTG_1.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	p_psusb0_cfg = XUsbPs_LookupConfig(psusb0_device_id);
	if (p_psusb0_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find PSUSB0.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	status = XUsbPs_CfgInitialize(p_periphs_inst->p_psusb0_inst, p_psusb0_cfg, p_psusb0_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize PSUSB0.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	xil_printf("david1109: %s:%s(%d) ST\r\n", __FILE__, __func__, __LINE__);

	/*
	 * Initialize the DMA Driver
	 */
	XDmaPs_Config *DmaCfg;
	XDmaPs *DmaInst = p_periphs_inst->p_pdma0_inst;
	DmaCfg = XDmaPs_LookupConfig(DMA_DEVICE_ID);
	if (DmaCfg == NULL) {
		xil_printf("david1109: %s:%s(%d) ST\r\n", __FILE__, __func__, __LINE__);
		return XST_FAILURE;
	}
	xil_printf("david1109: %s:%s(%d) ST\r\n", __FILE__, __func__, __LINE__);
	status = XDmaPs_CfgInitialize(DmaInst,
				   DmaCfg,
				   DmaCfg->BaseAddress);
	if (status != XST_SUCCESS) {
		xil_printf("david1109: %s:%s(%d) ST\r\n", __FILE__, __func__, __LINE__);
		return XST_FAILURE;
	}
	xil_printf("DMA DeviceId = %d, Base = 0x%08x\n\r", DMA_DEVICE_ID, DmaCfg->BaseAddress);

	/*
	 * Setup the interrupt system.
	 */
	status = SetupInterruptSystem(p_periphs_inst->p_scugic_inst, DmaInst);
	if (status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	xil_printf("\n\rdavid1101: %s:%s(%d) SP\r\n\n\r", __FILE__, __func__, __LINE__);
	return PERIPHS_SUCCESS;
}



// *****************************************************
// Public functions
// *****************************************************
int periphs_init
(
	periphs_t*   p_periphs_inst,
	unsigned int ps_gpio_device_id,
	unsigned int video_lock_device_id,
	unsigned int scugic_device_id,
	unsigned int scutimer_device_id,
	unsigned int NFrameReady_device_id,//JACKY1212
	unsigned int psuart0_device_id,
	//unsigned int vid_mux_sel_gpio_device_id,
	//unsigned int fmc_imageon_iic_base_addr,
	//unsigned int si570_iic_device_id,
	//unsigned int vtd_device_id,
	unsigned int tpg_GUI_device_id,
	//unsigned int scaler_camera_device_id,
	unsigned int YUV422toRGB_device_id,//JACKY XPAR_XVPROCSS_0_DEVICE_ID
	unsigned int scaler_camera_freeze_device_id,
	unsigned int vdma_camera_device_id,
	unsigned int vdma_camera_freeze_device_id,
	//unsigned int vdma_GUI_device_id,
	unsigned int vid_output_mixer_device_id,
	unsigned int vtg_device_id_0,
	unsigned int vtg_device_id_1,
	unsigned int psusb0_device_id,
	unsigned int fb_camera_start_addr,
	unsigned int fb_camera_freeze_start_addr,
	unsigned int fb_GUI_start_addr
)
{
	// Local variables
	int status = 0;
	u32 IntrMask = 0;
	//u32 BadByteCount = 0;
	
	// Attach subcore instances to object
	//p_periphs_inst->p_vid_mux_sel_gpio_inst = &vid_mux_sel_gpio_inst;
	//p_periphs_inst->p_vtd_inst              	= &vtd_inst;
	p_periphs_inst->p_ps_gpio_inst				= &ps_gpio_inst;
	p_periphs_inst->p_lock_monitor_inst			= &lock_monitor_inst;
	p_periphs_inst->p_scugic_inst				= &scugic_inst;
	p_periphs_inst->p_scutimer_inst				= &scutimer_inst;
	p_periphs_inst->p_NFrameReady_inst			= &NFrameReady_inst;//	JACKY1212
	p_periphs_inst->p_psuart0_inst				= &psuart0_inst;
	p_periphs_inst->p_tpg_GUI_inst          	= &tpg_GUI_inst;
	p_periphs_inst->p_scaler_camera_inst       	= &scaler_camera_inst;
	p_periphs_inst->p_scaler_camera_freeze_inst	= &scaler_camera_freeze_inst;
	p_periphs_inst->p_vdma_camera_inst         	= &vdma_camera_inst;
	p_periphs_inst->p_vdma_camera_freeze_inst  	= &vdma_camera_freeze_inst;
	p_periphs_inst->p_vdma_GUI_inst  			= &vdma_GUI_inst;
	p_periphs_inst->p_vid_output_mixer_l2_inst	= &vid_output_mixer_l2_inst;
	p_periphs_inst->p_vtg_inst_0              	= &vtg_inst_0;
	p_periphs_inst->p_vtg_inst_1              	= &vtg_inst_1;
	p_periphs_inst->p_psusb0_inst              	= &psusb0_inst;

	p_periphs_inst->p_pdma0_inst				= &psdma0_inst;

	// Store VDMA framebuffer addresses
	p_periphs_inst->fb_camera_start_addr  		= fb_camera_start_addr;
	p_periphs_inst->fb_camera_freeze_start_addr	= fb_camera_freeze_start_addr;
	p_periphs_inst->fb_GUI_start_addr			= fb_GUI_start_addr;

	// Video I/O
	p_periphs_inst->p_vid_io_camera_inst     	= &vid_io_camera_inst;
	p_periphs_inst->p_vid_io_camera_freeze_inst	= &vid_io_camera_freeze_inst;
	p_periphs_inst->p_vid_io_GUI_inst 			= &vid_io_GUI_inst;
	
	// Enable GUI TPG by default
	p_periphs_inst->bypass_GUI_tpg = PERIPHS_SEL_ENABLE_TPG;

	// VDMA default flag set to not park
	p_periphs_inst->enable_camera_freeze_vdma = PERIPHS_SEL_DISABLE_PARK;

	// Initialize Video Input/Output interface (External)
	xil_printf("Initializing Video Input/Output interface.\n\r");
	//status = vid_io_intf_init(p_periphs_inst->p_vid_io_intf_inst, fmc_imageon_iic_base_addr, si570_iic_device_id);
	status = vid_io_intf_init(p_periphs_inst->p_vid_io_camera_inst,
								p_periphs_inst->p_vid_io_camera_freeze_inst,
								p_periphs_inst->p_vid_io_GUI_inst);
	
	// Initialize Peripheral drivers, once only.
	xil_printf("Initializing peripheral drivers.\n\r");
	status = init_drivers
	(
		p_periphs_inst,
		ps_gpio_device_id,
		video_lock_device_id,
		scugic_device_id,
		scutimer_device_id,
		NFrameReady_device_id,//JACKY1212
		psuart0_device_id,
		//vid_mux_sel_gpio_device_id,
		//vtd_device_id,
		//tpg_old_device_id,
		tpg_GUI_device_id,
		//scaler_camera_device_id,
		YUV422toRGB_device_id,
		scaler_camera_freeze_device_id,
		vdma_camera_device_id,
		vdma_camera_freeze_device_id,
		//vdma_GUI_device_id,
		vid_output_mixer_device_id,
		vtg_device_id_0,
		vtg_device_id_1,
		psusb0_device_id

	);
	if (status != 0)
	{
		xil_printf("ERROR! Failed to initialize remaining peripheral drivers.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	/*
	xil_printf("david1029: %s:%s(%d) ST debug\r\n", __FILE__, __func__, __LINE__);
	//debug message
	read_vdma_regs(p_periphs_inst->p_vdma_camera_inst);
	*/

	// Video Path Config
	xil_printf("\n\rdavid1023: %s:%s(%d) Video Path Config ST\n\r\r\n",__FILE__,__func__,__LINE__);

	xil_printf("Bringing up input pipeline.\n\r");
	periphs_bring_up_input_pipeline(p_periphs_inst);

	xil_printf("Bringing up output pipeline. vid = VIDEO_RESOLUTION_1080P = %d fb_GUI_start_addr = 0x%08x\n\r", VIDEO_RESOLUTION_1080P, fb_GUI_start_addr);	//VIDEO_RESOLUTION_1080P = 7
	periphs_bring_up_output_pipeline(p_periphs_inst, VIDEO_RESOLUTION_1080P, fb_GUI_start_addr);

	xil_printf("\n\rdavid1023: %s:%s(%d) call periphs_configure_gpio_pins\r\n",__FILE__,__func__,__LINE__);
	// Control Path Config
	periphs_configure_gpio_pins(p_periphs_inst); // Set up GPIO Pins

	// Set up Exception Handler
	//Xil_ExceptionInit(); // Obsolete, used to maintain backward compatibility

	/*
	 * Connect the interrupt controller interrupt handler to the hardware
	 * interrupt handling logic in the processor.
	 */

	xil_printf("david0423: %s:%s(%d) ST\r\n", __FILE__, __func__, __LINE__);
	Xil_ExceptionRegisterHandler(XIL_EXCEPTION_ID_INT,
				(Xil_ExceptionHandler)XScuGic_InterruptHandler,
				p_periphs_inst->p_scugic_inst);

	// SCUTIMER - Connect the device driver handler that will be called when an interrupt for the device occurs
	xil_printf("david1206: %s:%s(%d) call XScuGic_Connect with Int_Id = XPAR_SCUTIMER_INTR = %lud\r\n", __FILE__, __func__, __LINE__, XPAR_SCUTIMER_INTR);
	status = XScuGic_Connect(p_periphs_inst->p_scugic_inst, XPAR_SCUTIMER_INTR,
				(Xil_ExceptionHandler)scutimer_IntrHandler, p_periphs_inst->p_scutimer_inst);
	if (status != XST_SUCCESS) {
		xil_printf("failed to connect scutimer\r\n");
		return status;
	}

	// Reset/Stop scutimer
	XScuTimer_Stop(p_periphs_inst->p_scutimer_inst);
	XScuTimer_DisableInterrupt(p_periphs_inst->p_scutimer_inst);
	XScuTimer_ClearInterruptStatus(p_periphs_inst->p_scutimer_inst);
	// Load scutimer values
	xil_printf("david0424: %s:%s(%d) XScuTimer_LoadTimer COUNTS_PER_MILLI_SECOND = %d\r\n", __FILE__, __func__, __LINE__, COUNTS_PER_MILLI_SECOND);
	xil_printf("david0507: %s:%s(%d) XScuTimer_LoadTimer base = 0x%08x\r\n", __FILE__, __func__, __LINE__, p_periphs_inst->p_scutimer_inst->Config.BaseAddr);
	XScuTimer_LoadTimer(p_periphs_inst->p_scutimer_inst, COUNTS_PER_MILLI_SECOND);
	XScuTimer_RestartTimer(p_periphs_inst->p_scutimer_inst);
	XScuTimer_SetPrescaler(p_periphs_inst->p_scutimer_inst, 0);
	XScuTimer_EnableAutoReload(p_periphs_inst->p_scutimer_inst);

	XScuTimer_Start(p_periphs_inst->p_scutimer_inst);
	// Enable the scugic interrupt for the scutimer.
	XScuGic_Enable(p_periphs_inst->p_scugic_inst, XPAR_SCUTIMER_INTR);
	XScuTimer_EnableInterrupt(p_periphs_inst->p_scutimer_inst);

	// psuart0 - Connect the device driver handler that will be called when an interrupt for the device occurs
	// Print UART settings
	xil_printf("david1206: %s:%s(%d) call XScuGic_Connect with Int_Id = XPAR_XUARTPS_0_INTR = %d\r\n", __FILE__, __func__, __LINE__, XPAR_XUARTPS_0_INTR);
	status = XScuGic_Connect(p_periphs_inst->p_scugic_inst, XPAR_XUARTPS_0_INTR,
				(Xil_ExceptionHandler)XUartPs_InterruptHandler, p_periphs_inst->p_psuart0_inst);
	if (status != XST_SUCCESS) {
		xil_printf("failed to connect psuart0\r\n");
		return status;
	}

	// Setup the handler for PSUART0
	XUartPs_SetHandler(p_periphs_inst->p_psuart0_inst, (XUartPs_Handler)psuart0_IntrHandler, p_periphs_inst->p_psuart0_inst);

	/*
	 * Enable the interrupt of the UART so interrupts will occur
	 */
	IntrMask =
		XUARTPS_IXR_TOUT | XUARTPS_IXR_PARITY | XUARTPS_IXR_FRAMING |
		XUARTPS_IXR_OVER | XUARTPS_IXR_TXEMPTY | XUARTPS_IXR_RXFULL |
		XUARTPS_IXR_RXOVR;

	if (p_periphs_inst->p_psuart0_inst->Platform == XPLAT_ZYNQ_ULTRA_MP) {
		IntrMask |= XUARTPS_IXR_RBRK;
	}
	XUartPs_SetInterruptMask(p_periphs_inst->p_psuart0_inst, IntrMask);
	XUartPs_SetBaudRate(p_periphs_inst->p_psuart0_inst, XUARTPS_DFT_BAUDRATE);
	/*
	 * Set the receiver timeout. If it is not set, and the last few bytes
	 * of data do not trigger the over-water or full interrupt, the bytes
	 * will not be received. By default it is disabled.
	 *
	 * The setting of 8 will timeout after 8 x 4 = 32 character times.
	 * Increase the time out value if baud rate is high, decrease it if
	 * baud rate is low.
	 */
	XUartPs_SetRecvTimeout(p_periphs_inst->p_psuart0_inst, 8);

//	xil_printf("psuart0 baudrate: %d\r\n", p_periphs_inst->p_psuart0_inst->BaudRate);
//	xil_printf("psuart0 callback: 0x%x\r\n", p_periphs_inst->p_psuart0_inst->CallBackRef);
//	xil_printf("psuart0 clock: %d\r\n", p_periphs_inst->p_psuart0_inst->InputClockHz);
//	xil_printf("psuart0 ready: %d\r\n", p_periphs_inst->p_psuart0_inst->IsReady);
//	xil_printf("psuart0 platform: %d\r\n", p_periphs_inst->p_psuart0_inst->Platform);
//	xil_printf("psuart0 rxbs_errot: %d\r\n", p_periphs_inst->p_psuart0_inst->is_rxbs_error);

	/* Enable the interrupt for the device */
	XScuGic_Enable(p_periphs_inst->p_scugic_inst, XPAR_XUARTPS_0_INTR);

	//XUartPs_SetOperMode(p_periphs_inst->p_psuart0_inst, XUARTPS_OPER_MODE_LOCAL_LOOP);
//	XUartPs_SetOperMode(p_periphs_inst->p_psuart0_inst, XUARTPS_OPER_MODE_NORMAL);

	/* Set the UART in Normal Mode */
	XUartPs_SetOperMode(p_periphs_inst->p_psuart0_inst, XUARTPS_OPER_MODE_NORMAL);


//	/* If any bytes were not correct, return an error */
//	if (BadByteCount != 0) {
//		xil_printf("UART NG\r\n");
//		return XST_FAILURE;
//	}
//
//	xil_printf("UART OK, badbytecount = 0, test pass\r\n");

	// GPIOPS - Connect the device driver handler that will be called when an interrupt for the device occurs
	// The handler defined above performs the specific interrupt processing for the device.
	xil_printf("david1206: %s:%s(%d) call XScuGic_Connect with Int_Id = XPAR_XGPIOPS_0_INTR = %d\r\n", __FILE__, __func__, __LINE__, XPAR_XGPIOPS_0_INTR);
	status = XScuGic_Connect(p_periphs_inst->p_scugic_inst, XPAR_XGPIOPS_0_INTR,
				(Xil_ExceptionHandler)XGpioPs_IntrHandler, p_periphs_inst->p_ps_gpio_inst);
	if (status != XST_SUCCESS) {
		xil_printf("failed to connect GPIOPS\r\n");
		return status;
	}

	// Set up PS GPIO Pin
	// Enable active high interrupts for input pins in bank 2.
	XGpioPs_SetIntrType(p_periphs_inst->p_ps_gpio_inst, XGPIOPS_BANK2, 0xffffffff, 0xffffffff, 0x00);

	// Set the handler for gpio interrupts. */
	XGpioPs_SetCallbackHandler(p_periphs_inst->p_ps_gpio_inst, (void *)p_periphs_inst->p_ps_gpio_inst, ps_gpio_IntrHandler);

	// Enable the GPIO interrupts of Bank 2. */
	XGpioPs_IntrEnable(p_periphs_inst->p_ps_gpio_inst, XGPIOPS_BANK2, INPUT_INTERRUPT_ALL); // TODO

	//Only used for edge sensitive Interrupts
	//XScuGic_SetPriorityTriggerType(p_periphs_inst->p_scugic_inst, XPAR_XGPIOPS_0_INTR, 0xa0, 3);

	// Enable the interrupt for the PS GPIO device.
	XScuGic_Enable(p_periphs_inst->p_scugic_inst, XPAR_XGPIOPS_0_INTR);




	// Lock Monitor - Connect the device driver handler that will be called when an interrupt for the device occurs
	// The handler defined above performs the specific interrupt processing for the device.
	// Use XPS define due to bug in generated x_parameter.h

	//xil_printf("david1206: %s:%s(%d) call XScuGic_Connect with Int_Id = lock_monitor = %d\r\n", __FILE__, __func__, __LINE__, XPAR_FABRIC_VIDEO_PATH_VIDEO_OUT_VIDEO_LOCK_MONITOR_VS_EQUAL_VSYNC_IP2INTC_IRPT_INTR);

	/*
	status = XScuGic_Connect(p_periphs_inst->p_scugic_inst, XPAR_FABRIC_VIDEO_PATH_VIDEO_OUT_VIDEO_LOCK_MONITOR_VS_EQUAL_VSYNC_IP2INTC_IRPT_INTR,
				(Xil_ExceptionHandler)lock_monitor_IntrHandler, p_periphs_inst->p_lock_monitor_inst);
	if (status != XST_SUCCESS)
	{
		xil_printf("failed to connect lock monitor\r\n");
		return status;
	}
	*/

	/*
	 * Enable the GPIO channel interrupts so that lock monitor can be
	 * detected and enable interrupts for the GPIO device
	 */

	xil_printf("david1206: %s:%s(%d) ST XGPIO_IR_CH2_MASK = 0x%x = %d\r\n", __FILE__, __func__, __LINE__, XGPIO_IR_CH2_MASK, XGPIO_IR_CH2_MASK);

	XGpio_InterruptEnable(p_periphs_inst->p_lock_monitor_inst, XGPIO_IR_CH2_MASK);

	XGpio_InterruptGlobalEnable(p_periphs_inst->p_lock_monitor_inst);

	//Only used for edge sensitive Interrupts
	XScuGic_SetPriorityTriggerType(p_periphs_inst->p_scugic_inst, XPS_FPGA6_INT_ID, 0x98, 1);

	// Enable the interrupt for the lock monitor device.
	XScuGic_Enable(p_periphs_inst->p_scugic_inst, XPS_FPGA6_INT_ID);

	// Connect USB to SCUGIC
	// Remaining parts are in TinyUSB HAL
	xil_printf("david1206: %s:%s(%d) call XScuGic_Connect with Int_Id = XPAR_XUSBPS_0_INTR = %d\r\n", __FILE__, __func__, __LINE__, XPAR_XUSBPS_0_INTR);
	status = XScuGic_Connect(p_periphs_inst->p_scugic_inst, XPAR_XUSBPS_0_INTR,
				//(Xil_ExceptionHandler)XUsbPs_IntrHandler,
				(Xil_ExceptionHandler)psusb0_IntrHandler,
				(void *)p_periphs_inst->p_psusb0_inst);
	if (status != XST_SUCCESS) {
		xil_printf("psusb0 connect to sgugic failed\r\n");
		return status;
	}

	/* Enable System wide interrupts in the Processor. */
	//Xil_ExceptionEnableMask(XIL_EXCEPTION_IRQ);
	Xil_ExceptionEnable();

	//debug message
	xil_printf("david1102: %s:%s(%d)  call read_vdma_regs\r\n", __FILE__, __func__, __LINE__);
	read_vdma_regs(p_periphs_inst->p_vdma_camera_inst);

	xil_printf("david1102: %s:%s(%d) SP\n\r\r\n", __FILE__, __func__, __LINE__);

	return PERIPHS_SUCCESS;
}

int periphs_get_fmc_status
(
	periphs_t* p_periphs_inst
)
{
	xil_printf("david1023: %s:%s(%d) ST xxxxxxxxxxxxxx\r\n",__FILE__,__func__,__LINE__);
	return vid_io_intf_get_fmc_status(p_periphs_inst->p_vid_io_camera_inst);
}

//int periphs_detect_input_fsize
//(
//	periphs_t* p_periphs_inst
//)
//{
//	// Local variables
//	int status = 0;
//
//	if (!p_periphs_inst->p_vid_io_camera_inst->fmc_imageon_is_present)
//	{
//		xil_printf("ERROR! FMC card is not present so we can't detect an incoming frame size.\n\r");
//		return PERIPHS_ERROR_NO_FMC_CARD;
//	}
//
//	// Put VTD in reset to hold off partial frames
//	//vtiming_det_stop(p_periphs_inst->p_vtd_inst);
//
//	// Detect input frame size from Video Input/Output interface
//	vid_io_intf_detect_input_fsize(p_periphs_inst->p_vid_io_camera_inst);
//
//	// Update scaler input frame size
////	status = scaler_old_set_input_size
////	(
////		p_periphs_inst->p_scaler_old_inst,
////		p_periphs_inst->p_vid_io_intf_inst->p_input_timing_inst->HActiveVideo,
////		p_periphs_inst->p_vid_io_intf_inst->p_input_timing_inst->VActiveVideo,
////		0 // Print configuration
////	);
////	if (status != SCALER_OLD_SUCCESS)
////	{
////		xil_printf("ERROR! Failed to set input size on the old scaler.\n\r");
////		return PERIPHS_ERROR_UNKNOWN;
////	}
//
//	// Update VPSS input frame size
//	status = scaler_new_set_size
//	(
//		p_periphs_inst->p_scaler_camera_inst,
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo,
//		1 // Print configuration
//	);
//	if (status != SCALER_NEW_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to set input size on the new VPSS-based scaler.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
//
//	// TPG gets reset, so re-configure it
////	test_pattern_gen_run
////	(
////		p_periphs_inst->p_tpg_old_inst,
////		p_periphs_inst->p_vid_io_intf_inst->p_input_timing_inst->HActiveVideo,
////		p_periphs_inst->p_vid_io_intf_inst->p_input_timing_inst->VActiveVideo,
////		p_periphs_inst->bypass_tpg,
////		1, // Box is blue for TPG on old scaler datapath
////		0  // print regs
////	);
//
////	test_pattern_gen_run
////	(
////		p_periphs_inst->p_tpg_new_inst,
////		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
////		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
////		p_periphs_inst->bypass_tpg,
////		0, // Box is red for TPG on new VPSS scaler datapath
////		0  // print regs
////	);
//
//	// Enable VTD to start letting video in
//	//vtiming_det_run(p_periphs_inst->p_vtd_inst);
//
//	return PERIPHS_SUCCESS;
//}

//int periphs_set_fsize
//(
//	XVprocSs*   p_scaler_inst,
//	vid_io_intf_t*  p_vid_io_inst
//)
//{
//	// Local variables
//	int           status = 0;
//	//vres_timing_t vres_timing;
//
//	// Look up timing info from ID
//	//vres_get_timing(new_input_timing, &vres_timing);
//
//	// Update scaler input frame size
//
//	// Update VPSS input frame size
//	status = scaler_new_set_size
//	(
//		p_scaler_inst,
//		p_vid_io_inst->p_input_timing_inst->HActiveVideo,
//		p_vid_io_inst->p_input_timing_inst->VActiveVideo,
//		p_vid_io_inst->p_output_timing_inst->HActiveVideo,
//		p_vid_io_inst->p_output_timing_inst->VActiveVideo,
//		1 // Print configuration
//	);
//
//	if (status != SCALER_NEW_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to set input size on the new VPSS-based scaler.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
//
//	return PERIPHS_SUCCESS;
//}

//int periphs_update_output_fsize
//(
//	periphs_t*   p_periphs_inst,
//	unsigned int new_output_timing
//)
//{
//	// Local variables
//	int status = 0;
//
//	// Put VTD in reset to hold off partial frames
////	if (periphs_get_fmc_status(p_periphs_inst))
////	{
////		vtiming_det_stop(p_periphs_inst->p_vtd_inst);
////	}
//
//	// Set output frame size for Video Output interface
//	vid_io_intf_update_output_fsize(p_periphs_inst->p_vid_io_GUI_inst, new_output_timing);
//
//	// Set VTG_0 output timing
//	vtiming_gen_run(p_periphs_inst->p_vtg_inst_0, new_output_timing, 0);
//
//	// Set VTG_1 output timing
//	vtiming_gen_run(p_periphs_inst->p_vtg_inst_1, new_output_timing, 0);
//
//	// Set VDMA frame size
//	// Set up Camera Frame buffer
//	xil_printf("Setting up Camera frame buffer.\n\r");
//	status = framebuffer_run
//	(
//		p_periphs_inst->p_vdma_camera_inst,
//		p_periphs_inst->p_vdma_camera_inst,
//		16, // 16-Bits per pixel
//		//24, // 24-Bits per pixel
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
//		p_periphs_inst->fb_camera_start_addr
//	);
//	if(status != PERIPHS_SUCCESS) {
//		xil_printf("ERROR! Failed to assign camera frame buffer.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
//
//	// Set up Camera Freeze Frame buffer
//	xil_printf("Setting up Camera freeze frame buffer.\n\r");
//	status = framebuffer_run
//	(
//		p_periphs_inst->p_vdma_camera_freeze_inst,
//		p_periphs_inst->p_vdma_camera_freeze_inst,
//		16, // 16-Bits per pixel
//		//24, // 24-Bits per pixel
//		p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo,
//		p_periphs_inst->fb_camera_freeze_start_addr
//	);
//	if(status != PERIPHS_SUCCESS) {
//		xil_printf("ERROR! Failed to assign camera freeze frame buffer.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
//
//	// Set up GUI Frame buffer
//	xil_printf("Setting up GUI frame buffer.\n\r");
//	status = framebuffer_run
//	(
//		NULL,
//		p_periphs_inst->p_vdma_GUI_inst,
//		//16, // 16-Bits per pixel
//		24, // 24-Bits per pixel
//		p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->VActiveVideo,
//		p_periphs_inst->fb_GUI_start_addr
//	);
//	if(status != PERIPHS_SUCCESS) {
//		xil_printf("ERROR! Failed to assign GUI framebuffer.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
//
//	// Set new (VPSS-based) Scaler parameters
////	xil_printf("Setting up new VPSS-based scaler.\n\r");
////	status = scaler_new_set_output_size
////	(
////		p_periphs_inst->p_scaler_camera_inst,
////		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo,
////		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo,
////		1 // Print configuration
////	);
////	if (status != SCALER_NEW_SUCCESS)
////	{
////		xil_printf("ERROR! Failed to set input size on the new VPSS-based scaler.\n\r");
////		return PERIPHS_ERROR_UNKNOWN;
////	}
//
//	// Update VPSS input frame size
//	xil_printf("Setting up Camera scaler.\n\r");
//	status = scaler_new_set_size
//	(
//		p_periphs_inst->p_scaler_camera_inst,
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo,
//		1 // Print configuration
//	);
//
//	if (status != SCALER_NEW_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to set Camera scaler.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
//
//	// Update VPSS input frame size
//	xil_printf("Setting up Camera Freeze scaler.\n\r");
//	status = scaler_new_set_size
//	(
//		p_periphs_inst->p_scaler_camera_freeze_inst,
//		p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo,
//		p_periphs_inst->p_vid_io_camera_freeze_inst->p_output_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_freeze_inst->p_output_timing_inst->VActiveVideo,
//		1 // Print configuration
//	);
//
//	if (status != SCALER_NEW_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to set Camera freeze scaler.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}
//
//	// TPG gets reset, so re-configure it
//	// Set camera TPG to Default VGA
//	xil_printf("Initialize Camera TPG to Camera size (VGA).\n\r");
//	test_pattern_gen_config
//	(
//		p_periphs_inst->p_tpg_camera_inst,
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
//		p_periphs_inst->bypass_camera_tpg,
//		0, // Box is red for TPG on new VPSS scaler datapath
//		XVIDC_CSF_YCRCB_422,
//		0  // print regs
//	);
//
//	// TPG gets reset, so re-configure it
//	// Set GUI TPG to Default 1080P
//	xil_printf("Initialize GUI TPG to 1080P.\n\r");
//	test_pattern_gen_config
//	(
//		p_periphs_inst->p_tpg_GUI_inst,
//		p_periphs_inst->p_vid_io_GUI_inst->p_input_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_GUI_inst->p_input_timing_inst->VActiveVideo,
//		p_periphs_inst->bypass_GUI_tpg,
//		0, // Box is red for TPG on new VPSS scaler datapath
//		XVIDC_CSF_RGB,
//		0  // print regs
//	);
//
//	// Enable VTD to start letting video in
////	if (periphs_get_fmc_status(p_periphs_inst))
////	{
////		vtiming_det_run(p_periphs_inst->p_vtd_inst);
////	}
//
//	return PERIPHS_SUCCESS;
//}

void periphs_select_scaler
(
	periphs_t* p_periphs_inst,
	scaler_option_t which_scaler
)
{
	which_scaler = PERIPHS_SEL_NEW_SCALER;
	xil_printf("david1023: %s:%s(%d) ST xxxxxxxxxxxxxxxxxxxxxxxx\r\n",__FILE__,__func__,__LINE__);

//	if (which_scaler == PERIPHS_SEL_NEW_SCALER)
//	{
//		XGpio_DiscreteSet(p_periphs_inst->p_vid_mux_sel_gpio_inst, 1, 1);
//	}
//	else if (which_scaler == PERIPHS_SEL_OLD_SCALER)
//	{
//		XGpio_DiscreteClear(p_periphs_inst->p_vid_mux_sel_gpio_inst, 1, 1);
//	}
	
}

int periphs_toggle_camera_tpg
(
	periphs_t* p_periphs_inst
)
{
	// Local variables
	xil_printf("david1023: %s:%s(%d) ST xxxxxxxxxxxxxxxxxxxxxxxxx\r\n",__FILE__,__func__,__LINE__);
//	xil_printf(">++++++Into Bypassing/Enable camera TPG.\n\r");
//
//	// Determine if we're in TPG or passthrough mode
//	if (p_periphs_inst->bypass_camera_tpg == PERIPHS_SEL_ENABLE_TPG)
//	{
//		p_periphs_inst->bypass_camera_tpg = PERIPHS_SEL_BYPASS_TPG;
//		xil_printf(">>>>>Bypassing camera TPG.\n\r");
//	}
//	else
//	{
//		p_periphs_inst->bypass_camera_tpg = PERIPHS_SEL_ENABLE_TPG;
//		xil_printf(">>>>>Enable camera TPG.\n\r");
//	}
//
//	periphs_bring_up_input_dma(p_periphs_inst);
//	//periphs_bring_up_output_dma(p_periphs_inst);


	
	return PERIPHS_SUCCESS;
}

int periphs_toggle_GUI_tpg
(
	periphs_t* p_periphs_inst
)
{
	// Local variables
	//int status = 0;
	xil_printf("david1023: %s:%s(%d) ST\r\n",__FILE__,__func__,__LINE__);
	xil_printf(">++++++Into Bypassing/Enable GUI TPG.\n\r");

	// TPG always on when no FMC card is present
//	if (!periphs_get_fmc_status(p_periphs_inst))
//	{
//		return PERIPHS_ERROR_NO_FMC_CARD;
//		xil_printf(">>>>>TPG:PERIPHS_ERROR_NO_FMC_CARD.\n\r");
//	}

	// Determine if we're in TPG or passthrough mode
	if (p_periphs_inst->bypass_GUI_tpg == PERIPHS_SEL_ENABLE_TPG)
	{
		xil_printf("11111\n\r");
		p_periphs_inst->bypass_GUI_tpg = PERIPHS_SEL_BYPASS_TPG;
		xil_printf(">>>>>Bypassing GUI TPG.\n\r");
	}
	else
	{
		xil_printf("22222\n\r");
		p_periphs_inst->bypass_GUI_tpg = PERIPHS_SEL_ENABLE_TPG;
		xil_printf(">>>>>Enable GUI TPG.\n\r");
	}

	// Put VTD in reset to hold off partial frames
	//vtiming_det_stop(p_periphs_inst->p_vtd_inst);

//	// Re-configure the VPSS to cause a reset to the TPG to avoid partial frame issue
//	status = scaler_new_set_size
//	(
//		p_periphs_inst->p_scaler_camera_inst,
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo,
//		1 // Print configuration
//	);
//	if (status != SCALER_NEW_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to set input size on the new VPSS-based scaler.\n\r");
//		return PERIPHS_ERROR_UNKNOWN;
//	}

	// Set TPG to Default VGA
	xil_printf("Initialize GUI TPG to 1080P. TPG\n\r");
	test_pattern_gen_config
	(
		p_periphs_inst->p_tpg_GUI_inst,
		p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->HActiveVideo,
		p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->VActiveVideo,
		p_periphs_inst->bypass_GUI_tpg,
		0, // Box is red for TPG on new VPSS scaler datapath
		XVIDC_CSF_RGB,
		XTPG_BKGND_COLOR_BARS,
		0  // print regs, normally no message
	);
	xil_printf("david1026: %s:%s(%d) HActive = %d VActive = %d\r\n", __FILE__, __func__, __LINE__, p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->HActiveVideo, p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->VActiveVideo);


	XV_tpg_EnableAutoRestart(p_periphs_inst->p_tpg_GUI_inst);
	XV_tpg_Start(p_periphs_inst->p_tpg_GUI_inst);

	// Enable VTD to start letting video in
	//vtiming_det_run(p_periphs_inst->p_vtd_inst);

	return PERIPHS_SUCCESS;
}

int ccc = 0;
int periphs_toggle_camera_freeze_vdma
(
	periphs_t* p_periphs_inst
)
{
	// Local variables
	//int status = 0;
	xil_printf(">++++++Into Park/Un-park Camera Freeze VDMA.\n\r");

	// Determine if we're in TPG or passthrough mode
	if (p_periphs_inst->enable_camera_freeze_vdma == PERIPHS_SEL_ENABLE_PARK)
	{
		p_periphs_inst->enable_camera_freeze_vdma = PERIPHS_SEL_DISABLE_PARK;
		XAxiVdma_StopParking(p_periphs_inst->p_vdma_camera_freeze_inst, XAXIVDMA_READ);

		xil_printf(">>>>>Unpark camera freeze vdma.\n\r");
	}
	else
	{
		ccc++;
		p_periphs_inst->enable_camera_freeze_vdma = PERIPHS_SEL_ENABLE_PARK;
		//XAxiVdma_StartParking(p_periphs_inst->p_vdma_camera_freeze_inst, 0, XAXIVDMA_READ);
		XAxiVdma_StartParking(p_periphs_inst->p_vdma_camera_freeze_inst, (ccc%3), XAXIVDMA_READ);
		xil_printf(">>>>>Park camera freeze vdma.\n\r");
	}

	return PERIPHS_SUCCESS;
}

int periphs_configure_gpio_pins
(
	periphs_t*   p_periphs_inst
)
{
	// Local variables
	int           status = 0;
	XGpioPs*	  p_gpio;
	XGpio*		  p_lock;

	p_gpio = p_periphs_inst->p_ps_gpio_inst;
	p_lock = p_periphs_inst->p_lock_monitor_inst;

	// Configure PS_GPIO Bank 2
	// Steps must be followed to prevent damage to chip, unused bank pins are set to output and tied to ground.
	xil_printf("Set up PS GPIO.\n\r");
	// bit[10:0], 11 bits - Output
	// bit[17:11], 7 bits - Input
	// bit[31:18], 14 bits - Output, default write value 0
	XGpioPs_SetDirection(p_gpio, XGPIOPS_BANK2, PIN_DIR_DEFAULT); // Direction is 32bit mapped, 0 = input, 1 = output, unused pins are set to output logic 0
	XGpioPs_Write(p_gpio, XGPIOPS_BANK2, PIN_DEF_DEFAULT); // Set to default outputs
	XGpioPs_SetOutputEnable(p_gpio, XGPIOPS_BANK2, PIN_DIR_DEFAULT);

	// Configure Video Lock - TODO
	xil_printf("Set up Video Lock Monitor.\n\r");
	// bit[3:0], Input
	// 0 - MMCM Locked
	// 1 - TFP410 Locked
	// 2 - CH7038 Locked
	// 3 - Matched K Code
	// Set the direction for all signals as inputs except the LED output */
	XGpio_SetDataDirection(p_lock, LOCK_MONITOR, 0xffff); // 0 = output, 1 = input

	// Debug
	status = XGpio_GetDataDirection(p_lock, LOCK_MONITOR);
	xil_printf("david1207: lock_monitor: 0x%08x\r\n", status);

	xil_printf("\n\r");

	return PERIPHS_SUCCESS;
}

//int periphs_configure_gpio_interrupts
//(
//	periphs_t*   p_periphs_inst
//)
//{
//	// Local variables
//	int           status = 0;
//	XGpioPs*	  p_gpio;
//	XGpio*		  p_lock_monitor;
//
//	p_gpio = p_periphs_inst->p_ps_gpio_inst;
//	p_lock_monitor = p_periphs_inst->p_lock_monitor_inst;
//
//	// Configure PS_GPIO Bank 2
//	// Steps must be followed to prevent damage to chip, unused bank pins are set to output and tied to ground.
//	xil_printf("Set up PS GPIO.\n\r");
//	// bit[10:0], 11 bits - Output
//	// bit[17:11], 7 bits - Input
//	// bit[31:18], 14 bits - Output, default write value 0
//	XGpioPs_SetDirection(p_gpio, XGPIOPS_BANK2, PIN_DIR_DEFAULT); // Direction is 32bit mapped, 0 = input, 1 = output, unused pins are set to output logic 0
//	XGpioPs_Write(p_gpio, XGPIOPS_BANK2, PIN_DEF_DEFAULT); // Set to default outputs
//	XGpioPs_SetOutputEnable(p_gpio, XGPIOPS_BANK2, PIN_DIR_DEFAULT);
//
//	// Configure Video Lock - TODO
//
//
//	return PERIPHS_SUCCESS;
//}



int periphs_bring_up_input_pipeline
(
	periphs_t*   p_periphs_inst
)
{
	// Local variables
	int           status = 0;
	XVprocSs* VprocInst;//JACKY

	//vres_timing_t vres_timing;
	// Look up timing info from ID
	//vres_get_timing(new_input_timing, &vres_timing);

	xil_printf("\n\rdavid1023: %s:%s(%d) ST\r\n",__FILE__,__func__,__LINE__);

	// Software Reset Camera/Camera Freeze Input Pipeline
	//
	//
	/////////////////////////////////////////////////////
	//VDMA Write Reset
	xil_printf("\n\rcall vdma_reset 1 camera vdma, base = 0x%08x\n\r", p_periphs_inst->p_vdma_camera_inst->BaseAddr);
	vdma_reset(p_periphs_inst->p_vdma_camera_inst , XAXIVDMA_WRITE); // Reset write channel
	xil_printf("\n\rcall vdma_reset 2 camera freeze vdma, base = 0x%08x\n\r", p_periphs_inst->p_vdma_camera_freeze_inst->BaseAddr);
	vdma_reset(p_periphs_inst->p_vdma_camera_freeze_inst , XAXIVDMA_WRITE); // Reset write channel
	xil_printf("\n\r");
	// Camera TPG cannot be software reset
	// VTD
//	xil_printf("Reset VTD.\n\r");
//	XVtc_Reset(p_periphs_inst->p_vtd_inst);

	// Configure Camera/Camera Freeze Input Pipeline
	//
	//
	//////////////////////////////////////////////////
	// Setup camera write channel
	//xil_printf("Set up camera/camera freeze write channel (VGA).\n\r");
	// Setup camera write channel
	xil_printf("Set up camera vdma write channel call framebuffer_write, setup start_addr = 0x%08x\n\r", p_periphs_inst->fb_camera_start_addr);
	status = framebuffer_write(	p_periphs_inst->p_vdma_camera_inst,
								//16,//Mark for add VPSS and width converter
								24,//Add for add VPSS and width converter
								p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
								p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
								p_periphs_inst->fb_camera_start_addr,
								CAMERA_STRIDE);
	xil_printf("david1026: %s:%s(%d) framebuffer_write camera vdma HActive = %d VActive = %d start_addr = 0x%08x\r\n", __FILE__, __func__, __LINE__,
			p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo, p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo, p_periphs_inst->fb_camera_start_addr);

	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the write side of the camera VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	xil_printf("\n\rSet up camera freeze vdma write channel call framebuffer_write, setup start addr = 0x%08x\n\r", p_periphs_inst->fb_camera_freeze_start_addr);
	// Setup camera freeze write channel
	status = framebuffer_write(	p_periphs_inst->p_vdma_camera_freeze_inst,
								//16,//Mark for add VPSS and width converter
								24,//Add for add VPSS and width converter
								p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo,
								p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo,
								p_periphs_inst->fb_camera_freeze_start_addr,
								CAMERA_STRIDE);
	xil_printf("david1026: %s:%s(%d) framebuffer_write camera freeze vdma HActive = %d VActive = %d start_addr = 0x%08x\r\n", __FILE__, __func__, __LINE__,
			p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo, p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo, p_periphs_inst->fb_camera_freeze_start_addr);

	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the write side of the camera freeze VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}
	xil_printf("\n\r");



	//------------------------------------------------------   JACKY   -------------------------------------------------------------
	//XVprocSs_SetUserTimerHandler(XVprocSs *InstancePtr, XVidC_DelayHandler CallbackFunc, void *CallbackRef);
	//XVprocSs_SetUserTimerHandler(p_periphs_inst->p_scaler_camera_freeze_inst, p_periphs_inst->p_vid_io_camera_freeze_inst->, void *CallbackRef);
	//xil_printf("Start XVprocSs_SetUserTimerHandler[If the application is not using the timing peripheral to implement the timeouts]\n\r");

	//XVprocSs_CfgInitialize(XVprocSs *InstancePtr, XVprocSs_Confg *CfgPtr,UINTPTR EffectiveAddr);
	//XVprocSs_CfgInitialize(VprocInst, XVprocSs_Confg *CfgPtr,UINTPTR EffectiveAddr);
	//status = XVprocSs_CfgInitialize(p_periphs_inst->p_scaler_camera_freeze_inst, p_vpss_camera_freeze_cfg, p_vpss_camera_freeze_cfg->BaseAddress);
	//xil_printf("Start XVprocSs_CfgInitialize\n\r");

	//XVprocSs_SetSubsystemConfig(XVprocss *InstancePtr);
	XVprocSs_SetSubsystemConfig(p_periphs_inst->p_scaler_camera_freeze_inst);
	xil_printf("Start XVprocSs_SetSubsystemConfig\n\r");

	//------------------------------------------------------   JACKY   -------------------------------------------------------------


	// VTD - To be implemented, ignore for now

	// Run IP /////////////////////////////////////////
	//
	//
	///////////////////////////////////////////////////

	// Start Camera write side VDMA
	//xil_printf("Run camera/camera freeze write channel (VGA).\n\r");
	xil_printf("DMA start camera VDMA XAXIVDMA_WRITE\n\r");
	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_camera_inst, XAXIVDMA_WRITE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to start the Camera write side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	// Start Camera Freeze write side VDMA
	xil_printf("\n\rDMA start camera freeze VDMA XAXIVDMA_WRITE\n\r");
	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_camera_freeze_inst, XAXIVDMA_WRITE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to start the Camera write side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	xil_printf("david1023: %s:%s(%d) SP\n\r\r\n",__FILE__,__func__,__LINE__);

	// VTD - TBD

	return PERIPHS_SUCCESS;
}

int periphs_bring_up_output_pipeline
(
	periphs_t*   p_periphs_inst,
	unsigned int new_output_timing,
	unsigned int fb_GUI_start_addr
)
{
	// Local variables
	int           status = 0;
	vres_timing_t vres_timing0, vres_timing1;
	XVidC_ColorFormat Cfmt;
	XVidC_VideoMode resId;
	XVidC_VideoStream VidStream;
	uint32_t i;

	xil_printf("\n\rdavid1023: %s:%s(%d) ST vid = %d fb_GUI_start_addr = 0x%08x\r\n",__FILE__,__func__,__LINE__, new_output_timing, fb_GUI_start_addr);

	// Look up timing info from ID
	xil_printf("call vres_get_timing for vres_timing0, vid = 0 (VGA)\n\r");
	vres_get_timing(0, &vres_timing0);
	xil_printf("call vres_get_timing for vres_timing1, vid = %d (1080p)\n\r", new_output_timing);
	vres_get_timing(new_output_timing, &vres_timing1);

	// Software Reset Output Pipeline
	//
	//
	/////////////////////////////////////////////////////
	// VTG 0/1 Reset
	xil_printf("Reset VTG 0/1.\n\r");
	vtiming_gen_reset(p_periphs_inst->p_vtg_inst_0);
	vtiming_gen_reset(p_periphs_inst->p_vtg_inst_1);

	xil_printf("vtg_inst_0 base = 0x%08x VTG_0(TFP410)\n\r", p_periphs_inst->p_vtg_inst_0->Config.BaseAddress);
	xil_printf("vtg_inst_1 base = 0x%08x VTG_1(CH7038)\n\r", p_periphs_inst->p_vtg_inst_1->Config.BaseAddress);


	//----------------------------------------------------------------------JACKKY1001------------------------------------------------------
	if (status != SCALER_NEW_SUCCESS)
	{
		xil_printf("ERROR! JACKYVPSS: Failed to set Camera scaler.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	xil_printf("\n\rJACKYVPSS: Setting up Camera CSC.  call scaler_new_set_size base = 0x%08x\n\r", p_periphs_inst->p_scaler_camera_inst->Config.BaseAddress);
	xil_printf("JACKYVPSS: base = 0x%08x input W = %d H = %d, output W = %d H = %d\n\r",
			p_periphs_inst->p_scaler_camera_inst->Config.BaseAddress,
			p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo, p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
			p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo, p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo);


    xil_printf("JACKY1001: periphs_bring_up_output_pipeline: %s:%s(%d)[H=%d, V=%d]\r\n",__FILE__,__func__,__LINE__, p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo, p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo);
	status = scaler_new_set_size
	(
		p_periphs_inst->p_scaler_camera_inst,
		//p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo/2,
		//p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo/2,
		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo - zoom_cut * 2,
		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo - zoom_cut * 3 / 4 * 2,
		XVIDC_CSF_YCRCB_422,
		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo,
		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo,
		//XVIDC_CSF_YCRCB_422,//Original422, JACKY Color Abnormal
		XVIDC_CSF_RGB,//Original422, JACKY Step 1:
		//XVIDC_CSF_YCRCB_444,//Step 2: Change color to 444 for IP YCrCb to RGB JACKY

		1 // Print configuration
	);
	if (status != SCALER_NEW_SUCCESS)
	{
		xil_printf("ERROR! Failed to set Camera freeze scaler.\n\r");
	    xil_printf("JACKY1001: %s:%s(%d) [default: %d\r\n",__FILE__,__func__,__LINE__, status);
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("\n\rJACKYVPSS: setup Camera CSC ok\n\r\n\r");
	//----------------------------------------------------------------------JACKKY1001------------------------------------------------------


	// Video Mixer Reset - no software reset, skip
	// GUI TPG cannot be software reset
	// Camera/Camera Freeze VPSS Reset - Already done by cfginitialize

	//VDMA Read Reset
	xil_printf("\n\rcall vdma_reset 3 camera vdma, base = 0x%08x\n\r", p_periphs_inst->p_vdma_camera_inst->BaseAddr);
	vdma_reset(p_periphs_inst->p_vdma_camera_inst , XAXIVDMA_READ); // Reset read channel
	xil_printf("\n\rcall vdma_reset 4 camera freeze vdma, base = 0x%08x\n\r", p_periphs_inst->p_vdma_camera_freeze_inst->BaseAddr);
	vdma_reset(p_periphs_inst->p_vdma_camera_freeze_inst , XAXIVDMA_READ); // Reset read channel
	xil_printf("\n\r");
	//vdma_reset(p_periphs_inst->p_vdma_GUI_inst , XAXIVDMA_READ); // Reset read channel

	// Configure Output Pipeline
	//
	//
	//////////////////////////////////////////////////
	// VTG 0 and 1
	xil_printf("Configure VTG 0 and VTG 1, vid = %d\n\r", new_output_timing);
	// Set output frame size for Video Output interface
	vid_io_intf_update_output_fsize(p_periphs_inst->p_vid_io_GUI_inst, new_output_timing);

	// Set VTG_0 output timing
	xil_printf("Set VTG_0 output timing, vid = %d base = 0x%08x VTG_0(TFP410)\n\r", new_output_timing, p_periphs_inst->p_vtg_inst_0->Config.BaseAddress);
	vtiming_gen_config(p_periphs_inst->p_vtg_inst_0, new_output_timing, 2);
	//vtiming_gen_config(p_periphs_inst->p_vtg_inst_0, 0, 2); // VGA, for test

	// Set VTG_1 output timing
	xil_printf("\n\rSet VTG_1 output timing, vid = %d base = 0x%08x VTG_1(CH7038)\n\r", new_output_timing, p_periphs_inst->p_vtg_inst_1->Config.BaseAddress);
	vtiming_gen_config(p_periphs_inst->p_vtg_inst_1, new_output_timing, 2);

	{
	// Video Mixer Config - set output frame size
	xil_printf("\n\rInitialize Video Mixer and settings.\n\r");
	// Set default stream (output, RGB, 8bit/color, 1 pix per clock)
	XVMix_GetLayerColorFormat(p_periphs_inst->p_vid_output_mixer_l2_inst, XVMIX_LAYER_MASTER, &Cfmt);
	// Get resolution ID from frame size
	resId = XVidC_GetVideoModeId(LAYER0_WIDTH, LAYER0_HEIGHT, XVIDC_FR_60HZ, FALSE);

	xil_printf("david1026: %s:%s(%d) resId = %d XVIDC_VM_1920x1080_60_P = %d\r\n", __FILE__, __func__, __LINE__, resId, XVIDC_VM_1920x1080_60_P);

	//xil_printf("resId: %d\n\r",resId);
	// Setup Video Mixer Input AXI-S Parameters
	VidStream.VmId           = resId;
	VidStream.Timing.HActive = p_periphs_inst->p_vid_io_GUI_inst->p_input_timing_inst->HActiveVideo;
	VidStream.Timing.VActive = p_periphs_inst->p_vid_io_GUI_inst->p_input_timing_inst->VActiveVideo;
	VidStream.ColorFormatId  = Cfmt;
	VidStream.ColorDepth     = 8;
	VidStream.PixPerClk      = 1;
	VidStream.FrameRate      = XVIDC_FR_60HZ;
	VidStream.IsInterlaced   = 0;

	xil_printf("david1026: %s:%s(%d) vid = %d HActive = %d VActive = %d ColorFormatId = %d\r\n", __FILE__, __func__, __LINE__,
			VidStream.VmId, VidStream.Timing.HActive, VidStream.Timing.VActive, VidStream.ColorFormatId);

	// TEST: write to GUI framebuffer
//	memset((void *)fb_GUI_start_addr, 0x80, GUI_STRIDE*1080);
//	memset((void *)fb_GUI_start_addr, 0x80, 0x2000000); // Clear Frame buffer

	// Move const overlay into frame buffer
//	ptr = (void *)fb_GUI_start_addr;
//	memcpy(ptr, &GUI_overlay[0], GUI_overlay_length);

//	i = fb_GUI_start_addr;
//	ptr =  (void *)i;
//	*ptr = 0x12345678;
//	xil_printf("*ptr:%x.\n\r", *ptr);

//	for(uint32_t i = fb_GUI_start_addr; i < fb_GUI_start_addr+0x2000000;i+=4)
//	{
//		ptr =  (void *)i;
//		//xil_printf("i: %x, ptr: %x, *ptr: %x.\n\r", i, ptr, *ptr);
//		if((*ptr) != 0x80808080)
//		{
//			//xil_printf("1. *ptr:%x.\n\r", *ptr);
//		}
//	}

	// configure mixer
	xil_printf("\n\rconfigure mixer call ConfigMixer, base = 0x%08x fb_GUI_start_addr = 0x%08x\r\n", p_periphs_inst->p_vid_output_mixer_l2_inst->Mix.Config.BaseAddress, fb_GUI_start_addr);
	xil_printf("david1105: %s:%s(%d) NumLayers = %d\r\n", __FILE__, __func__, __LINE__, p_periphs_inst->p_vid_output_mixer_l2_inst->Mix.Config.NumLayers);
    ConfigMixer(p_periphs_inst->p_vid_output_mixer_l2_inst, &VidStream, fb_GUI_start_addr);

//	for(uint32_t i = fb_GUI_start_addr; i < fb_GUI_start_addr+0x2000000;i+=4)
//	{
//		ptr =  (void *)i;
//		//xil_printf("i: %x, ptr: %x, *ptr: %x.\n\r", i, ptr, *ptr);
//		if((*ptr) != 0x80808080)
//		{
//			//xil_printf("2. *ptr:%x.\n\r", *ptr);
//		}
//	}

    // Mixer Debug
    xil_printf("\n\r\n\rMixer Debug\tdavid1016: %s:%s(%d) call XVMix_DbgReportStatus\r\n",__FILE__,__func__,__LINE__);
    XVMix_DbgReportStatus(p_periphs_inst->p_vid_output_mixer_l2_inst);

    xil_printf("david1016: %s:%s(%d) call XVMix_DbgLayerInfo\r\n",__FILE__,__func__,__LINE__);

	//for(i = XVMIX_LAYER_MASTER; i < (XVMIX_LAYER_LAST - 5); i++)
    for(i = XVMIX_LAYER_MASTER; i < 5; i++)
	{
		XVMix_DbgLayerInfo(p_periphs_inst->p_vid_output_mixer_l2_inst, i);
	}
	xil_printf("\n\r\n\r");
	}

	// GUI TPG Config - Set to Default 1080P
	xil_printf("\n\rInitialize GUI TPG to 1080P. bbb call test_pattern_gen_config, base = 0x%08x W = %d H = %d\n\r",
			p_periphs_inst->p_tpg_GUI_inst->Config.BaseAddress,p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->HActiveVideo, p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->VActiveVideo);

	test_pattern_gen_config
	(
		p_periphs_inst->p_tpg_GUI_inst,
		p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->HActiveVideo,
		p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->VActiveVideo,
		p_periphs_inst->bypass_GUI_tpg,
		0, // Box is red for TPG on new VPSS scaler datapath
		XVIDC_CSF_RGB,
		XTPG_BKGND_SOLID_GREEN,	//XTPG_BKGND_SOLID_BLACK,
		//XTPG_BKGND_COLOR_BARS,
		0  // print regs
	);
	xil_printf("\n\rsetup test pattern gen ok\n\r\n\r");

//	// Camera Scaler - Update camera/camera freeze frame size
//	xil_printf("Setting up Camera scaler.\n\r");
//	status = scaler_new_set_size
//	(
//		p_periphs_inst->p_scaler_camera_inst,
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
//		XVIDC_CSF_YCRCB_422,
//		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo,
//		p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo,
//		XVIDC_CSF_YCRCB_422,
//		//XVIDC_CSF_RGB,
//		1 // Print configuration
//	);

	if (status != SCALER_NEW_SUCCESS)
	{
		xil_printf("ERROR! Failed to set Camera scaler.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	xil_printf("\n\rSetting up Camera Freeze scaler.  call scaler_new_set_size base = 0x%08x\n\r", p_periphs_inst->p_scaler_camera_freeze_inst->Config.BaseAddress);
	xil_printf("base = 0x%08x input W = %d H = %d, output W = %d H = %d\n\r",
			p_periphs_inst->p_scaler_camera_freeze_inst->Config.BaseAddress,
			p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo, p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo,
			p_periphs_inst->p_vid_io_camera_freeze_inst->p_output_timing_inst->HActiveVideo, p_periphs_inst->p_vid_io_camera_freeze_inst->p_output_timing_inst->VActiveVideo);

	status = scaler_new_set_size
	(
		p_periphs_inst->p_scaler_camera_freeze_inst,
		//p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo/2,
		//p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo/2,
		p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo - zoom_cut * 2,
		p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo - zoom_cut * 3 / 4 * 2,
		//XVIDC_CSF_YCRCB_422, //MArk for add new VPSS JACKKY
		XVIDC_CSF_RGB,// for add new VPSS JACKKY
		p_periphs_inst->p_vid_io_camera_freeze_inst->p_output_timing_inst->HActiveVideo,
		p_periphs_inst->p_vid_io_camera_freeze_inst->p_output_timing_inst->VActiveVideo,
		//XVIDC_CSF_YCRCB_422,//Original422, JACKY Color Abnormal
		XVIDC_CSF_RGB,//Original422, JACKY Step 1:
		//XVIDC_CSF_YCRCB_444,//Step 2: Change color to 444 for IP YCrCb to RGB JACKY

		1 // Print configuration
	);
	if (status != SCALER_NEW_SUCCESS)
	{
		xil_printf("ERROR! Failed to set Camera freeze scaler.\n\r");
	    xil_printf("JACKY1001: %s:%s(%d) [default: %d\r\n",__FILE__,__func__,__LINE__, status);
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("\n\rsetup Camera Freeze scaler ok\n\r\n\r");

	// VDMA
	// Setup camera read channel
	xil_printf("\n\rSetup camera vdma read channel, start_addr = 0x%08x\n\r", p_periphs_inst->fb_camera_start_addr);
	xil_printf("\n\rSetup camera vdma read channel, start_addr = 0x%08x H = %d V = %d\n\r",
			p_periphs_inst->fb_camera_start_addr, p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo, p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo);
	status = framebuffer_read(	p_periphs_inst->p_vdma_camera_inst,
								24,
								p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
								p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
								//p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo,
								//p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo,
								p_periphs_inst->fb_camera_start_addr,
								CAMERA_STRIDE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the read side of the camera VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}
	xil_printf("\n\rSetup camera vdma read channel, start_addr = 0x%08x OK\n\r", p_periphs_inst->fb_camera_start_addr);

	xil_printf("\n\rSetup camera freeze vdma read channel, start_addr = 0x%08x\n\r", p_periphs_inst->fb_camera_freeze_start_addr);
	xil_printf("\n\rSetup camera freeze vdma read channel, start_addr = 0x%08x H = %d V = %d\n\r",
			p_periphs_inst->fb_camera_freeze_start_addr, p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo, p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo);
	// Setup camera freeze read channel
	status = framebuffer_read(	p_periphs_inst->p_vdma_camera_freeze_inst,
								24,
								//p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo/2,
								p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo  - zoom_cut * 2,
								p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo / 1,
								//p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo,
								//p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo,
								//p_periphs_inst->fb_camera_freeze_start_addr + 2048 * 120 + 4*160/2,
								p_periphs_inst->fb_camera_freeze_start_addr
								+ 2048 * zoom_cut * 3 / 4
								+ 2 * zoom_cut,
								CAMERA_STRIDE);

	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the read side of the camera freeze VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}
	xil_printf("\n\rSetup camera freeze vdma read channel, start_addr = 0x%08x OK\n\r", p_periphs_inst->fb_camera_freeze_start_addr);
	xil_printf("\n\r");
	// Setup GUI read channel
//	xil_printf("Set up GUI read channel (1080P).\n\r");
//	status = framebuffer_read(	p_periphs_inst->p_vdma_GUI_inst,
//								24,
//								p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->HActiveVideo,
//								p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->VActiveVideo,
//								p_periphs_inst->fb_GUI_start_addr,
//								GUI_STRIDE);
//	if (status != XST_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to configure the read side of the GUI VDMA.\n\r");
//		return FRAMEBUFFER_ERROR_UNKNOWN;
//	}

	// Run IP /////////////////////////////////////////
	//
	//
	///////////////////////////////////////////////////
	// VTG 0/1 Run
	xil_printf("david1023: %s:%s(%d) VTG run p_vtg_inst_0 base = 0x%08x\r\n",__FILE__,__func__,__LINE__, p_periphs_inst->p_vtg_inst_0->Config.BaseAddress);

	xil_printf("david1023: %s:%s(%d) VTG run p_vtg_inst_1 base = 0x%08x\r\n",__FILE__,__func__,__LINE__, p_periphs_inst->p_vtg_inst_1->Config.BaseAddress);
	vtiming_gen_start(p_periphs_inst->p_vtg_inst_0);
	//xil_printf("can not insert a message here\r\n",__FILE__,__func__,__LINE__);
	vtiming_gen_start(p_periphs_inst->p_vtg_inst_1);

	/*
	xil_printf("david1101: %s:%s(%d) call get_xvtc_version\r\n",__FILE__,__func__,__LINE__);
	get_xvtc_version(p_periphs_inst->p_vtg_inst_0);
	get_xvtc_version(p_periphs_inst->p_vtg_inst_1);
	*/


//	for(uint32_t i = fb_GUI_start_addr; i < fb_GUI_start_addr+0x2000000;i+=4)
//	{
//		ptr =  (void *)i;
//		//xil_printf("i: %x, ptr: %x, *ptr: %x.\n\r", i, ptr, *ptr);
//		if((*ptr) != 0x80808080)
//		{
//			//xil_printf("3. *ptr:%x.\n\r", *ptr);
//		}
//	}

//	// Start Mixer
//	RunMixer(p_periphs_inst->p_vid_output_mixer_l2_inst);

//	for(uint32_t i = fb_GUI_start_addr; i < fb_GUI_start_addr+0x2000000;i+=4)
//	{
//		ptr =  (void *)i;
//		//xil_printf("i: %x, ptr: %x, *ptr: %x.\n\r", i, ptr, *ptr);
//		if((*ptr) != 0x80808080)
//		{
//			//xil_printf("4. *ptr:%x.\n\r", *ptr);
//		}
//	}

//	// Move const overlay into frame buffer
//	ptr = (void *)fb_GUI_start_addr;
//	memcpy(ptr, &GUI_overlay[0], GUI_overlay_length);

	// Start GUI TPG
	xil_printf("\n\rRun GUI TPG (1080P).\n\r");
	XV_tpg_EnableAutoRestart(p_periphs_inst->p_tpg_GUI_inst);
	XV_tpg_Start(p_periphs_inst->p_tpg_GUI_inst);

	// Start Camera read side VDMA
	xil_printf("\n\rRun camera/camera freeze read channel (VGA).\n\r");
	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_camera_inst, XAXIVDMA_READ);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to start the Camera read side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	// Start Camera Freeze read side VDMA
	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_camera_freeze_inst, XAXIVDMA_READ);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to start the Camera read side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

//	// Start GUI read side VDMA
//	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_GUI_inst, XAXIVDMA_READ);
//	if (status != XST_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to start the GUI read side of the VDMA.\n\r");
//		return FRAMEBUFFER_ERROR_UNKNOWN;
//	}

	xil_printf("\n\rdavid1023: %s:%s(%d) SP\r\n\n\r",__FILE__,__func__,__LINE__);

	return PERIPHS_SUCCESS;
}

int periphs_bring_up_output_dma
(
	periphs_t*   p_periphs_inst
)
{
	// Local variables
	int           status = 0;

	xil_printf("david1026: %s:%s(%d) ST xxxxxxxxxxxxxxxxxx\r\n", __FILE__, __func__, __LINE__);

	//VDMA Read
	xil_printf("Reset camera/camera freeze VDMA read channel (VGA).\n\r");
	//vdma_reset(p_periphs_inst->p_vdma_camera_inst , XAXIVDMA_READ); // Reset read channel
	//vdma_reset(p_periphs_inst->p_vdma_camera_freeze_inst , XAXIVDMA_READ); // Reset read channel

	// VDMA
	// Setup camera read channel
	//xil_printf("Set up camera/camera freeze read channel (VGA).\n\r");
	xil_printf("\n\rxxxx Set up camera vdma read channel bbb xxx\n\r");
	status = framebuffer_read(	p_periphs_inst->p_vdma_camera_inst,
								24,
								p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
								p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
								//p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo,
								//p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo,
								p_periphs_inst->fb_camera_start_addr,
								CAMERA_STRIDE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the read side of the camera VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}
	// Setup camera freeze read channel
	xil_printf("\n\rxxxx Set up camera freeze vdma read channel bbb xxx\n\r");
	status = framebuffer_read(	p_periphs_inst->p_vdma_camera_freeze_inst,
								24,
								p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo,
								p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo,
								//p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo,
								//p_periphs_inst->p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo,
								p_periphs_inst->fb_camera_freeze_start_addr,
								CAMERA_STRIDE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the read side of the camera freeze VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	// Start Camera read side VDMA
	xil_printf("Run camera/camera freeze read channel (VGA).\n\r");
	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_camera_inst, XAXIVDMA_READ);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to start the Camera read side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	// Start Camera Freeze read side VDMA
	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_camera_freeze_inst, XAXIVDMA_READ);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to start the Camera read side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	return PERIPHS_SUCCESS;
}

int periphs_bring_up_input_dma
(
	periphs_t*   p_periphs_inst
)
{
	// Local variables
	int	status = 0;

	xil_printf("david1026: %s:%s(%d) ST xxxxxxxxxxxxxxxxxx\r\n", __FILE__, __func__, __LINE__);

	// park the Read side DMA
	XAxiVdma_StartParking(p_periphs_inst->p_vdma_camera_inst, 0, XAXIVDMA_READ);
	XAxiVdma_StartParking(p_periphs_inst->p_vdma_camera_freeze_inst, 0, XAXIVDMA_READ);

	// Stop the write side DMA
	XAxiVdma_DmaStop(p_periphs_inst->p_vdma_camera_inst, XAXIVDMA_WRITE);
	XAxiVdma_DmaStop(p_periphs_inst->p_vdma_camera_freeze_inst, XAXIVDMA_WRITE);

////	// Reset Write side DMA
//	vdma_reset(p_periphs_inst->p_vdma_camera_inst , XAXIVDMA_WRITE); // Reset write channel
//	vdma_reset(p_periphs_inst->p_vdma_camera_freeze_inst , XAXIVDMA_WRITE); // Reset write channel
////	xil_printf("DMA Reset Done\n\r");
//
//	status = framebuffer_write(	p_periphs_inst->p_vdma_camera_inst,
//								16,
//								p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
//								p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
//								p_periphs_inst->fb_camera_start_addr,
//								CAMERA_STRIDE);
//	if (status != XST_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to configure the write side of the camera VDMA.\n\r");
//		return FRAMEBUFFER_ERROR_UNKNOWN;
//	}
//	// Setup camera freeze write channel
//	status = framebuffer_write(	p_periphs_inst->p_vdma_camera_freeze_inst,
//								16,
//								p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo,
//								p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo,
//								p_periphs_inst->fb_camera_freeze_start_addr,
//								CAMERA_STRIDE);
//	if (status != XST_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to configure the write side of the camera freeze VDMA.\n\r");
//		return FRAMEBUFFER_ERROR_UNKNOWN;
//	}
//
	// Start Write side DMA
	xil_printf("david1030: %s:%s(%d) ST xxxxxxxxxxxxxxxxxx\r\n", __FILE__, __func__, __LINE__);
	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_camera_inst, XAXIVDMA_WRITE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to start the Camera write side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	xil_printf("david1030: %s:%s(%d) ST xxxxxxxxxxxxxxxxxx\r\n", __FILE__, __func__, __LINE__);
	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_camera_freeze_inst, XAXIVDMA_WRITE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to start the Camera freeze write side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	// Unpark read side DMA
	XAxiVdma_StopParking(p_periphs_inst->p_vdma_camera_inst, XAXIVDMA_READ);
	XAxiVdma_StopParking(p_periphs_inst->p_vdma_camera_freeze_inst, XAXIVDMA_READ);




	return PERIPHS_SUCCESS;
}

/******************************************************************************/
/**
*
* This is the interrupt handler routine for the scutimer
*
* @param	CallbackRef is the Callback reference for the handler.
*
* @return	None.
*
* @note		None.
*
******************************************************************************/
void scutimer_IntrHandler(void *CallbackRef)
{
	//XScuTimer *scutimer_Ptr = (XScu *)CallbackRef;

	g_ms_uptime++;

	// This interrupt is triggered often, therefore must be very fast, don't do too much here
	g_ms_tick++;

	if((g_ms_tick % 1000) == 0)
		flag_update_RTC_status = 1;
	else if((g_ms_tick % 1000) == 200)
	{
		//if(flag_camera_video_status == 0)
			flag_update_dongle_status = 1;
	}

	/*	for usb debug
	else if((g_ms_tick % 1200) == 400)
	{
		update_usb_status = 1;
	}
	else if((g_ms_tick % 1200) == 800)
	{
		update_usb_descriptor_status = 1;
	}
	*/

	// Clear the Interrupt
	XScuTimer_ClearInterruptStatus((XScuTimer *)CallbackRef);

}


//-----------------------------------------------------        JACKY121212       --------------------------
/******************************************************************************/
/**
*
* This function performs the GPIO set up for Interrupts
*
* @param	IntcInstancePtr is a reference to the Interrupt Controller
*		driver Instance
* @param	InstancePtr is a reference to the GPIO driver Instance
* @param	DeviceId is the XPAR_<GPIO_instance>_DEVICE_ID value from
*		xparameters.h
* @param	IntrId is XPAR_<INTC_instance>_<GPIO_instance>_IP2INTC_IRPT_INTR
*		value from xparameters.h
* @param	IntrMask is the GPIO channel mask
*
* @return	XST_SUCCESS if the Test is successful, otherwise XST_FAILURE
*
* @note		None.
*
******************************************************************************/
int GpioSetupIntrSystem(INTC *IntcInstancePtr, XGpio *InstancePtr,
			u16 DeviceId, u16 IntrId, u16 IntrMask)
{
	int Result;

	GlobalIntrMask = IntrMask;

					XScuGic_Config *IntcConfig;

					/*
					 * Initialize the interrupt controller driver so that it is ready to
					 * use.
					 */
					xil_printf("XPAR_INTC_0_DEVICE_ID/TESTAPP_GEN 3\n\r");
					xil_printf("XScuGic_LookupConfig\n\r");
					xil_printf("====================XScuGic_LookupConfig DeviceId=%d\n\r", INTC_DEVICE_ID);
					IntcConfig = XScuGic_LookupConfig(INTC_DEVICE_ID);
					if (NULL == IntcConfig) {
						return XST_FAILURE;
					}

					xil_printf("XScuGic_CfgInitialize--BLOCK scutimer_IntrHandler---------------------\n\r");
					xil_printf("=====XScuGic_CfgInitialize: IntcConfig=%8x,IntcConfig->CpuBaseAddress=%8x=====\n\r", IntcConfig,IntcConfig->CpuBaseAddress);
					Result = XScuGic_CfgInitialize(IntcInstancePtr, IntcConfig,
									IntcConfig->CpuBaseAddress);

					if (Result != XST_SUCCESS) {
						return XST_FAILURE;
					}

					xil_printf("XScuGic_SetPriorityTriggerType\n\r");
					XScuGic_SetPriorityTriggerType(IntcInstancePtr, IntrId,	0xA0, 0x3);

					/*
					 * Connect the interrupt handler that will be called when an
					 * interrupt occurs for the device.
					 */
					xil_printf("XScuGic_Connect\n\r");
					Result = XScuGic_Connect(IntcInstancePtr, IntrId,
								 (Xil_ExceptionHandler)GpioHandler, InstancePtr);
					if (Result != XST_SUCCESS) {
						return Result;
					}

					/* Enable the interrupt for the GPIO device.*/
					XScuGic_Enable(IntcInstancePtr, IntrId);

	/*
	 * Enable the GPIO channel interrupts so that push button can be
	 * detected and enable interrupts for the GPIO device
	 */
	XGpio_InterruptEnable(InstancePtr, IntrMask);
	XGpio_InterruptGlobalEnable(InstancePtr);

	/*
	 * Initialize the exception table and register the interrupt
	 * controller handler with the exception table
	 */
	Xil_ExceptionInit();

	Xil_ExceptionRegisterHandler(XIL_EXCEPTION_ID_INT,
			 (Xil_ExceptionHandler)INTC_HANDLER, IntcInstancePtr);

	/* Enable non-critical exceptions */
	Xil_ExceptionEnable();

	return XST_SUCCESS;
}
/******************************************************************************/
/**
*
* This function disables the interrupts for the GPIO
*
* @param	IntcInstancePtr is a pointer to the Interrupt Controller
*		driver Instance
* @param	InstancePtr is a pointer to the GPIO driver Instance
* @param	IntrId is XPAR_<INTC_instance>_<GPIO_instance>_VEC
*		value from xparameters.h
* @param	IntrMask is the GPIO channel mask
*
* @return	None
*
* @note		None.
*
******************************************************************************/
void GpioDisableIntr(INTC *IntcInstancePtr, XGpio *InstancePtr,
			u16 IntrId, u16 IntrMask)
{
	XGpio_InterruptDisable(InstancePtr, IntrMask);
#ifdef XPAR_INTC_0_DEVICE_ID
	XIntc_Disable(IntcInstancePtr, IntrId);
#else
	/* Disconnect the interrupt */
	XScuGic_Disable(IntcInstancePtr, IntrId);
	XScuGic_Disconnect(IntcInstancePtr, IntrId);
#endif
	return;
}

//--------------------------JACKY ADD------------------------------------------
/******************************************************************************/
/**
*
* This function  performs a test on the GPIO driver/device with the GPIO
* configured as INPUT
*
* @param	DeviceId is the XPAR_<GPIO_instance>_DEVICE_ID value from
*		xparameters.h
* @param	DataRead is the pointer where the data read from GPIO Input is
*		returned
*
* @return
*		- XST_SUCCESS if the Test is successful
*		- XST_FAILURE if the test is not successful
*
* @note	  	None.
*
******************************************************************************/
int GpioInputExample(u16 DeviceId, u32 *DataRead)
{
	 int Status;
     #define LED_CHANNEL 1

	 /*
	  * Initialize the GPIO driver so that it's ready to use,
	  * specify the device ID that is generated in xparameters.h
	  */
	 Status = XGpio_Initialize(&GpioInput, DeviceId);
	 if (Status != XST_SUCCESS) {
		  return XST_FAILURE;
	 }

	 /* Set the direction for all signals to be inputs */
	 XGpio_SetDataDirection(&GpioInput, LED_CHANNEL, 0xFFFFFFFF);

	 /* Read the state of the data so that it can be  verified */
	 *DataRead = XGpio_DiscreteRead(&GpioInput, LED_CHANNEL);

	 return XST_SUCCESS;

}

/******************************************************************************/
/**
*
* This function  performs a test on the GPIO driver/device with the GPIO
* configured as INPUT
*
* @param	DeviceId is the XPAR_<GPIO_instance>_DEVICE_ID value from
*		xparameters.h
* @param	DataRead is the pointer where the data read from GPIO Input is
*		returned
*
* @return
*		- XST_SUCCESS if the Test is successful
*		- XST_FAILURE if the test is not successful
*
* @note	  	None.
*
******************************************************************************/
//int GpioInputExample(u16 DeviceId, u32 *DataRead)  //JACKY2020
int GpioInput_Total_calc_Graylevel(u16 DeviceId, u32 *DataReadLW, u32 *DataReadSW)
{
	 int Status;
     #define LED_CHANNEL 1

	 /*
	  * Initialize the GPIO driver so that it's ready to use,
	  * specify the device ID that is generated in xparameters.h
	  */
	 Status = XGpio_Initialize(&GpioInput, DeviceId);
	 if (Status != XST_SUCCESS) {
		  return XST_FAILURE;
	 }

	 /* Set the direction for all signals to be inputs */
	 XGpio_SetDataDirection(&GpioInput, 1, 0xFFFFFFFF);
	 XGpio_SetDataDirection(&GpioInput, 2, 0xFFFFFFFF);

	 /* Read the state of the data so that it can be  verified */
	 *DataReadLW = XGpio_DiscreteRead(&GpioInput, 1);
	 *DataReadSW = XGpio_DiscreteRead(&GpioInput, 2);

	 return XST_SUCCESS;

}
/******************************************************************************/
/**
*
* This is the entry function from the TestAppGen tool generated application
* which tests the interrupts when enabled in the GPIO
*
* @param	IntcInstancePtr is a reference to the Interrupt Controller
*		driver Instance
* @param	InstancePtr is a reference to the GPIO driver Instance
* @param	DeviceId is the XPAR_<GPIO_instance>_DEVICE_ID value from
*		xparameters.h
* @param	IntrId is XPAR_<INTC_instance>_<GPIO_instance>_IP2INTC_IRPT_INTR
*		value from xparameters.h
* @param	IntrMask is the GPIO channel mask
* @param	DataRead is the pointer where the data read from GPIO Input is
*		returned
*
* @return
*		- XST_SUCCESS if the Test is successful
*		- XST_FAILURE if the test is not successful
*
* @note		None.
*
******************************************************************************/
int GpioIntrExample(INTC *IntcInstancePtr, XGpio* InstancePtr, u16 DeviceId,
			u16 IntrId, u16 IntrMask)
{
	int Status;

    //Status = GpioIntrExample(&intc, &video_path_camera_in_CDR_VIdeo_In_AXI4_rdy_CDR_Registers_axi_gpio_NFrameReady_Gpio, \
                             XPAR_VIDEO_PATH_CAMERA_IN_CDR_VIDEO_IN_AXI4_RDY_CDR_REGISTERS_AXI_GPIO_NFRAMESREADY_DEVICE_ID, \
                             XPAR_FABRIC_VIDEO_PATH_CAMERA_IN_CDR_VIDEO_IN_AXI4_RDY_CDR_REGISTERS_AXI_GPIO_NFRAMESREADY_IP2INTC_IRPT_INTR, \
                             GPIO_CHANNEL1);

	/* Initialize the GPIO driver. If an error occurs then exit */
	Status = XGpio_Initialize(InstancePtr, DeviceId);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	//Bock scutimer_IntrHandler JACKY1126
	Status = GpioSetupIntrSystem(IntcInstancePtr, InstancePtr, DeviceId,
					IntrId, IntrMask);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	//IntrFlag = 0;
	/*delay = 0;

	while(!IntrFlag && (delay < INTR_DELAY)) {
		delay++;
	}*/

	//GpioDisableIntr(IntcInstancePtr, InstancePtr, IntrId, IntrMask);
	//*DataRead = IntrFlag;

	return Status;
}

/*****************************************************************************/
/**
*
* This function does a minimal test on the GPIO device configured as OUTPUT
* and driver as a example.
*
*
* @param	DeviceId is the XPAR_<GPIO_instance>_DEVICE_ID value from
*		xparameters.h
* @param	GpioWidth is the width of the GPIO
*
* @return
*		- XST_SUCCESS if successful
*		- XST_FAILURE if unsuccessful
*
* @note		None
*
****************************************************************************/
int GpioOutputExample(u16 DeviceId, u32 GpioWidth, u8 FrameReadyCount)
{
	volatile int Delay;
	int Status;

	/*
	 * Initialize the GPIO driver so that it's ready to use,
	 * specify the device ID that is generated in xparameters.h
	 */
	 Status = XGpio_Initialize(&GpioOutput, DeviceId);
	 if (Status != XST_SUCCESS)  {
		  return XST_FAILURE;
	 }
	 xil_printf("JACKY1111: %s:%s(%d) Set the direction for all signals to be outputs\r\n",__FILE__,__func__,__LINE__);
	 /* Set the direction for all signals to be outputs */
	 XGpio_SetDataDirection(&GpioOutput, LED_CHANNEL, 0x0);

	 //FrameReadyCount=200;
     xil_printf("JACKY1111: %s:%s(%d) Set the GPIO outputs to FrameReadyCount=%d\r\n",__FILE__,__func__,__LINE__, FrameReadyCount);
	 /* Set the GPIO outputs to low */
	 XGpio_DiscreteWrite(&GpioOutput, LED_CHANNEL, FrameReadyCount);



	 return XST_SUCCESS;

}

/*****************************************************************************/
/**
*
* This function does a minimal test on the GPIO device configured as OUTPUT
* and driver as a example.
*
*
* @param	DeviceId is the XPAR_<GPIO_instance>_DEVICE_ID value from
*		xparameters.h
* @param	GpioWidth is the width of the GPIO
*
* @return
*		- XST_SUCCESS if successful
*		- XST_FAILURE if unsuccessful
*
* @note		None
*
****************************************************************************/
int GpioOutput_graylevel_axis_Write(u16 DeviceId, u32 graylevel_axis_Write_left_top, u32 graylevel_axis_Write_right_down)
{
	int Status;

	//xil_printf("GpioOutput_graylevel_axis_Write id = %d, data : 0x%08x 0x%08x\r\n", DeviceId, graylevel_axis_Write_left_top, graylevel_axis_Write_right_down);
	/*
	 * Initialize the GPIO driver so that it's ready to use,
	 * specify the device ID that is generated in xparameters.h
	 */
	 Status = XGpio_Initialize(&GpioOutput, DeviceId);
	 if (Status != XST_SUCCESS)  {
		  return XST_FAILURE;
	 }
	 //xil_printf("JACKY1111: %s:%s(%d) Set the direction for all signals to be outputs\r\n",__FILE__,__func__,__LINE__);
	 /* Set the direction for all signals to be outputs */
	 //CHANNEL 1
	 XGpio_SetDataDirection(&GpioOutput, 1, 0x0);
	 //CHANNEL 2
	 XGpio_SetDataDirection(&GpioOutput, 2, 0x0);

	 //FrameReadyCount=200;
     //xil_printf("JACKY1111: %s:%s(%d) Set the GPIO outputs to graylevel_axis_Write = 0x%08x\r\n",__FILE__,__func__,__LINE__, graylevel_axis_Write_left_top);
	 /* Set the GPIO outputs to low */
	 XGpio_DiscreteWrite(&GpioOutput, 1, graylevel_axis_Write_left_top);
     //xil_printf("JACKY1111: %s:%s(%d) Set the GPIO outputs to graylevel_axis_Write = 0x%08x\r\n",__FILE__,__func__,__LINE__, graylevel_axis_Write_right_down);
	 /* Set the GPIO outputs to low */
	 XGpio_DiscreteWrite(&GpioOutput, 2, graylevel_axis_Write_right_down);

	 return XST_SUCCESS;
}

int gray_monitor(u32 LSW_axisx, u32 LSW_axisy, u32 SSW_axisx, u32 SSW_axisy)
{
	u32 status, i;
	u32 DataReadLW, DataReadSW, LSW_Tpixels, SSW_Tpixels;

	xil_printf("gray_monitor %d %d %d %d\n\r", LSW_axisx, LSW_axisy, SSW_axisx, SSW_axisy);

	LSW_Tpixels=LSW_axisx*LSW_axisy;
	SSW_Tpixels=SSW_axisx*SSW_axisy;
	  //xil_printf("\r\n----------gray_monitor: LSW_axisx=%d, LSW_axisy=%d, LSW_Tpixels=%d----------\r\n", LSW_axisx, LSW_axisy, LSW_Tpixels);
	  //xil_printf("\r\n----------gray_monitor: SSW_axisx=%d, SSW_axisy=%d, SSW_Tpixels=%d----------\r\n", SSW_axisx, SSW_axisy, SSW_Tpixels);

	for(i=0;i<10;i++) {
		status = GpioInput_Total_calc_Graylevel(XPAR_VIDEO_PATH_CAMERA_IN_CDR_VIDEO_IN_AXI4_RDY_CDR_REGISTERS_AXI_GPIO_OTOTAL_CALC_LSW_GRAYLEVEL_DEVICE_ID, &DataReadLW, &DataReadSW);

		if (status == 0) {
			  xil_printf("gray_monitor: AverageGraylevel_LW = %d, AverageGraylevel_SW = %d\t[DataReadLW:DataReadSW = 0x%08x:0x%08x]\r\n", DataReadLW/LSW_Tpixels, DataReadSW/SSW_Tpixels, DataReadLW, DataReadSW);
		}
		else {
		   print("GpioInputExample FAILED.\r\n");
		}
	}

	return XST_SUCCESS;

}

int get_gray_value(u32 x_st, u32 y_st, u32 W, u32 H)
{
	int axis_right_top, axis_left_dwon;

	xil_printf("get_gray_value x_st = %d y _st = %d W = %d H = %d, result :", x_st, y_st, W, H);

	x_st += 1;
	y_st += 1;

	axis_right_top = (x_st << 16) | y_st;
	axis_left_dwon = ((x_st + W - 1) << 16) | (y_st + H - 1);
	GpioOutput_graylevel_axis_Write(XPAR_VIDEO_PATH_CAMERA_IN_CDR_VIDEO_IN_AXI4_RDY_CDR_REGISTERS_AXI_GPIO_OTOTAL_CALC_LSW_GRAYLEVEL_AXIS_WRITE_DEVICE_ID, axis_right_top, axis_left_dwon );
	usleep(100000);
	//sleep(1);

	u32 status, i;
	u32 DataReadLW, DataReadSW, total_pixels;

	total_pixels = W * H;


	for(i=0;i<10;i++) {
		status = GpioInput_Total_calc_Graylevel(XPAR_VIDEO_PATH_CAMERA_IN_CDR_VIDEO_IN_AXI4_RDY_CDR_REGISTERS_AXI_GPIO_OTOTAL_CALC_LSW_GRAYLEVEL_DEVICE_ID, &DataReadLW, &DataReadSW);

		if (status == 0) {
			  xil_printf(" %d", DataReadSW / total_pixels);
		}
		else {
		   print("GpioInputExample FAILED.\r\n");
		}
	}
	xil_printf("\n\r");

	return XST_SUCCESS;

}

/******************************************************************************/
/**
*
* This is the interrupt handler routine for the GPIO for this example.
*
* @param	CallbackRef is the Callback reference for the handler.
*
* @return	None.
*
* @note		None.
*
******************************************************************************/

int int_cnt = 0;
void GpioHandler(void *CallbackRef)
{
	XGpio *GpioPtr = (XGpio *)CallbackRef;

	IntrFlag = 1;

    //xil_printf("IntrFlag=%d+++++++++++++++++++++++++             GpioHandler            +++++++++++++++++++++++\r\n", IntrFlag);

    flag_update_dongle_status = 1;

	//xil_printf("ping.[flag_update_dongle_status=%d; flag_battery_fail=%d;flag_engineering_mode=%d; flag_camera_access=%d]-----\n\r", flag_update_dongle_status, flag_battery_fail, flag_engineering_mode, flag_camera_access);//JACKY1125

	// Clear the Interrupt
	XGpio_InterruptClear(GpioPtr, GlobalIntrMask);


	int_cnt++;
	int video_status = 0;
    u32 status;
    u32 DataRead;
    status = GpioInputExample(XPAR_VIDEO_PATH_CAMERA_IN_CDR_VIDEO_IN_AXI4_RDY_CDR_REGISTERS_AXI_GPIO_NFRAMESREADY_DEVICE_ID, &DataRead);
    if (status == 0) {
       //xil_printf("GpioInputExample PASSED. Read data:0x%X\r\n", DataRead);
       video_status = DataRead;
       if(video_status == 1)
    	   xil_printf("\n\r _ON_%d\n\r", int_cnt);
       else
    	   xil_printf("\n\r _OFF_%d\n\r", int_cnt);
    }
    else {
       //print("GpioInputExample FAILED.\r\n");
       video_status = 0;
    }
    flag_camera_video_status = video_status;

    return;
}


