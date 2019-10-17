using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Globalization;//for CultureInfo

namespace vcs_test_all_01_Richtextbox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.BackColor = Color.Pink;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.BackColor = Color.FromName("Control");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            colorDialog1.AllowFullOpen = true;
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.SelectionBackColor = colorDialog1.Color;
            }

        }

        private void button5_Click(object sender, EventArgs e)
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

        private void button6_Click(object sender, EventArgs e)
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

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            richTextBox2.Clear();
        }

        int value1 = 12345;
        double value2 = 123.456;
        double value3 = 1234.5678;

        private void button19_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("D");
        }

        private void button31_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("D8");
        }

        private void button30_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("X");
        }

        private void button28_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("X8");
        }

        private void button27_Click(object sender, EventArgs e)
        {
            textBox1.Text = value2.ToString("F4");
        }

        private void button26_Click(object sender, EventArgs e)
        {
            textBox1.Text = value3.ToString("#0.0");         //格式化，小數點後留1位
        }

        private void button25_Click(object sender, EventArgs e)
        {
            textBox1.Text = value3.ToString("#00000.000");   //格式化，小數點前5位，小數點後留3位四捨五入
        }

        private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
        {
            /*  像是沒需要 本來就有
            //C# richTextBox 按ctrl+a全選
            if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A)
                ((RichTextBox)sender).SelectAll();
            */


            if (tb_search.Text == "")
                richTextBox2.Text += "未輸入搜尋內容\n";
            if (e.KeyCode == Keys.F3)
            {
                richTextBox2.Text += "F3\n";

                // 使用System.Text.RegularExpressions來搜尋指定字串

                string strTxt = richTextBox1.Text;  // 準備要搜尋的來源字串
                string strKey = tb_search.Text;     // 指定字串

                richTextBox2.Text += "strKey = " + strKey + "\tLength = " + strKey.Length.ToString() + "\n";

                //richTextBox2.Text += "strTxt = " + strTxt + "\n";
                //richTextBox2.Text += "strKey = " + strKey + "\n";


                System.Text.RegularExpressions.MatchCollection matches = System.Text.RegularExpressions.Regex.Matches(strTxt, strKey);
                foreach (System.Text.RegularExpressions.Match m in matches)
                {
                    //lstIndex.Items.Add(m.Index);  // 將搜尋結果index顯示於ListBox中
                    richTextBox2.Text += "aaa" + m.Index.ToString() + "\n";
                    richTextBox1.SelectionStart = m.Index;
                    richTextBox1.SelectionLength = strKey.Length;
                }

            }



        }

        private void button13_Click(object sender, EventArgs e)
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

        private void button14_Click(object sender, EventArgs e)
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

        private void button15_Click(object sender, EventArgs e)
        {
            //string test_string = "ABC可否開啟檔案總管？";
            string test_string = "如果用MysonLink，就要燒錄mega上放的韌體。";
            string test_string2 = "ABCDE";
            /*
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
            for (int i = 0; i < test_string.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + test_string[i] + "\t" + Convert.ToString(((int)test_string[i]), 16) + "\n";
            }
            for (int i = 0; i < test_string2.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + test_string2[i] + "\t" + Convert.ToString(((int)test_string2[i]), 16) + "\n";
            }
            richTextBox1.Text += "\n文字編碼都是Unicode編碼\n";

        }

        private void button16_Click(object sender, EventArgs e)
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
            richTextBox1.Text += "\n文字編碼都是Unicode編碼\n";
        }

        private void button32_Click(object sender, EventArgs e)
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

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "RichTextBox1, lines = " + richTextBox1.Lines.Length.ToString() + "\t";
            richTextBox2.Text += "content : \n";
            int i;
            for (i = 0; i < richTextBox1.Lines.Length; i++)
            {
                richTextBox2.Text += "i = " + i.ToString() + "\t" + richTextBox1.Lines[i].Trim() + "\tlen = \t" + richTextBox1.Lines[i].Trim().Length.ToString() + "\n";
            }

        }

        private void button8_Click(object sender, EventArgs e)
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

        private void button9_Click(object sender, EventArgs e)
        {
            //richTextBox2.Text += "There are " + richTextBox1.Lines.Length.ToString() + " lines in richtextBox1\n";
            //Array.Sort(richTextBox1.Lines);   //useless
            string[] temp = richTextBox1.Lines;
            Array.Sort(temp);
            richTextBox1.Lines = temp;

        }

        private void button10_Click(object sender, EventArgs e)
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

        private void button11_Click(object sender, EventArgs e)
        {
            //RichTextBox 全選    TBD
            //((RichTextBox)sender).SelectAll();
            //richTextBox1.SelectAll();
        }

        private void button33_Click(object sender, EventArgs e)
        {
            //double x = 1234567890;
            int x = 12345;
            richTextBox1.Text += "十進位\t" + x.ToString() + "\n";
            richTextBox1.Text += "十六進位\t" + x.ToString("X2") + "\n";
            richTextBox1.Text += "數值格式\t" + x.ToString("N0") + "\n";

            double y = 123.456;
            richTextBox1.Text += "數值格式\t" + y.ToString("N4") + "\n";

        }

        private void button17_Click(object sender, EventArgs e)
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


    }
}
