#define TYPE1
//#define TYPE2

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Globalization; //for CultureInfo
using System.Threading;
using System.Diagnostics;   //for StackTrace
using System.Reflection;    //for MethodInfo

namespace vcs_test_all_03_Syntax
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
            textBox_hex.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單

            //For 驗證身份證字號
            txtInput.MaxLength = 10;//設定字元數最大值
            //txtInput.Focus();//程式啟動就把焦點移到txtInput
            this.AcceptButton = button36;//按下enter就觸發button click事件

            //顯示特殊符號
            lb_symbols_2.Text = "\u0460♪♫π∑∂€£∫⊗≥≅∡∞√∜⇒∊∫ℵ↝ℙ‡ЖЊæ÷";
            tb_symbols_2.Text = "\u0460♪♫π∑∂€£∫⊗≥≅∡∞√∜⇒∊∫ℵ↝ℙ‡ЖЊæ÷";

            string txt = "";
            for (int i = 0x460; i < 0x470; i++)
            {
                txt += (char)i;
            }
            lb_symbols_3.Text = txt;



            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 190;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button5.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            button6.Location = new Point(x_st + dx * 6, y_st + dy * 0);

            button7.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button8.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button11.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 5, y_st + dy * 1);
            button13.Location = new Point(x_st + dx * 6, y_st + dy * 1);

            button14.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button16.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button17.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button18.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button19.Location = new Point(x_st + dx * 5, y_st + dy * 2);
            button20.Location = new Point(x_st + dx * 6, y_st + dy * 2);

            button21.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button25.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            button26.Location = new Point(x_st + dx * 5, y_st + dy * 3);
            button27.Location = new Point(x_st + dx * 6, y_st + dy * 3);

            button28.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button29.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button30.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button32.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            button33.Location = new Point(x_st + dx * 5, y_st + dy * 4);
            button34.Location = new Point(x_st + dx * 6, y_st + dy * 4);

            button35.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button37.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button39.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            button40.Location = new Point(x_st + dx * 5, y_st + dy * 5);
            button41.Location = new Point(x_st + dx * 6, y_st + dy * 5);

            label11.Location = new Point(x_st + dx * 7, y_st + dy * 5 + 5);
            textBox_hex.Location = new Point(x_st + dx * 7 + 32, y_st + dy * 5);
            lb_dec.Location = new Point(x_st + dx * 7 + 148, y_st + dy * 5 + 5);
            lb_dec.Text = "";

            groupBox2.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 8, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 9, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 9, y_st + dy * 3);
            groupBox5.Location = new Point(x_st + dx * 0, y_st + dy * 12 + 20);

            label1.Location = new Point(x_st + dx * 0 / 2, y_st + dy * 7);
            label2.Location = new Point(x_st + dx * 1 / 2, y_st + dy * 7);
            label3.Location = new Point(x_st + dx * 2 / 2, y_st + dy * 7);
            label4.Location = new Point(x_st + dx * 3 / 2, y_st + dy * 7);
            label5.Location = new Point(x_st + dx * 4 / 2, y_st + dy * 7);

            label6.Location = new Point(x_st + dx * 0 / 2, y_st + dy * 8);
            label7.Location = new Point(x_st + dx * 1 / 2, y_st + dy * 8);
            label8.Location = new Point(x_st + dx * 2 / 2, y_st + dy * 8);
            label9.Location = new Point(x_st + dx * 3 / 2, y_st + dy * 8);
            label10.Location = new Point(x_st + dx * 4 / 2, y_st + dy * 8);

            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 7);
            richTextBox1.Size = new Size(750, 700);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //用法:  string.Format( “{編號0} {編號1}…{編號N}”, 變數0, 變數1, … 變數N );

            richTextBox1.Text += "\n類似sprintf的寫法\n";
            int number = 123;
            string name = "david";
            string information = string.Empty;
            information = string.Format("ID = {0}, Name = {1}", number.ToString(), name);
            richTextBox1.Text += "information1 : " + information + "\n";
            richTextBox1.Text += "information2 : " + string.Format("ID = {0}, Name = {1}", number.ToString(), name) + "\n";

            string msg1 = "Name : \"{0}\",\tKind \"{1}\".\n";
            string str = string.Empty;

            str = string.Format(msg1, "lion", "mouse");
            richTextBox1.Text += "str1 = " + str + "\n";

            string msg2 = "Using the {0} - \"{1}\" culture:";

            //各國語言(語系)代碼表(zh-tw, zh-cn,en-us...) json 格式 [繁中/簡中/英文格式] 
            CultureInfo ci;

            ci = new CultureInfo("en-US");
            str = string.Format(msg2, ci.DisplayName, ci.Name);
            richTextBox1.Text += "str = " + str + "\n";

            ci = new CultureInfo("zh-TW");
            str = string.Format(msg2, ci.DisplayName, ci.Name);
            richTextBox1.Text += "str = " + str + "\n";

            ci = new CultureInfo("zh-CN");
            str = string.Format(msg2, ci.DisplayName, ci.Name);
            richTextBox1.Text += "str = " + str + "\n";

            ci = new CultureInfo("zh-HK");
            str = string.Format(msg2, ci.DisplayName, ci.Name);
            richTextBox1.Text += "str = " + str + "\n";

            ci = new CultureInfo("zh-SG");
            str = string.Format(msg2, ci.DisplayName, ci.Name);
            richTextBox1.Text += "str = " + str + "\n";

            ci = new CultureInfo("zh-CHS");
            str = string.Format(msg2, ci.DisplayName, ci.Name);
            richTextBox1.Text += "str = " + str + "\n";

            ci = new CultureInfo("zh-CHT");
            str = string.Format(msg2, ci.DisplayName, ci.Name);
            richTextBox1.Text += "str = " + str + "\n";

            ci = new CultureInfo("ja-JP");
            str = string.Format(msg2, ci.DisplayName, ci.Name);
            richTextBox1.Text += "str = " + str + "\n";

            for (int i = 0; i < 10; i++)
            {
                string message = string.Format("{0} {1: yyyy/MM/dd HH:mm:ss.fff }", "現在時間 : ", DateTime.Now);
                richTextBox1.Text += message + "\n";
                Thread.Sleep(1234); //delay 1.234 秒
            }
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

        string[] LunarHolDayName = {
                  "小寒", "大寒", "立春", "雨水",
                  "驚蟄", "春分", "清明", "谷雨",
                  "立夏", "小滿", "芒種", "夏至",
                  "小暑", "大暑", "立秋", "處暑",
                  "白露", "秋分", "寒露", "霜降",
                  "立冬", "小雪", "大雪", "冬至"};

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
            richTextBox1.Text += "\n最大值為：" + a1[3].ToString() + "\n";

            foreach (string str in LunarHolDayName)
            {
                richTextBox1.Text += str + " ";
            }
            richTextBox1.Text += "\n";



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
                richTextBox1.Text += "字串" + string_a;
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
            //顯示控件上的文字
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "此Method的Name是\t" + GetMethodName() + "\n";
        }

        // Return the name of the method that called this one.
        private string GetMethodName()
        {
            return new StackTrace(1).GetFrame(0).GetMethod().Name;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "搜尋所有控件 符合種類 符合條件 的 做處理\n";
            foreach (Control ctl in Controls)
            {
                richTextBox1.Text += "找到控件\t" + ctl.Name;

                if ((ctl is Button) && (ctl == button2))
                {
                    richTextBox1.Text += "\t是button2, 清除其文字\n";
                    ctl.Text = "";
                }
                else
                    richTextBox1.Text += "\n";
            }

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
            int a, n, r;

            a = 12345;

            string[] m = {"0", "1", "2", "3",
                           "4", "5", "6", "7",
                           "8", "9", "A", "B",
                           "C", "D", "E", "F"};
            string s = "";

            richTextBox1.Text = "10進位數字\t" + a.ToString() + "\n";

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
        }

        //傳值呼叫 vs 傳址呼叫
        private void button34_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "傳值呼叫 vs 傳址呼叫\n";

            int a = 10;
            int b = 5;

            richTextBox1.Text += "原本 a = " + a.ToString() + ", b = " + b.ToString() + "\n";
            swap(a, b);
            richTextBox1.Text += "傳值呼叫後, a = " + a.ToString() + ", b = " + b.ToString() + "\n";

            a = 10;
            b = 5;
            richTextBox1.Text += "原本 a = " + a.ToString() + ", b = " + b.ToString() + "\n";
            swap(ref a, ref b);
            richTextBox1.Text += "傳址呼叫後, a = " + a.ToString() + ", b = " + b.ToString() + "\n";
        }

        void swap(int a, int b)
        {
            int t = a;
            a = b;
            b = t;
        }

        void swap(ref int a, ref int b)
        {
            int t = a;
            a = b;
            b = t;
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
            Dictionary<string, long> population_dict = new Dictionary<string, long>();

            // Population data from https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population.
            population_dict.Add("AK", 731545);
            population_dict.Add("AL", 4903185);
            population_dict.Add("AR", 3017825);
            population_dict.Add("AS", 55641);
            population_dict.Add("AZ", 7278717);
            population_dict.Add("CA", 39512223);
            population_dict.Add("CO", 5758736);
            population_dict.Add("CT", 3565287);
            population_dict.Add("DC", 705749);
            population_dict.Add("DE", 973764);
            population_dict.Add("FL", 21477737);
            population_dict.Add("GA", 10617423);
            population_dict.Add("GU", 165718);
            population_dict.Add("HI", 1415872);
            population_dict.Add("IA", 3155070);
            population_dict.Add("ID", 1787065);
            population_dict.Add("IL", 12671821);
            population_dict.Add("IN", 6732219);
            population_dict.Add("KS", 2913314);
            population_dict.Add("KY", 4467673);
            population_dict.Add("LA", 4648794);
            population_dict.Add("MA", 6949503);
            population_dict.Add("MD", 6045680);
            population_dict.Add("ME", 1344212);
            population_dict.Add("MI", 9986857);
            population_dict.Add("MN", 5639632);
            population_dict.Add("MO", 6137428);
            population_dict.Add("MP", 55194);
            population_dict.Add("MS", 2976149);
            population_dict.Add("MT", 1068778);
            population_dict.Add("NC", 10488084);
            population_dict.Add("ND", 762062);
            population_dict.Add("NE", 1934408);
            population_dict.Add("NH", 1359711);
            population_dict.Add("NJ", 8882190);
            population_dict.Add("NM", 2096829);
            population_dict.Add("NV", 3080156);
            population_dict.Add("NY", 19453561);
            population_dict.Add("OH", 11689100);
            population_dict.Add("OK", 3956971);
            population_dict.Add("OR", 4217737);
            population_dict.Add("PA", 12801989);
            population_dict.Add("PR", 3193694);
            population_dict.Add("RI", 1059361);
            population_dict.Add("SC", 5148714);
            population_dict.Add("SD", 884659);
            population_dict.Add("TN", 6833174);
            population_dict.Add("TX", 28995881);
            population_dict.Add("UT", 3205958);
            population_dict.Add("VA", 8535519);
            population_dict.Add("VI", 104914);
            population_dict.Add("VT", 623989);
            population_dict.Add("WA", 7614893);
            population_dict.Add("WI", 5822434);
            population_dict.Add("WV", 1792147);
            population_dict.Add("WY", 578759);

            // Get the state population.
            long all_pop = 0;
            foreach (int value in population_dict.Values)
            {
                all_pop += value;
            }
            population_dict.Add("ALL STATES", all_pop);

            richTextBox1.Text += "顯示此Dictionary的資料\n";
            richTextBox1.Text += "共有 " + population_dict.Count.ToString() + " 筆資料\n";
            foreach (string n in population_dict.Keys)
            {
                long p;
                richTextBox1.Text += "找到 州 " + n + "\t";
                if (population_dict.ContainsKey(n))
                    p = population_dict[n];
                else
                    p = 0;
                richTextBox1.Text += "人口 : " + p.ToString() + "\n";
            }

            string state_name;
            long population;

            state_name = "NY";
            if (population_dict.ContainsKey(state_name))
                population = population_dict[state_name];
            else
                population = 0;
            richTextBox1.Text += "州 : " + state_name + "\t人口 : " + population.ToString() + "\n";

            state_name = "CA";
            if (population_dict.ContainsKey(state_name))
                population = population_dict[state_name];
            else
                population = 0;
            richTextBox1.Text += "州 : " + state_name + "\t人口 : " + population.ToString() + "\n";

            state_name = "ALL STATES";
            if (population_dict.ContainsKey(state_name))
                population = population_dict[state_name];
            else
                population = 0;
            richTextBox1.Text += "全國 :\t人口 : " + population.ToString() + "\n";
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

        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法1\n";
            //Dictionary的用法
            Dictionary<string, string> AnimalData = new Dictionary<string, string>() {
            { "mouse", "Mickey" },
            { "bull", "Benny" },
            { "tiger", "Eric" },
            { "rabbit", "Cony" }
            };
            string animal_type;
            string animal_name;

            animal_type = "mouse";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "bull";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "tiger";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "rabbit";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "dragon";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";


        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "測試Dictionary與Class語法\n";


            // Make a dictionary.
            DictionaryWithDefault<string, string> dict = new DictionaryWithDefault<string, string>("<Missing>");


            // Add some items to the dictionary.
            dict["Ann"] = "Archer";
            dict["Chuck"] = "Cider";
            dict["Dora"] = "Deevers";

            // Display some values.
            richTextBox1.Text += "Ann" + "\t" + dict["Ann"] + "\n";
            richTextBox1.Text += "Ben" + "\t" + dict["Ben"] + "\n";
            richTextBox1.Text += "Chuck" + "\t" + dict["Chuck"] + "\n";
            richTextBox1.Text += "Dora" + "\t" + dict["Dora"] + "\n";
            richTextBox1.Text += "Ed" + "\t" + dict["Ed"] + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            for (int i = 1; i <= 10; i++)
            {
                this.Controls["label" + i.ToString()].Text = "這是label" + i.ToString();

            }

        }

        private void btn_check1_Click(object sender, EventArgs e)
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

        private void btn_check2_Click(object sender, EventArgs e)
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

        private void button27_Click(object sender, EventArgs e)
        {

        }

        bool check_textbox_hexadecimal(KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十六進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            

            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                return false;
            }
            else if ((e.KeyChar >= (Char)'A') && (e.KeyChar <= (Char)'F'))
            {
                return false;
            }
            else if ((e.KeyChar >= (Char)'a') && (e.KeyChar <= (Char)'f'))
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        private void textBox_hex_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十六進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || ((e.KeyChar >= 'A') && (e.KeyChar <= 'F')) || ((e.KeyChar >= 'a') && (e.KeyChar <= 'f')) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }

            e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                button35_Click(sender, e);
            }
        }

        private void textBox_hex_TextChanged(object sender, EventArgs e)
        {
            int value = 0;

            if (textBox_hex.Text.Length == 0)
            {
                value = 0;
                lb_dec.Text = value.ToString();
                return;
            }

            value = Convert.ToInt32(textBox_hex.Text, 16);
            lb_dec.Text = value.ToString();

        }

        private void button35_Click(object sender, EventArgs e)
        {
        }

        private void button36_Click(object sender, EventArgs e)
        {
        }

        private void btn_Click(object sender, EventArgs e)
        {
            if (sender.Equals(btn1))
            {
                richTextBox1.Text += "你按了 1\n";
            }
            else if (sender.Equals(btn2))
            {
                richTextBox1.Text += "你按了 2\n";
            }
            else if (sender.Equals(btn3))
            {
                richTextBox1.Text += "你按了 3\n";
            }
            else if (sender.Equals(btn4))
            {
                richTextBox1.Text += "你按了 4\n";
            }
            else if (sender.Equals(btn5))
            {
                richTextBox1.Text += "你按了 5\n";
            }

        }

        private void btn_check3_Click(object sender, EventArgs e)
        {
            if (txtInput.Text.Trim().Length == 10)//長度達十個字才驗證
            {
                if (isIdentificationId(txtInput.Text))//驗證身份證字號,正確回傳true
                {
                    txtInput.Text = txtInput.Text.ToUpper();//英文自動轉成大寫
                    MessageBox.Show(txtInput.Text + "是正確的身份證字號", "", MessageBoxButtons.OK, MessageBoxIcon.None);
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


        #region checkID
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
        #endregion

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // The dictionary of digit names.
        private Dictionary<int, string> Numbers = new Dictionary<int, string>()
        {
            {0, "Zero"},
            {1, "One"},
            {2, "Two"},
            {3, "Three"},
            {4, "Four"},
            {5, "Five"},
            {6, "Six"},
            {7, "Seven"},
            {8, "Eight"},
            {9, "Nine"}
        };

        private void button20_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法2\n";
            // Display values from the dictionary.
            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += i.ToString() + '\t' + Numbers[i] + "\n";
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //三元運算子
            richTextBox1.Text += (DateTime.Now.Hour < 12) ? "Good morning\n" : "Good afternoon\n";
        }

        private void button21_Click(object sender, EventArgs e)
        {
#if TYPE1
            richTextBox1.Text += "你使用了 #define TYPE1\n";
#elif TYPE2
            richTextBox1.Text += "你使用了 #define TYPE2\n";
#else
            richTextBox1.Text += "你沒有使用 #define\n";
#endif

#if ZZ01
            //在 方案總管/屬性/建置條件式編譯的符號/定義DEBUG常數/寫入ZZ01
            richTextBox1.Text += "你使用了 #define ZZ01\n";
#endif

        }

        // The enumerated type.
        private enum MealType
        {
            Breakfast,
            Brunch,
            Lunch,
            Luncheon = Lunch,
            Tiffin = Lunch,
            Tea,
            Nuncheon = Tea,
            Dinner,
            Supper
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //把ENUM的字串印出來
            // Convert values to and from strings.
            foreach (string value in Enum.GetNames(typeof(MealType)))
            {
                // Get the enumeration's value.
                MealType meal = (MealType)Enum.Parse(typeof(MealType), value);

                // Display the values.
                richTextBox1.Text += ((int)meal).ToString() + "\t" + value + "\n";
            }
        }

        // Invoke the method.
        private void bt_call_by_name_Click(object sender, EventArgs e)
        {
            try
            {
                Type this_type = this.GetType();
                MethodInfo method_info = this_type.GetMethod(textBox1.Text);
                method_info.Invoke(this, null);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "無法執行" + textBox1.Text + "\t原因\t" + ex.Message + "\n";
            }
        }

        // The public methods to invoke.
        public void Function1()
        {
            richTextBox1.Text += "執行了 Function1";
        }
        public void Function2()
        {
            richTextBox1.Text += "執行了 Function2";
        }

        #region 使用相同的函數用Tag區分
        // Use the selected color for the form's background.
        private void button_color(object sender, EventArgs e)
        {
            // Get the sender as a button.
            Button btn = sender as Button;

            // Convert its Tag value into a color.
            this.BackColor = Color.FromName(btn.Tag.ToString());
        }
        #endregion

        private void button23_Click(object sender, EventArgs e)
        {
            int a = 3;
            int b = 5;
            int c = 6;
            float avg;
            int prod;
            GetAverageProduct(a, b, c, out avg, out prod);
            richTextBox1.Text += "average = \t" + avg.ToString() + "\n";
            richTextBox1.Text += "product = \t" + prod.ToString() + "\n";
        }

        private void GetAverageProduct(int a, int b, int c, out float average, out int product)
        {
            average = (a + b + c) / (float)3;
            product = a * b * c;
        }


        // Perform the calculation.
        private void btnCalculate_Click(object sender, EventArgs e)
        {
            // Clear the result (in case the calculation fails).
            txtResult.Clear();

            try
            {
                // Perform the operations that might fail.
                int x = int.Parse(txtX.Text);
                int y = int.Parse(txtY.Text);
                float result = x / y;
                txtResult.Text = result.ToString();
            }
            catch (FormatException)
            {
                // A formatting error occurred.
                // Report the error to the user.
                richTextBox2.Text += "數值錯誤\n";
            }
            catch (Exception ex)
            {
                // Some other error occurred.
                // Report the error to the user.
                richTextBox2.Text += "計算錯誤\t原因 : " + ex + "\n";
                richTextBox2.Text += "計算錯誤\t原因 : " + ex.GetType().Name + "\n";
            }
            finally
            {
                richTextBox2.Text += "計算結束\n";
            }
        }


        //函式多載(function overloading) ST

        int add(int a, int b) { return a + b; }
        double add(double a, double b) { return a + b; }

        int add(int[] a)
        {
            int sum = 0;

            for (int i = 0; i < a.Length; i++)
                sum += a[i];

            return sum;
        }

        double add(double[] a)
        {
            double sum = 0.0;

            for (int i = 0; i < a.Length; i++)
                sum += a[i];

            return sum;
        }

        private void button32_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = "函式多載(function overloading)\n";

            int int_a = 15;
            int int_b = 23;
            int int_sum = add(int_a, int_b);
            richTextBox1.Text += "int_sum = " + int_sum.ToString() + "\n";

            double double_a = 15.123;
            double double_b = 23.456;
            double double_sum = add(double_a, double_b);
            richTextBox1.Text += "double_sum = " + double_sum.ToString() + "\n";

            int[] intArray = { 1, 2, 3, 4, 5 };
            int intArray_sum = add(intArray);
            richTextBox1.Text += "intArray_sum = " + intArray_sum.ToString() + "\n";

            double[] doubleArray = { 10.15, 20.27, 30.31, 40.44, 50.57 };
            double doubleArray_sum = add(doubleArray);
            richTextBox1.Text += "doubleArray_sum = " + doubleArray_sum.ToString() + "\n";
        }
        //函式多載(function overloading) SP

        private void button37_Click(object sender, EventArgs e)
        {

        }

        private void button38_Click(object sender, EventArgs e)
        {

        }

        private void button39_Click(object sender, EventArgs e)
        {

        }

        private void button40_Click(object sender, EventArgs e)
        {

        }

        private void button41_Click(object sender, EventArgs e)
        {
            //轉換為十進位
            if (textBox_hex.Text.Length <= 0)
            {
                richTextBox1.Text += "未輸入數字";
            }
            else
            {
                string input = textBox_hex.Text; ;
                double output = 0;
                byte value = 0;
                for (int i = 0; i < input.Length; i++)
                {
                    if ((input[i] >= (Char)48 && input[i] <= (Char)57))
                    {
                        value = (byte)(input[i] - 48);

                    }
                    else if ((input[i] >= 'A') && (input[i] <= 'F'))
                    {
                        value = (byte)(input[i] - 'A' + 10);
                    }
                    else if ((input[i] >= 'a') && (input[i] <= 'f'))
                    {
                        value = (byte)(input[i] - 'a' + 10);
                    }
                    output = output * 16 + value;
                    //MessageBox.Show("data : " + input[i] + " value : " + value);
                }
                richTextBox1.Text += "結果：" + output.ToString() + "\n";
            }

        }


    }
}


