using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for CompositingQuality

namespace vcs_DrawTransparent
{
    public partial class Form1 : Form
    {

        string filename = @"C:\______test_files\_case1\\pic1.jpg";

        Graphics g;
        Pen p;
        Bitmap bitmap1;


        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //使用不透明和半透明筆刷繪製

            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);

            //g.DrawImage(bitmap1, 50, 50, bitmap1.Width, bitmap1.Height);

            SolidBrush opaqueBrush = new SolidBrush(Color.FromArgb(255, 0, 0, 255));
            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(60, 0, 0, 255));

            g.FillEllipse(opaqueBrush, 35, 45, 145, 130);
            g.FillEllipse(semiTransBrush, 186, 45, 145, 130);

            g.CompositingQuality = CompositingQuality.GammaCorrected;   //指定要在合成期間使用的品質等級。
            g.FillEllipse(semiTransBrush, 140, 190, 186, 130);

            pictureBox1.Image = bitmap1;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用不透明和半透明筆刷繪製

            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);

            //g.DrawImage(bitmap1, 50, 50, bitmap1.Width, bitmap1.Height);

            /*
            SolidBrush opaqueBrush = new SolidBrush(Color.FromArgb(255, 0, 0, 255));
            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(60, 0, 0, 255));

            g.FillEllipse(opaqueBrush, 35, 45, 145, 130);
            g.FillEllipse(semiTransBrush, 186, 45, 145, 130);

            g.CompositingQuality = CompositingQuality.GammaCorrected;   //指定要在合成期間使用的品質等級。
            g.FillEllipse(semiTransBrush, 140, 190, 186, 130);
            */


            g.DrawString("驗證完成", new Font("標楷體", 100), new SolidBrush(Color.Blue), new PointF(20, 20));
            g.DrawString("驗證完成", new Font("標楷體", 100), new SolidBrush(Color.FromArgb(60, 0, 0, 255)), new PointF(20, 220));

            pictureBox1.Image = bitmap1;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //使用不透明和半透明筆刷繪製

            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);

            //g.DrawImage(bitmap1, 50, 50, bitmap1.Width, bitmap1.Height);

            /*
            SolidBrush opaqueBrush = new SolidBrush(Color.FromArgb(255, 0, 0, 255));
            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(60, 0, 0, 255));

            g.FillEllipse(opaqueBrush, 35, 45, 145, 130);
            g.FillEllipse(semiTransBrush, 186, 45, 145, 130);

            g.CompositingQuality = CompositingQuality.GammaCorrected;   //指定要在合成期間使用的品質等級。
            g.FillEllipse(semiTransBrush, 140, 190, 186, 130);
            */


            g.DrawString("貓", new Font("標楷體", 220), new SolidBrush(Color.Blue), new PointF(20, 20));
            g.DrawString("熊", new Font("標楷體", 220), new SolidBrush(Color.FromArgb(60, 0, 0, 255)), new PointF(20, 220));

            pictureBox1.Image = bitmap1;

        }
    }
}
