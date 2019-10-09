using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for StreamReader

namespace WindowsFormsApplication1_test_encoding
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                String line;
                //StreamReader sr = new StreamReader(openFileDialog1.FileName, Encoding.Default);	    //Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
                //StreamReader sr = new StreamReader(openFileDialog1.FileName, Encoding.GetEncoding("gb2312"));	    //Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
                StreamReader sr = new StreamReader(openFileDialog1.FileName, Encoding.GetEncoding("gb2312"), true);
                //StreamWriter swAcqflg = new StreamWriter(strFilePath + strFileName, false, System.Text.Encoding.GetEncoding("big5"));

                i = 0;
                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
                    i++;
                    line = sr.ReadLine();            // 讀取文字到 line 變數
                    richTextBox1.Text += "第" + i.ToString() + "行： " + line + "\tlength:" + line.Length.ToString() + "\n";
                    if (line.Length > 0)
                    {
                    }
                }
                sr.Close();


            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }


        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click_1(object sender, EventArgs e)
        {
            String filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, System.Text.Encoding.GetEncoding("big5"));   //指名編碼格式

            sw.WriteLine("ABCDE");

            sw.Close();

            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";

        }

        private void button5_Click_1(object sender, EventArgs e)
        {
            String filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, System.Text.Encoding.GetEncoding("gb2312"));   //指名編碼格式

            sw.WriteLine("ABCDE");

            sw.Close();

            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";

        }

        private void button6_Click_1(object sender, EventArgs e)
        {
            String filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            //StreamWriter sw = new StreamWriter(fs, System.Text.Encoding.GetEncoding("utf-8"));   //指名編碼格式 the same
            StreamWriter sw = new StreamWriter(fs, System.Text.Encoding.GetEncoding("unicode"));   //指名編碼格式

            sw.WriteLine("ABCDE");

            sw.Close();

            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";

        }





    }
}
