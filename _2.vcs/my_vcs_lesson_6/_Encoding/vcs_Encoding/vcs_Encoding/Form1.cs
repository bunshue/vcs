using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Encoding
{
    public partial class Form1 : Form
    {
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
            dx = 180;
            dy = 80;

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

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            int i;
            int len;

            string initial_string = "ABC密碼錯誤";
            richTextBox1.Text += "原資料 : " + initial_string + "\t";

            len = initial_string.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += initial_string[i].ToString() + "\n";
            }

            byte[] charData;

            richTextBox1.Text += "ASCII編碼 :\t";
            charData = Encoding.ASCII.GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "Default 編碼 = Big5編碼\t";
            charData = Encoding.Default.GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "Big5編碼 :\t";
            charData = Encoding.GetEncoding("big5").GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "gb2312編碼 :\t";
            charData = Encoding.GetEncoding("gb2312").GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "Unicode編碼 = utf-16 編碼\t";
            charData = Encoding.GetEncoding("unicode").GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "utf-16 編碼 :\t";
            charData = Encoding.GetEncoding("utf-16").GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "UTF8 編碼 :\t";
            charData = Encoding.UTF8.GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

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

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

    }
}
