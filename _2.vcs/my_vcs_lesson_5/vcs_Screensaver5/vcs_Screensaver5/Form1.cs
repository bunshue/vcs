using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


/*
Form1之屬性
FormBoderStyle屬性為None
ShowInTaskbar屬性為False
WindowState屬性為Maximized
*/

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
