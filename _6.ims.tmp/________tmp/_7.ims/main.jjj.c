

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
#include "gfx.h"

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

void pixmap_draw(GDisplay* pixmap, pixel_t* surface, coord_t pm_width, coord_t pm_height, gdispImage *p_Image, uint32_t pm_sx, uint32_t pm_sy, uint32_t img_sx, uint32_t img_sy);


volatile uint32_t g_ms_uptime = 0;
volatile uint32_t g_ms_tick = 0;
volatile uint32_t g_ms_tick_wait = 0;
uint32_t g_nn = 0;
uint32_t g_dongle_plugged = 0;
uint32_t g_camera_plugged = 0;

uint32_t g_conn_status = 2;

GListener	gl;
GHandle		ghLabel1, ghLabel2, ghLabel3, ghLabel4, ghLabel5, ghLabel6, ghLabel7;

uint32_t esc_mode = 0;

static gdispImage myImage;
static GDisplay* pixmap_1;
static pixel_t* surface_1;
static GDisplay* pixmap_2;
static pixel_t* surface_2;
//static GDisplay* pixmap_3;
//static pixel_t* surface_3;

// The handle for our console
static GHandle	GW;
GWindowInit		wic;

static void createWidgets(void);
static void createConsoleWidgets(void);
static void updateConsoleWidgets(void);
void main_loop(void);
void get_usb_descriptor(void);
void parse_uart_command(void);
void parse_uart_esc_command(void);
void get_system_up_time(void);

static const char last_command[] = "help";

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


    xil_printf("\n\n\n\nTest\n\r");
    xil_printf("Compiled time: %s %s\n\r", __DATE__, __TIME__);
    xil_printf("%s:%s(%d)\n\r\n\r",__FILE__,__func__,__LINE__);

    while(1)
    {
    	xil_printf("X");
    	xil_printf("\tg_ms_tick = %d\n\r", g_ms_tick);
    	usleep(200000);
        usleep(200000);
        usleep(200000);
        usleep(200000);
    	usleep(200000);
        usleep(200000);
        usleep(200000);
    }

    return 0;
}

#define RELEASE_INFO "Insight Medical Solutions Inc., August-17-2018\n"
#define PROMPT "[aries@ims]# "
#define UART_BUFFER_LEN 10
u8 buffer[UART_BUFFER_LEN];
u8 esc_buffer[3];
u8 ptr = 0;
u8 esc_ptr = 0;
u8 length = 0;

void main_loop()
{
	// Local variables
	char c[1]  = {0};
	int  ii = 0;
	unsigned int status = 0;
	gdispImage *p_Image;

	// Main loop
	while (1)
	{
		uint32_t status;
		//xil_printf("What would you like to do? Press 'p' to print available commands.\n\r");
		c[0] = XUartPs_RecvByte(XPAR_PS7_UART_1_BASEADDR);
		//XUartPs_Recv(g_psuart1_config->BaseAddress, &c[0], 1);
		
		//xil_printf("ping.\n\r");
		g_conn_status = psuart0_dongle_ping();

		//  Run USB Host Task Handlers
		tusb_task_runner(); // USB House Keeping
	    keyboard_host_app_task(NULL); // Keyboard tasks
	    //mouse_host_app_task(NULL); // Mouse Tasks
		//Xil_DCacheFlush();

		switch (c[0])
		{
			case 'p':
				xil_printf("\n\r");
				xil_printf("------------- Aries Demo -------------\n\r");
				xil_printf("'1' = Toggle Layer 1\n\r");
				xil_printf("'2' = Toggle Layer 2\n\r");
				xil_printf("'3' = Toggle Layer 3\n\r");
				xil_printf("'n' = Set to new scaler datapath\n\r");
//				xil_printf("'o' = Set to old scaler datapath\n\r");
				xil_printf("'t' = Enable/bypass camera TPG\n\r");
				xil_printf("'y' = Enable/bypass GUI TPG\n\r");
//				xil_printf("'d' = Detect or set input frame size\n\r");
				xil_printf("'u' = Park Camera Freeze VDMA\n\r");
				xil_printf("'s' = Set output frame size\n\r");
				xil_printf("'p' = Print this menu\n\r");
				xil_printf("---------------------------------------\n\r");
				xil_printf("\n\r");
				break;
			case '1':
				xil_printf("Enabling/bypassing Layer 1.\n\r");
				status = XVMix_IsLayerEnabled(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_1);
				if(status) { // Enabled
					XVMix_LayerDisable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_1);
				} else {
					XVMix_LayerEnable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_1);
				}
				break;
			case '2':
				xil_printf("Enabling/bypassing Layer 2.\n\r");
				status = XVMix_IsLayerEnabled(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_2);
				if(status) { // Enabled
					XVMix_LayerDisable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_2);
				} else {
					XVMix_LayerEnable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_2);
				}
				break;
			case '3':
				xil_printf("Enabling/bypassing Layer 3.\n\r");
				status = XVMix_IsLayerEnabled(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_3);
				if(status) { // Enabled
					XVMix_LayerDisable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_3);
				} else {
					XVMix_LayerEnable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_3);
				}
				break;
