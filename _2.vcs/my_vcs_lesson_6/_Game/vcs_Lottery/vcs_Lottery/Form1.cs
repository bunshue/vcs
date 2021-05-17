using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Lottery
{
    public partial class Form1 : Form
    {
        Random rd = new Random();  // 亂數
        int[] No = new int[7];     // 開獎的號碼
        int BallNo = 0; // 目前正要 開出第幾個號碼
        Label[] label = new Label[7];

        public Form1()
        {
            InitializeComponent();
            label[0] = label1;
            label[1] = label2;
            label[2] = label3;
            label[3] = label4;
            label[4] = label5;
            label[5] = label6;
            label[6] = label7;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            for (int i = BallNo; i <= 6; i++) // 尚未開出的號碼
            {
                No[i] = rd.Next(42) + 1; // 產生 亂數 1 ~ 42
                label[i].Text = Convert.ToString(No[i]);
            }
        }

        // 放入彩球 按鈕
        private void button1_Click(object sender, EventArgs e)
        {
            BallNo = 0; // 從第一個球 開始
            timer1.Enabled = true; // 開始跳號
            timer2.Enabled = false;// 不需開出號碼
        }
        // 開獎 按鈕
        private void button2_Click(object sender, EventArgs e)
        {
            BallNo = 0; // 從第一個球 開始
            timer1.Enabled = true; // 開始跳號
            timer2.Enabled = true; // 開始一一開出號碼
        }

        // 開始一一開出號碼
        private void timer2_Tick(object sender, EventArgs e)
        {
            if (CheckNoDuplicate(BallNo)) // 如果和前面的球號碼都不同
                BallNo++; // 開下一顆球的號碼

            if (BallNo == 7) // 已經開完了
            {
                timer1.Enabled = false;
                timer2.Enabled = false;
            }

        }

        // 確定 開出的號碼 和前面的號碼 有無重複
        bool CheckNoDuplicate(int count)
        {
            for (int i = 0; i < 7; i++)
            {
                if (count != i)
                {
                    if (No[count] == No[i]) return false; // 重複
                }
            }
            return true; // 不重複
        }
    }
}