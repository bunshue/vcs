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
        G2D_ColorRect rect01, rect02;  // 兩個顏色矩形物件

        public Form1()
        {
            InitializeComponent();

            int Cx = this.ClientSize.Width / 2;   // 視窗客戶區的中心點
            int Cy = this.ClientSize.Height / 2;

            rect01 = new G2D_ColorRect(Cx, Cy, 200, 100, Color.Black);
            rect02 = new G2D_ColorRect(Cx, Cy, 100, 200, Color.Black);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            rect01.Draw(e.Graphics); // 兩個顏色矩形物件 繪出
            rect02.Draw(e.Graphics);

            // 混色
            int red = trackBar1.Value + trackBar6.Value;
            //if (red > 255) red = 255;
            red = Math.Min(red, 255);

            int green = trackBar2.Value + trackBar5.Value;
            if (green > 255) green = 255;

            int blue = trackBar3.Value + trackBar4.Value;
            if (blue > 255) blue = 255;

            this.Text = "( " + red.ToString() + ", " + green.ToString() + ", " + blue.ToString() + " )";
            SolidBrush myBrush = new SolidBrush(Color.FromArgb(red, green, blue));

            Rectangle r1 = rect01.GetRect();
            Rectangle r2 = rect02.GetRect();
            Rectangle r3 = Rectangle.Intersect(r1, r2);   // 交集

            e.Graphics.FillRectangle(myBrush, r3);    // 混色的塗刷
            e.Graphics.DrawRectangle(Pens.White, r3); // 交集區域的繪出
        }

        // 第一個顏色矩形物件的 顏色調整
        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            Color color;

            color = Color.FromArgb(trackBar1.Value,
                                   trackBar2.Value,
                                   trackBar3.Value);

            rect01.color = color;

            groupBox1.Text = "( " + trackBar1.Value.ToString() + ", " +
                                    trackBar2.Value.ToString() + ", " +
                                    trackBar3.Value.ToString() + " )";
            this.Invalidate();
        }

        // 第二個顏色矩形物件的 顏色調整 
        private void trackBar6_Scroll(object sender, EventArgs e)
        {
            Color color;

            color = Color.FromArgb(trackBar6.Value,
                                   trackBar5.Value,
                                   trackBar4.Value);

            rect02.color = color;
            groupBox2.Text = "( " + trackBar6.Value.ToString() + ", " + trackBar5.Value.ToString() + ", " + trackBar4.Value.ToString() + " )";

            this.Invalidate();
        }

        // 滑鼠按下 看看是否能夠選到 顏色矩形物件
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            rect01.check(e.X, e.Y);
            rect02.check(e.X, e.Y);
        }

        // 滑鼠移動 被選到的 顏色矩形物件 要更新位置
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            rect01.update(e.X, e.Y);
            rect02.update(e.X, e.Y);
            this.Invalidate();
        }

        // 滑鼠放開 沒想到 顏色矩形物件 被選到
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            rect01.drag = false;
            rect02.drag = false;
        }
    }
}
