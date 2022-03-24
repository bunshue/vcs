using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

////用Visual C＃編寫屏幕保護程序
//最後運行該程序，把vcs_Screensaver5.exe改為vcs_Screensaver5.scr，拷入Windows系統目錄中，這樣就可以運行該屏幕保護程序。


/*
Visual C#是微軟公司推出的新一代程序開發語言，是微軟.Net框架中的一個重要組成部分。屏幕保護程序是以scr為擴展名的標准Windows可執行程序。屏幕保護程序不僅可以延長顯示器的使用壽命，還可以保護私人信息。本文向大家介紹一個.Net平台上用C#編寫的一個動態文本及圖形的屏幕保護程序。



　　一、具體實現步驟：

　　（1）在Visual Studio.Net下新建一個C＃的Windows應用程序工程，命名為vcs_Screensaver5

　　（2）現在我們來設計程序的主界面：

　　先將窗體的Name屬性設置為screen、Text屬性設置為空，BackColor屬性設置為Black、Size屬性設置為(800, 600)、 ControlBox、MaximizeBox、MinimizeBox、ShowInTaskbar屬性設置均為false、FormBorderStyle屬性設置為None。再往窗體上添加Label控件、PictureBox控件、Timer控件各一個。將Label控件的Name設置為Word、Text屬性設置為空；將PictureBox控件的Name設置為picture1、Image設置為一個預知圖片；將Timer控件的Name設置為timerSaver、Enabled 屬性設為true、Interval屬性設為5。

*/
namespace vcs_Screensaver5
{
    public partial class Form1 : Form
    {

        //加入私有成員變量

        //private System.ComponentModel.IContainer components;

        private int iSpeed = 2;

        private string str = "福建南紡股份公司計算機中心";

        //定義文本字體及大小

        private System.Drawing.Font TextStringFont = new System.Drawing.Font("宋體", 10, System.Drawing.FontStyle.Bold);

        private Color TextStringcolor = System.Drawing.Color.Yellow;    // 文本字體顏色

        private int iDistance;

        private int ixStart = 0;

        private int iyStart = 0;

        private int speed;

        private int x1, y1;

        int width1, height1;

        //private System.Windows.Forms.Timer timerSaver;    //計時器控件

        //private System.Windows.Forms.PictureBox picture1; //圖形控件

        //private System.Windows.Forms.Label Word;  //文本顯示控件



        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //System.Resources.ResourceManager resources = new system.Resources.ResourceManger(typeof(screen));

            this.label1 = new System.Windows.Forms.Label();

            this.timer1 = new System.Windows.Forms.Timer(this.components);

            this.pictureBox1 = new System.Windows.Forms.PictureBox();


            label1.Font = TextStringFont;

            label1.ForeColor = TextStringcolor;

            System.Windows.Forms.Cursor.Hide(); //隱藏光標



            this.SuspendLayout();

            //

            // 設置文本顯示控件(label1)屬性

            this.label1.ForeColor = System.Drawing.Color.Yellow;

            this.label1.Location = new System.Drawing.Point(624, 8);

            this.label1.Name = "label1";

            this.label1.Size = new System.Drawing.Size(168, 16);

            this.label1.TabIndex = 0;

            this.label1.Visible = false;

            //

            // 設置計時器控件(timer1)屬性

            this.timer1.Enabled = true;

            this.timer1.Interval = 5;

            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);

            //

            // 設置圖片控件(pictureBox1)屬性

            string filename = @"C:\______test_files\picture1.jpg";

            this.pictureBox1.Image = Image.FromFile(filename);

            this.pictureBox1.Location = new System.Drawing.Point(800, 600);

            this.pictureBox1.Name = "pictureBox1";

            this.pictureBox1.Size = new System.Drawing.Size(304, 224);

            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;

            this.pictureBox1.TabIndex = 1;

            this.pictureBox1.TabStop = false;

            //

            // 設置窗體(screen)屬性

            this.AutoScaleBaseSize = new System.Drawing.Size(6, 14);

            this.BackColor = System.Drawing.Color.Black;

            this.ClientSize = new System.Drawing.Size(800, 600);

            this.ControlBox = false;

            this.Controls.AddRange(new System.Windows.Forms.Control[] { this.pictureBox1, this.label1 });

            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;

            this.KeyPreview = true;

            this.MaximizeBox = false;

            this.MinimizeBox = false;

            this.Name = "screen";

            this.ShowInTaskbar = false;

            this.StartPosition = System.Windows.Forms.FormStartPosition.Manual;

            this.WindowState = System.Windows.Forms.FormWindowState.Maximized;

            //this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.screen_KeyDown);

