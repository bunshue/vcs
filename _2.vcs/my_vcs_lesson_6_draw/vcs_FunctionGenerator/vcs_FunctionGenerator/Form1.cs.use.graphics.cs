using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//用 Graphics 做

namespace vcs_FunctionGenerator
{
    public partial class Form1 : Form
    {
        int time = 0;
        double signal = 0;
        bool flag_increase = true;

        private const int N = 15;
        double[] y1_data = new double[N];
        int draw_max = 0;
        int draw_min = 0;
        int draw_zero = 0;
        private const int BORDER_W = 5;     //5% border
        private const int BORDER_H = 5;     //5% border

        int W;
        int H;
        int w;
        int h;
        int ratio_x = 1;
        int ratio_y = 1;
        int offset_x = 0;
        int offset_y = 0;

        Graphics g;

        public Form1()
        {
            InitializeComponent();
            g = panel1.CreateGraphics();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            W = panel1.Width;
            H = panel1.Height;
            w = W * (100 - BORDER_W * 2) / 100;
            h = H * (100 - BORDER_H * 2) / 100;
            offset_x = W * BORDER_W / 100;
            offset_y = H * BORDER_H / 100;

            check_signal_range();

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            int i;

            time++;

            if (rb_1.Checked == true)
            {
                if (flag_increase == true)
                    signal++;
                else
                    signal--;
                if (signal >= 10)
                    flag_increase = false;
                else if (signal <= -10)
                    flag_increase = true;
                signal += (double)numericUpDown_dc.Value;
            }
            else if (rb_2.Checked == true)
            {
                time %= 36;
                signal = 10 * (Math.Sin((Math.PI * (time * 10) / 180))) + (double)numericUpDown_dc.Value;
                richTextBox1.Text += "x = " + (time * 10).ToString() + ", y = " + signal.ToString() + "  ";
            }
            else if (rb_3.Checked == true)
            {
                Random r = new Random();
                signal = r.NextDouble() * 20 - 10 + (double)numericUpDown_dc.Value;
            }
            else
            {
                signal = (double)numericUpDown_dc.Value;
            }

            label1.Text = time.ToString();
            label2.Text = signal.ToString();

            double y1_value = 0;

            y1_value = signal;

            for (i = 0; i < (N - 1); i++)
            {
                y1_data[i] = y1_data[i + 1];
            }
            y1_data[N - 1] = y1_value * ratio_y;

            // Create pens.
            Pen redPen = new Pen(Color.Red, 3);

            g.Clear(Color.White);

            DrawLines();

            Point[] curvePoints = new Point[N];    //一維陣列內有 N 個Point

            for (i = 0; i < N; i++)
            {
                curvePoints[i].X = offset_x + ratio_x * i;
                //curvePoints[i].Y = H - (int)y1_data[i] - 100;
                //curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + (draw_max - draw_min) / 2000) * 2;
                curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + h / 2);
            }

            // Draw lines between original points to screen.
            g.DrawLines(redPen, curvePoints);   //畫直線

            // Draw curve to screen.
            //g.DrawCurve(redPen, curvePoints); //畫曲線
        }

        private void rb_1_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_1.Checked == true)
                check_signal_range();
        }

        private void rb_2_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_2.Checked == true)
                check_signal_range();
        }

        private void rb_3_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_3.Checked == true)
                check_signal_range();
        }

        private void rb_4_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_4.Checked == true)
                check_signal_range();
        }

        void check_signal_range()
        {
            if (rb_1.Checked == true)
            {
                draw_max = 10 + (int)numericUpDown_dc.Value;
                draw_min = -10 + (int)numericUpDown_dc.Value;
                draw_zero = (int)numericUpDown_dc.Value;
                richTextBox1.Text += "線性\tMax=" + draw_max.ToString() + ", min=" + draw_min.ToString() + ", zero=" + draw_zero.ToString() + "\n";
            }
            else if (rb_2.Checked == true)
            {
                draw_max = 10 + (int)numericUpDown_dc.Value;
                draw_min = -10 + (int)numericUpDown_dc.Value;
                draw_zero = (int)numericUpDown_dc.Value;
                richTextBox1.Text += "正弦\tMax=" + draw_max.ToString() + ", min=" + draw_min.ToString() + ", zero=" + draw_zero.ToString() + "\n";
            }
            else if (rb_3.Checked == true)
            {
                draw_max = 10 + (int)numericUpDown_dc.Value;
                draw_min = -10 + (int)numericUpDown_dc.Value;
                draw_zero = (int)numericUpDown_dc.Value;
                richTextBox1.Text += "隨機\tMax=" + draw_max.ToString() + ", min=" + draw_min.ToString() + ", zero=" + draw_zero.ToString() + "\n";
            }
            else if (rb_4.Checked == true)
            {
                draw_max = 10;
                draw_min = -10;
                draw_zero = 0;
                richTextBox1.Text += "DC\tMax=" + draw_max.ToString() + ", min=" + draw_min.ToString() + ", zero=" + draw_zero.ToString() + "\n";
            }
            else
            {
                draw_max = 10;
                draw_min = -10;
                draw_zero = 0;
                richTextBox1.Text += "XXXXXX\n";
            }

            double y_max = draw_max;
            double y_min = draw_min;
            double y_range = y_max - y_min;

            ratio_x = (int)((double)w / N);
            ratio_y = (int)((double)h / y_range);

            richTextBox1.Text += "pictureBox width = " + W.ToString() + "\n";
            richTextBox1.Text += "pictureBox height = " + H.ToString() + "\n";
            richTextBox1.Text += "pictureBox draw width = " + w.ToString() + "\n";
            richTextBox1.Text += "pictureBox draw height = " + h.ToString() + "\n";

            richTextBox1.Text += "y_max = " + y_max.ToString() + "\n";
            richTextBox1.Text += "y_min = " + y_min.ToString() + "\n";
            richTextBox1.Text += "y_range = " + y_range.ToString() + "\n";

            richTextBox1.Text += "ratio_x = " + ratio_x.ToString() + "\n";
            richTextBox1.Text += "ratio_y = " + ratio_y.ToString() + "\n";
        }

        private void numericUpDown_dc_ValueChanged(object sender, EventArgs e)
        {
            check_signal_range();
        }

        void DrawLines()
        {
            Point px1 = new Point(panel1.Width * BORDER_W / 100, panel1.Height * (100 - BORDER_H) / 100);
            Point px2 = new Point(panel1.Width * (100 - BORDER_W) / 100, panel1.Height * (100 - BORDER_H) / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            Point py1 = new Point(panel1.Width * BORDER_W / 100, panel1.Height * (100 - BORDER_H) / 100);
            Point py2 = new Point(panel1.Width * BORDER_W / 100, panel1.Height * BORDER_H / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);

            int x1;
            int x2;
            int y1;
            int y2;

            x1 = offset_x;
            y1 = offset_y + h / 2;
            x2 = offset_x + w;
            y2 = y1;

            Point pt1 = new Point(x1, y1);
            Point pt2 = new Point(x2, y2);
            g.DrawLine(new Pen(Brushes.Pink, 1), pt1, pt2);


        }
    }
}
