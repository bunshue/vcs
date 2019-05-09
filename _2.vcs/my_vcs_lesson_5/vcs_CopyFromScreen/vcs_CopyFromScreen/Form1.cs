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
            //全螢幕截圖
            //建立空白畫布
            Bitmap myImage = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
            //取得畫布的繪圖物件用以繪圖
            Graphics g = Graphics.FromImage(myImage);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);

            String file1 = Application.StartupPath + "\\image_full_" + DateTime.Now.ToString("yyyyMMdd_hhmmss") + ".jpg";
            //將裁切出的矩形存成JPG圖檔。
            myImage.Save(file1);
            richTextBox1.Text += "全螢幕截圖1，存檔檔名：" + file1 + "\n";

            //將裁切出的矩形存成其他格式
            String file2 = Application.StartupPath + "\\image_full_" + DateTime.Now.ToString("yyyyMMdd_hhmmss") + ".bmp";
            Image imgCanvas = (Image)myImage;
            imgCanvas.Save(file2, ImageFormat.Bmp);
            richTextBox1.Text += "全螢幕截圖2，存檔檔名：" + file2 + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //本程式截圖
            Bitmap myImage = new Bitmap(this.Width, this.Height);
            Graphics g = Graphics.FromImage(myImage);
            //public void CopyFromScreen(int sourceX, int sourceY, int destinationX, int destinationY, System.Drawing.Size blockRegionSize);
            g.CopyFromScreen(this.Location, new Point(0, 0), new Size(this.Width, this.Height));
            //richTextBox1.Text += "W = " + this.Width.ToString() + "\n";
            //richTextBox1.Text += "H = " + this.Height.ToString() + "\n";
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            String file = Application.StartupPath + "\\image_this_" + DateTime.Now.ToString("yyyyMMdd_hhmmss") + ".jpg";
            myImage.Save(file);
            richTextBox1.Text += "本程式截圖，存檔檔名：" + file + "\n";

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
            String file = Application.StartupPath + "\\image_partial_" + DateTime.Now.ToString("yyyyMMdd_hhmmss") + ".jpg";
            image.Save(file, ImageFormat.Jpeg); //把圖片存起來
            richTextBox1.Text += "已部分截圖存檔完成, 檔名 : " + file + "\n";
        }
    }
}
