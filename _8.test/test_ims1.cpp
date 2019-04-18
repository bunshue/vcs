#include "stdafx.h"
#include <iostream>
using namespace std;

#define FALSE						0
#define TRUE						1

typedef signed char		int8_t;
typedef unsigned char	uint8_t;
typedef signed short	int16_t;
typedef unsigned short	uint16_t;
typedef signed int		int32_t;
typedef unsigned int	uint32_t;

struct struct_vres_timing_t
{
	char *pName;
	uint32_t VActiveVideo;
	uint32_t VFrontPorch;
	uint32_t VSyncWidth;
	uint32_t VBackPorch;
	uint32_t VSyncPolarity;
	uint32_t HActiveVideo;
	uint32_t HFrontPorch;
	uint32_t HSyncWidth;
	uint32_t HBackPorch;
	uint32_t HSyncPolarity;
};
typedef struct struct_vres_timing_t vres_timing_t;

#define NUM_VIDEO_RESOLUTIONS      9

vres_timing_t vres_resolutions[NUM_VIDEO_RESOLUTIONS] = {
   // name     vav,  vfp,  vsw,  vbp,  vsp,  hav,  hfp,  hsw,  hbp,  hsp
   { "VGA",    480,   10,    2,   33,    0,  640,   16,   96,   48,    0 }, // VIDEO_RESOLUTION_VGA
   { "480P",   480,    9,    6,   30,    0,  720,   16,   62,   60,    0 }, // VIDEO_RESOLUTION_480P
   { "576P",   576,    5,    5,   39,    0,  720,   12,   64,   68,    0 }, // VIDEO_RESOLUTION_576P
   { "SVGA",   600,    1,    4,   23,    1,  800,   40,  128,   88,    1 }, // VIDEO_RESOLUTION_SVGA
   { "XGA",    768,    3,    6,   29,    0, 1024,   24,  136,  160,    0 }, // VIDEO_RESOLUTION_XGA
   { "720P",   720,    5,    5,   20,    1, 1280,  110,   40,  220,    1 }, // VIDEO_RESOLUTION_720P
   { "SXGA",  1024,    1,    3,   26,    0, 1280,   48,  184,  200,    0 }, // VIDEO_RESOLUTION_SXGA
   { "1080P", 1080,    4,    5,   36,    1, 1920,   88,   44,  148,    1 }, // VIDEO_RESOLUTION_1080P
   { "UXGA",  1200,    1,    3,   46,    0, 1600,   64,  192,  304,    0 }  // VIDEO_RESOLUTION_UXGA
};

char *vres_get_name(uint32_t resolutionId)
{
   if ( resolutionId < NUM_VIDEO_RESOLUTIONS )
   {
      return vres_resolutions[resolutionId].pName;
   }
   else
   {
      return "{UNKNOWN}";
   }
}

uint32_t vres_get_width(uint32_t resolutionId)
{
   return vres_resolutions[resolutionId].HActiveVideo; // horizontal active
}

uint32_t vres_get_height(uint32_t resolutionId)
{
   return vres_resolutions[resolutionId].VActiveVideo; // vertical active
}

int32_t vres_detect()
{
  int32_t i;

  for ( i = 0; i < NUM_VIDEO_RESOLUTIONS+2; i++ )
  {
		printf( "Detected Video Resolution = %s\n", vres_get_name(i) );
  }  
  return 0;
}

typedef uint8_t u8;
typedef uint16_t u16;
typedef uint32_t u32;

typedef struct {
	char label[64]; /* Label describing the resolution */
	u32 width; /*Width of the active video frame*/
	u32 height; /*Height of the active video frame*/
	u32 hps; /*Start time of Horizontal sync pulse, in pixel clocks (active width + H. front porch)*/
	u32 hpe; /*End time of Horizontal sync pulse, in pixel clocks (active width + H. front porch + H. sync width)*/
	u32 hmax; /*Total number of pixel clocks per line (active width + H. front porch + H. sync width + H. back porch) */
	u32 hpol; /*hsync pulse polarity*/
	u32 vps; /*Start time of Vertical sync pulse, in lines (active height + V. front porch)*/
	u32 vpe; /*End time of Vertical sync pulse, in lines (active height + V. front porch + V. sync width)*/
	u32 vmax; /*Total number of lines per frame (active height + V. front porch + V. sync width + V. back porch) */
	u32 vpol; /*vsync pulse polarity*/
	double freq; /*Pixel Clock frequency*/
} VideoMode;


/*
 * This driver currently supports 3 frames.
 */
#define DISPLAY_NUM_FRAMES 3

/* ------------------------------------------------------------ */
/*					General Type Declarations					*/
/* ------------------------------------------------------------ */

typedef enum {
	DISPLAY_STOPPED = 0,
	DISPLAY_RUNNING = 1
} DisplayState;

