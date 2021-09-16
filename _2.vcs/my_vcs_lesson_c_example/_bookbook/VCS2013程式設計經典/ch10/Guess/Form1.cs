using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Guess
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int guess, count, min, max;

        private void Form1_Load(object sender, EventArgs e)
        {
            Random r = new Random();
            guess = r.Next(1, 1000);
            min = 1;
            max = 999;
            count = 0;
            lblTitle.Text = min + " < ? < " + max;
            lblMsg.Text = "共猜了 " + count + " 次";
            btnOk.Enabled = true;
            txtGuess.Text = "";
        }

        private void btnOk_Click(object sender, EventArgs e)
        {
            count += 1;
            int myguess = 0;
            try
            {
                myguess = int.Parse(txtGuess.Text);
            }
            catch
            {
                MessageBox.Show("請輸入數字");
            }

            if (myguess >= 1 && myguess < 1000)
            {
                if (myguess == guess)
                {
                    MessageBox.Show("賓果");
                    btnOk.Enabled = false;
                }
                else if (myguess > guess)
                {
                    max = myguess;
                    MessageBox.Show("再小一點");
                }
                else if (myguess < guess)
                {
                    min = myguess;
                    MessageBox.Show("再大一點");
                }
            }
            else
            {
                MessageBox.Show("輸入提示範圍內的數字");
            }
            lblMsg.Text = "共猜了 " + count + " 次";
            lblTitle.Text = min + " < ? < " + max;
        }
       // 
        private void btnAgain_Click(object sender, EventArgs e)
        {
            Form1_Load(sender, e);
        }

        private void btnEnd_Click(object sender, EventArgs e)
        {
            // 顯示對話方塊，並判斷使用者是否按下對話方塊的 [確定] 鈕
            if (MessageBox.Show("請問是否離開遊戲嗎？", "猜數字遊戲", MessageBoxButtons.OKCancel, MessageBoxIcon.Information) ==  System.Windows.Forms.DialogResult.OK )
            {
                Application.Exit();
            }
        }
    }
}
