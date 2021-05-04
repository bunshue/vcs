using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Dice1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int getpoint;  // 宣告getpoint用來存放得到的點數
        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Interval = 50;  // 指定每50豪秒(即0.05秒)執行一次Timer1_Tick事件
            pic1.Image = imgDice.Images[0];
        }
        // 按 [開始] 鈕執行
        private void btnStart_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;  //啟動timer1計時器
        }
        // 按 [停止] 鈕執行
        private void btnStop_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false; // 停止timer1計時器
            lblMsg.Text = "你得到 " + Convert.ToString(getpoint + 1) + " 點 !!";
        }
        // 每50豪秒(即0.05秒)執行一次timer1_Tick事件
        private void timer1_Tick(object sender, EventArgs e)
        {
            Random rnd = new Random();
            getpoint = rnd.Next(0, 6);
            pic1.Image = imgDice.Images[getpoint];
        }
    }
}
