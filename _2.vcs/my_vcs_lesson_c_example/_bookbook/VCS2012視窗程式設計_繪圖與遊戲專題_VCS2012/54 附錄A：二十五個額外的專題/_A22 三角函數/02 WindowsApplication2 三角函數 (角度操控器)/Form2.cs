using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form2 : Form
    {
        Point ct = new Point(250,150); // control point 紅色控制點
        bool Moving = false; // 紅點 移動中
        Point current = new Point(); // 滑鼠游標 目前的座標
        double theta = 0; // 徑度
        double degree = 0; // 角度
        public Form1 form1; // 要丟回 form1 的 VLine 並且重畫

        public Form2()
        {
            InitializeComponent();
            this.ClientSize = new Size(320, 520);
        }

        private void Form2_Paint(object sender, PaintEventArgs e)
        {
            theta = degree * Math.PI / 180;

            ct.X = (int)(150 + 100 * Math.Cos(theta)); // 控制點
            ct.Y = (int)(150 + 100 * Math.Sin(theta));

            // 畫大圓、垂直線、水平線
            e.Graphics.DrawEllipse(Pens.Black, 50, 50, 200, 200);
            e.Graphics.DrawLine(Pens.DarkGray, 50, 150, 250, 150);
            e.Graphics.DrawLine(Pens.DarkGray, 150, 50, 150, 250);

            // 畫紅色小點
            e.Graphics.FillEllipse(Brushes.Red, ct.X-10, ct.Y-10, 20, 20);
            e.Graphics.DrawLine(Pens.Red, 150, 150, ct.X, ct.Y);

            double thetaSign = -theta; // Y軸往下 所以角度的旋轉方向也不同
            
            labelA1.Text = thetaSign.ToString() + " 徑度";
            textBox1.Text = Convert.ToString(thetaSign * 180 / Math.PI);
            labelA2.Text = Convert.ToString(Math.Sin(thetaSign));
            labelA3.Text = Convert.ToString(Math.Cos(thetaSign));
            labelA4.Text = Convert.ToString(Math.Tan(thetaSign));

            labelA5.Text = Convert.ToString(1/Math.Tan(thetaSign)); //cot
            labelA6.Text = Convert.ToString(1/Math.Cos(thetaSign)); //sec
            labelA7.Text = Convert.ToString(1/Math.Sin(thetaSign)); //csc

            form1.VLine = (float)(0.1 * thetaSign * 180 / Math.PI); // 徑度轉回角度再 縮小
            form1.Invalidate();
        }

        private void Form2_MouseDown(object sender, MouseEventArgs e)
        {
            double dis = Math.Sqrt((e.X - ct.X) * (e.X - ct.X) + (e.Y - ct.Y) * (e.Y - ct.Y));
            if (dis <= 10)
            {
                Moving = true;
                current.X = e.X;
                current.Y = e.Y;
            }
        }

        private void Form2_MouseUp(object sender, MouseEventArgs e)
        {
            Moving = false;
        }

        private void Form2_MouseMove(object sender, MouseEventArgs e)
        {
            //double theta_D = 0.01;
            int degree_D = 1;
            int temp;
            if (Moving)
            {
                temp = (int)Math.Round(degree);
                degree = temp;  // 先把 小數點 去掉

                if (degree > 360) degree = degree - 360;
                else if (degree < -360) degree = degree + 360;

                if (e.X >= 150) // 在右方
                {
                    if (e.Y < current.Y)  // 滑鼠往上
                        degree = degree - degree_D;
                    else if (e.Y > current.Y)  // 滑鼠往下
                        degree = degree + degree_D;
                }
                else // 在左方 
                {
                    if (e.Y < current.Y)  // 滑鼠往上
                        degree = degree + degree_D;
                    else if (e.Y > current.Y) // 滑鼠往下
                        degree = degree - degree_D;
                }


                if (e.Y <= 150) // 在上方
                {
                    if (e.X < current.X)  // 滑鼠往左
                        degree = degree - degree_D;
                    else if (e.X > current.X) // 滑鼠往右
                        degree = degree + degree_D;
                }
                else // 在下方 
                {
                    if (e.X < current.X)  // 滑鼠往左
                        degree = degree + degree_D;
                    else if (e.X > current.X)  // 滑鼠往右
                        degree = degree - degree_D;
                }

                current.X = e.X;
                current.Y = e.Y;
                this.Invalidate();
            }
        }

        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                //theta = -(Convert.ToDouble(textBox1.Text) * Math.PI / 180);
                degree = -Convert.ToDouble(textBox1.Text);
                this.Invalidate();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Visible = false;
        }
    }
}