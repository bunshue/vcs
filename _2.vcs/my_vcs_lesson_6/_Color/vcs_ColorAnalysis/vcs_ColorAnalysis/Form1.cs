using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ColorAnalysis
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\ims03.bmp";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            Graphics g = Graphics.FromImage(bitmap1);   //畫字用
            g.DrawString("分析一張圖的畫素的顏色", new Font("標楷體", 38), new SolidBrush(Color.Blue), new PointF(20, 100));
            pictureBox1.Image = bitmap1;
        }

        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            using (Bitmap bm = new Bitmap(pictureBox1.Image))
            {
                Color color = bm.GetPixel(e.X, e.Y);

                label1.Text = e.X.ToString() + ", " + e.Y.ToString();
                label2.Text = color.ToString();

                int r = color.R;
                int g = color.G;
                int b = color.B;
                if ((r > 192) && (g < 64) && (b < 64))
                {
                    label3.Text = "很紅";
                }
                else if ((r < 64) && (g > 192) && (b < 64))
                {
                    label3.Text = "很綠";
                }
                else if ((r < 64) && (g < 64) && (b > 192))
                {
                    label3.Text = "很藍";
                }
                else if ((r > 192) && (g > 192) && (b < 64))
                {
                    label3.Text = "很黃";
                }
                else if ((r > 192) && (g < 64) && (b > 192))
                {
                    label3.Text = "很洋紅";
                }
                else if ((r < 64) && (g > 192) && (b > 192))
                {
                    label3.Text = "很綠藍";
                }
                else if ((r < 64) && (g < 64) && (b < 64))
                {
                    label3.Text = "很暗";
                }
                else if ((r > 192) && (g > 192) && (b > 192))
                {
                    label3.Text = "很亮";
                }
                else if ((r > 128) && (g < 128) && (b < 128))
                {
                    label3.Text = "偏紅";
                }
                else if ((r < 128) && (g > 128) && (b < 128))
                {
                    label3.Text = "偏綠";
                }
                else if ((r < 128) && (g < 128) && (b > 128))
                {
                    label3.Text = "偏藍";
                }
                else if ((r > 128) && (g > 128) && (b < 128))
                {
                    label3.Text = "偏黃";
                }
                else if ((r > 128) && (g < 128) && (b > 128))
                {
                    label3.Text = "偏洋紅";
                }
                else if ((r < 128) && (g > 128) && (b > 128))
                {
                    label3.Text = "偏綠藍";
                }
                else if ((r < 128) && (g < 128) && (b < 128))
                {
                    label3.Text = "偏暗";
                }
                else if ((r > 128) && (g > 128) && (b > 128))
                {
                    label3.Text = "偏亮";
                }
                else
                {
                    label3.Text = "";
                }

                pictureBox2.BackColor = Color.FromArgb(r, g, b);
            }
        }
    }
}
