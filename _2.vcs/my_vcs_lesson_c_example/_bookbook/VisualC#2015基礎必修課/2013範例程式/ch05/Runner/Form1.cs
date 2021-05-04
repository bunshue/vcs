using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Runner
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int no;  // 用來表示目前是幾張圖
        DateTime timeNow;  // 用來記錄目前時間
        // 表單載入執行
        private void Form1_Load(object sender, EventArgs e)
        {
            picRunner.Image = imageList1.Images[0];// 顯示第1張圖
            timer1.Interval = 100;  // 設定timer1每0.1秒執行Tick事件一次
            no = 0;
            lblMsg.Text = "";
            btnStop.Enabled = false;
        }
        // 按開始鈕執行
        private void btnStart_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
            timeNow = DateTime.Now;
            btnStart.Enabled = false;
            btnStop.Enabled = true;
        }
        // timer1每0.1秒執行一次
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (no < 4)   // 判斷no是否小於4
            {
                picRunner.Image = imageList1.Images[no];  // 顯示第no張圖
                no++;   // 切換到下一張圖
            }
            else
            {
                no = 0;  // 切換到第一張圖
            }
        }
        // 按停止鈕執行
        private void btnStop_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;   // timer1停止
            // 計算花費時間
            lblMsg.Text = "總共花費" + (DateTime.Now - timeNow).TotalSeconds.ToString() + "秒";
            btnStart.Enabled = true;
            btnStop.Enabled = false;
        }
    }
}
