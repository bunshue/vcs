﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace 隱藏_顯示桌面圖標
{
    public partial class Form1 : Form
    {
        [DllImport("user32")]
        public static extern int FindWindow(string ClassName, string WindowName);
        [DllImport("user32")]
        public static extern int ShowWindow(int handle, int cmdshow);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.TopMost = true;
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                ShowWindow(FindWindow("progman", null), 0);
                richTextBox1.Text += "隱藏桌面圖標\n";
            }
            else
            {
                ShowWindow(FindWindow("progman", null), 5);
                richTextBox1.Text += "顯示桌面圖標\n";
            }
        }
    }
}

