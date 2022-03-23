using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Screensaver7
{
    public partial class screen : Form
    {
        //加入私有成員變量

        //private System.ComponentModel.IContainer components;

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

        private System.Windows.Forms.Timer timerSaver;　 //計時器控件

        private System.Windows.Forms.PictureBox picture1; //圖形控件

        private System.Windows.Forms.Label Word; //文本顯示控件

        public screen()
        {
            InitializeComponent();
        }

        private void screen_Load(object sender, EventArgs e)
        {
            this.components = new System.ComponentModel.Container();

            //System.Resources.ResourceManager resources = new System.Resources.ResourceManger(typeof(screen));

            this.Word = new System.Windows.Forms.Label();

            this.timerSaver = new System.Windows.Forms.Timer(this.components);

            this.picture1 = new System.Windows.Forms.PictureBox();

            this.SuspendLayout();

            //

            // 設置文本顯示控件(Word)屬性

            this.Word.ForeColor = Color.Yellow;

            this.Word.Location = new Point(624, 8);

            this.Word.Name = "Word";

            this.Word.Size = new Size(168, 16);

            this.Word.TabIndex = 0;

            this.Word.Visible = false;

            //

            // 設置計時器控件(timerSaver)屬性

            this.timerSaver.Enabled = true;

            this.timerSaver.Interval = 5;

            this.timerSaver.Tick += new System.EventHandler(this.timerSaver_Tick);

            //

            // 設置圖片控件(picture1)屬性

            string filename = @"C:\______test_files\picture1.jpg";
            this.picture1.Image = Image.FromFile(filename);

            //this.picture1.Image = ((Bitmap)(resources.GetObject("picture1.Image")));

            this.picture1.Location = new Point(800, 600);

            this.picture1.Name = "picture1";

            this.picture1.Size = new Size(304, 224);

            this.picture1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;

            this.picture1.TabIndex = 1;

            this.picture1.TabStop = false;

            //

            // 設置窗體(screen)屬性

            this.AutoScaleBaseSize = new Size(6, 14);

            this.BackColor = Color.Black;

            this.ClientSize = new Size(800, 600);

            this.ControlBox = false;

            this.Controls.AddRange(new System.Windows.Forms.Control[] { this.picture1, this.Word });

            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;

            this.KeyPreview = true;

            this.MaximizeBox = false;

            this.MinimizeBox = false;

            this.Name = "screen";

            this.ShowInTaskbar = false;

            this.StartPosition = System.Windows.Forms.FormStartPosition.Manual;

            this.WindowState = System.Windows.Forms.FormWindowState.Maximized;

            //鍵盤按下響應事件

            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.screen_KeyDown);


            //鼠標按下響應事件
            this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.screen_MouseDown);

            //窗體啟動調用事件
            //this.Load += new System.EventHandler(this.Form1_Load);


            //鼠標移動響應事件

            this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.screen_MouseMove);

            this.ResumeLayout(false);



            speed = 0;

            Rectangle ssWorkArea = System.Windows.Forms.Screen.GetWorkingArea(this);
            //屏幕顯示區域

            width1 = ssWorkArea.Width; //屏幕寬度

            height1 = ssWorkArea.Height; //屏幕高度


            Word.Font = new Font("標楷體", 20);

            Word.ForeColor = TextStringcolor;

            System.Windows.Forms.Cursor.Hide(); //隱藏光標




        }

        private void timerSaver_Tick(object sender, System.EventArgs e) //計時器響應事件
        {

            Word.Visible = true;

            Word.Text = str;

            Word.Height = Word.Font.Height; //設置文本的高度

            Word.Width = Word.Text.Length * (int)Word.Font.Size * 2; //設置文本的寬度

            PlayScreenSaver();

        }

        private void PlayScreenSaver() //自定義函數
        {

            //下面設置文本顯示框的位置坐標

            Word.Location = new Point(width1 - iDistance, Word.Location.Y);

            Word.Visible = true; //設置為可見

            iDistance += iSpeed;

            if (Word.Location.X <= -(Word.Width))
            {

                iDistance = 0;

                if (Word.Location.Y == 0)

                    Word.Location = new Point(Word.Location.X, height1 / 2);

                else if (Word.Location.Y == height1 / 2)

                    Word.Location = new Point(Word.Location.X, height1 - Word.Height);

                else

                    Word.Location = new Point(Word.Location.X, 0);

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

            picture1.Location = new Point(x1, y1);

        }

        private void StopScreenSaver() //停止屏幕保護程序運行
        {

            System.Windows.Forms.Cursor.Show();

            timerSaver.Enabled = false;

            Application.Exit();

        }


        private void screen_MouseMove(object sender, System.Windows.Forms.MouseEventArgs e)
        //鼠標移動事件
        {

            if (ixStart == 0 && iyStart == 0)
            {

                ixStart = e.X;

                iyStart = e.Y;

                return;

            }

            else if (e.X != ixStart || e.Y != iyStart)

                StopScreenSaver();

        }

        private void screen_MouseDown(object sender, System.Windows.Forms.MouseEventArgs e)	//鼠標按下事件
        {

            StopScreenSaver(); //停止運行屏幕保護程序

        }

        private void screen_KeyDown(object sender, System.Windows.Forms.KeyEventArgs e)　//鍵盤按下事件
        {

            StopScreenSaver(); //停止運行屏幕保護程序

        }





    }
}
