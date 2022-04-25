using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Paint8
{
    public partial class Form1 : Form
    {
        bool flag_start_capture = false;
        bool flag_mouse_down = false;

        //收集滑鼠點數

        //公用變數
        List<PointF> Points1 = new List<PointF>();
        List<PointF> Points2 = new List<PointF>();
        int cnt = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            flag_start_capture = true;
            cnt = 0;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int len = Points1.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (flag_start_capture == true)
            {
                flag_mouse_down = true;
                Points1 = new List<PointF>();
                timer1.Enabled = true;
            }

        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                Points1.Add(e.Location);
                this.pictureBox1.Invalidate();
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                timer1.Enabled = false;

                timer2.Enabled = true;
                Points2.Clear();
                flag_mouse_down = false;
                flag_start_capture = false;
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {

        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            int len = Points1.Count;
            Points2.Add(Points1[cnt]);
            pictureBox2.Invalidate();

            cnt++;
            if (cnt >= len)
            {
                timer2.Enabled = false;

            }


        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            if (Points1.Count > 1)
            {
                e.Graphics.DrawCurve(Pens.Red, Points1.ToArray());
            }
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            if (Points2.Count > 1)
            {
                e.Graphics.DrawCurve(Pens.Red, Points2.ToArray());
            }

        }

    }
}
