using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_TextBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Prepare the TextBox.
        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單

            // Register the TextChanged event handler.
            textBox2.TextChanged += textBox2_TextChanged;
            textBox2.Multiline = true;
            textBox2.ScrollBars = ScrollBars.None;

            // Make the TextBox fit its initial text.
            AutoSizeTextBox(textBox2);

            this.AcceptButton = button5;            //在表單按enter就執行button5按鈕的動作
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十六進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || ((e.KeyChar >= 'A') && (e.KeyChar <= 'F')) || ((e.KeyChar >= 'a') && (e.KeyChar <= 'f')) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length <= 0)
            {
                label2.Text = "未輸入數字";
            }
            else
            {
                string input = textBox1.Text; ;
                double output = 0;
                byte value = 0;
                for (int i = 0; i < input.Length; i++)
                {
                    if ((input[i] >= (Char)48 && input[i] <= (Char)57))
                    {
                        value = (byte)(input[i] - 48);

                    }
                    else if ((input[i] >= 'A') && (input[i] <= 'F'))
                    {
                        value = (byte)(input[i] - 'A' + 10);
                    }
                    else if ((input[i] >= 'a') && (input[i] <= 'f'))
                    {
                        value = (byte)(input[i] - 'a' + 10);
                    }
                    output = output * 16 + value;
                    //MessageBox.Show("data : " + input[i] + " value : " + value);
                }
                label2.Text = "結果：" + output.ToString();
            }
        }







        // Make the TextBox fit its new contents.
        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            AutoSizeTextBox(sender as TextBox);
        }

        // Make the TextBox fit its contents.
        private void AutoSizeTextBox(TextBox txt)
        {
            const int x_margin = 0;
            const int y_margin = 2;
            Size size = TextRenderer.MeasureText(txt.Text, txt.Font);
            txt.ClientSize =
                new Size(size.Width + x_margin, size.Height + y_margin);
        }

        //登入
        private void button5_Click(object sender, EventArgs e)
        {
            string Username;
            string Password;
            Username = tb_id.Text;	        //取得textBox的內容為名字
            Password = tb_password.Text;	//取得textBox的內容為密碼
            if (Username == "root" && Password == "123456")
                MessageBox.Show("您是合法的使用者！！");
            else
                MessageBox.Show("滾蛋！！！！");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            tb_id.Clear();
            tb_password.Text = "";
        }

        private void textBox3_KeyPress(object sender, KeyPressEventArgs e)
        {
            //只允許輸入數字
            if ((e.KeyChar != 8 && !char.IsDigit(e.KeyChar)) && e.KeyChar != 13)
            {
                //MessageBox.Show("只允許輸入數字", "操作提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                e.Handled = true;
            }

        }
    }
}
