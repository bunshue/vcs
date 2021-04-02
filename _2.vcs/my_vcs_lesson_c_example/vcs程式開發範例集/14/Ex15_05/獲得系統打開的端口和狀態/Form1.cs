using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;
using System.IO;
namespace 獲得系統打開的端口和狀態
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Process p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.Start();
            p.StandardInput.WriteLine(@"netstat -a -n > c:\port.txt");
           
           
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.richTextBox1.Text = "";
            try
            {
                string path = @"c:\port.txt";
                using (StreamReader sr = new StreamReader(path))
                {
                    while (sr.Peek() >= 0)
                    {
                        this.richTextBox1.Text += sr.ReadLine()+"\r\n";
                    }
                }
            }
            catch (Exception hy)
            {
                MessageBox.Show(hy.Message);
            }

        }
    }
}