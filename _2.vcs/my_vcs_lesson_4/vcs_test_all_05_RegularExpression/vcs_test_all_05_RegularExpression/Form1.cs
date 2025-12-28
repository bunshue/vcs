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


            //For 驗證身份證字號
            txtInput2.MaxLength = 10;//設定字元數最大值
            //txtInput2.Focus();//程式啟動就把焦點移到txtInput2
            //this.AcceptButton = button36;//按下enter就觸發button click事件     //要改??
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            groupBox0.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            groupBox2.Location = new Point(x_st + dx * 2 + 50, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 2 + 50, y_st + dy * 5);
            groupBox4.Location = new Point(x_st + dx * 4 + 0, y_st + dy * 0);

            richTextBox1.Size = new Size(310, 700);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 760);
            this.Text = "vcs_test_all_05_RegularExpression";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

        string getVid(string url)
        {
            string strRegex = "(?<=id_)(\\w+)";
            Regex reg = new Regex(strRegex);
            Match match = reg.Match(url);
            return match.ToString();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //正規表示式的使用
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

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void bt_re1_Click(object sender, EventArgs e)
        {
            //驗證每個月的天數
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

        private void bt_re2_Click(object sender, EventArgs e)
        {
            //驗證Email格式
            //tb_email
        }

        //驗證Email格式
        public bool IsEmail(string str_Email)
        {
            return System.Text.RegularExpressions.Regex.IsMatch(str_Email, @"^([/w-/.]+)@((/[[0-9]{1,3}/.[0-9] {1,3}/.[0-9]{1,3}/.)|(([/w-]+/.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(/)?]$");
        }

        private void bt_re3_Click(object sender, EventArgs e)
        {
            //驗證URl網址格式
            //tb_rul
        }

        //驗證URL網址格式
        public bool IsUrl(string str_url)
        {
            return System.Text.RegularExpressions.Regex.IsMatch(str_url, @"http(s)?://([/w-]+/.)+[/w-]+(/[/w- ./?%&=]*)?");
        }

        private void bt_re4_Click(object sender, EventArgs e)
        {
            //使用正則表達式判斷字串是否符合手機號碼格式。
            System.Text.RegularExpressions.Regex rex = new System.Text.RegularExpressions.Regex("^[0-9]{4}-[0-9]{6}$");
            if (rex.IsMatch(txtInput2.Text))
            {
                MessageBox.Show("符合");
            }
            else
            {
                MessageBox.Show("不符合");
            }
        }

        private void bt_re5_Click(object sender, EventArgs e)
        {
            //使用正則表達式判斷字串是否符合身分證格式。
            System.Text.RegularExpressions.Regex rex = new System.Text.RegularExpressions.Regex("^[A-Z]{1}[0-9]{9}$");
            if (rex.IsMatch(txtInput2.Text))
            {
                MessageBox.Show("符合");
            }
            else
            {
                MessageBox.Show("不符合");
            }
        }

        private void bt_re6_Click(object sender, EventArgs e)
        {
            if (txtInput2.Text.Trim().Length == 10)//長度達十個字才驗證
            {
                if (isIdentificationId(txtInput2.Text))//驗證身份證字號,正確回傳true
                {
                    txtInput2.Text = txtInput2.Text.ToUpper();//英文自動轉成大寫
                    MessageBox.Show(txtInput2.Text + "是正確的身份證字號", "", MessageBoxButtons.OK, MessageBoxIcon.None);
                }
                else//驗證身份證字號,不正確回傳false
                {
                    MessageBox.Show("身份證字號有誤", "", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else
            {
                MessageBox.Show("身份證字號有誤", "", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        // checkID
        public static bool isIdentificationId(string arg_Identify)
        {
            var d = false;
            if (arg_Identify.Length == 10)
            {
                arg_Identify = arg_Identify.ToUpper();
                if (arg_Identify[0] >= 0x41 && arg_Identify[0] <= 0x5A)
                {
                    var a = new[] { 10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33 };
                    var b = new int[11];
                    b[1] = a[(arg_Identify[0]) - 65] % 10;
                    var c = b[0] = a[(arg_Identify[0]) - 65] / 10;
                    for (var i = 1; i <= 9; i++)
                    {
                        b[i + 1] = arg_Identify[i] - 48;
                        c += b[i] * (10 - i);
                    }
                    if (((c % 10) + b[10]) % 10 == 0)
                    {
                        d = true;
                    }
                }
            }
            return d;
        }
    }
}
