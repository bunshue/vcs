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
        double theta = 0;// 徑度 (一圈為 Math.PI * 2)
        double r; // 半徑
        int x1, x2, y1, y2; //直線的兩個點
        bool First = true;//定義第一點 (通常不畫)
        Graphics G;// 畫布
        int a, b;// 方程式的 參數
        Pen MyPen = new Pen(Color.Black, 3);  //黑色筆 寬為 3

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(800, 600); // 定出
            G = this.CreateGraphics();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            theta = theta + 0.01;

            if (comboBox1.Text == "")
            {
                timer1.Enabled = false;
                label1.Text = "";
                return;
            }
            else if (comboBox1.Text == "Circle")
            {
                if (theta >= Math.PI * 2)
                {
                    timer1.Enabled = false;
                    label1.Text = "";
                }
                r = this.ClientSize.Height / 4;
                x2 = this.ClientSize.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = this.ClientSize.Height / 2 + (int)(r * Math.Sin(theta));
            }
            else if (comboBox1.Text == "Limacon")
            {
                if (theta >= Math.PI * 2)
                {
                    timer1.Enabled = false;
                    label1.Text = "";
                }
                a = 200; b = 100;
                r = a * Math.Cos(theta - Math.PI / 2) + b;
                x2 = this.ClientSize.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = this.ClientSize.Height / 4 + (int)(r * Math.Sin(theta));
            }
            else if (comboBox1.Text == "Cardiod")
            {
                if (theta >= Math.PI * 2)
                {
                    timer1.Enabled = false;
                    label1.Text = "";
                }
                a = 200;// b = 50;
                r = a * Math.Cos(theta - Math.PI / 2) + a;
                x2 = this.ClientSize.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = this.ClientSize.Height / 4 + (int)(r * Math.Sin(theta));
            }
            else if (comboBox1.Text == "Three Left")
            {
                if (theta >= Math.PI)
                {
                    timer1.Enabled = false;
                    label1.Text = "";
                }
                a = 275;
                r = a * Math.Cos(3.0 * theta);
                x2 = this.ClientSize.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = this.ClientSize.Height / 2 + (int)(r * Math.Sin(theta));
            }
            else if (comboBox1.Text == "Four Left")
            {
                if (theta >= Math.PI * 2)
                {
                    timer1.Enabled = false;
                    label1.Text = "";
                }
                a = 275;
                r = a * Math.Cos(2.0 * theta);
                x2 = this.ClientSize.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = this.ClientSize.Height / 2 + (int)(r * Math.Sin(theta));
            }
            else if (comboBox1.Text == "Spiral")
            {
                if (theta >= Math.PI * 20)
                {
                    timer1.Enabled = false;
                    label1.Text = "";
                }
                a = 175;
                r = a / 40.0 * theta;
                x2 = this.ClientSize.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = this.ClientSize.Height / 2 + (int)(r * Math.Sin(theta));
            }

            if (First) First = !First;
            else
                G.DrawLine(MyPen, x1, y1, x2, y2);

            x1 = x2;
            y1 = y2;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            label1.Text = comboBox1.Text.ToString();
            this.Invalidate();
            timer1.Enabled = true;
            theta = 0;
            First = true;
        }

    }
}