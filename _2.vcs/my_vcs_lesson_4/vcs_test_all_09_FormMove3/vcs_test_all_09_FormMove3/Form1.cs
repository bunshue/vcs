using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

/*
c# 移動窗體和控件

在winform程序裡面，有時候我們需要移動沒有標題欄窗體或是窗體內的控件，用幾個事件如鼠標單擊，移動，等再加上坐標的計算可以完成這一功能，但是最近發現了一個API函數，可以非常簡單方便的完成這個功能。如下：
*/


namespace vcs_test_all_09_FormMove3
{
    public partial class Form1 : Form
    {
        [DllImportAttribute("user32.dll")]
        private extern static bool ReleaseCapture();
        [DllImportAttribute("user32.dll")]
        private extern static int SendMessage(IntPtr handle, int m, int p, int h);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                this.Cursor = Cursors.SizeAll;
                ReleaseCapture();
                SendMessage(this.Handle, 0xA1, 0x2, 0);
                this.Cursor = Cursors.Default;
            }

        }

        private void button1_MouseDown(object sender, MouseEventArgs e)
        {
            Form1_MouseDown(sender, e);

        }
    }
}
