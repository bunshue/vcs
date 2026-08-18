using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Draw1b
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Size = new Size(1200, 860);
            this.Text = "vcs_Draw1b";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            Pen pen = new Pen(Color.Black, 1);

            draw_grid(g);

            Font f_index = new Font("Arial", 80, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.FromArgb(128, 255, 0, 0));

            int x_center = 110;
            int y_center = 120;
            g.DrawString("1", f_index, sb, new PointF(x_center, y_center));
            g.DrawRectangle(Pens.Red, x_center, y_center, 100, 100);

            double radius = 100;

            double[] x = new double[10];
            double[] y = new double[10];

            for (int i = 0; i <= 9; i++)
            {
                x[i] = x_center + radius * Math.Sin(36 * i * Math.PI / 180.0);
                y[i] = y_center + radius * Math.Cos(36 * i * Math.PI / 180);
            }

            for (int i = 0; i <= 9; i++)
            {
                for (int j = 0; j <= 9; j++)
                {
                    g.DrawLine(pen, (int)x[i], (int)y[i], (int)x[j], (int)y[j]);
                }
            }

            //------------------------------------------------------------  # 60個

            double xx;
            double yy;
            Point[] pts = new Point[100];

            x_center = 380;
            y_center = 120;
            g.DrawString("2", f_index, sb, new PointF(x_center, y_center));
            g.DrawRectangle(Pens.Red, x_center, y_center, 100, 100);

            radius = 100;

            for (int i = 0; i <= 99; i++)
            {
                xx = x_center + radius * Math.Sin(36 * i * Math.PI / 180);
                yy = y_center + radius * Math.Cos(36 * i * Math.PI / 180);
                pts[i] = new Point((int)xx, (int)yy);
                radius -= 1;
            }
            g.DrawLines(pen, pts);

            //------------------------------------------------------------  # 60個

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            Image img = Image.FromFile(filename);
            g.DrawImage(img, 0, 10 + 500);
            g.DrawImageUnscaled(img, 250, 10 + 500);
        }

        void draw_grid(Graphics g)
        {
            int W = this.Width;
            int H = this.Height;
            for (int i = 0; i <= W; i += 100)
            {
                g.DrawLine(Pens.Gray, i, 0, i, H);
            }
            for (int j = 0; j <= H; j += 100)
            {
                g.DrawLine(Pens.Gray, 0, j, W, j);
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

