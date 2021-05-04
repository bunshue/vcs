using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace guessNum
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int ans, times;     //宣告ans、times為成員變數，供所有事件處理函式使用

        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            ans = 73;      		// 指定答案為73
            lblShow.Text = "請輸入1到100之間的數字";
        }
        // 按 [確定] 鈕執行
        private void btnOk_Click(object sender, EventArgs e)
        {
            int guess;
            try
            {   // 使用 try...catch監控可能會發生執行時期例外的程式碼
                guess = int.Parse(txtGuess.Text);
            }
            catch   // 當txtGuess的Text屬性無法轉成整數時，會執行此處
            {
                MessageBox.Show("請輸入數字");
                return;
            }
            times += 1;                 	// 猜的次數加1次
            if (guess == ans)       // 若輸入數值等於答案
            {
                lblShow.Text = "您答對了！共猜了 " + times.ToString() + " 次！";
            }
            else if (guess < ans)  // 若輸入數值小於答案
            {
                lblShow.Text = "數字太小了！已猜了 " + times.ToString() + " 次！";
            }
            else                     // 其餘情況
            {
                lblShow.Text = "數字太大了！已猜了 " + times.ToString() + " 次！";
            }
        }
    }
}
