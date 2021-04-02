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
        string strpath;
        public Form1()
        {
            InitializeComponent();
            strpath = System.Environment.CurrentDirectory;
        }
        static int i = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            this.openFileDialog1.FileName = "";
            this.openFileDialog1.ShowDialog();
            StreamWriter s = new StreamWriter(strpath + "\\HyList.ini", true);
            s.WriteLine(openFileDialog1.FileName);
            s.Flush();
            s.Close();
            ShowWindows(openFileDialog1.FileName); 
        }
        public void ShowWindows(string fileName)
        {
            this.listBox1.Items.Add(fileName);
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            string str = Application.StartupPath;
            StreamReader sr = new StreamReader(str + "\\HyList.ini");
            while (sr.Peek() >= 0)
            {
                string strk=sr.ReadLine();
                if (strk!="")
                    listBox1.Items.Add(strk);    
            }
            sr.Close();
        }

        private void listBox1_DoubleClick(object sender, EventArgs e)
        {
            string strPath=listBox1.Items[listBox1.SelectedIndex].ToString();
            ShowPlay(strPath);
        }

        private void ShowPlay(string Path)
        {
            this.label2.Text = Path;
            this.axWindowsMediaPlayer1.URL =Path;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            i += 1;
            if (i % 2 == 0)
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