//			case 'n':
//				xil_printf("Using new VPSS-based scaler datapath.\n\r");
//				periphs_select_scaler(&periphs_inst, PERIPHS_SEL_NEW_SCALER);
//				break;
//			case 'o':
//				xil_printf("Using old scaler datapath.\n\r");
//				periphs_select_scaler(&periphs_inst, PERIPHS_SEL_OLD_SCALER);
//				break;
			case 't':
				xil_printf("Enabling/bypassing camera TPG.\n\r");
				//periphs_toggle_camera_tpg(&periphs_inst);
				break;
			case 'y':
				xil_printf("Enabling/bypassing GUI TPG.\n\r");
				periphs_toggle_GUI_tpg(&periphs_inst);
				break;
			case 'u':
				xil_printf("Park/Unpark Camera Freeze VDMA.\n\r");
				periphs_toggle_camera_freeze_vdma(&periphs_inst);
				// Determine if we're in TPG or passthrough mode
				if (periphs_inst.enable_camera_freeze_vdma == PERIPHS_SEL_ENABLE_PARK)
				{
					XVMix_LayerEnable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_2);
				}
				else
				{
					XVMix_LayerDisable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_2);
				}




				break;
//			case 'd':
//				if (periphs_get_fmc_status(&periphs_inst))
//				{
//					xil_printf("FMC IMAGEON card is connected. Detecting input frame size.\n\r");
//					//periphs_detect_input_fsize(&periphs_inst);
//				}
//				else
//				{
//					while (1)
//					{
//						xil_printf("FMC IMAGEON card is not connected. Using internal TPG as video source. Please select a resolution to set it to. Press 'p' to print available resolutions.\n\r");
//						c = XUartPs_RecvByte(XPAR_PS7_UART_1_BASEADDR);
//						if (c == 'p')
//						{
//							xil_printf("\n\r");
//							xil_printf("------------- Resolutions -------------\n\r");
//							for (ii = 0; ii < NUM_VIDEO_RESOLUTIONS; ii++)
//							{
//								xil_printf("%d = %s\n\r", ii, vres_get_name(ii));
//							}
//							xil_printf("'p' = Print this menu\n\r");
//							xil_printf("'q' = Quit\n\r");
//							xil_printf("---------------------------------------\n\r");
//							xil_printf("\n\r");
//						}
//						else if ((c == '0')||(c == '1')||(c == '2')||(c == '3')||(c == '4') ||
//								 (c == '5')||(c == '6')||(c == '7')||(c == '8'))
//						{
//							//periphs_set_input_fsize(&periphs_inst, (c-'0'));
//							break;
//						}
//						else if (c == 'q')
//						{
//							break;
//						}
//						else
//						{
//							xil_printf("ERROR! Illegal character. Try again.\n\r");
//						}
//					}
//					break;
//				}
//				break;
//			case 's':
//				while (1)
//				{
//					xil_printf("Setting output frame size. What resolution would you like? Press 'p' to print available resolutions.\n\r");
//					c = XUartPs_RecvByte(XPAR_PS7_UART_1_BASEADDR);
//
//					if (c == 'p')
//					{
//						xil_printf("\n\r");
//						xil_printf("------------- Resolutions -------------\n\r");
//						for (ii = 0; ii < NUM_VIDEO_RESOLUTIONS; ii++)
//						{
//							xil_printf("%d = %s\n\r", ii, vres_get_name(ii));
//						}
//						xil_printf("'p' = Print this menu\n\r");
//						xil_printf("'q' = Quit\n\r");
//						xil_printf("---------------------------------------\n\r");
//						xil_printf("\n\r");
//					}
//					else if ((c == '0')||(c == '1')||(c == '2')||(c == '3')||(c == '4') ||
//							 (c == '5')||(c == '6')||(c == '7')||(c == '8'))
//					{
//						//periphs_update_output_fsize(&periphs_inst, (c-'0'));
//						break;
//					}
//					else if (c == 'q')
//					{
//						break;
//					}
//					else
//					{
//						xil_printf("ERROR! Illegal character. Try again.\n\r");
//					}
//				}
//				break;

			case 0x0D:
			case ' ':
				xil_printf("\n\r\n\r\n\r\n\r");
				break;
			default:
				//xil_printf("\n\r---- unknown ---- c[0] = 0x%x\n\r", c[0]);
				/*
				p_periphs_inst222 = &periphs_inst;
				p_gpio = p_periphs_inst222->p_ps_gpio_inst;
				DataRead = XGpioPs_Read(p_gpio, XGPIOPS_BANK2);	//read bank 2 data, seems useless
				xil_printf("DataRead = 0x%x\n\r", DataRead);
				usleep(200000);
				*/

				//xil_printf("ERROR! Illegal character. Try again.\n\r");
				break;

		}
	}
}



