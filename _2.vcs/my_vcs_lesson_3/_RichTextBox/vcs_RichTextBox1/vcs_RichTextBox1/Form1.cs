using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FILE
using System.Diagnostics;   //for Process, Stopwatch


namespace vcs_RichTextBox1
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
            show_richtextbox_font();

            //RichTextBox 字數統計
            lb_richtextbox1_fx4.Text = "字數 : " + richTextBox1.TextLength.ToString() + ", 行數 : " + richTextBox1.Lines.Length.ToString();

            richTextBox1.Text +=
                "在RichTextBox控制元件上新增超連結文字\n" +
                "要在RichTextBox加上LinkClicked事件\n" +
                "雅虎：http://tw.yahoo.com\n" +
                "Google：http://www.google.com/\n" +
                "維基百科：https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5\n" +
                "雅虎字典：https://tw.dictionary.search.yahoo.com/\n";
            richTextBox1.LinkClicked += new LinkClickedEventHandler(richTextBox1_LinkClicked);
        }

        private void richTextBox1_LinkClicked(object sender, LinkClickedEventArgs e)
        {
            this.Text = e.LinkText;//設置與窗體關聯的文本
            Process.Start("firefox", e.LinkText);// 在firefox瀏覽器中瀏覽單擊的超鏈接
        }

        private void SelectRichText(RichTextBox rch, string target)
        {
            int pos = rch.Text.IndexOf(target);
            if (pos < 0)
            {
                // Not found. Select nothing.
                rch.Select(0, 0);//離開選取
            }
            else
            {
                // Found the text. Select it.
                rch.Select(pos, target.Length);//部分區域位置 ST, len
            }
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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            int dd = 30;
            lb_richtextbox1_fx1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd * 0);
            lb_richtextbox1_fx2.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd * 1);
            lb_richtextbox1_fx3.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd * 2);
            lb_richtextbox1_fx5.Location = new Point(x_st + dx * 3 + 360, y_st + dy * 0 + dd * 1);
            lb_richtextbox1_fx6.Location = new Point(x_st + dx * 3 + 360, y_st + dy * 0 + dd * 3 - 10);
            lb_richtextbox1_fx4.Location = new Point(x_st + dx * 3 + 360, y_st + dy * 0 + dd * 0);
            lb_richtextbox1_text.Location = new Point(x_st + dx * 3 + 360 + 260, y_st + dy * 0 + dd * 0);

            lb_richtextbox1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd * 4);
            richTextBox1.Size = new Size(850, 290);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd * 5);

            lb_richtextbox2.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            richTextBox2.Size = new Size(400, 200);
            richTextBox2.Location = new Point(x_st + dx * 3, y_st + dy * 7 + dd);

            lb_richtextbox_rtf.Location = new Point(x_st + dx * 5, y_st + dy * 7);
            richTextBox_rtf.Size = new Size(430, 200);
            richTextBox_rtf.Location = new Point(x_st + dx * 5, y_st + dy * 7 + dd);

            dd = 45;
            bt_open_rtf.Location = new Point(richTextBox_rtf.Location.X + richTextBox_rtf.Width - dd * 2, richTextBox_rtf.Location.Y);
            bt_save_rtf.Location = new Point(richTextBox_rtf.Location.X + richTextBox_rtf.Width - dd * 1, richTextBox_rtf.Location.Y);

            dd = 60;
            bt_analyze.Location = new Point(richTextBox1.Location.X + dd * 0, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_open1.Location = new Point(richTextBox1.Location.X + dd * 1, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_open2.Location = new Point(richTextBox1.Location.X + dd * 2, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_open3.Location = new Point(richTextBox1.Location.X + dd * 3, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_font.Location = new Point(richTextBox1.Location.X + dd * 4, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_backcolor.Location = new Point(richTextBox1.Location.X + dd * 5, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_part1.Location = new Point(richTextBox1.Location.X + dd * 6, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_search.Location = new Point(richTextBox1.Location.X + dd * 7, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_save1.Location = new Point(richTextBox1.Location.X + dd * 8, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_save2.Location = new Point(richTextBox1.Location.X + dd * 9 - 20, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_save3.Location = new Point(richTextBox1.Location.X + dd * 10 - 40, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_shape0.Location = new Point(richTextBox1.Location.X + dd * 11 - 60, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_shape1.Location = new Point(richTextBox1.Location.X + dd * 12 - 80, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_shape2.Location = new Point(richTextBox1.Location.X + dd * 13 - 100, richTextBox1.Location.Y + richTextBox1.Size.Height);
            bt_shape3.Location = new Point(richTextBox1.Location.X + dd * 14 - 120, richTextBox1.Location.Y + richTextBox1.Size.Height);

            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear1.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear1.Size.Height);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);

            this.Size = new Size(1500 + 20, 780);

            lb_richtextbox1.Text = "richTextBox1";
            lb_richtextbox2.Text = "richTextBox2 message";
            lb_richtextbox_rtf.Text = "richTextBox_rtf";
            lb_richtextbox1_text.Text = "抓出游標所指的字";
            this.Text = "vcs_RichTextBox1";
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        bool flag_change_rtb_backcolor = false;
        private void button0_Click(object sender, EventArgs e)
        {
            //改變/恢復 背景色
            if (flag_change_rtb_backcolor == false)
            {
                flag_change_rtb_backcolor = true;
                richTextBox1.BackColor = Color.Pink;
            }
            else
            {
                flag_change_rtb_backcolor = false;
                richTextBox1.BackColor = Color.FromName("Control");
            }

            //改變字體大小(加1號)
            //float oldSize = richTextBox1.SelectionFont.Size;//僅選取部分
            float oldSize = richTextBox1.Font.Size;//整個RTB

            float newSize = oldSize + 1;

            FontFamily currentFontFamily;
            Font newFont;
            currentFontFamily = this.richTextBox1.SelectionFont.FontFamily;//僅選取部分
            newFont = new Font(currentFontFamily, newSize);//整個RTB
            //this.richTextBox1.SelectionFont = newFont;//僅選取部分
            this.richTextBox1.Font = newFont;//整個RTB

            show_richtextbox_font();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string txt = "\n\nWelcome to the United States and have a nice day.";
            richTextBox1.Text = txt;

            richTextBox1.Select(txt.IndexOf("Welcome"), "Welcome".Length);
            richTextBox1.SelectionFont = new Font(richTextBox1.SelectionFont, FontStyle.Italic);

            richTextBox1.Select(txt.IndexOf("the"), "the".Length);
            richTextBox1.SelectionFont = new Font(richTextBox1.SelectionFont, FontStyle.Bold);
            richTextBox1.SelectionColor = Color.Brown;

            richTextBox1.Select(txt.IndexOf("United States"), "United States".Length);
            richTextBox1.SelectionFont = new Font(richTextBox1.SelectionFont, FontStyle.Bold);
            richTextBox1.SelectionColor = Color.Red;

            richTextBox1.Select(txt.IndexOf("have"), "have".Length);
            richTextBox1.SelectionFont = new Font(richTextBox1.SelectionFont, FontStyle.Underline);

            richTextBox1.Select(txt.IndexOf("nice"), "nice".Length);
            richTextBox1.SelectionFont = new Font(richTextBox1.SelectionFont, FontStyle.Bold);

            richTextBox1.Select(txt.IndexOf("day"), "day".Length);
            richTextBox1.SelectionFont = new Font(richTextBox1.SelectionFont, FontStyle.Bold);
            richTextBox1.SelectionColor = Color.Blue;

            richTextBox1.Select(0, 0);//離開選取
        }

        //#region 日誌記錄、支援其他執行緒訪問
        public delegate void LogAppendDelegate(Color color, string text);
        /// <summary> 
        /// 追加顯示文字 
        /// </summary> 
        /// <param name="color">文字顏色</param> 
        /// <param name="text">顯示文字</param> 
        public void LogAppend(Color color, string text)
        {
            richTextBox1.AppendText("\n");
            richTextBox1.SelectionColor = color;
            richTextBox1.AppendText(text);
        }
        /// <summary> 
        /// 顯示錯誤日誌 
        /// </summary> 
        /// <param name="text"></param> 
        public void LogError(string text)
        {
            LogAppendDelegate la = new LogAppendDelegate(LogAppend);
            richTextBox1.Invoke(la, Color.Red, DateTime.Now.ToString("HH:mm:ss ") + text);
        }
        /// <summary> 
        /// 顯示警告資訊 
        /// </summary> 
        /// <param name="text"></param> 
        public void LogWarning(string text)
        {
            LogAppendDelegate la = new LogAppendDelegate(LogAppend);
            richTextBox1.Invoke(la, Color.Violet, DateTime.Now.ToString("HH:mm:ss ") + text);
        }
        /// <summary> 
        /// 顯示資訊 
        /// </summary> 
        /// <param name="text"></param> 
        public void LogMessage(string text)
        {
            LogAppendDelegate la = new LogAppendDelegate(LogAppend);
            richTextBox1.Invoke(la, Color.Black, DateTime.Now.ToString("HH:mm:ss ") + text);
        }
        //#endregion

        private void button2_Click(object sender, EventArgs e)
        {
            string str1 = "C# RichTextBox顯示不同顏色文字 一般訊息";
            string str2 = "C# RichTextBox顯示不同顏色文字 錯誤訊息";
            string str3 = "C# RichTextBox顯示不同顏色文字 警告訊息";

            LogMessage(str1);
            LogError(str2);
            LogWarning(str3);
            LogMessage(str1);
            LogError(str2);
            LogWarning(str3);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //在方案總管vcs_RichTextBox1按加入/現有項目/選擇 RtfTable.cs, RtfTable.cs要改namespace為vcs_RichTextBox1
            RtfTable table = new RtfTable(4, 3, 120);
            table.SetColumnWidths(1720, 1720, 1720);    //設定表格寬度

            for (int r = 0; r < 4; r++)
            {
                for (int c = 0; c < 3; c++)
                {
                    table.Contents[r, c] = "(" + r.ToString() + ", " + c.ToString() + ")";
                }
            }
            // 在RichTextBox中的某處加入表格 Insert the table at @@@.
            richTextBox1.Rtf = richTextBox1.Rtf.Replace("@@@", table.ToString());
            // 在RichTextBox最後加入表格 Insert the table at the end.
            richTextBox1.Rtf = richTextBox1.Rtf.Trim().TrimEnd('}') + table.ToString() + "}";
        }

        int flag_rtb_sort = 0;
        private void button4_Click(object sender, EventArgs e)
        {
            if (flag_rtb_sort == 0)
            {
                flag_rtb_sort = 1;
                lb_richtextbox1.Text = "richTextBox1,  重新填資料";
                richTextBox1.Clear();
                richTextBox1.Text += "文天祥過零丁洋\n";
                richTextBox1.Text += "辛苦遭逢起一經\n";
                richTextBox1.Text += "干戈寥落四周星\n";
                richTextBox1.Text += "山河破碎風飄絮\n";
                richTextBox1.Text += "身世浮沉雨打萍\n";
                richTextBox1.Text += "惶恐灘頭說惶恐\n";
                richTextBox1.Text += "零丁洋裏歎零丁\n";
                richTextBox1.Text += "人生自古誰無死\n";
                richTextBox1.Text += "留取丹心照汗青";
            }
            else if (flag_rtb_sort == 1)
            {
                flag_rtb_sort = 2;
                lb_richtextbox1.Text = "richTextBox1,  排序";
                //richTextBox2.Text += "There are " + richTextBox1.Lines.Length.ToString() + " lines in richtextBox1\n";
                //Array.Sort(richTextBox1.Lines);   //useless
                string[] temp = richTextBox1.Lines;
                Array.Sort(temp);
                richTextBox1.Lines = temp;
            }
            else if (flag_rtb_sort == 2)
            {
                flag_rtb_sort = 0;
                lb_richtextbox1.Text = "richTextBox1,  任意排序";
                string[] temp = richTextBox1.Lines;
                double[] randomIndex = new double[temp.Length];
                Random r = new Random();
                for (int i = 0; i < temp.Length; i++)
                {
                    randomIndex[i] = r.NextDouble();
                }
                Array.Sort(randomIndex, temp);
                richTextBox1.Lines = temp;
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //richTextBox 內文變色

            richTextBox1.SelectionColor = Color.Red;
            richTextBox1.AppendText("內文變色\n");
            richTextBox1.AppendText("恢復原色\n");

            richTextBox1.SelectionColor = Color.Orange;
            richTextBox1.AppendText("多行內文變色\n多行內文變色\n多行內文變色\n多行內文變色\n多行內文變色\n多行內文變色\n");
            richTextBox1.AppendText("恢復原色\n");

            richTextBox1.SelectionColor = Color.Yellow;
            richTextBox1.AppendText("內文變色\n");
            richTextBox1.AppendText("恢復原色\n");

            richTextBox1.SelectionColor = Color.Green;
            richTextBox1.AppendText("內文變色\n");
            richTextBox1.AppendText("恢復原色\n");

            richTextBox1.SelectionColor = Color.Blue;
            richTextBox1.AppendText("內文變色\n");
            richTextBox1.AppendText("恢復原色\n");

            richTextBox1.SelectionColor = Color.Purple;
            richTextBox1.AppendText("內文變色\n");
            richTextBox1.AppendText("恢復原色\n");
            richTextBox1.AppendText("恢復原色\n");
            richTextBox1.AppendText("恢復原色\n");
        }

        int flag_select_all = 0;
        private void button6_Click(object sender, EventArgs e)
        {
            int len = richTextBox1.Text.Length;

            if (flag_select_all == 0)
            {
                flag_select_all = 1;

                //richTextBox 選取部分
                richTextBox1.Focus();
                richTextBox1.Select(len / 3, len / 3);//部分區域位置 ST, len
            }
            else if (flag_select_all == 1)
            {
                flag_select_all = 2;

                //RichTextBox 全選
                richTextBox1.Focus();
                richTextBox1.SelectAll();
            }
            else if (flag_select_all == 2)
            {
                flag_select_all = 0;

                //richTextBox 游標跳至指定位置

                //跳至前面
                richTextBox1.Focus();
                richTextBox1.Select(0, 0);//離開選取

                //跳至最後面
                richTextBox1.Focus();
                richTextBox1.Select(len, 0);//部分區域位置 ST, len

                //跳至某地
                richTextBox1.Focus();
                richTextBox1.Select(len * 4 / 5, 0);//部分區域位置 ST, len
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "RichTextBox用 += 印1000行資料\n";
            richTextBox1.Clear();
            Stopwatch sw = new Stopwatch();
            sw.Start();

            for (int i = 0; i < 1000; i++)
            {
                richTextBox1.Text += "ABCDEFGHIJKLMNOPQRSTUVWXYZ  " + i.ToString() + "\n";
            }

            sw.Stop();
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.00") + " 秒\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "RichTextBox先製造好1000行資料再一次印出來\n";
            richTextBox1.Clear();
            Stopwatch sw = new Stopwatch();
            sw.Start();

            string aaaa = string.Empty;
            for (int i = 0; i < 1000; i++)
            {
                aaaa += "ABCDEFGHIJKLMNOPQRSTUVWXYZ  " + i.ToString() + "\n";
            }

            richTextBox1.Text = aaaa;

            sw.Stop();
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.00") + " 秒\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //Hex mode顯示內容
            string data = "Hex mode顯示內容\n";
            string result = "";
            for (int i = 0; i < data.Length; i++)
            {
                result += ((int)data[i]).ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";
            richTextBox1.AppendText(result);     //打印一般文字訊息
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //RTB部分著色
            richTextBox1.SelectionStart = 30;
            richTextBox1.SelectionLength = 60;
            richTextBox1.SelectionBackColor = Color.Red;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //設定Tabs

            richTextBox1.Clear();

            richTextBox1.SelectionTabs = new int[] { 160, 320, 240 };
            richTextBox1.AcceptsTab = true;

            richTextBox1.Text += "顯示RichTextBox中的Tab功能\n\n";
            richTextBox1.Text +=
                "Breakfast\tLunch\tDinner\n" +
                "Coffee\tSoda\tWine\n" +
                "Bagel\tSandwich\tSalad\n" +
                "a\tb\tc\n" +
                "Fruit\tChips\tTofuburger\n" +
                "\tCookie\tVeggies";
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
            int j = 0;
            for (int i = 0x41; i < 0x5B; i++)
            {
                if ((i < 32) || (i > 126))
                    j = '-';
                else
                    j = i;
                richTextBox1.Text += i.ToString() + "\t0x" + i.ToString("X2") + "\t" + (char)j + "\n";
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            string str1 = "徹底修改matlab預設工作目錄";
            for (int i = 0; i < str1.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + str1[i] + "\t" + Convert.ToString(((int)str1[i]), 16) + "\n";
            }

            string str2 = "ABCDE";
            for (int i = 0; i < str2.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + str2[i] + "\t" + Convert.ToString(((int)str2[i]), 16) + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //string input = "Hello World!";
            string input = "基本運算制作USB启动盘ウィキペディア???世?生?????概?表????";
            char[] values = input.ToCharArray();
            foreach (char letter in values)
            {
                // Get the integral value of the character.
                int value = Convert.ToInt32(letter);
                // Convert the integer value to a hexadecimal value in string form.

                //Console.WriteLine($"Hexadecimal value of {letter} is {value:X}");
                richTextBox1.Text += "Hexadecimal value of " + letter + " is " + value.ToString("X4") + "\n";
            }
            richTextBox1.Text += "\n文字編碼都是Unicode編碼 Unicode (Big-Endian) 	1201 	utf-16BE\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        //用WordPad編輯rtf檔
        // Allow the user to edit the file with WordPad.
        private void button19_Click(object sender, EventArgs e)
        {
            string rtf_filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\text.rtf";

            // Hide.
            this.ShowInTaskbar = false;
            this.Hide();

            // We will open rtf_filename with wordpad.exe.
            ProcessStartInfo start_info = new ProcessStartInfo("wordpad.exe", rtf_filename);
            start_info.WindowStyle = ProcessWindowStyle.Maximized;

            // Open wordpad.
            Process process = new Process();
            process.StartInfo = start_info;
            process.Start();

            // Wait for wordpad to finish.
            process.WaitForExit();

            // Unhide.
            this.ShowInTaskbar = true;
            this.Show();
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
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

        private void button29_Click(object sender, EventArgs e)
        {
        }

        /// <summary>自定义方法 -- 
        ///  获取文本中(行和列)--光标--坐标位置的调用方法
        /// </summary>
        /// <param></param>
        /// <returns></returns>
        private void Ranks()
        {
            /*  得到光标行第一个字符的索引，
             *  即从第1个字符开始到光标行的第1个字符索引*/
            int index = richTextBox1.GetFirstCharIndexOfCurrentLine();
            /*得到光标行的行号,第1行从0开始计算，习惯上我们是从1开始计算，所以+1。 */
            int line = richTextBox1.GetLineFromCharIndex(index) + 1;
            /*  SelectionStart得到光标所在位置的索引
             *  再减去
             *  当前行第一个字符的索引
             *  = 光标所在的列数(从0开始)  */
            int column = richTextBox1.SelectionStart - index + 1;
            //this.label1.Text = string.Format("第：{0}行 {1}列", line.ToString(), column.ToString());
            this.Text = string.Format("列 {0}, 行 {1}", line.ToString(), column.ToString());
        }

        //取得游標所在的行號列號
        private void richTextBox1_KeyUp(object sender, KeyEventArgs e)
        {
            this.Ranks();  //按上、下、左、右时显示
        }

        //取得游標所在的行號列號
        private void richTextBox1_MouseUp(object sender, MouseEventArgs e)
        {
            this.Ranks();  //点击鼠标时显示
        }

        DateTime doubleClickTimer;
        private void richTextBox1_DoubleClick(object sender, EventArgs e)
        {
            doubleClickTimer = DateTime.Now; //記下DoubleClick的時間
        }

        private void richTextBox1_Click(object sender, EventArgs e)
        {
            TimeSpan t = (TimeSpan)(DateTime.Now - doubleClickTimer); //DoubleClick後又點了一下, 計算時間差

            if (t.TotalMilliseconds <= 200) //如果小於200豪秒就全選
            {
                richTextBox1.SelectAll();
            }
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            //RichTextBox 字數統計
            lb_richtextbox1_fx4.Text = "字數 : " + richTextBox1.TextLength.ToString() + ", 行數 : " + richTextBox1.Lines.Length.ToString();
        }

        private void bt_shape0_Click(object sender, EventArgs e)
        {
            //粗
            //選擇設置粗體或取消
            Font oldFont = this.richTextBox1.SelectionFont;
            Font newFont;
            if (oldFont.Bold)
                newFont = new Font(oldFont, oldFont.Style & ~FontStyle.Bold);
            else
                newFont = new Font(oldFont, oldFont.Style | FontStyle.Bold);
            this.richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();
        }

        private void bt_shape1_Click(object sender, EventArgs e)
        {
            //選擇設置斜體或取消
            Font oldFont = this.richTextBox1.SelectionFont;
            Font newFont;
            if (oldFont.Italic)
                newFont = new Font(oldFont, oldFont.Style & ~FontStyle.Italic);
            else
                newFont = new Font(oldFont, oldFont.Style | FontStyle.Italic);
            this.richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();
        }

        private void bt_shape2_Click(object sender, EventArgs e)
        {
            //選擇設置底線或取消
            Font oldFont = this.richTextBox1.SelectionFont;
            Font newFont;
            if (oldFont.Underline)
            {
                newFont = new Font(oldFont, oldFont.Style & ~FontStyle.Underline);
            }
            else
            {
                newFont = new Font(oldFont, oldFont.Style | FontStyle.Underline);
            }
            this.richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();
        }

        private void bt_shape3_Click(object sender, EventArgs e)
        {
            //選擇設置置中或取消
            if (this.richTextBox1.SelectionAlignment == HorizontalAlignment.Center)
                this.richTextBox1.SelectionAlignment = HorizontalAlignment.Left;
            else
                this.richTextBox1.SelectionAlignment = HorizontalAlignment.Center;
            this.richTextBox1.Focus();
        }

        private void bt_analyze_Click(object sender, EventArgs e)
        {
            int len = richTextBox1.Lines.Length;

            richTextBox2.Text += "分析RichTextBox1的內容\n";
            richTextBox2.Text += "RichTextBox1, 行數 : " + len.ToString() + "\t內容 :\n";
            for (int i = 0; i < len; i++)
            {
                richTextBox2.Text += "i = " + i.ToString() + "\t" + richTextBox1.Lines[i].Trim().Length.ToString() + "\t" + richTextBox1.Lines[i].Trim() + "\n";
            }
        }

        private void bt_open1_Click(object sender, EventArgs e)
        {
            //載入, 會覆蓋原本rtb內的資料

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\琵琶行.txt";

            //讀取純文字檔到richTextBox裏
            try
            {
                richTextBox1.LoadFile(filename, RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            catch (FileNotFoundException)
            {
                richTextBox2.Text += "找不到檔案\n";
            }
        }

        private void bt_open2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            //讀取純文字檔到richTextBox裏
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                // 運用 ReadAllText 方法 (String, Encoding) ，其中 Encoding 針對您txt檔案的編碼做變更，讀出的資料才不會有亂碼
                richTextBox1.Text += File.ReadAllText(openFileDialog1.FileName, System.Text.Encoding.Default);
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        private void bt_open3_Click(object sender, EventArgs e)
        {
        }

        private void bt_font_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowApply = true;
            fontDialog1.ShowColor = true;
            fontDialog1.ShowEffects = true;
            fontDialog1.ShowHelp = true;
            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                /*
                //僅選取部分
                //RichTextBox.SelectionFont取得目前選擇的文字，並且將FontDialog所設定的字型結果套入 
                richTextBox1.SelectionFont = fontDialog1.Font;
                richTextBox1.SelectionColor = fontDialog1.Color;
                richTextBox1.SelectionBackColor = Color.Lime;   //選取部分的背景色
                */

                //全部RTB
                richTextBox1.ForeColor = fontDialog1.Color;
                richTextBox1.Font = fontDialog1.Font;
            }
        }

        private void bt_backcolor_Click(object sender, EventArgs e)
        {
            //設定部分背景顏色

            colorDialog1.AllowFullOpen = true;
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.SelectionBackColor = colorDialog1.Color;//選取部分的背景色
            }
        }

        private void bt_part1_Click(object sender, EventArgs e)
        {
            //部分區域設定不同顏色
            richTextBox1.Select(43, 7);//部分區域位置 ST, len
            SelectRichText(richTextBox1, "莫聽穿林打葉聲");//same
            richTextBox1.SelectionColor = Color.Red;//部分區域前景色
            richTextBox1.SelectionBackColor = Color.Green; //部分區域背景色

            //richTextBox1.SelectionFont = new Font("標楷體", 20, FontStyle.Bold);//部分區域字型
            richTextBox1.SelectionFont = new Font("標楷體", 20, FontStyle.Italic);
            //richTextBox1.SelectionFont = new Font(richTextBox1.Font, FontStyle.Italic);

            richTextBox1.Select(0, 0);//離開選取            
        }

        private void bt_search_Click(object sender, EventArgs e)
        {
            //在RTF檔內搜尋
            richTextBox1.Find("雨", RichTextBoxFinds.MatchCase);
            richTextBox1.SelectionFont = new Font("標楷體", 30, FontStyle.Bold);
            richTextBox1.SelectionColor = Color.Red;
        }

        private void bt_save1_Click(object sender, EventArgs e)
        {
            string filename = "tmp1_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            try
            {
                richTextBox1.SaveFile(filename, RichTextBoxStreamType.PlainText);    //將richTextBox的資料寫入到指定的文字檔
                richTextBox2.Text += "存檔完成, 檔名 : " + filename + "\n";
            }
            catch (System.Exception err)
            {
                richTextBox2.Text += "存檔失敗, 原因 : " + err.Message + "\n";
            }
        }

        private void bt_save2_Click(object sender, EventArgs e)
        {
            string filename = "tmp2_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            //XXX richTextBox1.SaveFile(filename, RichTextBoxStreamType.PlainText);    //將richTextBox的資料寫入到指定的文字檔, 這樣會出現怪字型, 還是一行一行儲存比較好

            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("unicode"));   //指名編碼格式            
            sw.Write(richTextBox1.Text);
            sw.Close();
            richTextBox2.Text += "存檔完成, 檔名 : " + filename + "\n";
        }

        private void bt_save3_Click(object sender, EventArgs e)
        {
        }

        // Display the word under the mouse.
        private void richTextBox1_MouseMove(object sender, MouseEventArgs e)
        {
            lb_richtextbox1_text.Text = WordUnderMouse(richTextBox1, e.X, e.Y);

            char ch = richTextBox1.GetCharFromPosition(e.Location);     //取得指定位置的字元

            int nn = richTextBox1.GetCharIndexFromPosition(e.Location); //指定位置處的以零起始的字元索引

            lb_richtextbox1_fx5.Text = "MouseMove : " + ch.ToString() + " @ " + nn.ToString();
        }

        // Return the word under the mouse.
        private string WordUnderMouse(RichTextBox rch, int x, int y)
        {
            // Get the character's position.
            int pos = rch.GetCharIndexFromPosition(new Point(x, y));
            if (pos <= 0)
            {
                return "";
            }

            // Find the start of the word.
            string txt = rch.Text;

            int start_pos;
            for (start_pos = pos; start_pos >= 0; start_pos--)
            {
                // Allow digits, letters, and underscores
                // as part of the word.
                char ch = txt[start_pos];
                if (!char.IsLetterOrDigit(ch) && !(ch == '_'))
                {
                    break;
                }
            }
            start_pos++;

            // Find the end of the word.
            int end_pos;
            for (end_pos = pos; end_pos < txt.Length; end_pos++)
            {
                char ch = txt[end_pos];
                if (!char.IsLetterOrDigit(ch) && !(ch == '_'))
                {
                    break;
                }
            }
            end_pos--;

            // Return the result.
            if (start_pos > end_pos)
            {
                return "";
            }
            return txt.Substring(start_pos, end_pos - start_pos + 1);
        }

        private void richTextBox1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "C# richTextBox 點兩下全選\n";
            richTextBox1.SelectAll();
        }

        private void richTextBox1_SelectionChanged(object sender, EventArgs e)
        {
            lb_richtextbox1_fx6.Text = "SelectionChanged : ST " + richTextBox1.SelectionStart.ToString() + "   " + "len = " + richTextBox1.SelectionLength.ToString();
        }

        void show_richtextbox_font()
        {
            Font f = this.richTextBox1.Font;
            lb_richtextbox1.Text = "richTextBox1,  " + f.Name + ",  " + f.Size;
        }

        private void bt_open_rtf_Click(object sender, EventArgs e)
        {
            //富文字格式（Rich Text Format）即RTF格式，又稱多文字格式

            string rtf_filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\text.rtf";
            //string rtf_filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\SAMPO(PA63)變頻分離式室外機功能規格書_2014.08.18doc.rtf";

            richTextBox_rtf.LoadFile(rtf_filename);
        }

        private void bt_save_rtf_Click(object sender, EventArgs e)
        {
            //另存RTF檔
            string rtf_filename = "tmp_rtf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".rtf";
            richTextBox_rtf.SaveFile(rtf_filename);
            //richTextBox_rtf.SaveFile(rtf_filename, RichTextBoxStreamType.RichText);
            richTextBox2.Text += "已存檔 : " + rtf_filename + "\n";
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




