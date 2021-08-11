using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


//參考/加入參考  CV UI Util

//加入/現有項目 core231 highgui231 並設為有更新時才複製

//壓縮影像錄影, 需要再添加:  opencv_ffmpeg_64.dll

/*
把*.csproj
    <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|x86' ">
    <PlatformTarget>x86</PlatformTarget>
改
    <PlatformTarget>x64</PlatformTarget>
*/

using Emgu.CV;
using Emgu.CV.Structure;
/*
using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.Util;

using Emgu.Util;
using Emgu.CV.CvEnum;
using System.Threading;
*/


namespace vcs_WebCam_Emgu1
{
    public partial class Form1 : Form
    {
        private Capture cap = null;             // Webcam物件
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標

        Emgu.CV.UI.ImageBox ib1 = new Emgu.CV.UI.ImageBox();
        Emgu.CV.UI.ImageBox ib2 = new Emgu.CV.UI.ImageBox();
        Emgu.CV.UI.ImageBox ib3 = new Emgu.CV.UI.ImageBox();
        Emgu.CV.UI.ImageBox ib4 = new Emgu.CV.UI.ImageBox();

        Label[] camera_function = new Label[4];

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
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

            //動態產生元件並指定屬性與事件
            for (int i = 0; i < camera_function.Length; i++)
            {
                camera_function[i] = new Label();
                //camera_function[i].AutoSize = false;
                camera_function[i].Name = "label" + i.ToString();
                //camera_function[i].Text = "XXXXXXXX";
                camera_function[i].Location = new Point(x_st + dx * (i % 2), y_st + dy * (i / 2) - 20);

                //ib1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

                //camera_function[i].Size = new Size(W, H);
                camera_function[i].Tag = "sample : " + i.ToString() + " is " + "empty";
                //camera_function[i].BackColor = Color.Gray;
                this.Controls.Add(camera_function[i]);
            }
        }

        private void Application_Idle(object sender, EventArgs arg)
        {
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面

            Image<Gray, Byte> grayFrame = image.Convert<Gray, Byte>();      //彩色轉灰階
            Image<Gray, Byte> smallGrayFrame = grayFrame.PyrDown();
            Image<Gray, Byte> smoothedGrayFrame = smallGrayFrame.PyrUp();
            Image<Gray, Byte> cannyFrame = smoothedGrayFrame.Canny(new Gray(100), new Gray(60));

            pictureBox1.Image = cannyFrame.ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件
            ib1.Image = image;
            ib2.Image = grayFrame;
            ib3.Image = smoothedGrayFrame;
            ib4.Image = cannyFrame;
        }

        private void ReleaseData()
        {
            if (cap != null)
                cap.Dispose();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (cap == null)
            {
                try
                {
                    cap = new Capture(1);   //預設使用第一台的webcam
                }
                catch (NullReferenceException excpt)
                {
                    MessageBox.Show(excpt.Message);
                }
            }

            if (cap != null)
            {
                if (flag_webcam_ok == false)
                {
                    button1.Text = "關閉Webcam";
                    flag_webcam_ok = true;
                    Application.Idle += Application_Idle;

                    camera_function[0].Text = "Captured Image";
                    camera_function[1].Text = "Grayscale Image";
                    camera_function[2].Text = "Smoothed Grayscale";
                    camera_function[3].Text = "Canny Edges";
                }
                else
                {
                    button1.Text = "開啟Webcam";
                    flag_webcam_ok = false;
                    Application.Idle -= Application_Idle;

                    camera_function[0].Text = "";
                    camera_function[1].Text = "";
                    camera_function[2].Text = "";
                    camera_function[3].Text = "";

                    pictureBox1.Image = null;
                    ib1.Image = null;
                    ib2.Image = null;
                    ib3.Image = null;
                    ib4.Image = null;
                }
            }


        }
    }
}
