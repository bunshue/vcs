using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RichTextBox4_Find2
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files1\__RW\_txt\poetry.txt";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //StreamReader UTF_8Reader = new StreamReader(filename, Encoding.Default);//實現一個 TextReader，使其以一種特定的編碼從字節流中讀取字符。
            //richTextBox1.Text = UTF_8Reader.ReadToEnd();//在RichTextBox控件中顯示從字節流中讀取的字符

            richTextBox1.LoadFile(filename, RichTextBoxStreamType.PlainText);//從指定的位置加載TxT文件
        }

        //一次描紅一個
        private int search_position = 0;//定義一個int型的標識符
        private void button1_Click(object sender, EventArgs e)
        {
            if ((search_position = richTextBox1.Text.IndexOf(textBox1.Text, search_position)) == -1)//當文件中不存在要搜索的關鍵字時
            {
                MessageBox.Show("沒有要查找的結果", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出對應的信息提示
                search_position = 0;//重新為flag賦值
            }
            else//當在文件中存在對應的關鍵字時
            {
                richTextBox1.Select(search_position, textBox1.Text.Length);//在RichTextBox控件中搜索關鍵字
                search_position = search_position + textBox1.Text.Length;//遞增標識查詢關鍵字的初始長度
                richTextBox1.SelectionColor = Color.Red;//設定關鍵字為紅色
            }
            this.Text = search_position.ToString();


        }

        //一次描紅全部
        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            search_position = 0;
            Form1_Load(sender, e);



        }



    }
}
