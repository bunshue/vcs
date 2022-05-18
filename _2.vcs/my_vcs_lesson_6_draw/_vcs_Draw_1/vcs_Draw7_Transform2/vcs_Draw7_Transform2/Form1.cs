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

        private void button4_Click(object sender, EventArgs e)
        {
            //字串旋轉列印
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawString("字串旋轉列印", new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(20, 20));

            Font f = new Font("標楷體", 50);
            RotateDeawString(g, f, 35, "字串旋轉列印", 20, 20);


        }

        /// <summary>
        /// 旋轉列印字串
        /// </summary>
        /// <param name="e">PrintPageEventArgs</param>
        /// <param name="font">字型</param>
        /// <param name="degree">旋轉角度</param>
        /// <param name="msg">列印訊息</param>
        /// <param name="x">重設原點 X 位置</param>
        /// <param name="y">重設原點 Y 位置</param>
        private void RotateDeawString(Graphics g, Font font, int degree, string msg, int x, int y)
        {
            // 原點位置重設
            g.TranslateTransform(mmTo100InchX(x), mmTo100InchY(y));
            // 設定旋轉角度
            g.RotateTransform(degree);
            // 標題
            g.DrawString(msg, font, Brushes.Black, mmTo100InchX(0), mmTo100InchY(0));
            //繪圖畫布還原
            g.ResetTransform();
        }

        private int mmTo100InchX(int mm)
        {
            int times = 100;
            double result = (mm * times / 25.4);
            return (int)Math.Floor(result);
        }

        private int mmTo100InchY(int mm)
        {
            int times = 100;
            double result = (mm * times / 25.4);
            return (int)Math.Floor(result);
        }


    }
}
