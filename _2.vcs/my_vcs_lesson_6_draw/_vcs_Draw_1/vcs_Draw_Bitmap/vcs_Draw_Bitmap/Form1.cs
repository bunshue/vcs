using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for GraphicsPath

namespace vcs_Draw_Bitmap
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        Font f;

        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            p = new Pen(Color.Red, 3);
            bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            pictureBox1.Image = bitmap1;
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
            richTextBox1.Location = new Point(x_st + dx * 7 + 10, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void open_new_file()
        {
            richTextBox1.Text += "開啟一個 640 X 480 的空畫布\n";
            //指定畫布大小
            pictureBox1.Width = 640;
            pictureBox1.Height = 480;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
            return;
        }

        private void button0_Click(object sender, EventArgs e)
        {

            //Bitmap 經過 Rotate後, 會改變其寬高
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);
            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + ", H = " + bitmap1.Height.ToString() + "\n";

            bitmap1.RotateFlip(RotateFlipType.Rotate90FlipNone);
            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + ", H = " + bitmap1.Height.ToString() + "\n";

            pictureBox1.Image = bitmap1;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將Bitmap的資料放到剪貼簿裏\n";


            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            //複製到剪貼簿
            Clipboard.SetImage(bitmap1);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (timer1.Enabled == false)
            {
                timer1.Enabled = true;
            }
            else
            {
                timer1.Enabled = false;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //一個大bitmap貼上多個小bitmap

            //小圖
            string filename = @"C:\______test_files\__pic\_angry_bird\AB_red.jpg";

            //大bitmap
            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            //小bitmap
            Bitmap bitmap2 = new Bitmap(filename);

            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            for (int i = 0; i < 500; i += 120)
            {
                g.DrawImage(bitmap2, i, i, bitmap2.Width, bitmap2.Height);
            }

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //圖片轉向
            richTextBox1.Text += "圖片轉向\n";

            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            pictureBox1.Image = bitmap1;

            Bitmap bitmap2 = (Bitmap)Bitmap.FromFile(filename);
            bitmap2.RotateFlip(RotateFlipType.Rotate90FlipX);

            pictureBox1.Image = bitmap2;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //圖片旋轉, 可連續旋轉
            richTextBox1.Text += "圖片旋轉, 可連續旋轉\n";
            Image image = pictureBox1.Image;
            image.RotateFlip(RotateFlipType.Rotate90FlipXY);
            pictureBox1.Image = image;


        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "clone語法\t";
            richTextBox1.Text += "從bitmap1抓取一部分貼到bitmap2上\n";

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;


            RectangleF rect = new RectangleF(100, 100, 150, 150);

            Bitmap cloneBitmap = bitmap1.Clone(rect, PixelFormat.DontCare);


            Bitmap bitmap2 = new Bitmap(pictureBox1.Width, pictureBox1.Height);


            //pictureBox1.Image = bitmap1;

            //pictureBox1.Image = bm.Clone(rect, PixelFormat.Format32bppArgb);

            Graphics g = Graphics.FromImage(bitmap2);
            g.Clear(Color.White);

            for (int i = 0; i < 500; i += 120)
            {
                g.DrawImage(cloneBitmap, i, i, cloneBitmap.Width, cloneBitmap.Height);
                //g.DrawImage(cloneBitmap, 50, 50);
            }

            pictureBox1.Image = bitmap2;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //Bitmap存圖


            //Bitmap直接存圖
            bitmap1.Save("filename.bmp", ImageFormat.Bmp);



            /*            
            轉換圖片格式
            Bitmap bm = new Bitmap(舊檔名);
            bm.Save(新檔名, 新格式);	//格式為 ImageFormat.Bmp...
            */
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //創建32位元深度之Bitmap
            Bitmap bitmap1 = new Bitmap(100, 100, System.Drawing.Imaging.PixelFormat.Format32bppArgb);
            bitmap1.Save("aaaa.bmp", ImageFormat.Bmp);

            //創建24位元深度之Bitmap
            Bitmap bitmap2 = new Bitmap(100, 100, System.Drawing.Imaging.PixelFormat.Format24bppRgb);
            bitmap2.Save("bbbb.bmp", ImageFormat.Bmp);

            //沒寫, 預設為32位元深度之Bitmap
            Bitmap bitmap3 = new Bitmap(100, 100);
            bitmap3.Save("cccc.bmp", ImageFormat.Bmp);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //改變Bitmap大小
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);

            int W1 = image.Width;
            int H1 = image.Height;
            Bitmap bitmap1 = new Bitmap(image, W1 / 2, H1 / 2);

            int W2 = bitmap1.Width;
            int H2 = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(bitmap1, W2 * 5 / 2, H2 * 5 / 2);
            pictureBox1.Image = bitmap2;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //設置圖像的分辨率
            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            bitmap1.SetResolution(300f, 300f);
            g.DrawImage(bitmap1, 0, 0);
            bitmap1.SetResolution(1200f, 1200f);
            g.DrawImage(bitmap1, 180, 0);

        }

        private void button13_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將Bitmap的資料放到剪貼簿裏\n";

            Rectangle select_rectangle = new Rectangle(new Point(100, 100), new Size(150, 150));    //用來保存截圖的矩形

            // Copy the selection to the clipboard.
            CopyToClipboard(select_rectangle);
        }

        // Copy the selected area to the clipboard.
        private void CopyToClipboard(Rectangle src_rect)
        {
            // Make a bitmap for the selected area's image.
            Bitmap bm = new Bitmap(src_rect.Width, src_rect.Height);

            // Copy the selected area into the bitmap.
            using (Graphics g = Graphics.FromImage(bm))
            {
                Rectangle dest_rect = new Rectangle(0, 0, src_rect.Width, src_rect.Height);
                g.DrawImage(bitmap1, dest_rect, src_rect, GraphicsUnit.Pixel);
            }

            // Copy the selection image to the clipboard.
            Clipboard.SetImage(bm);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //縮小一半並存檔
            if (pictureBox1.Image == null)
                return;

            //顯示圖片
            richTextBox1.Text += "圖片大小：\tW=" + pictureBox1.Image.Width.ToString() + "\t";
            richTextBox1.Text += "H=" + pictureBox1.Image.Height.ToString() + "\n";

            #region 影像縮放(縮小一半)
            richTextBox1.Text += "縮小一半\n";
            //建立新的影像，長寬為原始影像的1/2
            Image zoomImage = new Bitmap(pictureBox1.Image.Width / 2, pictureBox1.Image.Height / 2) as Image;
            //準備繪製新的影像
            Graphics g = Graphics.FromImage(zoomImage);
            //於座標(0,0)開始繪製來源影像，長寬設置為來源影像的1/2
            g.DrawImage(pictureBox1.Image, 0, 0, pictureBox1.Image.Width / 2, pictureBox1.Image.Height / 2);
            g.Dispose();
            //儲存新的影像
            string filename = Application.StartupPath + "\\zoom_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            zoomImage.Save(filename, ImageFormat.Jpeg);
            richTextBox1.Text += "縮小一半，存檔完成，檔名：" + filename + "\n";
            #endregion
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //放大一倍並存檔
            if (pictureBox1.Image == null)
                return;

            //顯示圖片
            richTextBox1.Text += "圖片大小：\tW=" + pictureBox1.Image.Width.ToString() + "\t";
            richTextBox1.Text += "H=" + pictureBox1.Image.Height.ToString() + "\n";

            #region 影像放大(放大一倍)
            richTextBox1.Text += "放大一倍\n";
            //建立新的影像，長寬為原始影像的2倍
            Image zoomImageb = new Bitmap(pictureBox1.Image.Width * 2, pictureBox1.Image.Height * 2) as Image;
            //準備繪製新的影像
            Graphics g = Graphics.FromImage(zoomImageb);
            //於座標(0,0)開始繪製來源影像，長寬設置為來源影像的2倍
            g.DrawImage(pictureBox1.Image, 0, 0, pictureBox1.Image.Width * 2, pictureBox1.Image.Height * 2);
            g.Dispose();
            //儲存新的影像
            string filename = Application.StartupPath + "\\big_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            zoomImageb.Save(filename, ImageFormat.Jpeg);
            richTextBox1.Text += "放大一倍，存檔完成，檔名：" + filename + "\n";
            #endregion
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //設置圖像分辨率

            //測不太出來

            //設置圖像分辨率

            filename = @"C:\______test_files\elephant.jpg";
            Bitmap bmp = new Bitmap(filename);

            int W = bmp.Width;
            int H = bmp.Height;

            Bitmap bitmap1 = new Bitmap(W * 2, H);

            Graphics g = Graphics.FromImage(bitmap1);
            g.FillRectangle(Brushes.Pink, this.ClientRectangle);

            bmp.Save("圖片0.bmp", ImageFormat.Bmp);

            bmp.SetResolution(3f, 3f);
            bmp.Save("圖片30.bmp", ImageFormat.Bmp);

            g.DrawImage(bmp, 0, 0, bmp.Width, bmp.Height);


            bmp.SetResolution(1200f, 1200f);
            bmp.Save("圖片120.bmp", ImageFormat.Bmp);

            g.DrawImage(bmp, 200, 0, bmp.Width, bmp.Height);
            pictureBox1.Image = bitmap1;

        }

        private void button17_Click(object sender, EventArgs e)
        {
            //複製部分圖片
            // Create a Bitmap object from a file.
            Bitmap myBitmap = new Bitmap(@"C:/______test_files/bear.jpg");

            // Clone a portion of the Bitmap object.
            RectangleF cloneRect = new RectangleF(530, 30, 200, 200);
            PixelFormat format = myBitmap.PixelFormat;
            Bitmap cloneBitmap = myBitmap.Clone(cloneRect, format);

            // Draw the cloned portion of the Bitmap object.
            Graphics g = pictureBox1.CreateGraphics();
            g.DrawImage(cloneBitmap, 0, 0);
        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        public static Bitmap returnAlpha(Bitmap bmp, int alpha)
        {
            Color col;
            Bitmap bmp2 = new Bitmap(bmp);
            for (int i = 0; i < bmp.Width; i++)
            {
                for (int j = 0; j < bmp.Height; j++)
                {
                    col = bmp.GetPixel(i, j);
                    if ((col.A - alpha) >= 0)
                    {
                        bmp2.SetPixel(i, j, Color.FromArgb(Math.Abs(col.A - alpha), col.R, col.G, col.B));
                        //bmp2.SetPixel(i, j, Color.FromArgb(10, col.R, col.G, col.B));
                    }
                }
            }
            return bmp2;
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //改變圖片透明度
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap80 = returnAlpha(bitmap1, 80);
            Bitmap bitmap160 = returnAlpha(bitmap1, 160);
            Bitmap bitmap220 = returnAlpha(bitmap1, 220);

            bitmap80.Save(@"picture_80.bmp", ImageFormat.Bmp);
            bitmap160.Save(@"picture_160.bmp", ImageFormat.Bmp);
            bitmap220.Save(@"picture_220.bmp", ImageFormat.Bmp);

            Bitmap bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bmp);
            //g.Clear(Color.Pink);

            g.DrawImage(bitmap80, 0, 0);
            g.DrawImage(bitmap160, 305, 0);
            g.DrawImage(bitmap220, 305 * 2, 0);

            pictureBox1.Image = bmp;

            //pictureBox1.Image = bitmap160;
            //pictureBox1.Image = bitmap220;

            richTextBox1.Text += "OK\n";


        }



        double ratio = 0.5f;
        private void button21_Click(object sender, EventArgs e)
        {
            //改變Bitmap大小

            Bitmap bitmap1;
            Bitmap bitmap2;

            bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            bitmap2 = ImageResize.Resize(bitmap1, ratio);

            pictureBox1.Image = bitmap2;

            ratio += 0.2f;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //調整影像大小 1
            //使用 C# 中的 Bitmap 類調整影象大小
            string filename = @"C:\______test_files\picture1.jpg";
            Image image1 = Image.FromFile(filename);
            Bitmap bitmap1 = new Bitmap(image1);
            //Image image2 = resizeImage(bitmap1, new Size(image1.Width / 2, image1.Height / 2));
            Image image2 = resizeImage(bitmap1, new Size(100, 300));

            pictureBox1.Image = image2;
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //調整影像大小 2
            //使用 C# 中的 Graphics.DrawImage() 函式調整影象大小
            string filename = @"C:\______test_files\picture1.jpg";
            Image image1 = Image.FromFile(filename);
            Bitmap bitmap1 = new Bitmap(image1);
            Image image2 = resizeImage(bitmap1, new Size(200, 200));

            pictureBox1.Image = image2;

        }


        public static Image resizeImage(Image imgToResize, Size size)
        {
            return (Image)(new Bitmap(imgToResize, size));
        }

        public static Image resizeImage2(Image image, int width, int height)
        {
            var destinationRect = new Rectangle(0, 0, width, height);
            var destinationImage = new Bitmap(width, height);

            destinationImage.SetResolution(image.HorizontalResolution, image.VerticalResolution);

            using (var graphics = Graphics.FromImage(destinationImage))
            {
                graphics.CompositingMode = CompositingMode.SourceCopy;
                graphics.CompositingQuality = CompositingQuality.HighQuality;

                using (var wrapMode = new ImageAttributes())
                {
                    wrapMode.SetWrapMode(WrapMode.TileFlipXY);
                    graphics.DrawImage(image, destinationRect, 0, 0, image.Width, image.Height, GraphicsUnit.Pixel, wrapMode);
                }
            }

            return (Image)destinationImage;
            /*
            destinationImage.SetResolution() 函式保持影象的 dpi，而不考慮其實際大小
            graphics.CompositingMode = CompositingMode.SourceCopy 屬性指定在渲染顏色時它將覆蓋背景顏色
            graphics.CompositingQuality = CompositingQuality.HighQuality 屬性指定我們只希望渲染高質量的影象
            wrapMode.SetWrapMode(WrapMode.TileFlipXY) 函式可以防止在影象邊界周圍出現鬼影
            graphics.DrawImage() 繪製具有指定尺寸的實際影象。
            */
        }


        private void button24_Click(object sender, EventArgs e)
        {
            //MakeTransparent 使用 去背效果1
            string filename = @"C:\______test_files\__pic\banner_ims.png";
            Bitmap bitmap2 = (Bitmap)Image.FromFile(filename);	//給不透明使用
            Bitmap bitmap3 = (Bitmap)Image.FromFile(filename);	//給透明使用

            ////使用默認的透明顏色進行透明設定, 可重複設定
            bitmap3.MakeTransparent(Color.Pink);
            bitmap3.MakeTransparent(Color.Blue);

            Graphics g = Graphics.FromImage(bitmap1);

            //原圖貼上
            //               貼上位置x      貼上位置y      貼上大小W            貼上大小H
            g.DrawImage(bitmap2, 0, 400 - 160, 305, 80);
            g.DrawImage(bitmap3, 0, 400 - 80, 305, 80);

            pictureBox1.Image = bitmap1;
            richTextBox1.Text += "將粉紅色和藍色, 設定為透明色\n";
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //MakeTransparent 使用 去背效果2

            open_new_file();

            pictureBox1.BackColor = Color.Pink;

            string filename = @"C:\______test_files\__pic\_angry_bird\thumb-1920-283652.jpg";

            GraphicsUnit units = GraphicsUnit.Pixel;

            Bitmap bmp1 = new Bitmap(filename);
            Bitmap bmp2 = new Bitmap(filename);

            //bmp2 做 去背景
            bmp2.MakeTransparent(Color.White);  //MakeTransparent 用法, bmp2 去背景, 可以多重去背, 連續寫即可
            //bmp2.MakeTransparent(Color.Black);  //MakeTransparent 用法, bmp2 去背景, 可以多重去背, 連續寫即可

            Rectangle destRect1 = new Rectangle(30, 30, bmp1.Width / 5, bmp1.Height / 5);
            Rectangle destRect2 = new Rectangle(30, 200, bmp2.Width / 5, bmp2.Height / 5);

            g.DrawRectangle(new Pen(Color.Yellow, 10), 100, 100, 300, 300);


            SolidBrush sb = new SolidBrush(Color.Purple);
            Font f = new Font("標楷體", 20);

            g.DrawImage(bmp1, destRect1, 0, 0, bmp1.Width, bmp1.Height, units);
            g.DrawString("沒去背", f, sb, new PointF(destRect1.X + bmp1.Width / 5, destRect1.Y + 50));


            g.DrawImage(bmp2, destRect2, 0, 0, bmp2.Width, bmp2.Height, units);
            g.DrawString("有去背", f, sb, new PointF(destRect2.X + bmp2.Width / 5, destRect2.Y + 50));


        }

        private void button26_Click(object sender, EventArgs e)
        {
            //MakeTransparent 使用 去背效果3

            Bitmap bitmap1 = new Bitmap(filename);
            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + ", H = " + bitmap1.Height.ToString() + "\n";

            int x_st = 50;
            int y_st = 50;
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            pictureBox1.Size = new Size(W * 2 + 150, H + 100);
            pictureBox1.BackColor = Color.Pink;

            Application.DoEvents();

            GraphicsUnit units = GraphicsUnit.Pixel;

            // Create parallelogram for drawing image.
            Point ulCorner = new Point(x_st + 0, y_st);
            Point urCorner = new Point(x_st + W, y_st);
            Point llCorner = new Point(x_st + 0, y_st + H);
            Point[] destPara = { ulCorner, urCorner, llCorner };

            // Create rectangle for source image.
            Rectangle srcRect = new Rectangle(0, 0, W, H);

            Graphics g = pictureBox1.CreateGraphics();

            g.DrawImage((Image)bitmap1, destPara, srcRect, units);

            Application.DoEvents();

            bitmap1.MakeTransparent(Color.White);
            g.DrawImage((Image)bitmap1, new Point(x_st + W + 10, y_st));

            g.DrawString("MakeTransparent 用法, 指名將白色變成透明", new Font("標楷體", 20), new SolidBrush(Color.Navy), 10, 10);


        }

        private void button27_Click(object sender, EventArgs e)
        {
            //MakeTransparent 使用 去背效果4

            open_new_file();

            int dy = 150;

            //MakeTransparent 功能

            string filename = @"C:\______test_files\__pic\lion.bmp";

            richTextBox1.Text += "無 MakeTransparent\n";
            Bitmap bmp1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            g.DrawImage(bmp1, 0, 0, bmp1.Width, bmp1.Height);



            richTextBox1.Text += "有 MakeTransparent\n";
            Bitmap bmp2 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            //bmp2.MakeTransparent();    //沒寫就是預設的     程式碼會讓系統預設透明色彩透明
            bmp2.MakeTransparent(Color.White);//將圖片白色部分透明化, 將此 Bitmap 的指定色彩變為透明。

            g.DrawImage(bmp2, 0, dy, bmp2.Width, bmp2.Height);


            richTextBox1.Text += "有 MakeTransparent 指名某點顏色變透明\n";
            Bitmap bmp3 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            Color backColor = bmp3.GetPixel(20, 80);   //選取圖片邊緣的一個點的顏色當成背景色
            bmp3.MakeTransparent(backColor); //將此背景色設定為透明
            g.DrawImage(bmp3, 0, dy * 2, bmp3.Width, bmp3.Height);

            g.DrawString("無 MakeTransparent", new Font("標楷體", 20), new SolidBrush(Color.Navy), 0, bmp1.Height - 30);
            g.DrawString("有 MakeTransparent", new Font("標楷體", 20), new SolidBrush(Color.Navy), 0, dy + bmp2.Height - 30);
            g.DrawString("有 MakeTransparent 指名某點顏色變透明", new Font("標楷體", 20), new SolidBrush(Color.Navy), 0, dy * 2 + bmp3.Height - 30);

            pictureBox1.Image = bitmap1;

        }

        private void button28_Click(object sender, EventArgs e)
        {
            //MakeTransparent 使用 去背效果5

            open_new_file();

            string filename = @"C:\______test_files\__pic\banner_ims.png";
            Bitmap bmp0 = (Bitmap)Image.FromFile(filename);
            Bitmap bmp1 = (Bitmap)bmp0.Clone();

            bmp1.MakeTransparent(Color.Pink);     //使用默認的透明顏色進行透明設置
            bmp1.MakeTransparent(Color.Blue);    //使用默認的透明顏色進行透明設置

            g.DrawImage(bmp0, 0, 0);
            g.DrawImage(bmp1, 0, 210);

            g.DrawString("去除粉紅色與藍色", new Font("標楷體", 30), new SolidBrush(Color.Navy), 200, pictureBox1.Height - 60);
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //MakeTransparent 使用 去背效果6

            open_new_file();
            g.Clear(Color.Pink);

            string filename = @"C:\______test_files\__pic\_logo\cloud.png";
            Bitmap bmp0 = (Bitmap)Image.FromFile(filename);
            Bitmap bmp1 = (Bitmap)bmp0.Clone();

            //bmp1.MakeTransparent(Color.Pink);     //使用默認的透明顏色進行透明設置
            //bmp1.MakeTransparent(Color.Blue);    //使用默認的透明顏色進行透明設置

            g.DrawImage(bmp0, 0, 0, bmp0.Width, bmp0.Height);
            g.DrawImage(bmp1, 0, 210, bmp1.Width, bmp1.Height);


            filename = @"C:\______test_files\__pic\_logo\cloud.bmp";
            bmp0 = (Bitmap)Image.FromFile(filename);
            bmp1 = (Bitmap)bmp0.Clone();

            bmp1.MakeTransparent(Color.Black);     //使用默認的透明顏色進行透明設置

            g.DrawImage(bmp0, 300, 0, bmp0.Width, bmp0.Height);
            g.DrawImage(bmp1, 300, 210, bmp1.Width, bmp1.Height);

            g.DrawString("左: PNG已將外部設為透明  右: BMP的外部是黑色的", new Font("標楷體", 18), new SolidBrush(Color.Navy), 10, pictureBox1.Height - 60);
        }

        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            //讀取圖檔, 多一層Image結構
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);
            //pictureBox1.Image = image;

            this.Text = cnt.ToString();
            switch (cnt)
            {
                case 0: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate180FlipNone); break;
                case 1: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate180FlipX); break;
                case 2: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate180FlipXY); break;
                case 3: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate180FlipY); break;
                case 4: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate270FlipNone); break;
                case 5: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate270FlipX); break;
                case 6: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate270FlipXY); break;
                case 7: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate270FlipY); break;
                case 8: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate90FlipNone); break;
                case 9: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate90FlipX); break;
                case 10: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate90FlipXY); break;
                case 11: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.Rotate90FlipY); break;
                case 12: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.RotateNoneFlipNone); break;
                case 13: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.RotateNoneFlipX); break;
                case 14: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.RotateNoneFlipXY); break;
                case 15: pictureBox1.Image = ModifiedBitmap(image, RotateFlipType.RotateNoneFlipY); break;
                default: break;
            }
            cnt++;
            if (cnt > 15)
                cnt = 0;

        }


        // Copy the bitmap, rotate it, and return the result.
        private Bitmap ModifiedBitmap(Image image, RotateFlipType rotate_flip_type)
        {
            // Copy the Bitmap.
            Bitmap bitmap1 = new Bitmap(image);

            // Rotate and flip.
            bitmap1.RotateFlip(rotate_flip_type);

            // Return the result.
            return bitmap1;
        }
    }

    public class ImageResize
    {
        public static Bitmap Resize(Bitmap bitmap1, Double ratio)
        {
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int w = Convert.ToInt32(W * ratio);
            int h = Convert.ToInt32(H * ratio);

            return Process(bitmap1, W, H, w, h);
        }

        private static Bitmap Process(Bitmap bitmap1, int oriwidth, int oriheight, int width, int height)
        {
            Bitmap resizedbitmap = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(resizedbitmap);
            g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            g.Clear(Color.Transparent);
            g.DrawImage(bitmap1, new Rectangle(0, 0, width, height), new Rectangle(0, 0, oriwidth, oriheight), GraphicsUnit.Pixel);
            return resizedbitmap;
        }
    }
}
