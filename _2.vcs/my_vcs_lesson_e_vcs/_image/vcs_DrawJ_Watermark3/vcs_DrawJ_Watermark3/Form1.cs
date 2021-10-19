using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.IO;

//C#圖片加水印

namespace vcs_DrawJ_Watermark3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //讀取圖檔, 多一層Image結構
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);
            pictureBox1.Image = image;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取圖檔, 多一層Image結構
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);

            image = AddTextToImg(image, "牡丹亭");

            pictureBox1.Image = image;
        }

        //圖片加水印
        public static Image AddTextToImg(Image image, string text)
        {
            Bitmap bitmap = new Bitmap(image, image.Width, image.Height);
            Graphics g = Graphics.FromImage(bitmap);

            float fontSize = 12.0f; //字體大小
            float textWidth = text.Length * fontSize; //文本的長度
            //下面定義一個矩形區域，以後在這個矩形裡畫上白底黑字
            float rectX = 0;
            float rectY = 0;
            float rectWidth = text.Length * (fontSize + 8);
            float rectHeight = fontSize + 8;
            //聲明矩形域
            RectangleF textArea = new RectangleF(rectX, rectY, rectWidth, rectHeight);

            Font font = new Font("宋體", fontSize); //定義字體
            Brush whiteBrush = new SolidBrush(Color.White); //白筆刷，畫文字用
            Brush blackBrush = new SolidBrush(Color.Black); //黑筆刷，畫背景用

            g.FillRectangle(blackBrush, rectX, rectY, rectWidth, rectHeight);

            g.DrawString(text, font, whiteBrush, textArea);
            MemoryStream ms = new MemoryStream();
            //保存為Jpg類型
            bitmap.Save(ms, ImageFormat.Jpeg);

            Image h_hovercImg = Image.FromStream(ms);

            g.Dispose();
            bitmap.Dispose();
            return h_hovercImg;
        }

    }
}
