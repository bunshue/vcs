
// *****************************************************
// Dependencies
// *****************************************************
#include "periphs.h"
#include "sleep.h"
#include "main.h"
//#include "xuartps.h"

#define LOCK_MONITOR 1

uint32_t g_procedure_started = 0;


// *****************************************************
// Private data
// *****************************************************

// Subcore instantiations
//static XGpio         vid_mux_sel_gpio_inst;
static XGpioPs		 ps_gpio_inst;
static XGpio         lock_monitor_inst;
static XScuGic		 scugic_inst;
static XScuTimer     scutimer_inst;
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
	unsigned int psuart0_device_id,
	//unsigned int vid_mux_sel_gpio_device_id,
	//unsigned int vtd_device_id,
	//unsigned int tpg_old_device_id,
	unsigned int tpg_GUI_device_id,
	//unsigned int scaler_camera_device_id,
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
	XUartPs_Config*	 p_psuart0_cfg;
	//XVtc_Config*     p_vtd_cfg;
	XV_tpg_Config*   p_tpg_GUI_cfg;
	//XVprocSs_Config* p_vpss_camera_cfg;
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

	xil_printf("\n\r\n\rdavid0706: %s:%s(%d) ST\r\n",__FILE__,__func__,__LINE__);

	xil_printf("\n\r---PS GPIO for front panel 0xE000A000-----------------------------------------\n\r");
	// Initialize PS GPIO drivers
	xil_printf("Initializing PS GPIO.\n\r");
	//											0
	p_ps_gpio_cfg = XGpioPs_LookupConfig(ps_gpio_device_id);
	if (p_ps_gpio_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find PS GPIO.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	xil_printf("david0710: %s:%s(%d) ST\r\n",__FILE__,__func__,__LINE__);
	status = XGpioPs_CfgInitialize(p_periphs_inst->p_ps_gpio_inst, p_ps_gpio_cfg, p_ps_gpio_cfg->BaseAddr);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize the PS GPIO.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}

	xil_printf("david0704: %s:%s(%d) XGpioPs base address = 0x%x\r\n",__FILE__,__func__,__LINE__,p_ps_gpio_cfg->BaseAddr);

	xil_printf("\n\r---Video lock monitor 0x41200000-----------------------------------------\n\r");

	// Initialize Video lock monitor (GPIO) drivers
	xil_printf("Initializing video lock monitor GPIO.\n\r");
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

	xil_printf("\n\r---interrupt controller 0xF8F00100-----------------------------------------\n\r");
	// Initialize the interrupt controller
	p_scugic_cfg = XScuGic_LookupConfig(scugic_device_id);
	if (NULL == p_scugic_cfg)
	{
		xil_printf("ERROR! Failed to find scugic.\n\r");
		return XST_FAILURE;
	}

	status = XScuGic_CfgInitialize(p_periphs_inst->p_scugic_inst, p_scugic_cfg, p_scugic_cfg->CpuBaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize scugic.\n\r");
		return XST_FAILURE;
	}
	xil_printf("david0704: %s:%s(%d) XScuGic base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_scugic_cfg->CpuBaseAddress);

	xil_printf("\n\r---CPU private timer SCUTimer 0xF8F00600-----------------------------------------\n\r");
	// Initialize the CPU private timer
	p_scutimer_cfg = XScuTimer_LookupConfig(scutimer_device_id);	//0
	if (NULL == p_scutimer_cfg) {
		xil_printf("ERROR! Failed to find scutimer.\n\r");
		return XST_FAILURE;
	}

	status = XScuTimer_CfgInitialize(p_periphs_inst->p_scutimer_inst, p_scutimer_cfg, p_scutimer_cfg->BaseAddr);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize scutimer.\n\r");
		return XST_FAILURE;
	}
	xil_printf("david0704: %s:%s(%d) XScuTimer base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_scutimer_cfg->BaseAddr);

	xil_printf("\n\r---UART driver 0xE0000000 for dongle UART 0-----------------------------------------\n\r");

	// Initialize the UART driver so that it's ready to use

	xil_printf("david0712: %s:%s(%d) call XUartPs_LookupConfig with device = %d\r\n",__FILE__,__func__,__LINE__,psuart0_device_id);
	p_psuart0_cfg = XUartPs_LookupConfig(psuart0_device_id);
	if (NULL == p_psuart0_cfg)
	{
		xil_printf("ERROR! Failed to find psuart0.\n\r");
		return XST_FAILURE;
	}

	status = XUartPs_CfgInitialize(p_periphs_inst->p_psuart0_inst, p_psuart0_cfg,p_psuart0_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize psuart0.\n\r");
		return XST_FAILURE;
	}
	xil_printf("david0704: %s:%s(%d) XUartPs base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_psuart0_cfg->BaseAddress);

	xil_printf("\n\r---????? UART 1 for PC comm -----------------------------------------\n\r");


	xil_printf("david0712: %s:%s(%d) call XUartPs_LookupConfig with device = %d\r\n",__FILE__,__func__,__LINE__,XPAR_PS7_UART_1_DEVICE_ID);
	// Get psuart1 config							1
	g_psuart1_config = XUartPs_LookupConfig(XPAR_PS7_UART_1_DEVICE_ID);

	if (NULL == g_psuart1_config)
	{
		xil_printf("ERROR! Failed to find psuart0.\n\r");
		return XST_FAILURE;
	}

	//david: lack a XUartPs_CfgInitialize  ???

	xil_printf("\n\r---GUI TPG drivers 0x43D40000-----------------------------------------\n\r");

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
	xil_printf("david0704: %s:%s(%d) GUI TPG base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_tpg_GUI_cfg->BaseAddress);

	//xil_printf("\n\r--------------------------------------------\n\r");

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


	xil_printf("\n\r---Camera Freeze Scaler 0x43D00000 ????-----------------------------------------\n\r");
	xil_printf("Initializing Camera Freeze Scaler.\n\r");
	p_vpss_camera_freeze_cfg = XVprocSs_LookupConfig(scaler_camera_freeze_device_id);	//0
	if (p_vpss_camera_freeze_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find Camera Freeze scaler.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	status = XVprocSs_CfgInitialize(p_periphs_inst->p_scaler_camera_freeze_inst, p_vpss_camera_freeze_cfg, p_vpss_camera_freeze_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize Camera Freeze scaler.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("david0704: %s:%s(%d) Camera Freeze Scaler base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_vpss_camera_freeze_cfg->BaseAddress);

	xil_printf("\n\r---VDMA drivers 0x43000000-----------------------------------------\n\r");

	// Initialize VDMA drivers
	xil_printf("Initializing Camera VDMA.\n\r");
	p_vdma_camera_cfg = XAxiVdma_LookupConfig(vdma_camera_device_id);
	if (p_vdma_camera_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find Camera VDMA.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("david0725: %s:%s(%d) call XAxiVdma_CfgInitialize, base = 0x%x, for VDMA\r\n",__FILE__,__func__,__LINE__, p_vdma_camera_cfg->BaseAddress);
	status = XAxiVdma_CfgInitialize(p_periphs_inst->p_vdma_camera_inst, p_vdma_camera_cfg, p_vdma_camera_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize the Camera VDMA.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("david0704: %s:%s(%d) Camera VDMA base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_vdma_camera_cfg->BaseAddress);

	xil_printf("\n\r---Camera Freeze VDMA 0x43030000-----------------------------------------\n\r");

	xil_printf("Initializing Camera Freeze VDMA.\n\r");
	p_vdma_camera_freeze_cfg = XAxiVdma_LookupConfig(vdma_camera_freeze_device_id);
	if (p_vdma_camera_freeze_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find Camera Freeze VDMA.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("david0725: %s:%s(%d) call XAxiVdma_CfgInitialize, base = 0x%x, for camera freeze\r\n",__FILE__,__func__,__LINE__, p_vdma_camera_freeze_cfg->BaseAddress);
	status = XAxiVdma_CfgInitialize(p_periphs_inst->p_vdma_camera_freeze_inst, p_vdma_camera_freeze_cfg, p_vdma_camera_freeze_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize the Camera Freeze VDMA.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("david0704: %s:%s(%d) Camera Freeze VDMA base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_vdma_camera_freeze_cfg->BaseAddress);
	
	//xil_printf("--------------------------------------------\n\r");

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
	
	xil_printf("\n\r---Video Mixer 0x43CC0000-----------------------------------------\n\r");
	// Initialize Video Mixer driver
	xil_printf("Initializing Video Mixer.\n\r");
	//																				0
	status  = XVMix_Initialize(p_periphs_inst->p_vid_output_mixer_l2_inst, vid_output_mixer_device_id);
	if(status != XST_SUCCESS)
	{
	  xil_printf("ERR:: Mixer device not found\r\n");
	  return(XST_FAILURE);
	}
	//david: lack config?
	
	xil_printf("\n\r---VTG drivers Device 0 0x43C90000 for TFP410-----------------------------------------\n\r");
	// Initialize VTG drivers Device 0
	xil_printf("Initializing VTG_0.\n\r");
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
	xil_printf("david0704: %s:%s(%d) VTG drivers Device 0 base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_vtg_cfg_0->BaseAddress);

	xil_printf("\n\r---VTG drivers Device 1 0x43C80000 for CH7038-----------------------------------------\n\r");

	// Initialize VTG drivers Device 1
	xil_printf("Initializing VTG_1.\n\r");
	p_vtg_cfg_1 = XVtc_LookupConfig(vtg_device_id_1);
	if (p_vtg_cfg_1 == NULL)
	{
		xil_printf("ERROR! Failed to find VTG_1.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	status = XVtc_CfgInitialize(p_periphs_inst->p_vtg_inst_1, p_vtg_cfg_1, p_vtg_cfg_1->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize the VTG_1.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	xil_printf("david0704: %s:%s(%d) VTG drivers Device 1 base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_vtg_cfg_1->BaseAddress);

	xil_printf("\n\r---XUsbPs 0xE0002000-----------------------------------------\n\r");

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
	xil_printf("david0704: %s:%s(%d) XUsbPs base address = 0x%x\r\n\r\n",__FILE__,__func__,__LINE__, p_psusb0_cfg->BaseAddress);

	xil_printf("david0706: %s:%s(%d) SP\n\r\r\n",__FILE__,__func__,__LINE__);

	return PERIPHS_SUCCESS;
}

int test_gpio(periphs_t*   p_periphs_inst)
{
	XGpioPs *Gpio = p_periphs_inst->p_ps_gpio_inst;

	xil_printf("LED test ST\r\n");

	XGpioPs_WritePin(Gpio, GPIO_LED_1, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_2, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_3, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_4, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_5, 0);
	usleep(200000);
    usleep(200000);
	usleep(200000);
    usleep(200000);

	xil_printf("LED 1\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_1, 1);
	usleep(200000);
    usleep(200000);
	usleep(200000);
    usleep(200000);

	xil_printf("LED 2\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_1, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_2, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("LED 3\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_2, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_3, 1);
	usleep(200000);
    usleep(200000);
	usleep(200000);
    usleep(200000);

    xil_printf("LED 4\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_3, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_4, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

    xil_printf("LED 5\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_4, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_5, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("LED 3\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_5, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_3, 1);
	usleep(200000);
    usleep(200000);
	usleep(200000);
    usleep(200000);

	xil_printf("RED LED ON\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_RED, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("RED LED OFF\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_RED, 0);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);


	xil_printf("GPIO_LED_AUTO OFF\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_AUTO, 0);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("GPIO_LED_CEN ON\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_CEN, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("GPIO_LED_CEN OFF\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_CEN, 0);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("GPIO_LED_AVG ON\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_AVG, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("GPIO_LED_AVG OFF\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_AVG, 0);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("GPIO_LED_AUTO ON\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_AUTO, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

    xil_printf("LED test SP\r\n");
    return 0;
}



// *****************************************************
// Public functions
// *****************************************************
int periphs_init
(
	periphs_t*   p_periphs_inst,
	unsigned int ps_gpio_device_id,		//0
	unsigned int video_lock_device_id,	//0
	unsigned int scugic_device_id,		//0
	unsigned int scutimer_device_id,	//0
	unsigned int psuart0_device_id,		//0
	//unsigned int vid_mux_sel_gpio_device_id,
	//unsigned int fmc_imageon_iic_base_addr,
	//unsigned int si570_iic_device_id,
	//unsigned int vtd_device_id,
	unsigned int tpg_GUI_device_id,		//0
	//unsigned int scaler_camera_device_id,
	unsigned int scaler_camera_freeze_device_id,	//0
	unsigned int vdma_camera_device_id,				//0
	unsigned int vdma_camera_freeze_device_id,		//1
	//unsigned int vdma_GUI_device_id,
	unsigned int vid_output_mixer_device_id,		//0
	unsigned int vtg_device_id_0,		//1
	unsigned int vtg_device_id_1,		//0
	unsigned int psusb0_device_id,		//0
	unsigned int fb_camera_start_addr,			//0x3210_0000
	unsigned int fb_camera_freeze_start_addr,	//0x3250_0000
	unsigned int fb_GUI_start_addr				//0x3010_0000
)
{
	// Local variables
	int status = 0;
	u32 IntrMask = 0;
	//u32 Index = 0;
	//u32 BadByteCount = 0;


	xil_printf("david0628: %s:%s(%d) ST\r\n",__FILE__,__func__,__LINE__);
	xil_printf("\tps_gpio_device_id = %u\r\n", ps_gpio_device_id);		//0
	xil_printf("\tvideo_lock_device_id = %u\r\n", video_lock_device_id);
	xil_printf("\tscugic_device_id = %u\r\n", scugic_device_id);		//0
	xil_printf("\tscutimer_device_id = %u\r\n", scutimer_device_id);	//0
	xil_printf("\tpsuart0_device_id = %u\r\n", psuart0_device_id);		//0
	xil_printf("\ttpg_GUI_device_id = %u\r\n", tpg_GUI_device_id);
	xil_printf("\tscaler_camera_freeze_device_id = %u\r\n", scaler_camera_freeze_device_id);
	xil_printf("\tvdma_camera_device_id = %u\r\n", vdma_camera_device_id);
	xil_printf("\tvdma_camera_freeze_device_id = %u\r\n", vdma_camera_freeze_device_id);
	xil_printf("\tvid_output_mixer_device_id = %u\r\n", vid_output_mixer_device_id);
	xil_printf("\tvtg_device_id_0 = %u\r\n", vtg_device_id_0);
	xil_printf("\tvtg_device_id_1 = %u\r\n", vtg_device_id_1);
	xil_printf("\tpsusb0_device_id = %u\r\n", psusb0_device_id);
	xil_printf("\tfb_camera_start_addr = 0x%x\r\n", fb_camera_start_addr);
	xil_printf("\tfb_camera_freeze_start_addr = 0x%x\r\n", fb_camera_freeze_start_addr);
	xil_printf("\tfb_GUI_start_addr = 0x%x\r\n", fb_GUI_start_addr);
	
	// Attach subcore instances to object
	//p_periphs_inst->p_vid_mux_sel_gpio_inst = &vid_mux_sel_gpio_inst;
	//p_periphs_inst->p_vtd_inst              	= &vtd_inst;
	p_periphs_inst->p_ps_gpio_inst				= &ps_gpio_inst;
	p_periphs_inst->p_lock_monitor_inst			= &lock_monitor_inst;
	p_periphs_inst->p_scugic_inst				= &scugic_inst;
	p_periphs_inst->p_scutimer_inst				= &scutimer_inst;
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
		psuart0_device_id,
		//vid_mux_sel_gpio_device_id,
		//vtd_device_id,
		//tpg_old_device_id,
		tpg_GUI_device_id,
		//scaler_camera_device_id,
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

	// Video Path Config
	xil_printf("\n\r\n\rVideo Path Config\n\r");
	xil_printf("david0724: %s:%s(%d) call\t",__FILE__,__func__,__LINE__);
	xil_printf("Bringing up input pipeline.\n\r");
	periphs_bring_up_input_pipeline(p_periphs_inst);

	xil_printf("\n\rdavid0724: %s:%s(%d) call\t",__FILE__,__func__,__LINE__);
	xil_printf("Bringing up output pipeline.\n\r");
	periphs_bring_up_output_pipeline(p_periphs_inst, VIDEO_RESOLUTION_1080P, fb_GUI_start_addr);

	// Control Path Config
	xil_printf("\n\r\n\rControl Path Config\n\r");
	xil_printf("david0703: %s:%s(%d) call periphs_configure_gpio_pins, setup gpio\r\n",__FILE__,__func__,__LINE__);
	periphs_configure_gpio_pins(p_periphs_inst); // Set up GPIO Pins

	// Set up Exception Handler
	//Xil_ExceptionInit(); // Obsolete, used to maintain backward compatibility

	// Connect the interrupt controller interrupt handler to the hardware interrupt handling logic in the processor.
	Xil_ExceptionRegisterHandler(XIL_EXCEPTION_ID_INT,
				(Xil_ExceptionHandler)XScuGic_InterruptHandler,
				p_periphs_inst->p_scugic_inst);

	// SCUTIMER - Connect the device driver handler that will be called when an interrupt for the device occurs
	status = XScuGic_Connect(p_periphs_inst->p_scugic_inst, XPAR_SCUTIMER_INTR,
				(Xil_ExceptionHandler)scutimer_IntrHandler, p_periphs_inst->p_scutimer_inst);
	if (status != XST_SUCCESS) {
		xil_printf("failed to connect scutimer\r\n");
		return status;
	}

	// Reset/Stop scutimer
	xil_printf("\n\r\n\rReset/Stop scutimer\n\r");
	xil_printf("david0712: %s:%s(%d) timer\r\n",__FILE__,__func__,__LINE__);
	XScuTimer_Stop(p_periphs_inst->p_scutimer_inst);
	XScuTimer_DisableInterrupt(p_periphs_inst->p_scutimer_inst);
	XScuTimer_ClearInterruptStatus(p_periphs_inst->p_scutimer_inst);

	// Load scutimer values
	XScuTimer_LoadTimer(p_periphs_inst->p_scutimer_inst, COUNTS_PER_MILLI_SECOND);
	XScuTimer_RestartTimer(p_periphs_inst->p_scutimer_inst);
	XScuTimer_SetPrescaler(p_periphs_inst->p_scutimer_inst, 1);
	XScuTimer_EnableAutoReload(p_periphs_inst->p_scutimer_inst);
	XScuTimer_EnableInterrupt(p_periphs_inst->p_scutimer_inst);
	XScuTimer_Start(p_periphs_inst->p_scutimer_inst);

	// Enable the scugic interrupt for the scutimer.
	XScuGic_Enable(p_periphs_inst->p_scugic_inst, XPAR_SCUTIMER_INTR);

	xil_printf("\n\r\n\rDongle setup, use UART0\n\r");
	// psuart0 - Connect the device driver handler that will be called when an interrupt for the device occurs
	// Print UART settings
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

	xil_printf("\n\rdavid0709: %s:%s(%d) ST BaudRate =%d call XUartPs_SetBaudRate 333\r\n",__FILE__,__func__,__LINE__, XUARTPS_DFT_BAUDRATE);
	//maybe the same
	XUartPs_SetBaudRate(p_periphs_inst->p_psuart0_inst, XUARTPS_DFT_BAUDRATE);
	xil_printf("\r\n");


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

	xil_printf("psuart0 baudrate: %d\r\n", p_periphs_inst->p_psuart0_inst->BaudRate);
	xil_printf("psuart0 callback: 0x%x\r\n", p_periphs_inst->p_psuart0_inst->CallBackRef);
	xil_printf("psuart0 clock: %d\r\n", p_periphs_inst->p_psuart0_inst->InputClockHz);
	xil_printf("psuart0 ready: %d\r\n", p_periphs_inst->p_psuart0_inst->IsReady);
	xil_printf("psuart0 platform: %d\r\n", p_periphs_inst->p_psuart0_inst->Platform);
	xil_printf("psuart0 rxbs_errot: %d\r\n", p_periphs_inst->p_psuart0_inst->is_rxbs_error);

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
	xil_printf("david0702: %s:%s(%d) ST get status\r\n",__FILE__,__func__,__LINE__);
	status = XScuGic_Connect(p_periphs_inst->p_scugic_inst, XPAR_XGPIOPS_0_INTR,
				(Xil_ExceptionHandler)XGpioPs_IntrHandler, p_periphs_inst->p_ps_gpio_inst);
	xil_printf("david0702: %s:%s(%d) ST get status = 0x%x\r\n",__FILE__,__func__,__LINE__,status);
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

	xil_printf("\n\r\n\rLock Monitor\n\r");
	// Lock Monitor - Connect the device driver handler that will be called when an interrupt for the device occurs
	// The handler defined above performs the specific interrupt processing for the device.
	// Use XPS define due to bug in generated x_parameter.h
	status = XScuGic_Connect(p_periphs_inst->p_scugic_inst, XPS_FPGA10_INT_ID,
				(Xil_ExceptionHandler)lock_monitor_IntrHandler, p_periphs_inst->p_lock_monitor_inst);
	if (status != XST_SUCCESS) {
		xil_printf("failed to connect lock monitor\r\n");
		return status;
	}

	/*
	 * Enable the GPIO channel interrupts so that lock monitor can be
	 * detected and enable interrupts for the GPIO device
	 */
	XGpio_InterruptEnable(p_periphs_inst->p_lock_monitor_inst, XGPIO_IR_CH1_MASK);
	XGpio_InterruptGlobalEnable(p_periphs_inst->p_lock_monitor_inst);

	//Only used for edge sensitive Interrupts
	XScuGic_SetPriorityTriggerType(p_periphs_inst->p_scugic_inst, XPS_FPGA10_INT_ID, 0x98, 1);

	// Enable the interrupt for the lock monitor device.
	XScuGic_Enable(p_periphs_inst->p_scugic_inst, XPS_FPGA10_INT_ID);

	// Connect USB to SCUGIC
	// Remaining parts are in TinyUSB HAL
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

	xil_printf("david0724: %s:%s(%d) SP\r\n",__FILE__,__func__,__LINE__);

	return PERIPHS_SUCCESS;
}

int periphs_get_fmc_status
(
	periphs_t* p_periphs_inst
)
{
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
	//int status = 0;

	xil_printf("david0713: %s:%s(%d) ST XXXXXXXXXXXXXXXXXX\r\n",__FILE__,__func__,__LINE__);

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

int periphs_toggle_GUI_tpg(periphs_t* p_periphs_inst)
{
	//p_periphs_inst->bypass_tpg = PERIPHS_SEL_BYPASS_TPG;
	//xil_printf(">>>>>Always Bypassing TPG.\n\r");

	// Local variables
	//int status = 0;
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
		p_periphs_inst->bypass_GUI_tpg = PERIPHS_SEL_BYPASS_TPG;
		xil_printf(">>>>>Bypassing GUI TPG.\n\r");
	}
	else
	{
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
	xil_printf("Initialize GUI TPG to 1080P.\n\r");
	test_pattern_gen_config
	(
		p_periphs_inst->p_tpg_GUI_inst,
		p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->HActiveVideo,
		p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->VActiveVideo,
		p_periphs_inst->bypass_GUI_tpg,
		0, // Box is red for TPG on new VPSS scaler datapath
		XVIDC_CSF_RGB,
		XTPG_BKGND_COLOR_BARS,
		0  // print regs
	);

	xil_printf("call XV_tpg_EnableAutoRestart\n\r");
	XV_tpg_EnableAutoRestart(p_periphs_inst->p_tpg_GUI_inst);
	xil_printf("call XV_tpg_Start\n\r");
	XV_tpg_Start(p_periphs_inst->p_tpg_GUI_inst);

	// Enable VTD to start letting video in
	//vtiming_det_run(p_periphs_inst->p_vtd_inst);

	return PERIPHS_SUCCESS;
}

int periphs_toggle_camera_freeze_vdma(periphs_t* p_periphs_inst)
{
	// Local variables
	//int status = 0;
	//xil_printf(">++++++Into Park/Un-park Camera Freeze VDMA.\n\r");

	// Determine if we're in TPG or passthrough mode
	if (p_periphs_inst->enable_camera_freeze_vdma == PERIPHS_SEL_ENABLE_PARK)
	{
		p_periphs_inst->enable_camera_freeze_vdma = PERIPHS_SEL_DISABLE_PARK;
		//																		2
		XAxiVdma_StopParking(p_periphs_inst->p_vdma_camera_freeze_inst, XAXIVDMA_READ);

		xil_printf(">>>>>Unpark camera freeze vdma.\n\r");
	}
	else
	{
		p_periphs_inst->enable_camera_freeze_vdma = PERIPHS_SEL_ENABLE_PARK;
		//																		2
		XAxiVdma_StartParking(p_periphs_inst->p_vdma_camera_freeze_inst, 0, XAXIVDMA_READ);
		xil_printf(">>>>>Park camera freeze vdma.\n\r");
	}
	return PERIPHS_SUCCESS;
}

int periphs_configure_gpio_pins(periphs_t*   p_periphs_inst)
{
	// Local variables
	int           status = 0;
	XGpioPs*	  p_gpio;
	XGpio*		  p_lock;

	p_gpio = p_periphs_inst->p_ps_gpio_inst;
	p_lock = p_periphs_inst->p_lock_monitor_inst;

	// Configure PS_GPIO Bank 2
	// Steps must be followed to prevent damage to chip, unused bank pins are set to output and tied to ground.
	xil_printf("david0703: %s:%s(%d) ST Set up PS GPIO.\r\n",__FILE__,__func__,__LINE__);
	xil_printf("Set up PS GPIO.\n\r");
	// bit[10:0], 11 bits - Output
	// bit[17:11], 7 bits - Input
	// bit[31:18], 14 bits - Output, default write value 0
	XGpioPs_SetDirection(p_gpio, XGPIOPS_BANK2, PIN_DIR_DEFAULT); // Direction is 32bit mapped, 0 = input, 1 = output, unused pins are set to output logic 0
	XGpioPs_Write(p_gpio, XGPIOPS_BANK2, PIN_DEF_DEFAULT); // Set to default outputs
	XGpioPs_SetOutputEnable(p_gpio, XGPIOPS_BANK2, PIN_DIR_DEFAULT);

	// Configure Video Lock - TODO
	xil_printf("\n\rSet up Video Lock Monitor.\n\r");
	// bit[3:0], Input
	// 0 - MMCM Locked
	// 1 - TFP410 Locked
	// 2 - CH7038 Locked
	// 3 - Matched K Code
	// Set the direction for all signals as inputs except the LED output */
	XGpio_SetDataDirection(p_lock, LOCK_MONITOR, 0xffff); // 0 = output, 1 = input

	// Debug, just confirm if the data is written to the register
	status = XGpio_GetDataDirection(p_lock, LOCK_MONITOR);
	xil_printf("lock_monitor: %x\r\n", status);

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
	//vres_timing_t vres_timing;
	// Look up timing info from ID
	//vres_get_timing(new_input_timing, &vres_timing);

	// Software Reset Camera/Camera Freeze Input Pipeline
	//
	//
	/////////////////////////////////////////////////////
	//VDMA Write
	xil_printf("david0724: %s:%s(%d) ST\r\n",__FILE__,__func__,__LINE__);
	xil_printf("Reset camera/camera freeze VDMA write channel (VGA).\n\r");
	vdma_reset(p_periphs_inst->p_vdma_camera_inst , XAXIVDMA_WRITE); // Reset write channel
	vdma_reset(p_periphs_inst->p_vdma_camera_freeze_inst , XAXIVDMA_WRITE); // Reset write channel
	// Camera TPG cannot be software reset
	// VTD
//	xil_printf("Reset VTD.\n\r");
//	XVtc_Reset(p_periphs_inst->p_vtd_inst);

	// Configure Camera/Camera Freeze Input Pipeline
	//
	//
	//////////////////////////////////////////////////
	// Setup camera write channel
	xil_printf("Set up camera/camera freeze write channel (VGA).\n\r");
	// Setup camera write channel
	status = framebuffer_write(	p_periphs_inst->p_vdma_camera_inst,
								16,
								p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo,
								p_periphs_inst->p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo,
								p_periphs_inst->fb_camera_start_addr,
								CAMERA_STRIDE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the write side of the camera VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}
	// Setup camera freeze write channel
	status = framebuffer_write(	p_periphs_inst->p_vdma_camera_freeze_inst,
								16,
								p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo,
								p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo,
								p_periphs_inst->fb_camera_freeze_start_addr,
								CAMERA_STRIDE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the write side of the camera freeze VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}


	// VTD - To be implemented, ignore for now

	// Run IP /////////////////////////////////////////
	//
	//
	///////////////////////////////////////////////////
	// Start Camera write side VDMA
	xil_printf("david0724: %s:%s(%d) ST\r\n",__FILE__,__func__,__LINE__);
	xil_printf("Run camera/camera freeze write channel (VGA).\n\r");
	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_camera_inst, XAXIVDMA_WRITE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to start the Camera write side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	// Start Camera Freeze write side VDMA
	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_camera_freeze_inst, XAXIVDMA_WRITE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to start the Camera write side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

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
	//uint32_t *ptr, i;
	//uint32_t i;

	xil_printf("david0724: %s:%s(%d) ST\r\n",__FILE__,__func__,__LINE__);

	// Look up timing info from ID
	vres_get_timing(0, &vres_timing0);
	vres_get_timing(new_output_timing, &vres_timing1);

	// Software Reset Output Pipeline
	//
	//
	/////////////////////////////////////////////////////
	// VTG 0/1 Reset
	xil_printf("Reset VTG 0/1.\n\r");
	vtiming_gen_reset(p_periphs_inst->p_vtg_inst_0);
	vtiming_gen_reset(p_periphs_inst->p_vtg_inst_1);
	// Video Mixer Reset - no software reset, skip
	// GUI TPG cannot be software reset
	// Camera/Camera Freeze VPSS Reset - Already done by cfginitialize
	//VDMA Read
	xil_printf("Reset camera/camera freeze VDMA read channel (VGA).\n\r");
	vdma_reset(p_periphs_inst->p_vdma_camera_inst , XAXIVDMA_READ); // Reset read channel
	vdma_reset(p_periphs_inst->p_vdma_camera_freeze_inst , XAXIVDMA_READ); // Reset read channel
	//vdma_reset(p_periphs_inst->p_vdma_GUI_inst , XAXIVDMA_READ); // Reset read channel

	// Configure Output Pipeline
	//
	//
	//////////////////////////////////////////////////
	// VTG 0 and 1
	xil_printf("Configure VTG 0 and VTG 1.\n\r");
	// Set output frame size for Video Output interface
	vid_io_intf_update_output_fsize(p_periphs_inst->p_vid_io_GUI_inst, new_output_timing);
	// Set VTG_0 output timing
	vtiming_gen_config(p_periphs_inst->p_vtg_inst_0, new_output_timing, 2);
	//vtiming_gen_config(p_periphs_inst->p_vtg_inst_0, 0, 2); // VGA, for test
	// Set VTG_1 output timing
	vtiming_gen_config(p_periphs_inst->p_vtg_inst_1, new_output_timing, 2);

	{
	// Video Mixer Config - set output frame size
	xil_printf("Initialize Video Mixer and settings.\n\r");
	// Set default stream (output, RGB, 8bit/color, 1 pix per clock)
	XVMix_GetLayerColorFormat(p_periphs_inst->p_vid_output_mixer_l2_inst, XVMIX_LAYER_MASTER, &Cfmt);
	// Get resolution ID from frame size
	resId = XVidC_GetVideoModeId(LAYER0_WIDTH, LAYER0_HEIGHT, XVIDC_FR_60HZ, FALSE);
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
    XVMix_DbgReportStatus(p_periphs_inst->p_vid_output_mixer_l2_inst);
    XVMix_DbgLayerInfo(p_periphs_inst->p_vid_output_mixer_l2_inst, XVMIX_LAYER_MASTER);

	}

	// GUI TPG Config - Set to Default 1080P
	xil_printf("Initialize GUI TPG to 1080P.\n\r");
	test_pattern_gen_config
	(
		p_periphs_inst->p_tpg_GUI_inst,
		p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->HActiveVideo,
		p_periphs_inst->p_vid_io_GUI_inst->p_output_timing_inst->VActiveVideo,
		p_periphs_inst->bypass_GUI_tpg,
		0, // Box is red for TPG on new VPSS scaler datapath
		XVIDC_CSF_RGB,
		XTPG_BKGND_SOLID_BLACK,
		//XTPG_BKGND_COLOR_BARS,
		0  // print regs
	);

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
	xil_printf("Setting up Camera Freeze scaler.\n\r");
	status = scaler_new_set_size
	(
		p_periphs_inst->p_scaler_camera_freeze_inst,
		p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo,
		p_periphs_inst->p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo,
		XVIDC_CSF_YCRCB_422,
		p_periphs_inst->p_vid_io_camera_freeze_inst->p_output_timing_inst->HActiveVideo,
		p_periphs_inst->p_vid_io_camera_freeze_inst->p_output_timing_inst->VActiveVideo,
		XVIDC_CSF_YCRCB_422,
		1 // Print configuration
	);
	if (status != SCALER_NEW_SUCCESS)
	{
		xil_printf("ERROR! Failed to set Camera freeze scaler.\n\r");
		return PERIPHS_ERROR_UNKNOWN;
	}
	// VDMA
	// Setup camera read channel
	xil_printf("Set up camera/camera freeze read channel (VGA).\n\r");
	status = framebuffer_read(	p_periphs_inst->p_vdma_camera_inst,
								16,
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
	status = framebuffer_read(	p_periphs_inst->p_vdma_camera_freeze_inst,
								16,
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
	vtiming_gen_start(p_periphs_inst->p_vtg_inst_0);
	vtiming_gen_start(p_periphs_inst->p_vtg_inst_1);

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
	xil_printf("Run GUI TPG (1080P).\n\r");
	XV_tpg_EnableAutoRestart(p_periphs_inst->p_tpg_GUI_inst);
	XV_tpg_Start(p_periphs_inst->p_tpg_GUI_inst);

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

//	// Start GUI read side VDMA
//	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_GUI_inst, XAXIVDMA_READ);
//	if (status != XST_SUCCESS)
//	{
//		xil_printf("ERROR! Failed to start the GUI read side of the VDMA.\n\r");
//		return FRAMEBUFFER_ERROR_UNKNOWN;
//	}

	return PERIPHS_SUCCESS;
}

int periphs_bring_up_output_dma
(
	periphs_t*   p_periphs_inst
)
{
	// Local variables
	int           status = 0;
	//uint32_t *ptr, i;

	//VDMA Read
	xil_printf("Reset camera/camera freeze VDMA read channel (VGA).\n\r");
	//vdma_reset(p_periphs_inst->p_vdma_camera_inst , XAXIVDMA_READ); // Reset read channel
	//vdma_reset(p_periphs_inst->p_vdma_camera_freeze_inst , XAXIVDMA_READ); // Reset read channel

	// VDMA
	// Setup camera read channel
	xil_printf("Set up camera/camera freeze read channel (VGA).\n\r");
	status = framebuffer_read(	p_periphs_inst->p_vdma_camera_inst,
								16,
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
	status = framebuffer_read(	p_periphs_inst->p_vdma_camera_freeze_inst,
								16,
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
	status = XAxiVdma_DmaStart(p_periphs_inst->p_vdma_camera_inst, XAXIVDMA_WRITE);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to start the Camera write side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

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

	// This interrupt is triggered often, therefore must be very fast, don't do too much here
	g_ms_tick++;
	// Got Interrupt, Check which interrupt was signaled
	//xil_printf("scutimer!: %d\r\n", g_ms_tick);

	// Clear the Interrupt
	XScuTimer_ClearInterruptStatus((XScuTimer *)CallbackRef);

}


