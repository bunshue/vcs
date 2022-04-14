using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//C# 屏幕監控 自動截屏程序 主窗體隱藏，僅在進程中顯示

namespace vcs_ScreenCapture1
{
    public partial class Form1 : Form
    {
        string foldername = @"C:\dddddddddd\_screen_capture_" + DateTime.Now.ToString("yyyy-MM-dd");

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //主窗體桌面不顯示 僅在進程中顯示
            InitializeComponent();
            this.WindowState = FormWindowState.Minimized;
            this.ShowInTaskbar = false;
            SetVisibleCore(false);

            if (Directory.Exists(foldername) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(foldername);
                //richTextBox1.Text += "已建立一個新資料夾: " + foldername + "\n";
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + foldername + " 已存在，不用再建立\n";
            }
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
            string ImageName = DateTime.Now.ToString("yyyyMMdd_hhmmss") + ".jpg";
            bitmap1.Save(foldername + "/" + ImageName);
            //釋放資源  
            bitmap1.Dispose();
            g.Dispose();
            GC.Collect();
        }
    }
}

