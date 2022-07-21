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
}
