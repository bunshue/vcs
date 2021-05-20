using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NameBubble
{
    public partial class Form1 : Form
    {
        List<NameBubble> b1 = new List<NameBubble>(); // 動態陣列
        Random rd = new Random(); // 亂數

        string[] Names = new string[] { "陳奕誠", "黃紫音", "楊正瑋", "楊孟瑋", 
            "蘇崇維", "姚芝宜", "陳安晏", "林致禾", "江建榮", "品田翔平", "房兆軒", 
            "劉怡君", "蕭建瑋", "黃郁仁", "洪大鈞", "江禹賢", "劉不仕", "林柏邑" };

        int Counter_Pass = 0;   // 過關人次
        int Counter_Failed = 0; // 陣亡人次
        int Bubble_X = 100; // 新氣泡 X 軸的位置

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 反鋸齒設定  更好的輸出品質
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 繪出 全部的氣泡
            for (int i =0; i< b1.Count; i++)
              b1[i].Draw(e.Graphics);

            label1.Text = "過關人次：" + Counter_Pass.ToString();
            label2.Text = "陣亡人次：" + Counter_Failed.ToString();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            // 由後往前 更新 全部氣泡的位置
            for (int i = b1.Count - 1; i >= 0; i--)
            {
                b1[i].Update(this.ClientSize.Width, this.ClientSize.Height);

                // 如果氣泡 越過上緣就 從動態陣列中刪除
                if (b1[i].pos.Y < -b1[i].strSize.Width / 2)
                {
                    b1.RemoveAt(i);
                    Counter_Pass++;
                }
            }

            // 氣泡 兩兩碰撞處理
            double dis; // 兩個氣泡 的距離
            Point vec;
            for (int i = 0; i < b1.Count - 1; i++) // 動態陣列從前往後
                for (int j = i + 1; j < b1.Count; j++) // 和後面的氣泡相比
                {
                    dis = Math.Sqrt(
                        (b1[i].pos.X - b1[j].pos.X) * (b1[i].pos.X - b1[j].pos.X) +
                        (b1[i].pos.Y - b1[j].pos.Y) * (b1[i].pos.Y - b1[j].pos.Y));

                    // 如果 距離太短 => 有碰撞 => 彼此交換速度
                    if (dis < b1[i].strSize.Width / 2 + b1[j].strSize.Width / 2)
                    {
                        vec = b1[i].vec;

                        b1[i].vec = b1[j].vec;
                        b1[j].vec = vec;
                    }
                }
             
            this.Invalidate();
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            if (rd.NextDouble() < 0.2) // 產生新氣泡 的機率 約為 20%  
            {
                // 新氣泡 X 軸的位置往右移 取餘數是避免 越界
                Bubble_X = (Bubble_X + rd.Next(100) + 100) % this.ClientSize.Width;
                NameBubble bubble = new NameBubble(
                    new Point(Bubble_X, this.ClientSize.Height + 100),
                    new Point(rd.Next(-5, 5), rd.Next(-6, -3)), 
                    Names[rd.Next(Names.Length)],
                    G2D_Color.GetColor());

                b1.Add(bubble); // 加入 新氣泡
            }
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            // 滑鼠按下時就 嘗試刪除氣泡
            double dis;
            for (int j = b1.Count - 1; j >= 0; j--) // 由後往前
            {
                dis = Math.Sqrt(
                    (e.X - b1[j].pos.X) * (e.X - b1[j].pos.X) +
                    (e.Y - b1[j].pos.Y) * (e.Y - b1[j].pos.Y));

                if (dis < b1[j].strSize.Width / 2)
                {
                    b1.RemoveAt(j);
                    Counter_Failed++;
                }
            }

        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Space)
            {
                b1.Clear(); // 氣泡動態陣列 清空
                Counter_Pass = 0;   // 過關人次
                Counter_Failed = 0; // 陣亡人次
            }
        }
    }
}
