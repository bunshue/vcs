using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace vcs_ScreenCapture3
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

            this.timer1.Enabled = true;
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
            Bitmap bitmap = new Bitmap(rect.Width, rect.Height);
            Graphics g = Graphics.FromImage(bitmap);
            g.CopyFromScreen(0, 0, 0, 0, mySize);
            string ImageName = DateTime.Now.ToString("yyyyMMdd_hhmmss") + ".jpg";
            bitmap.Save(ImageName);
            //釋放資源  
            bitmap.Dispose();
            g.Dispose();
            GC.Collect();
        }
    }
}