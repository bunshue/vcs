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
        List<Point> pt = new List<Point>(); // 紀錄點座標的 動態陣列
        public Form1()
        {
            InitializeComponent();
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int k = pt.Count; // 點的數目
            k = k * (k - 1) / 2; // 總計 連線數目

            this.Text = "滑鼠 點對點 " + pt.Count.ToString() + " 個點 = " + k.ToString() + " 條線";
            // 點對點 連線
            for (int i = 0; i < pt.Count-1; i++)
                for (int j=i+1; j<pt.Count;j++)
                    e.Graphics.DrawLine(Pens.Black, pt[i], pt[j]); 
        }

        
        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left) // 滑鼠左鍵 加入一個點
                pt.Add(e.Location);
            else if (e.Button == MouseButtons.Right) // 滑鼠右鍵 清除全部的點
                pt.Clear();

            this.Invalidate(); // 要求表單重畫
        }

        int total_point = 3;
        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
            total_point++;
            if (total_point > 10)
            {
                total_point = 3;
            }
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int i;
            int j;
            
            List<Point> pt = new List<Point>(); // 紀錄點座標的 動態陣列
            pt.Clear();
            int cx = pictureBox1.Width / 2;
            int cy = pictureBox1.Height / 2;
            int r = Math.Min(pictureBox1.Width, pictureBox1.Height) / 2;

            double angle = 2*Math.PI / total_point;


            for (i = 0; i < total_point; i++)
            {
                pt.Add(new Point((int)(cx + r * Math.Cos(angle * i)), (int)(cy + r * Math.Sin(angle * i))));

            }

            for (i = 0; i < pt.Count; i++)
            {
                richTextBox1.Text += pt[i].ToString() + "\n";


            }
            richTextBox1.Text += "\n";


            int k = pt.Count; // 點的數目
            k = k * (k - 1) / 2; // 總計 連線數目

            this.Text = "滑鼠 點對點 " + pt.Count.ToString() + " 個點 = " + k.ToString() + " 條線";
            // 點對點 連線
            for (i = 0; i < pt.Count - 1; i++)
            {
                for (j = i + 1; j < pt.Count; j++)
                {
                    e.Graphics.DrawLine(Pens.Black, pt[i], pt[j]);
                }
            }


        }
    }
}