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

        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
            pictureBox1.Size = new Size(bitmap1.Width, bitmap1.Height);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = UprightnessInterleaving(bitmap1);
        }

        Bitmap UprightnessInterleaving(Bitmap bitmap1)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.WhiteSmoke);
            Bitmap bitmap2 = new Bitmap(W, H);
            int i = 0;
            while (i <= H / 2)
            {
                for (int m = 0; m <= W - 1; m++)
                {
                    bitmap2.SetPixel(m, i, bitmap1.GetPixel(m, i));
                }
                for (int n = 0; n <= W - 1; n++)
                {
                    bitmap2.SetPixel(n, H - i - 1, bitmap1.GetPixel(n, H - i - 1));
                }
                i++;
                this.Refresh();
                pictureBox1.Image = bitmap2;
                System.Threading.Thread.Sleep(10);
            }
            return bitmap2;

        }
    }
}