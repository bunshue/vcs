
// *****************************************************
// Dependencies
// *****************************************************
#include "mixer.h"
#include "main.h"


// *****************************************************
// Private functions
// *****************************************************

/*****************************************************************************/
/**
 * This function configures Mixer for defined mode
 *
 * @return none
 *
 *****************************************************************************/

void ConfigMixer(XV_Mix_l2 *mix, XVidC_VideoStream *StreamPtr, unsigned int MemAddr)
{
  XV_Mix_l2 *MixerPtr = mix;
  //XVidC_VideoWindow layer1;
  //XVidC_VideoWindow layer2, layer3;
  uint32_t  Status;
  //uint32_t baseaddr, Stride;
  //XVidC_ColorFormat Cfmt;
  //uint32_t MemAddr, NumLayers, index;

  /* Setup default config after reset */
  XVMix_LayerDisable(MixerPtr, XVMIX_LAYER_MASTER);
  //XVMix_LayerDisable(MixerPtr, XVMIX_LAYER_1);
  //XVMix_LayerDisable(MixerPtr, XVMIX_LAYER_2);
  //XVMix_LayerDisable(MixerPtr, XVMIX_LAYER_3);
  XVMix_SetVidStream(MixerPtr, StreamPtr);

  // Set up GUI Layer 3 address
//  Status = XVMix_SetLayerBufferAddr(MixerPtr, XVMIX_LAYER_3, MemAddr);
//  if (Status != XST_SUCCESS) {
//	  xil_printf("MIXER ERROR:: Unable to set layer %d buffer addr to 0x%X\r\n", index, MemAddr);
//  }

  /* Set Memory Layer Addresses */
  //NumLayers = XVMix_GetNumLayers(MixerPtr);
//  MemAddr = XVMIX_LAYER1_BASEADDR;
//  for(index = XVMIX_LAYER_1; index < NumLayers; ++index) {
//      Status = XVMix_SetLayerBufferAddr(MixerPtr, index, MemAddr);
//      if(Status != XST_SUCCESS) {
//          xil_printf("MIXER ERR:: Unable to set layer %d buffer addr to 0x%X\r\n",
//                      index, MemAddr);
//      } else {
//      //    MemAddr += XVMIX_LAYER_ADDR_OFFSET;
//      }
//  }

//  if(XVMix_IsLogoEnabled(MixerPtr)) {
//    XVidC_VideoWindow Win;
//
//    Win.StartX = 64;
//    Win.StartY = 64;
//    Win.Width  = 64;
//    Win.Height = 64;
//
//    Status = XVMix_LoadLogo(MixerPtr,
//                            &Win,
//                            Logo_R,
//                            Logo_G,
//                            Logo_B);
//    if(Status != XST_SUCCESS) {
//      xil_printf("MIXER ERR:: Unable to load Logo \r\n");
//    }
//
//    if(XVMix_IsLogoPixAlphaEnabled(MixerPtr)) {
//      Status = XVMix_LoadLogoPixelAlpha(MixerPtr, &Win, Logo_A);
//      if(Status != XST_SUCCESS) {
//        xil_printf("MIXER ERR:: Unable to load Logo pixel alpha \r\n");
//      }
//    }
//  } else {
//      xil_printf("INFO: Logo Layer Disabled in HW \r\n");
//  }
  XVMix_SetBackgndColor(MixerPtr, XVMIX_BKGND_BLUE, StreamPtr->ColorDepth);


  XVMix_LayerEnable(MixerPtr, XVMIX_LAYER_MASTER);
//  XVMix_LayerEnable(MixerPtr, XVMIX_LAYER_1);
//  XVMix_LayerEnable(MixerPtr, XVMIX_LAYER_2);
//  XVMix_LayerEnable(MixerPtr, XVMIX_LAYER_3);
  XVMix_InterruptDisable(MixerPtr); // use auto reload mode

  XVMix_Start(MixerPtr);
  xil_printf("INFO: Mixer configured for TPG image\r\n");
}

