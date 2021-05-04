// 專題名稱：身體質量指數計算 Body Mass Index
// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        Font myFont = new Font("標楷體", 14); // 字型
        string[] stringWeight = new string[] {"40","50","60","70","80","90","100", "公斤"};
        string[] stringHeight = new string[] {"140", "150", "160", "170", "180", "190", "200", "公分"};
        PointF[] pt = new PointF[61]; // 曲線 的關鍵點座標
        double myHeigh, myWeight; // 我的身高體重

        public Form1()
        {
            InitializeComponent();
            button1_Click(null, null);
        }

        // 表單重畫函數
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int Dx = this.ClientSize.Width / 11; //  畫面分格子
            int Dy = this.ClientSize.Height / 15;

            int Cx = 2 * Dx;  // 左下角的 座標
            int Cy = this.ClientSize.Height - 2 * Dy;

            // 垂直線
            e.Graphics.DrawLine(Pens.Black, Cx, Cy, Cx, Cy - 8 * Dy);
            for (int i = 1; i <= 8; i++)
                e.Graphics.DrawLine(Pens.Silver, Cx + i * Dx, Cy, Cx + i * Dx, Cy - 8 * Dy);

            // 水平線
            e.Graphics.DrawLine(Pens.Black, Cx, Cy, Cx + 8 * Dx, Cy);
            for (int i = 1; i <= 8; i++)
                e.Graphics.DrawLine(Pens.Silver, Cx, Cy - i * Dy, Cx + 8 * Dx, Cy - i * Dy);

            // 水平線 文字 -- 公分
            for (int i = 0; i <= 7; i++)
                e.Graphics.DrawString(stringHeight[i],  // 繪出文字字串
                    myFont,
                    Brushes.Black,
                    Cx + (i + 1) * Dx - 20, Cy + 20);

            // 垂直線 文字 -- 公斤
            for (int i = 0; i <= 7; i++)
                e.Graphics.DrawString(stringWeight[i],  // 繪出文字字串
                    myFont,
                    Brushes.Black,
                    Cx - 50, Cy - (i + 1) * Dy - 10);

            // BMI = 25 的曲線 的關鍵點
            for (int x = 140; x <= 200; x++)
            {
                float y = 25 * (x / 100.0f) * (x / 100.0f);

                float Nx = (x - 140.0f) / 10.0f * Dx + (Cx + Dx);
                float Ny = (Cy - Dy) - (y - 40.0f) / 10.0f * Dy;
                pt[x - 140] = new PointF(Nx, Ny);
            }
            e.Graphics.DrawLines(Pens.Red, pt);

            // BMI = 18.5 的曲線 的關鍵點
            for (int x = 140; x <= 200; x++)
            {
                float y = 18.5f * (x / 100.0f) * (x / 100.0f);

                float Nx = (x - 140.0f) / 10.0f * Dx + (Cx + Dx);
                float Ny = (Cy - Dy) - (y - 40.0f) / 10.0f * Dy;
                pt[x - 140] = new PointF(Nx, Ny);
            }
            e.Graphics.DrawLines(Pens.Blue, pt);

            // 我的身高體重 的點座標  myHeigh 是公尺
            float myNx = (float)((myHeigh*100 - 140.0f) / 10.0f * Dx + (Cx + Dx));
            float myNy = (float)((Cy - Dy) - (myWeight - 40.0f) / 10.0f * Dy);
            e.Graphics.FillEllipse(Brushes.Green, myNx - 5, myNy - 5, 10, 10);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try // 只怕輸入的不是 數字
            {
                myHeigh = Convert.ToDouble(textBox1.Text) / 100.0;
                myWeight = Convert.ToDouble(textBox2.Text);
            }
            catch
            {
                myHeigh = 0;
                myWeight = 0;
            }

            // BMI = 公斤 / 公尺 * 公尺
            double bmi = myWeight / (myHeigh * myHeigh);
            label5.Text = "BMI = " + bmi.ToString("###.##");

            double min = 18.5 * (myHeigh * myHeigh); // 合乎標準 BMI 的下限
            double max = 25 * (myHeigh * myHeigh); // 合乎標準 BMI 的上限
            label6.Text = "理想的體重：" + min.ToString("###.##") + " ~ " + max.ToString("###.##") + " 公斤";
            this.Invalidate();  // 要求重畫
        }
    }
}