using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_01_Richtextbox2
{
    public partial class Form1 : Form
    {
        /*

        /// <summary>获取 Form_Mxdr.RichTextBox<para>　<para>
        /// 获取 RichTextBox 的读写操作权限</para></para> </summary>
        public RichTextBox RichTxtBox
        {
            get { return this.txtInput; }
            set { this.txtInput = value; }
        }
       */

        public Form1()
        {
            InitializeComponent();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            start = 0;
            sum = 0;

            richTextBox1.Clear();

            try
            {
                richTextBox1.LoadFile(@"C:\______test_files\article.txt", RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            catch (System.IO.FileNotFoundException)
            {
                richTextBox2.Text += "找不到檔案\n";
            }

            button1.Enabled = true;
            button2.Enabled = true;
            button3.Enabled = true;

            button4.Enabled = true;

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button1.Enabled = false;
            button2.Enabled = false;
            button3.Enabled = false;

            button4.Enabled = false;
            radioButton2.Checked = true;

            label3.Text = "";
            label4.Text = "";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        #region ***********全局变量*************
        bool flag_search_pattern_start = false;
        int start = 0;
        int sum = 0;
        #endregion

        #region =★*★*★=    〖查找替换〗 函数     =★*★*★=
        /// <summary>向上查找指定字符 或 字符串 (不区分大小写)<para>　<para>
        /// 参数1(rbox):内容文本框,指定为 RichTextBox 文本框类型<para>
        /// 参数2(str):用户指定要查找的字符串</para>
        /// </para></para> </summary>
        /// <param name="rbox">内容文本框,指定为 RichTextBox 文本框类型</param>
        /// <param name="str">用户指定要查找的字符串</param>
        private void FindUp(RichTextBox rbox, string str)
        {
            richTextBox2.Text += "FindUp\n";
            int rboxL = rbox.SelectionStart;
            int index = rbox.Find(str, 0, rboxL, RichTextBoxFinds.Reverse);

            richTextBox2.Text += "index = " + index.ToString() + "\t" +
    "rboxL = " + rboxL.ToString() + "\t" +
    "sum = " + sum.ToString() + "\n";

            if (index > -1)
            {
                rbox.SelectionStart = index;
                rbox.SelectionLength = str.Length;
                sum++;
                rbox.Focus();
            }
            else if (index < 0)
            {
                seeks(str);

                //richTextBox2.Text += "搜尋到底了, sum = " + sum.ToString() + "\n";

                if ((checkBox3.Checked == true) && (sum > 0))
                {
                    sum = 0;
                    richTextBox2.Text += "搜尋到底了, 再搜尋\n";
                    //如果还想再找一遍,添加下面这句
                    rbox.SelectionStart = rbox.Text.Length;
                    FindUp(rbox, str);
                }
                else
                    sum = 0;
            }
        }

        /// <summary>向下查找指定字符 或 字符串 (不区分大小写)<para>　<para>
        /// 参数1(rbox):内容文本框,指定为 RichTextBox 文本框类型
        /// <para>参数2(str):用户指定要查找的字符串</para>
        /// </para></para> </summary>
        /// <param name="rbox">内容文本框,指定为 RichTextBox 文本框类型</param>
        /// <param name="str">用户指定要查找的字符串</param>
        private void FindDown(RichTextBox rbox, string str)
        {
            richTextBox2.Text += "FindDown\n";
            int rboxL = rbox.Text.Length;

            richTextBox2.Text += "start = " + start.ToString() + "\t" +
                "rboxL = " + rboxL.ToString() + "\t" +
                "sum = " + sum.ToString() + "\n";

            if (start < rboxL)
            {
                start = rbox.Find(str, start, RichTextBoxFinds.None);
                int los = rbox.SelectionStart + str.Length;
                richTextBox2.Text += "1111 start = " + start.ToString() + "\tlos = " + los.ToString() + "\n";

                if ((start < 0) || (start > rboxL))
                {
                    //richTextBox2.Text += "cannot find pattern\n";
                    this.seeks(str);

                    if (checkBox3.Checked == true)
                    {
                        richTextBox2.Text += "搜尋到底了, 再搜尋\n";
                        start = 0;
                        FindDown(rbox, str);
                    }
                    else
                    {
                        richTextBox2.Text += "搜尋到底了\n";
                        start = los;
                    }
                    sum = 0;
                }
                else if (start == rboxL || start < 0)
                {
                    richTextBox2.Text += "1111b\n";
                    this.seeks(str);
                    start = los;
                    sum = 0;
                }
                else
                {
                    richTextBox2.Text += "1111c\n";
                    sum++;
                    start = los;
                    rbox.Focus();
                }
            }
            else if (start == rboxL || start < 0)
            {
                richTextBox2.Text += "2222\n";
                int los = rbox.SelectionStart + str.Length;
                this.seeks(str);
                start = los;
                sum = 0;
            }
            else
            {
                richTextBox2.Text += "3333\n";
                int los = rbox.SelectionStart + str.Length;
                this.seeks(str);
                start = los;
                sum = 0;
            }
        }


        /// <summary>向下查找指定字符 或 字符串 (限定大小写)<para>　<para>
        /// 参数1(rbox):内容文本框,指定为 RichTextBox 文本框类型
        /// <para>参数2(str):用户指定要查找的字符串</para>
        /// </para></para> </summary>
        /// <param name="rbox">内容文本框,指定为 RichTextBox 文本框类型</param>
        /// <param name="str">用户指定要查找的字符串</param>
        private void FindDownM(RichTextBox rbox, string str)
        {
            richTextBox2.Text += "FindDownM\n";
            int rboxL = rbox.Text.Length;

            if (start < rboxL)
            {
                start = rbox.Find(str, start, RichTextBoxFinds.MatchCase);
                int los = rbox.SelectionStart + str.Length;


                if ((start < 0) || (start > rboxL))
                {
                    this.seeks(str);
                    start = los;
                    sum = 0;
                }
                else if (start == rboxL || start < 0)
                {
                    this.seeks(str);
                    start = los;
                    sum = 0;
                }
                else
                {
                    sum++;
                    start = los;
                    rbox.Focus();
                }
            }
            else if (start == rboxL || start < 0)
            {
                int los = rbox.SelectionStart + str.Length;
                this.seeks(str);
                start = los;
                sum = 0;
            }
            else
            {
                int los = rbox.SelectionStart + str.Length;
                this.seeks(str);
                start = los;
                sum = 0;
            }
        }


        /// <summary> 消息提示,提示用户查找结果<para>　<para>
        /// 参数1(str):用户指定要查找的字符串</para></para> </summary>
        /// <param name="str">用户指定要查找的字符串</param>
        private void seeks(string str)
        {
            if (sum != 0)
            {
                richTextBox2.Text += "已結束搜尋文件, 總共找到 " + sum.ToString() + " 筆資料\t\"" + str + "\"\n";
            }
            else
            {
                richTextBox2.Text += "搜尋的字串找不到!\t\"" + str + "\"\n";
            }
        }


        /// <summary> 全部替换指定〖字符 或 字符串〗<para>　<para>
        /// 参数1(rbox):要替换内容的文本框,指定为 RichTextBox 文本框类型<para>
        /// 参数2(str0):指定〖原有〗的内容(查找内容)</para><para>
        /// 参数3(str1):指定〖新〗的内容(替换内容)</para></para></para> </summary>
        /// <param name="rbox">要替换内容的文本框,指定为 RichTextBox 文本框类型</param>
        /// <param name="str0">指定〖原有〗的内容(查找内容)</param>
        /// <param name="str1">指定〖新〗的内容(替换内容)</param>
        private void ReplaceAll(RichTextBox rbox, string str0, string str1)
        {
            richTextBox2.Text += "ReplaceAll\n";
            rbox.Text = rbox.Text.Replace(str0, str1);
        }


        /// <summary>单次替换字符或字符串<para>　<para>
        /// 参数1(str0):查找的内容<para>
        /// 参数2(str1):要替换的内容
        /// </para> </para></para> </summary>
        /// <param name="str0">查找的内容</param>
        /// <param name="str1">要替换的内容</param>
        private void Replace(string str0, string str1)
        {
            //Replace 把所有的 "蘇子換成 "蘇東坡
            richTextBox2.Text += "Replace 把所有的 \"" + str0 + "\" 換成 \"" + str1 + "\"\n";
            //Form_Mxdr f1 = (Form_Mxdr)this.Owner;
            RichTextBox rbox = this.richTextBox1;
            rbox.SelectionLength = str0.Length;
            rbox.SelectedText = str1;//textBox2中放要替换的字符
        }
        #endregion

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_search_pattern_start == false)
            {
                flag_search_pattern_start = true;
                start = this.richTextBox1.SelectionStart;
                richTextBox2.Text += "目前游標位置 : " + start.ToString() + "\n";
            }

            RichTextBox rbox = this.richTextBox1;
            string str = this.textBox1.Text;
            if (this.checkBox1.Checked) //是否区分大小写
            {
                this.FindDownM(rbox, str);
            }
            else
            {
                if (this.radioButton2.Checked)
                {
                    this.FindDown(rbox, str);
                }
                else
                {
                    this.FindUp(rbox, str);
                }
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            string str0 = this.textBox1.Text, str1 = this.textBox2.Text;
            this.Replace(str0, str1);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Form_Mxdr f1 = (Form_Mxdr)this.Owner;
            RichTextBox rbox = this.richTextBox1;
            string str0 = textBox1.Text, str1 = textBox2.Text;
            this.ReplaceAll(rbox, str0, str1);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            label3.Text = "文字總長: " + richTextBox1.TextLength.ToString();
        }

        private void richTextBox1_SelectionChanged(object sender, EventArgs e)
        {
            if (richTextBox1.SelectionLength > 0)
                label4.Text = "選取長度: " + richTextBox1.SelectionLength.ToString();
            else
                label4.Text = "";

            /*   暫不改變字體
            if (richTextBox1.SelectionLength == 0)
            {
                // 將RichTextBox中選取的文字，透過 FontFamily 類別 
                // 同時設定 粗體文字 FontStyle.Bold 與 斜體文字 FontStyle.Italic 
                //Font MyFont = new Font(new FontFamily("新細明體"), 12, FontStyle.Bold | FontStyle.Italic);
                Font MyFont = new Font(new FontFamily("新細明體"), 12, FontStyle.Regular);
                //this.richTextBox1.Font = DefaultFont; fail
                this.richTextBox1.Font = MyFont;
            }
            else
            {
                // 將RichTextBox中選取的文字，透過 FontFamily 類別 
                // 同時設定 粗體文字 FontStyle.Bold 與 斜體文字 FontStyle.Italic 
                Font MyFont = new Font(new FontFamily("標楷體"), 16, FontStyle.Bold | FontStyle.Italic);
                //this.richTextBox1.Font = DefaultFont; fail
                this.richTextBox1.SelectionFont = MyFont;
            }
            */
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (richTextBox1.Focused == false)
            {
                //richTextBox2.Text += "F ";
                richTextBox1.Focus();
            }
        }

        private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (Control.ModifierKeys == Keys.Control)
            {
                if (e.KeyCode == Keys.F)
                {
                    richTextBox2.Text += "你按了 ctrl + F\n";
                }


            }

        }



 




    }
}
