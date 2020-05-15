using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory

namespace vcs_tmp_all
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            richTextBox2.Clear();
        }

        private void richTextBox1_SelectionChanged(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
        }


        private void button4_Click(object sender, EventArgs e)
        {

            string pattern1 = "山";
            string pattern2 = "人";
            string pattern3 = "夢中";
            string pattern4 = "三生";

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

        int i = 0;
        private void button1_Click_1(object sender, EventArgs e)
        {
            i = richTextBox1.Find("，", i, RichTextBoxFinds.None);
            richTextBox2.Text += "Found pattern at i = " + i.ToString() + "\n";
            if (i == -1)
                richTextBox2.Text += "己至最後, 重新搜尋\n";

            i++;
        }
    }
}
