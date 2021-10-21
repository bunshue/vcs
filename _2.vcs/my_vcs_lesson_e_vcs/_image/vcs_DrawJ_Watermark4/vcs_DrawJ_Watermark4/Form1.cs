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

namespace vcs_DrawJ_Watermark4
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
            Graphics g = this.pictureBox1.CreateGraphics();
            addWatermarkText1(g, 10, "lion-mouse", "WM_TOP_LEFT", 150, 150);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            addWatermarkText2(g, "Top", 20, "mouse");
        }

        static void addWatermarkText1(Graphics g, int fontsize, string _watermarkText, string _watermarkPosition, int _width, int _height)
        {
            int[] sizes = new int[] { 32, 14, 12, 10, 8, 6, 4 };
            Font crFont = null;
            SizeF crSize = new SizeF();

            crFont = new Font("微軟雅黑", fontsize, FontStyle.Bold);
            crSize = g.MeasureString(_watermarkText, crFont);

            float xpos = 0;
            float ypos = 0;
            Color color = Color.Firebrick;

            switch (_watermarkPosition)
            {
                case "WM_TOP_LEFT":
                    xpos = ((float)_width * (float).01) + (crSize.Width / 2);
                    ypos = (float)_height * (float).01;
                    break;
                case "WM_TOP_RIGHT":
                    xpos = ((float)_width * (float).99) - (crSize.Width / 2);
                    ypos = (float)_height * (float).01;
                    break;
                case "WM_BOTTOM_RIGHT":
                    xpos = ((float)_width * (float).99) - (crSize.Width / 2);
                    ypos = ((float)_height * (float).99) - crSize.Height;
                    break;
                case "WM_BOTTOM_LEFT":
                    xpos = ((float)_width * (float).01) + (crSize.Width / 2);
                    ypos = ((float)_height * (float).99) - crSize.Height;
                    break;
            }

            StringFormat StrFormat = new StringFormat();
            StrFormat.Alignment = StringAlignment.Center;
            SolidBrush semiTransBrush2 = new SolidBrush(Color.FromArgb(153, 0, 0, 0));//加陰影
            g.DrawString(_watermarkText, crFont, semiTransBrush2, xpos + 1, ypos + 1, StrFormat);

            SolidBrush semiTransBrush = new SolidBrush(color);  //添加水印
            g.DrawString(_watermarkText, crFont, semiTransBrush, xpos, ypos, StrFormat);

            semiTransBrush2.Dispose();
            semiTransBrush.Dispose();
        }

        static void addWatermarkText2(Graphics g, string type, int fontsize, string _watermarkText)
        {
            //1、先畫矩形
            RectangleF drawRect;
            Color color;
            if (type == "Top")
            {
                drawRect = new RectangleF(73, 135, 450, 64);
                //color = Color.FromArgb(255, 255, 255);
                color = Color.Red;

            }
            else
            {
                drawRect = new RectangleF(194, 245, 250, 39);
                //color = Color.FromArgb(244, 226, 38);
                color = Color.Pink;
            }

            //2、在基於矩形畫水印文字
            Font crFont = null;

            StringFormat StrFormat = new StringFormat();
            StrFormat.Alignment = StringAlignment.Center;

            crFont = new Font("微軟雅黑", fontsize, FontStyle.Bold);
            SolidBrush semiTransBrush = new SolidBrush(color);  //添加水印
            g.DrawString(_watermarkText, crFont, semiTransBrush, drawRect, StrFormat);

            semiTransBrush.Dispose();
        }

        /*       和第一種方法比起來，第二種方法更直觀，更短小精悍，只需要在你需要添加水印的圖片上計算好固定坐標然後先畫一個矩形，然後把水印漢字畫在矩形內，這樣不管水印漢字如何變化都可以在圖片固定位置居中。
        */

        private void button3_Click(object sender, EventArgs e)
        {
            //讀取圖檔, 多一層Image結構
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);
            image = AddTextToImg(image, "lion-mouse");
            pictureBox1.Image = image;
        }

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


