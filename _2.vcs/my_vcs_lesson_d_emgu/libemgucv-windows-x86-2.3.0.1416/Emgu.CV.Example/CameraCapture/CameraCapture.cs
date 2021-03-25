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

        Emgu.CV.UI.ImageBox ib1 = new Emgu.CV.UI.ImageBox();
        Emgu.CV.UI.ImageBox ib2 = new Emgu.CV.UI.ImageBox();
        Emgu.CV.UI.ImageBox ib3 = new Emgu.CV.UI.ImageBox();
        Emgu.CV.UI.ImageBox ib4 = new Emgu.CV.UI.ImageBox();

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

            //captureImageBox.Image = frame;
            //grayscaleImageBox.Image = grayFrame;
            //smoothedGrayscaleImageBox.Image = smoothedGrayFrame;
            //cannyImageBox.Image = cannyFrame;

            pictureBox1.Image = cannyFrame.ToBitmap(); // 把畫面轉換成bitmap型態，在丟給pictureBox元件

            ib1.Image = frame;
            ib2.Image = grayFrame;
            ib3.Image = smoothedGrayFrame;
            ib4.Image = cannyFrame;
        }

        private void ReleaseData()
        {
            if (cap != null)
                cap.Dispose();
        }

        private void CameraCapture_Load(object sender, EventArgs e)
        {
            int W = 640;
            int H = 480;
            int w = W / 2;
            int h = H / 2;
            int dx = w + 50;
            int dy = h + 50;
            int x_st = 700;
            int y_st = 50;

            ib1.SizeMode = PictureBoxSizeMode.Zoom;
            ib1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            ib1.Size = new Size(w, h);
            this.Controls.Add(ib1);

            ib2.SizeMode = PictureBoxSizeMode.Zoom;
            ib2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            ib2.Size = new Size(w, h);
            this.Controls.Add(ib2);

            ib3.SizeMode = PictureBoxSizeMode.Zoom;
            ib3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            ib3.Size = new Size(w, h);
            this.Controls.Add(ib3);

            ib4.SizeMode = PictureBoxSizeMode.Zoom;
            ib4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            ib4.Size = new Size(w, h);
            this.Controls.Add(ib4);
        }

        private void button1_Click(object sender, EventArgs e)
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
                    button1.Text = "Start Capture";
                    Application.Idle -= ProcessFrame;
                }
                else
                {
                    //start the capture
                    button1.Text = "Stop";
                    Application.Idle += ProcessFrame;
                }

                flag_webcam_ok = !flag_webcam_ok;
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (cap != null) cap.FlipHorizontal = !cap.FlipHorizontal;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (cap != null) cap.FlipVertical = !cap.FlipVertical;
        }

    }
}
