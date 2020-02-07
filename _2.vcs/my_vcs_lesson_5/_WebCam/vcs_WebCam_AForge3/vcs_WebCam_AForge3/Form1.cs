using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Imaging;   //for ImageFormat

using AForge.Video;             //需要添加這兩個.dll, 參考/加入參考/瀏覽此二檔
using AForge.Video.DirectShow;

/*
Aforge.Net 安裝路徑設定
Solution Explorer(方案總管) => References(參考)(右鍵) => Add Reference(加入參考) => AForge.Net的Release資料夾
加入AForge.Video.dll、AForge.Video.DirectShow.dll
*/

namespace vcs_WebCam_AForge3
{
    public partial class Form1 : Form
    {
        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

        //AForge下載鏈結
        //http://www.aforgenet.com/framework/downloads.html

        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        int[] saturation_array = new int[81];
        int[] saturation_deny_array = new int[81];

        int awb_x = 0;
        int awb_y = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                Cam.Start();   // WebCam starts capturing images.

                //以下為WebCam訊息與調整視窗大小
                Cam.VideoResolution = Cam.VideoCapabilities[0];
                string webcam_name = string.Empty;
                int ww;
                int hh;
                ww = Cam.VideoCapabilities[0].FrameSize.Width;
                hh = Cam.VideoCapabilities[0].FrameSize.Height;
                webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                this.Text = webcam_name;

                pictureBox1.Size = new Size(ww, hh);
                pictureBox1.Location = new Point(50, 50);
                this.ClientSize = new Size(pictureBox1.Size.Width + 100, pictureBox1.Size.Height + 100);
            }
            else
            {
                this.Text = "無影像裝置";
            }
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (Cam != null)
            {
                if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                {
                    Cam.Stop();   // WebCam stops capturing images.
                    Cam.SignalToStop();
                    Cam.WaitForStop();
                }
            }
        }

        public Bitmap bm = null;
        Graphics g;
        SolidBrush drawBrush;
        Font drawFont1;

        //自定義函數, 捕獲每一幀圖像並顯示
        /*  old
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();
            //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
            pictureBox1.Image = bm;

            GC.Collect();       //回收資源
        }
        */

        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            bm = (Bitmap)eventArgs.Frame.Clone();
            g = Graphics.FromImage(bm);

            int i;
            int j;
            int A;
            int R;
            int G;
            int B;

            int x_st = 0;
            int y_st = 0;


            int W = bm.Width;
            int H = bm.Height;
            int center_x = W / 2;
            int center_y = H / 2;

            int awb_block = 32;     //AWB block size width, height
            int awb_search_size = 256 + 32;   //256X256


            x_st = center_x - awb_search_size / 2;
            y_st = center_y - awb_search_size / 2;

            for (i = 0; i <= (awb_search_size / awb_block); i++)
            {
                g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + awb_search_size - 1, y_st + awb_block * i);
                g.DrawLine(new Pen(Color.Red, 1), x_st + awb_block * i, y_st, x_st + awb_block * i, y_st + awb_search_size - 1);
            }

            for (i = 0; i < saturation_array.Length; i++)
            {
                saturation_array[i] = 0;
            }

            int upper_bound = 255;
            for (j = y_st; j < (y_st + awb_search_size); j++)
            {
                for (i = x_st; i < (x_st + awb_search_size); i++)
                {
                    Color pp = bm.GetPixel(i, j);

                    A = pp.A;
                    R = pp.R;
                    G = pp.G;
                    B = pp.B;

                    if ((R >= upper_bound) && (G >= upper_bound) && (B >= upper_bound))
                    {
                        saturation_array[((i - x_st) / awb_block) + (((j - y_st) / awb_block)) * (awb_search_size / awb_block)]++;

                    }
                }
            }

            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(40, 0, 255, 0));
            SolidBrush semiTransBrushRed = new SolidBrush(Color.FromArgb(40, 255, 0, 0));
            //richTextBox1.Text += "\nresult:\n";

            int ii = 0;
            int jj = 0;
            int xx;
            int yy;

            for (i = 0; i < saturation_array.Length; i++)
            {
                //richTextBox1.Text += "saturation_array[" + i.ToString() + "] = " + saturation_array[i].ToString() + "\n";
                if (saturation_array[i] <= 40)
                {
                    if (saturation_deny_array[i] == 1)
                    {
                        xx = (i % (awb_search_size / awb_block));
                        yy = (i / (awb_search_size / awb_block));

                        g.FillRectangle(semiTransBrushRed, new Rectangle(x_st + awb_block * xx, y_st + awb_block * yy, awb_block, awb_block));
                    }
                    else
                    {
                        xx = (i % (awb_search_size / awb_block));
                        yy = (i / (awb_search_size / awb_block));

                        g.FillRectangle(semiTransBrush, new Rectangle(x_st + awb_block * xx, y_st + awb_block * yy, awb_block, awb_block));
                    }
                }
            }
            semiTransBrush = new SolidBrush(Color.FromArgb(60, 255, 0, 0));
            //g.FillRectangle(semiTransBrush, new Rectangle(x_st + awb_block * ii, y_st + awb_block * jj, awb_block, awb_block));
            //g.DrawRectangle(new Pen(Color.Red, 3), new Rectangle(x_st + awb_block * ii + 3, y_st + awb_block * jj + 3, awb_block - 6, awb_block - 6));
            g.DrawRectangle(new Pen(Color.Red, 1), new Rectangle(x_st + awb_block * ii + 2, y_st + awb_block * jj + 2, awb_block - 4, awb_block - 4));

            drawBrush = new SolidBrush(Color.Red);
            drawFont1 = new Font("Arial", 16, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);

            x_st = 200;
            y_st = 20;
            //g.DrawString(tmp, drawFont1, drawBrush, x_st, y_st);

            x_st = 580;
            y_st = 390 - 100 + 30;

            g.DrawRectangle(new Pen(Color.Red, 1), new Rectangle(x_st, y_st, 50, 25));
            g.DrawRectangle(new Pen(Color.Red, 1), new Rectangle(x_st, y_st + 25, 50, 40));

            //upper_bound
            drawBrush = new SolidBrush(Color.Red);
            drawFont1 = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
            g.DrawString(upper_bound.ToString(), drawFont1, drawBrush, x_st, y_st);

            g.DrawString(saturation_array[awb_x + awb_y * 9].ToString(), drawFont1, drawBrush, x_st + 8, y_st + 30);



            pictureBox1.Image = bm;

            GC.Collect();       //回收資源
        }
    
    }
}
