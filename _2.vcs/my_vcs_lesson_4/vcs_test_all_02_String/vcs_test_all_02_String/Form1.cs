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
            show_numbers();
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
            dx = 200 + 5;
            dy = 60 + 5;

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

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            groupBox1.Size = new Size(326, 650);
            groupBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            richTextBox1.Size = new Size(500, 650);
            richTextBox1.Location = new Point(x_st + dx * 5 - 70, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            dy = 70;
            int dd = 26;
            lb_number0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_number1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_number2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_number3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_number4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            lb_number5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            lb_number6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            lb_number0b.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            lb_number1b.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            lb_number2b.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            lb_number3b.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            lb_number4b.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            lb_number5b.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            lb_number6b.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            tb_number0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd);
            tb_number1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd);
            tb_number2.Location = new Point(x_st + dx * 0, y_st + dy * 2 + dd);
            tb_number3.Location = new Point(x_st + dx * 0, y_st + dy * 3 + dd);
            tb_number4.Location = new Point(x_st + dx * 0, y_st + dy * 4 + dd);
            tb_number5.Location = new Point(x_st + dx * 0, y_st + dy * 5 + dd);
            tb_number6.Location = new Point(x_st + dx * 0, y_st + dy * 6 + dd);

            this.Size = new Size(1490, 710);
            this.Text = "vcs_test_all_02_String";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "字串 轉 拜列, GetBytes\n";

            string str1 = "lion-mouse";
            richTextBox1.Text += "字串1 : " + str1 + "\n";
            byte[] byte_array1 = Encoding.ASCII.GetBytes(str1);

            richTextBox1.Text += "拜列長度 : " + byte_array1.Length.ToString() + "\n";
            richTextBox1.Text += "拜列內容 :\n";
            int i;
            for (i = 0; i < byte_array1.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + (char)byte_array1[i] + "\t" + byte_array1[i].ToString("X2") + "\n";
            }

            richTextBox1.Text += "\n拜列 轉 字串, GetString\n";
            byte[] byte_array2 = new byte[10];
            for (i = 0; i < byte_array2.Length; i++)
            {
                byte_array2[i] = (byte)(0x41 + i);
            }
            richTextBox1.Text += "拜列長度 : " + byte_array2.Length.ToString() + "\n";
            string str2 = Encoding.ASCII.GetString(byte_array2);
            richTextBox1.Text += "字串2 : " + str2 + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "字串功能測試\n";

            string str = "Alice is a good student!!";
            richTextBox1.Text += "原字串:\t\t\t" + str + "\n";
            richTextBox1.Text += "ToUpper() 轉大寫:\t" + str.ToUpper() + "\n";
            richTextBox1.Text += "ToLower() 轉小寫:\t" + str.ToLower() + "\n";
            richTextBox1.Text += "Insert() 插入字串:\t" + str.Insert(6, "Wang ") + "\n";

            richTextBox1.Text += "Split() 依空白拆開:\t";
            string[] strArray = str.Split(' ');
            for (int i = 0; i < strArray.Length; i++)
            {
                richTextBox1.Text += strArray[i] + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            str = "Welcome to the United States and have a nice day.";
            string[] split_str = new string[5];
            split_str = str.Split(' '); //以空白當分隔符號
            richTextBox1.Text += "\n原字串:\t" + str + "\n";
            richTextBox1.Text += "原字串依空白拆開:\n";
            foreach (string tmp in split_str)
            {
                richTextBox1.Text += tmp + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //分割字串範例
            string[] word_S = { };
            char[] split = { '-', ' ', ',', ':', '/' };     //依各種符號來切割字串

            string compile_time = "3/3/2021 01:35 下午";
            richTextBox1.Text += "原字串\t" + compile_time + "\n";
            richTextBox1.Text += "切割字串 :\n";

            word_S = compile_time.Split(split);     //切割字串

            foreach (string tmp in word_S)
            {
                richTextBox1.Text += tmp + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //字串的 Split & Join

            string ols_string = "This is a book.";

            // Split the values at spaces, removing duplicates.
            string[] values = ols_string.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

            int len = values.Length;
            richTextBox1.Text += "原字串 : " + ols_string + "\t依空白可拆分為 " + len.ToString() + " 個, 分別是：\n";
            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 項 : " + values[i] + "\n";
            }

            // Rejoin them.
            string result = String.Join("*", values);
            richTextBox1.Text += "用星號連結組合起來 : " + result + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //split
            str = "this-is-a-lion-mouse";
            string[] word = str.Split('-');
            richTextBox1.Text += "原字串: " + str + "\n";
            richTextBox1.Text += "分割後, len = " + word.Length.ToString() + ", 內容:\n";
            foreach (string s in word)
            {
                richTextBox1.Text += s + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //String用法
            //String用法 Remove

            str = "0123456789";
            string delstr1;
            string delstr2;
            delstr1 = str.Remove(6);//刪除字符串索引為6後面的字符
            delstr2 = str.Remove(5, 5);//刪除字符串索引自5開始後數5個長度的字符
            Console.WriteLine(delstr1);
            Console.WriteLine(delstr2);
            Console.ReadLine();

            //String用法 CopyTo
            str = "This is a string";
            string copystr;
            copystr = string.Copy(str);
            char[] newchar = new char[20];
            str.CopyTo(5, newchar, 0, 11);
            Console.WriteLine(copystr);
            Console.WriteLine(newchar);
            Console.ReadLine();

            //String用法 字串查找
            str = "This is a string";
            int rh1 = str.IndexOf("i");
            int rh2 = str.LastIndexOf("i");
            if (rh1 >= 0)
            {
                Console.WriteLine("字符i在字符串str第一次出現的位置是：{0}", rh1);
                Console.WriteLine("字符i在字符串str最後一次出現的位置是：{0}", rh2);
            }
            else
            {
                Console.WriteLine("字符i在字符串str未出現");
            }

            //轉義字符 @
            Console.WriteLine(@"C:\Windows\system32");//第一種輸出格式就是在前面加@
            Console.WriteLine("C:\\Windows\\system32");//第二種輸出格式就是將"\"改成"\\"
            Console.ReadLine();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //連接符 與 佔位符
            string str1 = "lion";
            string str2 = "mouse";
            string m = String.Format("{0}", str1);   //字符串格式輸出
            string n = String.Format("{0}", str2);

            richTextBox1.Text += "str = " + m + "-" + n + "\n";     //用“+”連接符
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            string old_string = "   歡迎來到 The United States of America     ";

            richTextBox1.Text += "\n";
            richTextBox1.Text += "字串:\t" + old_string + " 長度:\t" + old_string.Length.ToString() + "\n";

            string new_string = "";
            for (int i = 0; i < old_string.Length; i++)
            {
                new_string += old_string[i];
            }
            richTextBox1.Text += "原字串:\t" + old_string + " 長度:\t" + old_string.Length.ToString() + "\n";
            richTextBox1.Text += "新字串:\t" + new_string + " 長度:\t" + new_string.Length.ToString() + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string old_string = "   歡迎來到 The United States of America     ";

            int result;
            richTextBox1.Text += "\n原字串:\t" + old_string + "\n";
            result = old_string.IndexOf("m", 0);
            richTextBox1.Text += "找到m在 " + result.ToString() + "\n";

            result = old_string.IndexOf("m", result + 1);
            richTextBox1.Text += "找到m在 " + result.ToString() + "\n";

            result = old_string.IndexOf("m", result + 1);
            richTextBox1.Text += "找到m在 " + result.ToString() + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string old_string = "   歡迎來到 The United States of America     ";
            string new_string = "";
            richTextBox1.Text += "\n原字串:\t" + old_string + "\n";
            new_string = old_string.Substring(29, 7);
            richTextBox1.Text += "從第29字開始抓7字:\t" + new_string + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string old_string = "   歡迎來到 The United States of America     ";
            string new_string = "";
            new_string = old_string.Trim();

            richTextBox1.Text += "\n";
            richTextBox1.Text += "原字串:\t|" + old_string + "|\t長度:\t" + old_string.Length.ToString() + "\n";
            richTextBox1.Text += "新字串:\t|" + new_string + "|\t長度:\t" + new_string.Length.ToString() + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //各種進位轉換

            //十六進位顯示
            int value1 = 65535;
            int value2 = 0x12345;

            richTextBox1.Text += "十進位：" + value1 + "  十六進位： 0x" + Convert.ToString(value1, 16) + "\n";
            richTextBox1.Text += "十六進位： 0x" + Convert.ToString(value2, 16) + "  十進位：" + value2 + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //16進制與字符串、字節數組之間的轉換

            //十進制轉二進制
            Console.WriteLine("十進制166的二進制表示: " + Convert.ToString(166, 2));
            //十進制轉八進制
            Console.WriteLine("十進制166的八進制表示: " + Convert.ToString(166, 8));
            //十進制轉十六進制
            Console.WriteLine("十進制166的十六進制表示: " + Convert.ToString(166, 16));

            //二進制轉十進制
            Console.WriteLine("二進制 111101 的十進制表示: " + Convert.ToInt32("111101", 2));
            //八進制轉十進制
            Console.WriteLine("八進制 44 的十進制表示: " + Convert.ToInt32("44", 8));
            //十六進制轉十進制
            Console.WriteLine("十六進制 CC的十進制表示: " + Convert.ToInt32("CC", 16));

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //十六進位轉換
            string hexValues = "48 65 6C 6C 6F 20 57 6F 72 6C 64 21";
            string[] hexValuesSplit = hexValues.Split(' ');
            richTextBox1.Text += "hexValues\tvalue\tstringValue\tcharValue\n";
            foreach (String hex in hexValuesSplit)
            {
                // Convert the number expressed in base-16 to an integer.
                int value = Convert.ToInt32(hex, 16);
                // Get the character corresponding to the integral value.
                string stringValue = Char.ConvertFromUtf32(value);
                char charValue = (char)value;
                richTextBox1.Text += hex + '\t' + value.ToString() + '\t' + stringValue + '\t' + charValue + '\n';
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //10進位轉十六進位
            int dint = 170;
            string strHex = String.Format("{0:X2}", dint);    //X2的2代表若缺0會自動補0，所以沒有2也沒關係
            richTextBox1.Text += "result : " + strHex + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //16進位轉10進位
            string s2 = "AB";

            //轉換10進位
            int j = 0;
            int result = 0;

            for (int i = 0; i < s2.Length; i++)
            {
                result = result * 16;
                j = s2[i] - 48;
                if (j < 10)
                {
                    result = result + j;
                }
                else
                {
                    result = result + j - 39;
                }
            }
            richTextBox1.Text += "result : " + result.ToString() + "\n";

            //另一種寫法
            //Convert.ToInt32("100", 16);

            richTextBox1.Text += "result : " + Convert.ToInt32("AB", 16).ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //10進位轉各種進位
            int a, n, r;

            a = 12345;

            string[] m = {"0", "1", "2", "3",
                           "4", "5", "6", "7",
                           "8", "9", "A", "B",
                           "C", "D", "E", "F"};
            string s = "";

            richTextBox1.Text += "10進位數字\t" + a.ToString() + "\n";

            n = 2;
            s = "";
            for (; a > 0; a = a / n)
            {
                r = a % n;  //取得餘數

                s = m[r] + s; // 查表，串列左邊
            }

            richTextBox1.Text += "2進位\t" + s + "\n";

            a = 12345;
            n = 8;
            s = "";
            for (; a > 0; a = a / n)
            {
                r = a % n;  //取得餘數

                s = m[r] + s; // 查表，串列左邊
            }

            richTextBox1.Text += "8進位\t" + s + "\n";

            a = 12345;
            n = 16;
            s = "";
            for (; a > 0; a = a / n)
            {
                r = a % n;  //取得餘數
                s = m[r] + s; // 查表，串列左邊
            }

            richTextBox1.Text += "16進位\t" + s + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //StringBuilder語法

            StringBuilder sb1 = new StringBuilder();
            sb1.Append("字串111\n");
            sb1.Append("字串222\n");
            sb1.Append("字串333\n");
            sb1.Append("字串444\n");

            richTextBox1.Text += "取得字串 : " + sb1.ToString() + "\n";

            //StringBuilder 就是 字符串相加
            StringBuilder sb2 = new StringBuilder("字串111");
            sb2.Append("字串222");
            sb2.Append("字串333");
            sb2.Append("字串444");

            richTextBox1.Text += "取得字串 : " + sb2 + "\n";

            //StringBuilder語法3
            richTextBox1.Text += "aaa\n";

            StringBuilder sb3 = new StringBuilder();
            for (int i = 128; i < 128 + 20; i++)
            {
                sb3.Append(i.ToString("X2"));
            }

            string result = sb3.ToString();
            richTextBox1.Text += result + "\n";

            richTextBox1.Text += "bbb\n";

            StringBuilder sb4 = new StringBuilder();
            for (int i = 128; i < 128 + 20; i++)
            {
                sb4.AppendFormat("{0:X2}", i);
            }
            //foreach (byte b in ms.ToArray())
            {
                //sb.AppendFormat("{0:X2}", b);
            }
            string all_data = sb4.ToString();
            richTextBox1.Text += all_data + "\n";

            richTextBox1.Text += "ccc\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //StringBuilder語法

            //建立StringBuilder物件
            StringBuilder text = new StringBuilder();

            richTextBox1.Text += "預設容量：" + text.Capacity.ToString() + "\n";

            //使用 Append()方法附加字串
            text.Append("ABCDEFGHIJ");
            richTextBox1.Text += "目前長度：" + text.Length.ToString() + "\n";
            richTextBox1.Text += "目前容量：" + text.Capacity.ToString() + "\n";

            //再增加一筆資料 容量會長大
            text.Append("ABCDEFGHIJ");
            richTextBox1.Text += "目前長度：" + text.Length.ToString() + "\n";
            richTextBox1.Text += "目前容量：" + text.Capacity.ToString() + "\n";

            richTextBox1.Text += "在字串尾端加入換行字元後\n";
            text.AppendLine("\n");
            richTextBox1.Text += "目前長度：" + text.Length.ToString() + "\n";
            richTextBox1.Text += "目前容量：" + text.Capacity.ToString() + "\n";

            richTextBox1.Text += "在字串尾端加入另一個字串後\n";
            text.AppendLine("It is a wonderful English proverb.");
            richTextBox1.Text += "目前長度：" + text.Length.ToString() + "\n";
            richTextBox1.Text += "目前容量：" + text.Capacity.ToString() + "\n";

            richTextBox1.Text += "目前字串：" + text + "\n";

            richTextBox1.Text += "改變內容\n";
            for (int i = 0; i < 3; i++)
            {
                text[i] = 'X';
            }

            richTextBox1.Text += "變更後字串：" + text + "\n";

            //Remove()方法, 只移除一次
            string dddd = "EFG";    //欲移除字串
            //取得欲刪除字串的索引編號
            int index = text.ToString().IndexOf(dddd);
            if (index >= 0)
                text.Remove(index, dddd.Length);
            richTextBox1.Text += "變更後字串：" + text + "\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //string.Format語法

            string animal1 = "Cats";
            string animal2 = "dogs";
            string result = string.Format("{0} and {1} are animals.", animal1, animal2);
            richTextBox1.Text += "string.Format 的用法\n結果 : " + result + "\n";

            string filename = string.Format("bmp_{0:yyyyMMdd_HHmmss}.bmp", DateTime.Now);
            richTextBox1.Text += "用string.Format製作依時檔案\n結果 : " + filename + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //格式化列印

            Console.WriteLine("The value 99999 in different ways:");
            Console.WriteLine("c format : {0:c}", 99999);
            Console.WriteLine("d9 format : {0:d9}", 99999);
            Console.WriteLine("f format : {0:f3}", 99999);
            Console.WriteLine("g format : {0:g}", 99999);

            Console.WriteLine("n format : {0:n}", 99999);
            Console.WriteLine("E format : {0:E}", 99999);
            Console.WriteLine("e format : {0:e}", 99999);
            Console.WriteLine("X format : {0:X}", 99999);
            Console.WriteLine("x format : {0:x}", 99999);

            int x1 = 3;
            int x2 = 8;
            int x3 = 3;
            int x4 = 4;
            int x5 = 2;
            string xx = String.Format("{0}-{1}-{2}-{3}-{4}", x1, x2, x3, x4, x5);
            richTextBox1.Text += "xx = " + xx + "\n";

            richTextBox1.Text += "String.Format是將指定的 String類型的數據中的每個格式項替換為相應對象的值的文本等效項。\n";

            string p1 = "Jackie";
            string p2 = "Aillo";

            string string1 = String.Format("Hello {0}, I'm {1}", p1, p2);
            richTextBox1.Text += "string1 = " + string1 + "\n";

            string string2 = String.Format("Hello {0}, I'm {1}", "Jackie", "Aillo");
            richTextBox1.Text += "string2 = " + string2 + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            int aaa = 15;
            string s2 = string.Format("{0:00000}", Convert.ToInt16(aaa));
            richTextBox1.Text += s2 + "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //顯示錢單位

            string company = "aaaa";
            double sum = 1234567;
            double total = 2345678;

            Console.WriteLine("{0}分公司營業額：{1}元\t營業率：{2:p}", company, sum.ToString("c"), sum / total);
            Console.WriteLine("總營業額：{0}元", total.ToString("c"));

            string string1 = string.Format("{0}分公司營業額：{1}元\t營業率：{2:p}", company, sum.ToString("c"), sum / total);
            string string2 = string.Format("總營業額：{0}元", total.ToString("c"));
            richTextBox1.Text += string1 + "\n";
            richTextBox1.Text += string2 + "\n";
        }

        private void button13_Click(object sender, EventArgs e)
        {
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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //左邊補空 和 右邊補空

            richTextBox1.Text += "左邊補空 和 右邊補空, 共5位數\n";
            int i = 123;
            richTextBox1.Text += "左邊補空-----" + i.ToString().PadLeft(5) + "-----\n";       //共5位數, 左邊補空
            richTextBox1.Text += "右邊補空-----" + i.ToString().PadRight(5) + "-----\n";       //共5位數, 右邊補空

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //數字前面補0或是其他符號

            string s1 = "";
            string s2 = "";
            int a = 123;
            s1 = a.ToString().PadLeft(32, '0');

            richTextBox1.Text += "s1 " + s1 + "\n";

            s2 = a.ToString().PadLeft(32, '#');

            richTextBox1.Text += "s2 " + s2 + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //格式化字符串，向長度小於30的字符串末尾添加特定字符，補足n個字符，使用String類的PadRight(int,char)方法：
            String str = "1234";
            str = str.PadRight(30, ' '); //向長度小於30的字符串末尾添加空格，補足30個字符

            richTextBox1.Text += "string.PadLeft 字串統一長度或補字元\n";
            int aa = 15;
            string ss1 = aa.ToString().PadLeft(10, '-');
            richTextBox1.Text += ss1 + "\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //用科學記號與檔案大小表示數值

            // Display some sample values.
            double value = 12.345;
            long long_size;
            for (int i = 1; i < 11; i++)
            {
                richTextBox1.Text += "數值 : " + value.ToString() + "\t";
                richTextBox1.Text += "科學記號 : " + value.ToString("E") + "\t" + "檔案大小 : " + value.ToFileSize() + "\t";

                if (value <= long.MaxValue)
                {
                    long_size = (long)value;
                    richTextBox1.Text += "檔案大小 : " + long_size.ToFileSizeApi() + "\n";
                }
                else
                {
                    richTextBox1.Text += "\n";
                }
                value *= 1000;
            }

            richTextBox1.Text += "\n";

            value = 1023;
            richTextBox1.Text += "數值 : " + value.ToString() + "\t";
            richTextBox1.Text += "科學記號 : " + value.ToString("E") + "\t" + "檔案大小 : " + value.ToFileSize() + "\t";
            long_size = (long)value;
            richTextBox1.Text += "檔案大小 : " + long_size.ToFileSizeApi() + "\n";

            value = 1024;
            richTextBox1.Text += "數值 : " + value.ToString() + "\t";
            richTextBox1.Text += "科學記號 : " + value.ToString("E") + "\t" + "檔案大小 : " + value.ToFileSize() + "\t";
            long_size = (long)value;
            richTextBox1.Text += "檔案大小 : " + long_size.ToFileSizeApi() + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //(Console)各種數據格式的輸出

            Console.WriteLine("各種數據格式的輸出：");
            // Console.WriteLine 中各種數據格式的輸出
            Console.WriteLine("{0, 8 :C}", 2);     // $2.00
            Console.WriteLine("{0, 8 :C3}", 2);    // $2.000
            Console.WriteLine("{0 :D3}", 2);       // 002
            Console.WriteLine("{0 :E}", 2);        // 2.000000E+000
            Console.WriteLine("{0 :G}", 2);        // 2
            Console.WriteLine("{0 :N}", 2500000.00);    // 2,500,00.00
            Console.WriteLine("{0 :x4}", 12);      // 000c
            Console.WriteLine("{0, 2 :x}", 12);    //  c
            Console.WriteLine("{0 :000.000}", 12.23);   // 012.230
            Console.WriteLine("{0 :r}", 15.62);    // 15.62
            Console.WriteLine("{0 :d}", System.DateTime.Now);    // 2012-3-27
            Console.WriteLine("{0 :D}", System.DateTime.Now);    // 2012年3月27日

            Console.WriteLine("{0 :t}", System.DateTime.Now);    // 11:43
            Console.WriteLine("{0 :T}", System.DateTime.Now);    // 11:43:34

            Console.WriteLine("{0 :f}", System.DateTime.Now);    // 2012年3月27日 11:43
            Console.WriteLine("{0 :F}", System.DateTime.Now);    // 2012年3月27日 11:43:34

            Console.WriteLine("{0 :g}", System.DateTime.Now);    // 2012-3-27 11:43
            Console.WriteLine("{0 :G}", System.DateTime.Now);    // 2012-3-27 11:43:34

            Console.WriteLine("{0 :M}", System.DateTime.Now);    // 3月27日
            Console.WriteLine("{0 :r}", System.DateTime.Now);// Tue, 27 Mar 2012 11:43:34 GMT
            Console.WriteLine("{0 :s}", System.DateTime.Now);    // 2012-03-27T11:43:34
            Console.WriteLine("{0 :u}", System.DateTime.Now);    // 2012-03-27 11:43:34Z
            Console.WriteLine("{0 :U}", System.DateTime.Now);    // 2012年3月27日 3:43:34
            Console.WriteLine("{0 :Y}", System.DateTime.Now);    // 2012年3月

            Console.WriteLine("{0 :dd}", System.DateTime.Now);   // 27
            Console.WriteLine("{0 :ddd}", System.DateTime.Now);  // 二
            Console.WriteLine("{0 :dddd}", System.DateTime.Now); // 星期二

            Console.WriteLine("{0 :f}", System.DateTime.Now);    // 2012年3月27日 11:46
            Console.WriteLine("{0 :ff}", System.DateTime.Now);   // 18
            Console.WriteLine("{0 :fff}", System.DateTime.Now);  // 187
            Console.WriteLine("{0 :ffff}", System.DateTime.Now); // 1875
            Console.WriteLine("{0 :fffff}", System.DateTime.Now); // 18750

            Console.WriteLine("{0 :gg}", System.DateTime.Now);   // 公元
            Console.WriteLine("{0 :ggg}", System.DateTime.Now);  // 公元
            Console.WriteLine("{0 :gggg}", System.DateTime.Now); // 公元
            Console.WriteLine("{0 :ggggg}", System.DateTime.Now);     // 公元
            Console.WriteLine("{0 :gggggg}", System.DateTime.Now);    // 公元

            Console.WriteLine("{0 :hh}", System.DateTime.Now);   // 11
            Console.WriteLine("{0 :HH}", System.DateTime.Now);   // 11

            Console.WriteLine("{0 :mm}", System.DateTime.Now);   // 50
            Console.WriteLine("{0 :MM}", System.DateTime.Now);   // 03

            Console.WriteLine("{0 :MMM}", System.DateTime.Now);  // 三月
            Console.WriteLine("{0 :MMMM}", System.DateTime.Now); // 三月

            Console.WriteLine("{0 :ss}", System.DateTime.Now);   // 43
            Console.WriteLine("{0 :tt}", System.DateTime.Now);   // 上午

            Console.WriteLine("{0 :yy}", System.DateTime.Now);   // 12
            Console.WriteLine("{0 :yyyy}", System.DateTime.Now); // 2012
            Console.WriteLine("{0 :zz}", System.DateTime.Now);   // +08
            Console.WriteLine("{0 :zzz}", System.DateTime.Now);  // +08:00
            Console.WriteLine("{0 :hh:mm:ss}", System.DateTime.Now);  // 11：43：34
            Console.WriteLine("{0 :dd/MM/yyyy}", System.DateTime.Now); // 27-03-2012

            // TODO: Implement Functionality Here
        }

        //數字大寫顯示 ST
        private void button19_Click(object sender, EventArgs e)
        {
            //數字大寫顯示
            int money = 123456;
            string result = MoneyToChinese(money.ToString());
            richTextBox1.Text += result + "\n";
        }

        public static string MoneyToChinese(string strAmount)
        {
            string functionReturnValue = null;
            bool IsNegative = false; // 是否是負數
            if (strAmount.Trim().Substring(0, 1) == "-")
            {
                // 是負數則先轉為正數
                strAmount = strAmount.Trim().Remove(0, 1);
                IsNegative = true;
            }
            string strLower = null;
            string strUpart = null;
            string strUpper = null;
            int iTemp = 0;
            // 保留兩位小數123.489→123.49　　123.4→123.4
            strAmount = Math.Round(double.Parse(strAmount), 2).ToString();
            if (strAmount.IndexOf(".") > 0)
            {
                if (strAmount.IndexOf(".") == strAmount.Length - 2)
                {
                    strAmount = strAmount + "0";
                }
            }
            else
            {
                strAmount = strAmount + ".00";
            }

            strLower = strAmount;
            iTemp = 1;
            strUpper = "";
            while (iTemp <= strLower.Length)
            {
                switch (strLower.Substring(strLower.Length - iTemp, 1))
                {
                    case ".":
                        strUpart = "圓";
                        break;
                    case "0":
                        strUpart = "零";
                        break;
                    case "1":
                        strUpart = "壹";
                        break;
                    case "2":
                        strUpart = "貳";
                        break;
                    case "3":
                        strUpart = "三";
                        break;
                    case "4":
                        strUpart = "肆";
                        break;
                    case "5":
                        strUpart = "伍";
                        break;
                    case "6":
                        strUpart = "陸";
                        break;
                    case "7":
                        strUpart = "柒";
                        break;
                    case "8":
                        strUpart = "捌";
                        break;
                    case "9":
                        strUpart = "玖";
                        break;
                }

                switch (iTemp)
                {
                    case 1:
                        strUpart = strUpart + "分";
                        break;
                    case 2:
                        strUpart = strUpart + "角";
                        break;
                    case 3:
                        strUpart = strUpart + "";
                        break;
                    case 4:
                        strUpart = strUpart + "";
                        break;
                    case 5:
                        strUpart = strUpart + "拾";
                        break;
                    case 6:
                        strUpart = strUpart + "佰";
                        break;
                    case 7:
                        strUpart = strUpart + "仟";
                        break;
                    case 8:
                        strUpart = strUpart + "萬";
                        break;
                    case 9:
                        strUpart = strUpart + "拾";
                        break;
                    case 10:
                        strUpart = strUpart + "佰";
                        break;
                    case 11:
                        strUpart = strUpart + "仟";
                        break;
                    case 12:
                        strUpart = strUpart + "億";
                        break;
                    case 13:
                        strUpart = strUpart + "拾";
                        break;
                    case 14:
                        strUpart = strUpart + "佰";
                        break;
                    case 15:
                        strUpart = strUpart + "仟";
                        break;
                    case 16:
                        strUpart = strUpart + "萬";
                        break;
                    default:
                        strUpart = strUpart + "";
                        break;
                }
                strUpper = strUpart + strUpper;
                iTemp = iTemp + 1;
            }

            strUpper = strUpper.Replace("零拾", "零");
            strUpper = strUpper.Replace("零佰", "零");
            strUpper = strUpper.Replace("零仟", "零");
            strUpper = strUpper.Replace("零零零", "零");
            strUpper = strUpper.Replace("零零", "零");
            strUpper = strUpper.Replace("零角零分", "整");
            strUpper = strUpper.Replace("零分", "整");
            strUpper = strUpper.Replace("零角", "零");
            strUpper = strUpper.Replace("零億零萬零圓", "億圓");
            strUpper = strUpper.Replace("億零萬零圓", "億圓");
            strUpper = strUpper.Replace("零億零萬", "億");
            strUpper = strUpper.Replace("零萬零圓", "萬圓");
            strUpper = strUpper.Replace("零億", "億");
            strUpper = strUpper.Replace("零萬", "萬");
            strUpper = strUpper.Replace("零圓", "圓");
            strUpper = strUpper.Replace("零零", "零");

            // 對壹圓以下的金額的處理

            if (strUpper.Substring(0, 1) == "圓")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "零")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "角")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "分")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "整")
            {
                strUpper = "零圓整";
            }

            functionReturnValue = strUpper;

            if (IsNegative == true)
            {
                return "負" + functionReturnValue;
            }
            else
            {
                return functionReturnValue;
            }
        }
        //數字大寫顯示 SP

        private void button20_Click(object sender, EventArgs e)
        {
            //貨幣單位
            double money = 1234.567;
            richTextBox1.Text += "\n";
            richTextBox1.Text += money.ToString("C") + "\n";
            richTextBox1.Text += "新台幣：" + money.ToString("C0") + "元\n"; //到整數
            richTextBox1.Text += money.ToString("C", CultureInfo.CurrentCulture) + "\n";
            richTextBox1.Text += money.ToString("C", CultureInfo.CreateSpecificCulture("da-DK")) + "\n";
            richTextBox1.Text += money.ToString("C", CultureInfo.CreateSpecificCulture("en-US")) + "\n";
            richTextBox1.Text += money.ToString("C", CultureInfo.CreateSpecificCulture("ja-JP")) + "\n";
            richTextBox1.Text += money.ToString("C", CultureInfo.CreateSpecificCulture("fr-FR")) + "\n";


            //表示錢號的方法
            int n = 12345;
            richTextBox1.Text += "新台幣 " + n.ToString("C") + " 元\n";
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //數字顯示格式     百分比%

            //double x = 1234567890;
            int x = 12345;
            richTextBox1.Text += "十進位\t" + x.ToString() + "\n";
            richTextBox1.Text += "十六進位\t" + x.ToString("X2") + "\n";
            richTextBox1.Text += "數值格式\t" + x.ToString("N0") + "\n";

            double y = 123.456;
            richTextBox1.Text += "數值格式\t" + y.ToString("N4") + "\n";

            richTextBox1.Text += "將0.87顯示為87%\n";
            float percent = 0.87f;
            richTextBox1.Text += "percent = " + percent.ToString() + "\t數字\n";
            string percent_text = percent.ToString("P0");
            richTextBox1.Text += "percent = " + percent_text + "\t百分比\n";
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //小數點下n位四捨五入

            double pi = Math.PI;
            richTextBox1.Text += "小數點下2位\t" + pi.ToString("n2") + "\n";
            richTextBox1.Text += "小數點下4位\t" + pi.ToString("n4") + "\t四捨五入\n";
            richTextBox1.Text += "小數點下5位\t" + pi.ToString("n5") + "\n";
            richTextBox1.Text += "小數點下10位\t" + pi.ToString("n10") + "\n";
            richTextBox1.Text += "小數點下15位\t" + pi.ToString("n15") + "\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //字符型轉換 轉為字符串

            int value = 12345;
            richTextBox1.Text += "a\t" + value.ToString("n") + "\n"; //生成 12,345.00
            richTextBox1.Text += "b\t" + value.ToString("C") + "\n"; //生成 ￥12,345.00
            richTextBox1.Text += "c\t" + value.ToString("e") + "\n"; //生成 1.234500e+004
            richTextBox1.Text += "d\t" + value.ToString("f4") + "\n"; //生成 12345.0000
            richTextBox1.Text += "e\t" + value.ToString("x") + "\n"; //生成 3039 (16進制)
            richTextBox1.Text += "f\t" + value.ToString("p") + "\n"; //生成 1,234,500.00%
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //數字顯示

            /*
            保留兩位小數
            ToString("0.00");

            ToString("0.00");
            */

            /*
            double dis1 = 150000000000.0 / 340.0 / 60.0 / 60.0 / 24.0;
            //label4.Text = dis.ToString("#,###,###,###.##") + " 天";

            double dis2 = 150000000000.0 / 299792458.0;
            //label5.Text = dis.ToString() + " 秒";
            //label5.Text = dis.ToString("#,###,###,###.##") + " 秒";

            //txtValue.Text = pi.ToString("F15");		//小數點以下15位
            //txtError.Text = error.ToString("E");		//科學符號
            */
        }

        private void button25_Click(object sender, EventArgs e)
        {
            int nudPoint = 3;
            double num = 123.123456789;
            //根據nudPoint.Value來格式化顯示的數值
            richTextBox1.Text += num.ToString("F" + nudPoint.ToString()) + "\n";


            //在 C# 中使用 String.Format() 方法將字串轉換為十六進位制
            string decString = "0123456789";
            var hexString = string.Join("", decString.Select(c => String.Format("{0:X2}", Convert.ToInt32(c))));
            richTextBox1.Text += "hexString :" + hexString + "\n";
        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //CultureInfo

            //顯示百分比 錢號的方法
            //要using System.Globalization; //for CultureInfo
            int a = 2;
            int b = 3;
            richTextBox1.Text += "顯示一位小數的百分比 :\t\t" + ((double)a / (double)b).ToString("P1", CultureInfo.InvariantCulture) + "\n";
            richTextBox1.Text += "顯示兩位小數的百分比 :\t\t" + ((double)a / (double)b).ToString("P", CultureInfo.InvariantCulture) + "\n";
            richTextBox1.Text += "顯示十位小數的百分比 :\t\t" + ((double)a / (double)b).ToString("P10", CultureInfo.InvariantCulture) + "\n";

        }

        void show_numbers()
        {
            int value1 = 12345;
            double value2 = 123.456;
            double value3 = 1234.5678;
            tb_number0.Text = value1.ToString("D");
            tb_number1.Text = value1.ToString("D8");
            tb_number2.Text = value1.ToString("X");
            tb_number3.Text = value1.ToString("X8");

            tb_number4.Text = value2.ToString("F4");
            //tb_number4.Text = value2.ToString("F0");  //四捨五入到整數
            //tb_number4.Text = value2.ToString("F1");  //四捨五入到小數點下一位
            tb_number5.Text = value3.ToString("#0.00");         //格式化，小數點後留2位，四捨五入
            tb_number6.Text = value3.ToString("#00000.000");   //格式化，小數點前5位，小數點後留3位四捨五入

            lb_number0.Text = "十進位顯示";
            lb_number1.Text = "十進位顯示(8位)";
            lb_number2.Text = "十六進位顯示";
            lb_number3.Text = "十六進位顯示(8位)";
            lb_number4.Text = "小數點後4位";
            lb_number5.Text = "小數點後2位";
            lb_number6.Text = "小數點前5位後3位";
            lb_number0b.Text = value1.ToString();
            lb_number1b.Text = value1.ToString();
            lb_number2b.Text = value1.ToString();
            lb_number3b.Text = value1.ToString();
            lb_number4b.Text = value2.ToString();
            lb_number5b.Text = value3.ToString();
            lb_number6b.Text = value3.ToString();
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/



