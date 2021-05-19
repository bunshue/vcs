using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO; // for StreamWriter, StreamReader

namespace vcs_ReadWrite_TXT2
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\__RW\_txt\txt_rw.txt";

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //StreamWriter sw = new StreamWriter(filename); // true 是資料可附加至檔案, open write
            StreamWriter sw = new StreamWriter(filename, true); // true 是資料可附加至檔案 open write append

            int i;
            int len = richTextBox1.Lines.Length;
            //richTextBox2.Text += "lines = " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                //richTextBox2.Text += "i = " + i.ToString() + " : " + richTextBox1.Lines[i] + "\n";
                sw.WriteLine(richTextBox1.Lines[i]); // 寫入一行
            }

            /*
            sw.WriteLine("白日依山盡"); // 寫入一行
            sw.WriteLine("黃河入海流");
            sw.WriteLine("欲窮千里目");
            sw.WriteLine("更上一層樓");
            */
            sw.Close(); // 關閉檔案
        }

        private void button2_Click(object sender, EventArgs e)
        {
            StreamReader sr = new StreamReader(filename); // 開啟檔案

            string str;  // 宣告字串變數

            /* 方法一
            richTextBox2.Clear();   // 文字方塊 先清空
            str = sr.ReadLine(); // 讀出一行
            while (str != null)
            {
                richTextBox2.Text += str + "\n";    //一次讀一行 每一行都要加換行符號
                str = sr.ReadLine();
            }
            */

            //方法二
            richTextBox2.Clear();   // 文字方塊 先清空
            while (sr.Peek() != -1) // 傳回下一個可供使用的字元，但不消耗它
            {
                str = sr.ReadLine(); // 讀出一行 到字串 str
                richTextBox2.Text += str + "\n";    //一次讀一行 每一行都要加換行符號
            }

            sr.Close(); // 關閉檔案
        }
    }
}
