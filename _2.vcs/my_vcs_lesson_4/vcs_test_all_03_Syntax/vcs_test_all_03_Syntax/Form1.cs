﻿#define TYPE1
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
            //for Interaction,          //參考/加入參考/.NET/Microsoft.VisualBasic
            string uName = Microsoft.VisualBasic.Interaction.InputBox("請輸入姓名", "程式啟動時，輸入資料");
            DialogResult dr = MessageBox.Show(uName + "歡迎您！", "歡迎", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
            this.Text = uName;	//表單標題顯示姓名

            show_item_location();
            textBox_hex.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單

            //For 驗證身份證字號
            txtInput.MaxLength = 10;//設定字元數最大值
            //txtInput.Focus();//程式啟動就把焦點移到txtInput
            this.AcceptButton = button36;//按下enter就觸發button click事件     //要改??

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

            //離開按鈕的寫法
            bt_exit_setup();

            //最小化按鈕的寫法
            bt_minimize_setup();
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

        void bt_minimize_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_minimize = new Button();  // 實例化按鈕
            bt_minimize.Size = new Size(w, h);
            bt_minimize.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            //g.DrawLine(p, 0, 0, w - 1, h - 1);
            //g.DrawLine(p, w - 1, 0, 0, h - 1);
            g.DrawLine(p, w / 4, h / 2 - 1, w * 3 / 4, h / 2 - 1);
            bt_minimize.Image = bmp;

            bt_minimize.Location = new Point(this.ClientSize.Width - bt_minimize.Width * 2 - 2, 0);
            bt_minimize.Click += bt_minimize_Click;     // 加入按鈕事件

            this.Controls.Add(bt_minimize); // 將按鈕加入表單
            bt_minimize.BringToFront();     //移到最上層
        }

        private void bt_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
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

            button42.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button43.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button44.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button45.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button46.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            button47.Location = new Point(x_st + dx * 5, y_st + dy * 6);
            button48.Location = new Point(x_st + dx * 6, y_st + dy * 6);
            textBox_ratio.Location = new Point(x_st + dx * 6, y_st + dy * 7);

            label11.Location = new Point(x_st + dx * 7, y_st + dy * 5 + 5);
            textBox_hex.Location = new Point(x_st + dx * 7 + 32, y_st + dy * 5);
            lb_dec.Location = new Point(x_st + dx * 7 + 148, y_st + dy * 5 + 5);
            lb_dec.Text = "";

            groupBox2.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 8 - 50, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 9 - 70, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 9 - 70, y_st + dy * 3);

            groupBox5.Location = new Point(x_st + dx * 0, y_st + dy * 15);
            groupBox6.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            groupBox7.Location = new Point(x_st + dx * 3, y_st + dy * 10);

            /*
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
            */

            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 10);
            richTextBox1.Size = new Size(750, 550);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
        }

        private void button6_Click(object sender, EventArgs e)
        {
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
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得控件本身\n";
            Control con = (Control)sender;  //取得控件本身

            richTextBox1.Text += "控件畫圖\n";
            Graphics g = con.CreateGraphics();
            g.DrawRectangle(Pens.Red, 3, 3, 30, 30);


            richTextBox1.Text += "顯示控件上的文字: \t";
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


        int aaa = 100;
        int bbb = 5;
        private void button12_Click(object sender, EventArgs e)
        {
            //Debug.Assert 用法

            Debug.Assert(bbb != 0);
            richTextBox1.Text += aaa.ToString() + " / " + bbb.ToString() + " = " + (aaa / bbb).ToString() + "\n";

            bbb--;
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
            for (int i = 1; i <= 10; i++)
            {
                this.Controls["label" + i.ToString()].Text = "這是label" + i.ToString();
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //三元運算子
            richTextBox1.Text += (DateTime.Now.Hour < 12) ? "Good morning\n" : "Good afternoon\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //throw 範例

            try
            {
                int year = 2006;
                int age = verify(year);
                richTextBox1.Text += "您已成年, 今年" + age + "歲\n";
            }
            catch (ArgumentOutOfRangeException ex)
            {
                richTextBox1.Text += "您並未成年\t" + ex.Message + "\n";
            }
            catch (ArgumentException ex)
            {
                richTextBox1.Text += "您輸入的年份範圍不合理\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "發生其他例外，例外訊息: " + ex.Message + "\n";
            }
        }

        public static int verify(int year)
        {
            if (year < 1 || year > DateTime.Now.Year)
                throw new ArgumentException();
            else if (DateTime.Now.Year - year < 18)
                throw new ArgumentOutOfRangeException();
            else
                return DateTime.Now.Year - year;
        }


        private void button20_Click(object sender, EventArgs e)
        {
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

        private void button25_Click(object sender, EventArgs e)
        {
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

        enum Products { HardDrive = 0, PenDrive = 4, Keyboard = 8 };

        enum ANIMAL
        {
            mouse = 1,
            cow = 2,
            tiger = 3,
            rabbit = 4,
            dragon = 5
        }

        //ENUM的用法
        // 定義WeekDays列舉內容7個成員
        // 用來表示一星期的星期日到星期六的列舉常數值
        enum WeekDays : int
        {
            Monday = 1,      	// 星期一
            Tuesday = 2,         // 星期二
            Wednesday = 3,       // 星期三
            Thursday = 4,        // 星期四
            Friday = 5,          // 星期五
            Saturday = 6,        // 星期六
            Sunday = 7           // 星期日
        };

        //默認從0開始：分別為0，1，2，3
        enum Level1
        {
            Employee,
            Manager,
            Boss,
            BigBoss,
        }

        //未指定的列舉名的值將依著最后一個指定值向后依次遞增（注意是最后一個指定值）
        //列舉中定義的可以自定義整數值
        enum Level2
        {
            Employee = 100,
            Manager,
            Boss,
            BigBoss,
        }
        //結果為100，101，102，103

        //列舉中定義的整數值可以部分預設
        enum Level3
        {
            Employee = 100,
            Manager,
            Boss = 102,
            BigBoss,
        }
        //Manager自動為101，BigBoss自動為103

        enum Level4
        {
            Employee = 100,
            Manager,
            Boss = 101,
            BigBoss,
        }
        //結果為100，101，101，102，有兩個101也是合法的
        //但不能有兩個Manager，即enum中的名稱不能重復，

        //位元位式用法

        enum Skill
        {
            Drive = 1,  //二進制  0001
            Cook = 2,  //二進制  0010
            Program = 4, //二進制  0100
            Teach = 8, //二進制  1000
        }

        class Person
        {
            public int ID { get; set; }
            public string Name { get; set; }
            public Level1 Level { get; set; }
            public Skill Skill { get; set; }
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //ENUM的用法
            Products prod1 = Products.HardDrive;
            Products prod2 = Products.PenDrive;
            Products prod3 = Products.Keyboard;

            richTextBox1.Text += "印出各個變數\n";
            richTextBox1.Text += prod1 + "\n";
            richTextBox1.Text += prod2 + "\n";
            richTextBox1.Text += prod3 + "\n";

            int ret = prod3.CompareTo(prod2);

            if (ret > 0)
            {
                richTextBox1.Text += prod3 + " 比 " + prod2 + " 多\n";
            }
            else if (ret < 0)
            {
                richTextBox1.Text += prod3 + " 比 " + prod2 + " 少\n";
            }
            else
            {
                richTextBox1.Text += prod3 + " 比 " + prod2 + " 等同\n";
            }


            richTextBox1.Text += "打印ENUM的內容\n";
            string s;
            byte c;
            for (c = 0; c <= 8; c++)
            {
                ANIMAL a = (ANIMAL)c;
                richTextBox1.Text += a.ToString() + "\n";
            }

            richTextBox1.Text += "ENUM的用法\n";
            // 取出WeekDays.Wednesday列舉常數值之後再轉成整數
            richTextBox1.Text += "星期三列舉常數值：" + (int)WeekDays.Wednesday + "\n";
            richTextBox1.Text += "星期五列舉常數值：" + (int)WeekDays.Friday + "\n";


            //ENUM的用法




            Person person1 = new Person();
            person1.Level = Level1.Employee;

            richTextBox1.Text += "result : " + ((int)Level1.Boss).ToString() + "\n";
            //結果為2

            Person person2 = new Person();
            person2.Skill = Skill.Drive | Skill.Cook | Skill.Program | Skill.Teach; //二進制  1111，十進制的15 //結果為15

            richTextBox1.Text += "Skill : " + ((int)person2.Skill).ToString() + "\n";
            richTextBox1.Text += "Skill a : " + ((person2.Skill & Skill.Cook) > 0).ToString() + "\n";
            richTextBox1.Text += "Skill b : " + ((person2.Skill & Skill.Cook) == Skill.Cook).ToString() + "\n";

            Console.WriteLine(person2.Skill);
            Console.WriteLine((person2.Skill & Skill.Cook) > 0); //結果為True，（1111 & 0010 = 0010）
            Console.WriteLine((person2.Skill & Skill.Cook) == Skill.Cook); //結果為True

        }

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button31_Click(object sender, EventArgs e)
        {
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

        private void button33_Click(object sender, EventArgs e)
        {
        }

        //傳值呼叫 vs 傳址呼叫 ST
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
        //傳值呼叫 vs 傳址呼叫 SP

        private void button35_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "GetBytes GetString 使用範例 1\n";

            int len;

            string str = "ABCDE\n";

            richTextBox1.Text += "原字串 : " + str + "\n";

            len = str.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            byte[] B = Encoding.Default.GetBytes(str);  //翻譯字串Str為Byte陣列B   //GetBytes : 把字串翻譯成Byte陣列
            len = B.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            PrintHexBytes(B);

            B[1] += 5;
            B[3] += 7;

            str = Encoding.Default.GetString(B); //翻譯B陣列為字串A        //接收到的byte轉為文字
            richTextBox1.Text += "轉回來字串 : " + str + "\n";

            /*
            richTextBox1.Text += "byte[] 轉 char[]\n";

            byte[] byteData = new byte[5] { 0x01, 0x02, 0x03, 0x04, 0x05 };
            char[] cChar = Encoding.ASCII.GetChars(byteData);

            richTextBox1.Text += "char[] 轉 二進位碼的文字型態\n";
            char[] cChar = new char[5] { 'a', 'b', 'c', 'd', 'e' };
            byte[] byteData = Encoding.Default.GetBytes(cChar);
            */
        }

        public void PrintHexBytes(byte[] bytes)
        {
            if ((bytes == null) || (bytes.Length == 0))
            {
                richTextBox1.Text += "<none>";
            }
            else
            {
                for (int i = 0; i < bytes.Length; i++)
                {
                    richTextBox1.Text += bytes[i].ToString("X2") + "\n";
                }
            }
        }

        private void button36_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "GetBytes GetString 使用範例 2\n";

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

            str = Encoding.Default.GetString(byteArray);

            richTextBox1.Text += "使用GetString將拜列轉成字串:\t" + str + "\n";

            str = "this is a lion-mouse";
            richTextBox1.Text += "\n原字串:\t" + str + "\n";

            byteArray = Encoding.Default.GetBytes(str);
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

        private void button37_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "C# Extension Method 用法\n";

            var arr = new double[]
            {
                39456,
                39482,
                39484,
                39493,
                39496,
                39497,
                39270 
            };

            foreach (double val in arr)
            {
                // C# Extension Method: Double - FromOADate
                DateTime oaDate = val.FromOADate();

                richTextBox1.Text += "val = " + val + "\tOA Date = " + oaDate.ToShortDateString() + "\n";
            }

            DateTime date = new DateTime(2006, 3, 11);
            // C# Extension Method: DateTime - Age
            int age = date.Age();
            richTextBox1.Text += "Age : " + age.ToString() + "\n";


            Guid guid = Guid.NewGuid();

            Guid[] guids = new Guid[]
            {
                Guid.NewGuid(),
                Guid.NewGuid(),
                Guid.NewGuid(),
                guid
            };

            // C# Extension Method: Guid - In
            if (guid.In(guids))
            {
                richTextBox1.Text += "guid = " + guid + "exists in the list.\n";
            }
            else
            {
                richTextBox1.Text += "guid = " + guid + "doesn't exists in the list.\n";
            }
        }

        //swap範例 ST
        private void Swap(ref int n1, ref int n2)
        {
            int temp = n1;
            n1 = n2;
            n2 = temp;
        }

        private void button38_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\nswap範例\n";
            int a = 10, b = 15;
            richTextBox1.Text += "主程式:呼叫Swap方法前: a = " + a.ToString() + "  b = " + b.ToString() + "\n";
            Swap(ref a, ref b);
            richTextBox1.Text += "主程式:呼叫Swap方法後: a = " + a.ToString() + "  b = " + b.ToString() + "\n";
        }
        //swap範例 SP

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
                button41_Click(sender, e);
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

        private void bt_parse_data_Click(object sender, EventArgs e)
        {
            //各種Parse範例
            ParseData parse = new ParseData();
            parse.Show();
        }

        private void bt_example_Click(object sender, EventArgs e)
        {
            int x;  //被除數
            int y;  //除數

            x = 30;
            y = 0;

            try
            {
                richTextBox2.Text += "商為: " + x / y + "\t餘數為: " + x % y + "\n";
            }
            catch (Exception ex)
            {
                richTextBox2.Text += "例外發生\n";
                richTextBox2.Text += "訊息: " + ex.Message + "\n";
                richTextBox2.Text += "例外來源: " + ex.Source + "\n";
                richTextBox2.Text += "丟出例外的方法: " + ex.TargetSite + "\n";
                richTextBox2.Text += "詳細文字說明: " + ex.ToString() + "\n";
            }
        }

        private void button42_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\nout 語法 1\n";
            int r = 0;
            for (int i = 1; i < 10; i++)
            {
                Math.DivRem(i, 7, out r);
                richTextBox1.Text += i.ToString() + " 除以 7 的餘數 " + r.ToString() + "\n";
            }
        }

        private void button43_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\nout 語法 2\t呼叫一個函數 回傳兩個變數\n";
            int i;
            Random r = new Random();
            int[] array = new int[15];
            for (i = 0; i < array.Length; i++)
            {
                array[i] = r.Next(100);
                richTextBox1.Text += array[i].ToString() + " ";
            }

            richTextBox1.Text += "\n";

            int y_min;
            int y_max;
            GetDataValueRange(array, out y_min, out y_max);

            richTextBox1.Text += "y_min = " + y_min.ToString() + "\t" + "y_max = " + y_max.ToString() + "\n";
        }

        void GetDataValueRange(int[] array, out int y_min, out int y_max)
        {
            int i;
            int len = array.Length;
            y_min = int.MaxValue;
            y_max = int.MinValue;
            for (i = 0; i < len; i++)
            {
                if (y_min > array[i])
                {
                    y_min = array[i];
                }
                if (y_max < array[i])
                {
                    y_max = array[i];
                }
            }
        }

        //ASCII Table ST
        internal string TenToBinary(long value)//將十進制轉換為二進制
        {
            return Convert.ToString(value, 2).PadLeft(8, '0').Insert(4, "_");
        }

        private void button44_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            int k;
            for (j = 0; j < 32; j++)
            {
                for (i = 0; i < 128; i += 32)
                {
                    k = j + i;

                    richTextBox1.Text += k.ToString().PadLeft(3) + "  " + TenToBinary(k) + "  0x" + k.ToString("X2");
                    if (char.IsControl((char)k) == true)
                    {
                        richTextBox1.Text += " ";
                    }
                    else
                    {
                        richTextBox1.Text += " " + (char)k;
                    }
                    richTextBox1.Text += "\t";
                }
                richTextBox1.Text += "\n";
            }
        }
        //ASCII Table SP

        private void button45_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            int k;
            for (j = 0; j < 32; j++)
            {
                richTextBox1.Text += "<tr align=\"center\" bgcolor=\"#FFFFF0\">";
                for (i = 0; i < 128; i += 32)
                {
                    k = j + i;

                    richTextBox1.Text += "<td>" + k.ToString() + "</td><td>" + TenToBinary(k) + "</td><td>0x" + k.ToString("X2");
                    if (char.IsControl((char)k) == true)
                    {
                        richTextBox1.Text += "</td><td>";
                    }
                    else
                    {
                        richTextBox1.Text += "</td><td>" + (char)k;
                    }
                    //richTextBox1.Text += "\t";
                }
                richTextBox1.Text += "</tr>\n";
            }

        }

        private void button46_Click(object sender, EventArgs e)
        {

        }

        private void button47_Click(object sender, EventArgs e)
        {

        }

        private void button48_Click(object sender, EventArgs e)
        {
            //解讀比例

            float aspect_ratio = GetAspectRatio(textBox_ratio.Text);
            richTextBox1.Text += "解讀比例 : " + aspect_ratio.ToString() + "\n";
        }

        private float GetAspectRatio(string text)
        {
            try
            {
                // See if the text contains a colon.
                if (text.Contains(":"))
                {
                    float width = float.Parse(text.Split(':')[0]);
                    float height = float.Parse(text.Split(':')[1]);
                    return width / height;
                }
                else
                {
                    return float.Parse(text);
                }
            }
            catch
            {
                return 1;
            }
        }
    }

    public static partial class Extensions
    {
        //第一種Extension
        /// <summary>
        ///     Returns a  equivalent to the specified OLE Automation Date.
        /// </summary>
        /// <param name="d">An OLE Automation Date value.</param>
        /// <returns>An object that represents the same date and time as .</returns>
        public static DateTime FromOADate(this Double d)
        {
            return DateTime.FromOADate(d);
        }

        //第二種Extension
        /// <summary>
        ///     A DateTime extension method that ages the given this.
        /// </summary>
        /// <param name="this">The @this to act on.</param>
        /// <returns>An int.</returns>
        public static int Age(this DateTime @this)
        {
            if (DateTime.Today.Month < @this.Month || DateTime.Today.Month == @this.Month && DateTime.Today.Day < @this.Day)
            {
                return DateTime.Today.Year - @this.Year - 1;
            }
            return DateTime.Today.Year - @this.Year;
        }

        //第三種Extension
        /// <summary>
        ///     A T extension method to determines whether the object is equal to any of the provided values.
        /// </summary>
        /// <param name="this">The object to be compared.</param>
        /// <param name="values">The value list to compare with the object.</param>
        /// <returns>true if the values list contains the object, else false.</returns>
        /// ###
        /// <typeparam name="T">Generic type parameter.</typeparam>
        public static bool In(this Guid @this, params Guid[] values)
        {
            return Array.IndexOf(values, @this) != -1;
        }
    }
}
