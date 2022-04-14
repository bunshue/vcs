using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

//C# 屏幕監控 自動截屏程序 主窗體隱藏，僅在進程中顯示

namespace vcs_ScreenCapture2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //主窗體桌面不顯示 僅在進程中顯示  
            this.WindowState = FormWindowState.Minimized;
            this.ShowInTaskbar = false;
            SetVisibleCore(false);

            timer1.Enabled = true;
        }

        protected override void SetVisibleCore(bool value)
        {
            base.SetVisibleCore(value);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //獲得當前屏幕的大小
            Rectangle rect = new Rectangle();
            rect = System.Windows.Forms.Screen.GetWorkingArea(this);
            Size mySize = new Size(rect.Width, rect.Height);
            Bitmap bitmap1 = new Bitmap(rect.Width, rect.Height);
            Graphics g = Graphics.FromImage(bitmap1);
            g.CopyFromScreen(0, 0, 0, 0, mySize);

            string filename = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

            bitmap1.Save(filename);
            //釋放資源  
            bitmap1.Dispose();
            g.Dispose();
            GC.Collect();
        }
    }
}
