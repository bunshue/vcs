using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_03_Syntax
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //foreach(陣列元素資料型別 變數名in 陣列變數名)
            int[] arrayA = new int[5] { 10, 1, 2, 3, 4 };
            foreach (int a in arrayA)
            {
                MessageBox.Show("取得數字：" + a.ToString());
            }

            string[] studentName = new string[4] { "Alice", "Bob", "Ives", "John" };
            foreach (string name in studentName)
            {
                MessageBox.Show("取得字串：" + name);
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            string[] name = { "John", "Mary", "Emily", "Peppa", "Candy", "Eric" };
            int[] score = { 85, 90, 78, 94, 72, 88 };

            richTextBox1.Text += "所有名字\n";
            foreach (string nn in name)
            {
                richTextBox1.Text += nn + "\n";
            }
            richTextBox1.Text += "所有成績\n";
            foreach (int ss in score)
            {
                richTextBox1.Text += ss.ToString() + "\n";
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            string s1 = "lion-mouse";
            double d1 = 123.456;
            int i1 = 123;
            bool b1 = false;
            richTextBox1.Text += "s1的資料型別是：" + s1.GetType().ToString() + "\n";
            richTextBox1.Text += "d1的資料型別是：" + d1.GetType().ToString() + "\n";
            richTextBox1.Text += "i1的資料型別是：" + i1.GetType().ToString() + "\n";
            richTextBox1.Text += "b1的資料型別是：" + b1.GetType().ToString() + "\n";
            richTextBox1.Text += "日期的資料型別是：" + DateTime.Now.GetType().ToString() + "\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            int[] A = new int[5];
            int[] B = new int[] { 1, 2, 3, 4, 5 };
            int[] C = { 1, 3, 5, 7, 9 };
            int[,] D = new int[3, 3];
            int[,] E = new int[,] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
            int[,] F = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
            int[, ,] G = new int[3, 4, 5];

            //一維陣列
            int[] myArr = new int[4];	//宣告
            myArr[0] = 1;
            myArr[1] = 2;
            myArr[2] = 3;
            myArr[3] = 4;
            myArr = new int[] { 1, 2, 3, 4 };	//改值

            //三維陣列的寫法：
            int[, ,] myArray = new int[2, 3, 4];

            //鋸齒陣列	//不規則陣列
            char[][] ch = new char[][]
            {
                new char[] {'a','b','c'},
                new char[] {'c','d','e','f','g','h'},
                new char[] {'w','x','y','z'}
            };

            //Color陣列
            System.Drawing.Color[] color1 = new Color[5];
            color1[0] = Color.Brown;
            color1[1] = Color.Azure;
            color1[2] = Color.Chartreuse;
            color1[3] = Color.Cyan;
            color1[4] = Color.Gainsboro;

            //Point陣列
            Point a = new Point(10, 20);    //宣告一個Point變數
            a.X = 30;   //改值
            a.Y = 40;
            a = new Point(35, 45);          //同時更改XY兩個整數屬性的值


            int[] index = new int[4] { 2, 4, 6, 8 };
            int[] a1 = new int[4];
            a1[0] = 5;
            a1[1] = 4;
            a1[2] = 6;
            a1[3] = 2;
            Array.Sort(a1);
            richTextBox1.Text += "最大值為：" + a1[3].ToString() + "\n";




        }

        private void button6_Click(object sender, EventArgs e)
        {
            int value1 = 65535;
            int value2 = 0x12345;
            MessageBox.Show("十進位：" + value1 + "  十六進位： 0x" + Convert.ToString(value1, 16));
            MessageBox.Show("十六進位： 0x" + Convert.ToString(value2, 16) + "  十進位：" + value2);

        }

        private void button7_Click(object sender, EventArgs e)
        {
            MessageBox.Show("1您是合法的使用者！！");
            MessageBox.Show("2訊息內容_回覆按鈕OK", "標題", MessageBoxButtons.OK);
            MessageBox.Show("3訊息內容_回覆按鈕OKCancel", "標題", MessageBoxButtons.OKCancel);
            MessageBox.Show("4訊息內容_回覆按鈕AbortRetryIgnore", "標題", MessageBoxButtons.AbortRetryIgnore);
            MessageBox.Show("5訊息內容_回覆按鈕YesNoCancel", "標題", MessageBoxButtons.YesNoCancel);
            MessageBox.Show("6訊息內容_回覆按鈕YesNo", "標題", MessageBoxButtons.YesNo);
            MessageBox.Show("7訊息內容_回覆按鈕RetryCancel", "標題", MessageBoxButtons.RetryCancel);

            MessageBox.Show(" 8Question圖示", "圖示設定", MessageBoxButtons.OK, MessageBoxIcon.Question);
            MessageBox.Show(" 9Question圖示", "圖示設定", MessageBoxButtons.OK, MessageBoxIcon.Information);
            MessageBox.Show("10Question圖示", "圖示設定", MessageBoxButtons.OK, MessageBoxIcon.Error);
            MessageBox.Show("11Question圖示", "圖示設定", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            MessageBox.Show("12Question圖示", "圖示設定", MessageBoxButtons.OK, MessageBoxIcon.Stop);
            MessageBox.Show("13Question圖示", "圖示設定", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);


        }

        private void button8_Click(object sender, EventArgs e)
        {
            //確認字串是否為空
            string string_a = "";
            string string_b = "this is a string";

            //if not default it to "SSSS"
            if (string.IsNullOrEmpty(string_a) || string_a == null)
            {
                richTextBox1.Text += "字串" + string_a ;
                string_a = "SSSS";
                richTextBox1.Text += "是一個空字串，改成: " + string_a + "\n";
            }
            else
                richTextBox1.Text += "不是一個空字串，內容: " + string_a + "\n";

            //if not default it to "SSSS"
            if (string.IsNullOrEmpty(string_b) || string_a == null)
            {
                richTextBox1.Text += "字串" + string_b;
                string_b = "SSSS";
                richTextBox1.Text += "是一個空字串，改成: " + string_b + "\n";
            }
            else
                richTextBox1.Text += "不是一個空字串，內容: " + string_b + "\n";
        
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //不用宣告長度的陣列(Array)
            // 宣告myIntLists 為List
            // 以下List 裡為int 型態
            List<int> myIntLists = new List<int>();

            // 宣告myStringLists 為List
            // 以下List 裡為string 型態
            List<string> myStringLists = new List<string>();

            // 在List 裡新增int 整數
            myIntLists.Add(12);
            myIntLists.Add(34);
            myIntLists.Add(56);

            // 在List 裡新增string 字串
            myStringLists.Add("lion");
            myStringLists.Add("mouse");
            myStringLists.Add("cat");
            myStringLists.Add("dog");

            richTextBox1.Text += "\n"; 
            richTextBox1.Text += "myIntLists has" + myIntLists.Count.ToString() + " elements\n";
            richTextBox1.Text += "myStringLists has" + myStringLists.Count.ToString() + " elements\n";

            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (int ii in myIntLists)
            {
                richTextBox1.Text += "\t" + ii.ToString();
            }
            richTextBox1.Text += "\n"; 

            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in myStringLists)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n"; 

            richTextBox1.Text += "經過排序：\n"; 
            myStringLists.Sort();
            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in myStringLists)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n";


            richTextBox1.Text += "增加內容：\n";
            myStringLists.Insert(2, "elephant");
            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in myStringLists)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "刪除內容：\n";
            myStringLists.Remove("cat");
            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in myStringLists)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n"; 

        }

        private void button10_Click(object sender, EventArgs e)
        {
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
            richTextBox1.Text += "get string : " + new_string + "\n";

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //字串轉換為Byte型態的陣列
            String original_string = "lion-mouse.";
            Byte[] byte_array = Encoding.ASCII.GetBytes(original_string);
            foreach (char c in byte_array)
            {
                richTextBox1.Text += c.ToString() + "\n";
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        struct circle
        {
            public float cRadius;
            public string cColor;
        }
        struct wheel
        {
            public circle circle1;
            public string usage;
        };
        
        private void button12_Click(object sender, EventArgs e)
        {
            wheel wheel1;
            wheel1.circle1.cRadius = 50;
            wheel1.circle1.cColor = "黑色";
            wheel1.usage = "汽車";
            richTextBox1.Text += "輪胎半徑：" + wheel1.circle1.cRadius + "\n";
            richTextBox1.Text += "輪胎顏色：" + wheel1.circle1.cColor + "\n";
            richTextBox1.Text += "輪胎用途：" + wheel1.usage + "\n";

        }

        private class myList
        {
            public string ID { get; set; }
            public string Name { get; set; }
            public string Level { get; set; }
        }

        List<myList> myLists = new List<myList>();

        private void button13_Click(object sender, EventArgs e)
        {
            myLists.Add(new myList { ID = "A001", Name = "David", Level = "A" });
            myLists.Add(new myList { ID = "A002", Name = "John" });
            myLists.Add(new myList { ID = "A003", Name = "Tom", Level = "A" });

        }

        private void button14_Click(object sender, EventArgs e)
        {
            foreach (var showlist in myLists)
            {
                richTextBox1.Text += "ID : " + showlist.ID + "\tName : " + showlist.Name + "\tLevel : " + showlist.Level + "\n";
                //Console.WriteLine(showlist.ID + "->" + showlist.Name + "->" + showlist.Level); //column[0] & column[1]
            }
        }

        private void button31_Click(object sender, EventArgs e)
        {
            //使用正則表達式判斷字串是否符合手機號碼格式。
            System.Text.RegularExpressions.Regex rex = new System.Text.RegularExpressions.Regex("^[0-9]{4}-[0-9]{6}$");
            if (rex.IsMatch(txtInput.Text))
            {
                MessageBox.Show("符合");
            }
            else
            {
                MessageBox.Show("不符合");
            }

        }

        private void button34_Click(object sender, EventArgs e)
        {
            //使用正則表達式判斷字串是否符合身分證格式。
            System.Text.RegularExpressions.Regex rex = new System.Text.RegularExpressions.Regex("^[A-Z]{1}[0-9]{9}$");
            if (rex.IsMatch(txtInput.Text))
            {
                MessageBox.Show("符合");
            }
            else
            {
                MessageBox.Show("不符合");
            }

        }

        private void button24_Click(object sender, EventArgs e)
        {
            //搜尋指定字串的位置
            //使用System.Text.RegularExpressions來搜尋指定字串
            //準備要搜尋的來源字串
            string strTxt = "彩袖殷勤捧玉鍾，當筵拚卻醉顏紅。舞低楊柳樓心月，歌盡桃花扇底風。從別後，憶相逢，幾回魂夢與君同。今宵賸把銀釭照，猶恐相逢是夢中。";
            //指定字串
            string strKey = "，";
            System.Text.RegularExpressions.MatchCollection matches = System.Text.RegularExpressions.Regex.Matches(strTxt, strKey);
            foreach (System.Text.RegularExpressions.Match m in matches)
            {
                richTextBox1.Text += "找到在 " + m.Index.ToString() + "\n";

            }

        }

        private void button26_Click(object sender, EventArgs e)
        {
            string str = "this is a lion-mouse";
            richTextBox1.Text += "old string : " + str + "\n";

            byte[] byteArray = System.Text.Encoding.Default.GetBytes(str);
            richTextBox1.Text += "len = " + byteArray.Length.ToString() + ", to byte array\n";
            int i;
            for (i = 0; i < byteArray.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + (char)byteArray[i] + "\n";  //多了(char)變成%c
            }

        }

        private void button27_Click(object sender, EventArgs e)
        {
            byte[] byteArray = new byte[5] { 0x41, 0x42, 0x43, 0x44, 0x45 };

            string str = System.Text.Encoding.Default.GetString(byteArray);

            richTextBox1.Text += "get string : " + str + "\n";

        }

        private void button19_Click(object sender, EventArgs e)
        {
            byte[] byteData = new byte[5] { 0x01, 0x02, 0x03, 0x04, 0x05 };
            char[] cChar = Encoding.ASCII.GetChars(byteData);

        }

        private void button28_Click(object sender, EventArgs e)
        {
            char[] cChar = new char[5] { 'a', 'b', 'c', 'd', 'e' };
            byte[] byteData = Encoding.Default.GetBytes(cChar);

        }

        private void button25_Click(object sender, EventArgs e)
        {
            int dint = 170;
            string strHex = String.Format("{0:X2}", dint);    //X2的2代表若缺0會自動補0，所以沒有2也沒關係
            richTextBox1.Text += "result : " + strHex + "\n";

        }

        private void button30_Click(object sender, EventArgs e)
        {
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

        }

        private void button33_Click(object sender, EventArgs e)
        {
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

        }


    }
}
