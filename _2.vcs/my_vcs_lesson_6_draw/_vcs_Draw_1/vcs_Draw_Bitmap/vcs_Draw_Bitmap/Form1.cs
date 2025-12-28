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
        Bitmap bitmap1;

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

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

            pictureBox1.Size = new Size(640, 720);
            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            lb_rotate.Location = new Point(x_st + dx * 6 + 40, y_st + dy * 0);
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.Size = new Size(300, 300);
            pictureBox2.Location = new Point(x_st + dx * 6 + 40, y_st + dy * 0 + 30);

            richTextBox1.Size = new Size(300, 382);
            richTextBox1.Location = new Point(x_st + dx * 6 + 40, y_st + dy * 4 + 60);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1640, 790);
            this.Text = "vcs_Draw_Bitmap";
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
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將Bitmap的資料放到剪貼簿裏\n";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            //複製到剪貼簿
            Clipboard.SetImage(bitmap1);
        }

        private void button2_Click(object sender, EventArgs e)
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

        private void button3_Click(object sender, EventArgs e)
        {
            //複製部分圖片

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            richTextBox1.Text += "clone語法\t";
            richTextBox1.Text += "從bitmap1抓取一部分貼到bitmap2上\n";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = new Bitmap(filename);//same
            PixelFormat format = bitmap1.PixelFormat;
            pictureBox1.Image = bitmap1;

            int x_st = 100;
            int y_st = 100;
            int w = 150;
            int h = 150;
            RectangleF rect = new RectangleF(x_st, y_st, w, h);

            //Bitmap cloneBitmap = bitmap1.Clone(rect, PixelFormat.DontCare);//PixelFormat.Format32bppArgb
            Bitmap cloneBitmap = bitmap1.Clone(rect, format);//PixelFormat.Format32bppArgb

            Bitmap bitmap2 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap2);
            g.Clear(Color.Pink);

            g.DrawImage(cloneBitmap, 50, 50, w, h);
            g.DrawImage(cloneBitmap, 200, 200, w, h);
            g.DrawImage(cloneBitmap, 350, 350, w, h);

            pictureBox1.Image = bitmap2;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //小圖貼到大圖上, 一個大bitmap貼上多個小bitmap

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            Bitmap bitmap1 = new Bitmap(W, H);//大bitmap

            //小圖
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\AB_red.jpg";
            Bitmap bitmap2 = new Bitmap(filename);//小bitmap
            int w = bitmap2.Width;
            int h = bitmap2.Height;

            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Pink);

            g.DrawImage(bitmap2, 0, 0, w, h);
            g.DrawImage(bitmap2, 150, 0, w, h);

            Bitmap bmp = (Bitmap)bitmap2.Clone();
            g.DrawImage(bmp, 150, 150, w, h);

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //改變Bitmap大小1

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);

            int W1 = image.Width;
            int H1 = image.Height;
            Bitmap bitmap1 = new Bitmap(image, W1 / 2, H1 / 2);

            int W2 = bitmap1.Width;
            int H2 = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(bitmap1, W2 * 5 / 2, H2 * 5 / 2);
            pictureBox1.Image = bitmap2;

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


        }

        double ratio = 0.5f;
        private void button6_Click(object sender, EventArgs e)
        {
            //改變Bitmap大小2

            Bitmap bitmap1;
            Bitmap bitmap2;

            bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            bitmap2 = ImageResize.Resize(bitmap1, ratio);

            pictureBox1.Image = bitmap2;

            ratio += 0.2f;
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //Bitmap存圖

            string filename = "\\tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            bitmap1.Save(filename, ImageFormat.Bmp);
            //bitmap1.Save(filename, ImageFormat.Jpeg);
            /*            
            轉換圖片格式
            Bitmap bm = new Bitmap(舊檔名);
            bm.Save(新檔名, 新格式);	//格式為 ImageFormat.Bmp...
            */
            richTextBox1.Text += "存檔完成, 檔名：" + filename + "\n";
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
            bitmap1.Save("tmp_depth_32.bmp", ImageFormat.Bmp);

            //創建24位元深度之Bitmap
            Bitmap bitmap2 = new Bitmap(100, 100, System.Drawing.Imaging.PixelFormat.Format24bppRgb);
            bitmap2.Save("tmp_depth_24.bmp", ImageFormat.Bmp);

            //沒寫, 預設為32位元深度之Bitmap
            Bitmap bitmap3 = new Bitmap(100, 100);
            bitmap3.Save("tmp_depth_default.bmp", ImageFormat.Bmp);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //設定bmp檔之位元深度
            //讀取圖檔, 先放在Bitmap裏
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            string filename_default = "picture1_default.bmp";
            string filename_32 = "picture1_32.bmp";
            string filename_24 = "picture1_24.bmp";

            richTextBox1.Text += "設定bmp檔之位元深度 為 預設, 即 24 位元\n";
            bitmap1.Save(filename_default, ImageFormat.Bmp);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //設置圖像的分辨率
            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            bitmap1.SetResolution(300f, 300f);
            g.DrawImage(bitmap1, 0, 0);
            bitmap1.SetResolution(1200f, 1200f);
            g.DrawImage(bitmap1, 180, 0);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //設置圖像分辨率

            //測不太出來

            //設置圖像分辨率

            filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            Bitmap bmp = new Bitmap(filename);

            int W = bmp.Width;
            int H = bmp.Height;

            bitmap1 = new Bitmap(W * 2, H);

            g = Graphics.FromImage(bitmap1);
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

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null)
            {
                return;
            }

            richTextBox1.Text += "圖片大小：\tW=" + pictureBox1.Image.Width.ToString() + "\t";
            richTextBox1.Text += "H=" + pictureBox1.Image.Height.ToString() + "\n";

            richTextBox1.Text += "影像縮放(縮小一半)\n";
            //建立新的影像，長寬為原始影像的1/2
            Image zoomImage = new Bitmap(pictureBox1.Image.Width / 2, pictureBox1.Image.Height / 2) as Image;

            richTextBox1.Text += "影像放大(放大一倍)\n";
            //建立新的影像，長寬為原始影像的2倍
            Image zoomImageb = new Bitmap(pictureBox1.Image.Width * 2, pictureBox1.Image.Height * 2) as Image;

            //準備繪製新的影像
            Graphics g1 = Graphics.FromImage(zoomImage);
            //於座標(0,0)開始繪製來源影像，長寬設置為來源影像的1/2
            g.DrawImage(pictureBox1.Image, 0, 0, pictureBox1.Image.Width / 2, pictureBox1.Image.Height / 2);
            g.Dispose();


            //準備繪製新的影像
            Graphics g2 = Graphics.FromImage(zoomImageb);
            //於座標(0,0)開始繪製來源影像，長寬設置為來源影像的2倍
            g.DrawImage(pictureBox1.Image, 0, 0, pictureBox1.Image.Width * 2, pictureBox1.Image.Height * 2);
            g.Dispose();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //調整影像大小
            //使用 C# 中的 Bitmap 類調整影象大小
            //使用 C# 中的 Graphics.DrawImage() 函式調整影象大小
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image1 = Image.FromFile(filename);
            Bitmap bitmap1 = new Bitmap(image1);

            //Image image2 = resizeImage(bitmap1, new Size(image1.Width / 2, image1.Height / 2));
            Image image2 = resizeImage(bitmap1, new Size(100, 300));

            pictureBox1.Image = image2;
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
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
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            //改變圖片透明度
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap80 = returnAlpha(bitmap1, 80);
            Bitmap bitmap160 = returnAlpha(bitmap1, 160);
            Bitmap bitmap220 = returnAlpha(bitmap1, 220);

            bitmap80.Save(@"picture_80.bmp", ImageFormat.Bmp);
            bitmap160.Save(@"picture_160.bmp", ImageFormat.Bmp);
            bitmap220.Save(@"picture_220.bmp", ImageFormat.Bmp);

            Bitmap bmp = new Bitmap(W, H);
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

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {

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
            open_new_file();
            g.Clear(Color.Silver);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\banner_ims.png";
            Bitmap bmp0 = (Bitmap)Image.FromFile(filename);	//給不透明使用
            Bitmap bmp1 = (Bitmap)bmp0.Clone();	//給透明使用

            //bmp1.MakeTransparent();    //沒寫就是預設的     程式碼會讓系統預設透明色彩透明
            //bmp1.MakeTransparent(Color.White);//將圖片白色部分透明化, 將此 Bitmap 的指定色彩變為透明。
            //使用默認的透明顏色進行透明設定, 可重複設定
            bmp1.MakeTransparent(Color.Pink);     //使用默認的透明顏色進行透明設置
            bmp1.MakeTransparent(Color.Blue);    //使用默認的透明顏色進行透明設置
            bmp1.MakeTransparent(Color.FromArgb(255, 252, 238, 191));

            //去除紅色
            //Color backColor = bmp1.GetPixel(20, 80);   //選取圖片邊緣的一個點的顏色當成背景色
            //bmp1.MakeTransparent(backColor); //將此背景色設定為透明

            //g.DrawImage(bmp0, 0, 0);
            //g.DrawImage(bmp1, 0, 210);

            //               貼上位置x      貼上位置y      貼上大小W            貼上大小H
            g.DrawImage(bmp0, 20, 50, bmp0.Width / 2, bmp0.Height / 2);
            g.DrawImage(bmp1, 350, 50, bmp1.Width / 2, bmp1.Height / 2);

            g.DrawString("左 : 原圖               右: 去除粉紅色與藍色", new Font("標楷體", 18), new SolidBrush(Color.Black), 50, 10);
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //MakeTransparent 使用 去背效果2
            open_new_file();
            pictureBox1.BackColor = Color.Silver;

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\banner_ims.png";

            GraphicsUnit units = GraphicsUnit.Pixel;

            Bitmap bmp0 = new Bitmap(filename);
            Bitmap bmp1 = new Bitmap(filename);

            //bmp1 做 去背景
            bmp1.MakeTransparent(Color.Blue);  //MakeTransparent 用法, bmp1 去背景, 可以多重去背, 連續寫即可
            bmp1.MakeTransparent(Color.Pink);  //MakeTransparent 用法, bmp1 去背景, 可以多重去背, 連續寫即可

            Rectangle destRect1 = new Rectangle(30, 30, bmp0.Width / 2, bmp0.Height / 2);
            Rectangle destRect2 = new Rectangle(30, 200, bmp1.Width / 2, bmp1.Height / 2);

            //沒去背
            g.DrawImage(bmp0, new Rectangle(30, 30, bmp0.Width / 2, bmp0.Height / 2), 0, 0, bmp0.Width, bmp0.Height, units);

            //有去背
            g.DrawImage(bmp1, new Rectangle(30, 200, bmp1.Width / 2, bmp1.Height / 2), 0, 0, bmp1.Width, bmp1.Height, units);

            g.DrawRectangle(new Pen(Color.Yellow, 3), destRect1);
            g.DrawRectangle(new Pen(Color.Yellow, 3), destRect2);
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

            g.DrawImage((Image)bitmap1, new Point(x_st + W + 10, y_st));

            g.DrawString("MakeTransparent 用法, 指名將白色變成透明", new Font("標楷體", 20), new SolidBrush(Color.Navy), 10, 10);
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {

        }

        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\螺子黛.jpg";
            Image image = Image.FromFile(filename);
            Bitmap bitmap1 = (Bitmap)image;
            switch (cnt)
            {
                case 0:
                    lb_rotate.Text = "0, 旋轉180 + 無鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate180FlipNone);
                    break;
                case 1:
                    lb_rotate.Text = "1, 旋轉180 + X鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate180FlipX);
                    break;
                case 2:
                    lb_rotate.Text = "2, 旋轉180 + XY鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate180FlipXY);
                    break;
                case 3:
                    lb_rotate.Text = "3, 旋轉180 + Y鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate180FlipY);
                    break;
                case 4:
                    lb_rotate.Text = "4, 旋轉270 + 無鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate270FlipNone);
                    break;
                case 5:
                    lb_rotate.Text = "5, 旋轉270 + X鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate270FlipX);
                    break;
                case 6:
                    lb_rotate.Text = "6, 旋轉270 + XY鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate270FlipXY);
                    break;
                case 7:
                    lb_rotate.Text = "7, 旋轉270 + Y鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate270FlipY);
                    break;
                case 8:
                    lb_rotate.Text = "8, 旋轉90 + 無鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate90FlipNone);
                    break;
                case 9:
                    lb_rotate.Text = "9, 旋轉90 + X鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate90FlipX);
                    break;
                case 10:
                    lb_rotate.Text = "10, 旋轉90 + XY鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate90FlipXY);
                    break;
                case 11:
                    lb_rotate.Text = "11, 旋轉90 + Y鏡射";
                    bitmap1.RotateFlip(RotateFlipType.Rotate90FlipY);
                    break;
                case 12:
                    lb_rotate.Text = "12, 旋轉0 + 無鏡射";
                    bitmap1.RotateFlip(RotateFlipType.RotateNoneFlipNone);
                    break;
                case 13:
                    lb_rotate.Text = "13, 旋轉0 + X鏡射";
                    bitmap1.RotateFlip(RotateFlipType.RotateNoneFlipX);
                    break;
                case 14:
                    lb_rotate.Text = "14, 旋轉0 + XY鏡射";
                    bitmap1.RotateFlip(RotateFlipType.RotateNoneFlipXY);
                    break;
                case 15:
                    lb_rotate.Text = "15, 旋轉0 + Y鏡射";
                    bitmap1.RotateFlip(RotateFlipType.RotateNoneFlipY);
                    break;
                default:
                    break;
            }
            pictureBox2.Image = bitmap1;
            cnt++;
            if (cnt > 15)
            {
                cnt = 0;
            }
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

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出


*/

