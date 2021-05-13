using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for WindowsAPI的訊息框

namespace vcs_MessageBox2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        //用WindowsAPI的訊息框 ST

        public const int MB_OKCANCEL = 1;
        public const int MB_ICONINFORMATION = 64;

        [DllImport("user32.dll")]
        public static extern int MessageBox(int hWnd, string lpText, string lpCaption, uint wType);

        private void button4_Click(object sender, EventArgs e)
        {
            int iResult = MessageBox(0, "要通知的訊息內容", "使用Windows API", MB_OKCANCEL | MB_ICONINFORMATION);
        }
        //用WindowsAPI的訊息框 SP


        //新類別的訊息框
        private void button5_Click(object sender, EventArgs e)
        {
            int iResult = Test.MessageBox(0, "要通知的訊息內容", "使用自建類別", Test.MB_OKCANCEL | Test.MB_ICONINFORMATION);
        }

    }
}
