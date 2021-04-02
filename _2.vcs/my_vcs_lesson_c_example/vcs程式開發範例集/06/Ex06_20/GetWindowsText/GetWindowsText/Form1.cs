using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Runtime.InteropServices;


namespace GetWindowsText
{
    public partial class Form1 : Form
    {
        const int GW_HWNDNEXT = 2;//API參數：取得下一個同級窗口句柄
        public Form1()
        {
            InitializeComponent();
        }

        private  void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            StringBuilder text = new StringBuilder(2560) ;
            IntPtr currentHandle;
            currentHandle = GetWindow(this.Handle, GW_HWNDNEXT);
            int v = GetWindowText(currentHandle,text, 2560);
            richTextBox1.Text = text.ToString();

        }
        [DllImportAttribute("user32.dll")]
        private static extern int GetWindowText(IntPtr handle, StringBuilder Text, int MaxCount);
        [DllImportAttribute("user32.dll")]
        private static extern IntPtr GetWindow(IntPtr handle,int ucmd);

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}