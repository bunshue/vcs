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

/*
1)屏保运行起来是一个整个屏幕且无边框的窗体，不能显示任务栏，鼠标点击就会退出。当然你还可以在界面上自定义一些东西，如显示系统时间，屏保里面显示Rss内容等。

2)屏幕保护程序的扩展名虽然是".scr"，但本质是一个可执行的".exe"文件。
*/

namespace vcs_Screensaver4
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files1\picture1.jpg";
        //string filename = @"C:\______test_files1\_material\ims1.bmp";

        Label label1 = new Label();
        Timer timer1 = new Timer();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            /*
            全屏隨機位置顯示圖片
            Form1之屬性
            FormBorderStyle 改 None		//無邊框
            StartPosition 改 CenterScreen	//視窗居中顯示
            WindowState 改 Maximized	//畫面最大化
            ControlBox 改 False
            MaximizeBox 改 False
            MinimizeBox 改 False
            ShowIcon 改 False
            ShowInTaskbar 改 False
            TopMost 改 True
            KeyPreview 改 True
            */

            this.FormBorderStyle = FormBorderStyle.None;	//無邊框
            this.StartPosition = FormStartPosition.CenterScreen;	//視窗居中顯示
            this.WindowState = FormWindowState.Maximized;   //畫面最大化
            this.ControlBox = false;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.ShowIcon = false;
            this.ShowInTaskbar = false;	//不在任務欄中顯示
            this.KeyPreview = true;
            this.TopMost = true;
            this.BackColor = Color.White;
            this.AutoSize = true;
            //this.AutoSizeMode = AutoSizeMode.GrowAndShrink;     //讓表單大小可以自動隨著圖片大小變化。
            //this.TransparencyKey = SystemColors.ControlLight;   //將表單的TransparencyKey設為Control，這樣可以去掉桌面小玩意外圍多餘的部份

            this.BackgroundImage = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            this.BackgroundImageLayout = ImageLayout.Center;
            this.Deactivate += new System.EventHandler(this.Form1_Deactivate);
            this.Click += new System.EventHandler(Exit);
            this.BackColor = Color.White;

            this.DoubleBuffered = true;//設置本窗體
            SetStyle(ControlStyles.UserPaint, true);
            SetStyle(ControlStyles.AllPaintingInWmPaint, true);
            SetStyle(ControlStyles.DoubleBuffer, true);

            label1.Location = new Point((this.Size.Width / 10), this.Size.Height / 5 * 4);
            label1.AutoSize = true;
            label1.Font = new Font("Arial", 36);
            label1.BackColor = Color.Transparent;
            label1.BringToFront();
            this.Controls.Add(label1);

            timer1.Interval = 10;
            timer1.Tick += new System.EventHandler(LableTimeText);
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
