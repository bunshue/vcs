using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
平面任意N點互相連線

根據這N點 每點小小移動  再連線
*/

namespace vcs_DrawConnection
{
    public partial class Form1 : Form
    {
        int W;
        int H;

        int N = 30;

        List<Point> Points = new List<Point>();

        Graphics g;

        int type = 1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Points.Clear();
            W = this.pictureBox1.Width;
            H = this.pictureBox1.Height;
            g = this.pictureBox1.CreateGraphics();


        }

        private void button1_Click(object sender, EventArgs e)
        {

            this.pictureBox1.Invalidate();

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int i;
            int j;

            Random r = new Random();
            Points.Clear();
            for (i = 0; i < N; i++)
            {
                Points.Add(new Point(r.Next(W), r.Next(H)));
            }

            /*
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + Points[i].X.ToString() + "\t" + Points[i].Y.ToString() + "\n";
            }
            */

            for (j = 0; j < N; j++)
            {
                for (i = 0; i < N; i++)
                {
                    e.Graphics.DrawLine(new Pen(Color.Red, 1), Points[i], Points[j]);
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int N = 100000;
            int H = 500;
            int A = 30;

            int[] rnd = new int[N];
            int[] result = new int[H];

            richTextBox1.Text += "N = " + N.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";

            Random r = new Random();

            int i;
            for (i = 0; i < N; i++)
            {
                rnd[i] = r.Next(H);
            }

            for (i = 0; i < H; i++)
            {
                result[i] = 0;
            }

            for (i = 0; i < N; i++)
            {
                result[rnd[i]]++;
            }

            /*
            richTextBox1.Text += "rnd array\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += rnd[i].ToString() + " ";
            }

            richTextBox1.Text += "\n\n";

            richTextBox1.Text += "result array\n";
            for (i = 0; i < H; i++)
            {
                richTextBox1.Text += result[i].ToString() + " ";
            }
            richTextBox1.Text += "\n\n";
            */

            Graphics g = pictureBox1.CreateGraphics();

            int ratio = 2;

            Pen redPen = new Pen(Color.Red, 1);
            Point[] curvePoints = new Point[H];    //一維陣列內有 H 個Point

            for (i = 0; i < H; i++)
            {
                curvePoints[i].X = i;
                curvePoints[i].Y = result[i] * ratio;
            }
            // Draw lines between original points to screen.
            //g.DrawLines(redPen, curvePoints);   //畫直線

            for (i = 0; i < H; i++)
            {
                g.FillEllipse(Brushes.Red, curvePoints[i].X, curvePoints[i].Y, 5, 5);

            }




        }

        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                richTextBox1.Text += "兩兩相連\n";
                type = 1;
            }
            else if (radioButton2.Checked == true)
            {
                richTextBox1.Text += "圓點\n";
                type = 2;
            }
            else if (radioButton3.Checked == true)
            {
                richTextBox1.Text += "圓點連線\n";
                type = 3;
            }
            else if (radioButton4.Checked == true)
            {
                richTextBox1.Text += "布朗運動\n";
                type = 4;
            }
            else
            {
                richTextBox1.Text += "XXXXXX\n";
                type = 1;
            }

            this.pictureBox1.Invalidate();
        }
    }
}
