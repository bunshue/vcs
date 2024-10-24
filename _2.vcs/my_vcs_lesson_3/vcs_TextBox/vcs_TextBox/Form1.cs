﻿using System;
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
        TextBox RightKeyCarte;//聲明一個自定義類CustomTextBoxGroup的對象

        public Form1()
        {
            InitializeComponent();
        }

        // Prepare the TextBox.
        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單
            textBox_use_scrollbar.ScrollBars = ScrollBars.Both;

            // Register the TextChanged event handler.
            textBox2.TextChanged += textBox2_TextChanged;
            textBox2.Multiline = true;
            textBox2.ScrollBars = ScrollBars.None;

            // Make the TextBox fit its initial text.
            AutoSizeTextBox(textBox2);

            this.AcceptButton = button5;            //在表單按enter就執行button5按鈕的動作


            textBox4.MaxLength = 3;    //設最多只能輸入3位數
            textBox4.ReadOnly = false;   //設為唯讀不能輸入, 改了
            textBox4.TabIndex = 0;     //設為第一個停駐焦點
            textBox4.Focus();    //將停駐焦點移到txtDegree

            //製作一個加上底線的TextBox  在文字框下劃一條底線
            TextBox goal = new CustomTextBoxGroup();//定義一個TextBox對像goal
            goal.Parent = this;//獲取或設置自定義TextBox控件的父容器
            goal.Text = "在文字框下劃一條底線";
            goal.Size = new Size(200, 40);
            goal.BackColor = Color.Pink;
            goal.Location = new Point(470, 500);
            this.Controls.Add(goal);//向窗體中添加自定義TextBox控件goal


            this.RightKeyCarte = new CustomTextBoxGroup2();//實例化該類的對象
            this.RightKeyCarte.Parent = this; //設定自定義控件的父容器為當前窗口
            RightKeyCarte.Text = "禁止使用滑鼠右鍵";
            RightKeyCarte.Location = new Point(470, 550);

            this.Controls.Add(this.RightKeyCarte);//在當前窗體中添加自定義控件


            textBox8.KeyPress += new KeyPressEventHandler(textBox8_KeyPress);
            label11.Text = "TextBox只允許僅允許\n數字, Enter, Backspace, +-*/()";
        }


        /// <summary>
        /// 限制textBox中的字符輸入, 用KeyPress事件
        /// 僅允許 數字, Enter, Backspace, +-*/()
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        void textBox8_KeyPress(object sender, KeyPressEventArgs e)
        {
            //如果輸入的不是數字類別，也不是回車鍵、Backspace鍵、+ - * / ( )，則textBox1_KeyPress取消該輸入
            if (!(Char.IsNumber(e.KeyChar)) && e.KeyChar != (char)13 && e.KeyChar != (char)8 && e.KeyChar != (char)40 && e.KeyChar != (char)41 && e.KeyChar != (char)42 && e.KeyChar != (char)43 && e.KeyChar != (char)45 && e.KeyChar != (char)47)
            {
                e.Handled = true;
            } 
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十六進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || ((e.KeyChar >= 'A') && (e.KeyChar <= 'F')) || ((e.KeyChar >= 'a') && (e.KeyChar <= 'f')) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;  //未處理, 表示要顯示出來
            }
            else
            {
                e.Handled = true;   //已處理, 表示不顯示出來
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
            /* same
            if ((e.KeyChar != 8 && !char.IsDigit(e.KeyChar)) && e.KeyChar != 13)
            {
                //MessageBox.Show("只允許輸入數字", "操作提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                e.Handled = true;
            }
            */
            byte asc = Convert.ToByte(e.KeyChar);
            if (asc < 48 || asc > 57)
            {
                e.Handled = true;  //不接受字元
            }
        }

        private void textBox5_KeyPress(object sender, KeyPressEventArgs e)
        {
            //只允許輸入小寫英文字母
            if (e.KeyChar < 'a' || e.KeyChar > 'z')
            {
                e.Handled = true;  //不接受字元
            }
        }

        //拖曳文字內容到其他TextBox ST
        //須設定 textBox7.AllowDrop = true;
        private void textBox6_MouseMove(object sender, MouseEventArgs e)
        {
            if ((e.Button & MouseButtons.Left) == MouseButtons.Left)    //是否按下滑鼠左鍵
            {
                this.Cursor = new Cursor("../../arrow.cur");    //設置滑鼠鼠標樣式
                //拖曳文字
                DragDropEffects dropEffect = this.textBox6.DoDragDrop(this.textBox6.Text, DragDropEffects.Copy | DragDropEffects.Link);
            }
        }

        private void textBox7_DragDrop(object sender, DragEventArgs e)
        {
            textBox7.Text += e.Data.GetData(DataFormats.Text).ToString();//显示拖放文本
        }

        private void textBox7_DragEnter(object sender, DragEventArgs e)
        {
            e.Effect = DragDropEffects.Copy;//设置复制操作
        }
        //拖曳文字內容到其他TextBox SP



    }
}
