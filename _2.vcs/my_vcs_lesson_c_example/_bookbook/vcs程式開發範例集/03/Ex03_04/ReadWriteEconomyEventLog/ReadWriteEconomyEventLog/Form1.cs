using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace ReadWriteEconomyEventLog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //檢查事件源是否存在，如果不存在將註冊事件源
            if (System.Diagnostics.EventLog.SourceExists("ZhyScoure"))
            {
                System.Diagnostics.EventLog.DeleteEventSource("ZhyScoure");//註冊事件源
            }
            //為NewLog1日誌名稱註冊事件源
            System.Diagnostics.EventLog.CreateEventSource("ZhyScoure", "NewLog1");
            eventLog1.Log = "NewLog1";//NewLog1日誌，
            eventLog1.Source = "ZhyScoure";//事件源名
            this.eventLog1.MachineName = ".";//表示本機
           // this.eventLog1.Clear();   
        }
        //寫入日誌
        private void button1_Click(object sender, EventArgs e)
        {

            if (System.Diagnostics.EventLog.Exists("NewLog1"))
            {
                if (textBox1.Text != "")
                {
                    eventLog1.WriteEntry(textBox1.Text.ToString());
                    MessageBox.Show("日誌寫成功");
                    textBox1.Text = "";
                }
                else
                {
                    MessageBox.Show("日誌內容不能為空");
                }
            }
            else
            {
                MessageBox.Show("日誌不存在");
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            if (eventLog1.Entries.Count > 0)
            {
                foreach (System.Diagnostics.EventLogEntry entry
                   in eventLog1.Entries)
                {
                    listBox1.Items.Add(entry.Message);
                }
            }
            else
            {
                MessageBox.Show("日誌中沒有記錄.");
            }

        }

       
    }
}