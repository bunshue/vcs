using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RichTextBox4_Find
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        public int FindMyText(string text, int start)
        {
            // Initialize the return value to false by default.
            int returnValue = -1;

            // Ensure that a search string and a valid starting point are specified.
            if (text.Length > 0 && start >= 0)
            {
                // Obtain the location of the search string in richTextBox1.
                int indexToText = richTextBox1.Find(text, start, RichTextBoxFinds.MatchCase);
                // Determine whether the text was found in richTextBox1.
                if (indexToText >= 0)
                {
                    // Return the index to the specified search text.
                    returnValue = indexToText;
                }
            }
            return returnValue;
        }

        public int FindMyText(string text, int start, int end)
        {
            // Initialize the return value to false by default.
            int returnValue = -1;

            // Ensure that a search string and a valid starting point are specified.
            if (text.Length > 0 && start >= 0)
            {
                // Ensure that a valid ending value is provided.
                if (end > start || end == -1)
                {
                    // Obtain the location of the search string in richTextBox1.
                    int indexToText = richTextBox1.Find(text, start, end, RichTextBoxFinds.MatchCase);
                    // Determine whether the text was found in richTextBox1.
                    if (indexToText >= 0)
                    {
                        // Return the index to the specified search text.
                        returnValue = indexToText;
                    }
                }
            }
            return returnValue;
        }

        public bool FindMyText(string text)
        {
            // Initialize the return value to false by default.
            bool returnValue = false;

            // Ensure a search string has been specified.
            if (text.Length > 0)
            {
                // Obtain the location of the search string in richTextBox1.
                int indexToText = richTextBox1.Find(text);
                richTextBox2.Text += "index = " + indexToText.ToString() + "\n";
                // Determine whether the text was found in richTextBox1.
                if (indexToText >= 0)
                {
                    returnValue = true;
                }
            }

            return returnValue;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int match = 0;
            int position = 0;

            string str = textBox1.Text;

            while (true)
            {
                position = FindMyText(str, position);

                if (position == -1)
                {
                    richTextBox2.Text += "搜尋到底了, 搜尋字串\t" + str + "\t共出現 " + match.ToString() + " 次\n";
                    break;
                }
                else
                {
                    match++;
                    richTextBox2.Text += "position = " + position.ToString() + "\n";

                    //反白
                    richTextBox1.SelectionStart = position;
                    richTextBox1.SelectionLength = str.Length;
                    richTextBox1.SelectionBackColor = Color.Blue;

                    position++;
                }
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            int match = 0;
            int position = 0;

            string str = textBox1.Text;

            while (true)
            {
                position = FindMyText(str, position, richTextBox1.Text.Length / 2);

                if (position == -1)
                {
                    richTextBox2.Text += "搜尋到底了, 搜尋字串\t" + str + "\t共出現 " + match.ToString() + " 次\n";
                    break;
                }
                else
                {
                    match++;
                    richTextBox2.Text += "position = " + position.ToString() + "\n";

                    //反白
                    richTextBox1.SelectionStart = position;
                    richTextBox1.SelectionLength = str.Length;
                    richTextBox1.SelectionBackColor = Color.Blue;

                    position++;
                }
            }

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //恢復反白
            richTextBox1.SelectionStart = 0;
            richTextBox1.SelectionLength = richTextBox1.Text.Length;
            richTextBox1.SelectionBackColor = Color.White;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string str = textBox1.Text;

            bool flag_found = false;

            flag_found = FindMyText(str);

            if (flag_found == true)
                richTextBox2.Text += "有找到字串\t" + str + "\n";
            else
                richTextBox2.Text += "找不到字串\t" + str + "\n";

        }

        private void button11_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            //讀取純文字檔到richTextBox裏
            try
            {
                richTextBox1.LoadFile(@"C:\______test_files1\article.txt", RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            catch (System.IO.FileNotFoundException)
            {
                richTextBox2.Text += "找不到檔案\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int start = 0;
            String pattern1 = "酒";
            String pattern2 = "客";
            String pattern3 = "東";

            richTextBox2.Text += "搜尋字串:\t" + pattern1 + "\t" + pattern2 + "\t" + pattern3 + "\n";

            int end1 = richTextBox1.Text.LastIndexOf(pattern1);
            int end2 = richTextBox1.Text.LastIndexOf(pattern2);
            int end3 = richTextBox1.Text.LastIndexOf(pattern3);

            richTextBox1.SelectAll();
            richTextBox1.SelectionBackColor = Color.White;

            richTextBox2.Text += "end1 = " + end1.ToString() + "\n";
            richTextBox2.Text += "end2 = " + end2.ToString() + "\n";
            richTextBox2.Text += "end3 = " + end3.ToString() + "\n";
            richTextBox2.Text += "richTextBox len = " + richTextBox1.TextLength.ToString() + "\n";

            start = 0;
            while (start < end1)
            {
                richTextBox2.Text += "start = " + start.ToString() + "\n";

                richTextBox1.Find(pattern1, start, richTextBox1.TextLength, RichTextBoxFinds.MatchCase);

                richTextBox1.SelectionBackColor = Color.Yellow;

                start = richTextBox1.Text.IndexOf(pattern1, start) + 1;
            }

            start = 0;
            while (start < end2)
            {
                richTextBox2.Text += "---start = " + start.ToString() + "\n";
                richTextBox1.Find(pattern2, start, richTextBox1.TextLength, RichTextBoxFinds.MatchCase);

                richTextBox1.SelectionBackColor = Color.Yellow;

                start = richTextBox1.Text.IndexOf(pattern2, start) + 1;
            }


            start = 0;
            while (start < end3)
            {
                richTextBox1.Find(pattern3, start, richTextBox1.TextLength, RichTextBoxFinds.MatchCase);

                richTextBox1.SelectionBackColor = Color.Yellow;

                start = richTextBox1.Text.IndexOf(pattern3, start) + 1;
            }

        }

        int i = 0;
        private void button5_Click(object sender, EventArgs e)
        {
            string search_pattern = textBox1.Text;
            richTextBox2.Text += "搜尋 " + search_pattern + "\t";
            i = richTextBox1.Find(search_pattern, i, RichTextBoxFinds.None);
            if (i == -1)
            {
                richTextBox2.Text += "己至最後, 重新搜尋\n";
            }
            else
            {
                richTextBox2.Text += "找到, 在 i = " + i.ToString() + "\n";
                richTextBox1.SelectionStart = i;
                richTextBox1.SelectionLength = search_pattern.Length;
                richTextBox1.SelectionBackColor = Color.Red;
            }
            i++;


        }

        private void button12_Click(object sender, EventArgs e)
        {
            string pattern1 = "風";
            string pattern2 = "雨";
            string pattern3 = "山";
            string pattern4 = "人";

            richTextBox2.Text += "搜尋關鍵字\n";
            richTextBox2.Text += "pattern1 :\t" + pattern1 + "\n";
            richTextBox2.Text += "pattern2 :\t" + pattern2 + "\n";
            richTextBox2.Text += "pattern3 :\t" + pattern3 + "\n";
            richTextBox2.Text += "pattern4 :\t" + pattern4 + "\n";

            int position1;
            int position2;
            int position3;
            int position4;
            position1 = richTextBox1.Find(pattern1);
            position2 = richTextBox1.Find(pattern2);
            position3 = richTextBox1.Find(pattern3);
            position4 = richTextBox1.Find(pattern4);


            richTextBox2.Text += "找到 pattern1 :\t" + pattern1 + "\t在\t" + position1.ToString() + "\n";
            richTextBox2.Text += "找到 pattern2 :\t" + pattern2 + "\t在\t" + position2.ToString() + "\n";
            richTextBox2.Text += "找到 pattern3 :\t" + pattern3 + "\t在\t" + position3.ToString() + "\n";
            richTextBox2.Text += "找到 pattern4 :\t" + pattern4 + "\t在\t" + position4.ToString() + "\n";

        }

        private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
        {
            /*  像是沒需要 本來就有
            //C# richTextBox 按ctrl+a全選
            if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A)
            ((RichTextBox)sender).SelectAll();
            */

            if (textBox1.Text == "")
                richTextBox2.Text += "未輸入搜尋內容\n";
            if (e.KeyCode == Keys.F3)
            {
                richTextBox2.Text += "F3\n";

                // 使用System.Text.RegularExpressions來搜尋指定字串

                string strTxt = richTextBox1.Text;  // 準備要搜尋的來源字串
                string search_pattern = textBox1.Text; //欲搜尋的字串

                richTextBox2.Text += "搜尋字串 : " + search_pattern + "\tLength = " + search_pattern.Length.ToString() + "\n";

                System.Text.RegularExpressions.MatchCollection matches = System.Text.RegularExpressions.Regex.Matches(strTxt, search_pattern);

                foreach (System.Text.RegularExpressions.Match m in matches)
                {
                    //lstIndex.Items.Add(m.Index);  // 將搜尋結果index顯示於ListBox中
                    richTextBox2.Text += "找到, 在 m = " + m.Index.ToString() + "\n";
                    richTextBox1.SelectionStart = m.Index;
                    richTextBox1.SelectionLength = search_pattern.Length;
                    richTextBox1.SelectionBackColor = Color.Red;
                }
            }

        }
    }
}
