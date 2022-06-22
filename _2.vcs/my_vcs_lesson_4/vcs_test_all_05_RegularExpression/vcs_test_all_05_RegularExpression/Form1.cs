using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Text.RegularExpressions;

namespace vcs_test_all_05_RegularExpression
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

        private void button3_Click(object sender, EventArgs e)
        {
            //正規表示式的使用

            //正規表示式

            //使用方法
            //Regex.Match("String", @"正規表示式").ToString();

            string str = "USA stands for the United States of America with 50 states and 330 millions people.";

            string result = string.Empty;


            //只提出字串最前面或最後面的英文
            result = Regex.Match(str, @"[A-Z]+").ToString();
            richTextBox1.Text += "結果 : " + result + "\n";

            //只提出字串最前面或最後面的數字
            result = Regex.Match(str, @"[\d_]+").ToString();
            richTextBox1.Text += "結果 : " + result + "\n";

            //其他規則
            result = Regex.Match("123ABC456DEF", @"[A-Z]+[0-9]+").ToString(); //Output:"ABC456"
            richTextBox1.Text += "結果 : " + result + "\n";

            result = Regex.Match("123ABC456DeF", @"[0-9A-Z]+").ToString();//Output:"123ABC456D"
            richTextBox1.Text += "結果 : " + result + "\n";

            result = Regex.Match("123ABC456DeF", @"[0-9A-Za-z]+").ToString();//Output:"123ABC456DeF"
            richTextBox1.Text += "結果 : " + result + "\n\n\n\n";



            result = Regex.Match("ABC123D", @"[A-Z]+").ToString();//Output:"123ABC456DeF"
            richTextBox1.Text += "結果 : " + result + "\n";

            result = Regex.Match("ABC123", @"[A-Z]+").ToString();//Output:"123ABC456DeF"
            richTextBox1.Text += "結果 : " + result + "\n";

            result = Regex.Match("123ABC456DEF", @"[A-Z]+[0-9]+").ToString();//Output:"123ABC456DeF"
            richTextBox1.Text += "結果 : " + result + "\n";

            result = Regex.Match("123ABC", @"\d").ToString();//Output:"123ABC456DeF"
            richTextBox1.Text += "結果 : " + result + "\t數字\n";

            result = Regex.Match("ABC 123", @"[A-Z]+").ToString();//Output:"123ABC456DeF"
            richTextBox1.Text += "結果 : " + result + "\n";

            result = Regex.Match("123ABC456-DeF", @"[0-9A-Za-z\-]+").ToString();//Output:"123ABC456DeF"
            richTextBox1.Text += "結果 : " + result + "\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //驗證台灣手機號碼
            bool match;
            match = System.Text.RegularExpressions.Regex.IsMatch(textBox3.Text, @"^09[0-9]{8}$");
            if (match == true)
            {
                richTextBox1.Text += "OK\n";

            }
            else
            {
                richTextBox1.Text += "NG\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (Regex.IsMatch(textBox4.Text, @"^[\d,\.]+$"))
            {
                richTextBox1.Text += "是數值\n";
            }
            else
            {
                richTextBox1.Text += "不是數值\n";
            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //驗證Email格式
            //tb_email


        }

        //驗證Email格式
        public bool IsEmail(string str_Email)
        {
            return System.Text.RegularExpressions.Regex.IsMatch(str_Email, @"^([/w-/.]+)@((/[[0-9]{1,3}/.[0-9] {1,3}/.[0-9]{1,3}/.)|(([/w-]+/.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(/)?]$");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //驗證URl網址格式
            //tb_rul


        }

        //驗證URL網址格式
        public bool IsUrl(string str_url)
        {
            return System.Text.RegularExpressions.Regex.IsMatch(str_url, @"http(s)?://([/w-]+/.)+[/w-]+(/[/w- ./?%&=]*)?");
        }

        string getVid(string url)
        {
            string strRegex = "(?<=id_)(\\w+)";
            Regex reg = new Regex(strRegex);
            Match match = reg.Match(url);
            return match.ToString();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            string url = "http://v.youku.com/v_show/id_XNzk2NTI0MzMy.html";
            string vid = getVid(url);
            richTextBox1.Text += "vid : " + vid + "\n";
        }

    }
}
