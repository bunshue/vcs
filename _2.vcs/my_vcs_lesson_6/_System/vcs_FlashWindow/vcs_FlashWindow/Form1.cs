using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_FlashWindow
{
    public partial class Form1 : Form
    {
        /// 窗口閃動
        /// 
        ///窗口句柄
        ///是否為閃
        /// 成功返回0
        [DllImport("user32.dll")]
        public static extern bool FlashWindow(IntPtr hwnd, bool bInvert);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            cnt++;
            FlashWindow(this.Handle, (cnt % 2) == 0);
        }
    }
}
