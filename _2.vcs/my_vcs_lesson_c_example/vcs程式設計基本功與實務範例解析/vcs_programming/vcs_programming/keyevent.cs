using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class keyevent : Form
    {
        public keyevent()
        {
            InitializeComponent();
        }

        int curLeft, maxLeft;
        int score = 0;
        double time = 30;
        Label[] lblObj;
        Random rd1, rd2;

        private void keyevent_Load(object sender, EventArgs e)
        {
            this.ClientSize = new Size(300, 330);
            this.KeyPreview = true;

            //設定與記錄接受器的位置
            label1.Left = 125;
            label1.Top = 300;
            curLeft = label1.Left;
            maxLeft = 300 - 50; //最小值是0
            
            //動態產生8個落下的Label控制項
            lblObj = new Label[8];

            for (int i = 0; i < 8; i++)
            {
                lblObj[i] = new Label(); //通道編號i之掉落物控制項
                lblObj[i].Size = new Size(30, 30);
                lblObj[i].Left = 6 + i * 36 + 3;
                lblObj[i].BackColor = Color.HotPink;
                lblObj[i].BorderStyle = BorderStyle.Fixed3D;
                lblObj[i].TextAlign = ContentAlignment.MiddleCenter;
                lblObj[i].Visible = false; // 一開始為不可見
                this.Controls.Add(lblObj[i]); //加入表單容器中
            }

            rd1 = new Random();  //成員變數，選擇通道
            rd2 = new Random();  //成員變數，產生數字
        }

        private void keyevent_KeyUp(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Left:
                    curLeft -= 30;
                    if (curLeft < 0) curLeft = 0;
                    break;
                case Keys.Right:
                    curLeft += 30;
                    if (curLeft > maxLeft) curLeft = maxLeft;
                    break;
            }

            label1.Left = curLeft;

        }

        private void calcScore(int idx)
        {
            Label obj = lblObj[idx];

            //計算掉落物控制項的左、上、右、下座標值
            int left = obj.Left;
            int top = obj.Top;
            int right = left + 30;
            int bottom = top + 30;

            //計算接收器和掉落物，有所重疊(Hit)的邊界座標值
            int leftB = label1.Left - 30;
            int topB = label1.Top - 30;
            int rightB = leftB + label1.Width + 60;
            int bottomB = topB + label1.Height + 60;

            if (bottom > bottomB)
            {   // miss
                obj.Visible = false;
                return;
            }

            if (left >= leftB && right <= rightB &&
                top >= topB)
            {
                // overlap and hit
                int n = Convert.ToInt32(obj.Text);
                score += n;
                time += (n/5.0);
                obj.Visible = false;
                return;
            }
            //不是 Miss 和 Hit，則往下掉 30 pixels
            obj.Top += 30;
            
        }

        
        private void timer1_Tick(object sender, EventArgs e)
        {
            for(int i = 0; i < 8; i++)
                if (lblObj[i].Visible) {
                    calcScore(i); //傳入通道的編號i，更新分數與時間
                }

            int pos = rd1.Next(0, 8); //通道的編號
                
            if (lblObj[pos].Visible == false)
            {
                lblObj[pos].Visible = true;
                lblObj[pos].Top = 30;
                lblObj[pos].Text = rd2.Next(1, 10).ToString(); //分數
            }
            //更新時間
            time -= 0.5;
            if (time < 0) time = 0;

            //顯示時間和分數
            lblTime.Text = "時間: " + time.ToString("0.0");
            lblScore.Text = "分數: " + score;
            
            if (time <= 0)
            {
                timer1.Enabled = false;
                MessageBox.Show("遊戲結束!");
            }
        }
    }
}
