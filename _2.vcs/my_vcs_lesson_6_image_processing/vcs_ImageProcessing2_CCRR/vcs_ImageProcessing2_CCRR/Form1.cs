using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for PixelFormat
using System.Drawing.Drawing2D;

namespace vcs_ImageProcessing2_CCRR
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\pic_256X100.bmp";
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_map_city/global.c.gif";   //超大圖, 要很久
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint, true);
            this.UpdateStyles();
            //以上兩句是為了設置控件樣式為雙緩沖，這可以有效減少圖片閃爍的問題，關於這個大家可以自己去搜索下

            //this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            show_item_location();

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
            dx = 200 + 10;
            dy = 60 + 10;

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

            //button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);

            groupBox1.Size = new Size(200, 300);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_lanczos0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 10);
            bt_lanczos1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + 10);
            bt_lanczos2.Location = new Point(x_st + dx * 0, y_st + dy * 2 + 10);
            bt_lanczos3.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 10);

            pictureBox1.Size = new Size(800, 800);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_restore.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_restore.Size.Width, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_restore.Size.Height);

            richTextBox1.Size = new Size(300, 800);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1600, 870);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_restore_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(800, 800);
            Restore_Picture();
        }

        void Restore_Picture()
        {
            pictureBox1.Image = Image.FromFile(filename);
            Application.DoEvents();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //獲得圖片的分辨率和大小
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            double DPI = pictureBox1.Image.HorizontalResolution;//獲得分辨率 gisoracle
            double w = 1.0 * pictureBox1.Image.Width / DPI * 25.4;
            double h = 1.0 * pictureBox1.Image.Height / DPI * 25.4;

            richTextBox1.Text += "獲得圖片的分辨率和大小 : " + w.ToString("f2") + ":" + h.ToString("f2") + "\n";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //改變圖像大小

            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            // 改變圖像大小使用低質量的模式
            g.InterpolationMode = InterpolationMode.NearestNeighbor;

            g.DrawImage(bitmap1, new Rectangle(10, 10, 120, 120), // source rectangle
            new Rectangle(0, 0, W, H), // destination rectangle
            GraphicsUnit.Pixel);

            // 使用高質量模式
            //g.CompositingQuality = CompositingQuality.HighSpeed;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;

            g.DrawImage(bitmap1, new Rectangle(130, 10, 120, 120), new Rectangle(0, 0, W, H), GraphicsUnit.Pixel);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //重設大小
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = ResizeImage(bitmap1, new Size(bitmap1.Width / 2, bitmap1.Height / 2));
            pictureBox1.Image = bitmap2;
        }

        //重設大小
        public Bitmap ResizeImage(Bitmap bmp, Size size)
        {
            Bitmap newbmp = new Bitmap(size.Width, size.Height);
            using (Graphics g = Graphics.FromImage(newbmp))
            {
                g.DrawImage(bmp, new Rectangle(Point.Empty, size));
            }
            return newbmp;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //圖像切割 每100X100 切成一個小圖
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            ImageCut(filename, 100, 100);
        }

        void ImageCut(string filename1, int width, int height)
        {
            Bitmap bitmap1 = new Bitmap(filename1);
            int MaxRow = (int)Math.Ceiling((Decimal)bitmap1.Height / height);
            int MaxColumn = (int)Math.Ceiling((Decimal)bitmap1.Width / width);
            for (int i = 0; i < MaxRow; i++)
            {
                for (int j = 0; j < MaxColumn; j++)
                {
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
                    g.DrawString(i.ToString("D2") + " " + j.ToString("D2"), new Font("黑體", 14), new SolidBrush(Color.FromArgb(255, Color.Red)), 5, 5); //加水印

                    string filename2 = "tmp_bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_" + i.ToString("D2") + "_" + j.ToString("D2") + ".bmp";
                    try
                    {
                        bitmap2.Save(filename2, ImageFormat.Bmp);
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                    }
                }
            }
        }

        // 圖片裁剪
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
            Image.GetThumbnailImageAbort callback = new Image.GetThumbnailImageAbort(ThumbnailCallback);
            Image image = new Bitmap(@"c:\dddddddddd\FakePhoto.jpg");
            Image pThumbnail = image.GetThumbnailImage(100, 100, callback, new IntPtr());
            e.Graphics.DrawImage(pThumbnail, 10, 10, pThumbnail.Width, pThumbnail.Height);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //圖片剪下一塊存檔1
            //圖片剪下一塊存檔, 圖片裁剪
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"tmp_picture1_cut4.jpg";

            ImgReduceCutOut(200, 200, filename1, filename2);

            //看起來像是 305X400 轉成200X200
            richTextBox1.Text += "原檔案 : " + filename1 + "\n";
            richTextBox1.Text += "圖片剪下一塊存檔 : " + filename2 + "\n";
        }

        public static Image CutForCustomx(string imgPath, int top, int height)
        {
            FileStream fs = new FileStream(imgPath, FileMode.Open, FileAccess.Read);
            //從文件獲取原始圖片，並使用流中嵌入的顏色管理信息
            Image initImage = Image.FromStream(fs, true);

            Bitmap b = new Bitmap(initImage);

            Bitmap img = b.Clone(new Rectangle(0, top, initImage.Width, height), PixelFormat.DontCare);
            return (Image)(img);
        }

        public static Image CutForCustomx(string imgPath, Rectangle rec)
        {
            FileStream fs = new FileStream(imgPath, FileMode.Open, FileAccess.Read);
            //從文件獲取原始圖片，並使用流中嵌入的顏色管理信息
            Image initImage = Image.FromStream(fs, true);

            Bitmap b = new Bitmap(initImage);

            Bitmap img = b.Clone(rec, PixelFormat.DontCare);
            return (Image)(img);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //圖片剪下一塊存檔2

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"tmp_picture1_cut5.jpg";

            pictureBox1.Image = CutForCustomx(filename1, 150, 150);
            pictureBox1.Image.Save(filename2);
        }

        //圖片質量壓縮(不改變尺寸) ST
        /// <summary>
        /// 獲取圖片編碼信息
        /// </summary>
        private static ImageCodecInfo GetEncoderInfo(String mimeType)
        {
            int j;
            ImageCodecInfo[] encoders;
            encoders = ImageCodecInfo.GetImageEncoders();
            for (j = 0; j < encoders.Length; ++j)
            {
                if (encoders[j].MimeType == mimeType)
                    return encoders[j];
            }
            return null;
        }

        /// <summary>
        /// 圖片壓縮(降低質量以減小文件的大小)
        /// </summary>
        /// <param name="srcBitmap">傳入的Bitmap對象</param>
        /// <param name="destStream">壓縮後的Stream對象</param>
        /// <param name="level">壓縮等級，0到100，0 最差質量，100 最佳</param>
        public static void Compress(Bitmap srcBitmap, Stream destStream, long level)
        {
            ImageCodecInfo myImageCodecInfo;
            System.Drawing.Imaging.Encoder myEncoder;
            EncoderParameter myEncoderParameter;
            EncoderParameters myEncoderParameters;

            // Get an ImageCodecInfo object that represents the JPEG codec.
            myImageCodecInfo = GetEncoderInfo("image/jpeg");

            // Create an Encoder object based on the GUID

            // for the Quality parameter category.
            myEncoder = System.Drawing.Imaging.Encoder.Quality;

            // Create an EncoderParameters object.
            // An EncoderParameters object has an array of EncoderParameter
            // objects. In this case, there is only one

            // EncoderParameter object in the array.
            myEncoderParameters = new EncoderParameters(1);

            // Save the bitmap as a JPEG file with 給定的 quality level
            myEncoderParameter = new EncoderParameter(myEncoder, level);
            myEncoderParameters.Param[0] = myEncoderParameter;
            srcBitmap.Save(destStream, myImageCodecInfo, myEncoderParameters);
        }

        /// <summary>
        /// 圖片壓縮(降低質量以減小文件的大小)
        /// </summary>
        /// <param name="srcBitMap">傳入的Bitmap對象</param>
        /// <param name="destFile">壓縮後的圖片保存路徑</param>
        /// <param name="level">壓縮等級，0到100，0 最差質量，100 最佳</param>
        public static void Compress(Bitmap bitmap1, string destFile, long level)
        {
            Stream s = new FileStream(destFile, FileMode.Create);
            Compress(bitmap1, s, level);
            s.Close();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //圖片質量壓縮(不改變尺寸)

            //圖片質量壓縮(不改變尺寸)

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            richTextBox1.Text += "原圖 : " + filename + "\n";

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            Compress(bitmap1, "compressfile010.jpg", 10);
            Compress(bitmap1, "compressfile040.jpg", 40);
            Compress(bitmap1, "compressfile070.jpg", 70);
            Compress(bitmap1, "compressfile100.jpg", 100);

        }
        //圖片質量壓縮(不改變尺寸) SP

        //圖片壓縮、縮略圖生成代碼

        //#region imageCompress
        /**/
        /// <summary>
        /// 圖片壓縮函數
        /// </summary>
        /// <param name="sourceFile">原始圖片文件</param>
        /// <param name="quality">質量壓縮比</param>
        /// <param name="ouputFile">輸出文件名,請用 .jpg 后綴 </param>
        /// <returns>成功返回true，失敗則返回false</returns>
        public static bool imageCompress(String sourceFile, long quality, String outputFile)
        {
            try
            {
                long imageQuality = quality;
                Bitmap sourceImage = new Bitmap(sourceFile);
                ImageCodecInfo myImageCodecInfo = GetEncoderInfo("image/jpeg");
                System.Drawing.Imaging.Encoder myEncoder = System.Drawing.Imaging.Encoder.Quality;
                EncoderParameters myEncoderParameters = new EncoderParameters(1);
                EncoderParameter myEncoderParameter = new EncoderParameter(myEncoder, imageQuality);
                myEncoderParameters.Param[0] = myEncoderParameter;

                sourceImage.Save(outputFile, myImageCodecInfo, myEncoderParameters);
                return true;

            }
            catch
            {
                return false;
            }

        }
        //#endregion

        /*  
        圖片壓縮、縮略圖生成代碼匯總
        public static bool imageCompress(String sourceFile,long quality,String outputFile)
        public static bool getThumImage(String sourceFile, long quality, int multiple, String outputFile)
        */

        private void button7_Click(object sender, EventArgs e)
        {
            //圖片壓縮
            //圖片壓縮
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = "tmp_compress_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            bool result = imageCompress(filename1, 30, filename2);
            if (result == true)
                richTextBox1.Text += "OK\n";
            else
                richTextBox1.Text += "FAIL\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //改變圖片品質
            //改變圖片品質
            VaryQualityLevel();
        }

        private ImageCodecInfo GetEncoder(ImageFormat format)
        {
            ImageCodecInfo[] codecs = ImageCodecInfo.GetImageEncoders();

            foreach (ImageCodecInfo codec in codecs)
            {
                if (codec.FormatID == format.Guid)
                {
                    return codec;
                }
            }

            return null;
        }


        private void VaryQualityLevel()
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            // Get a bitmap.
            Bitmap bitmap1 = new Bitmap(filename);
            bitmap1.Save(@"picture_old.jpg", ImageFormat.Jpeg);

            ImageCodecInfo jpgEncoder = GetEncoder(ImageFormat.Jpeg);

            // Create an Encoder object based on the GUID
            // for the Quality parameter category.
            System.Drawing.Imaging.Encoder myEncoder = System.Drawing.Imaging.Encoder.Quality;

            // Create an EncoderParameters object.
            // An EncoderParameters object has an array of EncoderParameter
            // objects. In this case, there is only one
            // EncoderParameter object in the array.
            EncoderParameters myEncoderParameters = new EncoderParameters(1);

            EncoderParameter myEncoderParameter = new EncoderParameter(myEncoder, 50L);
            myEncoderParameters.Param[0] = myEncoderParameter;
            bitmap1.Save(@"TestPhotoQuality050.jpg", jpgEncoder, myEncoderParameters);

            myEncoderParameter = new EncoderParameter(myEncoder, 100L);
            myEncoderParameters.Param[0] = myEncoderParameter;
            bitmap1.Save(@"TestPhotoQuality100.jpg", jpgEncoder, myEncoderParameters);

            // Save the bitmap as a JPG file with zero quality level compression.
            myEncoderParameter = new EncoderParameter(myEncoder, 0L);
            myEncoderParameters.Param[0] = myEncoderParameter;
            bitmap1.Save(@"TestPhotoQuality000.jpg", jpgEncoder, myEncoderParameters);

            richTextBox1.Text += "完成\n";
        }


        private void button9_Click(object sender, EventArgs e)
        {
            //jpg縮略圖函數
            //在下
        }

        //jpg縮略圖函數 使用

        /// <summary>
        /// 生成jpg縮略圖字節,本人的小軟件中需要用到的功能，所以自己做了一個函數，和大家分享
        /// 為什麼要生成字節而不是文件，這是為了方便後續處理啦^_^
        /// </summary>
        /// <param name="originalImagePath">原始路徑</param>
        /// <param name="quality">質量0-100</param>
        /// <param name="width">寬度</param>
        /// <param name="height">高度</param>
        /// <param name="mode">模式：HW,W,H,Cut</param>
        /// <returns></returns>
        public static byte[] MakeJPGThumbnailBytes(string originalImagePath, long quality, int width, int height, string mode)
        {
            Image originalImage = Image.FromFile(originalImagePath);
            MemoryStream s = new MemoryStream();
            int towidth = width;
            int toheight = height;

            int x = 0;
            int y = 0;
            int ow = originalImage.Width;
            int oh = originalImage.Height;

            switch (mode)
            {
                case "HW"://指定高寬縮放（可能變形）
                    break;
                case "W"://指定寬，高按比例
                    toheight = originalImage.Height * width / originalImage.Width;
                    break;
                case "H"://指定高，寬按比例
                    towidth = originalImage.Width * height / originalImage.Height;
                    break;
                case "Cut"://指定高寬裁減（不變形）
                    if ((double)originalImage.Width / (double)originalImage.Height > (double)towidth / (double)toheight)
                    {
                        oh = originalImage.Height;
                        ow = originalImage.Height * towidth / toheight;
                        y = 0;
                        x = (originalImage.Width - ow) / 2;
                    }
                    else
                    {
                        ow = originalImage.Width;
                        oh = originalImage.Width * height / towidth;
                        x = 0;
                        y = (originalImage.Height - oh) / 2;
                    }
                    break;
                default:
                    break;
            }

            //新建一個bmp圖片
            Image bitmap = new Bitmap(towidth, toheight);

            //新建一個畫板
            Graphics g = Graphics.FromImage(bitmap);

            //設置高質量插值法
            g.InterpolationMode = InterpolationMode.High;

            //設置高質量,低速度呈現平滑程度
            g.SmoothingMode = SmoothingMode.HighQuality;

            //清空畫布並以透明背景色填充
            g.Clear(Color.Transparent);

            //在指定位置並且按指定大小繪制原圖片的指定部分
            g.DrawImage(originalImage, new Rectangle(0, 0, towidth, toheight),
            new Rectangle(x, y, ow, oh),
            GraphicsUnit.Pixel);

            try
            {
                //以jpg格式保存縮略圖
                EncoderParameters eps = new EncoderParameters(1);
                EncoderParameter ep = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, quality);
                eps.Param[0] = ep;
                bitmap.Save(s, GetCodecInfo("image/jpeg"), eps);
                return s.GetBuffer();
            }
            catch (System.Exception e)
            {
                throw e;
            }
            finally
            {
                originalImage.Dispose();
                bitmap.Dispose();
                s.Dispose();
                g.Dispose();
            }
        }

        /**/
        /// <summary>
        /// 保存JPG時用
        /// </summary>
        /// <param name="mimeType"></param>
        /// <returns>得到指定mimeType的ImageCodecInfo</returns>
        private static ImageCodecInfo GetCodecInfo(string mimeType)
        {
            ImageCodecInfo[] CodecInfo = ImageCodecInfo.GetImageEncoders();
            foreach (ImageCodecInfo ici in CodecInfo)
            {
                if (ici.MimeType == mimeType) return ici;
            }
            return null;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //設定圖片解析度
            //設定圖片解析度
            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            Bitmap bmp = new Bitmap(filename);
            g.FillRectangle(Brushes.White, this.ClientRectangle);

            richTextBox1.Text += "H res : " + bmp.HorizontalResolution.ToString() + "\n";
            richTextBox1.Text += "V res : " + bmp.VerticalResolution.ToString() + "\n";


            g.DrawImage(bmp, 0, 0);

            bmp.SetResolution(75f, 75f);

            g.DrawImage(bmp, 350, 0);

            richTextBox1.Text += "H res : " + bmp.HorizontalResolution.ToString() + "\n";
            richTextBox1.Text += "V res : " + bmp.VerticalResolution.ToString() + "\n";

            /*
            bmp.SetResolution(300f, 300f);
            g.DrawImage(bmp, 0, 0);
            bmp.SetResolution(1200f, 1200f);
            g.DrawImage(bmp, 350, 0);
            */

            pictureBox1.Image = bitmap1;

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //在PictureBox上測試旋轉圖片
            //測試RotateTransform, TranslateTransform和ResetTransform

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            int W = this.pictureBox1.Width;
            int H = this.pictureBox1.Height;

            Bitmap bitmap1 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap1);

            Pen p = new Pen(Color.Gray, 1);

            int i;
            for (i = 0; i <= W; i += 100)
            {
                g.DrawLine(p, i, 0, i, H);
            }
            for (i = 0; i <= H; i += 100)
            {
                g.DrawLine(p, 0, i, W, i);
            }


            Rectangle srcRect = new Rectangle(0, 0, W, H);   //擷取部分區域
            GraphicsUnit units = GraphicsUnit.Pixel;
            Image img = Image.FromFile(filename);


            int x_st = 0;
            int y_st = 0;
            int angle = 0;

            Point ulCorner = new Point(0, 0);
            Point urCorner = new Point(W, 0);
            Point llCorner = new Point(0, H);
            Point[] destRect = { ulCorner, urCorner, llCorner };

            x_st = 350 * 0;
            y_st = 200;
            angle = -10;
            ulCorner = new Point(0, 0);
            urCorner = new Point(W, 0);
            llCorner = new Point(0, H);
            destRect = new Point[] { ulCorner, urCorner, llCorner };

            g.TranslateTransform(x_st, y_st);
            g.RotateTransform(angle);//旋轉指定的角度
            g.DrawImage(img, destRect, srcRect, units);
            g.ResetTransform();//恢復坐標軸坐標 回 0 度


            x_st = 350 * 1;
            y_st = 200;
            angle = 0;
            ulCorner = new Point(0, 0);
            urCorner = new Point(W, 0);
            llCorner = new Point(0, H);
            destRect = new Point[] { ulCorner, urCorner, llCorner };

            g.TranslateTransform(x_st, y_st);
            g.RotateTransform(angle);//旋轉指定的角度
            g.DrawImage(img, destRect, srcRect, units);
            g.ResetTransform();//恢復坐標軸坐標 回 0 度


            x_st = 350 * 2;
            y_st = 200;
            angle = 10;
            ulCorner = new Point(0, 0);
            urCorner = new Point(W, 0);
            llCorner = new Point(0, H);
            destRect = new Point[] { ulCorner, urCorner, llCorner };

            g.TranslateTransform(x_st, y_st);
            g.RotateTransform(angle);//旋轉指定的角度
            g.DrawImage(img, destRect, srcRect, units);
            g.ResetTransform();//恢復坐標軸坐標 回 0 度





            pictureBox1.Image = bitmap1;

        }

        //連續旋轉一張圖片 ST
        float angle = 0;
        private void button12_Click(object sender, EventArgs e)
        {
            //連續旋轉一張圖片
            angle += 15;
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);

            Image image_rotated = image.GetRotateImage(angle);

            pictureBox1.Image = image_rotated;
            pictureBox1.Size = new Size(image_rotated.Width, image_rotated.Height);
        }
        //連續旋轉一張圖片 SP

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void bt_lanczos0_Click(object sender, EventArgs e)
        {
            //原圖
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";
            Bitmap bitmap1;
            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;
        }

        private Bitmap ZoomLanczos2Apply(Bitmap srcBitmap, double k)
        {
            Bitmap src = new Bitmap(srcBitmap);
            int width = src.Width;
            int height = src.Height;
            BitmapData srcData = src.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format32bppArgb);
            int w = (int)((double)width * k);
            int h = (int)((double)height * k);
            Bitmap dst = new Bitmap(w, h, PixelFormat.Format32bppArgb);
            unsafe
            {
                byte* pS = (byte*)srcData.Scan0;
                BitmapData dstData = dst.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadWrite, PixelFormat.Format32bppArgb);
                byte* d = (byte*)dstData.Scan0;
                int offset = dstData.Stride - w * 4;
                int x = 0, y = 0;
                double p = 0, q = 0;
                double n1 = 0, n2 = 0, n3 = 0, n4 = 0, nSum = 0;
                int p0 = 0, p1 = 0, p2 = 0, p3 = 0, p4 = 0, gray = 0;
                byte* temp = null;
                double[] NP1 = new double[] { -0.00623896218505032, -0.0122238956025722, -0.0179556611741633, -0.0234353793884155, -0.028664425422539, -0.0336444239814841, -0.0383772438642046, -0.0428649922670393, -0.0471100088344975, -0.0511148594680326, -0.0548823299036605, -0.0584154190695433, -0.0617173322348938, -0.0647914739617815, -0.0676414408716196, -0.0702710142382982, -0.0726841524200902, -0.0748849831426012, -0.0768777956451566, -0.0786670327031274, -0.0802572825387739, -0.0816532706332581, -0.0828598514525135, -0.0838820000996894, -0.0847248039068906, -0.0853934539789171, -0.0858932367016755, -0.0862295252278804, -0.0864077709525887, -0.0864334949910196, -0.086312279671003, -0.0860497600522689, -0.0856516154846428, -0.0851235612170509, -0.0844713400690516, -0.0837007141764163, -0.0828174568220629, -0.0818273443634177, -0.0807361482670294, -0.0795496272610035, -0.0782735196155422, -0.0769135355615895, -0.0754753498572731, -0.0739645945115212, -0.0723868516738999, -0.0707476466993797, -0.0690524413963838, -0.0673066274661114, -0.0655155201407567, -0.0636843520278618, -0.0618182671676555, -0.0599223153098279, -0.0580014464157926, -0.0560605053920726, -0.0541042270600343, -0.0521372313667693, -0.0501640188415028, -0.048188966301476, -0.0462163228108206, -0.0442502058955092, -0.0422945980170336, -0.0403533433070252, -0.0384301445645995, -0.0365285605177724, -0.0346520033498648, -0.0328037364913793, -0.0309868726774121, -0.0292043722702325, -0.0274590418462525, -0.0257535330461864, -0.0240903416868009, -0.0224718071322479, -0.0209001119225812, -0.0193772816566703, -0.0179051851263444, -0.0164855346982315, -0.015119886939392, -0.013809643482501, -0.0125560521259855, -0.0113602081641975, -0.0102230559423803, -0.00914539063088284, -0.00812786021277406, -0.00717096767873418, -0.00627507342282205, -0.00544039783246632, -0.00466702406578012, -0.00395490100907222, -0.00330384640720963, -0.00271355015928674, -0.00218357777186753, -0.00171337396189679, -0.00130226640121749, -0.000949469594490465, -0.00065408888218426, -0.000415124560192089, -0.000231476107535702, -0.000101946513534946, -0 };
                double[] NP2 = new double[] { 0.999794398630316, 0.999177779156011, 0.998150695261436, 0.996714069021198, 0.994869189802256, 0.992617712728975, 0.989961656713271, 0.986903402052547, 0.983445687598761, 0.979591607502511, 0.975344607536654, 0.9707084810045, 0.965687364238256, 0.960285731693901, 0.954508390649264, 0.948360475512591, 0.941847441749449, 0.934975059436304, 0.927749406449645, 0.920176861299994, 0.912264095620641, 0.904018066321406, 0.895446007418168, 0.886555421549337, 0.877354071190877, 0.867849969581877, 0.858051371373022, 0.847966763010743, 0.83760485287009, 0.826974561149762, 0.816085009542993, 0.804945510698284, 0.793565557484247, 0.781954812073053, 0.770123094857198, 0.758080373214511, 0.745836750136481, 0.733402452735159, 0.720787820644003, 0.708003294328147, 0.695059403319663, 0.68196675439345, 0.668736019699406, 0.655377924866579, 0.641903237094975, 0.628322753250659, 0.614647287979759, 0.600887661856885, 0.587054689583387, 0.573159168250756, 0.559211865684328, 0.545223508882287, 0.531204772564777, 0.517166267847729, 0.503118531055783, 0.489072012688425, 0.47503706655321, 0.461023939079635, 0.447042758826945, 0.433103526198797, 0.419216103377392, 0.405390204489315, 0.391635386014941, 0.37796103745288, 0.364376372250524, 0.350890419011333, 0.33751201298905, 0.324249787878619, 0.311112167913061, 0.298107360275149, 0.285243347832182, 0.272527882201696, 0.259968477155437, 0.247572402368387, 0.235346677519141, 0.223298066747373, 0.211433073473617, 0.199757935586031, 0.188278620998268, 0.177000823582037, 0.165929959477376, 0.155071163783102, 0.144429287629353, 0.13400889563358, 0.123814263740785, 0.113849377448258, 0.104117930414501, 0.0946233234514916, 0.0853686638988765, 0.0763567653781721, 0.0675901479244855, 0.059071038492763, 0.050801371835042, 0.0427827917446759, 0.0350166526629909, 0.0275040216433488, 0.0202456806670952, 0.0132421293054104, 0.00649358772061002 };
                double[] NP3 = new double[] { 0.00649358772061002, 0.0132421293054104, 0.0202456806670952, 0.0275040216433488, 0.0350166526629909, 0.0427827917446759, 0.0508013718350421, 0.059071038492763, 0.0675901479244855, 0.0763567653781721, 0.0853686638988765, 0.0946233234514916, 0.104117930414501, 0.113849377448258, 0.123814263740785, 0.13400889563358, 0.144429287629353, 0.155071163783102, 0.165929959477376, 0.177000823582037, 0.188278620998268, 0.199757935586031, 0.211433073473617, 0.223298066747373, 0.235346677519141, 0.247572402368387, 0.259968477155437, 0.272527882201696, 0.285243347832182, 0.298107360275149, 0.311112167913061, 0.324249787878619, 0.33751201298905, 0.350890419011333, 0.364376372250524, 0.37796103745288, 0.391635386014941, 0.405390204489315, 0.419216103377392, 0.433103526198797, 0.447042758826944, 0.461023939079634, 0.475037066553209, 0.489072012688425, 0.503118531055783, 0.517166267847729, 0.531204772564777, 0.545223508882287, 0.559211865684328, 0.573159168250756, 0.587054689583387, 0.600887661856885, 0.614647287979759, 0.628322753250659, 0.641903237094975, 0.655377924866579, 0.668736019699406, 0.68196675439345, 0.695059403319663, 0.708003294328147, 0.720787820644003, 0.733402452735159, 0.745836750136481, 0.758080373214511, 0.770123094857198, 0.781954812073053, 0.793565557484247, 0.804945510698284, 0.816085009542993, 0.826974561149762, 0.837604852870089, 0.847966763010743, 0.858051371373022, 0.867849969581877, 0.877354071190877, 0.886555421549337, 0.895446007418168, 0.904018066321406, 0.912264095620641, 0.920176861299994, 0.927749406449646, 0.934975059436304, 0.941847441749449, 0.948360475512591, 0.954508390649264, 0.960285731693901, 0.965687364238256, 0.9707084810045, 0.975344607536654, 0.979591607502512, 0.983445687598761, 0.986903402052547, 0.989961656713271, 0.992617712728975, 0.994869189802256, 0.996714069021198, 0.998150695261436, 0.999177779156011, 0.999794398630316 };
                double[] NP4 = new double[] { -0, -0.000101946513534946, -0.000231476107535702, -0.000415124560192089, -0.00065408888218426, -0.000949469594490465, -0.0013022664012175, -0.00171337396189679, -0.00218357777186754, -0.00271355015928674, -0.00330384640720965, -0.00395490100907222, -0.00466702406578012, -0.00544039783246632, -0.00627507342282205, -0.00717096767873415, -0.00812786021277406, -0.00914539063088281, -0.0102230559423803, -0.0113602081641975, -0.0125560521259855, -0.013809643482501, -0.015119886939392, -0.0164855346982315, -0.0179051851263444, -0.0193772816566703, -0.0209001119225812, -0.0224718071322479, -0.0240903416868009, -0.0257535330461864, -0.0274590418462525, -0.0292043722702326, -0.0309868726774121, -0.0328037364913794, -0.0346520033498648, -0.0365285605177724, -0.0384301445645995, -0.0403533433070252, -0.0422945980170336, -0.0442502058955092, -0.0462163228108205, -0.048188966301476, -0.0501640188415028, -0.0521372313667693, -0.0541042270600343, -0.0560605053920726, -0.0580014464157926, -0.0599223153098279, -0.0618182671676555, -0.0636843520278618, -0.0655155201407567, -0.0673066274661114, -0.0690524413963838, -0.0707476466993797, -0.0723868516738999, -0.0739645945115212, -0.0754753498572731, -0.0769135355615895, -0.0782735196155421, -0.0795496272610035, -0.0807361482670294, -0.0818273443634177, -0.0828174568220629, -0.0837007141764163, -0.0844713400690516, -0.0851235612170509, -0.0856516154846428, -0.0860497600522689, -0.086312279671003, -0.0864334949910196, -0.0864077709525887, -0.0862295252278804, -0.0858932367016755, -0.0853934539789171, -0.0847248039068906, -0.0838820000996894, -0.0828598514525135, -0.0816532706332581, -0.0802572825387739, -0.0786670327031274, -0.0768777956451566, -0.0748849831426012, -0.0726841524200902, -0.0702710142382982, -0.0676414408716196, -0.0647914739617815, -0.0617173322348938, -0.0584154190695433, -0.0548823299036604, -0.0511148594680326, -0.0471100088344975, -0.0428649922670393, -0.0383772438642045, -0.0336444239814841, -0.028664425422539, -0.0234353793884155, -0.0179556611741633, -0.0122238956025722, -0.00623896218505032 };
                for (int j = 0; j < h; j++)
                {
                    q = (double)j / (double)k;
                    y = (int)q;
                    q = Math.Abs(q - (double)y);
                    p0 = y * srcData.Stride;
                    y = y >= height ? height - 1 : y;
                    for (int i = 0; i < w; i++)
                    {
                        p = (double)i / (double)k;
                        x = (int)p;
                        p = Math.Abs(p - (double)x);
                        temp = d + i * 4 + j * dstData.Stride;
                        if (p != 0)
                        {
                            x = (x >= width - 3 ? width - 3 : x);
                            x = x < 1 ? 1 : x;
                            gray = (int)(p * 100.0) - 1;
                            gray = Math.Max(0, gray);
                            n1 = NP1[gray];
                            n2 = NP2[gray];
                            n3 = NP3[gray];
                            n4 = 1.0 - n1 - n2 - n3;// NP4[gray];
                            p2 = x * 4 + p0;
                            p1 = p2 - 4;
                            p3 = p2 + 4;
                            p4 = p2 + 8;
                            nSum = n1 + n2 + n3 + n4;
                            gray = (int)((n1 * (double)((pS + p1)[0]) + n2 * (double)((pS + p2)[0]) + n3 * (double)((pS + p3)[0]) + n4 * (double)((pS + p4)[0])));
                            gray = Math.Max(0, Math.Min(255, gray));
                            temp[0] = (byte)gray;
                            gray = (int)((n1 * (double)((pS + p1)[1]) + n2 * (double)((pS + p2)[1]) + n3 * (double)((pS + p3)[1]) + n4 * (double)((pS + p4)[1])));
                            gray = Math.Max(0, Math.Min(255, gray));
                            temp[1] = (byte)gray;
                            gray = (int)((n1 * (double)((pS + p1)[2]) + n2 * (double)((pS + p2)[2]) + n3 * (double)((pS + p3)[2]) + n4 * (double)((pS + p4)[2])));
                            gray = Math.Max(0, Math.Min(255, gray));
                            temp[2] = (byte)gray;
                        }
                        else
                        {
                            x = x >= width ? width - 1 : x;
                            gray = x * 4 + y * srcData.Stride;
                            temp[0] = (byte)(pS + gray)[0];
                            temp[1] = (byte)(pS + gray)[1];
                            temp[2] = (byte)(pS + gray)[2];
                        }
                        temp[3] = (byte)255;
                    }
                }
                for (int i = 0; i < w; i++)
                {
                    p = (double)i / (double)k;
                    x = (int)p;
                    p = Math.Abs(p - (double)x);
                    x = x >= width ? width - 1 : x;
                    for (int j = 0; j < h; j++)
                    {
                        q = (double)j / (double)k;
                        y = (int)q;
                        q = Math.Abs(q - (double)y);
                        p0 = y * srcData.Stride;
                        temp = d + i * 4 + j * dstData.Stride;
                        if (q != 0)
                        {
                            y = y >= height - 3 ? height - 3 : y;
                            y = y < 1 ? 1 : y;
                            gray = (int)(q * 100.0) - 1;
                            gray = Math.Max(0, gray);
                            n1 = NP1[gray];
                            n2 = NP2[gray];
                            n3 = NP3[gray];
                            n4 = 1.0 - n1 - n2 - n3;// NP4[gray];
                            nSum = n1 + n2 + n3 + n4;
                            p2 = x * 4 + y * srcData.Stride;
                            p1 = p2 - srcData.Stride;
                            p3 = p2 + srcData.Stride;
                            p4 = p3 + srcData.Stride;
                            gray = (int)((n1 * (double)((pS + p1)[0]) + n2 * (double)((pS + p2)[0]) + n3 * (double)((pS + p3)[0]) + n4 * (double)((pS + p4)[0])));
                            gray = Math.Max(0, Math.Min(255, gray));
                            temp[0] = (byte)gray;
                            gray = (int)((n1 * (double)((pS + p1)[1]) + n2 * (double)((pS + p2)[1]) + n3 * (double)((pS + p3)[1]) + n4 * (double)((pS + p4)[1])));
                            gray = Math.Max(0, Math.Min(255, gray));
                            temp[1] = (byte)gray;
                            gray = (int)((n1 * (double)((pS + p1)[2]) + n2 * (double)((pS + p2)[2]) + n3 * (double)((pS + p3)[2]) + n4 * (double)((pS + p4)[2])));
                            gray = Math.Max(0, Math.Min(255, gray));
                            temp[2] = (byte)gray;
                        }
                        else
                        {
                            y = y >= height ? height - 1 : y;
                            gray = x * 4 + y * srcData.Stride;
                            temp[0] = (byte)(pS + gray)[0];
                            temp[1] = (byte)(pS + gray)[1];
                            temp[2] = (byte)(pS + gray)[2];
                        }
                        temp[3] = (byte)255;
                    }
                }
                src.UnlockBits(srcData);
                dst.UnlockBits(dstData);
            }
            return dst;
        }

        private void bt_lanczos1_Click(object sender, EventArgs e)
        {
            //Lanczos 2倍
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;

            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            double k = 4.0;
            Bitmap bitmap2 = ZoomLanczos2Apply(bitmap1, k);
            pictureBox1.Image = bitmap2;
            //bitmap2.Save("ims02.lanczos.bmp", ImageFormat.Bmp);
        }

        private Bitmap Zoom2_copy(Bitmap srcBitmap)
        {
            int k = 2;
            Bitmap src = new Bitmap(srcBitmap);
            int w = src.Width;
            int h = src.Height;
            //BitmapData srcData = src.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadWrite, PixelFormat.Format32bppArgb);
            int W = w * k;
            int H = h * k;
            Bitmap dst = new Bitmap(W, H, PixelFormat.Format32bppArgb);
            Color p;

            for (int j = 0; j < h; j++)
            {
                for (int i = 0; i < w; i++)
                {
                    p = src.GetPixel(i, j);
                    dst.SetPixel(i * 2, j * 2, p);
                    dst.SetPixel(i * 2, j * 2 + 1, p);
                    dst.SetPixel(i * 2 + 1, j * 2, p);
                    dst.SetPixel(i * 2 + 1, j * 2 + 1, p);
                }
            }
            return dst;
        }

        private void bt_lanczos2_Click(object sender, EventArgs e)
        {
            //copy 拉大兩倍
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";

            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            Bitmap bitmap2 = Zoom2_copy(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        private void bt_lanczos3_Click(object sender, EventArgs e)
        {
            //StretchImage 拉大兩倍
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;
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


//bitmap2.Save("ims02.duplicate.bmp", ImageFormat.Bmp);

