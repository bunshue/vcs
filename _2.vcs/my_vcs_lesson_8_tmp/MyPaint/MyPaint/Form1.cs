using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;


namespace MyPaint
{
    public partial class Form1 : Form
    {
        private Point startPoint, oldPoint; //繪圖時紀錄滑鼠位置
        private bool isDrawing = false;     //是否正在繪圖
        private Image theImage;             //進行操作的bitmap
        Graphics g;         //Graphics實例
        Graphics ig;        //繪製bitmap的Graphics實例
        Color foreColor = Color.Red;
        Color backColor = Color.White;
        Pen PenStyle;

        public Form1()
        {
            InitializeComponent();
            //創建一個bitmap
            theImage = new Bitmap(this.ClientRectangle.Width, this.ClientRectangle.Height);
            g = this.CreateGraphics();
            ig = Graphics.FromImage(theImage);
            ig.Clear(backColor);

            PenStyle = new Pen(foreColor);
            PenStyle.Width = (int)numericUpDown1.Value;
            PenStyle.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.EndCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.Color = foreColor;


            //PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel;
            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Round;

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if ((isDrawing = !isDrawing) == true)
            {
                startPoint = new Point(e.X, e.Y);
                oldPoint = new Point(e.X, e.Y);
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDrawing)
            {
                g.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                ig.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                oldPoint.X = e.X;
                oldPoint.Y = e.Y;
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            isDrawing = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = "image." + DateTime.Now.ToString("yyyy.MMdd.HHmm.ss") + ".bmp";
            theImage.Save(filename, ImageFormat.Bmp);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            g.Clear(backColor);
            ig.Clear(backColor);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                foreColor = colorDialog1.Color;
                PenStyle.Color = foreColor;
            }

        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            PenStyle.Width = (int)numericUpDown1.Value;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Point p1, p2;

            p1 = new Point();
            p2 = new Point();

            p1.X = 50;
            p1.Y = 50;
            p2.X = 250;
            p2.Y = 250;

            g.DrawLine(PenStyle, p1, p2);
            ig.DrawLine(PenStyle, p1, p2);

            p1.X = 400;
            p1.Y = 200;

            g.DrawLine(PenStyle, p2, p1);
            ig.DrawLine(PenStyle, p2, p1);
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }
    }
}