            //this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.screen_MouseDown);

            this.Load += new System.EventHandler(this.Form1_Load);

            //this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.screen_MouseMove);

            //this.ResumeLayout(false);

            speed = 0;

            System.Drawing.Rectangle ssWorkArea = System.Windows.Forms.Screen.GetWorkingArea(this);
            //屏幕顯示區域

            width1 = ssWorkArea.Width;  //屏幕寬度

            height1 = ssWorkArea.Height;    //屏幕高度

        }

        private void timer1_Tick(object sender, EventArgs e)
        {

            label1.Visible = true;

            label1.Text = str;

            label1.Height = label1.Font.Height; //設置文本的高度

            label1.Width = label1.Text.Length * (int)label1.Font.Size * 2;    //設置文本的寬度

            PlayScreenSaver();
        }

        private void PlayScreenSaver() //自定義函數
        {

            //下面設置文本顯示框的位置坐標

            label1.Location = new System.Drawing.Point(width1 - iDistance, label1.Location.Y);

            label1.Visible = true;    // 設置為可見

            iDistance += iSpeed;

            if (label1.Location.X <= -(label1.Width))
            {

                iDistance = 0;

                if (label1.Location.Y == 0)

                    label1.Location = new System.Drawing.Point(label1.Location.X, height1 / 2);

                else if (label1.Location.Y == height1 / 2)

                    label1.Location = new System.Drawing.Point(label1.Location.X, height1 - label1.Height);

                else

                    label1.Location = new System.Drawing.Point(label1.Location.X, 0);

            }

            //下面是計算圖片框移動坐標

            speed++;

            if (speed <= 2 * height1)
            {

                x1 = System.Math.Abs(width1 - speed);

                y1 = System.Math.Abs(height1 - speed);

            }

            else if (speed > 2 * height1 && speed <= 2 * width1)
            {

                x1 = System.Math.Abs(width1 - speed);

                y1 = System.Math.Abs(height1 - (speed - speed / height1 * height1));

            }

            else if (speed > 2 * width1 && speed <= 3 * height1)
            {

                x1 = System.Math.Abs(width1 - (speed - speed / width1 * width1));

                y1 = System.Math.Abs(height1 - (speed - speed / height1 * height1));

            }

            else if (speed > 3 * height1 && speed < 4 * height1)
            {

                x1 = System.Math.Abs(width1 - (speed - speed / width1 * width1));

                y1 = System.Math.Abs(speed - speed / height1 * height1);

            }

            else if (speed >= 4 * height1 && speed < 5 * height1)
            {

                x1 = System.Math.Abs(speed - speed / width1 * width1);

                y1 = System.Math.Abs(height1 - (speed - speed / height1 * height1));

            }

            else if (speed >= 5 * height1 && speed < 4 * width1)
            {

                x1 = System.Math.Abs(speed - speed / width1 * width1);

                y1 = System.Math.Abs(speed - speed / height1 * height1);

            }

            else if (speed >= 4 * width1 && speed < 6 * height1)
            {

                x1 = System.Math.Abs(width1 - (speed - speed / width1 * width1));

                y1 = System.Math.Abs(speed - speed / height1 * height1);

            }

            else if (speed >= 6 * height1 && speed < 5 * width1)
            {

                x1 = System.Math.Abs(width1 - (speed - speed / width1 * width1));

                y1 = System.Math.Abs(height1 - (speed - speed / height1 * height1));

            }

            else if (speed >= 5 * width1 && speed < 7 * height1)
            {

                x1 = System.Math.Abs(speed - speed / width1 * width1);

                y1 = System.Math.Abs(height1 - (speed - speed / height1 * height1));

            }

            else if (speed >= 7 * height1 && speed < 6 * width1)
            {

                x1 = System.Math.Abs(speed - speed / width1 * width1);

                y1 = System.Math.Abs(speed - speed / height1 * height1);

            }

            if (speed == 6 * width1)

                speed = 0;

            pictureBox1.Location = new System.Drawing.Point(x1, y1);

        }

        private void StopScreenSaver() //停止屏幕保護程序運行
        {

            System.Windows.Forms.Cursor.Show();
            timer1.Enabled = false;


            Application.Exit();

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            StopScreenSaver();  //停止運行屏幕保護程序

        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            //鼠標移動事件

            if (ixStart == 0 && iyStart == 0)
            {

                ixStart = e.X;

                iyStart = e.Y;

                return;

            }

            else if (e.X != ixStart || e.Y != iyStart)

                StopScreenSaver();


        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            //鍵盤按下事件
            StopScreenSaver();  //停止運行屏幕保護程序
        }
    }
}

