using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;

namespace vcs_Process6_TabTip
{
    public partial class Form1 : Form
    {
        string keyboardPath = @"C:\Program Files\Common Files\Microsoft Shared\ink\TabTip.exe";
        Process myProcess = new Process();
        int focus_at = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox4.Text += keyboardPath + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            focus_at = 1;
            remove_osd_keyboard();
            myProcess = Process.Start(keyboardPath);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            focus_at = 2;
            remove_osd_keyboard();
            myProcess = Process.Start(keyboardPath);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            focus_at = 3;
            remove_osd_keyboard();
            myProcess = Process.Start(keyboardPath);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            remove_osd_keyboard();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (focus_at == 1)
            {
                richTextBox1.Focus();
            }
            else if (focus_at == 2)
            {
                richTextBox2.Focus();
            }
            else if (focus_at == 3)
            {
                richTextBox3.Focus();
            }
        }

        void remove_osd_keyboard()
        {
            //richTextBox4.Text += "關閉螢幕鍵盤\n";

            bool flag_close_osd_keyboard = false;
            Process[] MyProcesses;
            string program_name = "TabTip";

            MyProcesses = Process.GetProcessesByName(program_name);//需要監控的程序名，該方法帶出該程序所有用到的進程
            foreach (Process myprocess in MyProcesses)
            {
                if (myprocess.ProcessName.ToLower() == program_name.ToLower())
                {
                    myprocess.Kill();
                    //richTextBox4.Text += "關閉程式 : " + program_name + "\n";
                    flag_close_osd_keyboard = true;
                }
            }

            if (flag_close_osd_keyboard == true)
            {
                richTextBox4.Text += "已關閉螢幕鍵盤\n";
            }
            else
            {
                richTextBox4.Text += "無已開啟之螢幕鍵盤\n";
            }
        }
    }
}