static void createWidgets(void) {
	GWidgetInit	wi;

	coord_t wide = 600;
	coord_t thick = 40;

	// Apply some default values for GWIN
	gwinWidgetClearInit(&wi);
	wi.g.show = TRUE;

	gwinSetDefaultFont(gdispOpenFont("iskpota232"));

	// Create label
	wi.g.width = wide; wi.g.height = thick; wi.g.x = BORDER_X, wi.g.y = BORDER_Y + thick * 0;
	wi.text = "ID NO:";
	ghLabel1 = gwinLabelCreate(0, &wi);

	// Create label
	wi.g.width = wide; wi.g.height = thick; wi.g.x = BORDER_X, wi.g.y = BORDER_Y + thick * 1;
	wi.text = "NAME:";
	ghLabel2 = gwinLabelCreate(0, &wi);

	// Create label
	wi.g.width = wide; wi.g.height = thick; wi.g.x = BORDER_X, wi.g.y = BORDER_Y + thick * 3;
	wi.text = "SEX:";
	ghLabel3 = gwinLabelCreate(0, &wi);

	// Create label
	wi.g.width = wide; wi.g.height = thick; wi.g.x = BORDER_X, wi.g.y = BORDER_Y + thick * 4;
	wi.text = "AGE:";
	ghLabel4 = gwinLabelCreate(0, &wi);

	// Create label
	wi.g.width = wide; wi.g.height = thick; wi.g.x = BORDER_X, wi.g.y = BORDER_Y + thick * 5;
	wi.text = "D.O.BIRTH:";
	ghLabel5 = gwinLabelCreate(0, &wi);

	// Create label
	wi.g.width = wide; wi.g.height = thick; wi.g.x = BORDER_X, wi.g.y = BORDER_Y + thick * 7;
	wi.text = "06/03/2017";
	ghLabel4 = gwinLabelCreate(0, &wi);

	// Create label
	wi.g.width = wide; wi.g.height = thick; wi.g.x = BORDER_X, wi.g.y = BORDER_Y + thick * 8;
	wi.text = "00:00:00";
	ghLabel5 = gwinLabelCreate(0, &wi);


	/*
	// Create label
	wi.g.width = wide; wi.g.height = thick; wi.g.x = 1920/6, wi.g.y =600;
	wi.text = "XXXXXXXXXXXXXXXXXXXXXxx";
	ghLabel5 = gwinLabelCreate(0, &wi);
	*/




}

