using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh2_2_41
{
    public partial class Form1 : Form
    {
        // 判斷使用者是否已輸入數字
        private bool nonNumberEntered = false;

        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            // 假設使用者已輸入數字
            nonNumberEntered = false;

            // 判斷使用者是否使用鍵盤上頭的數字鍵
            if (e.KeyCode < Keys.D0 || e.KeyCode > Keys.D9)
            {
                // 判斷使用者是否使用數字盤(keypad)輸入數字
                if (e.KeyCode < Keys.NumPad0 || e.KeyCode > Keys.NumPad9)
                {
                    // 判斷使用者是否輸入退後鍵(Backspace)
                    if (e.KeyCode != Keys.Back)
                    {
                        // 因為使用者並沒有輸入數字，因此將之設為true
                        nonNumberEntered = true;
                    }
                }
            }
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 判斷使用者是否已輸入數字
            if (nonNumberEntered == true)
            {
                // 因為沒有輸入數字，因此該輸入不予顯示，並提示使用者相關的訊息
                e.Handled = true;

                label2.Text = e.KeyChar + " 是不被允許的，" + Environment.NewLine;
                label2.Text += "請輸入數字或是退後鍵修正數字 !!!";
            }
            else
                label2.Text = e.KeyChar + " 是OK的";
        }
        public Form1()
        {
            InitializeComponent();
        }
    }
}