typedef struct {
		u32 dynClkAddr; /*Physical Base address of the dynclk core*/
		//XAxiVdma *vdma; /*VDMA driver struct*/
		//XAxiVdma_DmaSetup vdmaConfig; /*VDMA channel configuration*/
		//XVtc vtc; /*VTC driver struct*/
		VideoMode vMode; /*Current Video mode*/
		u8 *framePtr[DISPLAY_NUM_FRAMES]; /* Array of pointers to the framebuffers */
		u32 stride; /* The line stride of the framebuffers, in bytes */
		double pxlFreq; /* Frequency of clock currently being generated */
		u32 curFrame; /* Current frame being displayed */
		DisplayState state; /* Indicates if the Display is currently running */
} DisplayCtrl;


DisplayCtrl dispCtrl;

typedef unsigned int	DWORD;

DWORD get_fattime (void)
{
	return	((DWORD)(2010U - 1980U) << 25U)	/* Fixed to Jan. 1, 2010 */
		| ((DWORD)1 << 21)
		| ((DWORD)1 << 16)
		| ((DWORD)0 << 11)
		| ((DWORD)0 << 5)
		| ((DWORD)0 >> 1);
}

int XIicPs_SetDate(u32 year, u8 month, u8 date, u8 day, u8 hour, u8 minutes, u8 seconds);
void ShowDateInfo(u8 *RecvBuffer);

int main()
{
	cout << "歡迎使用C++！\n";
	printf("This is a lion-mouse.\n");
	vres_detect();


	DWORD dw;
	dw = get_fattime();
	printf("dw = 0x%x\n",dw);


	printf("\n\n");



		//XIicPs_SetDate(2018, 7, 20, 5, 11, 25, 30);
	//XIicPs_SetDate(2018, 11, 22, 5, 22, 33, 44);
	u8 data[30];
	u8 name[] = "lion-mouse";
	u8 send_data[31];
	int i;
	for(i = 0 ;i<30;i++)
		data[i] = '_';
	for(i = 0 ;i<30;i++)
		printf("%c", data[i]);
	printf("\n");
	data = &name[0];


	





	getchar();//或system("pause");
	return 0;
}



int XIicPs_SetDate(u32 year, u8 month, u8 date, u8 day, u8 hour, u8 minutes, u8 seconds)
{
	//int Status;
	u8 RecvBuffer[7];
	printf("raw data: %d/%d/%d %d %d:%d:%d\r\n", year, month, date, day, hour, minutes, seconds);

	seconds = ((seconds/10)<<4) + (seconds % 10);
	minutes = ((minutes/10)<<4) + (minutes % 10);
	hour = ((hour/10)<<4) + (hour % 10);
	date = ((date/10)<<4) + (date % 10);
	month = ((month/10)<<4) + (month % 10);
	year = (((year-1970)/10)<<4) + ((year-1970) % 10);

	printf("new data: %d/%d/%d %d %d:%d:%d\r\n", year, month, date, day, hour, minutes, seconds);

	printf("\n\n");

	RecvBuffer[0] = seconds;
	RecvBuffer[1] = minutes;
	RecvBuffer[2] = hour;
	RecvBuffer[3] = day;
	RecvBuffer[4] = date;
	RecvBuffer[5] = month;
	RecvBuffer[6] = year;

	ShowDateInfo(RecvBuffer);


	return 0;
}

void ShowDateInfo(u8 *RecvBuffer)
{
	u8 seconds = (((RecvBuffer[0] >> 4) & 0x07) * 10) + (RecvBuffer[0] & 0x0f);
	u8 minutes = (((RecvBuffer[1] >> 4) & 0x07) * 10) + (RecvBuffer[1] & 0x0f);
	u8 hour = (((RecvBuffer[2] >> 4) & 0x07) * 10) + (RecvBuffer[2] & 0x0f);
	u8 day = RecvBuffer[3] & 0x07;
	u8 date = (((RecvBuffer[4] >> 4) & 0x03) * 10) + (RecvBuffer[4] & 0x0f);
	u8 month = (((RecvBuffer[5] >> 4) & 0x01) * 10) + (RecvBuffer[5] & 0x0f);
	u32 year = (((RecvBuffer[6] >> 4) & 0x0f) * 10) + (RecvBuffer[6] & 0x0f) +1970;

	printf("raw data: %d/%d/%d %d %d:%d:%d\r\n", RecvBuffer[6], RecvBuffer[5], RecvBuffer[4], RecvBuffer[3], RecvBuffer[2], RecvBuffer[1], RecvBuffer[0]);
	printf("new data: %d/%d/%d %d %d:%d:%d\r\n", year, month, date, day, hour, minutes, seconds);
	printf("Date: %d/%d/%d %d:%d:%d\r\n", year, month, date, hour, minutes, seconds);

}

