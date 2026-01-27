using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//圖片加水印

namespace vcs_Draw_Watermark1
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

            reset_picturebox();
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

            pictureBox1.Size = new Size(640, 480);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y);

            richTextBox1.Size = new Size(400, 660);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1520, 720);
            this.Text = "vcs_Draw_Watermark1";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void reset_picturebox()
        {
            //讀取圖檔, 多一層Image結構
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename1);
            pictureBox1.Image = image;
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            reset_picturebox();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            Bitmap bitmap1 = new Bitmap(filename1);
            Graphics g = Graphics.FromImage(bitmap1);

            int fontsize = 20;
            string _watermarkText = "lion-mouse";
            string _watermarkPosition = "WM_TOP_LEFT";
            int _width = 150;
            int _height = 150;

            int[] sizes = new int[] { 32, 14, 12, 10, 8, 6, 4 };
            Font crFont = null;
            SizeF crSize = new SizeF();

            crFont = new Font("微軟雅黑", fontsize, FontStyle.Bold);
            crSize = g.MeasureString(_watermarkText, crFont);

            float xpos = 0;
            float ypos = 0;
            Color color = Color.Firebrick;

            switch (_watermarkPosition)
            {
                case "WM_TOP_LEFT":
                    xpos = ((float)_width * (float).01) + (crSize.Width / 2);
                    ypos = (float)_height * (float).01;
                    break;
                case "WM_TOP_RIGHT":
                    xpos = ((float)_width * (float).99) - (crSize.Width / 2);
                    ypos = (float)_height * (float).01;
                    break;
                case "WM_BOTTOM_RIGHT":
                    xpos = ((float)_width * (float).99) - (crSize.Width / 2);
                    ypos = ((float)_height * (float).99) - crSize.Height;
                    break;
                case "WM_BOTTOM_LEFT":
                    xpos = ((float)_width * (float).01) + (crSize.Width / 2);
                    ypos = ((float)_height * (float).99) - crSize.Height;
                    break;
            }

            StringFormat StrFormat = new StringFormat();
            StrFormat.Alignment = StringAlignment.Center;
            SolidBrush semiTransBrush2 = new SolidBrush(Color.FromArgb(153, 0, 0, 0));//加陰影
            g.DrawString(_watermarkText, crFont, semiTransBrush2, xpos + 1, ypos + 1, StrFormat);

            SolidBrush semiTransBrush = new SolidBrush(color);  //添加水印
            g.DrawString(_watermarkText, crFont, semiTransBrush, xpos, ypos, StrFormat);

            semiTransBrush2.Dispose();
            semiTransBrush.Dispose();

            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();

            string type = "Top";
            string _watermarkText = "牡丹亭";

            //1、先畫矩形
            RectangleF drawRect;
            Color color;
            if (type == "Top")
            {
                drawRect = new RectangleF(73, 135, 450, 64);
                //color = Color.FromArgb(255, 255, 255);
                color = Color.Red;
            }
            else
            {
                drawRect = new RectangleF(194, 245, 250, 39);
                //color = Color.FromArgb(244, 226, 38);
                color = Color.Pink;
            }

            //2、在基於矩形畫水印文字
            Font crFont = new Font("微軟雅黑", 20, FontStyle.Bold);
            SolidBrush semiTransBrush = new SolidBrush(color);  //添加水印
            StringFormat StrFormat = new StringFormat();
            StrFormat.Alignment = StringAlignment.Center;
            g.DrawString(_watermarkText, crFont, semiTransBrush, drawRect, StrFormat);

            semiTransBrush.Dispose();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //要加上浮水印的圖片
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\_material\ims-small-logo.png";
            Image image_watermark = Image.FromFile(filename2);

            Bitmap bitmap1 = new Bitmap(pictureBox1.Image);

            Bitmap watermark_bm = new Bitmap(image_watermark);

            int x = (bitmap1.Width - watermark_bm.Width) / 2;
            int y = (bitmap1.Height - watermark_bm.Height) / 2;
            DrawWatermark1(watermark_bm, bitmap1, x, y);

            pictureBox1.Image = bitmap1;
        }

        // Copy the watermark image over the result image.
        private void DrawWatermark1(Bitmap bitmap1, Bitmap result_bm, int x, int y)
        {
            const byte ALPHA = 128;
            // Set the watermark's pixels' Alpha components.
            Color clr;
            for (int py = 0; py < bitmap1.Height; py++)
            {
                for (int px = 0; px < bitmap1.Width; px++)
                {
                    clr = bitmap1.GetPixel(px, py);
                    bitmap1.SetPixel(px, py, Color.FromArgb(ALPHA, clr.R, clr.G, clr.B));
                }
            }

            // Set the watermark's transparent color.
            bitmap1.MakeTransparent(bitmap1.GetPixel(0, 0));

            // Copy onto the result image.
            using (Graphics g = Graphics.FromImage(result_bm))
            {
                g.DrawImage(bitmap1, x, y);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
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

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            Image image = Image.FromFile(filename1);
            //pictureBox1.Image = image;

            Bitmap bitmap1 = new Bitmap(filename1);
            //bitmap1.SetResolution(3, 3);

            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.FromName("white"));

            g.InterpolationMode = InterpolationMode.High;
            g.SmoothingMode = SmoothingMode.HighQuality;

            pictureBox1.Image = bitmap1;
*/
