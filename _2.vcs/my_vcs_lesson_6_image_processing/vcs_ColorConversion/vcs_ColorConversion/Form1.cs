using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ColorConversion
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 80;

            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 7 + 25);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }


        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

        }

        private void button1_Click(object sender, EventArgs e)
        {

            //change

            int ratio_r = hScrollBar1.Value;
            int ratio_g = hScrollBar2.Value;
            int ratio_b = hScrollBar3.Value;

            string filename = @"C:\_git\vcs\_1.data\______test_files1\real1.bmp";

            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            richTextBox1.Text += "圖片寬度 : " + W.ToString() + "\n";
            richTextBox1.Text += "圖片高度 : " + H.ToString() + "\n";

            int i;
            int j;

            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    Color cc = bitmap1.GetPixel(i, j);
                    //bitmap1.SetPixel(i, j, Color.FromArgb(255, cc.R, cc.B, 0));
                    int R_old = cc.R;
                    int G_old = cc.G;
                    int B_old = cc.B;
                    int R_new = R_old * ratio_r / 100;
                    int G_new = G_old * ratio_g / 100;
                    int B_new = B_old * ratio_b / 100;
                    R_new -= 50;
                    if (R_new < 0)
                        R_new = 0;

                    B_new += 50;
                    if (B_new > 255)
                        B_new = 255;
                    bitmap1.SetPixel(i, j, Color.FromArgb(255, R_new, G_new, B_new));
                }
            }
            //Graphics g = Graphics.FromImage(bitmap1);
            //g.DrawRectangle(Pens.Red, 5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10);

            pictureBox1.Image = bitmap1;


        }

    }
}
