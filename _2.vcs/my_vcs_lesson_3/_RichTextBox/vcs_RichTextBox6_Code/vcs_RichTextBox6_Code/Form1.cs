﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File

namespace vcs_RichTextBox6_Code
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Font = new Font("Consolas", 40);

            byte[] bytes = File.ReadAllBytes(Application.ExecutablePath);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < bytes.Length; i++)
            {
                string value = Convert.ToString(bytes[i], 2);
                value = value.PadLeft(8, '0');
                sb.Append(value + ' ');
            }
            richTextBox1.Text = sb.ToString();

            //byte[] bytes = File.ReadAllBytes(Application.ExecutablePath);
            //string[] strings = Array.ConvertAll(bytes,
            //    b => Convert.ToString(b, 2).PadLeft(8, '0'));
            //richTextBox1.Text = string.Join(" ", strings);

            //var query =
            //    from byte b in File.ReadAllBytes(Application.ExecutablePath)
            //    select Convert.ToString(b, 2).PadLeft(8, '0');
            //richTextBox1.Text = string.Join(" ", query.ToArray());
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
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
            Application.Exit();
        }
    }
}
