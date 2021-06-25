using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace InvolveMemorizePlayImplement
{
    public partial class Form1 : Form
    {
        static int index = 0;
        string filename = @"C:\______test_files\_mp3\list.m3u";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀取檔案 : " + filename + "\n";
            StreamReader sr = new StreamReader(filename, Encoding.Default);
            while (sr.Peek() >= 0)
            {
                string strk = sr.ReadLine();
                if (strk != "")
                {
                    richTextBox1.Text += "加入項目 : " + strk + "\n";
                    listBox1.Items.Add(strk);
                }
            }
            sr.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.openFileDialog1.FileName = "";
            this.openFileDialog1.ShowDialog();
            StreamWriter s = new StreamWriter(filename, true);
            s.WriteLine(openFileDialog1.FileName);
            s.Flush();
            s.Close();
            ShowWindows(openFileDialog1.FileName);
        }

        public void ShowWindows(string fileName)
        {
            this.listBox1.Items.Add(fileName);
        }

        private void listBox1_DoubleClick(object sender, EventArgs e)
        {
            string strPath = listBox1.Items[listBox1.SelectedIndex].ToString();
            ShowPlay(strPath);
        }

        private void ShowPlay(string Path)
        {
            this.label2.Text = Path;
            this.axWindowsMediaPlayer1.URL = Path;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            index += 1;
            if (index % 2 == 0)
            {
                this.axWindowsMediaPlayer1.Ctlcontrols.play();
            }
            else
            {
                this.axWindowsMediaPlayer1.Ctlcontrols.pause();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ShowPlay(openFileDialog1.FileName);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.Ctlcontrols.stop();
        }
    }
}

