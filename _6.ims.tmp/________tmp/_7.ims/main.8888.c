

// *****************************************************
// Dependencies
// *****************************************************
#include <stdio.h>
#include <stdlib.h>
#include "xil_cache.h"
#include "platform.h"
#include "main.h"
#include "xuartps_hw.h"
#include "periphs.h"
#include "mixer.h"
#include "gpio.h"
#include "ulpi.h"


/* global timer registers*/
#define SCU_GLOBAL_TIMER_COUNT_L32	(XPAR_PS7_GLOBALTIMER_0_S_AXI_BASEADDR)
#define SCU_GLOBAL_TIMER_COUNT_U32	(XPAR_PS7_GLOBALTIMER_0_S_AXI_BASEADDR+0x04)
#define SCU_GLOBAL_TIMER_CONTROL	(XPAR_PS7_GLOBALTIMER_0_S_AXI_BASEADDR+0x08)
#define SCU_GLOBAL_TIMER_ISR		(XPAR_PS7_GLOBALTIMER_0_S_AXI_BASEADDR+0x0C)
#define SCU_GLOBAL_TIMER_COMP_L32	(XPAR_PS7_GLOBALTIMER_0_S_AXI_BASEADDR+0x10)
#define SCU_GLOBAL_TIMER_COMP_U32	(XPAR_PS7_GLOBALTIMER_0_S_AXI_BASEADDR+0x14)
#define SCU_GLOBAL_TIMER_AUTO_INC	(XPAR_PS7_GLOBALTIMER_0_S_AXI_BASEADDR+0x18)


static const char ims_logo[] = "ims-small-logo.png";
static const char step_1[] = "step1.png";
static const char step_2[] = "step2.png";
static const char step_3[] = "step3.png";
static const char lion[] = "lion.png";
static const char lion2[] = "lion2.png";

static const char pic1[] = "pic1.png";
static const char pic2[] = "pic2.png";
static const char pic3[] = "pic3.png";
static const char pic4[] = "pic4.png";
static const char pic5[] = "pic5.png";
static const char pic6[] = "pic6.png";


void pixmap_draw(GDisplay* pixmap, pixel_t* surface, coord_t pm_width, coord_t pm_height, gdispImage *p_Image, uint32_t pm_sx, uint32_t pm_sy, uint32_t img_sx, uint32_t img_sy);

volatile uint32_t g_ms_tick = 0;
uint32_t g_nn = 0;
uint32_t g_dongle_plugged = 0;
uint32_t g_camera_plugged = 0;

uint32_t g_conn_status = 2;

GListener	gl;
GHandle		ghLabel1, ghLabel2, ghLabel3, ghLabel4, ghLabel5, ghLabel6, ghLabel7;

#define USE_IMSLINK

#ifdef USE_IMSLINK
u8 gui_cmd[5] = {0};
u8 gui_cmd_index = 0;
u8 start_data = 0;
#endif

static gdispImage myImage;
static GDisplay* pixmap_1;
static pixel_t* surface_1;
static GDisplay* pixmap_2;
static pixel_t* surface_2;
//static GDisplay* pixmap_3;
//static pixel_t* surface_3;

void main_loop(void);

