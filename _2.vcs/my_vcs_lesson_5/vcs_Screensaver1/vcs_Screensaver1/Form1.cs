using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Screensaver1
{
    public partial class Form1 : Form
    {
        //加入私有成員變量

        private string filename = @"C:\______test_files\picture1.jpg";
        private int iSpeed = 2;
        private string str = "福建南紡股份公司計算機中心";

        //定義文本字體及大小

        private Font TextStringFont = new Font("宋體", 10, FontStyle.Bold);

        private Color TextStringcolor = Color.Yellow; //文本字體顏色

        private int iDistance;

        private int ixStart = 0;

        private int iyStart = 0;

        private int speed;

        private int x1, y1;

        int width1, height1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            setup_controls();
        }

        void setup_controls()
        {
            label1.ForeColor = Color.Yellow;

            label1.Location = new Point(624, 8);

            label1.Name = "label1";

            label1.Size = new Size(168, 16);

            label1.TabIndex = 0;

            label1.Visible = false;

            label1.Font = TextStringFont;

            label1.ForeColor = TextStringcolor;


            timer1.Enabled = true;

            timer1.Interval = 5;

            timer1.Tick += new System.EventHandler(timer1_Tick);

            pictureBox1.Image = Image.FromFile(filename);

            pictureBox1.Location = new Point(800, 600);

            pictureBox1.Name = "pictureBox1";

            pictureBox1.Size = new Size(304, 224);

            // 設置窗體(screen)屬性
            this.AutoScaleBaseSize = new Size(6, 14);
            this.BackColor = Color.Black;
            this.ClientSize = new Size(800, 600);
            this.ControlBox = false;
            this.FormBorderStyle = FormBorderStyle.None;
            this.KeyPreview = true;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "screen";
            this.ShowInTaskbar = false;
            this.StartPosition = FormStartPosition.Manual;
            this.WindowState = FormWindowState.Maximized;
            this.KeyDown += new KeyEventHandler(this.Form1_KeyDown);//鍵盤按下響應事件
            this.MouseDown += new MouseEventHandler(this.Form1_MouseDown);	//鼠標按下響應事件
            this.MouseMove += new MouseEventHandler(this.Form1_MouseMove);	//鼠標移動響應事件

            speed = 0;

            Rectangle ssWorkArea = Screen.GetWorkingArea(this);
            //屏幕顯示區域

            width1 = ssWorkArea.Width; //屏幕寬度
            height1 = ssWorkArea.Height; //屏幕高度
            Cursor.Hide(); //隱藏光標
        }

        private void timer1_Tick(object sender, System.EventArgs e) //計時器響應事件
        {
            label1.Visible = true;
            label1.Text = str;
            label1.Height = label1.Font.Height; //設置文本的高度
            label1.Width = label1.Text.Length * (int)label1.Font.Size * 2; //設置文本的寬度
            PlayScreenSaver();
        }

        private void PlayScreenSaver() //自定義函數
        {
            //下面設置文本顯示框的位置坐標
            label1.Location = new Point(width1 - iDistance, label1.Location.Y);
            label1.Visible = true; //設置為可見
            iDistance += iSpeed;
            if (label1.Location.X <= -(label1.Width))
            {
                iDistance = 0;
                if (label1.Location.Y == 0)
                {
                    label1.Location = new Point(label1.Location.X, height1 / 2);
                }
                else if (label1.Location.Y == height1 / 2)
                {
                    label1.Location = new Point(label1.Location.X, height1 - label1.Height);
                }
                else
                {
                    label1.Location = new Point(label1.Location.X, 0);
                }
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
            {
                speed = 0;
            }

            pictureBox1.Location = new Point(x1, y1);
        }

        private void StopScreenSaver() //停止屏幕保護程序運行
        {
            Cursor.Show();
            timer1.Enabled = false;
            Application.Exit();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)　//鍵盤按下事件
        {
            StopScreenSaver(); //停止運行屏幕保護程序
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)//鼠標按下事件
        {
            StopScreenSaver(); //停止運行屏幕保護程序
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)　//鼠標移動事件
        {
            if (ixStart == 0 && iyStart == 0)
            {
                ixStart = e.X;
                iyStart = e.Y;
                return;
            }
            else if (e.X != ixStart || e.Y != iyStart)
            {
                StopScreenSaver();
            }
        }
    }
}
