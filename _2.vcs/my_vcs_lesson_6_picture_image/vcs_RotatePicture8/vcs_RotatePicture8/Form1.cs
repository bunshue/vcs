using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RotatePicture8
{
    public partial class Form1 : Form
    {
        float angle = 0;
        string filename = @"C:\______test_files1\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Image image = Image.FromFile(filename);
            pictureBox1.Image = image;
            pictureBox1.Size = new Size(image.Width, image.Height);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            angle += 15;

            string filename = @"C:\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);

            Image image_rotated = image.GetRotateImage(angle);

            pictureBox1.Image = image_rotated;
            pictureBox1.Size = new Size(image_rotated.Width, image_rotated.Height);
        }
    }

    public static class ImageEx
    {
        public static Image GetRotateImage(this Image img, float angle)
        {
            angle = angle % 360;//弧度轉換
            double radian = angle * Math.PI / 180.0;
            double cos = Math.Cos(radian);
            double sin = Math.Sin(radian);
            //原圖的寬和高
            int w = img.Width;
            int h = img.Height;
            int W = (int)(Math.Max(Math.Abs(w * cos - h * sin), Math.Abs(w * cos + h * sin)));
            int H = (int)(Math.Max(Math.Abs(w * sin - h * cos), Math.Abs(w * sin + h * cos)));

            Console.WriteLine("W = " + W.ToString() + ", H = " + H.ToString());

            //目標位圖
            Image dsImage = new Bitmap(W, H, img.PixelFormat);
            using (System.Drawing.Graphics g = System.Drawing.Graphics.FromImage(dsImage))
            {
                g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.Bilinear;
                g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                g.Clear(Color.White);
                //計算偏移量
                Point Offset = new Point((W - w) / 2, (H - h) / 2);
                //構造圖像顯示區域：讓圖像的中心與窗口的中心點一致
                Rectangle rect = new Rectangle(Offset.X, Offset.Y, w, h);
                Point center = new Point(rect.X + rect.Width / 2, rect.Y + rect.Height / 2);
                g.TranslateTransform(center.X, center.Y);
                g.RotateTransform(360 - angle);
                //恢復圖像在水平和垂直方向的平移
                g.TranslateTransform(-center.X, -center.Y);
                g.DrawImage(img, rect);
                //重至繪圖的所有變換
                g.ResetTransform();
                g.Save();
            }
            return dsImage;
        }
    }
}

