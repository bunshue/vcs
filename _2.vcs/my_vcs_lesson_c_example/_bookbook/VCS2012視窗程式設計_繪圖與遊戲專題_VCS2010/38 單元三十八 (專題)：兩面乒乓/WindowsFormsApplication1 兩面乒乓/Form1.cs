using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Point Ball_Pos;    // 球的位置
        Point Ball_Vel = new Point(-3, -5); // 球的速度
        int Ball_D = 15;  // 球的半徑

        Point Mouse_Pos;     // 滑鼠的位置
        int Bar_Length = 50; // 擋板的長度的一半
        int Bar_Margin = 10;  // 擋板離邊界的距離

        Pen myPen = new Pen(Color.Red, 6);
        Pen myPen2 = new Pen(Color.Pink, 3);

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(800, 400);
            myPen2.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
            Ball_Pos = new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 球
            e.Graphics.FillEllipse(Brushes.Blue, Ball_Pos.X - Ball_D, Ball_Pos.Y - Ball_D, Ball_D * 2, Ball_D * 2);
            e.Graphics.DrawEllipse(Pens.Black, Ball_Pos.X - Ball_D, Ball_Pos.Y - Ball_D, Ball_D * 2, Ball_D * 2);

            // 對準輔助虛線
            e.Graphics.DrawLine(myPen2, Mouse_Pos.X, 0, Mouse_Pos.X, this.ClientSize.Height - Bar_Margin);
            e.Graphics.DrawLine(myPen2, 0, Mouse_Pos.Y, this.ClientSize.Width - Bar_Margin, Mouse_Pos.Y);

            // 擋板
            e.Graphics.DrawLine(myPen, Mouse_Pos.X - Bar_Length, this.ClientSize.Height - Bar_Margin, Mouse_Pos.X + Bar_Length, this.ClientSize.Height - Bar_Margin);
            e.Graphics.DrawLine(myPen, this.ClientSize.Width - Bar_Margin, Mouse_Pos.Y - Bar_Length, this.ClientSize.Width - Bar_Margin, Mouse_Pos.Y + Bar_Length);
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            Mouse_Pos = e.Location;
            //this.Invalidate();  //重畫會影響 球的速度
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Ball_Pos.X = Ball_Pos.X + Ball_Vel.X; // 球移動
            if (Ball_Pos.X < Ball_D)  // 碰到 左邊界
            {
                Ball_Pos.X = 0 + Ball_D;
                Ball_Vel.X *= -1;
            }
            else if (Ball_Pos.X > this.ClientSize.Width - Bar_Margin - Ball_D) // 碰到 右邊界
            {
                if (Ball_Pos.Y > Mouse_Pos.Y - Bar_Length - Ball_D &&  // 擋板有擋住
                    Ball_Pos.Y < Mouse_Pos.Y + Bar_Length + Ball_D)
                {
                    Ball_Pos.X = this.ClientSize.Width - Ball_D - Bar_Margin;
                    Ball_Vel.X *= -1;  // 球轉向
                }
                else  // 擋板沒有擋住
                {
                    timer1.Enabled = false;
                    MessageBox.Show("You Lose!");
                }
            }

            Ball_Pos.Y = Ball_Pos.Y + Ball_Vel.Y;
            if (Ball_Pos.Y < Ball_D)  // 碰到 上邊界
            {
                Ball_Pos.Y = 0 + Ball_D;
                Ball_Vel.Y *= -1;
            }
            else if (Ball_Pos.Y > this.ClientSize.Height - Bar_Margin - Ball_D) // 碰到 下邊界
            {
                if (Ball_Pos.X > Mouse_Pos.X - Bar_Length - Ball_D &&  // 擋板有擋住
                    Ball_Pos.X < Mouse_Pos.X + Bar_Length + Ball_D)
                {
                    Ball_Pos.Y = this.ClientSize.Height - Ball_D - Bar_Margin;
                    Ball_Vel.Y *= -1;
                }
                else  // 擋板沒有擋住
                {
                    timer1.Enabled = false;
                    MessageBox.Show("You Lose!");
                }
            }

            this.Invalidate();
        }

        // 重新開始
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            Ball_Pos = new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2);
            Ball_Vel = new Point(-3, -5); // 球的速度
            timer1.Enabled = true;
        }
    }
}