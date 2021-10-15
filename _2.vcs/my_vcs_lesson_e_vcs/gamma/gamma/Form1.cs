using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ColorAdjustType
namespace gamma
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            Image img = Image.FromFile(filename);
            pictureBox1.Image = img;


        }

        private void button1_Click(object sender, EventArgs e)
        {
            float gamma = 1.5f;

            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;


            Bitmap bitmap2 = KiGamma(bitmap1, gamma);

            pictureBox1.Image = bitmap2;

        }


        //C#圖片處理之Gamma校正
        //gamma值是用曲線表示的，這是一種人的眼睛對光的一種感應曲線，其中包括了物理量、身理感官及心理的感知度。

        /// <summary>
        /// Gamma校正
        /// </summary>
        /// <param name="bmp">輸入Bitmap</param>
        /// <param name="val">[0 <-明- 1 -暗-> 2]</param>
        /// <returns>輸出Bitmap</returns>
        public static Bitmap KiGamma(Bitmap bmp, float val)
        {
            if (bmp == null)
            {
                return null;
            }

            // 1表示無變化，就不做
            if (val == 1.0000f) return bmp;

            try
            {
                Bitmap b = new Bitmap(bmp.Width, bmp.Height);
                Graphics g = Graphics.FromImage(b);
                ImageAttributes attr = new ImageAttributes();

                attr.SetGamma(val, ColorAdjustType.Bitmap);
                g.DrawImage(bmp, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, attr);
                g.Dispose();
                return b;
            }
            catch
            {
                return null;
            }
        }


    }
}
