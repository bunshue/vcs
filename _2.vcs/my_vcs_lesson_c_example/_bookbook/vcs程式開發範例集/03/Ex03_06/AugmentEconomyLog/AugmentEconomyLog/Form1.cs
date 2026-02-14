using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;

namespace AugmentEconomyLog
{
    public partial class Form1 : Form
    {
        public int intCount = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (eventLog1.Entries.Count > 0)
            {
                foreach (System.Diagnostics.EventLogEntry entry in eventLog1.Entries)
                {
                    if (comboBox1.Items.Count == 0)
                    {
                        comboBox1.Items.Add(entry.Source.ToString());
                    }
                    else
                    {
                        if (entry.Source.ToString() != comboBox1.Items[intCount].ToString())
                        {
                            comboBox1.Items.Add(entry.Source.ToString());
                            intCount++;
                        }
                    }
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (comboBox1.SelectedItem == null)
            {
                MessageBox.Show("請選擇日誌名稱");
                return;
            }
            if (textBox1.Text == "")
            {
                MessageBox.Show("請填寫日誌內容");
                textBox1.Focus();
                return;
            }
            eventLog1.Log = "System";
            eventLog1.Source = comboBox1.SelectedItem.ToString();
            eventLog1.MachineName = ".";
            eventLog1.WriteEntry(textBox1.Text);
            MessageBox.Show("添加成功");
            if (eventLog1.Entries.Count > 0)
            {
                foreach (System.Diagnostics.EventLogEntry entry in eventLog1.Entries)
                {
                    listView1.Items.Add(entry.Message);
                }

            }
        }
    }
}