// *****************************************************
// Main program entry point
// *****************************************************
int main()
{
	// Local variables
	int status = 0;
	coord_t swidth, sheight;
	gdispImage *p_Image;
	uint8_t *p_byte, byte;
	uint32_t i,j, Index;
	GEvent* pe;

	p_Image = &myImage;

	// Setup UART and caches
    init_platform();

    xil_printf("Aries Main Program\n\r");

    // Initialize peripherals
    status = periphs_init
    (
    	&periphs_inst,
    	//XPAR_CONTROL_PATH_AXI_GPIO_0_DEVICE_ID,
    	//XPAR_CONTROL_PATH_AXI_IIC_0_BASEADDR,
		//XPAR_XIICPS_0_DEVICE_ID,
		XPAR_PS7_GPIO_0_DEVICE_ID,
		XPAR_VIDEO_PATH_VIDEO_OUT_VIDEO_LOCK_MONITOR_DEVICE_ID,
		XPAR_PS7_SCUGIC_0_DEVICE_ID,
		XPAR_PS7_SCUTIMER_0_DEVICE_ID,
		XPAR_PS7_UART_0_DEVICE_ID,
		//XPAR_VIDEO_PATH_CAMERA_IN_V_TC_VTD_DEVICE_ID,
    	//XPAR_VIDEO_PATH_TPG_OLD_TPG_OLD_DEVICE_ID,
		XPAR_VIDEO_PATH_V_TPG_0_DEVICE_ID,
		//XPAR_VIDEO_PATH_CAMERA_SCALER_V_PROC_SS_1_DEVICE_ID,
		XPAR_VIDEO_PATH_CAMERA_SCALER_FREEZE_V_PROC_SS_1_DEVICE_ID,
		XPAR_VIDEO_PATH_FRAMEBUFFER_AXI_VDMA_CAMERA_DEVICE_ID,
		XPAR_VIDEO_PATH_FRAMEBUFFER_AXI_VDMA_CAMERA_FREEZE_DEVICE_ID,
		//XPAR_VIDEO_PATH_FRAMEBUFFER_OUTPUT_AXI_VDMA_GUI_DEVICE_ID,
		XPAR_VIDEO_PATH_OUTPUT_MIXER_V_MIX_0_DEVICE_ID,
		XPAR_VIDEO_PATH_VIDEO_OUT_V_TC_TFP410_DEVICE_ID,
		XPAR_VIDEO_PATH_VIDEO_OUT_V_TC_CH7038_DEVICE_ID,
		XPAR_PS7_USB_0_DEVICE_ID,
    	FRAMEBUFFER_CAMERA_START_ADDR,
		FRAMEBUFFER_CAMERA_FREEZE_START_ADDR,
		FRAMEBUFFER_GUI_START_ADDR
    );
	if (status != 0)
	{
		xil_printf("Initialization failed.\n\r");
		return -1;
	}

	// Set up Mixer Layers
	//RunMixer(periphs_inst.p_vid_output_mixer_l2_inst);

    // Initialize uGFX
    gfxInit();
    xil_printf("gfxInit() complete\r\n");
	// Background process
	xil_printf("Initialization complete. Switching to background process.\n\r");

	// Set up pixmap for layer 1
	//								1216		912
    pixmap_1 = gdispPixmapCreate(LAYER1_WIDTH, LAYER1_HEIGHT);
    surface_1 = gdispPixmapGetBits(pixmap_1);

    // Draw transparency required on layer 1
    //									1216		912
    pixmap_draw(pixmap_1, surface_1, LAYER1_WIDTH, LAYER1_HEIGHT, NULL, 0, 0, 0, 0);

	// Set up pixmap for layer 2
    //								640				480
    pixmap_2 = gdispPixmapCreate(LAYER2_WIDTH, LAYER2_HEIGHT);
    surface_2 = gdispPixmapGetBits(pixmap_2);
    // Draw transparency required on layer 2
    pixmap_draw(pixmap_2, surface_2, LAYER2_WIDTH, LAYER2_HEIGHT, NULL, 0, 0, 0, 0);

	// Open image for layer 3
	// Get the display dimensions
	swidth = gdispGetWidth();
	xil_printf("swidth: %d\r\n", swidth);
	sheight = gdispGetHeight();
	xil_printf("sheight: %d\r\n", sheight);

	xil_printf("david0807: %s:%s(%d) open ims_logo\r\n",__FILE__,__func__,__LINE__);
	status = gdispImageOpenFile(p_Image, ims_logo);

	xil_printf("david0807: %s:%s(%d) ImageDraw X=%d Y=%d W=%d H=%d\r\n",__FILE__,__func__,__LINE__,swidth-p_Image->width-BORDER_X*2, sheight-p_Image->height-BORDER_Y*2, p_Image->width, p_Image->height);
	status = gdispImageDraw(p_Image, swidth-p_Image->width-BORDER_X*2, sheight-p_Image->height-BORDER_Y*2, p_Image->width, p_Image->height, 0, 0);
	//xil_printf("status maindraw: %d\r\n", status);
	gdispImageClose(p_Image);

	// Blit surface_1 to the real display at the new position

	xil_printf("david0807: %s:%s(%d) Blit X=%d Y=%d W=%d H=%d\r\n",__FILE__,__func__,__LINE__,LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT);
	gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);

	// Blit surface_2 to the real display at the new position

	xil_printf("david0807: %s:%s(%d) Blit X=%d Y=%d W=%d H=%d\r\n",__FILE__,__func__,__LINE__,BORDER_X, LAYER0_HEIGHT-LAYER2_HEIGHT-BORDER_Y, LAYER2_WIDTH, LAYER2_HEIGHT);
	gdispBlitArea(BORDER_X, LAYER0_HEIGHT-LAYER2_HEIGHT-BORDER_Y, LAYER2_WIDTH, LAYER2_HEIGHT, surface_2);

	Xil_DCacheFlush();

	// Set up Mixer Layers
	RunMixer(periphs_inst.p_vid_output_mixer_l2_inst);

	// Set the widget defaults
	gwinSetDefaultFont(gdispOpenFont("*"));
	gwinSetDefaultStyle(&BlackWidgetStyle, FALSE);
	//gdispClear(White);

	Xil_DCacheFlush();

	//mouse_host_app_init(); // Mouse Host Init
	Xil_DCacheFlush(); // Flush DCache after USB Init();
	//Xil_DCacheInvalidate();

	//Xil_DCacheDisable();	//Enable DCache fast, but USB fail, so, disable it.

	xil_printf("\n\r\n\rdavid0808: %s:%s(%d) start main_loop\r\n\n\r",__FILE__,__func__,__LINE__);

	main_loop();

    cleanup_platform();
    return 0;
}

