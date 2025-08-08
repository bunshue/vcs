using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Text;

namespace vcs_Rhythm
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

        List<DateTime> points = new List<DateTime>();
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            points.Add(DateTime.Now);
            //PointF new_point = new PointF(e.X, e.Y);
            //points
            if (points.Count > 10)
            {
                double[] time_diff = new double[10];
                //richTextBox1.Text += points.ToArray().ToString() + "\n";
                for (int i = 0; i < (points.Count - 1); i++)
                {
                    //richTextBox1.Text += points[i].ToLongTimeString() +"\n";
                    //richTextBox1.Text += "耗時 : " + (DateTime.Now - bootup_time).TotalSeconds.ToString("0.00") + " 秒\n\n";

                    time_diff[i] = (points[i + 1] - points[i]).TotalMilliseconds;
                    //richTextBox1.Text += (points[i + 1] - points[i]).TotalMilliseconds.ToString() + "\n";
                }

                for (int i = 0; i < 10; i++)
                {
                    richTextBox1.Text += time_diff[i] + "\n";
                }

                int wid = pictureBox3.ClientSize.Width;
                int hgt = pictureBox3.ClientSize.Height;

                Bitmap bm = new Bitmap(wid, hgt);

                richTextBox1.Text += "sum =" + time_diff.Sum().ToString() + "\n";
                double total = time_diff.Sum();
                double ratio = total / wid;
                richTextBox1.Text += "ratio =" + ratio.ToString() + "\n";

                Graphics g = Graphics.FromImage(bm);
                g.SmoothingMode = SmoothingMode.AntiAlias;
                g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

                Pen p = Pens.Black;

                double current = 0;
                for (int i = 0; i < 10; i++)
                {
                    current += time_diff[i];
                    float x1 = (float)(current / ratio);
                    float y1 = (float)0;
                    float x2 = (float)(current / ratio);
                    float y2 = (float)hgt;

                    g.DrawLine(p, x1, y1, x2, y2);
                }
                pictureBox3.Image = bm;

                points.Clear();

            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {

        }
    }
}
