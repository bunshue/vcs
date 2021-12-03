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


namespace vcs_Form8_FormMove3
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

        //鼠標點擊按鈕拖動窗體 ST

        //記錄窗體的X坐標 
        private int startX;

        //記錄窗體的Y坐標 
        private int startY;

        private void button3_MouseDown(object sender, MouseEventArgs e)
        {
            //判斷點擊的是不是左鍵 
            if (e.Button == MouseButtons.Left)
            {
                //得到窗體的X值 
                startX = e.X;
                //得到窗體的Y值 
                startY = e.Y;
            }
        }

        private void button3_MouseMove(object sender, MouseEventArgs e)
        {
            //判斷點擊的是不是左鍵 
            if (e.Button == MouseButtons.Left)
            {

                //重新繪制窗體X 

                this.Left += e.X - startX;

                //重新繪制窗體Y 

                this.Top += e.Y - startY;
            }
        }
        //鼠標點擊按鈕拖動窗體 SP
    }
}