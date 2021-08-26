using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Text.RegularExpressions;

namespace vcs_RegularExpression
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            txtString_TextChanged(sender, e);
            txtTestString_TextChanged(sender, e);
        }

        private void txtString_TextChanged(object sender, EventArgs e)
        {
            // Display only letters.
            txtLetters.Text = Regex.Replace(txtString.Text, "[^a-zA-Z]", "");

            // Display only digits.
            txtDigits.Text = Regex.Replace(txtString.Text, "[^0-9]", "");
        }

        // Make the replacements.
        private void txtTestString_TextChanged(object sender, EventArgs e)
        {
            Regex reg_exp = new Regex(txtPattern.Text);
            lblResult.Text = reg_exp.Replace(txtTestString.Text, txtReplacementPattern.Text);
        }

        private void do_regular_expression(object sender, EventArgs e)
        {
            try
            {
                Regex reg_exp = new Regex(txtPattern2.Text);
                lblResult2.Text = reg_exp.Replace(txtInput.Text, txtReplacementPattern2.Text);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //验证手机号是否正确
            if (!IsHandset(textBox1.Text))
            {
                richTextBox1.Text += "NG ";
            }
            else
            {
                richTextBox1.Text += "OK ";
            }
        }

        /// <summary>
        /// 验证手机号是否正确
        /// </summary>
        /// <param name="str_handset">手机号码字符串</param>
        /// <returns>返回布尔值</returns>
        public bool IsHandset(string str_handset)
        {
            //使用正则表达式判断是否匹配
            return System.Text.RegularExpressions.Regex.IsMatch(str_handset, @"^[1]+[3,5]+\d{9}$");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //验证每月的31天
            if (!IsDay(textBox2.Text.Trim()))
            {
                richTextBox1.Text += "输入日期的范围不正确!!!\n";
            }
            else
            {
                richTextBox1.Text += "输入信息正确!!!!!\n";
            }
        }

        /// <summary>
        /// 验证每月的31天
        /// </summary>
        /// <param name="str_day">每月的天数</param>
        /// <returns>返回布尔值</returns>
        public bool IsDay(string str_day)
        {
            //使用正则表达式判断是否匹配
            return System.Text.RegularExpressions.Regex.IsMatch(str_day, @"^((0?[1-9])|((1|2)[0-9])|30|31)$");
        }





    }
}
