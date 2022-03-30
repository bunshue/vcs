using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
最後把bin/debug或者bin/release下的可執行程序後綴改成scr，並拷貝到系統盤Windows的system32下。
這樣通過桌面個性化的屏幕保護程序設置一下就可以投入使用了，
*/

namespace vcs_Screensaver5
{
    public partial class Form1 : Form
    {
        Timer timer1 = new Timer();
        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.None;	//無邊框
            this.StartPosition = FormStartPosition.CenterScreen;	//視窗居中顯示
            this.WindowState = FormWindowState.Maximized;   //畫面最大化
            this.ControlBox = false;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.ShowIcon = false;
            //this.ShowInTaskbar = false;	//不在任務欄中顯示

            this.KeyPreview = true;
            this.TopMost = true;
            this.BackColor = Color.White;
            this.BackgroundImageLayout = ImageLayout.Center;

            this.AutoSize = true;
            //this.AutoSizeMode = AutoSizeMode.GrowAndShrink;     //讓表單大小可以自動隨著圖片大小變化。
            //this.TransparencyKey = SystemColors.ControlLight;   //將表單的TransparencyKey設為Control，這樣可以去掉桌面小玩意外圍多餘的部份

            this.DoubleBuffered = true;//設置本窗體
            SetStyle(ControlStyles.UserPaint, true);
            SetStyle(ControlStyles.AllPaintingInWmPaint, true);
            SetStyle(ControlStyles.DoubleBuffer, true);

            this.BackgroundImage = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            this.Click += new System.EventHandler(Exit);
            this.BackColor = System.Drawing.Color.White;
            this.label1.Location = new System.Drawing.Point((this.Size.Width / 10), this.Size.Height / 5 * 4);

            timer1.Interval = 10;
            this.timer1.Tick += new System.EventHandler(LableTimeText);
            timer1.Start();
        }

        private void Exit(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void LableTimeText(object sender, EventArgs e)
        {
            label1.Text = DateTime.Now.ToString();
        }

        private void Form1_Deactivate(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
