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
            show_item_location();

            txtString_TextChanged(sender, e);
            txtTestString_TextChanged(sender, e);
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 600;
            y_st = 10;
            dx = 160 + 10;
            dy = 40 + 10;

            button8.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button16.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button17.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button18.Location = new Point(x_st + dx * 0, y_st + dy * 10);
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
            richTextBox1.Text += "正規表示式的使用\n";
            string url = "http://v.youku.com/v_show/id_XNzk2NTI0MzMy.html";
            string vid = getVid(url);
            richTextBox1.Text += "vid : " + vid + "\n";

            richTextBox1.Text += "取得email帳號\n";

            //取得email帳號

            string senderEmail = @"david@insighteyes.com";
            string[] sendFromUser = senderEmail.Split('@');
            int len = sendFromUser.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + sendFromUser[i] + "\n";
            }


            richTextBox1.Text += "用Regular Expression拆解e-mail帳號\n";

            List<string> emailList = new List<string>();
            string email = "xue@163.,xue@163.com12,2707@qq.com,,xue@yahoo.com.cn,xue@163.com,xue@163.com12";
            //  Regex reg2 = new Regex(@"^\da-zA-Z_]+@([-\dA-Za-z]+\.)+[a-zA-Z]{2,}$");驗證email的正則表達式  

            Regex reg = new Regex(@"(?<email>[\da-zA-Z_]+@([-\dA-Za-z]+\.)+[a-zA-Z]{2,})");
            Match m = reg.Match(email);
            foreach (Match item in reg.Matches(email))
            {
                emailList.Add(item.Groups["email"].Value);
            }
            len = emailList.Count;
            richTextBox1.Text += "共取得 : " + len.ToString() + " 個帳號\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + emailList[i] + "\n";
            }

            richTextBox1.Text += "正規表示式的使用";


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


            richTextBox1.Text += "檢查台灣手機號碼\n";

            string text = "0922123456";

            richTextBox1.Text += "Text = " + text + "\n";
            bool match;
            match = System.Text.RegularExpressions.Regex.IsMatch(text, @"^09[0-9]{8}$");
            if (match == true)
            {
                richTextBox1.Text += "OK\n";
            }
            else
            {
                richTextBox1.Text += "NG\n";
            }


            richTextBox1.Text += "檢查中國手機號碼\n";

            text = "13987654321";

            richTextBox1.Text += "Text = " + text + "\n";

            if (!IsHandset(text))
            {
                richTextBox1.Text += "NG ";
            }
            else
            {
                richTextBox1.Text += "OK ";
            }

            richTextBox1.Text += "檢查是否為數值\n";

            text = "0x1234";

            richTextBox1.Text += "Text = " + text + "\n";

            if (Regex.IsMatch(text, @"^[\d,\.]+$"))
            {
                richTextBox1.Text += "是數值\n";
            }
            else
            {
                richTextBox1.Text += "不是數值\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {


        }
    }
}
