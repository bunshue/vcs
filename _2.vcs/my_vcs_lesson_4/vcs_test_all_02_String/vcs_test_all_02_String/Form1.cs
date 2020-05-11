using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_02_String
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string str = "Alice is a good student!!";
            richTextBox1.Text += "\n原字串:\t" + str + "\n";
            richTextBox1.Text += "轉成大寫:\t︰" + str.ToUpper() + "\n";
            richTextBox1.Text += "轉成小寫:\t" + str.ToLower() + "\n";
            richTextBox1.Text += "插入字串寫:\t" + str.Insert(6, "Wang ") + "\n";
            richTextBox1.Text += "原字串依空白拆開:\n";

            string[] strArray = str.Split(' ');
            for (int i = 0; i < strArray.Length; i++)
            {
                richTextBox1.Text += strArray[i] + "\n";
                //Console.WriteLine(strArray[i]);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string str = "Welcome to the United States and have a nice day.";
            string[] split_str = new string[5];
            split_str = str.Split(' '); //以空白當分隔符號
            richTextBox1.Text += "\n原字串:\t" + str + "\n";
            richTextBox1.Text += "原字串依空白拆開:\n";
            foreach (string tmp in split_str)
            {
                richTextBox1.Text += tmp + "\n";
            }
        }

        string my_string = "   歡迎來到Myson Century!   ";
        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n";
            richTextBox1.Text += "字串:\t" + my_string + " 長度:\t" + my_string.Length.ToString() + "\n";

            string new_string = "";
            for (int i = 0; i < my_string.Length; i++)
            {
                new_string += my_string[i];
            }
            richTextBox1.Text += "原字串:\t" + my_string + " 長度:\t" + my_string.Length.ToString() + "\n";
            richTextBox1.Text += "新字串:\t" + new_string + " 長度:\t" + new_string.Length.ToString() + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int result;
            richTextBox1.Text += "\n原字串:\t" + my_string + "\n";
            result = my_string.IndexOf("n", 0);
            richTextBox1.Text += "找到n在 " + result.ToString() + "\n";

            result = my_string.IndexOf("n", result + 1);
            richTextBox1.Text += "找到n在 " + result.ToString() + "\n";

            result = my_string.IndexOf("n", result + 1);
            richTextBox1.Text += "找到n在 " + result.ToString() + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string new_string = "";
            richTextBox1.Text += "\n原字串:\t" + my_string + "\n";
            new_string = my_string.Substring(7, 5);
            richTextBox1.Text += "從第7字開始抓5字:\t" + new_string + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string new_string = "";
            new_string = my_string.Trim();

            richTextBox1.Text += "\n";
            richTextBox1.Text += "原字串:\t|" + my_string + "|\t長度:\t" + my_string.Length.ToString() + "\n";
            richTextBox1.Text += "新字串:\t|" + new_string + "|\t長度:\t" + new_string.Length.ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //字串處理
            string str1 = "群曜醫電股份有限公司 Insight Medical Solutions Inc.";
            string str2 = string.Empty;
            richTextBox1.Text += "\n原字串:\t" + str1 + "\n";
            str2 = str1.Substring(0, 4);    //從0取4
            richTextBox1.Text += "原字串從0取4字:\t" + str2 + "\n";
            str2 = str1.Substring(4, 6);    //從4取6
            richTextBox1.Text += "原字串從4取6字:\t" + str2 + "\n";
            str2 = str1.Substring(8, 10);   //從8取10
            richTextBox1.Text += "原字串從8取10字:\t" + str2 + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            string str;
            //char[] cChar = new char[5] { 'a', 'b', 'c', 'd', 'e' };
            str = "中間路線";
            richTextBox1.Text += "\n原字串:\t" + str + "\n";
            byte[] byteData = Encoding.Default.GetBytes(str);
            richTextBox1.Text += "使用GetBytes轉成拜列\t";
            foreach (byte b in byteData)
            {
                richTextBox1.Text += b.ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";

            string nn = string.Empty;
            nn = Encoding.Default.GetString(byteData);
            richTextBox1.Text += "將此拜列使用GetString轉成字串, 新字串:\t" + nn + "\n";

            byteData[1] = (byte)(byteData[1] + 2);
            nn = Encoding.Default.GetString(byteData);
            richTextBox1.Text += "修改拜列, 將此拜列使用GetString轉成字串, 新字串:\t" + nn + "\n";

            str = "ABCDE";
            // Encoding.GetBytes方法，將 String 轉為 Byte 序列
            byte[] stringConvByte = Encoding.Default.GetBytes(str);
            // Encoding.GetString方法，將 Byte 序列 轉為 String
            string byteConvStrig = Encoding.Default.GetString(stringConvByte);

            int i;
            richTextBox1.Text += "\n原字串:\t" + str + "\t長度:\t" + str.Length.ToString() + "\t內容:\t";
            for (i = 0; i < str.Length; i++)
            {
                richTextBox1.Text += str[i] + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "轉成拜列\t長度:\t" + stringConvByte.Length.ToString() + "\t內容:\t";
            for (i = 0; i < stringConvByte.Length; i++)
            {
                richTextBox1.Text += stringConvByte[i].ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "轉成字串\t長度:\t" + byteConvStrig.Length.ToString() + "\n";

            byte[] byteArray = new byte[5] { 0x41, 0x42, 0x43, 0x44, 0x45 };

            str = System.Text.Encoding.Default.GetString(byteArray);

            richTextBox1.Text += "使用GetString將拜列轉成字串:\t" + str + "\n";

            str = "this is a lion-mouse";
            richTextBox1.Text += "\n原字串:\t" + str + "\n";

            byteArray = System.Text.Encoding.Default.GetBytes(str);
            richTextBox1.Text += "使用GetBytes將字串轉成拜列\t內容:\t";
            for (i = 0; i < byteArray.Length; i++)
            {
                richTextBox1.Text += (char)byteArray[i] + " ";  //多了(char)變成%c
            }
            richTextBox1.Text += "\n";

            //Byte型態的陣列轉換為字串
            int bytes = 0;
            Byte[] byte_array = new Byte[256];
            String new_string = "";
            byte_array[0] = (byte)'A';
            byte_array[1] = (byte)'B';
            byte_array[2] = (byte)'C';
            bytes = 3;
            // 將Byte型態的陣列轉換為字串
            new_string = Encoding.ASCII.GetString(byte_array, 0, bytes);
            richTextBox1.Text += "使用GetString將拜列轉成字串\t" + new_string + "\n";

            //字串轉換為Byte型態的陣列
            str = "this is a lion-mouse";
            Byte[] byte_array2 = Encoding.ASCII.GetBytes(str);
            richTextBox1.Text += "使用GetBytes將字串轉成拜列\t內容:\t";
            foreach (char c in byte_array2)
            {
                richTextBox1.Text += c.ToString() + " ";
            }
            richTextBox1.Text += "\n";


        }


    }
}
