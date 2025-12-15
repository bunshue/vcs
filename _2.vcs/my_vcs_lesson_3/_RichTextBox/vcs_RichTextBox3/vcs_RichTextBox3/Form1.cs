using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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


            richTextBox2.Size = new Size(470, 325);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);
        }


        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        private void button6_Click(object sender, EventArgs e)
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

        private void button7_Click(object sender, EventArgs e)
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

        private void button8_Click(object sender, EventArgs e)
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

        private void button2_Click(object sender, EventArgs e)
        {
            string strInsertText = " [Hello] ";
            int start = this.richTextBox1.SelectionStart;
            this.richTextBox1.Text = this.richTextBox1.Text.Insert(start, strInsertText);
            this.richTextBox1.Focus();
            this.richTextBox1.SelectionStart = start;
            this.richTextBox1.SelectionLength = strInsertText.Length;
        }

        private void button3_Click(object sender, EventArgs e)
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

        private void button4_Click(object sender, EventArgs e)
        {
            //顯示一般信息
            string message = string.Empty;
            message = "顯示一般信息\n";
            LogMessage(message);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //顯示警告信息
            string message = string.Empty;
            message = "顯示警告信息\n";
            LogWarning(message);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //顯示錯誤信息
            string message = string.Empty;
            message = "顯示錯誤信息\n";
            LogError(message);
        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }
    }
}

