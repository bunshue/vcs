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


            //逐點製作圖檔
            /*
            int dd = 1;    //相隔
            int nx = 256 / dd;
            int ny = 256 / dd;
            int nz = 256 / dd;

            int total_points = nx * ny * nz;  //共有？點

            richTextBox1.Text += "相隔 : " + dd.ToString() + "\n";
            richTextBox1.Text += "nx : " + nx.ToString() + "\n";
            richTextBox1.Text += "ny : " + ny.ToString() + "\n";
            richTextBox1.Text += "nz : " + nz.ToString() + "\n";
            richTextBox1.Text += "共有 : " + total_points.ToString() + " 點\n";

            richTextBox1.Text += "sqrt = " + Math.Sqrt(total_points).ToString() + "\n";

            //int W = (int)Math.Sqrt(total_points);
            //int H = (int)Math.Sqrt(total_points);
            int W = 2048;
            int H = total_points / W;

            richTextBox1.Text += "圖片寬度 : " + W.ToString() + "\n";
            richTextBox1.Text += "圖片高度 : " + H.ToString() + "\n";

            Bitmap bitmap1 = new Bitmap(W, H);

            int i;
            int j;
            int k;
            int xx;
            int yy;
            int index = 0;

            for (k = 0; k < 256; k += dd)
            {
                for (j = 0; j < 256; j += dd)
                {
                    for (i = 0; i < 256; i += dd)
                    {

                        xx = index % W;
                        yy = index / W;

             
             //richTextBox1.Text += "(" + xx.ToString() + "," + yy.ToString() + ")";
                        //if ((index % 16) == 15)
                          //  richTextBox1.Text += "\n";
                        

                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, i, j, k));



                        index++;

                    }

                }

            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "total = " + index.ToString() + "\n";

            bitmap1.Save("all_color.bmp", ImageFormat.Bmp);

            pictureBox1.Image = bitmap1;
            */


            //逐點製作圖檔
            int dd = 1;    //相隔
            int nx = 256 / dd;
            int ny = 256 / dd;

            int total_points = nx * ny; ;  //共有？點

            richTextBox1.Text += "相隔 : " + dd.ToString() + "\n";
            richTextBox1.Text += "nx : " + nx.ToString() + "\n";
            richTextBox1.Text += "ny : " + ny.ToString() + "\n";
            richTextBox1.Text += "共有 : " + total_points.ToString() + " 點\n";

            //richTextBox1.Text += "sqrt = " + Math.Sqrt(total_points).ToString() + "\n";

            //int W = (int)Math.Sqrt(total_points);
            //int H = (int)Math.Sqrt(total_points);
            int W = 256;
            int H = total_points / W;

            richTextBox1.Text += "圖片寬度 : " + W.ToString() + "\n";
            richTextBox1.Text += "圖片高度 : " + H.ToString() + "\n";

            Bitmap bitmap1 = new Bitmap(W, H);

            int i;
            int j;
            //int k;
            //int xx;
            //int yy;
            int index = 0;

            //for(x=1,y=1,z=1; x+y+z<15; z++)

            for (j = 0; j < 256; j += dd)
            {
                for (i = 0; i < 256; i += dd)
                {

                    bitmap1.SetPixel(i, j, Color.FromArgb(255, i, i, i));

                    index++;

                }
            }

            richTextBox1.Text += "\n";

            richTextBox1.Text += "total = " + index.ToString() + "\n";

            bitmap1.Save("all_color.bmp", ImageFormat.Bmp);

            pictureBox1.Image = bitmap1;

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
            //影像資料處理1
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\rgb.bmp";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
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

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            //將另一幅圖片畫到畫布上
            g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);

            //寫版權信息到圖片上。
            g.DrawString("群曜醫電", new Font("黑體", 15), new SolidBrush(Color.Red), new Rectangle(20, 20, 100, 100));

            //顯示
            this.pictureBox1.Image = bitmap;

            //保存圖片
            bitmap.Save("abc.bmp", ImageFormat.Bmp);
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

        double red = 0;
        double green = 0;
        double blue = 0;

        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //test

            //title: "Wavelength",
            //value: 500,
            //units: "nm",
            //range:[380,780],
            //resolution:1
            /*
            int wavelength = 720;
            nmToRGB(wavelength);
            richTextBox1.Text += "R = " + red.ToString() + "\n";
            richTextBox1.Text += "G = " + green.ToString() + "\n";
            richTextBox1.Text += "B = " + blue.ToString() + "\n";
            this.BackColor = Color.FromArgb(255, (int)red, (int)green, (int)blue);
            */


            Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
            //g.DrawLines(Pens.Red, gray.ToArray());

            g.Clear(Color.White);

            g.DrawRectangle(Pens.Red, 0, 0, 440, 300);

            for (int wavelength = 380; wavelength <= 780; wavelength += 4)
            {
                nmToRGB(wavelength);
                Color cc = Color.FromArgb(255, (int)red, (int)green, (int)blue);

                g.DrawLine(new Pen(cc, 2), wavelength - 380, 0, wavelength - 380, 300);

            }


            /*
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

            */

        }


        void nmToRGB(int wavelength)
        {
            var Gamma = 0.80;
            var IntensityMax = 255;
            double factor = 0;

            red = 0;
            green = 0;
            blue = 0;

            if ((wavelength >= 380) && (wavelength < 440))
            {
                red = -(wavelength - 440) / (440 - 380);
                green = 0.0;
                blue = 1.0;
            }
            else if ((wavelength >= 440) && (wavelength < 490))
            {
                red = 0.0;
                green = (wavelength - 440) / (490 - 440);
                blue = 1.0;
            }
            else if ((wavelength >= 490) && (wavelength < 510))
            {
                red = 0.0;
                green = 1.0;
                blue = -(wavelength - 510) / (510 - 490);
            }
            else if ((wavelength >= 510) && (wavelength < 580))
            {
                red = (wavelength - 510) / (580 - 510);
                green = 1.0;
                blue = 0.0;
            }
            else if ((wavelength >= 580) && (wavelength < 645))
            {
                red = 1.0;
                green = -(wavelength - 645) / (645 - 580);
                blue = 0.0;
            }
            else if ((wavelength >= 645) && (wavelength < 781))
            {
                red = 1.0;
                green = 0.0;
                blue = 0.0;
            }
            else
            {
                red = 0.0;
                green = 0.0;
                blue = 0.0;
            };
            // Let the intensity fall off near the vision limits
            if ((wavelength >= 380) && (wavelength < 420))
            {
                factor = 0.3 + 0.7 * (wavelength - 380) / (420 - 380);
            }
            else if ((wavelength >= 420) && (wavelength < 701))
            {
                factor = 1.0;
            }
            else if ((wavelength >= 701) && (wavelength < 781))
            {
                factor = 0.3 + 0.7 * (780 - wavelength) / (780 - 700);
            }
            else
            {
                factor = 0.0;
            };
            if (red != 0)
            {
                red = Math.Round(IntensityMax * Math.Pow(red * factor, Gamma));
            }
            if (green != 0)
            {
                green = Math.Round(IntensityMax * Math.Pow(green * factor, Gamma));
            }
            if (blue != 0)
            {
                blue = Math.Round(IntensityMax * Math.Pow(blue * factor, Gamma));
            }
            //return [red,green,blue];
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

            x_st = 50;
            y_st = 50 + 50;
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

            x_st = 150;
            y_st = 50;
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

            x_st = 100;
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

            double[] gray = new double[350];

            gray[0] = 1.00900867283951;
            gray[1] = 1.55640148148148;
            gray[2] = 6.88660753086508;
            gray[3] = 13.8359580864256;
            gray[4] = 22.2184109876531;
            gray[5] = 28.8497460493796;
            gray[6] = 35.1483108950597;
            gray[7] = 41.1816046913577;
            gray[8] = 47.0013740740761;
            gray[9] = 52.7444471604969;
            gray[10] = 58.4925512037076;
            gray[11] = 63.9892757098829;
            gray[12] = 69.3183035185245;
            gray[13] = 74.658451172845;
            gray[14] = 79.5170869444495;
            gray[15] = 84.2333481790164;
            gray[16] = 88.7950452160538;
            gray[17] = 93.0260337963002;
            gray[18] = 97.0959177469191;
            gray[19] = 100.895518518523;
            gray[20] = 104.753417654325;
            gray[21] = 108.480677623462;
            gray[22] = 111.923783209881;
            gray[23] = 115.318282376547;
            gray[24] = 118.73543848766;
            gray[25] = 121.954907129633;
            gray[26] = 125.221329537043;
            gray[27] = 128.286525401239;
            gray[28] = 131.279339320992;
            gray[29] = 134.269772191361;
            gray[30] = 137.161603086425;
            gray[31] = 139.885520925932;
            gray[32] = 142.783000679017;
            gray[33] = 145.460383024694;
            gray[34] = 148.00202308642;
            gray[35] = 150.552878395065;
            gray[36] = 153.032126111112;
            gray[37] = 155.394792037037;
            gray[38] = 157.690436111109;
            gray[39] = 159.952090216048;
            gray[40] = 162.11185265432;
            gray[41] = 164.291073333329;
            gray[42] = 166.364057191354;
            gray[43] = 168.334361172833;
            gray[44] = 170.409032191347;
            gray[45] = 172.372230740727;
            gray[46] = 174.270800524679;
            gray[47] = 176.171832314801;
            gray[48] = 178.050211543195;
            gray[49] = 179.892309444431;
            gray[50] = 181.781950185169;
            gray[51] = 183.592881882697;
            gray[52] = 185.382820432079;
            gray[53] = 187.154298395046;
            gray[54] = 188.890309351831;
            gray[55] = 190.648492901209;
            gray[56] = 192.352594382693;
            gray[57] = 194.055527932079;
            gray[58] = 195.694869691337;
            gray[59] = 197.346421697509;
            gray[60] = 198.953659567879;
            gray[61] = 200.497421543188;
            gray[62] = 202.043470648128;
            gray[63] = 203.506410401213;
            gray[64] = 205.078366728371;
            gray[65] = 206.502439074054;
            gray[66] = 207.960326111086;
            gray[67] = 209.345987870348;
            gray[68] = 210.716789660476;
            gray[69] = 212.168414629608;
            gray[70] = 213.477881975283;
            gray[71] = 214.799350092569;
            gray[72] = 216.092125339487;
            gray[73] = 217.453935709854;
            gray[74] = 218.555674537012;
            gray[75] = 219.908621604916;
            gray[76] = 221.408621604916;
            gray[77] = 222.287581172813;
            gray[78] = 223.467443333307;
            gray[79] = 224.597678641946;
            gray[80] = 225.677567191334;
            gray[81] = 226.751085123428;
            gray[82] = 227.77076570985;
            gray[83] = 228.838520154292;
            gray[84] = 229.835574104906;
            gray[85] = 230.759151604911;
            gray[86] = 231.671378487624;
            gray[87] = 232.645209876513;
            gray[88] = 233.430553919723;
            gray[89] = 234.259339197503;
            gray[90] = 235.192826820966;
            gray[91] = 235.948180339482;
            gray[92] = 236.749151635777;
            gray[93] = 237.419081604913;
            gray[94] = 238.172184753064;
            gray[95] = 238.791867530844;
            gray[96] = 239.459488487634;
            gray[97] = 240.081322901214;
            gray[98] = 240.737454969117;
            gray[99] = 241.330262314798;
            gray[100] = 241.887978950596;
            gray[101] = 242.445097870355;
            gray[102] = 242.951899320973;
            gray[103] = 243.438450987638;
            gray[104] = 243.957556172827;
            gray[105] = 244.418575493814;
            gray[106] = 244.824507623441;
            gray[107] = 245.293516851836;
            gray[108] = 245.75957370369;
            gray[109] = 246.070656358015;
            gray[110] = 246.49771345678;
            gray[111] = 246.870360092582;
            gray[112] = 247.170360092582;
            gray[113] = 247.505630277766;
            gray[114] = 247.852624783942;
            gray[115] = 248.2049069753;
            gray[116] = 248.447781265421;
            gray[117] = 248.785751049371;
            gray[118] = 249.057203456782;
            gray[119] = 249.333963888878;
            gray[120] = 249.550165030853;
            gray[121] = 249.812987160485;
            gray[122] = 249.996779567892;
            gray[123] = 250.290785864191;
            gray[124] = 250.508038024681;
            gray[125] = 250.720169938263;
            gray[126] = 250.859880061722;
            gray[127] = 251.098477962957;
            gray[128] = 251.266466851845;
            gray[129] = 251.453085216045;
            gray[130] = 251.648107376537;
            gray[131] = 251.82749172839;
            gray[132] = 251.932877129624;
            gray[133] = 252.083052191354;
            gray[134] = 252.236006018513;
            gray[135] = 252.370963796291;
            gray[136] = 252.494106327154;
            gray[137] = 252.601936759253;
            gray[138] = 252.707993271599;
            gray[139] = 252.851702191351;
            gray[140] = 252.94527401234;
            gray[141] = 253.063203271602;
            gray[142] = 253.137698456785;
            gray[143] = 253.227324166663;
            gray[144] = 253.318710524688;
            gray[145] = 253.416192222217;
            gray[146] = 253.501922654318;
            gray[147] = 253.588719506168;
            gray[148] = 253.657823487649;
            gray[149] = 253.719692376542;
            gray[150] = 253.782666944442;
            gray[151] = 253.856560709873;
            gray[152] = 253.903209537033;
            gray[153] = 253.961351450612;
            gray[154] = 254.033884814813;
            gray[155] = 254.080620216047;
            gray[156] = 254.121377129626;
            gray[157] = 254.17248141975;
            gray[158] = 254.20786898148;
            gray[159] = 254.257156820988;
            gray[160] = 254.294456975308;
            gray[161] = 254.34212552469;
            gray[162] = 254.38212552469;
            gray[163] = 254.408731388887;
            gray[164] = 254.431429074073;
            gray[165] = 254.470446543208;
            gray[166] = 254.502729598764;
            gray[167] = 254.535404660492;
            gray[168] = 254.5603125;
            gray[169] = 254.577502530863;
            gray[170] = 254.603023179012;
            gray[171] = 254.624034382714;
            gray[172] = 254.644510895061;
            gray[173] = 254.664510895061;
            gray[174] = 254.690712530865;
            gray[175] = 254.702566450616;
            gray[176] = 254.717322037036;
            gray[177] = 254.735003827159;
            gray[178] = 254.753764938271;
            gray[179] = 254.763686728395;
            gray[180] = 254.778108796294;
            gray[181] = 254.794384938271;
            gray[182] = 254.8036920679;
            gray[183] = 254.820527006173;
            gray[184] = 254.834644351851;
            gray[185] = 254.84701824074;
            gray[186] = 254.850060524691;
            gray[187] = 254.86367802469;
            gray[188] = 254.866043765432;
            gray[189] = 254.886052839505;
            gray[190] = 254.887237499999;
            gray[191] = 254.89126845679;
            gray[192] = 254.906473086419;
            gray[193] = 254.907714351852;
            gray[194] = 254.91614728395;
            gray[195] = 254.918374722221;
            gray[196] = 254.926159876543;
            gray[197] = 254.937555833334;
            gray[198] = 254.943707932099;
            gray[199] = 254.946672746914;
            gray[200] = 254.946087129629;
            gray[201] = 254.94750191358;
            gray[202] = 254.954697067901;
            gray[203] = 254.95982462963;
            gray[204] = 254.960204969135;
            gray[205] = 254.968172746913;
            gray[206] = 254.967210493827;
            gray[207] = 254.971220154321;
            gray[208] = 254.972564074074;
            gray[209] = 254.976282839506;
            gray[210] = 254.978052067901;
            gray[211] = 254.97861212963;
            gray[212] = 254.982160709876;
            gray[213] = 254.985306635802;
            gray[214] = 254.979370216049;
            gray[215] = 254.983408117284;
            gray[216] = 254.989879783951;
            gray[217] = 254.987366944444;
            gray[218] = 254.99006808642;
            gray[219] = 254.990836203704;
            gray[220] = 254.988598117284;
            gray[221] = 254.991593950618;
            gray[222] = 254.991824660494;
            gray[223] = 254.991818487654;
            gray[224] = 254.991879012346;
            gray[225] = 254.993955401235;
            gray[226] = 254.995471234568;
            gray[227] = 254.9977575;
            gray[228] = 254.996474753086;
            gray[229] = 254.997324104938;
            gray[230] = 254.997102283951;
            gray[231] = 254.997711358025;
            gray[232] = 254.997932839506;
            gray[233] = 254.998292746914;
            gray[234] = 254.997951296296;
            gray[235] = 254.999040246914;
            gray[236] = 254.998957191358;
            gray[237] = 254.998957191358;
            gray[238] = 254.997268395062;
            gray[239] = 254.998117407407;
            gray[240] = 254.999261728395;
            gray[241] = 254.999114074074;
            gray[242] = 254.999861574074;
            gray[243] = 254.998809537037;
            gray[244] = 254.998809537037;
            gray[245] = 254.999206358025;
            gray[246] = 254.999926172839;
            gray[247] = 255;
            gray[248] = 254.999907716049;
            gray[249] = 254.999806203704;
            gray[250] = 254.998809537037;
            gray[251] = 254.999732376543;
            gray[252] = 254.999593950617;
            gray[253] = 255;
            gray[254] = 254.999861574074;
            gray[255] = 254.999990771605;
            gray[256] = 254.99998154321;
            gray[257] = 254.99996308642;
            gray[258] = 254.999990771605;
            gray[259] = 255;
            gray[260] = 255;
            gray[261] = 255;
            gray[262] = 255;
            gray[263] = 254.999953858025;
            gray[264] = 255;
            gray[265] = 255;
            gray[266] = 255;
            gray[267] = 255;
            gray[268] = 255;
            gray[269] = 255;
            gray[270] = 255;
            gray[271] = 255;
            gray[272] = 255;
            gray[273] = 255;
            gray[274] = 255;
            gray[275] = 255;
            gray[276] = 255;
            gray[277] = 255;
            gray[278] = 255;
            gray[279] = 255;
            gray[280] = 255;
            gray[281] = 255;
            gray[282] = 255;
            gray[283] = 255;
            gray[284] = 255;
            gray[285] = 255;
            gray[286] = 255;
            gray[287] = 255;
            gray[288] = 255;
            gray[289] = 255;
            gray[290] = 255;
            gray[291] = 255;
            gray[292] = 255;
            gray[293] = 255;
            gray[294] = 255;
            gray[295] = 255;
            gray[296] = 255;
            gray[297] = 255;
            gray[298] = 255;
            gray[299] = 255;
            gray[300] = 255;
            gray[301] = 255;
            gray[302] = 255;
            gray[303] = 255;
            gray[304] = 255;
            gray[305] = 255;
            gray[306] = 255;
            gray[307] = 255;
            gray[308] = 255;
            gray[309] = 255;
            gray[310] = 255;
            gray[311] = 255;
            gray[312] = 255;
            gray[313] = 255;
            gray[314] = 255;
            gray[315] = 255;
            gray[316] = 255;
            gray[317] = 255;
            gray[318] = 255;
            gray[319] = 255;
            gray[320] = 255;
            gray[321] = 255;
            gray[322] = 255;
            gray[323] = 255;
            gray[324] = 255;
            gray[325] = 255;
            gray[326] = 255;
            gray[327] = 255;
            gray[328] = 255;
            gray[329] = 255;
            gray[330] = 255;
            gray[331] = 255;
            gray[332] = 255;
            gray[333] = 255;
            gray[334] = 255;
            gray[335] = 255;
            gray[336] = 255;
            gray[337] = 255;
            gray[338] = 255;
            gray[339] = 255;
            gray[340] = 255;
            gray[341] = 255;
            gray[342] = 255;
            gray[343] = 255;
            gray[344] = 255;
            gray[345] = 255;
            gray[346] = 255;
            gray[347] = 255;
            gray[348] = 255;
            gray[349] = 255;


            Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
            //g.DrawLines(Pens.Red, gray.ToArray());

            g.Clear(Color.White);

            g.DrawRectangle(Pens.Red, 0, 0, 700, 256);
            PointF[] curvePoints = new PointF[350];    //一維陣列內有 8 個Point

            int i;
            for (i = 0; i < 350; i++)
            {
                curvePoints[i].X = (float)i * 2;
                curvePoints[i].Y = 255 - (float)(gray[i]);
            }


            // Draw lines between original points to screen.
            g.DrawLines(Pens.Red, curvePoints);   //畫直線
            // Draw curve to screen.
            //gc.DrawCurve(redPen, curvePoints); //畫曲線





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

            //檢視圖片的像素
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

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


        private void button26_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //取得一層jpg檔

            string foldername = @"C:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony1";
            string[] filenames = Directory.GetFiles(foldername, "*.jpg");

            foreach (string filename in filenames)
            {
                richTextBox1.Text += "取得檔案 : " + filename + "\n";
            }
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
