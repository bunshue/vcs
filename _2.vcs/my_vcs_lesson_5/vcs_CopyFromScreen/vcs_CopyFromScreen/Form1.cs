using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Imaging;   //ImageFormat

namespace vcs_CopyFromScreen
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            save_fullscreen_to_local_drive();       //全螢幕截圖
        }

        void save_fullscreen_to_local_drive()
        {
            //全螢幕截圖
            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;

            using (Bitmap bitmap1 = new Bitmap(W, H))   //建立空白畫布
            {
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    //取得畫布的繪圖物件用以繪圖
                    g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(W, H));
                    //richTextBox1.Text += "W = " + W.ToString() + "\n";
                    //richTextBox1.Text += "H = " + H.ToString() + "\n";
                    IntPtr dc1 = g.GetHdc();
                    g.ReleaseHdc(dc1);
                }

                //存成bmp檔
                String filename = Application.StartupPath + "\\image_full_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    bitmap1.Save(filename, ImageFormat.Bmp);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                richTextBox1.Text += "全螢幕截圖，存檔檔名：" + filename + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            save_current_program_to_local_drive();  //本程式截圖
        }

        void save_current_program_to_local_drive()
        {
            //本程式截圖
            int W = this.Width;
            int H = this.Height;

            using (Bitmap bitmap1 = new Bitmap(W, H))
            {
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    //public void CopyFromScreen(int sourceX, int sourceY, int destinationX, int destinationY, System.Drawing.Size blockRegionSize);
                    g.CopyFromScreen(this.Location, new Point(0, 0), new Size(W, H));
                    //richTextBox1.Text += "W = " + W.ToString() + "\n";
                    //richTextBox1.Text += "H = " + H.ToString() + "\n";
                    IntPtr dc1 = g.GetHdc();
                    g.ReleaseHdc(dc1);
                }

                //存成bmp檔
                String filename = Application.StartupPath + "\\image_this_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    bitmap1.Save(filename, ImageFormat.Bmp);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }

                //存成jpg檔
                //String filename = Application.StartupPath + "\\image_this_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                //bitmap1.Save(filename, ImageFormat.Jpeg);

                richTextBox1.Text += "本程式截圖，存檔檔名：" + filename + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //抓螢幕某區塊為檔案
            Image image = new Bitmap(410, 410);   //宣告Image類別
            Graphics g = Graphics.FromImage(image);
            g.CopyFromScreen(new Point(340, 255), new Point(0, 0), new Size(410, 410));
            //取得螢幕上x=340 y=255為左上角，長寬為410的區域
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            //this.pictureBox1.Image = image;   若有picturebox 可以貼上

            //存成bmp檔
            String filename = Application.StartupPath + "\\image_partial_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            try
            {
                image.Save(filename, ImageFormat.Bmp); //把圖片存起來
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

            richTextBox1.Text += "已部分截圖存檔完成, 檔名 : " + filename + "\n";

            //存成jpg檔
            //String filename = Application.StartupPath + "\\image_partial_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            //image.Save(filename, ImageFormat.Jpeg); //把圖片存起來
            //richTextBox1.Text += "已部分截圖存檔完成, 檔名 : " + filename + "\n";
        }
    }
}
