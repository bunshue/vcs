using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
namespace ConserveEconomyLog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //事件源，用於存儲系系的錯誤日誌
            if (System.Diagnostics.EventLog.SourceExists("ErrEventLog"))
            {
                System.Diagnostics.EventLog.DeleteEventSource("ErrEventLog");
            }
            //事件類型為Application創建事件源
            System.Diagnostics.EventLog.CreateEventSource("ErrEventLog", "Application");
            eventLog2.Log = "Application";
            eventLog2.Source = "ErrEventLog";
            this.eventLog1.MachineName = ".";
            eventLog2.Clear();//清除ErrEventLog事件源的日誌信息

        }
        private void button1_Click(object sender, EventArgs e)
        {  
           //查找系統日誌
            if (eventLog1.Entries.Count > 0)
            {
                foreach (System.Diagnostics.EventLogEntry entry in eventLog1.Entries)
                {
                    if (entry.EntryType == System.Diagnostics.EventLogEntryType.Error)
                    {
                        //MessageBox.Show(entry.Message);
                        listBox1.Items.Add(entry.Message);
                        eventLog2.WriteEntry(entry.Message,System.Diagnostics.EventLogEntryType.Error);
                    }
                }
            }
            else
            {
                MessageBox.Show("系統沒有錯誤日誌.");
            }
        }
    }
}