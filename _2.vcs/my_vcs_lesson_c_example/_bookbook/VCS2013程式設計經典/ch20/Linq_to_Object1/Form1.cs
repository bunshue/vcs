using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;

using System.Text;
using System.Windows.Forms;

using System.Linq;  // 使用LINQ查詢必須引用System.Linq命名空間
using System.IO;   // 欲使用檔案處理必須引用System.IO命名空間

namespace Linq_to_Object1
{
    public partial class Form1 : Form
    {
        int[] score = new int[] { 89, 45, 100, 78, 60, 54, 37 };

        public Form1()
        {
            InitializeComponent();
        }

        // 表單載入時執行此事件處理函式
        private void Form1_Load(object sender, EventArgs e)
        {
            listBox1.DataSource = score;
        }

        // 按 [查詢] 鈕執行此事件處理函式
        private void btnSearch_Click(object sender, EventArgs e)
        {
            int sss = 75;
            richTextBox1.Text += "搜尋 大於等於 " + sss.ToString() + " 的成績\n";
            var result = from s in score orderby s ascending where s > sss select s;
            richTextBox1.Text += "共 " + (result.Count()).ToString() + " 筆資料大於等於 " + sss + "\n";
            if (result.Count() > 0)
            {
                richTextBox1.Text += "大於等於 " + sss + " 資料：";
                foreach (var s in result)
                {
                    richTextBox1.Text += s + ", ";
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\_case1";

            try
            {
                DirectoryInfo dir = new DirectoryInfo(foldername);
                FileInfo[] f = dir.GetFiles();
                var myFile = from s in f select s.FullName;
                foreach (var s in myFile)
                {
                    richTextBox1.Text += s + Environment.NewLine;
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text = "路徑有錯";
            }

        }
    }
}