void main_loop()
{
	// Local variables
	char c[1]  = {0};
	int  ii = 0;
	unsigned int status = 0;
	gdispImage *p_Image;


	#ifdef USE_IMSLINK
	unsigned int DongleAddr;
	unsigned char DongleData;
	int i;
	u8 xx, yy, zz;
	#endif

	// Main loop
	while (1)
	{
		uint32_t status;

		c[0] = XUartPs_RecvByte(XPAR_PS7_UART_1_BASEADDR);

		g_conn_status = psuart0_dongle_ping();

		if((start_data == 0) && ((c[0] == 0xA0) ||(c[0] == 0xA1) ||(c[0] == 0xB0) ||(c[0] == 0xB1) ||(c[0] == 0xD0)))
		{
			start_data = 1;
			gui_cmd[gui_cmd_index] = c[0];
			gui_cmd_index++;
		}
		else if(start_data == 1)
		{
			gui_cmd[gui_cmd_index] = c[0];
			gui_cmd_index++;
			if(gui_cmd_index == 5)
			{
				gui_cmd_index = 0;
				start_data = 0;

				if(gui_cmd[0] == 0xA0)
				{
					//xil_printf("cmd ok %2x %2x %2x %2x %2x\n", gui_cmd[0], gui_cmd[1], gui_cmd[2], gui_cmd[3], gui_cmd[4]);
					DongleAddr = gui_cmd[1] << 8 | gui_cmd[2];
					DongleData = gui_cmd[3];

					dongle_write_data(DongleAddr, DongleData);
				}
				else if(gui_cmd[0] == 0xD0)
				{
					xx = gui_cmd[1];
					yy = gui_cmd[2];
					zz = gui_cmd[3];
					xil_printf("cmd ok %2x %2x %2x %2x %2x\n", gui_cmd[0], xx, yy, zz, gui_cmd[4]);
					if(zz == 0xff)
					{
						xil_printf("david0806: %s:%s(%d) get layer status\r\n",__FILE__,__func__,__LINE__);

						for(i = 0 ;i <= 7; i++)
						{
							status = XVMix_IsLayerEnabled(periphs_inst.p_vid_output_mixer_l2_inst, i);
							xil_printf("layer %d, status = %d\n\r", i, status);
						}
						xil_printf("david0806: %s:%s(%d) get layer status OK\r\n",__FILE__,__func__,__LINE__);

						// Mixer Debug
						xil_printf("\n\rdavid0806: %s:%s(%d) ST call XVMix_DbgReportStatus\r\n",__FILE__,__func__,__LINE__);
						XVMix_DbgReportStatus(periphs_inst.p_vid_output_mixer_l2_inst);

						xil_printf("\n\rdavid0806: %s:%s(%d) ST call XVMix_DbgLayerInfo\r\n",__FILE__,__func__,__LINE__);
						for(i = 0 ;i <= 6; i++)
						{
							xil_printf("-------------------------------------------------------------\n\r");
							XVMix_DbgLayerInfo(periphs_inst.p_vid_output_mixer_l2_inst, i);
						}
						xil_printf("-------------------------------------------------------------\n\r");

					}
					else if(xx == 0)	//write
					{
						xil_printf("david0806: %s:%s(%d) write data = 0x%x\r\n",__FILE__,__func__,__LINE__, yy);
						//RunMixer(periphs_inst.p_vid_output_mixer_l2_inst);
						XV_mix_WriteReg(periphs_inst.p_vid_output_mixer_l2_inst->Mix.Config.BaseAddress, XV_MIX_CTRL_ADDR_HWREG_LAYERENABLE_DATA, yy);
					}
					else if(xx == 2)	//picture
					{
						if(yy == 0)	//clear
						{
							pixmap_draw(pixmap_1, surface_1, LAYER1_WIDTH, LAYER1_HEIGHT, NULL, 0, 0, 0, 0);
							gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							Xil_DCacheFlush();
						}
						else if(yy == 1)	//step_1
						{
							p_Image = &myImage;
							status = gdispImageOpenFile(p_Image, step_1);
							pixmap_draw(pixmap_1, surface_1, LAYER1_WIDTH, LAYER1_HEIGHT, p_Image, 0, 0, 0, 0);
							gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispImageClose(p_Image);
							Xil_DCacheFlush();
						}
						else if(yy == 2)	//step_2
						{

							p_Image = &myImage;
							status = gdispImageOpenFile(p_Image, step_2);
							pixmap_draw(pixmap_1, surface_1, LAYER1_WIDTH, LAYER1_HEIGHT, p_Image, 0, 0, 0, 0);
							gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispImageClose(p_Image);
							Xil_DCacheFlush();
						}
						else if(yy == 3)	//step_3
						{
							p_Image = &myImage;
							status = gdispImageOpenFile(p_Image, step_3);
							pixmap_draw(pixmap_1, surface_1, LAYER1_WIDTH, LAYER1_HEIGHT, p_Image, 0, 0, 0, 0);
							gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispImageClose(p_Image);
							Xil_DCacheFlush();
						}
						else if(yy == 4)	//logo
						{
							p_Image = &myImage;
							status = gdispImageOpenFile(p_Image, ims_logo);
							pixmap_draw(pixmap_1, surface_1, LAYER1_WIDTH, LAYER1_HEIGHT, p_Image, 0, 0, 0, 0);
							gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispImageClose(p_Image);
							Xil_DCacheFlush();
						}
						else if(yy == 5)	//lion
						{
							p_Image = &myImage;
							status = gdispImageOpenFile(p_Image, lion);
							pixmap_draw(pixmap_1, surface_1, LAYER1_WIDTH, LAYER1_HEIGHT, p_Image, 0, 0, 0, 0);
							gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispImageClose(p_Image);
							Xil_DCacheFlush();
						}
						else if(yy == 6)	//lion
						{
							p_Image = &myImage;
							status = gdispImageOpenFile(p_Image, lion);
							pixmap_draw(pixmap_1, surface_1, LAYER1_WIDTH/2, LAYER1_HEIGHT/2, p_Image, 0, 0, 0, 0);
							gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispImageClose(p_Image);
							Xil_DCacheFlush();
						}
						else if(yy == 7)	//lion
						{
							p_Image = &myImage;
							status = gdispImageOpenFile(p_Image, lion);
							pixmap_draw(pixmap_1, surface_1, 0 + p_Image->width, 0 + p_Image->height, p_Image, 0, 0, 0, 0);



							xil_printf("david0808: %s:%s(%d) x=%d y=%d w=%d h=%d\r\n",__FILE__,__func__,__LINE__,LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT);
							//				1920	  -		1216   -  16	    16		  1216			912
							gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispImageClose(p_Image);
							Xil_DCacheFlush();
						}
						else if(yy == 8)	//pic
						{
							p_Image = &myImage;
							status = gdispImageOpenFile(p_Image, pic1);
							pixmap_draw(pixmap_1, surface_1, 0 + p_Image->width, 0 + p_Image->height, p_Image, 0, 0, 0, 0);


							xil_printf("david0808: %s:%s(%d) x=%d y=%d w=%d h=%d\r\n",__FILE__,__func__,__LINE__,LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT);
							//				1920	  -		1216   -  16	    16		  1216			912
							gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispImageClose(p_Image);
							Xil_DCacheFlush();
						}
						else if(yy == 20)	//test gistImageDraw
						{
							xil_printf("david0807: %s:%s(%d) open lion\r\n",__FILE__,__func__,__LINE__);
							p_Image = &myImage;
							status = gdispImageOpenFile(p_Image, lion);
							//xil_printf("david0807: %s:%s(%d) ImageDraw X=%d Y=%d W=%d H=%d\r\n",__FILE__,__func__,__LINE__,swidth-p_Image->width-BORDER_X*2, sheight-p_Image->height-BORDER_Y*2, p_Image->width, p_Image->height);
							status = gdispImageDraw(p_Image, 1920/2, 1080/2, p_Image->width, p_Image->height, 0, 0);
							//g_nn = 0;
							//xil_printf("status maindraw: %d\r\n", status);
							gdispImageClose(p_Image);
							Xil_DCacheFlush();
						}
						else if(yy == 21)	//specified position
						{
							p_Image = &myImage;
							status = gdispImageOpenFile(p_Image, lion);
							//									1216			912
							pixmap_draw(pixmap_1, surface_1, p_Image->width+60, p_Image->height+60, p_Image, 0, 0, 0, 0);
							//				1920		1216		16			16		1216			912
							//gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispBlitArea(0, 0, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispImageClose(p_Image);
							Xil_DCacheFlush();
						}
						else if(yy == 22)	//specified position
						{
							p_Image = &myImage;
							status = gdispImageOpenFile(p_Image, pic6);
							//									1216			912
							pixmap_draw(pixmap_1, surface_1, p_Image->width+60, p_Image->height+600, p_Image, 0, 0, 0, 0);
							//				1920		1216		16			16		1216			912
							//gdispBlitArea(LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X, BORDER_Y, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispBlitArea(0, 0, LAYER1_WIDTH, LAYER1_HEIGHT, surface_1);
							gdispImageClose(p_Image);
							Xil_DCacheFlush();
						}

					}
				}
			}
		}

	}
}

