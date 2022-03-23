using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D;
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;

namespace vcs_Mix03_draw_image
{
    public partial class Form1 : Form
    {
        DateTime start_time = DateTime.Now;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 80;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox_time.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 7 + 25);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //圖像切割

            string filename = @"C:\______test_files\picture1.jpg";
            ImageManager.Cut(filename, 300, 300);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            Bitmap bitmap1 = new Bitmap(300, 200);
            Graphics g = Graphics.FromImage(bitmap1);
            Font f = new Font("arial", 11f);
            Brush b = Brushes.Blue;

            string txt = "Rotate text animation!";
            SizeF sz = g.MeasureString(txt, f);
            g.Clear(Color.WhiteSmoke);
            g.DrawString(txt, f, b, 50 - sz.Width / 2, 50 - sz.Height / 2);
            g.Flush();

            for (int i = 1; i < 36; ++i)
            {
                g.Clear(Color.WhiteSmoke);
                g.TranslateTransform(50, 50);
                g.RotateTransform(10f * i);
                g.DrawString(txt, f, b, sz.Width / -2, sz.Height / -2);
                g.ResetTransform();
                g.DrawString("Hello", f, Brushes.Red, -50 + i * 4, 20);
                g.DrawString("Yeah", f, Brushes.Orange, 60, -20 + i * 4);

                g.Flush();

                pictureBox1.Image = bitmap1;
                Application.DoEvents();
                delay(300);
            }

            f.Dispose();
            g.Dispose();
            bitmap1.Dispose();

        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
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
            show_button_text(sender);
            //實現任意角度旋轉圖像主要使用Graphics類提供的RotateTransform()方法


            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            //pictureBox1.Image = bitmap1;

            //以任意角度旋轉顯示圖像
            Graphics g = this.pictureBox1.CreateGraphics();
            float MyAngle = 0;//旋轉的角度
            while (MyAngle < 360)
            {
                TextureBrush MyBrush = new TextureBrush(bitmap1);
                this.pictureBox1.Refresh();
                MyBrush.RotateTransform(MyAngle);
                g.FillRectangle(MyBrush, 0, 0, this.ClientRectangle.Width, this.ClientRectangle.Height);
                MyAngle += 0.5f;
                System.Threading.Thread.Sleep(50);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //實現任意角度旋轉圖片
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);

