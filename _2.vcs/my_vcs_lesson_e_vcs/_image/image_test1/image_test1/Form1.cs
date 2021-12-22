using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ColorAdjustType
using System.Drawing.Drawing2D;

namespace image_test1
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
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
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            label1.Location = new Point(x_st + dx * 2, y_st + dy * 0+20);
            pictureBox2.Location = new Point(x_st + dx * 3+100, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            richTextBox1.Location = new Point(x_st + dx * 6 - 50, y_st + dy * 0);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //圖片剪下一塊存檔
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = @"C:\______test_files\picture1_cut.jpg";

            ImgReduceCutOut(200, 200, filename1, filename2);
        }

        //C# 圖片裁剪代碼，
        /// <summary>
        /// 縮小裁剪圖片
        /// </summary>
        /// <param name="int_Width">要縮小裁剪圖片寬度</param>
        /// <param name="int_Height">要縮小裁剪圖片長度</param>
        /// <param name="filename_old">要處理圖片路徑</param>
        /// <param name="filename_new">處理完畢圖片路徑</param>
        public void ImgReduceCutOut(int int_Width, int int_Height, string filename_old, string filename_new)
        {
            // ＝＝＝上傳標准圖大小＝＝＝
            int int_Standard_Width = 160;
            int int_Standard_Height = 160;

            int Reduce_Width = 0; // 縮小的寬度
            int Reduce_Height = 0; // 縮小的高度
            int CutOut_Width = 0; // 裁剪的寬度
            int CutOut_Height = 0; // 裁剪的高度
            int level = 100; //縮略圖的質量 1-100的范圍

            // ＝＝＝獲得縮小，裁剪大小＝＝＝
            if (int_Standard_Height * int_Width / int_Standard_Width > int_Height)
            {
                Reduce_Width = int_Width;
                Reduce_Height = int_Standard_Height * int_Width / int_Standard_Width;
                CutOut_Width = int_Width;
                CutOut_Height = int_Height;
            }
            else if (int_Standard_Height * int_Width / int_Standard_Width < int_Height)
            {
                Reduce_Width = int_Standard_Width * int_Height / int_Standard_Height;
                Reduce_Height = int_Height;
                CutOut_Width = int_Width;
                CutOut_Height = int_Height;
            }
            else
            {
                Reduce_Width = int_Width;
                Reduce_Height = int_Height;
                CutOut_Width = int_Width;
                CutOut_Height = int_Height;
            }

            // ＝＝＝通過連接創建Image對象＝＝＝
            Image oldimage = Image.FromFile(filename_old);

            // ＝＝＝縮小圖片＝＝＝
            Image thumbnailImage = oldimage.GetThumbnailImage(Reduce_Width, Reduce_Height, new Image.GetThumbnailImageAbort(ThumbnailCallback), IntPtr.Zero);
            Bitmap bm = new Bitmap(thumbnailImage);

            // ＝＝＝處理JPG質量的函數＝＝＝
            ImageCodecInfo[] codecs = ImageCodecInfo.GetImageEncoders();
            ImageCodecInfo ici = null;
            foreach (ImageCodecInfo codec in codecs)
            {
                if (codec.MimeType == "image/jpeg")
                    ici = codec;
            }
            EncoderParameters ep = new EncoderParameters();

            //Encoder myEncoder = Encoder.Quality;

            // Create an Encoder object based on the GUID  
            // for the Quality parameter category.  
            System.Drawing.Imaging.Encoder myEncoder = System.Drawing.Imaging.Encoder.Quality;

            ep.Param[0] = new EncoderParameter(myEncoder, (long)level);

            //bm.Save(Server.MapPath("2.jpg"), ici, ep);

            // ＝＝＝裁剪圖片＝＝＝
            Rectangle cloneRect = new Rectangle(0, 0, CutOut_Width, CutOut_Height);
            PixelFormat format = bm.PixelFormat;
            Bitmap cloneBitmap = bm.Clone(cloneRect, format);

            // ＝＝＝保存圖片＝＝＝
            cloneBitmap.Save(filename_new, ici, ep);
        }

        public bool ThumbnailCallback()
        {
            return true;
        }

        private void GetThumbnail(PaintEventArgs e)
        {
            Image.GetThumbnailImageAbort callback =
                new Image.GetThumbnailImageAbort(ThumbnailCallback);
            Image image = new Bitmap(@"c:\dddddddddd\FakePhoto.jpg");
            Image pThumbnail = image.GetThumbnailImage(100, 100, callback, new
               IntPtr());
            e.Graphics.DrawImage(
               pThumbnail,
               10,
               10,
               pThumbnail.Width,
               pThumbnail.Height);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //使用byte[]數據，生成Bitmap
            //使用byte[]數據，生成Bitmap

            int W = 256;
            int H = 256;
            byte[] imagedata = new byte[W * H];

            int i;
            int j;
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    imagedata[256 * i + j] = (byte)i;
                }
            }
            Bitmap bitmap1 = CreateBitmap(imagedata, W, H);
            pictureBox1.Image = bitmap1;
        }

        //C#中使用byte[]數據，生成Bitmap
        /// <summary>
        /// 使用byte[]數據，生成256色灰度　BMP 位圖
        /// </summary>
        /// <param name="originalImageData"></param>
        /// <param name="originalWidth"></param>
        /// <param name="originalHeight"></param>
        /// <returns></returns>
        public static Bitmap CreateBitmap(byte[] originalImageData, int originalWidth, int originalHeight)
        {
            //指定8位格式，即256色
            Bitmap resultBitmap = new Bitmap(originalWidth, originalHeight, System.Drawing.Imaging.PixelFormat.Format8bppIndexed);
            //將該位圖存入內存中
            MemoryStream curImageStream = new MemoryStream();
            resultBitmap.Save(curImageStream, System.Drawing.Imaging.ImageFormat.Bmp);
            curImageStream.Flush();
            //由於位圖數據需要DWORD對齊（4byte倍數），計算需要補位的個數
            int curPadNum = ((originalWidth * 8 + 31) / 32 * 4) - originalWidth;
            //最終生成的位圖數據大小
            int bitmapDataSize = ((originalWidth * 8 + 31) / 32 * 4) * originalHeight;
            //數據部分相對文件開始偏移，具體可以參考位圖文件格式
            int dataOffset = ReadData(curImageStream, 10, 4);
            //改變調色板，因為默認的調色板是32位彩色的，需要修改為256色的調色板
            int paletteStart = 54;
            int paletteEnd = dataOffset;
            int color = 0;
            for (int i = paletteStart; i < paletteEnd; i += 4)
            {
                byte[] tempColor = new byte[4];
                tempColor[0] = (byte)color;
                tempColor[1] = (byte)color;
                tempColor[2] = (byte)color;
                tempColor[3] = (byte)0;
                color++;
                curImageStream.Position = i;
                curImageStream.Write(tempColor, 0, 4);
            }
            //最終生成的位圖數據，以及大小，高度沒有變，寬度需要調整
            byte[] destImageData = new byte[bitmapDataSize];
            int destWidth = originalWidth + curPadNum;
            //生成最終的位圖數據，注意的是，位圖數據 從左到右，從下到上，所以需要顛倒
            for (int originalRowIndex = originalHeight - 1; originalRowIndex >= 0; originalRowIndex--)
            {
                int destRowIndex = originalHeight - originalRowIndex - 1;
                for (int dataIndex = 0; dataIndex < originalWidth; dataIndex++)
                {
                    //同時還要注意，新的位圖數據的寬度已經變化destWidth，否則會產生錯位
                    destImageData[destRowIndex * destWidth + dataIndex] = originalImageData[originalRowIndex * originalWidth + dataIndex];
                }
            }
            //將流的Position移到數據段　　
            curImageStream.Position = dataOffset;
            //將新位圖數據寫入內存中
            curImageStream.Write(destImageData, 0, bitmapDataSize);
            curImageStream.Flush();
            //將內存中的位圖寫入Bitmap對象
            resultBitmap = new Bitmap(curImageStream);
            return resultBitmap;
        }

        /// <summary>
        /// 從內存流中指定位置，讀取數據
        /// </summary>
        /// <param name="curStream"></param>
        /// <param name="startPosition"></param>
        /// <param name="length"></param>
        /// <returns></returns>
        public static int ReadData(MemoryStream curStream, int startPosition, int length)
        {
            int result = -1;
            byte[] tempData = new byte[length];
            curStream.Position = startPosition;
            curStream.Read(tempData, 0, length);
            result = BitConverter.ToInt32(tempData, 0);
            return result;
        }

        /// <summary>
        /// 向內存流中指定位置，寫入數據
        /// </summary>
        /// <param name="curStream"></param>
        /// <param name="startPosition"></param>
        /// <param name="length"></param>
        /// <param name="value"></param>
        public static void WriteData(MemoryStream curStream, int startPosition, int length, int value)
        {
            curStream.Position = startPosition;
            curStream.Write(BitConverter.GetBytes(value), 0, length);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //底片效果
            //原理: GetPixel方法獲得每一點像素的值, 然後再使用SetPixel方法將取反後的顏色值設置到對應的點.
            //以底片效果顯示圖像
            try
            {
                int Height = this.pictureBox1.Image.Height;
                int Width = this.pictureBox1.Image.Width;
                Bitmap newbitmap = new Bitmap(Width, Height);
                Bitmap oldbitmap = (Bitmap)this.pictureBox1.Image;
                Color pixel;
                for (int x = 1; x < Width; x++)
                {
                    for (int y = 1; y < Height; y++)
                    {
                        int r, g, b;
                        pixel = oldbitmap.GetPixel(x, y);
                        r = 255 - pixel.R;
                        g = 255 - pixel.G;
                        b = 255 - pixel.B;
                        newbitmap.SetPixel(x, y, Color.FromArgb(r, g, b));
                    }
                }
                this.pictureBox1.Image = newbitmap;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //浮雕效果
            //原理: 對圖像像素點的像素值分別與相鄰像素點的像素值相減後加上128, 然後將其作為新的像素點的值
            //以浮雕效果顯示圖像
            //C#實現浮雕效果顯示圖片

            /*
            使圖像產生浮雕的效果，主要通過對圖像像素點的像素值分別與相鄰像素點的像素值相減後加上128，然後將其作為新的像素點的值。
            以浮雕效果顯示圖像主要通過GetPixel方法獲得每一點像素的值，通過SetPixel設置該像素點的像素值。
            */

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

        private void button4_Click(object sender, EventArgs e)
        {
            //Image Cut
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            string mesg = "lion-mouse";

            Cut(filename1, filename2, 200, 200, mesg);
        }

        /// <summary>
        /// 圖像切割
        /// </summary>
        /// <param name="filename1">原圖片路徑</param>
        /// <param name="filename2">切割後圖片路徑</param>
        /// <param name="width">切割後圖像寬度</param>
        /// <param name="height">切割後圖像高度</param>
        public static void Cut(string filename1, string filename2, int width, int height, string message)
        {
            Bitmap bitmap = new Bitmap(filename1);
            Decimal MaxRow = Math.Ceiling((Decimal)bitmap.Height / height);
            Decimal MaxColumn = Math.Ceiling((decimal)bitmap.Width / width);
            for (decimal i = 0; i < MaxRow; i++)
            {
                for (decimal j = 0; j < MaxColumn; j++)
                {
                    Bitmap bitmap1 = new Bitmap(width, height);
                    for (int offsetX = 0; offsetX < width; offsetX++)
                    {
                        for (int offsetY = 0; offsetY < height; offsetY++)
                        {
                            if (((j * width + offsetX) < bitmap.Width) && ((i * height + offsetY) < bitmap.Height))
                            {
                                bitmap1.SetPixel(offsetX, offsetY, bitmap.GetPixel((int)(j * width + offsetX), (int)(i * height + offsetY)));
                            }
                        }
                    }
                    Graphics g = Graphics.FromImage(bitmap1);
                    g.DrawString(message, new Font("黑體", 20), new SolidBrush(Color.FromArgb(70, Color.WhiteSmoke)), 0, 0);//加水印

                    try
                    {
                        //bitmap1.Save(@file1, ImageFormat.Jpeg);
                        bitmap1.Save(filename2, ImageFormat.Bmp);
                        //bitmap1.Save(@file3, ImageFormat.Png);

                        //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                        //richTextBox1.Text += "已存檔 : " + filename + "\n";
                        //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                    }
                    catch (Exception ex)
                    {
                        //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                    }
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            float gamma = 1.5f;

            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            Bitmap bitmap2 = KiGamma(bitmap1, gamma);

            pictureBox1.Image = bitmap2;

        }


        //C#圖片處理之Gamma校正
        //gamma值是用曲線表示的，這是一種人的眼睛對光的一種感應曲線，其中包括了物理量、身理感官及心理的感知度。

        /// <summary>
        /// Gamma校正
        /// </summary>
        /// <param name="bmp">輸入Bitmap</param>
        /// <param name="val">[0 <-明- 1 -暗-> 2]</param>
        /// <returns>輸出Bitmap</returns>
        public static Bitmap KiGamma(Bitmap bmp, float val)
        {
            if (bmp == null)
            {
                return null;
            }

            // 1表示無變化，就不做
            if (val == 1.0000f) return bmp;

            try
            {
                Bitmap b = new Bitmap(bmp.Width, bmp.Height);
                Graphics g = Graphics.FromImage(b);
                ImageAttributes attr = new ImageAttributes();

                attr.SetGamma(val, ColorAdjustType.Bitmap);
                g.DrawImage(bmp, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, attr);
                g.Dispose();
                return b;
            }
            catch
            {
                return null;
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //生成縮略圖, shrink模式
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = @"C:\______test_files\picture1small.jpg";

            ShowThumbnail(filename1, filename2, 100, 200);
        }

        public void ShowThumbnail(string oldfile, string newfile, int white, int height)
        {
            System.Drawing.Image image = System.Drawing.Image.FromFile(oldfile);
            //获取原图高度和宽度
            int oldh = image.Height;
            int oldw = image.Width;
            int neww, newh;
            neww = white; newh = height;   //直接设定新图的高宽,,

            try
            {
                System.Drawing.Image bt = new System.Drawing.Bitmap(neww, newh);
                System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bt);
                gr.Clear(Color.White);
                gr.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                gr.DrawImage(image, new Rectangle(0, 0, neww, newh), 0, 0, oldw, oldh, GraphicsUnit.Pixel);
                switch (oldfile.Substring(oldfile.Length - 3).ToUpper())
                {
                    case "JPG":
                        bt.Save(newfile, ImageFormat.Jpeg);
                        break;
                    case "GIF":
                        bt.Save(newfile, ImageFormat.Gif);
                        break;
                    case "PNG":
                        bt.Save(newfile, ImageFormat.Png);
                        break;
                    default:
                        bt.Save(newfile, ImageFormat.Jpeg);
                        break;
                }
                gr.Dispose();
                bt.Dispose();
                image.Dispose();
            }
            catch { }
        }


        private void button7_Click(object sender, EventArgs e)
        {
            //生成縮略圖
            string filename1 = @"C:\______test_files\elephant.jpg";
            string filename2 = Application.StartupPath + "\\small_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

            Image image = System.Drawing.Image.FromFile(filename1);
            int W1 = image.Width;
            int H1 = image.Height;
            float ratio = (float)W1 / H1;

            //微缩图高度和宽度  
            int DefaultHeight = 300;    //縮略圖之高度
            int W2 = H1 <= DefaultHeight ? W1 : Convert.ToInt32(DefaultHeight * ratio);
            int H2 = H1 <= DefaultHeight ? H1 : DefaultHeight;

            CreateThumbnailPicture(filename1, filename2, W2, H2);

            richTextBox1.Text += "縮略圖之高度 = " + DefaultHeight.ToString() + "\n";
            richTextBox1.Text += "已存檔 : " + filename2 + "\n";
        }

        /// <summary>
        /// 圖片微縮圖處理
        /// </summary>
        /// <param name="srcPath">源圖片</param>
        /// <param name="destPath">目標圖片</param>
        /// <param name="width">寬度</param>
        /// <param name="height">高度</param>
        public static void CreateThumbnailPicture(string srcPath, string destPath, int width, int height)
        {
            //根據圖片的磁盤絕對路徑獲取 源圖片 的Image對象
            System.Drawing.Image img = System.Drawing.Image.FromFile(srcPath);

            //bmp： 最終要建立的 微縮圖 位圖對象。
            Bitmap bmp = new Bitmap(width, height);

            //g: 繪制 bmp Graphics 對象
            Graphics g = Graphics.FromImage(bmp);
            g.Clear(Color.Transparent);
            //為Graphics g 對象 初始化必要參數，很容易理解。
            g.PixelOffsetMode = System.Drawing.Drawing2D.PixelOffsetMode.HighQuality;
            g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            g.CompositingQuality = System.Drawing.Drawing2D.CompositingQuality.HighQuality;

            //源圖片寬和高
            int imgWidth = img.Width;
            int imgHeight = img.Height;

            //繪制微縮圖
            g.DrawImage(img, new System.Drawing.Rectangle(0, 0, width, height), new System.Drawing.Rectangle(0, 0, imgWidth, imgHeight)
                        , GraphicsUnit.Pixel);

            ImageFormat format = img.RawFormat;
            ImageCodecInfo info = ImageCodecInfo.GetImageEncoders().SingleOrDefault(i => i.FormatID == format.Guid);
            EncoderParameter param = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, 100L);
            EncoderParameters parameters = new EncoderParameters(1);
            parameters.Param[0] = param;
            img.Dispose();

            //保存已生成微缩图，这里将GIF格式转化成png格式。  
            if (format == ImageFormat.Gif)
            {
                destPath = destPath.ToLower().Replace(".gif", ".png");
                bmp.Save(destPath, ImageFormat.Png);
            }
            else
            {
                if (info != null)
                {
                    bmp.Save(destPath, info, parameters);
                }
                else
                {

                    bmp.Save(destPath, format);
                }
            }

            img.Dispose();
            g.Dispose();
            bmp.Dispose();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";

            string filename = @"C:\______test_files\elephant.jpg";

            System.Drawing.Image.GetThumbnailImageAbort callb = null;

            try
            {
                // 保存到指定的文件夾
                Image MyImage = Image.FromFile(filename);
                // 保存大圖(原圖)
                Image NewImage = MyImage.GetThumbnailImage(800, 1000, callb, new System.IntPtr());
                NewImage.Save("big.jpg");
                // 保存中圖
                NewImage = MyImage.GetThumbnailImage(400, 500, callb, new System.IntPtr());
                NewImage.Save("middle.jpg");

                // 單款衣服的圖片大小
                NewImage = MyImage.GetThumbnailImage(255, 319, callb, new System.IntPtr());
                NewImage.Save("SingleImage.jpg");

                // 保存小圖
                NewImage = MyImage.GetThumbnailImage(115, 144, callb, new System.IntPtr());
                NewImage.Save("small.jpg");
                // 保存極小圖
                NewImage = MyImage.GetThumbnailImage(45, 56, callb, new System.IntPtr());
                NewImage.Save("dinky.jpg");

                MyImage.Dispose();
                NewImage.Dispose();
                // 一定要釋放，否則進程被占用
            }
            catch (Exception ex)
            {
                //Response.Write(ex.ToString());
            }
            richTextBox1.Text += "完成\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //檢視圖片的像素
            string filename = @"C:\______test_files\picture1.jpg";

            Image image = Image.FromFile(filename);
            richTextBox1.Text += "檔案 : " + filename + ",\t" + "圖片像素：[" + image.Width + "*" + image.Height + "]" + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //圖片測試
            string filename = @"C:\______test_files\elephant.jpg";
            Image sample = new Bitmap(filename);
            MemoryStream buf = new MemoryStream();
            sample.Save(buf, ImageFormat.Bmp);
            byte[] currentImage = buf.GetBuffer();

            int[] stats = new int[3];
            for (int i = 0; i < currentImage.Length; )
            {
                for (int j = 0; j < 3; j++)
                {
                    stats[j] += currentImage[i];
                    ++i;
                }
            }
            richTextBox1.Text += "Blue: " + stats[0] + "\n";
            richTextBox1.Text += "Green: " + stats[1] + "\n";
            richTextBox1.Text += "Red: " + stats[2] + "\n";
            if ((stats[0] > stats[1]) && (stats[0] > stats[2]))
            {
                richTextBox1.Text += "This is a cold picture." + "\n";
            }
            if ((stats[1] > stats[0]) && (stats[1] > stats[2]))
            {
                richTextBox1.Text += "This is a summer picture." + "\n";
            }
            if ((stats[2] > stats[0]) && (stats[2] > stats[1]))
            {
                richTextBox1.Text += "This is a fiery picture." + "\n";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //為圖片生成縮略圖
            //為圖片生成縮略圖
            //讀取圖檔, 多一層Image結構
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);

            Image image2 = GetThumbnail(image, image.Width / 2, image.Height / 2);

            pictureBox1.Image = image2;
        }

        /// 為圖片生成縮略圖
        /// 原圖片的路徑
        /// 縮略圖寬
        /// 縮略圖高
        /// 
        public Image GetThumbnail(Image image, int width, int height)
        {
            Bitmap bmp = new Bitmap(width, height);
            //從Bitmap創建一個Graphics
            Graphics gr = Graphics.FromImage(bmp);
            //設置 
            gr.SmoothingMode = SmoothingMode.HighQuality;
            //下面這個也設成高質量
            gr.CompositingQuality = CompositingQuality.HighQuality;
            //下面這個設成High
            gr.InterpolationMode = InterpolationMode.HighQualityBicubic;
            //把原始圖像繪制成上面所設置寬高的縮小圖
            Rectangle rectDestination = new Rectangle(0, 0, width, height);

            gr.DrawImage(image, rectDestination, 0, 0, image.Width, image.Height, GraphicsUnit.Pixel);
            return bmp;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            /*
            用到的算法是robert算子，這是一種比較簡單的算法：
            f(x,y)=sqrt((g(x,y)-g(x+1,y+1))^2+(g(x+1,y)-g(x,y+1))^2)
            */

            //圖像邊緣提取
            Image_Test();
        }

        private void Image_Test()
        {
            if (pictureBox1.Image != null)
            {
                int W = pictureBox1.Image.Width;
                int H = pictureBox1.Image.Height;
                Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
                Bitmap bitmap2 = new Bitmap(W, H, PixelFormat.Format24bppRgb);
                BitmapData bitmapdata1 = bitmap1.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);  //原圖
                BitmapData bitmapdata2 = bitmap2.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);  //新圖即邊緣圖

                unsafe
                {
                    //首先第一段代碼是提取邊緣，邊緣置為黑色，其他部分置為白色
                    byte* pin_1 = (byte*)(bitmapdata1.Scan0.ToPointer());
                    byte* pin_2 = pin_1 + (bitmapdata1.Stride);
                    byte* pout = (byte*)(bitmapdata2.Scan0.ToPointer());
                    for (int y = 0; y < bitmapdata1.Height - 1; y++)
                    {
                        for (int x = 0; x < bitmapdata1.Width; x++)
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
                        pin_1 += bitmapdata1.Stride - bitmapdata1.Width * 3;
                        pin_2 += bitmapdata1.Stride - bitmapdata1.Width * 3;
                        pout += bitmapdata2.Stride - bitmapdata2.Width * 3;
                    }

                    /*
                    //這裡博主加粗了一下線條- -，不喜歡的同學可以刪了這段代碼
                    byte* pin_5 = (byte*)(bitmapdata2.Scan0.ToPointer());
                    for (int y = 0; y < bitmapdata1.Height - 1; y++)
                    {
                        for (int x = 3; x < bitmapdata1.Width; x++)
                        {
                            if (pin_5[0] == 0 && pin_5[1] == 0 && pin_5[2] == 0)
                            {
                                pin_5[-3] = 0;
                                pin_5[-2] = 0;
                                pin_5[-1] = 0;      //邊緣點的前一個像素點置為黑色（注意一定要是遍歷過的像素點）                                                    
                            }
                            pin_5 += 3;

                        }
                        pin_5 += bitmapdata2.Stride - bitmapdata2.Width * 3;
                    }
                    */

                    /*
                    //這段代碼是把原圖和邊緣圖重合
                    byte* pin_3 = (byte*)(bitmapdata1.Scan0.ToPointer());
                    byte* pin_4 = (byte*)(bitmapdata2.Scan0.ToPointer());
                    for (int y = 0; y < bitmapdata1.Height - 1; y++)
                    {
                        for (int x = 0; x < bitmapdata1.Width; x++)
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
                        pin_3 += bitmapdata1.Stride - bitmapdata1.Width * 3;
                        pin_4 += bitmapdata2.Stride - bitmapdata2.Width * 3;
                    }
                    */

                    bitmap1.UnlockBits(bitmapdata1);
                    bitmap2.UnlockBits(bitmapdata2);

                    pictureBox1.Image = bitmap2;
                }
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //圖片剪下一塊存檔 另法
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = @"C:\______test_files\picture1_cut.jpg";

            pictureBox1.Image = CutForCustomx(filename1, 150, 150);
            pictureBox1.Image.Save(filename2);
        }

        public static Image CutForCustomx(string imgPath, int top, int height)
        {
            FileStream fs = new FileStream(imgPath, FileMode.Open, FileAccess.Read);
            //從文件獲取原始圖片，並使用流中嵌入的顏色管理信息
            System.Drawing.Image initImage = System.Drawing.Image.FromStream(fs, true);

            Bitmap b = new Bitmap(initImage);

            Bitmap img = b.Clone(new Rectangle(0, top, initImage.Width, height), System.Drawing.Imaging.PixelFormat.DontCare);
            return (Image)(img);
        }

        public static Image CutForCustomx(string imgPath, Rectangle rec)
        {
            FileStream fs = new FileStream(imgPath, FileMode.Open, FileAccess.Read);
            //從文件獲取原始圖片，並使用流中嵌入的顏色管理信息
            System.Drawing.Image initImage = System.Drawing.Image.FromStream(fs, true);

            Bitmap b = new Bitmap(initImage);

            Bitmap img = b.Clone(rec, System.Drawing.Imaging.PixelFormat.DontCare);
            return (Image)(img);
        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            MyTempImage myTempImage = new MyTempImage();

            //myTempImage.CreateImage();
            pictureBox2.Image = Image.FromFile(myTempImage.CreateImage());



            //string thefullname = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + ".gif"; // "nowtime.gif";
            //richTextBox1.Text += thefullname + "\n";

        }
    }

    public class MyTempImage
    {
        public string CreateImage()
        {
            string str = DateTime.Now.ToString();
            Bitmap image = new Bitmap(200, 30);
            Graphics g = Graphics.FromImage(image);
            string thefullname = DateTime.Now.ToString("yyyy-MM-dd HH-mm-ss") + ".gif"; // "nowtime.gif";

            g.Clear(Color.White);
            g.DrawString(str, new Font("CourIEr New", 10), new SolidBrush(Color.Red), 20, 5);
            //Graphics 類還有很多繪圖方法可以繪制 直線、曲線、圓等等 
            image.Save(thefullname, System.Drawing.Imaging.ImageFormat.Gif);
            return thefullname;
        }
    }

}
