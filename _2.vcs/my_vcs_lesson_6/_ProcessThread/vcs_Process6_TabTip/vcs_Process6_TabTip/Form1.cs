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
        //win10的虛擬鍵盤是一個程式，即c:\Program Files\Common Files\Microsoft Shared\ink\TabTip.exe
        string keyboardPath = @"C:\Program Files\Common Files\Microsoft Shared\ink\TabTip.exe";

        Process process = new Process();
        int focus_at = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox4.Text += keyboardPath + "\n";
            bt_clear.Location = new Point(richTextBox4.Location.X + richTextBox4.Size.Width - bt_clear.Size.Width, richTextBox4.Location.Y + richTextBox4.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox4.Clear();
        }

        private void richTextBox1_MouseDown(object sender, MouseEventArgs e)
        {
            do_keyin_richTextBox(1);
        }

        private void richTextBox2_MouseDown(object sender, MouseEventArgs e)
        {
            do_keyin_richTextBox(2);
        }

        private void richTextBox3_MouseDown(object sender, MouseEventArgs e)
        {
            do_keyin_richTextBox(3);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            do_keyin_richTextBox(1);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            do_keyin_richTextBox(2);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            do_keyin_richTextBox(3);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            remove_osd_keyboard();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox4.Text += "Info\n";

            string program_name = "TabTip";

            Process[] processes = Process.GetProcessesByName(program_name);//需要監控的程序名，該方法帶出該程序所有用到的進程
            foreach (Process process in processes)
            {
                richTextBox4.Text += "取得程式 : " + process.ProcessName + "\n";

                if (process.ProcessName.ToLower() == program_name.ToLower())
                {
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + program_name + "\n";
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.ProcessName + "\n";
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.BasePriority.ToString() + "\n";
                    //richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.ExitTime.ToLongDateString() + "\n";
                    //richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.HasExited.ToString() + "\n";
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.Id + "\n";
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.MachineName + "\n";
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.MainWindowTitle + "\n";

                    //richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.Modules.Count.ToString() +"\n";
                    //richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.ProcessorAffinity.ToString() + "\n";
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.SessionId + "\n";
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.Site + "\n";
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.StartInfo.CreateNoWindow.ToString() + "\n";
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.StartTime + "\n";
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.Threads + "\n";
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.TotalProcessorTime + "\n";

                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.StartInfo.CreateNoWindow.ToString() + "\n";

                    process.StartInfo.CreateNoWindow = true;
                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.StartInfo.CreateNoWindow.ToString() + "\n";

                    process.Kill();

                    richTextBox4.Text += "取得螢幕鍵盤程式 : " + process.StartInfo.CreateNoWindow.ToString() + "\n";

                }
            }
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
            /*
            bool flag_close_osd_keyboard = false;
            string program_name = "TabTip";

            Process[] processes = Process.GetProcessesByName(program_name);//需要監控的程序名，該方法帶出該程序所有用到的進程
            foreach (Process process in processes)
            {
                if (process.ProcessName.ToLower() == program_name.ToLower())
                {
                    process.Kill();
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
            */

            bool flag_close_osd_keyboard = false;
            foreach (var process in Process.GetProcessesByName("TabTip"))
            {
                process.Kill();
                flag_close_osd_keyboard = true;
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

        void do_keyin_richTextBox(int rtb)
        {
            focus_at = rtb;
            remove_osd_keyboard();
            process = Process.Start(keyboardPath);

            if (rtb == 1)
                richTextBox1.SelectAll();
            else if (rtb == 2)
                richTextBox2.SelectAll();
            else if (rtb == 3)
                richTextBox3.SelectAll();
        }
    }
}
