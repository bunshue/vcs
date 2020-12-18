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

namespace vcs_PicPick
{
    public partial class Form1 : Form
    {
        int clear_label_count = 0;
        
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Visible = false;
            label1.Text = "";
            //show_item_location();

            string Path;
            //檢查存d10d的資料夾
            Path = "C:\\dddddddddd";
            if (Directory.Exists(Path) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(Path);
                richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
            }
            else
                richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";

            button1.Text = "截圖存檔";
            button1.Location = new Point(10, 10);
            button1.Size = new Size(60, 50);

            button2.Font = new Font(button2.Font.Name, 14);
            button2.Text = "全螢幕截圖";
            button2.Location = new Point(button1.Location.X + button1.Size.Width + 2, 10);
            button2.Size = new Size(115, 25);

            label1.Location = new Point(75, 40);

            this.Size = new Size(205, 110);

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
                string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                bitmap1.Save(filename, ImageFormat.Jpeg);
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

    }
}
