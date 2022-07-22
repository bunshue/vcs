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
        //Graphics g;
        //Pen p;
        //SolidBrush sb;
        Bitmap bitmap1;

        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

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

        private void button0_Click(object sender, EventArgs e)
        {
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
            //Bitmap先變成Graphics, 拿來畫圖用
            Graphics g = Graphics.FromImage(bitmap1);
            //pHdc = g.GetHdc();
            g.ReleaseHdc();
            //g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);
            g.Dispose();

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //改變Bitmap大小
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);
            Bitmap bitmap1 = new Bitmap(image, image.Width / 2, image.Height / 2);
            Bitmap bitmap2 = new Bitmap(bitmap1, bitmap1.Width * 5 / 2, bitmap1.Height * 5 / 2);
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
            Graphics graphics0 = Graphics.FromImage(zoomImage);
            //於座標(0,0)開始繪製來源影像，長寬設置為來源影像的1/2
            graphics0.DrawImage(pictureBox1.Image, 0, 0, pictureBox1.Image.Width / 2, pictureBox1.Image.Height / 2);
            graphics0.Dispose();
            //儲存新的影像
            string filename = Application.StartupPath + "\\zoom_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            zoomImage.Save(@filename, ImageFormat.Jpeg);
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
            Graphics graphics0a = Graphics.FromImage(zoomImageb);
            //於座標(0,0)開始繪製來源影像，長寬設置為來源影像的2倍
            graphics0a.DrawImage(pictureBox1.Image, 0, 0, pictureBox1.Image.Width * 2, pictureBox1.Image.Height * 2);
            graphics0a.Dispose();
            //儲存新的影像
            string filename = Application.StartupPath + "\\big_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            zoomImageb.Save(@filename, ImageFormat.Jpeg);
            richTextBox1.Text += "放大一倍，存檔完成，檔名：" + filename + "\n";
            #endregion
        }

        private void button16_Click(object sender, EventArgs e)
        {

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

        private void button20_Click(object sender, EventArgs e)
        {

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

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

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
        public static Bitmap Resize(Bitmap originImage, Double times)
        {
            int width = Convert.ToInt32(originImage.Width * times);
            int height = Convert.ToInt32(originImage.Height * times);

            return Process(originImage, originImage.Width, originImage.Height, width, height);
        }

        private static Bitmap Process(Bitmap originImage, int oriwidth, int oriheight, int width, int height)
        {
            Bitmap resizedbitmap = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(resizedbitmap);
            g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            g.Clear(Color.Transparent);
            g.DrawImage(originImage, new Rectangle(0, 0, width, height), new Rectangle(0, 0, oriwidth, oriheight), GraphicsUnit.Pixel);
            return resizedbitmap;
        }
    }
}