            //以任意角度旋轉顯示圖像
            Graphics g = this.pictureBox1.CreateGraphics();
            float angle = 0;//旋轉的角度
            while (angle < 360)
            {
                TextureBrush tb = new TextureBrush(image);
                this.pictureBox1.Refresh();
                tb.RotateTransform(angle);
                g.FillRectangle(tb, 0, 0, this.ClientRectangle.Width, this.ClientRectangle.Height);
                angle += 0.5f;
                System.Threading.Thread.Sleep(50);
            }



        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //不規則圖形裁剪圖片

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename, false);
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            GraphicsPath path = new GraphicsPath();

            Point[] p = {
                            new Point(W/2,10),
                            new Point(W/5,H/5),
                            new Point(10,H/2),
                            new Point(W/5,H*4/5),
                            new Point(W/2,H-10),
                            new Point(W*4/5,H*4/5),
                            new Point(W-10,H/2),
                            new Point(W*4/5,H/5),
                            new Point(W/2,10)
                        };
            path.AddLines(p);

            Bitmap bitmap2 = null;
            BitmapCrop(bitmap1, path, out bitmap2);
            pictureBox1.Image = bitmap2;

            bitmap2.Save(@"aaaaa.jpg");
        }

        /// <summary>
        /// 圖片截圖
        /// </summary>
        /// <param name="bitmap">原圖</param>
        /// <param name="path">裁剪路徑</param>
        /// <param name="outputBitmap">輸出圖</param>
        /// <returns></returns>
        public static Bitmap BitmapCrop(Bitmap bitmap, GraphicsPath path, out Bitmap outputBitmap)
        {
            RectangleF rect = path.GetBounds();
            int left = (int)rect.Left;
            int top = (int)rect.Top;
            int width = (int)rect.Width;
            int height = (int)rect.Height;
            Bitmap image = (Bitmap)bitmap.Clone();
            outputBitmap = new Bitmap(width, height);
            for (int i = left; i < left + width; i++)
            {
                for (int j = top; j < top + height; j++)
                {
                    //判斷坐標是否在路徑中   
                    if (path.IsVisible(i, j))
                    {
                        //復制原圖區域的像素到輸出圖片   
                        outputBitmap.SetPixel(i - left, j - top, image.GetPixel(i, j));
                        //設置原圖這部分區域為透明   
                        image.SetPixel(i, j, Color.FromArgb(0, image.GetPixel(i, j)));
                    }
                    else
                    {
                        outputBitmap.SetPixel(i - left, j - top, Color.FromArgb(0, 255, 255, 255));
                    }
                }
            }
            bitmap.Dispose();
            return image;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //用GetThumbnailImage製作小圖


            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;


            Bitmap bitmap2 = (Bitmap)bitmap1.GetThumbnailImage(bitmap1.Width / 3, bitmap1.Height / 3, null, IntPtr.Zero);
            pictureBox1.Image = bitmap2;

            //自動檔名 與 存檔語法
            string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap2.Save(filename2, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);


            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height, PixelFormat.Format24bppRgb);
            Graphics g = Graphics.FromImage(bitmap1);
            //Graphics g = this.CreateGraphics();
            g.Clear(Color.White);
            Font font = new Font(Font.Name, 11);
            SolidBrush brush = new SolidBrush(Color.Black);
            Pen pen = new Pen(Color.Black);
            pen.EndCap = LineCap.ArrowAnchor;
            pen.DashStyle = DashStyle.Solid;
            //坐标轴
            Point pCenter = new Point(300, 260);
            g.DrawLine(pen, new Point(pCenter.X - 200, pCenter.Y), new Point(pCenter.X + 200, pCenter.Y));//x
            g.DrawLine(pen, new Point(pCenter.X, pCenter.Y + 200), new Point(pCenter.X, pCenter.Y - 200));//y            
            int iX = 30;
            //轴标格
            for (int i = 0; i < 5; i++)
            {
                g.DrawLine(Pens.Black, new Point(pCenter.X - iX * i, pCenter.Y), new Point(pCenter.X - iX * i, pCenter.Y - 4));//x
                g.DrawString((-i).ToString(), font, brush, new PointF(pCenter.X - iX * i, pCenter.Y));
                g.DrawLine(Pens.Black, new Point(pCenter.X + iX * i, pCenter.Y), new Point(pCenter.X + iX * i, pCenter.Y - 4));//x
                g.DrawString(i.ToString(), font, brush, new PointF(pCenter.X + iX * i, pCenter.Y));
                g.DrawLine(Pens.Black, new Point(pCenter.X, pCenter.Y - iX * i), new Point(pCenter.X + 4, pCenter.Y - iX * i));//y
                g.DrawString(i.ToString(), font, brush, new PointF(pCenter.X, pCenter.Y - iX * i));
                g.DrawLine(Pens.Black, new Point(pCenter.X, pCenter.Y + iX * i), new Point(pCenter.X + 4, pCenter.Y + iX * i));//y
                g.DrawString((-i).ToString(), font, brush, new PointF(pCenter.X, pCenter.Y + iX * i));
            }

            StringFormat sf = new StringFormat();
            sf.Alignment = StringAlignment.Far;
            g.DrawString("x", font, brush, new PointF(pCenter.X + 200, pCenter.Y));
            g.DrawString("y", font, brush, new PointF(pCenter.X, pCenter.Y - 200));
            g.DrawString("0", font, brush, new PointF(pCenter.X, pCenter.Y));
            //定义比例尺
            int BX = 4;
            int BY = 4;
            Point new1 = getNewPoint(new Point(200, 300), pCenter, BX, BY);
            Point new2 = getNewPoint(new Point(-300, 400), pCenter, BX, BY);
            Point new3 = getNewPoint(new Point(-400, -500), pCenter, BX, BY);
            Point new4 = getNewPoint(new Point(500, -300), pCenter, BX, BY);
            //g.DrawLine(Pens.Black, pCenter, new1);
            g.DrawArc(Pens.Black, new1.X, new1.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p1", font, brush, new PointF(new1.X, new1.Y));
            g.DrawArc(Pens.Black, new2.X, new2.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p2", font, brush, new PointF(new2.X, new2.Y));
            g.DrawArc(Pens.Black, new3.X, new3.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p3", font, brush, new PointF(new3.X, new3.Y));
            g.DrawArc(Pens.Black, new4.X, new4.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p4", font, brush, new PointF(new4.X, new4.Y));
            g.DrawLine(Pens.Black, new1, new2);
            g.DrawLine(Pens.Black, new2, new3);
            g.DrawLine(Pens.Black, new3, new4);
            g.DrawLine(Pens.Black, new4, new1);
            bitmap1.Save("aaa.bmp");

            pictureBox1.Image = bitmap1;
            g.Dispose();

        }



        Point getNewPoint(Point p, Point pZero, int bx, int by)
        {
            Point myp = new Point();
            myp.X = pZero.X + p.X / bx;
            if (p.Y > 0)
                myp.Y = pZero.Y - Math.Abs(p.Y / by);
            else
                myp.Y = pZero.Y + Math.Abs(p.Y / by);
            return myp;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //字串旋轉列印
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawString("字串旋轉列印", new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(20, 20));

            Font f = new Font("標楷體", 50);
            RotateDeawString(g, f, 35, "字串旋轉列印", 20, 20);
        }

        /// <summary>
        /// 旋轉列印字串
        /// </summary>
        /// <param name="e">PrintPageEventArgs</param>
        /// <param name="font">字型</param>
        /// <param name="degree">旋轉角度</param>
        /// <param name="msg">列印訊息</param>
        /// <param name="x">重設原點 X 位置</param>
        /// <param name="y">重設原點 Y 位置</param>
        private void RotateDeawString(Graphics g, Font font, int degree, string msg, int x, int y)
        {
            // 原點位置重設
            g.TranslateTransform(mmTo100InchX(x), mmTo100InchY(y));
            // 設定旋轉角度
            g.RotateTransform(degree);
            // 標題
            g.DrawString(msg, font, Brushes.Black, mmTo100InchX(0), mmTo100InchY(0));
            //繪圖畫布還原
            g.ResetTransform();
        }

        private int mmTo100InchX(int mm)
        {
            int times = 100;
            double result = (mm * times / 25.4);
            return (int)Math.Floor(result);
        }

        private int mmTo100InchY(int mm)
        {
            int times = 100;
            double result = (mm * times / 25.4);
            return (int)Math.Floor(result);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            Bitmap bitmap2 = Process(bitmap1);

            pictureBox1.Image = bitmap2;


        }

        private static Bitmap Process(Bitmap bitmap)
        {
            //1.創建一個新的圖片
            Bitmap newBitmap = new Bitmap(bitmap.Width, bitmap.Height);
            //2.遍歷整個圖片
            for (int x = 0; x < bitmap.Width; x++)
            {
                for (int y = 0; y < bitmap.Height; y++)
                {
                    //3.去掉邊框操作
                    if (x == 0 || y == 0 || x == bitmap.Width - 1 || y == bitmap.Height - 1)
                    {
                        newBitmap.SetPixel(x, y, Color.White);
                    }
                    else
                    {

                        Color color = bitmap.GetPixel(x, y);
                        //4.如果點的顏色是背景干擾色就設置為白色
                        if (color.Equals(Color.FromArgb(204, 204, 51)) ||
                        color.Equals(Color.FromArgb(153, 204, 51)) ||
                        color.Equals(Color.FromArgb(204, 204, 204)) ||
                        color.Equals(Color.FromArgb(204, 255, 51)) ||
                        color.Equals(Color.FromArgb(204, 255, 102)))
                        {
                            newBitmap.SetPixel(x, y, Color.White);
                        }
                        else
                        {
                            //5.否則就設成原來的顏色
                            newBitmap.SetPixel(x, y, color);
                        }
                    }
                }
            }
            return newBitmap;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button17_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button19_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button20_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button25_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button26_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button27_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button28_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button29_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox_time.Invalidate();
        }

        private void pictureBox_time_Paint(object sender, PaintEventArgs e)
        {
            Font f = new Font("arial", 26f);

            DateTime current_time = DateTime.Now;

            TimeSpan use_time = current_time - start_time;

            string text = "空心字體 " + DateTime.Now + "    " + use_time.ToString(@"hh\:mm\:ss");

            for (var i = -1; i <= 1; ++i)
            {
                for (var j = -1; j <= 1; ++j)
                {
                    e.Graphics.DrawString(text, f, Brushes.Black, 2 + i, 2 + j);
                }
            }
            e.Graphics.DrawString(text, f, Brushes.White, 2, 2);
        }
    }

    public class ImageManager
    {
        /// <summary>
        /// 圖像切割
        /// </summary>
        /// <param name="url">圖像文件名稱</param>
        /// <param name="width">切割後圖像寬度</param>
        /// <param name="height">切割後圖像高度</param>
        public static void Cut(string filename1, int width, int height)
        {
            Bitmap bitmap1 = new Bitmap(filename1);
            Decimal MaxRow = Math.Ceiling((Decimal)bitmap1.Height / height);
            Decimal MaxColumn = Math.Ceiling((decimal)bitmap1.Width / width);
            for (decimal i = 0; i < MaxRow; i++)
            {
                for (decimal j = 0; j < MaxColumn; j++)
                {
                    //string filename = i.ToString() + "," + j.ToString() + "." + fileExt;
                    Bitmap bitmap2 = new Bitmap(width, height);
                    for (int offsetX = 0; offsetX < width; offsetX++)
                    {
                        for (int offsetY = 0; offsetY < height; offsetY++)
                        {
                            if (((j * width + offsetX) < bitmap1.Width) && ((i * height + offsetY) < bitmap1.Height))
                            {
                                bitmap2.SetPixel(offsetX, offsetY, bitmap1.GetPixel((int)(j * width + offsetX), (int)(i * height + offsetY)));
                            }
                        }
                    }
                    Graphics g = Graphics.FromImage(bitmap2);
                    //g.DrawString("", new Font("黑體", 20), new SolidBrush(Color.FromArgb(70, Color.WhiteSmoke)), 60, height / 2);//加水印

                    string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                    try
                    {
                        //bitmap2.Save(@file1, ImageFormat.Jpeg);
                        bitmap2.Save(filename2, ImageFormat.Bmp);
                        //bitmap2.Save(@file3, ImageFormat.Png);

                        //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                        //richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                        //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                    }
                    catch (Exception ex)
                    {
                        //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                    }
                }
            }
        }
    }
}
