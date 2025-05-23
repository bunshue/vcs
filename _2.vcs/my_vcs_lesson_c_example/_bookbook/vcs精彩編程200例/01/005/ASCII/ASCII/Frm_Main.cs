﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ASCII
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        private void btn_ToASCII_Click(object sender, EventArgs e)
        {
            if (txt_char.Text != string.Empty)//判断输入是否为空
            {
                //判断输入是否为字母                         //頗為特別的語法
                if (Encoding.GetEncoding("unicode").GetBytes(new char[] { txt_char.Text[0] })[1] == 0)
                {
                    //得到字符的ASCII码值
                    txt_ASCII.Text = Encoding.GetEncoding("unicode").GetBytes(txt_char.Text)[0].ToString();
                }
                else
                {
                    txt_ASCII.Text = string.Empty;  //输出空字符串
                    MessageBox.Show("请输入字母！", "提示！");//提示用户信息
                }
            }
        }

        private void btn_ToChar_Click(object sender, EventArgs e)
        {
            if (txt_ASCII2.Text != string.Empty)//判断输入是否为空
            {
                int P_int_Num;//定义整型局部变量

                //将输入的字符转换为数字
                if (int.TryParse(txt_ASCII2.Text, out P_int_Num))
                {
                    txt_Char2.Text = ((char)P_int_Num).ToString();//将ASCII码转换为字符
                }
                else
                {
                    //如果输入不符合要求弹出提示框
                    MessageBox.Show("请输入正确ASCII码值。", "错误！");
                }
            }

            string P_str_temp = "abc";
            string P_str = Encoding.GetEncoding("unicode").GetBytes(new char[] { P_str_temp[0] })[0].ToString();
            richTextBox1.Text += "aaa\t" + P_str_temp + "\n";
            richTextBox1.Text += "bbb\t" + P_str + "\n";
        }
    }
}

