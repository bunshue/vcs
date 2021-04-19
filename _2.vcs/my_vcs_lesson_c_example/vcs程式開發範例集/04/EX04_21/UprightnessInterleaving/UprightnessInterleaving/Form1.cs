using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace UprightnessInterleaving
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        Bitmap myBitmap;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Image myImage = System.Drawing.Image.FromFile(filename);
            myBitmap = new Bitmap(myImage);
            this.BackgroundImage = myBitmap;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                int intWidth = this.BackgroundImage.Width;
                int intHeight = this.BackgroundImage.Height;
                Graphics myGraphics = this.CreateGraphics();
                myGraphics.Clear(Color.WhiteSmoke);
                Bitmap bitmap = new Bitmap(intWidth, intHeight);
                int i = 0;
                while (i <= intHeight / 2)
                {
                    for (int m = 0; m <= intWidth - 1; m++)
                    {
                        bitmap.SetPixel(m, i, myBitmap.GetPixel(m, i));
                    }
                    for (int n = 0; n <= intWidth - 1; n++)
                    {
                        bitmap.SetPixel(n, intHeight - i - 1, myBitmap.GetPixel(n, intHeight - i - 1));
                    }
                    i++;
                    this.Refresh();
                    this.BackgroundImage = bitmap;
                    System.Threading.Thread.Sleep(10);
                }
            }
            catch { }
        }
    }
}