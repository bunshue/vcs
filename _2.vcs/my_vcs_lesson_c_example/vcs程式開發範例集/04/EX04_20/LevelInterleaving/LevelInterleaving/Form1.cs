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
            pictureBox1.Image = LevelInterleaving(bitmap1);
        }

        Bitmap LevelInterleaving(Bitmap bitmap1)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.WhiteSmoke);
            Bitmap bitmap2 = new Bitmap(W, H);
            int i = 0;
            while (i <= W / 2)
            {
                for (int m = 0; m <= H - 1; m++)
                {
                    bitmap2.SetPixel(i, m, bitmap1.GetPixel(i, m));
                }
                for (int n = 0; n <= H - 1; n++)
                {
                    bitmap2.SetPixel(W - i - 1, n, bitmap1.GetPixel(W - i - 1, n));
                }
                i++;
                this.Refresh();
                this.pictureBox1.Image = bitmap2;
                System.Threading.Thread.Sleep(10);
            }



            return bitmap2;
        }

    }
}