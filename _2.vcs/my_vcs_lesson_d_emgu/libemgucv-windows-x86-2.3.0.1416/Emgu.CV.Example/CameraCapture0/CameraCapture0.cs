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

namespace CameraCapture0
{
    public partial class CameraCapture0 : Form
    {
        private Capture cap = null;             // Webcam����
        private bool flag_webcam_ok = false;    //�P�_�O�_�Ұ�webcam���X��

        public CameraCapture0()
        {
            InitializeComponent();
        }

        private void Application_Idle(object sender, EventArgs arg)
        {
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam ���e��
            pictureBox1.Image = image.ToBitmap(); // ��e���ഫ��bitmap���A�A�A�ᵹpictureBox����

            /*  ��L�B�z
            Image<Gray, Byte> grayFrame = image.Convert<Gray, Byte>();      //�m����Ƕ�
            Image<Gray, Byte> smallGrayFrame = grayFrame.PyrDown();
            Image<Gray, Byte> smoothedGrayFrame = smallGrayFrame.PyrUp();
            Image<Gray, Byte> cannyFrame = smoothedGrayFrame.Canny(new Gray(100), new Gray(60));
            */
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
                if (flag_webcam_ok == false)
        {
                    button1.Text = "����Webcam";
                    flag_webcam_ok = true;
                    Application.Idle += Application_Idle;
                }
                else
                {
                    button1.Text = "�}��Webcam";
                    flag_webcam_ok = false;
                    Application.Idle -= Application_Idle;
                }
            }
        }

        private void ReleaseData()
        {
            if (cap != null)
            {
                cap.Dispose();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (cap != null)
            {
                cap.FlipHorizontal = !cap.FlipHorizontal;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (cap != null)
            {
                cap.FlipVertical = !cap.FlipVertical;
            }
        }
    }
}
