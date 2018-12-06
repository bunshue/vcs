using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace aaaddddd
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int cnt = 0;
            richTextBox1.Text += Directory.GetCurrentDirectory() + "\n";

            DirectoryInfo dir = new DirectoryInfo("c:\\______test_vcs");
            richTextBox1.Text += "addr = " + dir.ToString() + "\n";

            DirectoryInfo[] dddd = dir.GetDirectories();
            richTextBox1.Text += "\nfiles\n";
            cnt = 0;
            foreach (DirectoryInfo d in dddd)
            {
                cnt++;
                richTextBox1.Text += cnt.ToString() + "\t" + d + "\n";
            }

            FileInfo[] aaaa  = dir.GetFiles();
            richTextBox1.Text += "\nfiles\n";
            cnt = 0;
            foreach (FileInfo b in aaaa)
            {
                cnt++;
                richTextBox1.Text += cnt.ToString() + "\t" + b + "\n";
            }
            richTextBox1.Text += "\n";

            DirectoryInfo dir2 = new DirectoryInfo("c:\\______test_vcs\\______test_vcszzzzzznew");
            richTextBox1.Text += "addr2 = " + dir2.ToString() + "\n";
            richTextBox1.Text += "create" + dir2 + "\n";
            dir2.Create();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Size = new Size(1920/2, 1080/2);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Location = new Point(1920/2, 0);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //this.Opacity(30%);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //button4.Right += 30;
            //panel1.Right += 30;
            //pictureBox1.Right += 10;
            //label1.Text = "aaaa";
            label1.Text = richTextBox1.SelectionLength.ToString();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //c:\\______test_vcs\\eula.3084.txt
            richTextBox1.LoadFile("c:\\______test_vcs\\eula.3084.txt", RichTextBoxStreamType.PlainText);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            /*
            string pattern1 = "電話";
            string pattern2 = "硬碟";
            string pattern3 = "目錄";
            string pattern4 = "介紹";
            */
            string pattern1 = "HDMI";
            string pattern2 = "USB";
            string pattern3 = "Matlab";
            string pattern4 = "print";
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

        private void richTextBox1_LocationChanged(object sender, EventArgs e)
        {
            //label1.Text += richTextBox1.
        }
    }
}
