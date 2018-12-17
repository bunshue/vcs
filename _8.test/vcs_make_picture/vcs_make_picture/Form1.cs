using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_make_picture
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int xx;
            int yy;
            int width = 640;
            int height = 480;
            pictureBox1.Size = new Size(width, height);
            Bitmap bmp = new Bitmap(width, height);
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //Color p = Color.FromName("SlateBlue");
                    /*
                    Color p ;
                    p.A = (byte)(xx % 255);
                    p.R = (byte)(xx % 127 + 127);
                    p.G = (byte)(xx % 127);
                    p.B = (byte)(xx % 63);
                    */


                    //獲取像素的ＲＧＢ顏色值
                    //srcColor = srcBitmap.GetPixel(x, y);
                    //byte temp = (byte)(srcColor.R * .299 + srcColor.G * .587 + srcColor.B * .114);

                    //byte temp = (byte)((byte)(xx % 255) + (byte)(xx % 127 + 127) + (byte)(xx % 63));

                    byte aa = (byte)(xx % 255);
                    byte rr = (byte)(xx % 127 + 127);
                    byte gg = (byte)(xx % 127);
                    byte bb = (byte)(xx % 63);

                    aa = 30;
                    rr = 200;
                    gg = 110;
                    bb = 110;

                    //設置像素的ＲＧＢ顏色值
                    bmp.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                }
            }
            pictureBox1.Image = bmp;

            bmp.Save("D:\\my_picture.jpg", ImageFormat.Jpeg);
            bmp.Save("D:\\my_picture.png", ImageFormat.Png);
            bmp.Save("D:\\my_picture.bmp", ImageFormat.Bmp);
        }
    }
}
