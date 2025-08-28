using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace Mosaic
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            Image myImage = System.Drawing.Image.FromFile(filename);
            this.BackgroundImage = myImage;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap myBitmap = new Bitmap(this.BackgroundImage);
            int intWidth = myBitmap.Width / 50;
            int intHeight = myBitmap.Height / 50;
            Graphics myGraphics = this.CreateGraphics();
            myGraphics.Clear(Color.WhiteSmoke);
            Point[] myPoint = new Point[2500];
            for (int i = 0; i < 50; i++)
            {
                for (int j = 0; j < 50; j++)
                {
                    myPoint[i * 50 + j].X = i * intWidth;
                    myPoint[i * 50 + j].Y = j * intHeight;
                }
            }
            Bitmap bitmap = new Bitmap(myBitmap.Width, myBitmap.Height);
            for (int i = 0; i < 10000; i++)
            {
                Random rand = new Random();
                int intPos = rand.Next(2500);
                for (int m = 0; m < intWidth; m++)
                {
                    for (int n = 0; n < intHeight; n++)
                    {
                        bitmap.SetPixel(myPoint[intPos].X + m, myPoint[intPos].Y + n, myBitmap.GetPixel(myPoint[intPos].X + m, myPoint[intPos].Y + n));
                    }
                }
                this.Refresh();
                this.BackgroundImage = bitmap;
                for (int k = 0; k < 2500; k++)
                {
                    for (int m = 0; m < intWidth; m++)
                    {
                        for (int n = 0; n < intHeight; n++)
                        {
                            bitmap.SetPixel(myPoint[k].X + m, myPoint[k].Y + n, myBitmap.GetPixel(myPoint[k].X + m, myPoint[k].Y + n));
                        }
                    }
                    this.Refresh();
                    this.BackgroundImage = bitmap;
                }
            }
        }
    }
}
