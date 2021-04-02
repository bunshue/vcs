using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace VerdictEconomyLogWetherAmendOrNot
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = Environment.SystemDirectory + "\\config";
            textBox1.Enabled = false;
           
        }

        private void button1_Click(object sender, EventArgs e)
        {
            fileSystemWatcher1.Path = textBox1.Text;
            //提示對於此示例，您可以使用本地計算機上所希望的任何目錄。
            this.fileSystemWatcher1.Filter = "*.Evt";//此屬獲取或設置篩選字符串，用於確定在目錄中監視哪些文件。
            this.fileSystemWatcher1.EndInit();
        }
        //創建文件是發生
        private void fileSystemWatcher1_Created(object sender, System.IO.FileSystemEventArgs e)
        {
            listBox1.Items.Add("日誌文件:" + e.FullPath+"被創建");
        }
        private void fileSystemWatcher1_Changed(object sender, System.IO.FileSystemEventArgs e)
        {
            listBox1.Items.Add("日誌文件:" + e.FullPath + "被更改");
        }
        private void fileSystemWatcher1_Deleted(object sender, System.IO.FileSystemEventArgs e)
        {
            listBox1.Items.Add("日誌文件:" + e.FullPath + "被冊除");
        }
    }
}