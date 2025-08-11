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
                    //time_diff[i] = 50 + 10 * i;//debug

                    richTextBox1.Text += time_diff[i] + "\n";
                }

                //畫在 pictureBox2
                int wid = pictureBox2.ClientSize.Width;
                int hgt = pictureBox2.ClientSize.Height;

                Bitmap bm = new Bitmap(wid, hgt);

                richTextBox1.Text += "wid =" + wid.ToString() + "\n";
                richTextBox1.Text += "hgt =" + hgt.ToString() + "\n";
                richTextBox1.Text += "sum =" + time_diff.Sum().ToString() + "\n";
                //double total = time_diff.Sum();
                //double ratio = total / wid;
                //richTextBox1.Text += "ratio =" + ratio.ToString() + "\n";
                double max = time_diff.Max();
                double min = time_diff.Min();
                double avg = time_diff.Average();
                double diff1 = max - avg;
                double diff2 = avg - min;
                double diff = 0;
                if (diff1 > diff2)
                    diff = diff1;
                else
                    diff = diff2;

                double ratio = wid / (diff * 2);

                richTextBox1.Text += "max =" + max.ToString() + "\n";
                richTextBox1.Text += "min =" + min.ToString() + "\n";
                richTextBox1.Text += "avg =" + avg.ToString() + "\n";
                richTextBox1.Text += "diff =" + diff.ToString() + "\n";
                richTextBox1.Text += "ratio =" + ratio.ToString() + "\n";

                Graphics g = Graphics.FromImage(bm);
                g.SmoothingMode = SmoothingMode.AntiAlias;
                g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

                Pen p = new Pen(Brushes.Red, 5);
                //g.DrawRectangle(Pens.Red, new Rectangle(20, 20, 100, 100));

                for (int i = 0; i < 10; i++)
                {
                    float x1 = (float)((time_diff[i]-min) * ratio);
                    float y1 = (float)0;
                    float x2 = (float)((time_diff[i] - min) * ratio);
                    float y2 = (float)hgt;

                    g.DrawLine(p, x1, y1, x2, y2);
                }




                pictureBox2.Image = bm;





                //畫在 pictureBox3
                wid = pictureBox3.ClientSize.Width;
                hgt = pictureBox3.ClientSize.Height;

                bm = new Bitmap(wid, hgt);

                richTextBox1.Text += "sum =" + time_diff.Sum().ToString() + "\n";
                double total = time_diff.Sum();
                ratio = total / wid;
                richTextBox1.Text += "ratio =" + ratio.ToString() + "\n";

                g = Graphics.FromImage(bm);
                g.SmoothingMode = SmoothingMode.AntiAlias;
                g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

                p = Pens.Black;

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
