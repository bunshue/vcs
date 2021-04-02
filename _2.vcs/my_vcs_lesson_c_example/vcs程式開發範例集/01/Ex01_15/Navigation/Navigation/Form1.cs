using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace Navigation
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.Clear();
            listView1.LargeImageList = imageList1;
            listView1.Items.Add("設置上下班時間", "設置上下班時間", 0);
            listView1.Items.Add("是否啟用短信提醒", "是否啟用短信提醒", 1);
            listView1.Items.Add("設置密碼", "設置密碼", 2);

        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            listView1.Dock = DockStyle.None;
            button2.Dock = DockStyle.Top;
            button1.SendToBack();
            button1.Dock = DockStyle.Top;
            button3.Dock = DockStyle.Bottom;
            listView1.Dock = DockStyle.Bottom;
            listView1.Clear();
            listView1.Items.Add("近期工作記錄", "近期工作記錄", 3);
            listView1.Items.Add("近期工作計劃", "近期工作計劃", 4);
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            listView1.Dock = DockStyle.None;
            button3.SendToBack();
            button3.Dock = DockStyle.Top;
            button2.SendToBack();
            button2.Dock = DockStyle.Top;
            button1.SendToBack();
            button1.Dock = DockStyle.Top;
            listView1.Dock = DockStyle.Bottom;
            listView1.Clear();
            listView1.Items.Add("編輯工作進度報告", "編輯工作進度報告", 5);
            listView1.Items.Add("編輯項目設計圖", "編輯項目設計圖", 6);
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            listView1.Dock = DockStyle.None;
            button1.Dock = DockStyle.Top;
            button2.Dock = DockStyle.Bottom;
            button3.SendToBack();
            button3.Dock = DockStyle.Bottom;
            listView1.BringToFront();
            listView1.Dock = DockStyle.Bottom;
            listView1.Clear();
            listView1.Items.Add("設定上下班時間", "設定上下班時間", 0);
            listView1.Items.Add("是否啟用簡訊提醒", "是否啟用簡訊提醒", 1);
            listView1.Items.Add("設定密碼", "設定密碼", 2);
        }

        private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }
    }
}