void RunMixer(XV_Mix_l2 *mix)
{
  XV_Mix_l2 *MixerPtr = mix;
  XVidC_VideoWindow layer1;
  XVidC_VideoWindow layer2, layer3;
  uint32_t baseaddr, Stride;
  uint32_t  Status;
  XVidC_ColorFormat Cfmt;

  //xil_printf("\r\n--> Test Memory Layer 3\r\n");3
  baseaddr = XVMix_GetLayerBufferAddr(MixerPtr, XVMIX_LAYER_3);
  xil_printf("\r\nLayer 3 Buffer Addr: 0x%X\r\n", baseaddr);

  // Set up layer 1
  XVMix_GetLayerColorFormat(MixerPtr, XVMIX_LAYER_1, &Cfmt);
  xil_printf("\r\nLayer 1 Color Format: %s\r\n", XVidC_GetColorFormatStr(Cfmt));
  //Stride = ((Cfmt == XVIDC_CSF_YCRCB_422) ? 2: 4); //BytesPerPixel
  Stride = 0; // Not used for streaming channels

  // Camera Freeze Layer
  layer1.Width = LAYER1_WIDTH;
  layer1.Height = LAYER1_HEIGHT;
  layer1.StartX = LAYER0_WIDTH-LAYER1_WIDTH-BORDER_X;
  layer1.StartY = BORDER_Y;

  xil_printf("Set Layer 1 Window (%3d, %3d, %3d, %3d): ",
          layer1.StartX, layer1.StartY, layer1.Width, layer1.Height);
  Status = XVMix_SetLayerWindow(MixerPtr, XVMIX_LAYER_1, &layer1, Stride);
  if(Status != XST_SUCCESS) {
      xil_printf("<ERR:: Command Failed>\r\n");
      //++ErrorCount;
  } else {
      xil_printf("Done\r\n");
  }

  xil_printf("Set Layer 1 Alpha to %d: ", XVMIX_ALPHA_MAX);
  if(XVMix_IsAlphaEnabled(MixerPtr, XVMIX_LAYER_1)) {
    Status = XVMix_SetLayerAlpha(MixerPtr, XVMIX_LAYER_1, XVMIX_ALPHA_MAX);
    if(Status != XST_SUCCESS) {
      xil_printf("<ERR:: Command Failed>\r\n");
      //++ErrorCount;
    } else {
      xil_printf("Done\r\n");
    }
  } else {
      xil_printf("(Disabled in HW)\r\n");
  }

//  xil_printf("Enable Layer 1: ");
//  Status = XVMix_LayerEnable(MixerPtr, XVMIX_LAYER_1);
//  if(Status != XST_SUCCESS) {
//      xil_printf("<ERR:: Command Failed>\r\n");
//  } else {
//      xil_printf("Done\r\n");
//  }

  XVMix_DbgLayerInfo(MixerPtr, XVMIX_LAYER_1);


  // Set up layer 2
  XVMix_GetLayerColorFormat(MixerPtr, XVMIX_LAYER_2, &Cfmt);
  xil_printf("\r\nLayer 2 Color Format: %s\r\n", XVidC_GetColorFormatStr(Cfmt));
  //Stride = ((Cfmt == XVIDC_CSF_YCRCB_422) ? 2: 4); //BytesPerPixel
  Stride = 0; // Not used for streaming channels

  // Camera Layer
  layer2.Width = LAYER2_WIDTH;
  layer2.Height = LAYER2_HEIGHT;
  layer2.StartX = BORDER_X;
  layer2.StartY = LAYER0_HEIGHT-LAYER2_HEIGHT-BORDER_Y;


  xil_printf("Set Layer 2 Window (%3d, %3d, %3d, %3d): ",
          layer2.StartX, layer2.StartY, layer2.Width, layer2.Height);
  Status = XVMix_SetLayerWindow(MixerPtr, XVMIX_LAYER_2, &layer2, Stride);
  if(Status != XST_SUCCESS) {
      xil_printf("<ERR:: Command Failed>\r\n");
      //++ErrorCount;
  } else {
      xil_printf("Done\r\n");
  }

  xil_printf("Set Layer 2 Alpha to %d: ", XVMIX_ALPHA_MAX);
  if(XVMix_IsAlphaEnabled(MixerPtr, XVMIX_LAYER_2)) {
    Status = XVMix_SetLayerAlpha(MixerPtr, XVMIX_LAYER_1, XVMIX_ALPHA_MAX);
    if(Status != XST_SUCCESS) {
      xil_printf("<ERR:: Command Failed>\r\n");
      //++ErrorCount;
    } else {
      xil_printf("Done\r\n");
    }
  } else {
      xil_printf("(Disabled in HW)\r\n");
  }

//  xil_printf("Enable Layer 2: ");
//  Status = XVMix_LayerEnable(MixerPtr, XVMIX_LAYER_2);
//  if(Status != XST_SUCCESS) {
//      xil_printf("<ERR:: Command Failed>\r\n");
//  } else {
//      xil_printf("Done\r\n");
//  }

  XVMix_DbgLayerInfo(MixerPtr, XVMIX_LAYER_2);

  // Set up layer 3
  XVMix_GetLayerColorFormat(MixerPtr, XVMIX_LAYER_3, &Cfmt);
  xil_printf("\r\nLayer 3 Color Format: %s\r\n", XVidC_GetColorFormatStr(Cfmt));
  //Stride = ((Cfmt == XVIDC_CSF_YCRCB_422) ? 2: 4); //BytesPerPixel
  Stride = GUI_STRIDE;

  // GUI Layer
  layer3.Width = LAYER3_WIDTH;
  layer3.Height = LAYER3_HEIGHT;
  layer3.StartX = 0;
  layer3.StartY = 0;

  xil_printf("Set Layer 3 Window (%3d, %3d, %3d, %3d): ",
          layer3.StartX, layer3.StartY, layer3.Width, layer3.Height);
  Status = XVMix_SetLayerWindow(MixerPtr, XVMIX_LAYER_3, &layer3, Stride);
  if(Status != XST_SUCCESS) {
      xil_printf("<ERR:: Command Failed>: %d\r\n", Status);
      //++ErrorCount;
  } else {
      xil_printf("Done\r\n");
  }

  xil_printf("Set Layer 3 Alpha to %d: ", XVMIX_ALPHA_MAX);
  if(XVMix_IsAlphaEnabled(MixerPtr, XVMIX_LAYER_3)) {
    Status = XVMix_SetLayerAlpha(MixerPtr, XVMIX_LAYER_3, XVMIX_ALPHA_MAX);
    if(Status != XST_SUCCESS) {
      xil_printf("<ERR:: Command Failed>\r\n");
      //++ErrorCount;
    } else {
      xil_printf("Done\r\n");
    }
  } else {
      xil_printf("(Disabled in HW)\r\n");
  }

  xil_printf("Enable Layer 3: ");
  Status = XVMix_LayerEnable(MixerPtr, XVMIX_LAYER_3);
  if(Status != XST_SUCCESS) {
      xil_printf("<ERR:: Command Failed>\r\n");
  } else {
      xil_printf("Done\r\n");
  }

  XVMix_DbgLayerInfo(MixerPtr, XVMIX_LAYER_3);


}
