using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Diagnostics;

namespace vcs_Thread_Example2
{
    public partial class Form1 : Form
    {
        private Thread m_worker;
        private bool m_RunFlag = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //C# 強制關閉 Process
            Process.GetCurrentProcess().Kill();

            Application.Exit();


        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (m_RunFlag == false)
            {
                m_RunFlag = true;
                m_worker = new Thread(new ThreadStart(this.ModbusThreadProc));
                m_worker.Start();
            }
            else
            {
                m_RunFlag = false;
            }

        }

        private void ModbusThreadProc()
        {
            Console.WriteLine("Start Modbus Slave");
            byte[] bytData = new byte[1];
            while (m_RunFlag)
            {
                //do something infinitely
                richTextBox1.Text += ".";
                //serial.Read(bytData, 0, bytData.Length, Timeout.Infinite);
                //RtuSlave(bytData[0]);
            }
        }


    }
}

