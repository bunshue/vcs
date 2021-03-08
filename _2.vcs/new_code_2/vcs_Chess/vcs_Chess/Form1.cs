using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Chess
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        byte[,] S;
        Bitmap bmp;
        Graphics g;

        private void Form1_Load(object sender, EventArgs e)
        {
            bmp = new Bitmap(570, 570);
            g = Graphics.FromImage(bmp);
            g.Clear(Color.White);
            int i;
            int j;
            for (i = 15; i <= 555; i += 30)
            {
                g.DrawLine(Pens.Black, i, 15, i, 555);
            }
            for (j = 15; j <= 555; j += 30)
            {
                g.DrawLine(Pens.Black, 15, j, 555, j);
            }
            panel1.BackgroundImage = bmp;

            //g.DrawRectangle(Pens.Red, 100, 100, 100, 100);
            S = new byte[19, 19];
        }

        void Chess(int i, int j, Color BW)
        {
            int w = 26;
            int h = 26;
            int x_st = i * 30 + 2;
            int y_st = j * 30 + 2;
            g.FillEllipse(Brushes.Black, x_st, y_st, w, h);

            g.DrawRectangle(Pens.Red, 100, 100, 100, 100);

            this.Text = i.ToString() + ", " + j.ToString();
            panel1.BackgroundImage = bmp;


        }

        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {
            int i = e.X / 30;
            int j = e.Y / 30;
            if (S[i, j] == 0)
            {
                Chess(i, j, Color.Black);
                S[i, j] = 1;

            }

        }
    }
}
