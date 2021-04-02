using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace 取得任務欄尺寸大小
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        [DllImport("user32.dll")]
        public static extern int FindWindow(string lpClassName, string lpWindowName);

        [DllImport("user32.dll")]
        public static extern int GetWindowRect(int hwnd, ref Rectangle lpRect);

        Rectangle myrect;

        private void button1_Click(object sender, EventArgs e)
        {
            if (GetWindowRect(FindWindow("Shell_TrayWnd", null), ref myrect) == 0)
                return;
            else
            {
                textBox1.Text = Convert.ToString(myrect.Left);
                textBox2.Text = Convert.ToString(myrect.Top);
                textBox3.Text = Convert.ToString(myrect.Right);
                textBox4.Text = Convert.ToString(myrect.Bottom);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}