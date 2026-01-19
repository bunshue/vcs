using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw6_Rectangle1
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
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.DoubleBuffered = true;

            //創建一個bitmap
            theImage = new Bitmap(this.ClientRectangle.Width, this.ClientRectangle.Height);
            g = this.CreateGraphics();
            ig = Graphics.FromImage(theImage);
            ig.Clear(backColor);

            PenStyle = new Pen(foreColor);
            PenStyle.Width = 8;
            PenStyle.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.EndCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.Color = foreColor;

            //PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel;
            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Round;
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                //如果开始绘制，则开始记录鼠标位置
                if ((isDrawing = !isDrawing) == true)
                {
                    startPoint = new Point(e.X, e.Y);
                    oldPoint = new Point(e.X, e.Y);
                }
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDrawing)
            {
                //首先恢复此次操作之前的图像，然后再添加Rectangle
                this.Form1_Paint(this, new PaintEventArgs(this.CreateGraphics(), this.ClientRectangle));
                g.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            isDrawing = false;
            ig.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            //将Image中保存的图像，绘制出来
            Graphics g = this.CreateGraphics();
            if (theImage != null)
            {
                g.Clear(Color.White);
                g.DrawImage(theImage, this.ClientRectangle);
            }

        }

        private void Form1_SizeChanged(object sender, EventArgs e)
        {
            this.Form1_Paint(this, new PaintEventArgs(this.CreateGraphics(), this.ClientRectangle));
        }

    }
}
