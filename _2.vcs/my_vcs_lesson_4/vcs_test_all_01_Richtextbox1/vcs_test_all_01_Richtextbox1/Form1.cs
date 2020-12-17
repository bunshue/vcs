using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Globalization;//for CultureInfo

namespace vcs_test_all_01_Richtextbox1
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
            label4.Text = "字數 : " + richTextBox1.TextLength.ToString();
            label6.Text = "";

            // Format RichTextBox1.
            richTextBox_format_1.Select(4, 5);
            richTextBox_format_1.SelectionColor = Color.Red;
            richTextBox_format_1.Select(16, 3);
            richTextBox_format_1.SelectionFont = new Font(richTextBox_format_1.Font, FontStyle.Italic);
            richTextBox_format_1.Select(35, 4);
            richTextBox_format_1.SelectionBackColor = Color.Yellow;
            richTextBox_format_1.SelectionColor = Color.Brown;
            richTextBox_format_1.Select(0, 0);

            // Format RichTextBox2.
            SelectRichText(richTextBox_format_2, "quick");
            richTextBox_format_2.SelectionColor = Color.Red;
            SelectRichText(richTextBox_format_2, "fox");
            richTextBox_format_2.SelectionFont = new Font(richTextBox_format_2.Font, FontStyle.Italic);
            SelectRichText(richTextBox_format_2, "lazy");
            richTextBox_format_2.SelectionBackColor = Color.Yellow;
            richTextBox_format_2.SelectionColor = Color.Brown;
            richTextBox_format_2.Select(0, 0);

            show_richtextbox_tabs();
        }

        // Select the indicated text.
        private void SelectRichText(RichTextBox rch, string target)
        {
            int pos = rch.Text.IndexOf(target);
            if (pos < 0)
            {
                // Not found. Select nothing.
                rch.Select(0, 0);
            }
            else
            {
                // Found the text. Select it.
                rch.Select(pos, target.Length);
            }
        }

        void show_richtextbox_tabs()
        {
            // Set the tabs and enter some text.
            richTextBox2.SelectionTabs = new int[] { 80, 160, 240 };
            richTextBox2.AcceptsTab = true;

            richTextBox2.Text += "顯示RichTextBox中的Tab功能\n\n";
            richTextBox2.Text +=
                "Breakfast\tLunch\tDinner\n" +
                "Coffee\tSoda\tWine\n" +
                "Bagel\tSandwich\tSalad\n" +
                "Fruit\tChips\tTofuburger\n" +
                "\tCookie\tVeggies";
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
            dx = 225;
            dy = 45;

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 14);

            button15.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button24.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button26.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            button27.Location = new Point(x_st + dx * 1, y_st + dy * 12);
            button28.Location = new Point(x_st + dx * 1, y_st + dy * 13);
            button29.Location = new Point(x_st + dx * 1, y_st + dy * 14);

            textBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button40.Location = new Point(x_st + dx * 2, y_st + dy * 10);

            bt_open1.Location = new Point(richTextBox1.Location.X, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_open1.Size.Height * 2 - 5);
            bt_open2.Location = new Point(richTextBox1.Location.X, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_open2.Size.Height);
            bt_font.Location = new Point(richTextBox1.Location.X + bt_open2.Size.Width + 5, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_open2.Size.Height);
            bt_save.Location = new Point(richTextBox1.Location.X + bt_open2.Size.Width + 5 + bt_font.Size.Width + 5, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_open2.Size.Height);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);

            label4.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - 140, richTextBox1.Location.Y + 5);
            label6.Location = new Point(richTextBox1.Location.X + 100, richTextBox1.Location.Y + 5);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.BackColor = Color.Pink;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.BackColor = Color.FromName("Control");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            colorDialog1.AllowFullOpen = true;
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.SelectionBackColor = colorDialog1.Color;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowApply = true;
            fontDialog1.ShowColor = true;
            fontDialog1.ShowEffects = true;
            fontDialog1.ShowHelp = true;
            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.SelectionFont = fontDialog1.Font;
                richTextBox1.SelectionColor = fontDialog1.Color;
                //richTextBox1.SelectionBackColor
            }
        }

        private void button4_Click(object sender, EventArgs e)
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

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "RichTextBox1, lines = " + richTextBox1.Lines.Length.ToString() + "\t";
            richTextBox2.Text += "content : \n";
            int i;
            for (i = 0; i < richTextBox1.Lines.Length; i++)
            {
                richTextBox2.Text += "i = " + i.ToString() + "\t" + richTextBox1.Lines[i].Trim() + "\tlen = \t" + richTextBox1.Lines[i].Trim().Length.ToString() + "\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
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

        private void button7_Click(object sender, EventArgs e)
        {
            //richTextBox2.Text += "There are " + richTextBox1.Lines.Length.ToString() + " lines in richtextBox1\n";
            //Array.Sort(richTextBox1.Lines);   //useless
            string[] temp = richTextBox1.Lines;
            Array.Sort(temp);
            richTextBox1.Lines = temp;
        }

        private void button8_Click(object sender, EventArgs e)
        {
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

        private void button9_Click(object sender, EventArgs e)
        {
            //RichTextBox 全選    TBD
            //((RichTextBox)sender).SelectAll();
            //richTextBox1.SelectAll();
        }

        private void button10_Click(object sender, EventArgs e)
        {
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

        private void button11_Click(object sender, EventArgs e)
        {
            //顯示百分比
            //要using System.Globalization; //for CultureInfo
            int a = 2;
            int b = 3;
            richTextBox1.Text += "顯示一位小數的百分比 :\t\t" + ((double)a / (double)b).ToString("P1", CultureInfo.InvariantCulture) + "\n";
            richTextBox1.Text += "顯示兩位小數的百分比 :\t\t" + ((double)a / (double)b).ToString("P", CultureInfo.InvariantCulture) + "\n";
            richTextBox1.Text += "顯示十位小數的百分比 :\t\t" + ((double)a / (double)b).ToString("P10", CultureInfo.InvariantCulture) + "\n";
        }

        #region 日誌記錄、支援其他執行緒訪問
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
        #endregion

        private void button12_Click(object sender, EventArgs e)
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

        private void button13_Click(object sender, EventArgs e)
        {
            //在方案總管vcs_test_all_01_Richtextbox1按加入/現有項目/選擇 RtfTable.cs, RtfTable.cs要改namespace為vcs_test_all_01_Richtextbox1
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

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
            int j = 0;
            for (int i = 0; i < 256; i++)
            {
                if ((i < 32) || (i > 126))
                    j = '-';
                else
                    j = i;
                richTextBox1.Text += i.ToString() + "\t" + (char)j + "\n";
            }
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
            string str2 = "ABCDE";
            /*  ASCII表
            int j = 0;
            for (int i = 0; i < 256; i++)
            {
                if ((i < 32) || (i > 126))
                    j = '-';
                else
                    j = i;
                richTextBox1.Text += i.ToString() + "\t" + (char)j + "\n";

            }
            */
            for (int i = 0; i < str1.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + str1[i] + "\t" + Convert.ToString(((int)str1[i]), 16) + "\n";
            }
            for (int i = 0; i < str2.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + str2[i] + "\t" + Convert.ToString(((int)str2[i]), 16) + "\n";
            }
            richTextBox1.Text += "\n文字編碼都是Unicode編碼 Unicode (Big-Endian) 	1201 	utf-16BE\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
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

        private void button19_Click(object sender, EventArgs e)
        {
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

        private void button20_Click(object sender, EventArgs e)
        {
            richTextBox1.SaveFile("C:\\______test_files\\MyDocument.rtf", RichTextBoxStreamType.RichText);
        }

        private void button21_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            try
            {
                richTextBox1.LoadFile("C:\\______test_files\\SAMPO(PA63)變頻分離式室外機功能規格書_2014.08.18doc.rtf");
            }
            catch (System.IO.FileNotFoundException)
            {
                MessageBox.Show("File not found!");
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            richTextBox1.Find("壓縮機", RichTextBoxFinds.MatchCase);

            richTextBox1.SelectionFont = new Font("Verdana", 30, FontStyle.Bold);
            richTextBox1.SelectionColor = Color.Red;
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //float oldSize = richTextBox1.SelectionFont.Size;
            float oldSize = richTextBox1.Font.Size;
            float newSize = oldSize + 1;
            FontFamily currentFontFamily;
            Font newFont;
            currentFontFamily = this.richTextBox1.SelectionFont.FontFamily;
            newFont = new Font(currentFontFamily, newSize);
            //this.richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Font = newFont;
        }

        private void button24_Click(object sender, EventArgs e)
        {
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

        private void button25_Click(object sender, EventArgs e)
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

        private void button26_Click(object sender, EventArgs e)
        {
            //選擇設置底線或取消
            Font oldFont = this.richTextBox1.SelectionFont;
            Font newFont;
            if (oldFont.Underline)
                newFont = new Font(oldFont, oldFont.Style & ~FontStyle.Underline);
            else
                newFont = new Font(oldFont, oldFont.Style | FontStyle.Underline);
            this.richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //選擇設置置中或取消
            if (this.richTextBox1.SelectionAlignment == HorizontalAlignment.Center)
                this.richTextBox1.SelectionAlignment = HorizontalAlignment.Left;
            else
                this.richTextBox1.SelectionAlignment = HorizontalAlignment.Center;
            this.richTextBox1.Focus();
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }

        int value1 = 12345;
        double value2 = 123.456;
        double value3 = 1234.5678;

        private void button31_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("D");
        }

        private void button32_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("D8");
        }

        private void button33_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("X");
        }

        private void button34_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("X8");
        }

        private void button35_Click(object sender, EventArgs e)
        {
            textBox1.Text = value2.ToString("F4");
        }

        private void button36_Click(object sender, EventArgs e)
        {
            textBox1.Text = value3.ToString("#0.0");         //格式化，小數點後留1位
        }

        private void button37_Click(object sender, EventArgs e)
        {
            textBox1.Text = value3.ToString("#00000.000");   //格式化，小數點前5位，小數點後留3位四捨五入
        }

        private void button38_Click(object sender, EventArgs e)
        {
            int money = 1234;
            richTextBox1.Text += "\n";
            richTextBox1.Text += money.ToString("C") + "\n";
            richTextBox1.Text += money.ToString("C", CultureInfo.CurrentCulture) + "\n";
            richTextBox1.Text += money.ToString("C", CultureInfo.CreateSpecificCulture("da-DK")) + "\n";
            richTextBox1.Text += money.ToString("C", CultureInfo.CreateSpecificCulture("en-US")) + "\n";
            richTextBox1.Text += money.ToString("C", CultureInfo.CreateSpecificCulture("ja-JP")) + "\n";
            richTextBox1.Text += money.ToString("C", CultureInfo.CreateSpecificCulture("fr-FR")) + "\n";
        }

        private void button39_Click(object sender, EventArgs e)
        {
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

        private void button40_Click(object sender, EventArgs e)
        {
            double pi = Math.PI;
            richTextBox1.Text += "小數點下2位\t" + pi.ToString("n2") + "\n";
            richTextBox1.Text += "小數點下4位\t" + pi.ToString("n4") + "\t四捨五入\n";
            richTextBox1.Text += "小數點下5位\t" + pi.ToString("n5") + "\n";
            richTextBox1.Text += "小數點下10位\t" + pi.ToString("n10") + "\n";
            richTextBox1.Text += "小數點下15位\t" + pi.ToString("n15") + "\n";
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

        private void textBox2_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar < 48 || e.KeyChar > 57) && e.KeyChar != 8 && e.KeyChar != 13)
            {
                e.Handled = true;
            }
            else if (e.KeyChar == 13)
            {
                int textSize = int.Parse(textBox2.Text);
                ApplyTextSize(textSize);

                e.Handled = true;
                this.richTextBox1.Focus();
            }  
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
                richTextBox1.SelectAll();
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            label4.Text = "字數 : " + richTextBox1.TextLength.ToString();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_open1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            //讀取純文字檔到richTextBox裏
            try
            {
                richTextBox1.LoadFile(@"C:\______test_files\article.txt", RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            catch (System.IO.FileNotFoundException)
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
                richTextBox1.Text += System.IO.File.ReadAllText(openFileDialog1.FileName, System.Text.Encoding.Default);
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        private void bt_font_Click(object sender, EventArgs e)
        {
            if (fontDialog1.ShowDialog().Equals(DialogResult.OK))
            {
                // RichTextBox.SelectionFont取得目前選擇的文字，並且將FontDialog所設定的字型結果套入 
                //richTextBox1.SelectionFont = fontDialog1.Font;
                richTextBox1.Font = fontDialog1.Font;
            }
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

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

        private void bt_set_font_size_Click(object sender, EventArgs e)
        {
            int textSize = int.Parse(textBox2.Text);
            ApplyTextSize(textSize);
        }

        //改变字体大小
        private void ApplyTextSize(int textSize)
        {
            FontFamily currentFontFamily;
            Font newFont;
            currentFontFamily = this.richTextBox1.SelectionFont.FontFamily;
            newFont = new Font(currentFontFamily, textSize);
            this.richTextBox1.SelectionFont = newFont;
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        // Display the word under the mouse.
        private void richTextBox1_MouseMove(object sender, MouseEventArgs e)
        {
            label6.Text = WordUnderMouse(richTextBox1, e.X, e.Y);
        }

        // Return the word under the mouse.
        private string WordUnderMouse(RichTextBox rch, int x, int y)
        {
            // Get the character's position.
            int pos = rch.GetCharIndexFromPosition(new Point(x, y));
            if (pos <= 0) return "";

            // Find the start of the word.
            string txt = rch.Text;

            int start_pos;
            for (start_pos = pos; start_pos >= 0; start_pos--)
            {
                // Allow digits, letters, and underscores
                // as part of the word.
                char ch = txt[start_pos];
                if (!char.IsLetterOrDigit(ch) && !(ch == '_')) break;
            }
            start_pos++;

            // Find the end of the word.
            int end_pos;
            for (end_pos = pos; end_pos < txt.Length; end_pos++)
            {
                char ch = txt[end_pos];
                if (!char.IsLetterOrDigit(ch) && !(ch == '_')) break;
            }
            end_pos--;

            // Return the result.
            if (start_pos > end_pos) return "";
            return txt.Substring(start_pos, end_pos - start_pos + 1);
        }


    }
}