void pixmap_draw(GDisplay* pixmap, pixel_t* surface, coord_t pm_width, coord_t pm_height, gdispImage *p_Image, uint32_t pm_sx, uint32_t pm_sy, uint32_t img_sx, uint32_t img_sy)
{
	uint32_t i, j, status;
	color_t color = 0;

	//xil_printf("enter pixmap_draw\r\n");
	// Clear pixmap with 0
	memset(surface, 0, pm_width*pm_height*4); // Clear buffer

	// Overlay file is necessary
	if(p_Image != NULL) {
		// Load image
		status = gdispGImageDraw(pixmap, p_Image, (pm_width-p_Image->width) >> 1, (pm_height-p_Image->height) >> 1, p_Image->width, p_Image->height, 0, 0);
		//xil_printf("status draw: %d\r\n", status);
	}

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

///* Global timer set up*/
//
///* start timer */
// void gtimer_start_clock(void)
//{
//	*(volatile unsigned int*)SCU_GLOBAL_TIMER_CONTROL = ((1 << 0) | // Timer Enable
//														 (1 << 1) | // Comparator Comparison Enable
//						      	  	  	  	  	  	  	 (1 << 3) | // Auto-increment
//														 (0 << 8) 	// Pre-scale
//	);
//}
//
///* stop timer and reset timer count regs */
// void gtimer_reset_clock(void)
//{
//	gtimer_disable_clock();
//	*(volatile unsigned int*)SCU_GLOBAL_TIMER_COUNT_L32 = 0; // Reset Clock
//	*(volatile unsigned int*)SCU_GLOBAL_TIMER_COUNT_U32 = 0;
//}
//
// /* Set Comparator values */
//  void gtimer_set_comparator(uint32_t L32, uint32_t U32)
// {
// 	*(volatile unsigned int*)SCU_GLOBAL_TIMER_COMP_L32 = L32;
// 	*(volatile unsigned int*)SCU_GLOBAL_TIMER_COMP_U32 = U32;
// }
//
///* stop timer */
// void gtimer_disable_clock(void)
//{
//	*(volatile unsigned int*)SCU_GLOBAL_TIMER_CONTROL = 0;
//}
//
///* Compute mask for given delay in miliseconds*/
//int get_number_of_cycles_for_delay(unsigned int delay)
//{
//  // GTC is always clocked at 1/2 of the CPU frequency (CPU_3x2x)
//  return (XPAR_PS7_CORTEXA9_0_CPU_CLK_FREQ_HZ*delay/(2*1000));
//
//}
//
//void gtimer_reset_and_start_timer()
//{
//  	    gtimer_reset_clock();
//	    gtimer_start_clock();
//}

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

void reset_usb(void)
{
	uint8_t reg;
	uint8_t val = 0;

	usb_reset_status = 1;
	usb_reset_status_old = 0;
	//xil_printf("david0823: %s:%s(%d) ST usb_reset_status = %d\r\n",__FILE__,__func__,__LINE__,usb_reset_status);

	xil_printf("usb reset\n\r");
	reg = ULPI_OTG_CTRL;
	val = 0;
	val = ulpi_ReadReg(reg);
	xil_printf("read value : %02X\n\r", val);

	val &= 0xDF;
	xil_printf("set value : %02X\n\r", val);
	ulpi_WriteReg(val, reg);

	usleep(500000);

	val |= 0x20;
	xil_printf("set value : %02X\n\r", val);
	ulpi_WriteReg(val, reg);
}

void parse_uart_esc_command(void)
{
	int i;
	if((buffer[0] == 0x1B)&&(buffer[1] == '[')&&(buffer[2] == 'A'))
	{
		//xil_printf("Up\t");
		xil_printf("\r%s", PROMPT);
		xil_printf("%s", last_command);
		ptr = sizeof(last_command) - 1;
		for(i = 0; i < ptr; i++)
		{
			buffer[i] = last_command[i];
		}
	}
	else if((buffer[0] == 0x1B)&&(buffer[1] == '[')&&(buffer[2] == 'B'))
	{
		//xil_printf("Down\t");
		xil_printf("\r%s", PROMPT);
		xil_printf("%s", last_command);
		ptr = sizeof(last_command) - 1;
		for(i = 0; i < ptr; i++)
		{
			buffer[i] = last_command[i];
		}
	}
	else if((buffer[0] == 0x1B)&&(buffer[1] == '[')&&(buffer[2] == 'C'))
	{
		//xil_printf("Right\t");
		xil_printf("\r%s", PROMPT);
		xil_printf("%s", last_command);
		ptr = sizeof(last_command) - 1;
		for(i = 0; i < ptr; i++)
		{
			buffer[i] = last_command[i];
		}
	}
	else if((buffer[0] == 0x1B)&&(buffer[1] == '[')&&(buffer[2] == 'D'))
	{
		//xil_printf("Left\t");
		// not very good
		if(ptr >= 2)
		{
			xil_printf("%c", 0x08);
			//xil_printf(".");
			ptr -= 2;
		}
		else
			ptr--;
	}
	else if((buffer[0] == 0x1B)&&(buffer[1] == '[')&&(buffer[2] == 0x35))
	{
		xil_printf("PageUp\t");
	}
	else if((buffer[0] == 0x1B)&&(buffer[1] == '[')&&(buffer[2] == 0x5B))
	{
		xil_printf("PageDown\t");
	}
	else if((buffer[0] == 0x1B)&&(buffer[1] == '[')&&(buffer[2] == 0x31))
	{
		xil_printf("Home\t");
	}
	else if((buffer[0] == 0x1B)&&(buffer[1] == '[')&&(buffer[2] == 0x32))
	{
		xil_printf("Insert\t");
	}
	else if((buffer[0] == 0x1B)&&(buffer[1] == '[')&&(buffer[2] == 0x33))
	{
		xil_printf("Delete\t");
	}
	else if((buffer[0] == 0x1B)&&(buffer[1] == '[')&&(buffer[2] == 0x34))
	{
		xil_printf("End\t");
	}
	else
	{
		xil_printf("XXXX\t");
		for( i = 0; i<3; i++)
		{
			xil_printf("0x%x ", buffer[i]);
		}
		xil_printf("\t");
	}
}


void parse_uart_command(void)
{
	int status;
	int i;
	uint32_t value = 0;
	uint8_t reg;
	uint8_t val = 0;

	if(length == 8)
	{
		if((buffer[0] == 'c')&&(buffer[1] == 'o')&&(buffer[2] == 'n')&&(buffer[3] == 's')&&(buffer[4] == 'o')&&(buffer[5] == 'l')&&(buffer[6] == 'e'))
		{
			/* initialize and clear the display */
			//gfxInit();

			/* Set a font */
			gwinSetDefaultFont(gdispOpenFont("*"));

			/* create the console window */
			GWindowInit		wi;

			gwinClearInit(&wi);
			wi.show = TRUE;
			wi.x = gdispGetWidth() / 2 - 200;
			wi.y = gdispGetHeight()-140;
			wi.width = 600;
			wi.height = 120;

			xil_printf("W = %d, H = %d\n\r", wi.width, wi.height);
			GW = gwinConsoleCreate(0, &wi);

			/* Set the fore- and background colors for the console */
			gwinSetColor(GW, White);
			gwinSetBgColor(GW, Purple);
			gwinClear(GW);

			gwinPrintf(GW, "gwinConsoleCreate size = %d X %d\n", wi.width, wi.height);

			gwinPrintf(GW, "AAAAAAAAAAAAAAA\n");
			gwinPrintf(GW, "BBBBBBBBBBBBBBBB\n");
			gwinPrintf(GW, "\n");

			for(i = 0; i < 25 ; i++)
			{
				gwinPrintf(GW, "CCCCCCCCCCCCC %2d\n", i);
				sleep(1);
			}

		}
		else if((buffer[0] == 't')&&(buffer[1] == ' '))
		{
		}
	}
	else if(length == 7)
	{
		if((buffer[0] == 'u')&&(buffer[1] == 'p')&&(buffer[2] == 't')&&(buffer[3] == 'i')&&(buffer[4] == 'm')&&(buffer[5] == 'e'))
		{
			//Get System Up time
			get_system_up_time();
		}
		else if((buffer[0] == 's')&&(buffer[1] == 'e')&&(buffer[2] == 'n')&&(buffer[3] == 's')&&(buffer[4] == 'o')&&(buffer[5] == 'r'))
		{
		}
		else if((buffer[0] == 't')&&(buffer[1] == ' '))
		{
		}
	}
	else if(length == 6)
	{
		if((buffer[0] == 'c')&&(buffer[1] == 'l')&&(buffer[2] == 'o')&&(buffer[3] == 'c')&&(buffer[4] == 'k'))
		{
		}
		else if((buffer[0] == 'p')&&(buffer[1] == 'r')&&(buffer[2] == 'i')&&(buffer[3] == 'n')&&(buffer[4] == 't'))
		{
			xil_printf("ABCDEFGHIJKLMNOPQ");
			sleep(3);
			xil_printf("%c", 0x08);
			xil_printf("%c", 0x08);
			xil_printf("%c", 0x08);
			xil_printf("%c", 0x08);
			xil_printf("%c", 0x08);
			xil_printf("%c", 0x08);
			xil_printf("%c", 0x08);
			xil_printf("%c", 0x08);
			xil_printf("%c", 0x08);
			xil_printf("%c", 0x08);
			xil_printf("abcdefg");
			sleep(3);
			xil_printf("\r");
			xil_printf("-------");

		}
		else if((buffer[0] == 'u')&&(buffer[1] == 's')&&(buffer[2] == 'b')&&(buffer[3] == 'r')&&(buffer[4] == '1'))
		{
			xil_printf("\n\rusb HW reset\n\r");
			reset_usb();
		}
		else if((buffer[0] == 'u')&&(buffer[1] == 's')&&(buffer[2] == 'b')&&(buffer[3] == 'r')&&(buffer[4] == '2'))
		{
			xil_printf("\n\rusb SW reset\n\r");
			tusb_init(); // initialize tinyusb stack
			value = 0x60;
			ulpi_WriteReg(value, ULPI_FC_CTRL);	//0x16
			port_connect_status_change_isr(0);
			tusb_isr(0);
		}
		else if((buffer[0] == 't')&&(buffer[1] == ' '))
		{
		}
	}
	else if(length == 5)
	{
		if((buffer[0] == 'h')&&(buffer[1] == 'e')&&(buffer[2] == 'l')&&(buffer[3] == 'p'))
		{
			xil_printf("\n\rIMS command prompt, ");
			//xil_printf(RELEASE_INFO);
			xil_printf("\n\r");
			xil_printf("------------- Aries Demo -------------\n\r");
			xil_printf("1:\tToggle Layer 1\n\r");
			xil_printf("2:\tToggle Layer 2\n\r");
			xil_printf("3:\tToggle Layer 3\n\r");
			//xil_printf("'n' = Set to new scaler datapath\n\r");
			xil_printf("t:\tEnable/bypass camera TPG\n\r");
			xil_printf("y:\tEnable/bypass GUI TPG\n\r");
			xil_printf("u:\tPark Camera Freeze VDMA\n\r");
			//xil_printf("'s' = Set output frame size\n\r");
			//xil_printf("'p' = Print this menu\n\r");
			xil_printf("usb:\tread USB registers\n\r");
			xil_printf("r:\tread USB registers\n\r");
			xil_printf("usbr1:\tUSB HW reset\n\r");
			xil_printf("usbr2:\tUSB SW reset\n\r");
			xil_printf("dd:\tDCache Disable\n\r");
			xil_printf("de:\tDCache Enable\n\r");
			xil_printf("help:\thelp menu\n\r");
			xil_printf("---------------------------------------\n\r");
		}
		else if((buffer[0] == 'u')&&(buffer[1] == 's')&&(buffer[2] == 'b')&&(buffer[3] == 'r'))
		{
			xil_printf("\n\rPlease use 'usbr1' or 'usbr2'\n\r");
		}
		else if((buffer[0] == 's')&&(buffer[1] == 'l')&&(buffer[2] == 'o')&&(buffer[3] == 'w'))
		{
		}
		else if((buffer[0] == 'l')&&(buffer[1] == 'o')&&(buffer[2] == 'c')&&(buffer[3] == 'k'))
		{
		}
		else if((buffer[0] == 's')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x30) || (buffer[2] > 0x39) || (buffer[3] < 0x30) || (buffer[3] > 0x39))
			{
				xil_printf("\nIllegal parameters.\n");
				return;
			}
			//PWM_start_duty = (buffer[2] - 0x30) * 10 + (buffer[3] - 0x30);
			//xil_printf("\nPWM_start_duty: ");printd(PWM_start_duty);xil_printf("\n\r");
		}
		else if((buffer[0] == 'd')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x30) || (buffer[2] > 0x39) || (buffer[3] < 0x30) || (buffer[3] > 0x39))
			{
				xil_printf("\nIllegal parameters.\n");
				return;
			}
			//PWM_duty = (buffer[2] - 0x30) * 10 + (buffer[3] - 0x30);
			//xil_printf("\nPWM_duty: ");printd(PWM_duty);xil_printf("\n\r");
		}
		else if((buffer[0] == 't')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x30) || (buffer[2] > 0x39) || (buffer[3] < 0x30) || (buffer[3] > 0x39))
			{
				xil_printf("\nIllegal parameters.\n\r");
				return;
			}
			//target_speed_tmp = (buffer[2] - 0x30) * 10 + (buffer[3] - 0x30);
			//SETUP_target_speed(target_speed_tmp);
			//xil_printf("\nTarget_speed: ");printd(target_speed);xil_printf("\n\r");
		}
	}
	else if(length == 4)
	{
		if((buffer[0] == 'u')&&(buffer[1] == 's')&&(buffer[2] == 'b'))
		{
			read_usb_registers();
		}
		else if((buffer[0] == 't')&&(buffer[1] == 'i')&&(buffer[2] == 'c'))
		{
			g_ms_tick = 0;
		}
		else if((buffer[0] == 't')&&(buffer[1] == 'o')&&(buffer[2] == 'c'))
		{
			uint32_t tt = g_ms_tick;
			uint32_t hh;
			uint32_t mm;
			uint32_t ss;
			uint32_t dd;

			dd = tt % 500 * 2;
			ss = (tt / 500) % 60;
			mm = ((tt / 500) / 60) % 60;
			hh = ((tt / 500) / 60) / 60;

			xil_printf("\n\rElasped time is %02d:%02d:%02d.%03d\n\r", hh, mm, ss, dd);
		}
		else if((buffer[0] == 'i')&&(buffer[1] == 'f')&&(buffer[2] == 'b'))
		{

		}
	}
	else if(length == 3)
	{
		if(((buffer[0] == 'l')&&(buffer[1] == 's'))||(buffer[0] == 'l')&&(buffer[1] == 'l'))
		{
			xil_printf("\n\r");
			xil_printf("Type `help' to see help list.\n\r");
		}
		else if((buffer[0] == 'd')&&(buffer[1] == 'e'))
		{
			xil_printf("Xil_DCacheEnable()\n\r");
			Xil_DCacheEnable();
		}
		else if((buffer[0] == 'd')&&(buffer[1] == 'd'))
		{
			xil_printf("Xil_DCacheDisable()\n\r");
			Xil_DCacheDisable();
		}
	}
	else if(length == 2)
	{
		xil_printf("\n\r");
		if(buffer[0] == 'p')
		{

		}

		else if(buffer[0] == '1')
		{
			xil_printf("Enabling/bypassing Layer 1.\n\r");
			status = XVMix_IsLayerEnabled(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_1);
			if(status) { // Enabled
				XVMix_LayerDisable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_1);
			} else {
				XVMix_LayerEnable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_1);
			}
		}
		else if(buffer[0] == '2')
		{
			xil_printf("Enabling/bypassing Layer 2.\n\r");
			status = XVMix_IsLayerEnabled(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_2);
			if(status) { // Enabled
				XVMix_LayerDisable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_2);
			} else {
				XVMix_LayerEnable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_2);
			}
		}
		else if(buffer[0] == '3')
		{
			xil_printf("Enabling/bypassing Layer 3.\n\r");
			status = XVMix_IsLayerEnabled(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_3);
			if(status) { // Enabled
				XVMix_LayerDisable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_3);
			} else {
				XVMix_LayerEnable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_3);
			}
		}
		else if(buffer[0] == 't')
		{
			xil_printf("Enabling/bypassing camera TPG.\n\r");
			periphs_toggle_camera_tpg(&periphs_inst);
		}
		else if(buffer[0] == 'y')
		{
			xil_printf("Enabling/bypassing GUI TPG.\n\r");
			periphs_toggle_GUI_tpg(&periphs_inst);
		}
		else if(buffer[0] == 'u')
		{
			xil_printf("Park/Unpark Camera Freeze VDMA.\n\r");
			periphs_toggle_camera_freeze_vdma(&periphs_inst);
			// Determine if we're in TPG or passthrough mode
			if (periphs_inst.enable_camera_freeze_vdma == PERIPHS_SEL_ENABLE_PARK)
			{
				XVMix_LayerEnable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_2);
			}
			else
			{
				XVMix_LayerDisable(periphs_inst.p_vid_output_mixer_l2_inst, XVMIX_LAYER_2);
			}
		}
		else if(buffer[0] == 'r')
		{
			read_usb_registers();
		}
		else if(buffer[0] == 'g')
		{
			get_usb_descriptor();
		}
		else if(buffer[0] == 'd')
		{
			xil_printf("david debug\n\r");

			xil_printf("size of last_command is %d\n\r", sizeof(last_command));
		}
		else
		{
			xil_printf("Invalid command : %c\n\r", buffer[0]);
		}
	}
	length = 0;
}

void get_system_up_time(void)
{
	uint32_t tt = g_ms_uptime;
	uint32_t hh;
	uint32_t mm;
	uint32_t ss;
	uint32_t dd;

	dd = tt % 500 * 2;
	ss = (tt / 500) % 60;
	mm = ((tt / 500) / 60) % 60;
	hh = ((tt / 500) / 60) / 60;

	xil_printf("\n\rSystem up time is %02d:%02d:%02d.%03d\n\r", hh, mm, ss, dd);
}


