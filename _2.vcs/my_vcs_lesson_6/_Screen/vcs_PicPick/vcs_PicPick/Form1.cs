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
using System.Diagnostics;       //for Process

namespace vcs_PicPick
{
    public partial class Form1 : Form
    {
        string foldername = @"C:\dddddddddd";

        int clear_label_count = 0;

        // The image of the whole screen.
        private Bitmap ScreenBm, VisibleBm;

        // The area we are selecting.
        private int X0, Y0, X1, Y1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //檢查存圖的資料夾
            if (Directory.Exists(foldername) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(foldername);
                richTextBox1.Text += "已建立一個新資料夾: " + foldername + "\n";
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + foldername + " 已存在，不用再建立\n";
            }
        }

        void show_item_location()
        {
            this.Text = string.Empty;
            this.ControlBox = false;
            this.BackColor = Color.LightPink;

            richTextBox1.Visible = false;
            label1.Text = "";

            button1.Location = new Point(10, 10);
            button1.Size = new Size(60, 60);
            button1.Visible = true;

            button2.Font = new Font(button2.Font.Name, 14);
            button2.Location = new Point(button1.Location.X + button1.Size.Width + 2, 10);
            button2.Size = new Size(115, 25);
            button2.Visible = true;

            button3.Font = new Font(button2.Font.Name, 14);
            button3.Location = new Point(button2.Location.X, button2.Location.Y + button2.Size.Height + 9);
            button3.Size = new Size(115, 25);
            button3.Visible = true;

            bt_open_folder.Location = new Point(button2.Location.X + button2.Size.Width + 5, button2.Location.Y + 5);
            bt_open_folder.BackgroundImage = Properties.Resources.folder_open;
            bt_open_folder.BackgroundImageLayout = ImageLayout.Zoom;

            label1.Location = new Point(10, button2.Location.Y + button2.Size.Height + button3.Size.Height + 15);

            this.Size = new Size(205 + 50, 110 + 35);

            //設定執行後的表單起始位置, 在螢幕的最右下方
            const int margin = 0;
            int x = Screen.PrimaryScreen.WorkingArea.Right - this.Width - margin;
            int y = Screen.PrimaryScreen.WorkingArea.Bottom - this.Height - margin;
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(x, y);
            //關閉最大化,最小化按鈕, 且固定不能改變表單大小
            //this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D;

            //this.ShowInTaskbar = false;     //false : 表單不顯示在 Windows 工作列中
            this.TopMost = true;
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

        private void button1_Click(object sender, EventArgs e)
        {
            IDataObject dataObject = Clipboard.GetDataObject();   //GetDataObject() 讀取當前剪貼簿中的數據內容
            if (dataObject.GetDataPresent(DataFormats.Bitmap))  //圖片類
            {
                richTextBox1.Text += "取得圖片\n";

                //取出Bitmap資料, 可做處理
                Bitmap bitmap1 = (Bitmap)dataObject.GetData(DataFormats.Bitmap);  //取得Bitmap資料
                if (bitmap1 != null)
                {
                    string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                    try
                    {
                        bitmap1.Save(@filename, ImageFormat.Jpeg);

                        //richTextBox1.Text += "存檔成功\n";
                        //richTextBox1.Text += "已存檔 : " + filename + "\n";
                        label1.Text = "存檔成功";
                        timer1.Enabled = true;
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                    }
                }
                else
                {
                    richTextBox1.Text += "無圖可存\n";
                    label1.Text = "無圖可存";
                    timer1.Enabled = true;
                }
            }
            else
            {
                richTextBox1.Text += "無圖片\n";
                label1.Text = "無圖片";
                timer1.Enabled = true;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();    // Hide this form.
            delay(100);

            /*
            //全螢幕截圖 法一
            //建立空白畫布
            Bitmap bitmap1 = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
            //取得畫布的繪圖物件用以繪圖
            Graphics g = Graphics.FromImage(bitmap1);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);

            //將裁切出的矩形存成JPG圖檔。
            string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            try
            {
                bitmap1.Save(@filename, ImageFormat.Jpeg);
                //richTextBox1.Text += "全螢幕截圖1，存檔檔名：" + filename + "\n";
                label1.Text = "存檔成功";
                timer1.Enabled = true;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
            */

            //全螢幕截圖 法二
            // Get the screen's image.
            using (Bitmap bitmap1 = GetScreenImage())
            {
                //存成bmp檔
                string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                bitmap1.Save(filename, ImageFormat.Bmp);
                //richTextBox1.Text += "全螢幕截圖1，存檔檔名：" + filename + "\n";
                label1.Text = "存檔成功";
                timer1.Enabled = true;
            }
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

        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

        // Let the user select a part of the screen.
        private void button3_Click(object sender, EventArgs e)
        {
            // Get the whole screen's image.
            ScreenBm = GetScreenImage();

            // Display a copy.
            VisibleBm = (Bitmap)ScreenBm.Clone();

            // Display it.
            button1.Visible = false;
            button2.Visible = false;
            button3.Visible = false;
            this.BackgroundImage = VisibleBm;
            this.Location = new Point(0, 0);
            this.ClientSize = VisibleBm.Size;
            this.MouseDown += Form1_MouseDown;
            this.Show();
        }

        // Start selecting an area.
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Down\n";
            X0 = e.X;
            Y0 = e.Y;
            X1 = e.X;
            Y1 = e.Y;

            this.MouseDown -= Form1_MouseDown;
            this.MouseMove += Form1_MouseMove;
            this.MouseUp += Form1_MouseUp;
        }

        // Continue selecting an area.
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            X1 = e.X;
            Y1 = e.Y;

            using (Graphics gr = Graphics.FromImage(VisibleBm))
            {
                // Copy the original image.
                gr.DrawImage(ScreenBm, 0, 0);

                // Draw the selected area.
                Rectangle rect = new Rectangle(
                    Math.Min(X0, X1),
                    Math.Min(Y0, Y1),
                    Math.Abs(X1 - X0),
                    Math.Abs(Y1 - Y0));
                gr.DrawRectangle(Pens.Yellow, rect);
            }
            this.Refresh();
        }

        // Finish selecting an area.
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Up\n";
            this.Visible = false;
            this.MouseMove -= Form1_MouseMove;
            this.MouseUp -= Form1_MouseUp;

            // Save the selected part of the image.
            int W = Math.Abs(X1 - X0);
            int H = Math.Abs(Y1 - Y0);
            Rectangle dest_rect = new Rectangle(0, 0, W, H);
            Rectangle source_rect = new Rectangle(
                Math.Min(X0, X1),
                Math.Min(Y0, Y1),
                Math.Abs(X1 - X0),
                Math.Abs(Y1 - Y0));

            using (Bitmap selection = new Bitmap(W, H))
            {
                // Copy the selected area.
                using (Graphics gr = Graphics.FromImage(selection))
                {
                    gr.DrawImage(ScreenBm, dest_rect, source_rect, GraphicsUnit.Pixel);
                }

                // Save the selected area.
                //存成bmp檔
                string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                selection.Save(filename, ImageFormat.Jpeg);
                //richTextBox1.Text += "全螢幕截圖1，存檔檔名：" + filename + "\n";
                Form1_Load(sender, e);
                label1.Text = "存檔成功";
                timer1.Enabled = true;
                this.Show();    // Show this form again.
            }

            // Dispose of the other bitmaps.
            this.BackgroundImage = null;
            ScreenBm.Dispose();
            VisibleBm.Dispose();
            ScreenBm = null;
            VisibleBm = null;
        }

        private void bt_open_folder_Click(object sender, EventArgs e)
        {
            //開啟檔案總管
            Process.Start(foldername);

        }
    }
}

