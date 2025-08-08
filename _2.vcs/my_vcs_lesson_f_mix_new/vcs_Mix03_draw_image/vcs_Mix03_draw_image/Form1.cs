using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageFormat, ImageLockMode, Encoder, ImageCodecInfo
using System.Drawing.Drawing2D;  // for GraphicsPath
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_Mix03_draw_image
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //圖像切割

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            //圖像切割 每100X100 切成一個小圖
            ImageManager.Cut(filename, 100, 100);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //圖片剪下一塊存檔, 圖片裁剪
            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\picture1_cut.jpg";

            ImgReduceCutOut(200, 200, filename1, filename2);

            //看起來像是 305X400 轉成200X200
            richTextBox1.Text += "原檔案 : " + filename1 + "\n";
            richTextBox1.Text += "圖片剪下一塊存檔 : " + filename2 + "\n";
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

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //圖片剪下一塊存檔 另法
            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\picture1_cut.jpg";

            pictureBox1.Image = CutForCustomx(filename1, 150, 150);
            pictureBox1.Image.Save(filename2);
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

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //圖片質量壓縮(不改變尺寸)

            string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            richTextBox1.Text += "原圖 : " + filename + "\n";

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            Compress(bitmap1, "compressfile010.jpg", 10);
            Compress(bitmap1, "compressfile040.jpg", 40);
            Compress(bitmap1, "compressfile070.jpg", 70);
            Compress(bitmap1, "compressfile100.jpg", 100);

        }
        //圖片質量壓縮(不改變尺寸) SP

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //設定圖片解析度
            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

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

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //獲取圖片的指定部分

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            Bitmap bitmap1 = GetPart(filename, 0, 0, 150, 200, 0, 0);

            pictureBox1.Image = bitmap1;
        }

        //C#獲取圖片的指定部分

        /// <summary>
        /// http://www.cnblogs.com/KissKnife/archive/2007/10/13/923352.Html
        /// 獲取圖片指定部分
        /// </summary>
        /// <param name="pPath">圖片路徑</param>
        /// <param name="pPartStartPointX">目標圖片開始繪制處的坐標X值(通常為0)</param>
        /// <param name="pPartStartPointY">目標圖片開始繪制處的坐標Y值(通常為0)</param>
        /// <param name="pPartWidth">目標圖片的寬度</param>
        /// <param name="pPartHeight">目標圖片的高度</param>
        /// <param name="pOrigStartPointX">原始圖片開始截取處的坐標X值</param>
        /// <param name="pOrigStartPointY">原始圖片開始截取處的坐標Y值</param>
        static Bitmap GetPart(string pPath, int pPartStartPointX, int pPartStartPointY, int pPartWidth, int pPartHeight, int pOrigStartPointX, int pOrigStartPointY)
        {
            Image originalImg = Image.FromFile(pPath);

            Bitmap partImg = new Bitmap(pPartWidth, pPartHeight);
            Graphics graphics = Graphics.FromImage(partImg);
            Rectangle destRect = new Rectangle(new Point(pPartStartPointX, pPartStartPointY), new Size(pPartWidth, pPartHeight));//目標位置
            Rectangle origRect = new Rectangle(new Point(pOrigStartPointX, pOrigStartPointY), new Size(pPartWidth, pPartHeight));//原圖位置（默認從原圖中截取的圖片大小等於目標圖片的大小）

            graphics.DrawImage(originalImg, destRect, origRect, GraphicsUnit.Pixel);

            return partImg;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            pictureBox1.Size = new Size(1920, 1080);
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.BringToFront();

            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            timer1.Enabled = true;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //從pictureBox開始畫圖

            int[] gray = new int[220];

            Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
            //g.DrawLines(Pens.Red, gray.ToArray());

            //g.Clear(Color.White);

            g.DrawRectangle(Pens.Red, 0, 0, 440, 256);

            Point[] curvePoints = new Point[220];    //一維陣列內有 8 個Point

            int i;
            for (i = 0; i < 220; i++)
            {
                curvePoints[i].X = i * 2;
                curvePoints[i].Y = i * 2;
            }


            // Draw lines between original points to screen.
            g.DrawLines(Pens.Red, curvePoints);   //畫直線
            // Draw curve to screen.
            //gc.DrawCurve(redPen, curvePoints); //畫曲線


        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            double DPI = pictureBox1.Image.HorizontalResolution;//獲得分辨率 gisoracle
            double w = 1.0 * pictureBox1.Image.Width / DPI * 25.4;
            double h = 1.0 * pictureBox1.Image.Height / DPI * 25.4;

            richTextBox1.Text += "獲得圖片的分辨率和大小 : " + w.ToString("f2") + ":" + h.ToString("f2") + "\n";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //改變圖片品質
            VaryQualityLevel();
        }

        private void VaryQualityLevel()
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

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

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //jpg縮略圖函數
            //在下
        }

        //C#編程 jpg縮略圖函數 使用

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

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            int W = 500;
            int H = 500;

            richTextBox1.Text += "建立空白 Bitmap\n";
            Bitmap bitmap1 = new Bitmap(W, H);

            richTextBox1.Text += "對此Bitmap畫圖\n";
            Graphics g = Graphics.FromImage(bitmap1);

            Color pt;
            int ALPHA = 255;
            int i, j, w, h;
            int x_st, y_st;
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    bitmap1.SetPixel(i, j, Color.FromArgb(ALPHA, 0, 0, 0));
                }
            }

            x_st = 50 + 100;
            y_st = 150;
            w = 300;
            h = 300;
            for (j = y_st; j < y_st + h; j++)
            {
                for (i = x_st; i < x_st + w; i++)
                {
                    pt = bitmap1.GetPixel(i, j);
                    bitmap1.SetPixel(i, j, Color.FromArgb(ALPHA, 255, pt.G, pt.B));
                }
            }

            x_st = 100;
            y_st = 30;
            w = 300;
            h = 300;

            for (j = y_st; j < y_st + h; j++)
            {
                for (i = x_st; i < x_st + w; i++)
                {
                    pt = bitmap1.GetPixel(i, j);
                    bitmap1.SetPixel(i, j, Color.FromArgb(ALPHA, pt.R, 255, pt.B));
                }
            }

            x_st = 50;
            y_st = 150;
            w = 300;
            h = 300;

            for (j = y_st; j < y_st + h; j++)
            {
                for (i = x_st; i < x_st + w; i++)
                {
                    pt = bitmap1.GetPixel(i, j);
                    bitmap1.SetPixel(i, j, Color.FromArgb(ALPHA, pt.R, pt.G, 255));
                }
            }

            pictureBox1.Image = bitmap1;
        }

        private void button17_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //public void bitSlicing(Bitmap Image)
        public void bitSlicing()
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\ims01.bmp"; //stomach

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            int xx;
            int yy;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    byte rrr = bitmap1.GetPixel(xx, yy).R;
                    byte ggg = bitmap1.GetPixel(xx, yy).G;
                    byte bbb = bitmap1.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap1.SetPixel(xx, yy, zz);
                }
            }
            pictureBox1.Image = bitmap1;

            //Bitmap GrayImg = imop.getGrayImage8(Image);

            int width = bitmap1.Width;
            int height = bitmap1.Height;

            Bitmap level1 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level2 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level3 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level4 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level5 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level6 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level7 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level8 = new Bitmap(width, height, PixelFormat.Format24bppRgb);


            BitmapData level1Data = level1.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level2Data = level2.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level3Data = level3.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level4Data = level4.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level5Data = level5.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level6Data = level6.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level7Data = level7.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level8Data = level8.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData GrayImgData = bitmap1.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            int size = GrayImgData.Stride * GrayImgData.Height;

            IntPtr intPtr = GrayImgData.Scan0;
            IntPtr intPtr1 = level1Data.Scan0;
            IntPtr intPtr2 = level2Data.Scan0;
            IntPtr intPtr3 = level3Data.Scan0;
            IntPtr intPtr4 = level4Data.Scan0;
            IntPtr intPtr5 = level5Data.Scan0;
            IntPtr intPtr6 = level6Data.Scan0;
            IntPtr intPtr7 = level7Data.Scan0;
            IntPtr intPtr8 = level8Data.Scan0;


            byte[] GrayImgBytes = new byte[size];
            byte[] level1Bytes = new byte[size];
            byte[] level2Bytes = new byte[size];
            byte[] level3Bytes = new byte[size];
            byte[] level4Bytes = new byte[size];
            byte[] level5Bytes = new byte[size];
            byte[] level6Bytes = new byte[size];
            byte[] level7Bytes = new byte[size];
            byte[] level8Bytes = new byte[size];

            Marshal.Copy(intPtr, GrayImgBytes, 0, size);
            Marshal.Copy(intPtr1, level1Bytes, 0, size);
            Marshal.Copy(intPtr2, level2Bytes, 0, size);
            Marshal.Copy(intPtr3, level3Bytes, 0, size);
            Marshal.Copy(intPtr4, level4Bytes, 0, size);
            Marshal.Copy(intPtr5, level5Bytes, 0, size);
            Marshal.Copy(intPtr6, level6Bytes, 0, size);
            Marshal.Copy(intPtr7, level7Bytes, 0, size);
            Marshal.Copy(intPtr8, level8Bytes, 0, size);

            int k = 3;
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    byte R = GrayImgBytes[i * GrayImgData.Stride + j * k];
                    int L1 = R & 1;
                    if (L1 != 0) { L1 = 255; }
                    int L2 = R & 2;
                    if (L2 != 0) { L2 = 255; }
                    int L3 = R & 4;
                    if (L3 != 0) { L3 = 255; }
                    int L4 = R & 8;
                    if (L4 != 0) { L4 = 255; }
                    int L5 = R & 16;
                    if (L5 != 0) { L5 = 255; }
                    int L6 = R & 32;
                    if (L6 != 0) { L6 = 255; }
                    int L7 = R & 64;
                    if (L7 != 0) { L7 = 255; }
                    int L8 = R & 128;
                    if (L8 != 0) { L8 = 255; }
                    level1Bytes[i * GrayImgData.Stride + j * k] = (byte)L1;
                    level1Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L1;
                    level1Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L1;
                    level2Bytes[i * GrayImgData.Stride + j * k] = (byte)L2;
                    level2Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L2;
                    level2Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L2;
                    level3Bytes[i * GrayImgData.Stride + j * k] = (byte)L3;
                    level3Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L3;
                    level3Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L3;
                    level4Bytes[i * GrayImgData.Stride + j * k] = (byte)L4;
                    level4Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L4;
                    level4Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L4;
                    level5Bytes[i * GrayImgData.Stride + j * k] = (byte)L5;
                    level5Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L5;
                    level5Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L5;
                    level6Bytes[i * GrayImgData.Stride + j * k] = (byte)L6;
                    level6Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L6;
                    level6Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L6;
                    level7Bytes[i * GrayImgData.Stride + j * k] = (byte)L7;
                    level7Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L7;
                    level7Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L7;
                    level8Bytes[i * GrayImgData.Stride + j * k] = (byte)L8;
                    level8Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)L8;
                    level8Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)L8;
                }
            }
            Marshal.Copy(level1Bytes, 0, intPtr1, level1Bytes.Length);
            Marshal.Copy(level2Bytes, 0, intPtr2, level2Bytes.Length);
            Marshal.Copy(level3Bytes, 0, intPtr3, level3Bytes.Length);
            Marshal.Copy(level4Bytes, 0, intPtr4, level4Bytes.Length);
            Marshal.Copy(level5Bytes, 0, intPtr5, level5Bytes.Length);
            Marshal.Copy(level6Bytes, 0, intPtr6, level6Bytes.Length);
            Marshal.Copy(level7Bytes, 0, intPtr7, level7Bytes.Length);
            Marshal.Copy(level8Bytes, 0, intPtr8, level8Bytes.Length);

            level1.UnlockBits(level1Data);
            level2.UnlockBits(level2Data);
            level3.UnlockBits(level3Data);
            level4.UnlockBits(level4Data);
            level5.UnlockBits(level5Data);
            level6.UnlockBits(level6Data);
            level7.UnlockBits(level7Data);
            level8.UnlockBits(level8Data);
            bitmap1.UnlockBits(GrayImgData);

            int W = pictureBox1.Size.Width;
            int H = pictureBox1.Size.Height;
            Bitmap bmp = new Bitmap(W - 50, H - 50);

            Graphics g = Graphics.FromImage(bmp);
            //g.DrawRectangle(Pens.Red, 100, 100, 100, 100);

            int w = 640 * 3 / 8;
            int h = 480 * 3 / 9;
            int x_st = 20;
            int y_st = 20;
            int dx = w + 20;
            int dy = h + 20;

            g.DrawImage(level1, x_st + dx * 0, y_st + dy * 0, w, h);
            g.DrawImage(level2, x_st + dx * 0, y_st + dy * 1, w, h);
            g.DrawImage(level3, x_st + dx * 0, y_st + dy * 2, w, h);
            g.DrawImage(level4, x_st + dx * 0, y_st + dy * 3, w, h);
            g.DrawImage(level5, x_st + dx * 1, y_st + dy * 0, w, h);
            g.DrawImage(level6, x_st + dx * 1, y_st + dy * 1, w, h);
            g.DrawImage(level7, x_st + dx * 1, y_st + dy * 2, w, h);
            g.DrawImage(level8, x_st + dx * 1, y_st + dy * 3, w, h);

            pictureBox1.Image = bmp;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //灰階位圖分割 (bit-plane slicing)
            //自然二進位分割

            pictureBox1.BackColor = Color.Pink;
            pictureBox1.Size = new Size(512 * 2 - 250, 800);

            bitSlicing();
        }

        //public void grayCodeSlicing(Bitmap Image)
        public void grayCodeSlicing()
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\ims01.bmp"; //stomach

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            int xx;
            int yy;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    byte rrr = bitmap1.GetPixel(xx, yy).R;
                    byte ggg = bitmap1.GetPixel(xx, yy).G;
                    byte bbb = bitmap1.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap1.SetPixel(xx, yy, zz);
                }
            }
            pictureBox1.Image = bitmap1;

            //Bitmap GrayImg = imop.getGrayImage8(Image);

            int width = bitmap1.Width;
            int height = bitmap1.Height;

            Bitmap level1 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level2 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level3 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level4 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level5 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level6 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level7 = new Bitmap(width, height, PixelFormat.Format24bppRgb);
            Bitmap level8 = new Bitmap(width, height, PixelFormat.Format24bppRgb);


            BitmapData level1Data = level1.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level2Data = level2.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level3Data = level3.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level4Data = level4.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level5Data = level5.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level6Data = level6.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level7Data = level7.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData level8Data = level8.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData GrayImgData = bitmap1.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            int size = GrayImgData.Stride * GrayImgData.Height;

            IntPtr intPtr = GrayImgData.Scan0;
            IntPtr intPtr1 = level1Data.Scan0;
            IntPtr intPtr2 = level2Data.Scan0;
            IntPtr intPtr3 = level3Data.Scan0;
            IntPtr intPtr4 = level4Data.Scan0;
            IntPtr intPtr5 = level5Data.Scan0;
            IntPtr intPtr6 = level6Data.Scan0;
            IntPtr intPtr7 = level7Data.Scan0;
            IntPtr intPtr8 = level8Data.Scan0;


            byte[] GrayImgBytes = new byte[size];
            byte[] level1Bytes = new byte[size];
            byte[] level2Bytes = new byte[size];
            byte[] level3Bytes = new byte[size];
            byte[] level4Bytes = new byte[size];
            byte[] level5Bytes = new byte[size];
            byte[] level6Bytes = new byte[size];
            byte[] level7Bytes = new byte[size];
            byte[] level8Bytes = new byte[size];

            Marshal.Copy(intPtr, GrayImgBytes, 0, size);
            Marshal.Copy(intPtr1, level1Bytes, 0, size);
            Marshal.Copy(intPtr2, level2Bytes, 0, size);
            Marshal.Copy(intPtr3, level3Bytes, 0, size);
            Marshal.Copy(intPtr4, level4Bytes, 0, size);
            Marshal.Copy(intPtr5, level5Bytes, 0, size);
            Marshal.Copy(intPtr6, level6Bytes, 0, size);
            Marshal.Copy(intPtr7, level7Bytes, 0, size);
            Marshal.Copy(intPtr8, level8Bytes, 0, size);

            int k = 3;
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    byte R = GrayImgBytes[i * GrayImgData.Stride + j * k];
                    int L1 = R & 1;
                    if (L1 != 0) { L1 = 1; }
                    int L2 = R & 2;
                    if (L2 != 0) { L2 = 1; }
                    int L3 = R & 4;
                    if (L3 != 0) { L3 = 1; }
                    int L4 = R & 8;
                    if (L4 != 0) { L4 = 1; }
                    int L5 = R & 16;
                    if (L5 != 0) { L5 = 1; }
                    int L6 = R & 32;
                    if (L6 != 0) { L6 = 1; }
                    int L7 = R & 64;
                    if (L7 != 0) { L7 = 1; }
                    int L8 = R & 128;
                    if (L8 != 0) { L8 = 1; }

                    int G8 = L8;
                    if (G8 != 0) { G8 = 255; }
                    int G7 = L8 ^ L7;
                    if (G7 != 0) { G7 = 255; }
                    int G6 = L7 ^ L6;
                    if (G6 != 0) { G6 = 255; }
                    int G5 = L6 ^ L5;
                    if (G5 != 0) { G5 = 255; }
                    int G4 = L5 ^ L4;
                    if (G4 != 0) { G4 = 255; }
                    int G3 = L4 ^ L3;
                    if (G3 != 0) { G3 = 255; }
                    int G2 = L3 ^ L2;
                    if (G2 != 0) { G2 = 255; }
                    int G1 = L2 ^ L1;
                    if (G1 != 0) { G1 = 255; }

                    level1Bytes[i * GrayImgData.Stride + j * k] = (byte)G1;
                    level1Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G1;
                    level1Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G1;
                    level2Bytes[i * GrayImgData.Stride + j * k] = (byte)G2;
                    level2Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G2;
                    level2Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G2;
                    level3Bytes[i * GrayImgData.Stride + j * k] = (byte)G3;
                    level3Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G3;
                    level3Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G3;
                    level4Bytes[i * GrayImgData.Stride + j * k] = (byte)G4;
                    level4Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G4;
                    level4Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G4;
                    level5Bytes[i * GrayImgData.Stride + j * k] = (byte)G5;
                    level5Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G5;
                    level5Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G5;
                    level6Bytes[i * GrayImgData.Stride + j * k] = (byte)G6;
                    level6Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G6;
                    level6Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G6;
                    level7Bytes[i * GrayImgData.Stride + j * k] = (byte)G7;
                    level7Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G7;
                    level7Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G7;
                    level8Bytes[i * GrayImgData.Stride + j * k] = (byte)G8;
                    level8Bytes[i * GrayImgData.Stride + j * k + 1] = (byte)G8;
                    level8Bytes[i * GrayImgData.Stride + j * k + 2] = (byte)G8;
                }
            }
            Marshal.Copy(level1Bytes, 0, intPtr1, level1Bytes.Length);
            Marshal.Copy(level2Bytes, 0, intPtr2, level2Bytes.Length);
            Marshal.Copy(level3Bytes, 0, intPtr3, level3Bytes.Length);
            Marshal.Copy(level4Bytes, 0, intPtr4, level4Bytes.Length);
            Marshal.Copy(level5Bytes, 0, intPtr5, level5Bytes.Length);
            Marshal.Copy(level6Bytes, 0, intPtr6, level6Bytes.Length);
            Marshal.Copy(level7Bytes, 0, intPtr7, level7Bytes.Length);
            Marshal.Copy(level8Bytes, 0, intPtr8, level8Bytes.Length);

            level1.UnlockBits(level1Data);
            level2.UnlockBits(level2Data);
            level3.UnlockBits(level3Data);
            level4.UnlockBits(level4Data);
            level5.UnlockBits(level5Data);
            level6.UnlockBits(level6Data);
            level7.UnlockBits(level7Data);
            level8.UnlockBits(level8Data);
            bitmap1.UnlockBits(GrayImgData);


            int W = pictureBox1.Size.Width;
            int H = pictureBox1.Size.Height;
            Bitmap bmp = new Bitmap(W - 50, H - 50);

            Graphics g = Graphics.FromImage(bmp);
            //g.DrawRectangle(Pens.Red, 100, 100, 100, 100);

            int w = 640 * 3 / 8;
            int h = 480 * 3 / 9;
            int x_st = 20;
            int y_st = 20;
            int dx = w + 20;
            int dy = h + 20;

            g.DrawImage(level1, x_st + dx * 0, y_st + dy * 0, w, h);
            g.DrawImage(level2, x_st + dx * 0, y_st + dy * 1, w, h);
            g.DrawImage(level3, x_st + dx * 0, y_st + dy * 2, w, h);
            g.DrawImage(level4, x_st + dx * 0, y_st + dy * 3, w, h);
            g.DrawImage(level5, x_st + dx * 1, y_st + dy * 0, w, h);
            g.DrawImage(level6, x_st + dx * 1, y_st + dy * 1, w, h);
            g.DrawImage(level7, x_st + dx * 1, y_st + dy * 2, w, h);
            g.DrawImage(level8, x_st + dx * 1, y_st + dy * 3, w, h);

            pictureBox1.Image = bmp;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //格雷碼風格

            pictureBox1.BackColor = Color.Pink;
            pictureBox1.Size = new Size(512 * 2 - 250, 800);

            grayCodeSlicing();
        }


        private void button20_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //撈出所有圖片檔 並存成一個List
            string foldername = @"C:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";

            filenames.Clear();

            GetAllFiles(foldername);
            int len = filenames.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";
            }
        }

        List<String> filenames = new List<String>();
        //多層 且指明副檔名
        public void GetAllFiles(string foldername)
        {
            DirectoryInfo di = new DirectoryInfo(foldername);
            //richTextBox1.Text += "資料夾 : " + di.FullName + "\n";
            FileSystemInfo[] fileinfo = di.GetFileSystemInfos();
            foreach (FileSystemInfo fi in fileinfo)
            {
                if (fi is DirectoryInfo)
                {
                    GetAllFiles(((DirectoryInfo)fi).FullName);
                }
                else
                {
                    string fullname = fi.FullName;
                    string shortname = fi.Name;
                    string ext = fi.Extension.ToLower();
                    string forename = shortname.Substring(0, shortname.Length - ext.Length);    //前檔名

                    if (ext == ".jpg" || ext == ".jpeg" || ext == ".bmp" || ext == ".png" || ext == ".gif")
                    {
                        //richTextBox1.Text += "長檔名: " + fullname + "\t副檔名: " + ext + "\n";
                        //richTextBox1.Text += "短檔名: " + shortname + "\n";
                        //richTextBox1.Text += "前檔名: " + forename + "\n";
                        filenames.Add(fullname);
                    }
                }
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_button_text(sender);


            string foldername = @"C:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony1";

            filenames.Clear();

            if (Directory.Exists(foldername) == false)
            {
                richTextBox1.Text += "圖片資料夾不存在, 離開\n";
                return;
            }

            // Load the list of files.
            filenames = FindFiles(foldername, "*.bmp;*.png;*.jpg;*.tif;*.gif", false);

            for (int i = 0; i < filenames.Count; i++)
            {
                richTextBox1.Text += "get file \t" + filenames[i] + "\n";
            }
            richTextBox1.Text += "共有 " + filenames.Count.ToString() + " 個檔案\n";
        }

        // See: Search for files that match multiple patterns in C#
        //      http://csharphelper.com/blog/2015/06/find-files-that-match-multiple-patterns-in-c/
        // Search for files matching the patterns.
        private List<string> FindFiles(string fname, string patterns, bool search_subdirectories)
        {
            // Make the result list.
            List<string> files = new List<string>();

            // Get the patterns.
            string[] pattern_array = patterns.Split(';');

            // Search.
            SearchOption search_option = SearchOption.TopDirectoryOnly;
            if (search_subdirectories) search_option = SearchOption.AllDirectories;
            foreach (string pattern in pattern_array)
            {
                foreach (string filename in Directory.GetFiles(fname, pattern, search_option))
                {
                    if (!files.Contains(filename)) files.Add(filename);
                }
            }

            // Sort.
            files.Sort();

            // Return the result.
            return files;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //圖片壓縮、縮略圖生成代碼

        #region imageCompress
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
        #endregion

        /*  
        圖片壓縮、縮略圖生成代碼匯總
        public static bool imageCompress(String sourceFile,long quality,String outputFile)
        public static bool getThumImage(String sourceFile, long quality, int multiple, String outputFile)
        */


        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //圖片壓縮
            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = Application.StartupPath + "\\compress_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            bool result = imageCompress(filename1, 30, filename2);
            if (result == true)
                richTextBox1.Text += "OK\n";
            else
                richTextBox1.Text += "FAIL\n";
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

        int W = 0;
        int H = 0;
        int cx = 0;
        int cy = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            W = pictureBox1.Width;
            H = pictureBox1.Height;

            richTextBox1.Text += "圖片寬度 : " + W.ToString() + "\n";
            richTextBox1.Text += "圖片高度 : " + H.ToString() + "\n";

            cx += 5;
            cy += 5;
            if (cx > W)
                cx = 0;
            if (cy > H)
                cy = 0;

            Bitmap bitmap1 = new Bitmap(W, H);

            int i;
            int j;

            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    int dist = (int)Math.Sqrt((i - cx) * (i - cx) + (j - cy) * (j - cy));
                    if (dist > 255)
                        dist = 255;

                    bitmap1.SetPixel(i, j, Color.FromArgb(255, dist, dist, 128));
                }
            }
            Graphics g = Graphics.FromImage(bitmap1);
            //g.DrawRectangle(Pens.Red, 5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10);

            pictureBox1.Image = bitmap1;
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

                    string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_" + i.ToString("D2") + "_" + j.ToString("D2") + ".bmp";
                    //Console.WriteLine(filename2);

                    try
                    {
                        bitmap2.Save(filename2, ImageFormat.Bmp);
                        //richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show(ex.Message);
                        //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                    }
                }
            }
        }
    }
}
