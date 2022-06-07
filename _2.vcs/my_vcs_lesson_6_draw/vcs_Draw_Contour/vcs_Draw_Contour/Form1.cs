using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Contour
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }


        int COLUMN = 360 + 1 + 360;
        int ROW = 360 + 1 + 360;

        void draw_contour(int cx, int cy)
        {
            int i, j;
            //                    R   C
            //int[,] gray = new int[ROW, COLUMN];    //Row = 19, Column = 8
            double[,] brightness = new double[ROW, COLUMN];    //Row = 19, Column = 8
            int[,] brightness2 = new int[ROW, COLUMN];    //Row = 19, Column = 8

            //richTextBox1.Text += "assign value\n";

            double stepx = 360.0 / ((COLUMN - 1) / 2);
            double stepy = 360.0 / ((ROW - 1) / 2);

            double max = 0;
            double min = 100;
            double vv = 0;

            richTextBox1.Text += "stepx = " + stepx.ToString() + "\n";
            richTextBox1.Text += "stepy = " + stepy.ToString() + "\n";


            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COLUMN; i++)
                {
                    //gray[j, i] = (i - COLUMN / 2) * 10 + (j - ROW / 2) * 10;

                    //vv = cosd((i - COLUMN / 2) * stepx) + cosd((j - ROW / 2) * stepy);
                    vv = cosd((i - cx) * 1) + cosd((j - cy) * 1);

                    brightness[j, i] = vv;
                    if (vv > max)
                        max = vv;
                    else if (vv < min)
                        min = vv;

                    //對應到0~255
                    brightness2[j, i] = (int)((vv + 2.0) * 64);
                    if (brightness2[j, i] == 256)
                        brightness2[j, i] = 255;
                    brightness2[j, i] = (brightness2[j, i] / 5) * 5;
                }
            }

            richTextBox1.Text += "max = " + max.ToString() + "\n";
            richTextBox1.Text += "min = " + min.ToString() + "\n";


            /*
            richTextBox1.Text += "print value\n";
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    richTextBox1.Text += gray[j, i].ToString("D2") + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            /*
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    //richTextBox1.Text += brightness[j, i].ToString("D2") + "\t";
                    //richTextBox1.Text += brightness[j, i].ToString() + "\t";
                    richTextBox1.Text += ((int)(brightness[j, i] * 100)).ToString("D2") + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            //逐點製作圖檔

            Bitmap bitmap1 = new Bitmap(COLUMN, ROW);

            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COLUMN; i++)
                {
                    //bitmap1.SetPixel(i, j, Color.FromArgb(255, (byte)(brightness[j, i] * 100), (byte)(brightness[j, i] * 100), (byte)(brightness[j, i] * 100)));
                    bitmap1.SetPixel(i, j, Color.FromArgb(255, (byte)(brightness2[j, i]), (byte)(brightness2[j, i]), (byte)(brightness2[j, i])));
                }
            }

            /*
            Graphics g = Graphics.FromImage(bitmap1);
            Pen p = new Pen(Color.Red, 5);
            Point point1a = new Point(0, 360);
            Point point2a = new Point(720, 360);
            g.DrawLine(p, point1a, point2a);

            point1a = new Point(360, 0);
            point2a = new Point(360, 720);
            g.DrawLine(p, point1a, point2a);
            */

            pictureBox1.Image = bitmap1;
            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;


        }
        private void button1_Click(object sender, EventArgs e)
        {
            draw_contour(cx, cy);
        }

        int dd = 20;
        int cx = 360;
        int cy = 360;
        private void timer1_Tick(object sender, EventArgs e)
        {
            cx += dd;
            cy += dd;
            if (cx > 721)
                cx = dd;
            if (cy > 721)
                cy = dd;
            draw_contour(cx, cy);
        }
    }
}
