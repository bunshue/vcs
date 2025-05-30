﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyToolbox
{
    public partial class Form2 : Form
    {
        public Form2(string filename, int page)
        {
            InitializeComponent();

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            //this.Size = new Size(1920, 1040);
            //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

            //richTextBox1.Text += "檔案 : " + filename + "\n";
            //richTextBox1.Text += "頁數 : " + page.ToString() + "\n";

            //指名頁數
            if (page > 0)
            {
                webBrowser1.Navigate(filename + "?#initZoom=fitToPage&view=fit&navpanes=0&toolbar=0&page=" + page.ToString());
            }
            else
            {
                webBrowser1.Navigate(filename + "?#initZoom=fitToPage&view=fit&navpanes=0&toolbar=0");
            }
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
