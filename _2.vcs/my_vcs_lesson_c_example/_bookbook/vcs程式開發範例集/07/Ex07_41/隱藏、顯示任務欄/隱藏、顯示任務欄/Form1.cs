using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace 隱藏_顯示任務欄
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const int SW_HIDE = 0;
        private const int SW_RESTORE = 9;

        [DllImport("user32.dll")]
        public static extern int FindWindow(string lpClassName, string lpWindowName);

        [DllImport("user32.dll")]
        public static extern int ShowWindow(int hwnd, int nCmdShow);

        private void button1_Click(object sender, EventArgs e)
        {
            if (radioButton1.Checked)
                ShowWindow(FindWindow("Shell_TrayWnd", null), SW_HIDE);
            if (radioButton2.Checked)
                ShowWindow(FindWindow("Shell_TrayWnd", null), SW_RESTORE);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}