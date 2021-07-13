using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Class4
{
    public partial class Form1 : Form
    {
        Random rd = new Random(); // 亂數
        List<ClassBall> ballList = new List<ClassBall>();  // ClassBall 物件的動態陣列
        bool dragging = false; // 是否拖拉中
        ClassBall Selected_Ball; // 被選到的球

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Button button = (Button)sender; // 三個按鈕共用一個事件
            Color color = Color.Red;  // 三個按鈕 的顏色 各不相同

            if (button == button1)
            {
                color = Color.Red;
                richTextBox1.Text += "紅";
            }
            else if (button == button2)
            {
                color = Color.Green;
                richTextBox1.Text += "綠";
            }
            else if (button == button3)
            {
                color = Color.Blue;
                richTextBox1.Text += "藍";
            }

            ClassBall aBall;  // 新增 一個 ClassBall 物件
            aBall = new ClassBall(
                new Point(rd.Next(20, this.pictureBox1.ClientSize.Width - 20),
                          rd.Next(40, this.pictureBox1.ClientSize.Height - 20)),
                color);
            ballList.Add(aBall); // 新增 一個 ClassBall 物件到 動態陣列

            this.pictureBox1.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            foreach (ClassBall aBall in ballList) // 繪出全部的球
            {
                e.Graphics.FillEllipse(new SolidBrush(aBall.color), aBall.pt.X - 10, aBall.pt.Y - 10, 20, 20);
                e.Graphics.DrawEllipse(Pens.Black, aBall.pt.X - 10, aBall.pt.Y - 10, 20, 20);
            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // 測試 哪一顆球 被選到
            foreach (ClassBall aBall in ballList)
            {
                if (aBall.CheckSelected(e.X, e.Y))
                {
                    Selected_Ball = aBall; // 這一顆球 被選到
                    dragging = true;
                    break;
                }
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging)
            {
                Selected_Ball.Move(e.X, e.Y); // 移動 被選到的球
                this.pictureBox1.Invalidate();
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            dragging = false;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int cnt = ballList.Count;
            richTextBox1.Text += "\n目前共有 : " + cnt.ToString() + " 球\n";
            if (cnt > 0)
            {
                for (int i = 0; i < cnt; i++)
                {
                    richTextBox1.Text += ballList[i].color + ballList[i].pt.ToString() + "\n";
                }
            }
        }
    }
}
