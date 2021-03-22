//----------------------------------------------------------------------------
//  Copyright (C) 2004-2011 by EMGU. All rights reserved.       
//----------------------------------------------------------------------------

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.Util;

namespace CameraCapture
{
   public partial class CameraCapture : Form
   {
                                           private Capture cap = null;             // Webcam物件
                                           private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標

      public CameraCapture()
      {
         InitializeComponent();
      }

                                                  private void ProcessFrame(object sender, EventArgs arg)
                                                  {
                                                      Image<Bgr, Byte> frame = cap.QueryFrame();

                                                     Image<Gray, Byte> grayFrame = frame.Convert<Gray, Byte>();
                                                     Image<Gray, Byte> smallGrayFrame = grayFrame.PyrDown();
                                                     Image<Gray, Byte> smoothedGrayFrame = smallGrayFrame.PyrUp();
                                                     Image<Gray, Byte> cannyFrame = smoothedGrayFrame.Canny(new Gray(100), new Gray(60));

                                                     captureImageBox.Image = frame;
                                                     //grayscaleImageBox.Image = grayFrame;
                                                     //smoothedGrayscaleImageBox.Image = smoothedGrayFrame;
                                                     //cannyImageBox.Image = cannyFrame;
                                                  }

      private void captureButtonClick(object sender, EventArgs e)
      {
                                                     #region if capture is not created, create it now
                                                      if (cap == null)
                                                     {
                                                        try
                                                        {
                                                            cap = new Capture();
                                                        }
                                                        catch (NullReferenceException excpt)
                                                        {
                                                           MessageBox.Show(excpt.Message);
                                                        }
                                                     }
                                                     #endregion

                                                      if (cap != null)
                                                     {
                                                         if (flag_webcam_ok)
                                                        {  //stop the capture
                                                           captureButton.Text = "Start Capture";
                                                           Application.Idle -= ProcessFrame;
                                                        }
                                                        else
                                                        {
                                                           //start the capture
                                                           captureButton.Text = "Stop";
                                                           Application.Idle += ProcessFrame;
                                                        }

                                                        flag_webcam_ok = !flag_webcam_ok;
                                                     }
      }

      private void ReleaseData()
      {
          if (cap != null)
              cap.Dispose();
      }

      private void FlipHorizontalButtonClick(object sender, EventArgs e)
      {
                                            if (cap != null) cap.FlipHorizontal = !cap.FlipHorizontal;
      }

      private void FlipVerticalButtonClick(object sender, EventArgs e)
      {
                                            if (cap != null) cap.FlipVertical = !cap.FlipVertical;
      }
   }
}
