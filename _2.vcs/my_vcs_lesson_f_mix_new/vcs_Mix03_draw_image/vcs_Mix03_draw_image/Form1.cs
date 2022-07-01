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
            //圖像切割 每100X100 切成一個小圖
            ImageManager.Cut(filename, 100, 100);
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

            //圖片剪下一塊存檔
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = @"C:\______test_files\picture1_cut.jpg";

            ImgReduceCutOut(200, 200, filename1, filename2);

            //看起來像是 305X400 轉成200X200
            richTextBox1.Text += "原檔案 : " + filename1 + "\n";
            richTextBox1.Text += "圖片剪下一塊存檔 : " + filename2 + "\n";
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



        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

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

            Bitmap img = b.Clone(new Rectangle(0, top, initImage.Width, height), PixelFormat.DontCare);
            return (Image)(img);
        }

        public static Image CutForCustomx(string imgPath, Rectangle rec)
        {
            FileStream fs = new FileStream(imgPath, FileMode.Open, FileAccess.Read);
            //從文件獲取原始圖片，並使用流中嵌入的顏色管理信息
            System.Drawing.Image initImage = System.Drawing.Image.FromStream(fs, true);

            Bitmap b = new Bitmap(initImage);

            Bitmap img = b.Clone(rec, PixelFormat.DontCare);
            return (Image)(img);
        }

        //圖片質量壓縮(不改變尺寸) ST
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
        public static void Compress(Bitmap srcBitMap, string destFile, long level)
        {
            Stream s = new FileStream(destFile, FileMode.Create);
            Compress(srcBitMap, s, level);
            s.Close();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //圖片質量壓縮(不改變尺寸)
            
            string filename = @"C:\______test_files\elephant.jpg";
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

            richTextBox1.Text += "獲得圖片的分辨率和大小 : " + w.ToString("f2") + ":" + h.ToString("f2") + "\n";
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


            //檢視圖片的像素
            string filename = @"C:\______test_files\picture1.jpg";

            Image image = Image.FromFile(filename);
            richTextBox1.Text += "檔案 : " + filename + ",\t" + "圖片像素：[" + image.Width + "*" + image.Height + "]" + "\n";

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
                        //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                    }
                }
            }
        }
    }
}
