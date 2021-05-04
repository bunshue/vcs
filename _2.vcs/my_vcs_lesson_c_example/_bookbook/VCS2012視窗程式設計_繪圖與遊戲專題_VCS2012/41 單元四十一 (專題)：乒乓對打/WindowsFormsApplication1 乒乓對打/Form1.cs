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
        Point Ball_pos = new Point(); // 球的位置
        int Ball_Width = 30;          // 球的寬度 (直徑)
        Point Ball_Speed = new Point();// 球的速度
        Pen myPen1 = new Pen(Color.Black, 5); // 擋板的筆刷
        Pen myPen2 = new Pen(Color.Brown, 5);// 擋板的筆刷
        Pen myPen3 = new Pen(Color.Brown, 2);// 輔助線的筆刷

        int Margin_Left = 40;     // 左端擋板的 X 軸 偏移値
        int Margin_Right = 120;   // 右端擋板的 X 軸 偏移値
        int Bar_Len = 50;   // 擋板長度的一半
        int Y_Right = 0;    // 右端擋板的 Y 軸位置
        int Y_Left = 0;     // 左端擋板的 Y 軸位置
        Random rd = new Random();

        public Form1()
        {
            InitializeComponent();
            Ball_pos.X = this.ClientSize.Width / 2; // 球的初始位置
            Ball_pos.Y = this.ClientSize.Height / 2;
            Ball_Speed = new Point(rd.Next(5) + 5, rd.Next(8) + 4);// 球的速度
            Y_Left = this.ClientSize.Height / 2;
            Y_Right = this.ClientSize.Height / 2;

            myPen3.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 繪出 球體
            e.Graphics.FillEllipse(Brushes.Blue,
                Ball_pos.X - Ball_Width / 2,
                Ball_pos.Y - Ball_Width / 2,
                Ball_Width, Ball_Width);
            e.Graphics.DrawEllipse(Pens.Black,
                Ball_pos.X - Ball_Width / 2,
                Ball_pos.Y - Ball_Width / 2,
                Ball_Width, Ball_Width);

            // 繪出 左端擋板
            e.Graphics.DrawLine(myPen1,
                0 + Margin_Left, Y_Left - Bar_Len,
                0 + Margin_Left, Y_Left + Bar_Len);

            // 繪出 右端擋板
            e.Graphics.DrawLine(myPen2,
                this.ClientSize.Width - Margin_Right, Y_Right - Bar_Len,
                this.ClientSize.Width - Margin_Right, Y_Right + Bar_Len);

            // 繪出 右端擋板 的輔助線
            e.Graphics.DrawLine(myPen3,
                0, Y_Right,
                this.ClientSize.Width, Y_Right);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Ball_pos.Y += Ball_Speed.Y;

            // 碰到視窗下緣
            if (Ball_pos.Y >= this.ClientSize.Height - Ball_Width / 2)
            {
                Ball_pos.Y = this.ClientSize.Height - Ball_Width / 2;
                Ball_Speed.Y = -Ball_Speed.Y; // 球體轉向
            }
            else if (Ball_pos.Y < Ball_Width / 2) // 碰到視窗上緣
            {
                Ball_pos.Y = Ball_Width / 2;
                Ball_Speed.Y = -Ball_Speed.Y; // 球體轉向
            }

            Ball_pos.X += Ball_Speed.X;
            if (Ball_pos.X < 200) // 如果球體離開視窗左邊邊緣 已經很近了
            {
                if (Ball_pos.Y > Y_Left) // 如果左擋板在上面 就將它拉下來
                    Y_Left += 10 + rd.Next(11) - 5; // 用一些亂數
                else if (Ball_pos.Y < Y_Left) // 如果左擋板在下面 就將它拉上來
                    Y_Left -= 10 + rd.Next(11) - 5;
            }

            // 如果球體超過右邊邊緣
            if (Ball_pos.X >= this.ClientSize.Width - Ball_Width / 2 - Margin_Right)
            {
                // 如果右擋板 可以擋住 球體
                if (Ball_pos.Y <= Y_Right + Bar_Len + Ball_Width &&
                    Ball_pos.Y >= Y_Right - Bar_Len - Ball_Width)
                {
                    Ball_pos.X = this.ClientSize.Width - Ball_Width / 2 - Margin_Right;
                    Ball_Speed.X = -Ball_Speed.X; // 球體轉向
                }
                else // 如果右擋板 無法擋住 球體
                {
                    this.Invalidate();
                    timer1.Enabled = false;
                    MessageBox.Show("你輸了!");
                }
            }
            // 如果球體超過左邊邊緣
            else if (Ball_pos.X < Ball_Width / 2 + Margin_Left)
            {
                if (Ball_pos.Y <= Y_Left + Bar_Len + Ball_Width &&
                    Ball_pos.Y >= Y_Left - Bar_Len - Ball_Width)
                {
                    Ball_pos.X = Ball_Width / 2 + Margin_Left;
                    Ball_Speed.X = -Ball_Speed.X;
                }
                else
                {
                    this.Invalidate();
                    timer1.Enabled = false;
                    MessageBox.Show("你贏了!");
                }
            }

            this.Invalidate();
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            Y_Right = e.Y; // 隨著滑鼠游標 更新右擋板
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Space)
            {
                Ball_pos.X = this.ClientSize.Width / 2; // 球的初始位置
                Ball_pos.Y = this.ClientSize.Height / 2;
                Ball_Speed = new Point(rd.Next(5) + 5, rd.Next(8) + 4);// 球的速度
                Y_Left = this.ClientSize.Height / 2;
                Y_Right = this.ClientSize.Height / 2;
                timer1.Enabled = true;
            }
        }
    }
}