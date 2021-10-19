using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


//[C#] Graphics平移縮放旋轉


namespace vcs_draw_rotate
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //平移
        private void button1_Click(object sender, EventArgs e)
        {
            Graphics graphics = this.CreateGraphics();
            // 紅色筆
            Pen pen = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(0, 0, 200, 50);
            // 用紅色筆畫矩形
            graphics.DrawRectangle(pen, rect);
            // 向左平移100向下平移50
            graphics.TranslateTransform(100, 50);
            // 藍色筆
            pen.Color = Color.Blue;
            // 用藍色筆重新畫平移之後的矩形
            graphics.DrawRectangle(pen, rect);
            graphics.Dispose();
            pen.Dispose();

        }

        //縮放
        private void button2_Click(object sender, EventArgs e)
        {
            Graphics graphics = this.CreateGraphics();
            // 紅色筆
            Pen pen = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(0, 0, 200, 50);
            // 用紅色筆畫矩形
            graphics.DrawRectangle(pen, rect);
            graphics.ScaleTransform(0.5f, 2);
            // 藍色筆
            pen.Color = Color.Blue;
            // 用藍色筆重新畫平移之後的矩形
            graphics.DrawRectangle(pen, rect);
            graphics.Dispose();
            pen.Dispose();

            //寬縮小一半，高放大一倍
        }

        //旋轉
        //坐標原點為矩形的左上點
        private void button3_Click(object sender, EventArgs e)
        {
            Graphics graphics = this.CreateGraphics();
            // 紅色筆
            Pen pen = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(0, 0, 200, 50);
            // 用紅色筆畫矩形
            graphics.DrawRectangle(pen, rect);
            graphics.TranslateTransform(200, 0);
            graphics.RotateTransform(90);
            // 藍色筆
            pen.Color = Color.Blue;
            // 用藍色筆重新畫平移之後的矩形
            graphics.DrawRectangle(pen, rect);
            graphics.Dispose();
            pen.Dispose();

        }
    }
}
