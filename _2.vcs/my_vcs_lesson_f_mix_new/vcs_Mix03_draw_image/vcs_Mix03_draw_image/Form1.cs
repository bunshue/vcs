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
using System.Drawing.Drawing2D;  // for GraphicsPath
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;

using System.Runtime.InteropServices;

namespace vcs_Mix03_draw_image
{
    public partial class Form1 : Form
    {
        //本程式截圖 ST
        [DllImportAttribute("gdi32.dll")]

        private static extern bool BitBlt(
        IntPtr hdcDest, //目的DC的句柄
        int nXDest, //目的圖形的左上角的x坐標
        int nYDest, //目的圖形的左上角的y坐標
        int nWidth, //目的圖形的矩形寬度
        int nHeight, //目的圖形的矩形高度
        IntPtr hdcSrc, //源DC的句柄
        int nXSrc, //源圖形的左上角的x坐標
        int nYSrc, //源圖形的左上角的x坐標
        System.Int32 dwRop //光柵操作代碼
        );
        //本程式截圖 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        //直接寫一個OnPaint在此
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10);
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

            //本程式截圖
            Graphics g1 = this.CreateGraphics();//獲得窗體圖形對象

            Image image = new Bitmap(this.ClientRectangle.Width, this.ClientRectangle.Height, g1);

            Graphics g2 = Graphics.FromImage(image);//創建位圖圖形對象

            IntPtr dc1 = g1.GetHdc();//獲得窗體的上下文設備

            IntPtr dc2 = g2.GetHdc();//獲得位圖文件的上下文設備

            BitBlt(dc2, 0, 0, this.ClientRectangle.Width, this.ClientRectangle.Height, dc1, 0, 0, 13369376);//寫入到位圖

            g1.ReleaseHdc(dc1);//釋放窗體的上下文設備

            g2.ReleaseHdc(dc2);//釋放位圖文件的上下文設備


            //自動檔名 與 存檔語法
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            try
            {
                image.Save(filename, ImageFormat.Bmp);
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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
            //全屏幕截圖 1

            int W = Screen.PrimaryScreen.Bounds.Width;

            int H = Screen.PrimaryScreen.Bounds.Height;

            Bitmap bitmap1 = new Bitmap(W, H); //創建一個與屏幕大小一樣的位圖

            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.CopyFromScreen(0, 0, 0, 0, new Size(W, H));  //用Graphics.CopyFromScreen()把屏幕位圖拷貝到該位圖上
            }
            pictureBox1.Image = bitmap1;



            //全屏幕截圖 2
            int width = Screen.PrimaryScreen.Bounds.Width;
            int height = Screen.PrimaryScreen.Bounds.Height;

            Bitmap bmp = new Bitmap(width, height);

            using (Graphics g = Graphics.FromImage(bmp))
            {
                g.CopyFromScreen(0, 0, 0, 0, new Size(width, height));
            }
            bmp.Save("111.jpg");

            //bmp.Dispose();
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = bmp;



