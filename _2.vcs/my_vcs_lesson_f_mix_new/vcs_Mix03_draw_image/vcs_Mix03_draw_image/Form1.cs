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
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //圖片剪下一塊存檔, 圖片裁剪
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = @"C:\______test_files\picture1_cut.jpg";

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
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = @"C:\______test_files\picture1_cut.jpg";

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
            //影像資料處理1
            string filename = @"C:\______test_files\__pic\rgb.bmp";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //影像資料處理2
            Graphics g = this.pictureBox1.CreateGraphics();

            string filename = @"C:\______test_files\__pic\rgb.jpg";

            richTextBox1.Text += "filename : " + filename + "\n";
            //Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);  //使用Image.FromFile創建圖形對象 same
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            int bytes_per_pixel = 0;    //每個像素使用的拜數 bmp/png每點用4拜, jpg每點用3拜

            g.DrawImage(bitmap1, 0, 0);

            //把圖像複製到內存中

            //獲取圖像的BitmapData對像
            Rectangle rect = new Rectangle(0, 0, W, H);	//位圖矩形

            //以可讀寫的方式鎖定全部位圖像素
            BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, bitmap1.PixelFormat);   // Lock the bits.
            //BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb); //指明PixelFormat

            // Get the address of the first line.
            IntPtr ptr = bmpData.Scan0; //得到首地址

            // Declare an array to hold the bytes of the bitmap.
            //int len = W * 4 * H;    //每個pixel要用4拜存資料 R G B A
            int len = Math.Abs(bmpData.Stride) * H;   //24位BMP位圖字節數 stride = W * 4, 每個pixel要用4拜存資料 R G B A, 也有可能是3拜
            //stride : 每個掃描行的長度

            bytes_per_pixel = Math.Abs(bmpData.Stride) / W;

            richTextBox1.Text += "stride = " + bmpData.Stride.ToString() + "\n";
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            //存bitmap資料的陣列
            byte[] rgbValues = new byte[len]; //定義位圖數組

            richTextBox1.Text += "len = " + len.ToString() + "\n";
            // Copy the RGB values into the array.
            Marshal.Copy(ptr, rgbValues, 0, len); //複製被鎖定的位圖像素到位圖數組

            richTextBox1.Text += "len2 = " + rgbValues.Length.ToString() + "\n";
            int i;
            string result = string.Empty;
            for (i = 0; i < len; i++)
            {
                if ((bytes_per_pixel == 4) && (((i % (256 * bytes_per_pixel)) == (256 * bytes_per_pixel - 1))))
                {
                    result += "\n";
                }

                if ((bytes_per_pixel == 4) && ((i % 4) == 3))
                    continue;

                result += rgbValues[i].ToString("X2");
                if ((i % (256 * bytes_per_pixel)) == (256 * bytes_per_pixel - 1))
                {
                    result += "\n";
                }
                else
                {
                    result += " ";
                }
            }
            richTextBox1.Text += result + "\n";

            // Set every third value to 255. A 24bpp bitmap will look red.  
            for (int counter = 2; counter < rgbValues.Length; counter += bytes_per_pixel)
            {
                rgbValues[counter] = 255;
            }

            // Copy the RGB values back to the bitmap
            Marshal.Copy(rgbValues, 0, ptr, len);

            // Unlock the bits.
            bitmap1.UnlockBits(bmpData);

            // Draw the modified image.
            g.DrawImage(bitmap1, 0, 50);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //設定圖片解析度
            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            string filename = @"C:\______test_files\picture1.jpg";

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

            string filename = @"C:\______test_files\picture1.jpg";

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
        }

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //畫OV亮度

            int[] gray = new int[220];
            gray[0] = 4;
            gray[1] = 6;
            gray[2] = 9;
            gray[3] = 11;
            gray[4] = 14;
            gray[5] = 16;
            gray[6] = 18;
            gray[7] = 20;
            gray[8] = 22;
            gray[9] = 24;
            gray[10] = 26;
            gray[11] = 28;
            gray[12] = 30;
            gray[13] = 32;
            gray[14] = 33;
            gray[15] = 35;
            gray[16] = 37;
            gray[17] = 38;
            gray[18] = 40;
            gray[19] = 41;
            gray[20] = 43;
            gray[21] = 44;
            gray[22] = 46;
            gray[23] = 47;
            gray[24] = 49;
            gray[25] = 50;
            gray[26] = 51;
            gray[27] = 53;
            gray[28] = 54;
            gray[29] = 55;
            gray[30] = 57;
            gray[31] = 58;
            gray[32] = 59;
            gray[33] = 61;
            gray[34] = 62;
            gray[35] = 63;
            gray[36] = 65;
            gray[37] = 66;
            gray[38] = 67;
            gray[39] = 68;
            gray[40] = 70;
            gray[41] = 71;
            gray[42] = 72;
            gray[43] = 73;
            gray[44] = 74;
            gray[45] = 75;
            gray[46] = 77;
            gray[47] = 78;
            gray[48] = 79;
            gray[49] = 80;
            gray[50] = 81;
            gray[51] = 82;
            gray[52] = 83;
            gray[53] = 84;
            gray[54] = 85;
            gray[55] = 86;
            gray[56] = 87;
            gray[57] = 88;
            gray[58] = 89;
            gray[59] = 90;
            gray[60] = 91;
            gray[61] = 92;
            gray[62] = 93;
            gray[63] = 94;
            gray[64] = 95;
            gray[65] = 96;
            gray[66] = 97;
            gray[67] = 98;
            gray[68] = 99;
            gray[69] = 99;
            gray[70] = 100;
            gray[71] = 101;
            gray[72] = 102;
            gray[73] = 103;
            gray[74] = 103;
            gray[75] = 104;
            gray[76] = 105;
            gray[77] = 106;
            gray[78] = 106;
            gray[79] = 107;
            gray[80] = 108;
            gray[81] = 109;
            gray[82] = 109;
            gray[83] = 110;
            gray[84] = 111;
            gray[85] = 111;
            gray[86] = 112;
            gray[87] = 113;
            gray[88] = 113;
            gray[89] = 114;
            gray[90] = 115;
            gray[91] = 115;
            gray[92] = 116;
            gray[93] = 116;
            gray[94] = 117;
            gray[95] = 118;
            gray[96] = 118;
            gray[97] = 119;
            gray[98] = 119;
            gray[99] = 120;
            gray[100] = 120;
            gray[101] = 121;
            gray[102] = 122;
            gray[103] = 122;
            gray[104] = 123;
            gray[105] = 123;
            gray[106] = 124;
            gray[107] = 124;
            gray[108] = 125;
            gray[109] = 125;
            gray[110] = 126;
            gray[111] = 126;
            gray[112] = 127;
            gray[113] = 127;
            gray[114] = 128;
            gray[115] = 128;
            gray[116] = 129;
            gray[117] = 129;
            gray[118] = 130;
            gray[119] = 130;
            gray[120] = 130;
            gray[121] = 131;
            gray[122] = 131;
            gray[123] = 132;
            gray[124] = 132;
            gray[125] = 133;
            gray[126] = 133;
            gray[127] = 134;
            gray[128] = 134;
            gray[129] = 134;
            gray[130] = 135;
            gray[131] = 135;
            gray[132] = 136;
            gray[133] = 136;
            gray[134] = 140;
            gray[135] = 143;
            gray[136] = 145;
            gray[137] = 149;
            gray[138] = 151;
            gray[139] = 153;
            gray[140] = 156;
            gray[141] = 159;
            gray[142] = 161;
            gray[143] = 163;
            gray[144] = 165;
            gray[145] = 168;
            gray[146] = 169;
            gray[147] = 171;
            gray[148] = 173;
            gray[149] = 176;
            gray[150] = 179;
            gray[151] = 182;
            gray[152] = 184;
            gray[153] = 187;
            gray[154] = 189;
            gray[155] = 191;
            gray[156] = 193;
            gray[157] = 196;
            gray[158] = 197;
            gray[159] = 199;
            gray[160] = 200;
            gray[161] = 202;
            gray[162] = 203;
            gray[163] = 204;
            gray[164] = 206;
            gray[165] = 207;
            gray[166] = 209;
            gray[167] = 211;
            gray[168] = 212;
            gray[169] = 214;
            gray[170] = 215;
            gray[171] = 216;
            gray[172] = 217;
            gray[173] = 218;
            gray[174] = 219;
            gray[175] = 219;
            gray[176] = 220;
            gray[177] = 220;
            gray[178] = 221;
            gray[179] = 221;
            gray[180] = 221;
            gray[181] = 222;
            gray[182] = 222;
            gray[183] = 223;
            gray[184] = 223;
            gray[185] = 223;
            gray[186] = 223;
            gray[187] = 224;
            gray[188] = 224;
            gray[189] = 223;
            gray[190] = 224;
            gray[191] = 224;
            gray[192] = 225;
            gray[193] = 225;
            gray[194] = 225;
            gray[195] = 225;
            gray[196] = 226;
            gray[197] = 226;
            gray[198] = 226;
            gray[199] = 226;
            gray[200] = 226;
            gray[201] = 226;
            gray[202] = 226;
            gray[203] = 226;
            gray[204] = 226;
            gray[205] = 226;
            gray[206] = 226;
            gray[207] = 226;
            gray[208] = 226;
            gray[209] = 226;
            gray[210] = 226;
            gray[211] = 226;
            gray[212] = 226;
            gray[213] = 226;
            gray[214] = 226;
            gray[215] = 226;
            gray[216] = 226;
            gray[217] = 226;
            gray[218] = 226;
            gray[219] = 226;

            Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
            //g.DrawLines(Pens.Red, gray.ToArray());

            g.Clear(Color.White);

            g.DrawRectangle(Pens.Red, 0, 0, 440, 256);
            Point[] curvePoints = new Point[220];    //一維陣列內有 8 個Point

            int i;
            for (i = 0; i < 220; i++)
            {
                curvePoints[i].X = i * 2;
                curvePoints[i].Y = 255 - (gray[i]);
            }


            // Draw lines between original points to screen.
            g.DrawLines(Pens.Red, curvePoints);   //畫直線
            // Draw curve to screen.
            //gc.DrawCurve(redPen, curvePoints); //畫曲線


        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //給圖片添加版權信息

            //創建一張位圖
            Bitmap bitmap = new Bitmap(this.pictureBox1.Width, this.pictureBox1.Height, System.Drawing.Imaging.PixelFormat.Format24bppRgb);

            //根據位圖獲取畫布
            Graphics g = Graphics.FromImage(bitmap);

            //清空畫布並用透明色填充
            g.Clear(Color.Transparent);

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            //將另一幅圖片畫到畫布上
            g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);

            //寫版權信息到圖片上。
            g.DrawString("群曜醫電", new Font("黑體", 15), new SolidBrush(Color.Red), new Rectangle(20, 20, 100, 100));

            //顯示
            this.pictureBox1.Image = bitmap;

            //保存圖片
            bitmap.Save("abc.bmp", System.Drawing.Imaging.ImageFormat.Bmp);
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

            //改變圖片品質
            VaryQualityLevel();
        }

        private void VaryQualityLevel()
        {
            string filename = @"C:\______test_files\elephant.jpg";

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
            //撈出所有圖片檔 並存成一個List
            string foldername = @"C:\______test_files\__pic";

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
                        richTextBox1.Text += "短檔名: " + shortname + "\n";
                        richTextBox1.Text += "前檔名: " + forename + "\n";
                        //filenames.Add(fullname);
                    }
                }
            }
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

            //圖片 拜列 MemoryStream Bitmap轉換

            string filename = @"C:\______test_files\picture1.jpg";

            richTextBox1.Text += "圖檔 轉 Bitmap\n";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            richTextBox1.Text += "Bitmap 轉 MemoryStream\n";
            MemoryStream ms = new MemoryStream();
            bitmap1.Save(ms, ImageFormat.Jpeg);

            richTextBox1.Text += "MemoryStream 轉 拜列\n";
            byte[] pic_array1 = ms.ToArray();


            richTextBox1.Text += "建立空白 Bitmap\n";
            bitmap1 = new Bitmap(100, 100);

            richTextBox1.Text += "對此Bitmap畫圖\n";
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            ms = new MemoryStream();
            bitmap1.Save(ms, ImageFormat.Bmp);
            byte[] pic_array2 = ms.ToArray();

            richTextBox1.Text += "len = " + pic_array2.Length.ToString() + "\n";


        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //圖片壓縮
            string filename1 = @"C:\______test_files\picture1.jpg";
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
                        MessageBox.Show(ex.Message);
                        //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                    }
                }
            }
        }
    }
}

