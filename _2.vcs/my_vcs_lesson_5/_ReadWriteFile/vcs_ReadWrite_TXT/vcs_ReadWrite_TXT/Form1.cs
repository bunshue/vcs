using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ReadWrite_TXT
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, System.Text.Encoding.GetEncoding("big5"));   //指名編碼格式

            richTextBox2.Text += "RichTextBox1, lines = " + richTextBox1.Lines.Length.ToString() + "\t";
            richTextBox2.Text += "content : \n";
            int i;

            for (i = 0; i < richTextBox1.Lines.Length; i++)
            {
                richTextBox2.Text += "i = " + i.ToString() + "\t" + richTextBox1.Lines[i].Trim() + "\tlen = \t" + richTextBox1.Lines[i].Trim().Length.ToString() + "\n";
            }
            
            for (i = 0; i < richTextBox1.Lines.Length; i++)
            {
                sw.WriteLine(richTextBox1.Lines[i]);
            }

            sw.Close();

            richTextBox2.Text += "\n存檔完成, 檔名 : " + filename + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                richTextBox1.LoadFile("pipa.txt", RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            catch (System.IO.FileNotFoundException)
            {
                MessageBox.Show("找不到檔案");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //法一
            // 運用 ReadAllText 方法 (String, Encoding) ，其中 Encoding 針對您txt檔案的編碼做變更，讀出的資料才不會有亂碼
            //richTextBox1.Text = System.IO.File.ReadAllText("pipa.txt", System.Text.Encoding.Default);

            //法二
            //讀取檔案
            string y = File.ReadAllText("pipa.txt", System.Text.Encoding.Default);
            richTextBox1.Text += "檔案內容 : " + y + "\n";
            richTextBox1.Text += "長度：" + y.Length.ToString() + "\n";



        }
    }
}
