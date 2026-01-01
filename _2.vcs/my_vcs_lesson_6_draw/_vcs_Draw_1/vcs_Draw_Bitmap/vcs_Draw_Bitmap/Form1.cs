using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat, PixelFormat
using System.Drawing.Drawing2D; //for GraphicsPath, InterpolationMode

namespace vcs_Draw_Bitmap
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        //SolidBrush sb;
        Bitmap bitmap1;

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            button15.BackColor = Color.Pink;

            p = new Pen(Color.Red, 3);
            bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            pictureBox1.Image = bitmap1;

            p = new Pen(Color.Red, 3);

            //指定畫布大小
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
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

            pictureBox1.Size = new Size(1080, 840);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            lb_rotate.Location = new Point(x_st + dx * 7 + 40, y_st + dy * 0);
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.Size = new Size(300, 300);
            pictureBox2.Location = new Point(x_st + dx * 7 + 40, y_st + dy * 0 + 30);

            richTextBox1.Size = new Size(300, 498);
            richTextBox1.Location = new Point(x_st + dx * 7 + 40, y_st + dy * 4 + 60);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1860, 910);
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

        void draw_grid(Graphics g)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            for (int i = 0; i <= W; i += 100)
            {
                g.DrawLine(Pens.Gray, i, 0, i, H);//垂直線
            }
            for (int j = 0; j <= H; j += 100)
            {
                g.DrawLine(Pens.Gray, 0, j, W, j);//水平線
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Image img = Image.FromFile(filename);
            int W = img.Width;
            int H = img.Height;

            int sx = 130;
            int sy = 110;
            int sw = W / 3;
            int sh = H / 3;

            //舊圖上標明位置
            Graphics g_old = pictureBox1.CreateGraphics();
            //標示下一步要擷取的區域
            g_old.DrawRectangle(new Pen(Color.Red, 2), new Rectangle(sx, sy, sw, sh));
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將Bitmap的資料放到剪貼簿裏\n";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            //從pictureBox取得Bitmap
            //Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //圖像截取
            filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            Bitmap bitmap3 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Rectangle source_area = new Rectangle(180, 60, 200, 400);//要截取的矩形區域
            Rectangle destination_area1 = new Rectangle(20, 300, 200, 400);//要顯示到Form的矩形區域
            Rectangle destination_area2 = new Rectangle(240, 300, 120, 240);//要顯示到Form的矩形區域
            Rectangle destination_area3 = new Rectangle(380, 300, 240, 240);//要顯示到Form的矩形區域
            g.DrawImage(bitmap3, destination_area1, source_area, GraphicsUnit.Pixel);
            g.DrawImage(bitmap3, destination_area2, source_area, GraphicsUnit.Pixel);
            g.DrawImage(bitmap3, destination_area3, source_area, GraphicsUnit.Pixel);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //圖像截取
            int x_st = 200;
            int y_st = 70;
            w = 80;
            h = 80;

            //這個矩形定義了，你將要在被截取的圖像上要截取的圖像區域的左頂點位置和截取的大小
            Rectangle rectSource = new Rectangle(x_st, y_st, w, h);

            //這個矩形定義了，你將要把 截取的圖像區域 繪制到初始化的位圖的位置和大小
            //我的定義，說明，我將把截取的區域，從位圖左頂點開始繪制，繪制截取的區域原來大小
            Rectangle rectDest = new Rectangle(100, 100, w, h);

            bitmap2 = (Bitmap)Bitmap.FromFile(filename);

            //第一個參數就是加載你要截取的圖像對象，
            //第二個和第三個參數及如上所說定義截取和繪制圖像過程中的相關屬性，
            //第四個屬性定義了屬性值所使用的度量單位
            rectDest = new Rectangle(300, 50, w, h);
            g.DrawImage(bitmap2, rectDest, rectSource, GraphicsUnit.Pixel);

            rectDest = new Rectangle(400, 70, w, h);
            g.DrawImage(bitmap2, rectDest, rectSource, GraphicsUnit.Pixel);

            rectDest = new Rectangle(500, 90, w, h);
            g.DrawImage(bitmap2, rectDest, rectSource, GraphicsUnit.Pixel);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //在指定位置畫上一圖
            filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_貓咪\cat2.png";
            Image image = Image.FromFile(filename);
            int x = 100;
            int y = 100;
            //貼上原圖
            g.DrawImage(image, x, y);
            //貼上原圖 1/4
            g.DrawImage(image, x + 150, y + 150, image.Width / 2, image.Height / 2);
            //圖片改變比例
            g.DrawImage(image, x + 300, y + 150, image.Width / 2, image.Height * 2);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
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
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //創建32位元深度之Bitmap
            Bitmap bitmap1 = new Bitmap(100, 100, PixelFormat.Format32bppArgb);
            bitmap1.Save("tmp_depth_32.bmp", ImageFormat.Bmp);

            //創建24位元深度之Bitmap
            Bitmap bitmap2 = new Bitmap(100, 100, PixelFormat.Format24bppRgb);
            bitmap2.Save("tmp_depth_24.bmp", ImageFormat.Bmp);

            //沒寫, 預設為32位元深度之Bitmap
            Bitmap bitmap3 = new Bitmap(100, 100);
            bitmap3.Save("tmp_depth_default32.bmp", ImageFormat.Bmp);
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

            g.DrawImage(bmp, 0, 0, W, H);

            bmp.SetResolution(1200f, 1200f);
            bmp.Save("圖片120.bmp", ImageFormat.Bmp);

            g.DrawImage(bmp, 200, 0, W, H);
            pictureBox1.Image = bitmap1;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //改變圖片透明度
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

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

        public static Bitmap returnAlpha(Bitmap bmp, int alpha)
        {
            Color col;
            Bitmap bmp2 = new Bitmap(bmp);
            int W = bmp.Width;
            int H = bmp.Height;

            for (int i = 0; i < W; i++)
            {
                for (int j = 0; j < H; j++)
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

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //bitmap1 是 整個pictureBox1的大小
            //bmp 是 測試圖片, 不改動

            //讀出測試圖片
            Bitmap bmp = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bmp = new Bitmap(filename);//same
            int W = bmp.Width;
            int H = bmp.Height;

            //貼上位置
            int x_st = 0;
            int y_st = 50;
            //來源 sx, sy, sw, sh
            int sx = 0;
            int sy = 0;
            int sw = 0;
            int sh = 0;
            //目的 dx, dy, dw, dh
            int dx = 0;
            int dy = 0;
            int dw = 0;
            int dh = 0;

            //全圖縮放 縮成1/2
            //         影像,貼上位置x,貼上位置y,貼上大小W,貼上大小H
            g.DrawImage(bmp, x_st, y_st, W / 2, H / 2);
            g.DrawString("全圖縮放", new Font("Arial", 20), Brushes.Red, x_st, y_st - 30);

            draw_grid(g);

            x_st = 0;
            y_st = 300;

            //直接改變Bitmap的大小
            //Bitmap bitmap1 = new Bitmap(image, image.Width / 2, image.Height / 2);
            //Bitmap bitmap2 = new Bitmap(bitmap1, bitmap1.Width * 5 / 2, bitmap1.Height * 5 / 2);
            //Bitmap bmp1b = new Bitmap(bmp, new Size(100, 300));   //用Bitmap直接進行縮放
            Bitmap bmp1b = new Bitmap(bmp, W / 2, H / 2);   //用Bitmap直接進行縮放
            g.DrawImage(bmp1b, x_st, y_st);
            g.DrawString("直接改變Bitmap的大小", new Font("Arial", 16), Brushes.Red, x_st, y_st - 30);

            //clone語法
            x_st = 800;
            y_st = 400;
            double ratio = 0.456f;
            Bitmap bmp1c = Resize(bmp, ratio);
            g.DrawImage(bmp1c, x_st, y_st);
            g.DrawString("直接改變Bitmap的大小", new Font("Arial", 16), Brushes.Red, x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            x_st = 200;
            y_st = 200;
            dx = 180;
            dy = 90;
            //原圖貼上, 改變貼上比例
            //               貼上位置x      貼上位置y      貼上大小W   貼上大小H
            g.DrawImage(bmp, x_st + dx * 0, y_st + dy * 0, W * 3 / 10, H * 7 / 10);  //改變貼上比例
            g.DrawString("改變貼上比例", new Font("Arial", 16), Brushes.Red, x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //決定繪製影像的縮放比例和切變
            x_st = 500;
            y_st = 400;
            int w = W / 1;
            int h = H / 1;
            // Create parallelogram for drawing image.
            Point ulCorner3 = new Point(x_st, y_st);   //左上
            Point urCorner3 = new Point(x_st + w, y_st);   //右上
            Point llCorner3 = new Point(x_st - 50, y_st + h);   //左下
            Point[] destPara = { ulCorner3, urCorner3, llCorner3 };
            g.DrawImage(bmp, destPara);
            g.DrawString("HHH", new Font("Arial", 20), Brushes.Red, x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //改變影像位置與大小, 用DrawImage貼上影像 並改變影像位置與大小
            //使用Rectangle結構
            x_st = 0;
            y_st = 550;
            dx = x_st;
            dy = y_st;
            dw = W / 2;
            dh = H / 2;
            Rectangle destRect4 = new Rectangle(dx, dy, dw, dh);
            g.DrawImage(bmp, destRect4);
            g.DrawString("使用Rectangle結構", new Font("Arial", 16), Brushes.Red, x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //用DrawImage畫出不同圖片大小的圖

            x_st = 200;
            y_st = 550;
            float scale;
            w = 0;
            h = 0;
            g.InterpolationMode = InterpolationMode.NearestNeighbor;   // No smoothing.

            Rectangle source = new Rectangle(0, 0, W, H);
            Point[] dest =
                {
                    new Point(x_st+0, y_st +0),
                    new Point(x_st+w, y_st +0),
                    new Point(x_st+0, y_st +h),
                };

            //改變圖形大小
            for (scale = 0.75f; scale > 0.20f; scale -= 0.25f)
            {
                w = (int)(W * scale);
                h = (int)(H * scale);

                dest[0] = new Point(x_st + 0, y_st + 0);
                dest[1] = new Point(x_st + w, y_st + 0);
                dest[2] = new Point(x_st + 0, y_st + h);
                g.DrawImage(bmp, dest, source, GraphicsUnit.Pixel);
            }
            g.DrawString("不同比例", new Font("Arial", 16), Brushes.Red, x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //以下為部分擷取

            //來源
            //Rectangle srcRect = new Rectangle(0, 0, W, H); //擷取全圖

            sx = 130;
            sy = 110;
            sw = W / 3;
            sh = H / 3;
            Rectangle srcRect = new Rectangle(sx, sy, sw, sh);   //擷取部分區域
            GraphicsUnit units = GraphicsUnit.Pixel;

            x_st = 200;
            y_st = 50;
            // 準備貼上的位置與放大縮小量,以平行四邊形(parallelogram)的左上點右上點左下點表示
            Point ulCorner = new Point(x_st, y_st);//左上
            Point urCorner = new Point(x_st + 100, y_st);//右上
            Point llCorner = new Point(x_st, y_st + 100);//左下
            Point[] destRect1 = { ulCorner, urCorner, llCorner };
            //擷取部分圖片貼上
            //            貼上位置與大小,擷取部分圖片位置與大小,單位
            g.DrawImage(bmp, destRect1, srcRect, units);
            g.DrawString("BBB", new Font("Arial", 20), Brushes.Red, x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            x_st = 400;
            y_st = 50;
            //擷取部分圖片[非矩形]貼上
            Point ulCorner2 = new Point(x_st, y_st);//左上
            Point urCorner2 = new Point(x_st + 100, y_st);//右上
            Point llCorner2 = new Point(x_st - 50, y_st + 100);//左下
            Point[] destRect2 = { ulCorner2, urCorner2, llCorner2 };
            //擷取部分圖片貼上
            //            貼上位置與大小,擷取部分圖片位置與大小,單位
            g.DrawImage(bmp, destRect2, srcRect, units);
            g.DrawString("CCC", new Font("Arial", 20), Brushes.Red, x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            x_st = 550;
            y_st = 50;
            dx = x_st;
            dy = y_st;
            dw = 180;
            dh = 120;

            Rectangle destRect3 = new Rectangle(dx, dy, dw, dh);
            sx = 50;
            sy = 50;
            sw = 150;
            sh = 150;
            g.DrawImage(bmp, destRect3, sx, sy, sw, sh, units);
            g.DrawRectangle(Pens.Red, destRect3);
            g.DrawString("DDD", new Font("Arial", 20), Brushes.Red, x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            x_st = 750;//貼上位置
            y_st = 50;

            //來源
            Rectangle srcRect2 = new Rectangle(50, 50, 150, 150);   //來源矩形
            //          影像  目的   來源    單位
            g.DrawImage(bmp, x_st, y_st, srcRect2, units);
            g.DrawString("EEE", new Font("Arial", 20), Brushes.Red, x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用兩個Rectangle結構

            x_st = 900;//貼上位置
            y_st = 50;
            //目的
            Rectangle destRect = new Rectangle(x_st, y_st, 200, 100);
            //來源
            Rectangle srcRect3 = new Rectangle(100, 100, 100, 50);
            //          影像  目的     來源      單位
            g.DrawImage(bmp, destRect, srcRect3, units);
            g.DrawRectangle(Pens.Green, destRect);
            g.DrawString("FFF", new Font("Arial", 20), Brushes.Red, x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //取得圖片的一部分

            x_st = 400;
            y_st = 200;
            sx = 0;
            sy = 0;
            sw = W / 2;
            sh = H / 2;
            dx = x_st;
            dy = y_st;
            dw = W / 3;
            dh = H / 3;

            Image image = Image.FromFile(filename);

            //來源
            Rectangle rec1 = new Rectangle(new Point(sx, sy), new Size(sw, sh));//原圖位置
            //目標
            Rectangle rec2 = new Rectangle(new Point(dx, dy), new Size(dw, dh));//目標位置
            g.DrawImage(image, rec2, rec1, GraphicsUnit.Pixel);
            g.DrawString("LLL", new Font("Arial", 20), Brushes.Red, x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //clone語法, 複製部分圖片

            x_st = 100;
            y_st = 100;
            w = 150;
            h = 150;
            RectangleF rect = new RectangleF(x_st, y_st, w, h);

            PixelFormat format = bitmap1.PixelFormat;
            //Bitmap cloneBitmap = bitmap1.Clone(rect, PixelFormat.DontCare);//PixelFormat.Format32bppArgb
            Bitmap cloneBitmap = bmp.Clone(rect, format);//PixelFormat.Format32bppArgb

            //Bitmap bitmap2 = new Bitmap(W, H);
            //Graphics g = Graphics.FromImage(bitmap2);
            //g.Clear(Color.Pink);

            g.DrawImage(cloneBitmap, 800, 200, w, h);
            g.DrawString("Clone語法", new Font("Arial", 16), Brushes.Red, 800, 200 - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //獲取圖片的指定部分

            x_st = 550;
            y_st = 200;
            //來源 sx, sy, sw, sh
            sx = 0;
            sy = 0;
            sw = 120;
            sh = 180;
            //目的 dx, dy, dw, dh
            dx = x_st;
            dy = y_st;
            dw = 120;
            dh = 180;

            destRect = new Rectangle(new Point(dx, dy), new Size(dw, dh));//目標位置
            srcRect = new Rectangle(new Point(sx, sy), new Size(sw, sh));//原圖位置（默認從原圖中截取的圖片大小等於目標圖片的大小）
            g.DrawImage(bmp, destRect, srcRect, GraphicsUnit.Pixel);
            g.DrawString("獲取圖片的指定部分", new Font("Arial", 16), Brushes.Red, x_st, y_st - 30);

            pictureBox1.Image = bitmap1;
        }

        Bitmap Resize(Bitmap bitmap1, Double ratio)
        {
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int w = Convert.ToInt32(W * ratio);
            int h = Convert.ToInt32(H * ratio);

            return Process(bitmap1, W, H, w, h);
        }

        Bitmap Process(Bitmap bitmap1, int oriwidth, int oriheight, int width, int height)
        {
            Bitmap resizedbitmap = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(resizedbitmap);
            g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            g.Clear(Color.Transparent);
            g.DrawImage(bitmap1, new Rectangle(0, 0, width, height), new Rectangle(0, 0, oriwidth, oriheight), GraphicsUnit.Pixel);
            return resizedbitmap;
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //MakeTransparent 去背效果1
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

        private void button18_Click(object sender, EventArgs e)
        {
            //MakeTransparent 去背效果2
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

        private void button19_Click(object sender, EventArgs e)
        {
            //MakeTransparent 去背效果3

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
            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height, PixelFormat.Format32bppRgb);
            Bitmap bitmap2 = (Bitmap)Bitmap.FromFile(filename);

            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);


            pictureBox1.Image = (Image)bitmap1;

            g.Dispose();

            g.DrawString("改變Bitmap大小,\n貼在原點", new Font("Arial", 30), Brushes.Red, new PointF(100, 400));

            Bitmap bmp = new Bitmap(filename, true);
            g.DrawImage(bmp, 0, 0, W, H);
            g.DrawImage(bmp, 0, 450, W, H / 2);
 * 
*/
