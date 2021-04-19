using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Imaging;

namespace LevelInterleaving
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
                while (i <= intWidth / 2)
                {
                    for (int m = 0; m <= intHeight - 1; m++)
                    {
                        bitmap.SetPixel(i, m, myBitmap.GetPixel(i, m));
                    }
                    for (int n = 0; n <= intHeight - 1; n++)
                    {
                        bitmap.SetPixel(intWidth - i - 1, n, myBitmap.GetPixel(intWidth - i - 1, n));
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