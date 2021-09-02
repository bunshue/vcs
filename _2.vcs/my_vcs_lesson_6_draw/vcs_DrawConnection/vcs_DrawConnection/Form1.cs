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
            int i;

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

            for (i = 0; i < N; i++)
            {
                //richTextBox1.Text += i.ToString() + "\t" + Points[i].X.ToString() + "\t" + Points[i].Y.ToString() + "\n";

            }


            for (j = 0; j < N; j++)
            {
                for (i = 0; i < N; i++)
                {
                    e.Graphics.DrawLine(new Pen(Color.Red, 1), Points[i], Points[j]);

                }

            }



        }
    }
}
