using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Globalization;//for CultureInfo

namespace vcs_test_all_02_String
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
            dy = 40 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Text += "\n\n";
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {

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

        private void button2_Click(object sender, EventArgs e)
        {

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

        private void button4_Click(object sender, EventArgs e)
        {
            string my_string = "   歡迎來到 The United States of America     ";

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
            string my_string = "   歡迎來到 The United States of America     ";

            int result;
            richTextBox1.Text += "\n原字串:\t" + my_string + "\n";
            result = my_string.IndexOf("m", 0);
            richTextBox1.Text += "找到m在 " + result.ToString() + "\n";

            result = my_string.IndexOf("m", result + 1);
            richTextBox1.Text += "找到m在 " + result.ToString() + "\n";

            result = my_string.IndexOf("m", result + 1);
            richTextBox1.Text += "找到m在 " + result.ToString() + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string my_string = "   歡迎來到 The United States of America     ";

            string new_string = "";
            richTextBox1.Text += "\n原字串:\t" + my_string + "\n";
            new_string = my_string.Substring(29, 7);
            richTextBox1.Text += "從第29字開始抓7字:\t" + new_string + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string my_string = "   歡迎來到 The United States of America     ";
            string new_string = "";
            new_string = my_string.Trim();

            richTextBox1.Text += "\n";
            richTextBox1.Text += "原字串:\t|" + my_string + "|\t長度:\t" + my_string.Length.ToString() + "\n";
            richTextBox1.Text += "新字串:\t|" + new_string + "|\t長度:\t" + new_string.Length.ToString() + "\n";
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
            //分割字串範例
            string[] word_S = { };
            char[] split = { '-', ' ', ',', ':', '/' };     //依各種符號來切割字串

            string compile_time = "3/3/2021 01:35 下午";
            richTextBox1.Text += "原字串\t" + compile_time + "\n";
            richTextBox1.Text += "切割字串 :\n";

            word_S = compile_time.Split(split);     //切割字串

            foreach (string str in word_S)
            {
                richTextBox1.Text += str + "\n";
            }
        }

        //字串的 Split & Join
        private void button10_Click(object sender, EventArgs e)
        {
            string ols_string = "This is a book.";

            // Split the values at spaces, removing duplicates.
            string[] values = ols_string.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

            int len = values.Length;
            richTextBox1.Text += "原字串 : " + ols_string + "\t依空白可拆分為 " + len.ToString() + " 個, 分別是：\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 項 : " + values[i] + "\n";
            }

            // Rejoin them.
            string result = String.Join("*", values);
            richTextBox1.Text += "用星號連結組合起來 : " + result + "\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {
            //格式化列印 String.Format

            int a, b, c, d, ee, f;

            a = 123456;
            b = 2006;
            c = 3;
            d = 11;
            ee = 1234567890;
            f = 2468;

            richTextBox1.Text += "數字保留10位, 向左靠齊\n";
            richTextBox1.Text += string.Format("{0,-10}{1,-10}{2,-10}{3,-10}{4,-10}{5,-10}", a.ToString(), b.ToString(), c.ToString(), d.ToString(), ee.ToString(), f.ToString()) + "\n";
            richTextBox1.Text += "數字保留10位, 向右靠齊\n";
            richTextBox1.Text += string.Format("{0,10}{1,10}{2,10}{3,10}{4,10}{5,10}", a.ToString(), b.ToString(), c.ToString(), d.ToString(), ee.ToString(), f.ToString()) + "\n";
            richTextBox1.Text += "字串保留10位, 向左靠齊\n";
            richTextBox1.Text += string.Format("{0,-10}{1,-10}{2,-10}{3,-10}{4,-10}{5,-10}", "David", "Mary", "Doraemon", "Cat", "Dog", "Lion") + "\n";

            Random rnd = new Random();
            // Create new thread and display three random numbers.
            richTextBox1.Text += "Some currency values:\n";
            for (int ctr = 0; ctr <= 3; ctr++)
            {
                richTextBox1.Text += string.Format("{0:C2}", rnd.NextDouble() * 100) + "\n";
            }

            double aa = 123456789012345.456789;
            richTextBox1.Text += aa.ToString("N0", CultureInfo.InvariantCulture) + "\n";

            int bb = 1234567890;
            richTextBox1.Text += bb.ToString("N0", CultureInfo.InvariantCulture) + "\n";


            double used = 197594525696;

            double used2 = 184.02;

            //已使用空間 :	197,593,485,312 個位元組	184.02 GB
            richTextBox1.Text += string.Format("{0,-15}{1,20}{2,-10}{3,-10}",
                "已使用空間 :", used.ToString("N0", CultureInfo.InvariantCulture), " 個位元組", used2.ToString() + " GB") + "\n";

            //richTextBox1.Text += "已使用空間 :\t" + (drive.TotalSize - drive.AvailableFreeSpace).ToString("N0", CultureInfo.InvariantCulture) + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize - drive.AvailableFreeSpace)) + "\n";

        }

        private void button14_Click(object sender, EventArgs e)
        {
            //將數字前面補0

            // 將數字前面補0，補足長度為6 
            String snum = "5";
            String pnum = snum.PadLeft(5, '0');
            String fnum = String.Format("{0:00000}", Convert.ToInt16(snum));
            //MessageBox.Show("原始字串 : " + snum + "\n 透過 PadLeft : " + pnum + "\n 透過 String.Format : " + fnum);


            int n = 123;
            string zz1 = n.ToString().PadLeft(10, '0');
            richTextBox1.Text += "\nzz1 = " + zz1 + "\n";

            //string zz2 = Convert.ToInt32(n);
            string zz2 = String.Format("{0:0000000000}", Convert.ToInt16(n));
            richTextBox1.Text += "zz2 = " + zz2 + "\n";

            string zz3 = n.ToString("D10");
            richTextBox1.Text += "zz3 = " + zz3 + "\n";

        }

        private void button15_Click(object sender, EventArgs e)
        {
            //string.Format 的用法
            string animal1 = "Cats";
            string animal2 = "dogs";
            string result = string.Format("{0} and {1} are animals.", animal1, animal2);
            richTextBox1.Text += "string.Format 的用法\n結果 : " + result + "\n";

            string filename = string.Format("bmp_{0:yyyyMMdd_HHmmss}.bmp", DateTime.Now);
            richTextBox1.Text += "用string.Format製作依時檔案\n結果 : " + filename + "\n";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "左邊補空 和 右邊補空, 共5位數\n";
            int i = 123;
            richTextBox1.Text += "左邊補空-----" + i.ToString().PadLeft(5) + "-----\n";       //共5位數, 左邊補空
            richTextBox1.Text += "右邊補空-----" + i.ToString().PadRight(5) + "-----\n";       //共5位數, 右邊補空
        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }
    }
}

