using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                //for Directory
using System.Drawing.Imaging;   //for ImageFormat
using System.Threading;//延時函式要用

namespace vcs_PicPick2
{
    public partial class Form1 : Form
    {
        bool flag_mouse_down = false;
        bool flag_have_painted = false;
        Point start, end;
        Point start1, end1;
        Size size = new Size(0, 0);

        int clear_label_count = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";

            //檢查存圖的資料夾
            string Path = @"C:\dddddddddd";
            if (Directory.Exists(Path) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(Path);
                //richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //自訂截圖存檔
            ReadyToCaptrue();
        }

        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //全螢幕截圖存檔

            this.Hide();    // Hide this form.
            delay(100);

            ReadyToCaptrueFullScreen();

            this.Show();    // Show this form again.
        }

        // Get the screen's image.
        private Bitmap GetScreenImage()
        {
            // Make a bitmap to hold the result.
            Bitmap bitmap1 = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height, PixelFormat.Format24bppRgb);

            // Copy the image into the bitmap.
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.CopyFromScreen(Screen.PrimaryScreen.Bounds.X, Screen.PrimaryScreen.Bounds.Y, 0, 0, Screen.PrimaryScreen.Bounds.Size, CopyPixelOperation.SourceCopy);
            }

            // Return the result.
            return bitmap1;
        }

        private void ReadyToCaptrueFullScreen()
        {
            // Get the screen's image.
            using (Bitmap bitmap1 = GetScreenImage())
            {
                //存成bmp檔
                string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                bitmap1.Save(filename, ImageFormat.Jpeg);
                //richTextBox1.Text += "全螢幕截圖1，存檔檔名：" + filename + "\n";
                label1.Text = "存檔成功";
                timer1.Enabled = true;
            }


        }

        private void ReadyToCaptrue()
        {
            this.Opacity = 0.1;
            panel1.Visible = false;
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            start = e.Location;
            flag_mouse_down = true;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                if (size.Width != 0 && size.Height != 0 && (flag_have_painted == true))
                {
                    ControlPaint.DrawReversibleFrame(new Rectangle(start1, size), Color.Transparent, FrameStyle.Dashed);
                }
                end1 = e.Location;
                size.Width = Math.Abs(end1.X - start.X);
                size.Height = Math.Abs(end1.Y - start.Y);
                start1.X = (start.X > end1.X) ? end1.X : start.X;
                start1.Y = (start.Y > end1.Y) ? end1.Y : start.Y;

                if (size.Width != 0 && size.Height != 0)
                {
                    ControlPaint.DrawReversibleFrame(new Rectangle(start1, size), Color.Transparent, FrameStyle.Dashed);
                    flag_have_painted = true;
                }
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            if (size.Width != 0 && size.Height != 0)
            {
                ControlPaint.DrawReversibleFrame(new Rectangle(start1, size), Color.Transparent, FrameStyle.Dashed);
                flag_have_painted = false;
            }
            end = e.Location;
            if (start.X > end.X)
            {
                int temp = end.X;
                end.X = start.X;
                start.X = temp;
            }

            if (start.Y > end.Y)
            {
                int temp = end.Y;
                end.Y = start.Y;
                start.Y = temp;
            }
            this.Opacity = 0.0;
            Thread.Sleep(200);
            if (end.X - start.X > 0 && end.Y - start.Y > 0)
            {
                Bitmap bitmap1 = new Bitmap(end.X - start.X, end.Y - start.Y);
                Graphics g = Graphics.FromImage(bitmap1);
                g.CopyFromScreen(start, new Point(0, 0), bitmap1.Size);

                //自訂截圖存檔
                String filename = "C:\\dddddddddd\\part_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                bitmap1.Save(filename, ImageFormat.Bmp);
                //richTextBox1.Text += "全螢幕截圖，存檔檔名：\n" + filename + "\n";

                //複製到剪貼簿
                Clipboard.SetImage(bitmap1);

                g.Dispose();
            }
            this.WindowState = FormWindowState.Normal;
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            panel1.Visible = true;
            this.Opacity = 1;
            flag_mouse_down = false;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            clear_label_count++;
            if (clear_label_count == 3)
            {
                clear_label_count = 0;
                label1.Text = "";
                timer1.Enabled = false;
            }

        }
    }
}

