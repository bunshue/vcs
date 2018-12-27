
#ifndef _PSUART0_H_
#define _PSUART0_H_

// *****************************************************
// Dependencies
// *****************************************************

#include "xscugic.h"
#include "xuartps.h"
//#include "main.h"
#include "periphs.h"

// *****************************************************
// Function status return values
// *****************************************************
#define PSUART0_SUCCESS        0
#define PSUART0_ERROR_UNKNOWN -1

#define PSUART0_BUFFER_SIZE	64

static u8 SendBuffer[PSUART0_BUFFER_SIZE];	/* Buffer for Transmitting Data */
static u8 RecvBuffer[PSUART0_BUFFER_SIZE];	/* Buffer for Receiving Data */

void psuart0_IntrHandler(void *CallBackRef, u32 Event, unsigned int EventData);
unsigned int psuart0_dongle_ping(void);
unsigned int test_dongle_read_write(void);
unsigned int dongle_read_data(unsigned int addr);
void psuart0_exposure(unsigned int exposure);

volatile int TotalReceivedCount;
volatile int TotalSentCount;
int TotalErrorCount;

#endif // _PSUART0_H_

