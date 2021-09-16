using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinButton1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        int guess;  // 要猜的數字，即電腦產生的亂數，亂數範圍1-3

        // CheckAns方法用來判斷答案是否正確
        void CheckAns(int ans)
        {
            // 如果guess(電腦產生的亂數)等於ans(使用者的答案)
            if (guess == ans)
            {
                lblShow.Text = "太棒了...答對了!!";
                // 如果ans等於1即button1顯示snowman.jpg影像圖
                if (ans == 1) button1.Image = new Bitmap("snowman.jpg");
                // 如果ans等於2即button2顯示snowman.jpg影像圖
                if (ans == 2) button2.Image = new Bitmap("snowman.jpg");
                // 如果ans等於3即button3顯示snowman.jpg影像圖
                if (ans == 3) button3.Image = new Bitmap("snowman.jpg");
            }
            else
            {
                lblShow.Text = "不在這裡, 猜錯了!! 請按重完鈕 ...";
            }
        }

        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            // 呼叫btnAgain_Click事件處理函式，產生1-3的亂數並指定給guess
            btnAgain_Click(sender, e);
            this.Text = "找雪人遊戲";
            lblShow.Text = "請問雪人在上面哪個按鈕";
            // 設定lblShow字型大小為14
            lblShow.Font = new Font(lblShow.Font.FontFamily, 14, FontStyle.Regular);
        }

        // 按重玩鈕執行
        private void btnAgain_Click(object sender, EventArgs e)
        {
            Random r = new Random();    // 建立Random亂數物件r
            guess = r.Next(1, 4);               // 產生1-3亂數並指定給guess
            lblShow.Text = "";
            // 設定button1, button2, button3三個按鈕有效
            button1.Enabled = button2.Enabled = button3.Enabled = true;
            // 設定button1, button2, button3三個按鈕不顯示影像圖示
            button1.Image = button2.Image = button3.Image = null;
            lblShow.Text = "請問雪人在上面哪個按鈕";
        }

        // 按離開鈕執行
        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }       
        
        // 按下 button1 表示指定答案 1
        private void button1_Click(object sender, EventArgs e)
        {
            CheckAns(1);  // 呼叫CheckAns方法，並傳入答案1
            button2.Enabled = false;
            button3.Enabled = false;
        }

        // 按下 button2 表示指定答案 2
        private void button2_Click(object sender, EventArgs e)
        {
            CheckAns(2);   // 呼叫CheckAns方法，並傳入答案2
            button1.Enabled = false;
            button3.Enabled = false;
        }

        // 按下 button3 表示指定答案 3
        private void button3_Click(object sender, EventArgs e)
        {
            CheckAns(3);     // 呼叫CheckAns方法，並傳入答案3
            button1.Enabled = false;
            button2.Enabled = false;
        }
        
    }
}
