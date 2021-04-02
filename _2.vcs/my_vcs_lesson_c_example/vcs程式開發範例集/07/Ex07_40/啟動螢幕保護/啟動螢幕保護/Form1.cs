using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace 啟動螢幕保護
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const int WM_SYSCOMMAND = 0x0112;
        private const int SC_SCREENSAVE = 0xf140;

        [DllImport("user32.dll")]
        public static extern bool SendMessage(IntPtr hwnd, int wMsg, int wParam, int lParam);

        private void button1_Click(object sender, EventArgs e)
        {
            SendMessage(this.Handle, WM_SYSCOMMAND, SC_SCREENSAVE, 0);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}