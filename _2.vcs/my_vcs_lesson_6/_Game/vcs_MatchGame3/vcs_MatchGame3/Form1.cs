using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;
using System.Media;
using System.Threading;

namespace vcs_MatchGame3
{
    public partial class Form1 : Form
    {
        int[] card = new int[16];    // 16 張牌
        Random rd = new Random();    // 亂數
        Bitmap[] b = new Bitmap[8];  // 8 張圖形

        int First_Sceond = 1;
        int FirstCardNo;
        Panel FirstCardPanel;

        int Good = 0, Bad = 0; // 猜對 猜錯 次數

        Stopwatch sw = new Stopwatch(); // 計時碼表
        TimeSpan ts; // 經過的時間

        public Form1()
        {
            InitializeComponent();

            // 上載 8 張圖形
            b[0] = Properties.Resources.Box;
            b[1] = Properties.Resources.Cone;
            b[2] = Properties.Resources.Cylinder;
            b[3] = Properties.Resources.Pyramid;
            b[4] = Properties.Resources.Sphere;
            b[5] = Properties.Resources.Teapot;
            b[6] = Properties.Resources.Torus;
            b[7] = Properties.Resources.Tube;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int temp, t1, t2;
            // 16 張牌的封面 
            foreach (Control ctrl in this.Controls)
            {
                if (ctrl is Panel)
                {
                    ((Panel)ctrl).BackgroundImage = Properties.Resources.Cover;
                    ((Panel)ctrl).Enabled = true;
                }
            }

            // 排好 16 張牌的圖形編號 0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7
            for (int i = 0; i < 16; i++)
                card[i] = i % 8;

            // 兩兩打亂
            for (int i = 0; i < 100; i++)
            {
                t1 = rd.Next(16);
                t2 = rd.Next(16);
                temp = card[t1];
                card[t1] = card[t2];
                card[t2] = temp;
            }

            Good = 0; label3.Text = Convert.ToString(Good);
            Bad = 0; label4.Text = Convert.ToString(Bad);
            sw.Reset(); // 碼表歸零
            sw.Start(); // 開始計時
            timer1.Enabled = true;
        }

        // 每一張牌 被玩家點按 翻牌
        private void panel0_Click(object sender, EventArgs e)
        {
            Panel PanelX = (Panel)sender;
            int CardNo = Convert.ToInt32(PanelX.Tag); // 第幾張牌 0~ 15

            PanelX.BackgroundImage = b[card[CardNo]]; // 第幾張牌的圖形
            PanelX.Enabled = false;
            PanelX.Refresh(); // 重繪 (翻牌)

            if (First_Sceond == 1) // 是按第一次
            {
                FirstCardNo = card[CardNo]; // 紀錄第一次翻牌的圖形編號
                FirstCardPanel = PanelX;
                First_Sceond = 2;
            }
            else // 是按第二次
            {
                // 第二次翻牌的圖形編號 和 第一次翻牌的圖形編號 是一致的
                if (FirstCardNo == card[CardNo])
                {
                    PanelX.Enabled = false; // 將 第二次翻牌的 Panel 設為不能再翻牌
                    FirstCardPanel.Enabled = false; // 將 第一次翻牌的 Panel 設為不能再翻牌
                    Good++; // 猜對次數 加一
                    label3.Text = Convert.ToString(Good);
                    if (Good == 8) // 如果已經 猜對八次
                    {
                        sw.Stop();
                        timer1.Enabled = false; // 就結束了
                    }
                }
                else // 第二次翻牌的圖形編號 和 第一次翻牌的圖形編號 是不一致的
                {
                    SystemSounds.Beep.Play(); // 發聲 警告
                    Thread.Sleep(500); // 停  0.5 秒

                    // 回復 第一、二次 Panel 的封面
                    FirstCardPanel.BackgroundImage = Properties.Resources.Cover;
                    PanelX.BackgroundImage = Properties.Resources.Cover;

                    FirstCardPanel.Enabled = true;
                    PanelX.Enabled = true;

                    Bad++; // 猜錯次數 加一
                    label4.Text = Convert.ToString(Bad);
                }
                First_Sceond = 1;
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            ts = TimeSpan.FromMilliseconds(sw.ElapsedMilliseconds);
            label5.Text = Convert.ToString(ts.Minutes) + "分 " +
                          Convert.ToString(ts.Seconds) + "秒." +
                          Convert.ToString(ts.Milliseconds);
        }
    }
}