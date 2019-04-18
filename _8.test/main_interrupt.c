#include "stdio.h"
#include "xil_io.h"
#include "xil_printf.h"
#include "xil_exception.h"

#define MER_OFFSET 28
#define MASTER_ENABLE_MASK      0x1UL
#define HARDWARE_ENABLE_MASK    0x2UL
#define IER_OFFSET      8
#define IAR_OFFSET      12
#define MASK 0X000001
#define Interrupt 0

volatile int counter = 0;
int Handler();


int main()
{


  	xil_printf("Interrupt Test.... \n\r");

  	microblaze_enable_interrupts();


	Xil_ExceptionRegisterHandler(XIL_EXCEPTION_ID_INT,(Xil_ExceptionHandler) Handler,0x41200000);


  	//Master Enable
	Xil_Out32(0x41200000 + MER_OFFSET, MASTER_ENABLE_MASK | HARDWARE_ENABLE_MASK);

  	//Enable interrupt on the Interrupt Controller
  	Xil_Out32(0x41200000 + IER_OFFSET, MASK);


  	xil_printf("Wait for Interrupts.... \n\r");
  	while(1) {
  		if(counter == 10){
  			break;
  		}
  	}

  	xil_printf("Exit Application \n\r");
  	return 0;
}


int Handler()
{
	counter++;
	xil_printf("Interrupt #%d \n\r",counter);
	Xil_Out32(0x41200000 + IAR_OFFSET, MASK);
	return 0;
}

