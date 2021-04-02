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
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp|*.jpg;*.jpeg;*.bmp";
            openFileDialog1.ShowDialog();
            Image myImage = System.Drawing.Image.FromFile(openFileDialog1.FileName);
            this.BackgroundImage = myImage;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Graphics myGraphics = this.CreateGraphics();
            Bitmap myBitmap = new Bitmap(this.BackgroundImage);
            int myWidth, myHeight, i, j, iAvg, iPixel;
            Color myColor, myNewColor;
            RectangleF myRect;
            myWidth = myBitmap.Width;
            myHeight = myBitmap.Height;
            myRect = new RectangleF(0, 0, myWidth, myHeight);
            Bitmap bitmap = myBitmap.Clone(myRect, System.Drawing.Imaging.PixelFormat.DontCare);
            i = 0;
            while (i < myWidth - 1)
            {
                j = 0;
                while (j < myHeight - 1)
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
            myGraphics.Clear(Color.WhiteSmoke);
            myGraphics.DrawImage(bitmap, new Rectangle(0, 0, myWidth, myHeight));
        }
    }
}