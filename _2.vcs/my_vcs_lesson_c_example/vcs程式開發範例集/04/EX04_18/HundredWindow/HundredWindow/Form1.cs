using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Imaging;

namespace HundredWindow
{
    public partial class Form1 : Form
    {
        Image myImage;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp|*.jpg;*.jpeg;*.bmp";
            openFileDialog1.ShowDialog();
            myImage = System.Drawing.Image.FromFile(openFileDialog1.FileName);
            this.BackgroundImage = myImage;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                Bitmap myBitmap = (Bitmap)this.BackgroundImage.Clone();
                int intWidth = myBitmap.Width;
                int intHeight = myBitmap.Height / 20;
                Graphics myGraphics = this.CreateGraphics();
                myGraphics.Clear(Color.WhiteSmoke);
                Point[] myPoint = new Point[30];
                for (int i = 0; i < 30; i++)
                {
                    myPoint[i].X = 0;
                    myPoint[i].Y = i * intHeight;
                }
                Bitmap bitmap = new Bitmap(myBitmap.Width, myBitmap.Height);
                for (int m = 0; m < intHeight; m++)
                {
                    for (int n = 0; n < 20; n++)
                    {
                        for (int j = 0; j < intWidth; j++)
                        {
                            bitmap.SetPixel(myPoint[n].X + j, myPoint[n].Y + m, myBitmap.GetPixel(myPoint[n].X + j, myPoint[n].Y + m));
                        }
                    }
                    this.Refresh();
                    this.BackgroundImage = bitmap;
                    System.Threading.Thread.Sleep(100);
                }
            }
            catch { }
        }
    }
}