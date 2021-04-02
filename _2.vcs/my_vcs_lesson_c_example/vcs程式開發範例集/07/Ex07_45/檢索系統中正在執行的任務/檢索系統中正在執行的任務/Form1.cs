using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;

namespace 檢索系統中正在執行的任務
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text=string.Empty;
            Process[] myProcesses = Process.GetProcesses();
            foreach (Process myProcess in myProcesses)
            {
                if (myProcess.MainWindowTitle.Length > 0)
                    richTextBox1.Text += "任務名：" + myProcess.MainWindowTitle + "\n";
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}