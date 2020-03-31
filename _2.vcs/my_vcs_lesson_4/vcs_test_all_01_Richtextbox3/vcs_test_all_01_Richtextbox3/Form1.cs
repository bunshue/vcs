using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_01_Richtextbox3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            try
            {
                richTextBox1.LoadFile(@"C:\______test_files\article.txt", RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            catch (System.IO.FileNotFoundException)
            {
                MessageBox.Show("File not found!");
            }  
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            try
            {
                richTextBox1.SaveFile(filename, RichTextBoxStreamType.PlainText);    //將richTextBox的資料寫入到指定的文字檔
                richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";
            }
            catch (System.Exception err)
            {
                MessageBox.Show(err.Message);
            }  
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
            MoveCurorLast();
        }

        private void MoveCurorLast()
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


    }
}
