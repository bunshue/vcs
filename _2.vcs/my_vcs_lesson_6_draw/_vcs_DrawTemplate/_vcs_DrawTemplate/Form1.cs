using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for LineCap
using System.Drawing.Imaging;   //for ImageFormat

using System.Runtime.InteropServices;   //for Marshal


namespace _vcs_DrawTemplate
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();

            button2.Enabled = false;
            button3.Enabled = false;
            button4.Enabled = false;
            button5.Enabled = false;
            button7.Enabled = false;
            button9.Enabled = false;

            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            p = new Pen(Color.Red, 3);
            sb = new SolidBrush(Color.Red);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            button2.Enabled = true;
            button3.Enabled = true;
            button4.Enabled = true;
            button5.Enabled = true;
            button7.Enabled = true;
            button9.Enabled = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //載入圖片至畫布
            string filename = string.Empty;
            //filename = "C:\\______test_files\\bear.jpg";
            filename = "C:\\______test_files\\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";
            bitmap1 = new Bitmap(filename);

            int width;
            int height;

            width = bitmap1.Width;
            height = bitmap1.Height;

            richTextBox1.Text += "畫布大小 : W = " + width.ToString() + " H = " + height.ToString() + "\n";

            //pictureBox1.Size = new Size(width, height);   //改變圖框大小
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.Image = bitmap1;

            g = Graphics.FromImage(bitmap1);

            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //畫東西
            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));
            g.DrawRectangle(new Pen(Color.Red, 5), new Rectangle(100, 100, 300, 300));

            int width = 200;
            int height = 200;
            Point[] points = new Point[3];
            points[0] = new Point(width / 2, height / 8);
            points[1] = new Point(width * 7 / 8, height * 7 / 8);
            points[2] = new Point(width * 1 / 8, height * 7 / 8);
            g.FillPolygon(sb, points);

            //畫箭頭
            Pen pen = new Pen(Color.FromArgb(255, 0, 0, 255), 8);
            pen.StartCap = LineCap.RoundAnchor;
            pen.EndCap = LineCap.ArrowAnchor;
            g.DrawLine(pen, 100, 100, 300, 300);

            //畫聯結線條
            GraphicsPath path = new GraphicsPath();
            Pen penJoin = new Pen(Color.FromArgb(255, 0, 0, 255), 20);

            path.StartFigure();
            path.AddLine(new Point(50, 200), new Point(100, 200));
            path.AddLine(new Point(100, 200), new Point(100, 250));

            penJoin.LineJoin = LineJoin.Bevel;
            g.DrawPath(penJoin, path);

            //繪製自訂虛線
            float[] dashValues = { 5, 2, 15, 4 };
            Pen greenPen = new Pen(Color.Green, 10);
            greenPen.DashPattern = dashValues;
            g.DrawLine(greenPen, new Point(50, 150), new Point(600, 150));
            
            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //清除畫布
            g.Clear(Color.White);

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //逐點繪圖
            int width = bitmap1.Width;
            int height = bitmap1.Height;
            int xx;
            int yy;
            Color pt;

            //讀取/修改每一的的RGB值
            for (yy = 0; yy < height / 2; yy += 1)
            {
                for (xx = 0; xx < width / 2; xx += 1)
                {
                    pt = bitmap1.GetPixel(xx, yy);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 255 - pt.R, 255 - pt.G, 255 - pt.B));
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    //bitmap1.SetPixel(xx, yy, Color.White);
                }
            }
            pictureBox1.Image = bitmap1;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Random rnd = new Random();
            int width;
            int height;
            int xx;
            int yy;

            int r;
            int g;
            int b;

            r = rnd.Next(256);
            g = rnd.Next(256);
            b = rnd.Next(256);

            width = 300;
            height = 300;
            bitmap1 = new Bitmap(width, height);

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    r = rnd.Next(256);
                    g = rnd.Next(256);
                    b = rnd.Next(256);

                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, r, g, b));
                }
            }

            pictureBox1.Image = bitmap1;

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //馬賽克   TBD
            int block_size = 30;

            int i;
            int xx;
            int yy;
            int r_total = 0;
            int g_total = 0;
            int b_total = 0;
            byte rrr;
            byte ggg;
            byte bbb;

            for (yy = 0; yy < bitmap1.Height / 5; yy++)
            {
                for (xx = 0; xx < bitmap1.Width / 5; xx += 5)
                {
                    r_total = 0;
                    g_total = 0;
                    b_total = 0;

                    for (i = 0; i < block_size; i++)
                    {

                        rrr = bitmap1.GetPixel(xx + i, yy).R;
                        ggg = bitmap1.GetPixel(xx + i, yy).G;
                        bbb = bitmap1.GetPixel(xx + i, yy).B;
                        r_total += rrr;
                        g_total += ggg;
                        b_total += bbb;
                    }

                    Color zz = Color.FromArgb(255, (byte)(r_total / block_size), (byte)(g_total / block_size), (byte)(b_total / block_size));
                    for (i = 0; i < block_size; i++)
                    {
                        bitmap1.SetPixel(xx + i, yy, zz);
                    }
                }
            }

            pictureBox1.Image = bitmap1;

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //產生驗證圖片

            //從已知幾個元素中任意選出幾個
            int num = 10;

            string vaildNumAnswer = "";

            Random rr = new Random();

            List<char> myList = new List<char>();   //用來存放篩選後的字

            /*  不均勻分配
            myList.Add('A');
            myList.Add('A');
            myList.Add('A');
            myList.Add('B');
            myList.Add('C');
            */

            //特定分配
            for (int i = 50; i <= 57; i++)
                //ASCII碼，找出數字
                myList.Add((char)i); //從2開始，排除了0，1，放入列表


            for (int i = 65; i <= 90; i++)
            {
                //ASCII碼，找出大寫英文
                if (i == 73) continue; //排除I
                if (i == 79) continue; //排除O
                myList.Add((char)i);
            }


            for (int i = 97; i <= 122; i++)
            {
                //參考ASCII碼，找出小寫英文
                if (i == 108) continue; //排除l
                if (i == 111) continue; //排除o
                myList.Add((char)i);
            }


            char[] texts = new char[myList.Count];
            texts = myList.ToArray();

            //亂數產生驗證答案
            vaildNumAnswer = "";
            for (int i = 1; i <= num; i++)
            {
                char c = texts[rr.Next(texts.Length)];
                vaildNumAnswer += c;
            }


            richTextBox1.Text += vaildNumAnswer + "\n";


            RenderImage(vaildNumAnswer);



        }

        //產生驗證圖片
        private void RenderImage(string vaildNumAnswer)
        {
            Random rr = new Random();

            int num = 6;
            int ww = 30 * 2 + num * 20;
            //寬度=(留邊)30*2 + 每個字*20
            int hh = 70;

            Bitmap vaildNumImage = new Bitmap(ww, hh);
            Graphics gg = Graphics.FromImage(vaildNumImage);

            //產生背景色
            Color cc = Color.FromArgb(rr.Next(256), rr.Next(256), rr.Next(256));
            Brush bb = new SolidBrush(cc);
            gg.FillRectangle(bb, 0, 0, ww, hh);

            //產生字色，斥掉背景色
            bb = new SolidBrush(Color.FromArgb(cc.R ^ 255, cc.G ^ 255, cc.B ^ 255));
            //產生字體
            Font ff = new Font("Arial Black", 18, FontStyle.Regular);
            //逐一畫每一個字

            for (int i = 0; i < vaildNumAnswer.Length; i++)
            {
                gg.DrawString(vaildNumAnswer.Substring(i, 1), ff, bb, i * 20 + 30, 20);
            }

            //加入雜點
            bb = new SolidBrush(Color.White);
            for (int i = 1; i <= 500; i++)
                gg.FillRectangle(bb, rr.Next(ww), rr.Next(hh), 2, 2);


            pictureBox1.Image = vaildNumImage;


        }


        private void button11_Click(object sender, EventArgs e)
        {
            Graphics g;
            g = pictureBox1.CreateGraphics();



            // Create a new bitmap.
            Bitmap bmp = new Bitmap("c:\\______test_files\\picture1.jpg");
            //Bitmap bmp = new Bitmap("c:\\______test_files\\pattern.jpg");


            bmp = RGB2Gray(bmp);

            //g.DrawImage(bmp, 0, 0);
            pictureBox1.Image = bmp;

        }


        /// 建立8位灰度影像
        /// </summary>
        /// <param name="width"></param>
        /// <param name="height"></param>
        /// <returns></returns>
        public static Bitmap CreateGrayscaleImage(int width, int height)
        {
            // create new image
            Bitmap bmp = new Bitmap(width, height, System.Drawing.Imaging.PixelFormat.Format8bppIndexed);
            // set palette to grayscale
            SetGrayscalePalette(bmp);
            // return new image
            return bmp;
        }

        ///<summary>
        /// Set pallete of the image to grayscale
        ///</summary>
        public static void SetGrayscalePalette(Bitmap srcImg)
        {
            // check pixel format
            if (srcImg.PixelFormat != System.Drawing.Imaging.PixelFormat.Format8bppIndexed)
                throw new ArgumentException();
            // get palette
            ColorPalette cp = srcImg.Palette;
            // init palette
            for (int i = 0; i < 256; i++)
            {
                cp.Entries[i] = System.Drawing.Color.FromArgb(i, i, i);
            }
            srcImg.Palette = cp;
        }

        /// <summary>
        /// 轉為灰度影象，位深度也改變
        /// </summary>
        /// <param name="srcBitmap"></param>
        /// <returns></returns>
        public static Bitmap RGB2Gray(Bitmap srcBitmap)
        {
            int wide = srcBitmap.Width;
            int height = srcBitmap.Height;
            Rectangle rect = new Rectangle(0, 0, wide, height);
            //將Bitmap鎖定到系統記憶體中,獲得BitmapData
            BitmapData srcBmData = srcBitmap.LockBits(rect, ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format24bppRgb);
            //建立Bitmap
            Bitmap dstBitmap = CreateGrayscaleImage(wide, height);//這個函式在後面有定義
            BitmapData dstBmData = dstBitmap.LockBits(rect, ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format8bppIndexed);
            //點陣圖中第一個畫素資料的地址。它也可以看成是點陣圖中的第一個掃描行
            System.IntPtr srcPtr = srcBmData.Scan0;
            System.IntPtr dstPtr = dstBmData.Scan0;
            //將Bitmap物件的資訊存放到byte陣列中
            int src_bytes = srcBmData.Stride * height;
            byte[] srcValues = new byte[src_bytes];
            int dst_bytes = dstBmData.Stride * height;
            byte[] dstValues = new byte[dst_bytes];
            //複製GRB資訊到byte陣列
            System.Runtime.InteropServices.Marshal.Copy(srcPtr, srcValues, 0, src_bytes);
            System.Runtime.InteropServices.Marshal.Copy(dstPtr, dstValues, 0, dst_bytes);
            //根據Y=0.299*R+0.114*G+0.587B,Y為亮度
            for (int i = 0; i < height; i++)
                for (int j = 0; j < wide; j++)
                {
                    //只處理每行中影象畫素資料,捨棄未用空間
                    //注意點陣圖結構中RGB按BGR的順序儲存
                    int k = 3 * j;
                    byte temp = (byte)(srcValues[i * srcBmData.Stride + k + 2] * .299 + srcValues[i * srcBmData.Stride + k + 1] * .587 + srcValues[i * srcBmData.Stride + k] * .114);
                    dstValues[i * dstBmData.Stride + j] = temp;
                }
            System.Runtime.InteropServices.Marshal.Copy(dstValues, 0, dstPtr, dst_bytes);
            //解鎖點陣圖
            srcBitmap.UnlockBits(srcBmData);
            dstBitmap.UnlockBits(dstBmData);
            return dstBitmap;
        }


        private void button12_Click(object sender, EventArgs e)
        {
            //二值化圖片
            Graphics g;
            g = pictureBox1.CreateGraphics();



            // Create a new bitmap.
            Bitmap bmp = new Bitmap("c:\\______test_files\\picture1.jpg");
            //Bitmap bmp = new Bitmap("c:\\______test_files\\pattern.jpg");


            bmp = OtsuThreshold(bmp);

            //g.DrawImage(bmp, 0, 0);
            pictureBox1.Image = bmp;

        }




        #region 二值化
        #region Otsu閾值法二值化模組
        /// <summary>   
        /// Otsu閾值   
        /// </summary>   
        /// <param name="b">點陣圖流</param>   
        /// <returns></returns>   
        public Bitmap OtsuThreshold(Bitmap bitmap)
        {

            // 影象灰度化   
            // b = Gray(b);   
            int width = bitmap.Width;
            int height = bitmap.Height;
            byte threshold = 0;
            int[] hist = new int[256];

            int AllPixelNumber = 0, PixelNumberSmall = 0, PixelNumberBig = 0;

            double MaxValue, AllSum = 0, SumSmall = 0, SumBig, ProbabilitySmall, ProbabilityBig, Probability;
            BitmapData bmpData = bitmap.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format32bppArgb);


            unsafe
            {
                byte* p = (byte*)bmpData.Scan0;
                int offset = bmpData.Stride - width * 4;
                for (int j = 0; j < height; j++)
                {
                    for (int i = 0; i < width; i++)
                    {
                        hist[p[0]]++;
                        p += 4;
                    }
                    p += offset;
                }
                bitmap.UnlockBits(bmpData);
            }
            //計算灰度為I的畫素出現的概率   
            for (int i = 0; i < 256; i++)
            {
                AllSum += i * hist[i];     //   質量矩   
                AllPixelNumber += hist[i];  //  質量       
            }
            MaxValue = -1.0;
            for (int i = 0; i < 256; i++)
            {
                PixelNumberSmall += hist[i];
                PixelNumberBig = AllPixelNumber - PixelNumberSmall;
                if (PixelNumberBig == 0)
                {
                    break;
                }

                SumSmall += i * hist[i];
                SumBig = AllSum - SumSmall;
                ProbabilitySmall = SumSmall / PixelNumberSmall;
                ProbabilityBig = SumBig / PixelNumberBig;
                Probability = PixelNumberSmall * ProbabilitySmall * ProbabilitySmall + PixelNumberBig * ProbabilityBig * ProbabilityBig;
                if (Probability > MaxValue)
                {
                    MaxValue = Probability;
                    threshold = (byte)i;
                }
            }
            this.Threshoding(bitmap, threshold);
            bitmap = twoBit(bitmap);
            return bitmap;

        }
        #endregion

        #region      固定閾值法二值化模組
        public Bitmap Threshoding(Bitmap b, byte threshold)
        {
            int width = b.Width;
            int height = b.Height;
            BitmapData data = b.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format32bppArgb);
            unsafe
            {
                byte* p = (byte*)data.Scan0;
                int offset = data.Stride - width * 4;
                byte R, G, B, gray;
                for (int y = 0; y < height; y++)
                {
                    for (int x = 0; x < width; x++)
                    {
                        R = p[2];
                        G = p[1];
                        B = p[0];
                        gray = (byte)((R * 19595 + G * 38469 + B * 7472) >> 16);
                        if (gray >= threshold)
                        {
                            p[0] = p[1] = p[2] = 255;
                        }
                        else
                        {
                            p[0] = p[1] = p[2] = 0;
                        }
                        p += 4;
                    }
                    p += offset;
                }
                b.UnlockBits(data);
                return b;

            }

        }
        #endregion


        #region 建立1點陣圖像

        /// <summary>
        /// 建立1點陣圖像
        /// </summary>
        /// <param name="srcBitmap"></param>
        /// <returns></returns>
        public Bitmap twoBit(Bitmap srcBitmap)
        {
            int midrgb = System.Drawing.Color.FromArgb(128, 128, 128).ToArgb();
            int stride;//簡單公式((width/8)+3)&(~3)
            stride = (srcBitmap.Width % 8) == 0 ? (srcBitmap.Width / 8) : (srcBitmap.Width / 8) + 1;
            stride = (stride % 4) == 0 ? stride : ((stride / 4) + 1) * 4;
            int k = srcBitmap.Height * stride;
            byte[] buf = new byte[k];
            int x = 0, ab = 0;
            for (int j = 0; j < srcBitmap.Height; j++)
            {
                k = j * stride;//因影象寬度不同、有的可能有填充位元組需要跳越
                x = 0;
                ab = 0;
                for (int i = 0; i < srcBitmap.Width; i++)
                {
                    //從灰度變單色（下法如果直接從彩色變單色效果不太好，不過反相也可以在這裡控制）
                    if ((srcBitmap.GetPixel(i, j)).ToArgb() > midrgb)
                    {
                        ab = ab * 2 + 1;
                    }
                    else
                    {
                        ab = ab * 2;
                    }
                    x++;
                    if (x == 8)
                    {
                        buf[k++] = (byte)ab;//每位元組賦值一次，陣列buf中儲存的是十進位制。
                        ab = 0;
                        x = 0;
                    }
                }
                if (x > 0)
                {
                    //迴圈實現：剩餘有效資料不滿1位元組的情況下須把它們移往位元組的高位部分
                    for (int t = x; t < 8; t++) ab = ab * 2;
                    buf[k++] = (byte)ab;
                }
            }
            int width = srcBitmap.Width;
            int height = srcBitmap.Height;
            Bitmap dstBitmap = new Bitmap(width, height, System.Drawing.Imaging.PixelFormat.Format1bppIndexed);
            BitmapData dt = dstBitmap.LockBits(new Rectangle(0, 0, dstBitmap.Width, dstBitmap.Height), ImageLockMode.ReadWrite, dstBitmap.PixelFormat);
            Marshal.Copy(buf, 0, dt.Scan0, buf.Length);
            dstBitmap.UnlockBits(dt);
            return dstBitmap;
        }

        #endregion


        #endregion





    }
}
