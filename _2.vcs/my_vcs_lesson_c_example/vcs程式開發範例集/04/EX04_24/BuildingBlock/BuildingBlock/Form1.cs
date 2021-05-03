using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace BuildingBlock
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Image image = Image.FromFile(filename);
            pictureBox1.Image = image;
        }

        Bitmap ToBlock(Bitmap bitmap1)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            int W, H, i, j, iAvg, iPixel;
            Color myColor, myNewColor;
            RectangleF myRect;
            W = bitmap1.Width;
            H = bitmap1.Height;
            myRect = new RectangleF(0, 0, W, H);
            Bitmap bitmap = bitmap1.Clone(myRect, System.Drawing.Imaging.PixelFormat.DontCare);
            i = 0;
            while (i < W - 1)
            {
                j = 0;
                while (j < H - 1)
                {
                    myColor = bitmap.GetPixel(i, j);
                    iAvg = (myColor.R + myColor.G + myColor.B) / 3;
                    iPixel = 0;
                    if (iAvg >= 128)
                        iPixel = 255;
                    else
                        iPixel = 0;
                    myNewColor = Color.FromArgb(255, iPixel, iPixel, iPixel);
                    bitmap.SetPixel(i, j, myNewColor);
                    j = j + 1;
                }
                i = i + 1;
            }
            g.Clear(Color.WhiteSmoke);
            g.DrawImage(bitmap, new Rectangle(0, 0, W, H));

            return bitmap;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap bmp = new Bitmap(filename);

            pictureBox1.Image = ToBlock(bmp);
        }
    }
}

