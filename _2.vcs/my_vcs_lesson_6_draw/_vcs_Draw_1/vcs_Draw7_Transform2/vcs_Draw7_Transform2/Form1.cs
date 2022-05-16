using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//Graphics平移縮放旋轉

namespace vcs_Draw7_Transform2
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
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(0, 0, 200, 50);

            g.DrawRectangle(p, rect);   //用紅色筆畫矩形

            //向左平移100向下平移50
            g.TranslateTransform(100, 50);
            p.Color = Color.Green;
            g.DrawRectangle(p, rect);   //用綠色筆畫平移後的圖形

            g.ResetTransform(); //恢復
            g.DrawString("平移, 紅色是原本的, 綠色是平移後的", new Font("標楷體", 16), new SolidBrush(Color.Blue), new PointF(0, 0));

            g.Dispose();
            p.Dispose();
        }

        //縮放
        private void button2_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(0, 0, 200, 50);
            g.DrawRectangle(p, rect);   //用紅色筆畫矩形
            g.ScaleTransform(0.5f, 2);

            p.Color = Color.Green;
            g.DrawRectangle(p, rect);   //用綠色筆畫縮放後的圖形

            g.ResetTransform(); //恢復
            g.DrawString("縮放, 紅色是原本的, 綠色是縮放後的", new Font("標楷體", 16), new SolidBrush(Color.Blue), new PointF(0, 0));

            g.Dispose();
            p.Dispose();

            //寬縮小一半，高放大一倍
        }

        //旋轉
        //坐標原點為矩形的左上點
        private void button3_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(0, 0, 200, 50);
            g.DrawRectangle(p, rect);   //用紅色筆畫矩形
            g.TranslateTransform(200, 0);
            g.RotateTransform(90);

            p.Color = Color.Green;
            g.DrawRectangle(p, rect);   //用綠色筆畫旋轉後的圖形

            g.ResetTransform(); //恢復
            g.DrawString("旋轉, 紅色是原本的, 綠色是旋轉後的", new Font("標楷體", 16), new SolidBrush(Color.Blue), new PointF(0, 0));

            g.Dispose();
            p.Dispose();

        }
    }
}
