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

        private void button5_Click(object sender, EventArgs e)
        {
            int cnt = 0;
            richTextBox1.Text += Directory.GetCurrentDirectory() + "\n";

            DirectoryInfo dir = new DirectoryInfo("c:\\______test_files");
            richTextBox1.Text += "addr = " + dir.ToString() + "\n";

            DirectoryInfo[] dddd = dir.GetDirectories();
            richTextBox1.Text += "\nfiles\n";
            cnt = 0;
            foreach (DirectoryInfo d in dddd)
            {
                cnt++;
                richTextBox1.Text += cnt.ToString() + "\t" + d + "\n";
            }

            FileInfo[] aaaa = dir.GetFiles();
            richTextBox1.Text += "\nfiles\n";
            cnt = 0;
            foreach (FileInfo b in aaaa)
            {
                cnt++;
                richTextBox1.Text += cnt.ToString() + "\t" + b + "\n";
            }
            richTextBox1.Text += "\n";


        }

        private void button4_Click(object sender, EventArgs e)
        {
            string pattern1 = "山";
            string pattern2 = "人";
            string pattern3 = "夢中";
            string pattern4 = "三生";
            int position1;
            int position2;
            int position3;
            int position4;
            position1 = richTextBox1.Find(pattern1);
            position2 = richTextBox1.Find(pattern2);
            position3 = richTextBox1.Find(pattern3);
            position4 = richTextBox1.Find(pattern4);

            richTextBox2.Text += position1.ToString() + " " +
                position2.ToString() + " " +
                position3.ToString() + " " +
                position4.ToString() + "\n";

        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
            int i;
            for (i = 0; i < 256; i++)
            {
                richTextBox2.Text += i.ToString() + " ";
            }
            File.WriteAllText(@"C:\______test_vcs\\my_text_file.txt", richTextBox2.Text, Encoding.Default);
            richTextBox2.Text += "\n已存檔C:\\______test_vcs\\my_text_file.txt\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
            int i;
            byte[] aaaaa = new byte[256];
            for (i = 0; i < 256; i++)
            {
                //richTextBo21.Text += i.ToString();
                aaaaa[i] = (byte)i;
            }
            File.WriteAllBytes(@"C:\______test_vcs\\my_bin_file.bin", aaaaa);
            richTextBox2.Text += "已存檔C:\\______test_vcs\\my_bin_file.bin\n";
        }


    }
}