void pixmap_draw(GDisplay* pixmap, pixel_t* surface, coord_t pm_width, coord_t pm_height, gdispImage *p_Image, uint32_t pm_sx, uint32_t pm_sy, uint32_t img_sx, uint32_t img_sy)
{
	uint32_t i, j, status;
	color_t color = 0;


	xil_printf("david0807: %s:%s(%d) ST W=%d H = %d psx = %d psy = %d isx = %d isy = %d\r\n",__FILE__,__func__,__LINE__,pm_width,pm_height,pm_sx,pm_sy,img_sx,img_sy);


	xil_printf("enter pixmap_draw\t");
	// Clear pixmap with 0
	memset(surface, 0, pm_width*pm_height*4); // Clear buffer

	// Overlay file is necessary
	if(p_Image != NULL) {
		// Load image
		status = gdispGImageDraw(pixmap, p_Image, (pm_width-p_Image->width) >> 1, (pm_height-p_Image->height) >> 1, p_Image->width, p_Image->height, 0, 0);
		xil_printf("status draw: %d\r\n", status);
	}
	else
		xil_printf("image is null\n\r");

    // Draw transparency required on layer 1
    for(j = 0; j < pm_height; j++) {
    	for(i = 0; i < pm_width; i++) {

    		if((j > (1.5*(pm_height >> 3)-1)) && (j < (pm_height-1.5*(pm_height >> 3)))) {
    			//color = gdisp_lld_get_pixel_color(pixmap);
    			//xil_printf("color: %x\r\n", color);
    			if(surface[j*pm_width + i] == 0) {
    				surface[j*pm_width + i] = ABGR2COLOR(0x00, 0x00, 0x00, 0x00);
    			}
//    			else {
    				//surface[j*pm_width + i] = ABGR2COLOR(0x00, 0x00, 0x00, 0x00);
    			//}

    		}
    		else {

				if(j < 1.5*(pm_height >> 3)) { // Top lines

					if (  (i < (1.5*(pm_height >> 3)-j)) || (i > ((pm_width-1.5*(pm_height >> 3))-1+j)    )  ) {
    					surface[j*pm_width + i] = ABGR2COLOR(0x80, 0xff, 0xff, 0xff);
    					//xil_printf("c: %x\r\n", surface_1[j*PIXMAP_WIDTH_1 + i]);
    				}
    				else {
    	    			//if(surface[j*pm_width + i] == 0) {
    	    				surface[j*pm_width + i] = ABGR2COLOR(0x00, 0x00, 0x00, 0x00);
    	    			//}
    				}

				}
				else { // Bottom lines

					if( (i < (j+1.5*(pm_height >> 3)-pm_height) ) || i > ((pm_width-(1.5*(pm_height >> 3)-(pm_height-j)))-1) ){
						surface[j*pm_width + i] = ABGR2COLOR(0x80, 0xff, 0xff, 0xff);
					}
					else {
    	    			if(surface[j*pm_width + i] == 0) {
    	    				surface[j*pm_width + i] = ABGR2COLOR(0x00, 0x00, 0x00, 0x00);
    	    			}
					}
				}
     		}
    	}
    }
}

// uGFX SystemTick
systemticks_t gfxSystemTicks(void)
{
	return g_ms_tick;
}

systemticks_t gfxMillisecondsToTicks(delaytime_t ms)
{
	return ms;
}
/////////////////////////////////////

uint32_t tusb_tick_get(void)
{
  //return system_ticks;
  return g_ms_tick;
}

