

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

//----------------------------------------------------
// MAIN FUNCTION
//----------------------------------------------------

int main()
{
	int status;
	u32 value;
    usleep(200000);usleep(200000);usleep(200000);usleep(200000);


    xil_printf("\n\n\n\nTest\n\r");
    xil_printf("Compiled time: %s %s\n\r", __DATE__, __TIME__);
    xil_printf("%s:%s(%d)\n\r\n\r",__FILE__,__func__,__LINE__);

    status = periphs_gpio_init
    		(
    	    	&periphs_gpio_inst,
    			XPAR_PS7_GPIO_0_DEVICE_ID,
    			XPAR_VIDEO_PATH_VIDEO_OUT_VIDEO_LOCK_MONITOR_DEVICE_ID,
    			XPAR_PS7_SCUGIC_0_DEVICE_ID,
    			XPAR_PS7_SCUTIMER_0_DEVICE_ID
				);
    while(1)
    {
    	//xil_printf("\tg_ms_tick = %d\n\r", g_ms_tick);
    	sleep(2);
    	Xil_Out32(0xE000A298, 0x1000);
    	sleep(2);

    	value = Xil_In32(0xE000A068);

    	xil_printf("\tg_ms_tick = %d value = 0x%08x\n\r", g_ms_tick, value);

    }

    return 0;
}

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

