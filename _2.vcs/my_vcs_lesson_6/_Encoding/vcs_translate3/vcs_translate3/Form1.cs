using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_translate3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        void print_data(byte[] data)
        {
            int i;
            int len;
            len = data.Length;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");
                if (i != (len - 1))
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button22_Click(object sender, EventArgs e)
        {
            string str = tb_string.Text;

            byte[] byteArray;

            richTextBox1.Text += "日語(Shift-JIS)編碼\n";
            byteArray = Encoding.GetEncoding("shift_jis").GetBytes(str);  //指名使用日語(Shift-JIS)編碼, 把字串轉成拜列
            print_data(byteArray);

            richTextBox1.Text += "簡體中文(GB2312)編碼\n";
            byteArray = Encoding.GetEncoding("gb2312").GetBytes(str);  //指名使用簡體中文(GB2312)編碼, 把字串轉成拜列
            print_data(byteArray);

            richTextBox1.Text += "正體中文(Big5)編碼\n";
            byteArray = Encoding.GetEncoding("big5").GetBytes(str);  //指名使用正體中文(Big5)編碼, 把字串轉成拜列
            print_data(byteArray);

            richTextBox1.Text += "Unicode編碼\n";
            byteArray = Encoding.GetEncoding("utf-16").GetBytes(str);  //指名使用Unicode編碼, 把字串轉成拜列
            print_data(byteArray);

            richTextBox1.Text += "Unicode (Big-Endian)編碼\n";
            byteArray = Encoding.GetEncoding("utf-16BE").GetBytes(str);  //指名使用Unicode (Big-Endian)編碼, 把字串轉成拜列
            print_data(byteArray);

            richTextBox1.Text += "Unicode (UTF-8)編碼\n";
            byteArray = Encoding.GetEncoding("utf-8").GetBytes(str);  //指名使用Unicode (UTF-8)編碼, 把字串轉成拜列
            print_data(byteArray);

        }

        byte ascii2int(char c)
        {
            byte value = 0;
            if ((c >= (Char)48 && c <= (Char)57))
                value = (byte)(c - 48);
            else if ((c >= 'A') && (c <= 'F'))
            {
                value = (byte)(c - 'A' + 10);
            }
            else if ((c >= 'a') && (c <= 'f'))
            {
                value = (byte)(c - 'a' + 10);
            }
            return value;
        }

        private void button23_Click(object sender, EventArgs e)
        {
            int i;
            int len;
            string str;
            str = tb_number.Text;
            richTextBox1.Text += "str is " + str + "\n";
            len = str.Length;
            richTextBox1.Text += "len is " + len.ToString() + "\n";
            str = str.Replace(" ", "");
            len = str.Length;
            richTextBox1.Text += "str is " + str + "\n";
            richTextBox1.Text += "len is " + len.ToString() + "\n";

            byte[] byteArray = new byte[len / 2];
            for (i = 0; i < (len / 2); i++)
            {
                byteArray[i] = (byte)(ascii2int(str[2 * i]) * 16 + ascii2int(str[2 * i + 1]));
            }

            print_data(byteArray);

            //byte[]轉成string：
            str = Encoding.Default.GetString(byteArray);
            richTextBox1.Text += "用預設編碼轉成字串\t" + str + "\n";

            richTextBox1.Text += "日語(Shift-JIS)解碼\n";
            str = Encoding.GetEncoding("shift_jis").GetString(byteArray);	//指名使用日語(Shift-JIS)解碼, 把拜列轉成字串
            richTextBox1.Text += str + "\n";

            richTextBox1.Text += "簡體中文(GB2312)解碼\n";
            str = Encoding.GetEncoding("gb2312").GetString(byteArray);	//指名使用簡體中文(GB2312)解碼, 把拜列轉成字串
            richTextBox1.Text += str + "\n";

            richTextBox1.Text += "正體中文(Big5)解碼\n";
            str = Encoding.GetEncoding("big5").GetString(byteArray);	//指名使用正體中文(Big5)解碼, 把拜列轉成字串
            richTextBox1.Text += str + "\n";

            richTextBox1.Text += "Unicode解碼\n";
            str = Encoding.GetEncoding("utf-16").GetString(byteArray);	//指名使用Unicode解碼解碼, 把拜列轉成字串
            richTextBox1.Text += str + "\n";

            richTextBox1.Text += "Unicode (Big-Endian)解碼\n";
            str = Encoding.GetEncoding("utf-16BE").GetString(byteArray);	//指名使用Unicode (Big-Endian)解碼, 把拜列轉成字串
            richTextBox1.Text += str + "\n";

            richTextBox1.Text += "Unicode (UTF-8)解碼\n";
            str = Encoding.GetEncoding("utf-8").GetString(byteArray);	//指名使用Unicode (UTF-8)解碼, 把拜列轉成字串
            richTextBox1.Text += str + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