            //全屏幕截圖 3
            //獲得當前屏幕的分辨率
            Screen scr = Screen.PrimaryScreen;
            Rectangle rc = scr.Bounds;
            int iWidth = rc.Width;
            int iHeight = rc.Height;
            //創建一個和屏幕一樣大的Bitmap
            Image myImage = new Bitmap(iWidth, iHeight);
            //從一個繼承自Image類的對象中創建Graphics對象
            Graphics g3 = Graphics.FromImage(myImage);
            //抓屏並拷貝到myimage裡
            g3.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(iWidth, iHeight));
            //保存為文件
            myImage.Save("aaaaaa.jpeg");


        }

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);


            double DPI = pictureBox1.Image.HorizontalResolution;//獲得分辨率 gisoracle
            double w = 1.0 * pictureBox1.Image.Width / DPI * 25.4;
            double h = 1.0 * pictureBox1.Image.Height / DPI * 25.4;

            MessageBox.Show(w.ToString("f2") + ":" + h.ToString("f2"));
        }

        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);


            /*
使圖像產生浮雕的效果，主要通過對圖像像素點的像素值分別與相鄰像素點的像素值相減後加上128，然後將其作為新的像素點的值。

以浮雕效果顯示圖像主要通過GetPixel方法獲得每一點像素的值，通過SetPixel設置該像素點的像素值。
*/

            //以浮雕效果顯示圖像
            try
            {
                int Height = this.pictureBox1.Image.Height;
                int Width = this.pictureBox1.Image.Width;
                Bitmap newBitmap = new Bitmap(Width, Height);
                Bitmap oldBitmap = (Bitmap)this.pictureBox1.Image;
                Color pixel1, pixel2;
                for (int x = 0; x < Width - 1; x++)
                {
                    for (int y = 0; y < Height - 1; y++)
                    {
                        int r = 0, g = 0, b = 0;
                        pixel1 = oldBitmap.GetPixel(x, y);
                        pixel2 = oldBitmap.GetPixel(x + 1, y + 1);
                        r = Math.Abs(pixel1.R - pixel2.R + 128);
                        g = Math.Abs(pixel1.G - pixel2.G + 128);
                        b = Math.Abs(pixel1.B - pixel2.B + 128);
                        if (r > 255)
                            r = 255;
                        if (r < 0)
                            r = 0;
                        if (g > 255)
                            g = 255;
                        if (g < 0)
                            g = 0;
                        if (b > 255)
                            b = 255;
                        if (b < 0)
                            b = 0;
                        newBitmap.SetPixel(x, y, Color.FromArgb(r, g, b));
                    }
                }
                this.pictureBox1.Image = newBitmap;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        //C#獲取圖片的指定部分
        /// <summary>
        /// 獲取圖片指定部分
        /// </summary>
        /// <param name="filename">圖片路徑</param>
        /// <param name="sx">原始圖片開始截取處的坐標X值</param>
        /// <param name="sy">原始圖片開始截取處的坐標Y值</param>
        /// <param name="sWidth">原始圖片的寬度</param>
        /// <param name="sHeight">原始圖片的高度</param>
        /// <param name="dx">目標圖片開始繪制處的坐標X值(通常為0)</param>
        /// <param name="dy">目標圖片開始繪制處的坐標Y值(通常為0)</param>
        /// <param name="dWidth">目標圖片的寬度</param>
        /// <param name="dHeight">目標圖片的高度</param>
        static Bitmap GetPart(string filename, int sx, int sy, int sWidth, int sHeight, int dx, int dy, int dWidth, int dHeight)
        {
            Image image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(dWidth, dHeight);
            Graphics g = Graphics.FromImage(bitmap1);
            Rectangle rec1 = new Rectangle(new Point(sx, sy), new Size(sWidth, sHeight));//原圖位置
            Rectangle rec2 = new Rectangle(new Point(dx, dy), new Size(dWidth, dHeight));//目標位置

            g.DrawImage(image, rec2, rec1, GraphicsUnit.Pixel);

            return bitmap1;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //取得圖片的一部分


            //取得圖片的一部分

            string filename = @"C:\______test_files\picture1.jpg";

            int sx = 0;
            int sy = 0;
            int sWidth = 305 / 2;
            int sHeight = 400 / 2;
            int dx = 0;
            int dy = 0;
            int dWidth = 305 / 1;
            int dHeight = 400 / 1;

            Bitmap bitmap1 = GetPart(filename, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);
            pictureBox1.Image = bitmap1;


        }

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //圖像邊緣提取

            /*
            用到的算法是robert算子，這是一種比較簡單的算法：

            f(x,y)=sqrt((g(x,y)-g(x+1,y+1))^2+(g(x+1,y)-g(x,y+1))^2)

            博主一共寫了三段代碼，第一段是邊緣提取，第二段是線條加粗，第三段是原圖和邊緣圖重合，三段代碼可以放在一起，但為了看得清晰我就把他們分開了。
            */

            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            if (this.pictureBox1.Image != null)
            {

                int Height = this.pictureBox1.Image.Height;
                int Width = this.pictureBox1.Image.Width;
                Bitmap bitmap = new Bitmap(Width, Height, PixelFormat.Format24bppRgb);
                Bitmap MyBitmap = (Bitmap)this.pictureBox1.Image;
                BitmapData oldData = MyBitmap.LockBits(new Rectangle(0, 0, Width, Height), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb); //原圖
                BitmapData newData = bitmap.LockBits(new Rectangle(0, 0, Width, Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);  //新圖即邊緣圖
                unsafe
                {
                    //首先第一段代碼是提取邊緣，邊緣置為黑色，其他部分置為白色
                    byte* pin_1 = (byte*)(oldData.Scan0.ToPointer());
                    byte* pin_2 = pin_1 + (oldData.Stride);
                    byte* pout = (byte*)(newData.Scan0.ToPointer());
                    for (int y = 0; y < oldData.Height - 1; y++)
                    {
                        for (int x = 0; x < oldData.Width; x++)
                        {
                            //使用robert算子
                            double b = System.Math.Sqrt(((double)pin_1[0] - (double)(pin_2[0] + 3)) * ((double)pin_1[0] - (double)(pin_2[0] + 3)) + ((double)(pin_1[0] + 3) - (double)pin_2[0]) * ((double)(pin_1[0] + 3) - (double)pin_2[0]));
                            double g = System.Math.Sqrt(((double)pin_1[1] - (double)(pin_2[1] + 3)) * ((double)pin_1[1] - (double)(pin_2[1] + 3)) + ((double)(pin_1[1] + 3) - (double)pin_2[1]) * ((double)(pin_1[1] + 3) - (double)pin_2[1]));
                            double r = System.Math.Sqrt(((double)pin_1[2] - (double)(pin_2[2] + 3)) * ((double)pin_1[2] - (double)(pin_2[2] + 3)) + ((double)(pin_1[2] + 3) - (double)pin_2[2]) * ((double)(pin_1[2] + 3) - (double)pin_2[2]));
                            double bgr = b + g + r;//博主一直在糾結要不要除以3，感覺沒差，選阈值的時候調整一下就好了- -

                            if (bgr > 80) //阈值，超過阈值判定為邊緣（選取適當的阈值）
                            {
                                b = 0;
                                g = 0;
                                r = 0;
                            }
                            else
                            {
                                b = 255;
                                g = 255;
                                r = 255;
                            }
                            pout[0] = (byte)(b);
                            pout[1] = (byte)(g);
                            pout[2] = (byte)(r);
                            pin_1 = pin_1 + 3;
                            pin_2 = pin_2 + 3;
                            pout = pout + 3;

                        }
                        pin_1 += oldData.Stride - oldData.Width * 3;
                        pin_2 += oldData.Stride - oldData.Width * 3;
                        pout += newData.Stride - newData.Width * 3;
                    }

                    //這裡博主加粗了一下線條- -，不喜歡的同學可以刪了這段代碼
                    byte* pin_5 = (byte*)(newData.Scan0.ToPointer());
                    for (int y = 0; y < oldData.Height - 1; y++)
                    {
                        for (int x = 3; x < oldData.Width; x++)
                        {
                            if (pin_5[0] == 0 && pin_5[1] == 0 && pin_5[2] == 0)
                            {
                                pin_5[-3] = 0;
                                pin_5[-2] = 0;
                                pin_5[-1] = 0;      //邊緣點的前一個像素點置為黑色（注意一定要是遍歷過的像素點）                                                    
                            }
                            pin_5 += 3;

                        }
                        pin_5 += newData.Stride - newData.Width * 3;
                    }

                    //這段代碼是把原圖和邊緣圖重合
                    byte* pin_3 = (byte*)(oldData.Scan0.ToPointer());
                    byte* pin_4 = (byte*)(newData.Scan0.ToPointer());
                    for (int y = 0; y < oldData.Height - 1; y++)
                    {
                        for (int x = 0; x < oldData.Width; x++)
                        {
                            if (pin_4[0] == 255 && pin_4[1] == 255 && pin_4[2] == 255)
                            {
                                pin_4[0] = pin_3[0];
                                pin_4[1] = pin_3[1];
                                pin_4[2] = pin_3[2];
                            }
                            pin_3 += 3;
                            pin_4 += 3;
                        }
                        pin_3 += oldData.Stride - oldData.Width * 3;
                        pin_4 += newData.Stride - newData.Width * 3;
                    }
                    //......
                    bitmap.UnlockBits(newData);
                    MyBitmap.UnlockBits(oldData);
                    this.pictureBox1.Image = bitmap;
                }
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);


            //TBD

            return;

            DrawingCurve MyDc = new DrawingCurve();

            Bitmap img = new Bitmap(100, 100);

            img = MyDc.DrawingImg();

            Graphics g = Graphics.FromImage(MyDc.DrawingImg());

            //显示图形
            pictureBox1.Image = img;
            //img.Save(Response.OutputStream, ImageFormat.Jpeg);;

            //g.Dispose();

            //Response.Write("<br>" + MyDc.intData.ToString());
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
            //畫貝茲線
            Graphics g = this.pictureBox1.CreateGraphics();
            Pen p = new Pen(Color.Red, 5);
            float startX = 50.0F;
            float startY = 80.0F;
            float controlX1 = 150.0F;
            float controlY1 = 20.0F;
            float controlX2 = 230.0F;
            float controlY2 = 50.0F;
            float endX = 190.0F;
            float endY = 80.0F;
            g.DrawBezier(p, startX, startY, controlX1, controlY1, controlX2, controlY2, endX, endY);
            //4個Point點分別表示起始點、第一個控制點、第二個控制點和結束點。

        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //Mandelbrot 圖形
            double realCoord, imagCoord;
            double realTemp, imagTemp, realTemp2, arg;
            int iterations;
            for (imagCoord = 1.2; imagCoord >= -1.2; imagCoord -= 0.05)
            {
                for (realCoord = -0.6; realCoord <= 1.77; realCoord += 0.03)
                {
                    iterations = 0;
                    realTemp = realCoord;
                    imagTemp = imagCoord;
                    arg = (realCoord * realCoord) + (imagCoord * imagCoord);
                    while ((arg < 4) && (iterations < 40))
                    {
                        realTemp2 = (realTemp * realTemp) - (imagTemp * imagTemp) - realCoord;
                        imagTemp = (2 * realTemp * imagTemp) - imagCoord;
                        realTemp = realTemp2;
                        arg = (realTemp * realTemp) + (imagTemp * imagTemp);
                        iterations += 1;
                    }
                    switch (iterations % 4)
                    {
                        case 0:
                            richTextBox1.Text += "."; break;
                        case 1:
                            richTextBox1.Text += "o"; break;
                        case 2:
                            richTextBox1.Text += "O"; break;
                        case 3:
                            richTextBox1.Text += "@"; break;
                    }
                }
                richTextBox1.Text += "\n";
            }
        }

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //畫棒圖
            Draw_Imgbar();
        }

        //畫棒圖
        void Draw_Imgbar()
        {
            //創建一個長度爲400，寬帶爲400的Bitmap實例
            Bitmap bmp = new Bitmap(400, 300);
            Graphics g;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Snow);
            string[] sitem = { "很好", "好", "一般", "差" };
            int[] num = { 1000, 69, 90, 2000 };
            int cnt, i, len, iBarWidth;
            float scale;
            float[] nflt;
            string header;
            header = "";
            cnt = 0;
            iBarWidth = 40;
            scale = 1;
            len = num.Length;
            //nflt.Length = len;
            nflt = new float[len];
            for (i = 0; i < len; i++)
            {
                cnt += num[i];
            }
            //flt = cnt /len;
            for (i = 0; i < len; i++)
            {
                nflt[i] = 200 * num[i] / cnt;
                //nflt[i] = scale * num[i]/cnt;
            }


            header = "調查統計結果一覽圖";
            g.DrawString(header, new Font("宋體", 12, FontStyle.Bold), Brushes.Black, new Point(75, 10));
            Point myRec = new Point(300, 40);
            Point myDec = new Point(320, 40);


            for (i = 0; i < len; i++)
            {
                g.DrawRectangle(Pens.Black, myRec.X, myRec.Y, 20, 10);
                //繪製小方塊
                g.FillRectangle(new SolidBrush(Return_Color(i)), myRec.X, myRec.Y, 20, 10);
                //填充小方塊
                g.DrawString(" " + sitem[i], new Font("宋體", 9), Brushes.Black, myDec);
                //繪製小方塊右邊的文字
                myRec.Y += 15;
                myDec.Y += 15;

                g.DrawRectangle(Pens.Black, (i * iBarWidth) + 15, 290 - (nflt[i] * scale), 20, (nflt[i] * scale) + 5);
                //繪製Bar圖
                g.FillRectangle(new SolidBrush(Return_Color(i)), (i * iBarWidth) + 15, 290 - (nflt[i] * scale), 20, (nflt[i] * scale) + 5);
                //以指定的色彩填充Bar圖
                g.DrawString(num[i].ToString(), new Font("宋體", 9), Brushes.Black, (i * iBarWidth) + 20, 275 - (nflt[i] * scale));
                //顯示Bar圖代表的數據

                //s = s + nflt[i];    
            }
            Pen p = new Pen(Color.Black, 1);
            g.DrawRectangle(p, 1, 1, 398, 298);
            //bmp.Save(Response.OutputStream, System.Drawing.Imaging.ImageFormat.Jpeg);
            bmp.Dispose();
        }

        private void button25_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //畫餅圖
            Draw_Img();
        }

        //畫餅圖
        void Draw_Img()
        {
            Bitmap bmp = new Bitmap(400, 300);
            //創建一個長度爲400，寬帶爲400的Bitmap實例
            Graphics g;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Snow);
            string[] sitem = { "很好", "好", "一般", "差" };
            int[] num = { 1000, 69, 90, 20 };
            int cnt, i, len;
            float s;
            float[] nflt;
            string header;
            header = "";
            cnt = 0;
            s = 0;
            len = num.Length;
            //nflt.Length = len;
            nflt = new float[len];
            for (i = 0; i < len; i++)
            {
                cnt += num[i];
            }
            //flt = cnt /len;
            for (i = 0; i < len; i++)
            {

                nflt[i] = 360 * num[i] / cnt;
            }


            header = "調查統計結果一覽圖";
            g.DrawString(header, new Font("宋體", 12, FontStyle.Bold), Brushes.Black, new Point(75, 10));
            g.DrawString("單位：次", new Font("宋體", 9), Brushes.Black, new Point(300, 25));

            Point myRec = new Point(300, 40);
            Point myDec = new Point(320, 40);


            for (i = 0; i < len; i++)
            {
                if (i == len - 1)
                {
                    //s = 360-s;
                    nflt[i] = 360 - s;
                }

                g.DrawRectangle(Pens.Black, myRec.X, myRec.Y, 20, 10);
                //繪製小方塊
                g.FillRectangle(new SolidBrush(Return_Color(i)), myRec.X, myRec.Y, 20, 10);
                //填充小方塊
                g.DrawString(" " + sitem[i] + " " + num[i], new Font("宋體", 9), Brushes.Black, myDec);
                //繪製小方塊右邊的文字
                myRec.Y += 15;
                myDec.Y += 15;

                g.FillPie(new SolidBrush(Return_Color(i)), 50, 50, 200, 200, s, nflt[i]);
                g.DrawPie(Pens.Black, 50, 50, 200, 200, s, nflt[i]);
                s = s + nflt[i];
            }
            Pen p = new Pen(Color.Black, 1);
            g.DrawRectangle(p, 1, 1, 398, 298);
            //bmp.Save(Response.OutputStream, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
        public Color Return_Color(int i)
        {
            switch (i)
            {
                case 0:
                    return Color.Red;
                //break;
                case 1:
                    return Color.Blue;
                //break;
                case 2:
                    return Color.Yellow;
                case 3:
                    return Color.Green;
                //break;
                case 4:
                    return Color.Pink;
                //break;
                case 5:
                    return Color.Plum;
                //break;
                case 6:
                    return Color.Gray;
                //break;
                case 7:
                    return Color.Salmon;
                //break;
                case 8:
                    return Color.RosyBrown;
                //break;
                case 9:
                    return Color.Teal;
                //break;
                case 10:
                    return Color.Orange;
                //break;
                case 11:
                    return Color.Thistle;
                //break;
                case 12:
                    return Color.Maroon;
                //break;
                default:
                    return Color.WhiteSmoke;
                //break;

            }
        }



        private void button26_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //色階調整

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            Bitmap bitmap2 = img_color_gradation(bitmap1, 0, 100, 0);

            pictureBox1.Image = bitmap2;


        }

        //色階調整
        public static unsafe Bitmap img_color_gradation(Bitmap src, int r, int g, int b)
        {
            int width = src.Width;
            int height = src.Height;
            Bitmap back = new Bitmap(width, height);
            Rectangle rect = new Rectangle(0, 0, width, height);
            //這種速度最快  
            BitmapData bmpData = src.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);//24位rgb顯示一個像素，即一個像素點3個字節，每個字節是BGR分量。Format32bppRgb是用4個字節表示一個像素  
            byte* ptr = (byte*)(bmpData.Scan0);
            for (int j = 0; j < height; j++)
            {
                for (int i = 0; i < width; i++)
                {
                    //ptr[2]爲r值，ptr[1]爲g值，ptr[0]爲b值  
                    int red = ptr[2] + r; if (red > 255) red = 255; if (red < 0) red = 0;
                    int green = ptr[1] + g; if (green > 255) green = 255; if (green < 0) green = 0;
                    int blue = ptr[0] + b; if (blue > 255) blue = 255; if (blue < 0) blue = 0;
                    back.SetPixel(i, j, Color.FromArgb(red, green, blue));
                    ptr += 3; //Format24bppRgb格式每個像素佔3字節  
                }
                ptr += bmpData.Stride - bmpData.Width * 3;//每行讀取到最後“有用”數據時，跳過未使用空間XX  
            }
            src.UnlockBits(bmpData);
            return back;
        }



        private void button27_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //格式轉換
            //Stream 和 byte[] 之間的轉換

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            // 打開文件
            FileStream fileStream = new FileStream(filename, FileMode.Open, FileAccess.Read, FileShare.Read);

            // 讀取文件的 byte[]
            byte[] bytes1 = new byte[fileStream.Length];
            fileStream.Read(bytes1, 0, bytes1.Length);
            fileStream.Close();

            // 把 byte[] 轉換成 Stream
            Stream stream = new MemoryStream(bytes1);



            // 將 Stream 轉成 byte[]
            byte[] bytes2 = new byte[stream.Length];
            stream.Read(bytes2, 0, bytes2.Length);
            // 設置當前流的位置為流的開始
            stream.Seek(0, SeekOrigin.Begin);

            // 將 byte[] 轉成 Stream
            Stream stream2 = new MemoryStream(bytes2);


            //將 Stream 寫入文件
            // 把 Stream 轉換成 byte[]
            byte[] bytes3 = new byte[stream.Length];
            stream.Read(bytes3, 0, bytes3.Length);
            // 設置當前流的位置為流的開始
            stream.Seek(0, SeekOrigin.Begin);

            // 把 byte[] 寫入文件
            FileStream fs = new FileStream("aaaaaa.jpg", FileMode.Create);
            BinaryWriter bw = new BinaryWriter(fs);
            bw.Write(bytes3);
            bw.Close();
            fs.Close();


            //二進制轉換成圖片

            MemoryStream ms = new MemoryStream(bytes3);
            ms.Position = 0;
            Image img = Image.FromStream(ms);
            ms.Close();
            pictureBox1.Image = img;





        }


        private void button28_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button29_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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

    /// <summary>
    /// DrawingCurve 的摘要說明
    /// </summary>
    public class DrawingCurve
    {
        public int intXLong = 800;   //圖片大小 長
        public int intYLong = 600;   //圖片大小 高
        public int intXMultiple = 1;    //零刻度的值 X

        public int intYMultiple = 0;    //零刻度的值 Y
        public int intXMax = 12;    //最大刻度(點數) X
        public int intYMax = 30;    //最大刻度(點數) Y

        public int intLeft = 50;   //左邊距
        public int intRight = 120; //右邊距
        public int intTop = 30;    //上邊距
        public int intEnd = 50;    //下邊距

        public string strXText = "時間(單位:月)";    //單位 X
        public string strYText = "數量(單位:個)";    //單位 Y
        public string strTitle = "趨勢線圖";    //標題
        public DataTable tbData;    //要統計的數據

        private int intXScale = 30;    //一刻度長度 X
        private int intYScale = 30;    //一刻度高度 Y
        //private int intX = 0;   //0點 X坐標
        //private int intY = 0;   //0點 Y坐標
        public int intData = 0;    //記錄數

        public DrawingCurve()
        {
            intXScale = (intXLong - intLeft - intRight) / (intXMax + 1);//一刻度長度 X
            intYScale = (intYLong - intTop - intEnd) / (intYMax + 1);//一刻度高度 Y

            //intX = intXLong - intLeft;   //0點 X坐標
            //intY = intYLong - intEnd;   //0點 Y坐標
        }

        public Bitmap DrawingImg()
        {
            Bitmap img = new Bitmap(intXLong, intYLong); //圖片大小
            Graphics g = Graphics.FromImage(img);

            g.Clear(Color.Snow);
            g.DrawString(strTitle, new Font("宋體", 14), Brushes.Black, new Point(5, 5));
            g.DrawLine(new Pen(Color.Black, 2), intLeft, intYLong - intEnd, intXLong - intRight, intYLong - intEnd); //繪制橫向
            g.DrawLine(new Pen(Color.Black, 2), intLeft, intTop, intLeft, intYLong - intEnd);   //繪制縱向

            //繪制縱坐標
            g.DrawString(strYText, new Font("宋體", 12), Brushes.Black, new Point(intLeft, intTop));//Y 單位
            Point p1 = new Point(intLeft - 10, intYLong - intEnd);

            for (int j = 0; j <= intYMax; j++)
            {

                p1.Y = intYLong - intEnd - j * intYScale;

                Point pt = new Point(p1.X + 10, p1.Y);
                //繪制縱坐標的刻度和直線
                g.DrawLine(Pens.Black, pt, new Point(p1.X + 15, p1.Y));
                //繪制縱坐標的文字說明
                g.DrawString(Convert.ToString(j + intYMultiple), new Font("宋體", 12), Brushes.Black, new Point(p1.X - 25, p1.Y - 8));
            }

            //繪制橫坐標
            g.DrawString(strXText, new Font("宋體", 12), Brushes.Black, new Point(intXLong - intRight, intYLong - intEnd));//X 單位
            Point p = new Point(intLeft, intYLong - intEnd);

            for (int i = 0; i < intXMax; i++)
            {

                p.X = intLeft + i * intXScale;
                //繪制橫坐標刻度和直線
                g.DrawLine(Pens.Black, p, new Point(p.X, p.Y - 5));
                //繪制橫坐標的文字說明
                g.DrawString(Convert.ToString(i + intXMultiple), new Font("宋體", 12), Brushes.Black, p);
            }

            intData = tbData.Rows.Count;
            if (intData > 0)
            {
                //趨勢線圖
                for (int i = 0; i < intData - 1; i++)
                {

                    DataRow Row1 = tbData.Rows[i];

                    DataRow Row2 = tbData.Rows[i + 1];
                    //定義起點
                    Point rec = new Point(Convert.ToInt32(intLeft + ((TurnNumber(Row1[0].ToString()) - intXMultiple) * intXScale)), Convert.ToInt32(intYLong - intEnd - (TurnNumber(Row1[1].ToString()) - intYMultiple) * intYScale));
                    //定義終點
                    Point dec = new Point(Convert.ToInt32(intLeft + ((TurnNumber(Row2[0].ToString()) - intXMultiple) * intXScale)), Convert.ToInt32(intYLong - intEnd - (TurnNumber(Row2[1].ToString()) - intYMultiple) * intYScale));
                    //繪制趨勢折線
                    g.DrawLine(new Pen(Color.Red), rec, dec);
                }
            }
            return img;
        }

        //转换数字
        private double TurnNumber(string str)
        {
            double dubReturn;
            try
            {
                dubReturn = Convert.ToDouble(str);
            }
            catch
            {
                dubReturn = 0;
            }
            return dubReturn;
        }
    }
}
