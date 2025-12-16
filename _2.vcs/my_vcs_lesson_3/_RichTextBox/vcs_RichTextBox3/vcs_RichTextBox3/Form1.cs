using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_RichTextBox3
{
    public partial class Form1 : Form
    {
        //richTextBox顯示不同顏色文字 ST
        public delegate void LogAppendDelegate(Color color, string text);

        /// <summary>  
        /// 追加顯示文本  
        /// </summary>  
        /// <param name="color">文本顏色</param>  
        /// <param name="text">顯示文本</param>  
        public void LogAppend(Color color, string text)
        {
            richTextBox1.AppendText(" ");
            richTextBox1.SelectionColor = color;
            richTextBox1.AppendText(text);
        }

        /// <summary>  
        /// 顯示錯誤信息
        /// </summary>  
        /// <param name="text"></param>  
        public void LogError(string text)
        {
            LogAppendDelegate la = new LogAppendDelegate(LogAppend);
            richTextBox1.Invoke(la, Color.Red, DateTime.Now.ToString("HH:mm:ss ") + text);
        }

        /// <summary>  
        /// 顯示警告信息  
        /// </summary>  
        /// <param name="text"></param>  
        public void LogWarning(string text)
        {
            LogAppendDelegate la = new LogAppendDelegate(LogAppend);
            richTextBox1.Invoke(la, Color.Violet, DateTime.Now.ToString("HH:mm:ss ") + text);
        }

        /// <summary>  
        /// 顯示一般信息  
        /// </summary>  
        /// <param name="text"></param>  
        public void LogMessage(string text)
        {
            LogAppendDelegate la = new LogAppendDelegate(LogAppend);
            richTextBox1.Invoke(la, Color.Black, DateTime.Now.ToString("HH:mm:ss ") + text);
        }
        //richTextBox顯示不同顏色文字 SP

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

            richTextBox1.Size = new Size(400, 680);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            richTextBox2.Size = new Size(350, 680);
            richTextBox2.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);

            this.Size = new Size(1420, 760);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        private void richTextBox1_LinkClicked(object sender, LinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start(e.LinkText);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            int length = this.richTextBox1.TextLength;
            int selection_start = this.richTextBox1.SelectionStart;
            int selection_length = this.richTextBox1.SelectionLength;

            richTextBox2.Text += "richTextBox1 資料\n";
            richTextBox2.Text += "richTextBox1資料長度 : " + length.ToString() + "\n";
            richTextBox2.Text += "目前游標位置/選取範圍開始位置 : " + selection_start.ToString() + "\n";
            richTextBox2.Text += "選取範圍資料長度 : " + selection_length.ToString() + "\n";

            //還要知道目前游標位置在第幾行第幾點
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Ranks();
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
            richTextBox2.Text += "第" + line.ToString() + "行 第" + column.ToString() + "列\n";
            //this.label1.Text = string.Format("第：{0}行 {1}列", line.ToString(), column.ToString());
        }

        private void button2_Click(object sender, EventArgs e)
        {
            MoveCursorLast();
        }

        private void MoveCursorLast()
        {
            //让文本框获取焦点 
            richTextBox1.Focus();
            //设置光标的位置到文本尾 
            richTextBox1.Select(this.richTextBox1.TextLength, 0);
            //滚动到控件光标处 
            richTextBox1.ScrollToCaret();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string strInsertText = " [Hello] ";
            int start = this.richTextBox1.SelectionStart;
            this.richTextBox1.Text = this.richTextBox1.Text.Insert(start, strInsertText);
            this.richTextBox1.Focus();
            this.richTextBox1.SelectionStart = start;
            this.richTextBox1.SelectionLength = strInsertText.Length;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.LoadFile(@"../../Form1.cs", RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            ColorizeCode(richTextBox1);
        }

        //設置代碼Code高亮顯示成藍色，code高亮顯示
        private static void ColorizeCode(RichTextBox rtb)
        {
            string[] keywords = {"as", "do", "if", "in", "is", "for", "int", "new", "out", "ref", "try", "base",
                                "bool", "byte", "case", "char", "else", "enum", "goto", "lock", "long", "null",
                                "this", "true", "uint", "void", "break", "catch", "class", "const", "event", "false",
                                "fixed", "float", "sbyte", "short", "throw", "ulong", "using", "where", "while",
                                "yield", "double", "extern", "object", "params", "public", "return", "sealed",
                                "sizeof", "static", "string", "struct", "switch", "typeof", "unsafe", "ushort",
                                "checked", "decimal", "default", "finally", "foreach", "partial", "private",
                                "virtual", "abstract", "continue", "delegate", "explicit", "implicit", "internal",
                                "operator", "override", "readonly", "volatile",
                                "interface", "namespace", "protected", "unchecked",
                                "stackalloc",
                                "from", "in", "where", "select", "join", "equals", "let", "on", "group", "by",
                                "into", "orderby", "ascending", "descending", "var"};
            string text = rtb.Text;

            rtb.SelectAll();
            rtb.SelectionColor = rtb.ForeColor;

            foreach (String keyword in keywords)
            {
                int keywordPos = rtb.Find(keyword, RichTextBoxFinds.MatchCase | RichTextBoxFinds.WholeWord);
                while (keywordPos != -1)
                {
                    int commentPos = text.LastIndexOf("//", keywordPos, StringComparison.OrdinalIgnoreCase);
                    int newLinePos = text.LastIndexOf("\n", keywordPos, StringComparison.OrdinalIgnoreCase);
                    int quoteCount = 0;
                    int quotePos = text.IndexOf("\"", newLinePos + 1, keywordPos - newLinePos, StringComparison.OrdinalIgnoreCase);
                    while (quotePos != -1)
                    {
                        quoteCount++;
                        quotePos = text.IndexOf("\"", quotePos + 1, keywordPos - (quotePos + 1), StringComparison.OrdinalIgnoreCase);
                    }

                    if (newLinePos >= commentPos && quoteCount % 2 == 0)
                        rtb.SelectionColor = Color.Blue;

                    keywordPos = rtb.Find(keyword, keywordPos + rtb.SelectionLength, RichTextBoxFinds.MatchCase | RichTextBoxFinds.WholeWord);
                }
            }
            rtb.Select(0, 0);
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //顯示一般信息
            string message = string.Empty;
            message = "顯示一般信息\n";
            LogMessage(message);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //顯示警告信息
            string message = string.Empty;
            message = "顯示警告信息\n";
            LogWarning(message);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //顯示錯誤信息
            string message = string.Empty;
            message = "顯示錯誤信息\n";
            LogError(message);
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //測試RTB內的連結


        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //開啟RTF檔案
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\text.rtf";

            try
            {
                richTextBox1.LoadFile(filename);
            }
            catch (FileNotFoundException)
            {
                MessageBox.Show("沒找到相關文件");
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //另存RTF檔案
            try
            {
                richTextBox1.SaveFile("tmp_aaaa.rtf");
            }
            catch (Exception err)
            {
                MessageBox.Show(err.Message);
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //粗體
            try
            {
                Font oldFont;
                Font newFont;
                oldFont = richTextBox1.SelectionFont;
                if (oldFont.Bold == true)
                {
                    newFont = new Font(oldFont, oldFont.Style & ~FontStyle.Bold);
                }
                else
                {
                    newFont = new Font(oldFont, oldFont.Style | FontStyle.Bold);
                }
                richTextBox1.SelectionFont = newFont;
                this.richTextBox1.Focus();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //斜體
            Font oldFont;
            Font newFont;
            oldFont = richTextBox1.SelectionFont;

            if (richTextBox1.SelectionFont.Italic == true)
            {
                newFont = new Font(oldFont, oldFont.Style & ~FontStyle.Italic);
            }
            else
            {
                newFont = new Font(oldFont, oldFont.Style | FontStyle.Italic);
            }
            richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //居中
            if (this.richTextBox1.SelectionAlignment == HorizontalAlignment.Center)
            {
                richTextBox1.SelectionAlignment = HorizontalAlignment.Left;
            }
            else
            {
                richTextBox1.SelectionAlignment = HorizontalAlignment.Center;
            }
            richTextBox1.Focus();

        }

        private void button17_Click(object sender, EventArgs e)
        {
            //下劃線
            Font oldFont;
            Font newFont;
            oldFont = richTextBox1.SelectionFont;
            if (oldFont.Underline == true)
            {
                newFont = new Font(oldFont, oldFont.Style & ~FontStyle.Underline);
            }
            else
            {
                newFont = new Font(oldFont, oldFont.Style | FontStyle.Underline);
            }
            richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();
        }

        private void button18_Click(object sender, EventArgs e)
        {
            if (richTextBox1.SelectionLength <= 0)
            {
                return;
            }

            Font oldFont;
            Font newFont;
            oldFont = richTextBox1.SelectionFont;

            float font_size = richTextBox1.SelectionFont.Size;
            font_size++;
            newFont = new Font(oldFont.Name, font_size);
            richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();

            /*
            FontFamily currentFontFamily = richTextBox1.SelectionFont.FontFamily;
            Font newFont = new Font(currentFontFamily, font_size);
            richTextBox1.SelectionFont = newFont;
            this.richTextBox1.Focus();
            */
        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {
            int i;
            int len = richTextBox1.Lines.Length;

            richTextBox2.Text += "richTextBox1 共有 : " + len.ToString() + " 行\n";
            for (i = 0; i < len; i++)
            {
                richTextBox2.Text += "i = " + i.ToString() + "\t" + richTextBox1.Lines[i] + "\tlen = " + richTextBox1.Lines[i].Length.ToString() + "\n";
            }

        }

        private void button21_Click(object sender, EventArgs e)
        {
            //check
            int i;
            int j;
            int len = richTextBox1.Lines.Length;

            richTextBox2.Text += "richTextBox1 共有 : " + len.ToString() + " 行\n";
            for (i = 0; i < (len - 1); i++)
            {
                if (richTextBox1.Lines[i].Length <= 0)
                    continue;

                for (j = (i + 1); j < len; j++)
                {
                    if (richTextBox1.Lines[j].Length <= 0)
                        continue;

                    if (richTextBox1.Lines[i].Trim().Contains(richTextBox1.Lines[j].Trim()))
                    {
                        richTextBox2.Text += "第 " + i.ToString() + " 行 包含 第 " + j.ToString() + " 行\n";
                    }
                    else if (richTextBox1.Lines[j].Trim().Contains(richTextBox1.Lines[i].Trim()))
                    {
                        richTextBox2.Text += "第 " + j.ToString() + " 行 包含 第 " + i.ToString() + " 行\n";
                    }
                }
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //Richtextbox 的比例因子 ZoomFactor
            richTextBox1.ZoomFactor = (float)3.2;
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //Richtextbox 的比例因子 ZoomFactor
            richTextBox1.ZoomFactor = (float)1.0;
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //字體
            //Font f = new Font("標楷體", 20F, FontStyle.Regular, GraphicsUnit.Point);
            Font f = new Font("標楷體", 20F, FontStyle.Bold, GraphicsUnit.Point);      //粗體

            richTextBox1.Font = f;
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

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            //richTextBox2.Text += "A ";
        }

        private void richTextBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            //抓 Ctrl + R
            byte asc = Convert.ToByte(e.KeyChar);
            //richTextBox2.Text += "|  " + e.KeyChar.ToString() + "  |  " + asc.ToString() + "  |  " + asc.ToString("X2") + "  |\n";
            if (asc == 18)  //ctrl + A = 1, ctrl + B = 2, ..., ctrl + R = 18
            {
                e.Handled = true;
                richTextBox2.Text += "你按了 ctrl + R\n";
            }

            //抓 Enter 鍵
            if (e.KeyChar == (char)Keys.Enter)
            {
                e.Handled = true;
                richTextBox2.Text += "你按了 Enter\n";
            }
        }
    }
}
