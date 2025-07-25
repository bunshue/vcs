using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Threading;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;   //for BitmapData

using System.Runtime.InteropServices;   //for Marshal
using System.Diagnostics;   //for Stopwatch

//C#圖像處理(各種旋轉、改變大小、柔化、銳化、霧化、底片、浮雕、黑白、濾鏡效果)
//http://www.aspphp.online/bianchen/cyuyan/gycyy/201701/81415.html

namespace vcs_ImageProcessing3
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\_image_processing\isinbaeva.jpg";

        Stopwatch sw = new Stopwatch();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button8.Text = "百葉窗效果 垂直/水平";
            button9.Text = "馬賽克效果";
            button10.Text = "油畫效果";
            button11.Text = "扭曲效果 TBD";
            button12.Text = "積木效果";

            reset_pictureBox();
            show_item_location();
        }

        void reset_pictureBox()
        {
            //讀取圖檔
            pictureBox1.Image = Image.FromFile(filename);
            pictureBox2.Image = Image.FromFile(filename);
        }

        void show_item_location()
        {
            int x_st = 10;
            int y_st = 10;
            int dx = 140 + 10;
            int dy = 40 + 10;
            int W = 150;
            int H = 400;

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 14);
            button15.Location = new Point(x_st + dx * 0, y_st + dy * 15);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button24.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button26.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button27.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            button28.Location = new Point(x_st + dx * 1, y_st + dy * 12);
            button29.Location = new Point(x_st + dx * 1, y_st + dy * 13);
            button30.Location = new Point(x_st + dx * 1, y_st + dy * 14);
            button31.Location = new Point(x_st + dx * 1, y_st + dy * 15);

            groupBox0.Size = new Size(W, H);
            groupBox1.Size = new Size(W, H);
            groupBox2.Size = new Size(W, H);
            groupBox0.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 8);

            pictureBox1.Size = new Size(680, 680);
            pictureBox1.Location = new Point(x_st + dx * 4 + 10, y_st + dy * 0);
            pictureBox2.Size = new Size(680, 680);
            pictureBox2.Location = new Point(x_st + dx * 4 + 10, y_st + dy * 0 + 680);

            bt_restore.Location = new Point(x_st + dx * 10, y_st + dy * 0);
            richTextBox1.Size = new Size(300, 900);
            richTextBox1.Location = new Point(x_st + dx * 10 + 100, y_st + dy * 0);

            x_st = 20;
            y_st = 30;
            dy = 35 + 10;
            bt_image_process_p0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_image_process_p1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_image_process_p2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_image_process_p3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_image_process_p4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_image_process_p5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_image_process_p6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_image_process_p7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            bt_image_process_m0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_image_process_m1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_image_process_m2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_image_process_m3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_image_process_m7.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_image_process_m5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_image_process_m6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_image_process_m7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            bt_edge_detection0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_edge_detection1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_edge_detection2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_edge_detection3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_edge_detection4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_edge_detection5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_edge_detection6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_edge_detection7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_open_file_setup();
            bt_exit_setup();
        }

        private void bt_open_file_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();

            openFileDialog1.Title = "單選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //單選
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";

                filename = openFileDialog1.FileName;
                reset_pictureBox();
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        void bt_open_file_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_open_file = new Button();  // 實例化按鈕
            bt_open_file.Size = new Size(w, h);
            bt_open_file.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Blue, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, w / 4, 0, (w - 1) / 2, h - 1);
            g.DrawLine(p, (w - 1) * 3 / 4, 0, (w - 1) / 2, h - 1);
            bt_open_file.Image = bmp;

            bt_open_file.Location = new Point(this.ClientSize.Width - bt_open_file.Width, 0 + h);
            bt_open_file.Click += bt_open_file_Click;     // 加入按鈕事件

            this.Controls.Add(bt_open_file); // 將按鈕加入表單
            bt_open_file.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Name = "bt_exit";
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_restore_Click(object sender, EventArgs e)
        {
            reset_pictureBox();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "彩虹化圖片\n";
            string filename = @"C:\_git\vcs\_1.data\______test_files1\bear.jpg";
            pictureBox1.Image = ToRainbow(filename);
        }

        private Bitmap ToRainbow(string filename)
        {
            Image image = Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            //get image dimension
            int width = image.Width;
            int height = image.Height;

            Bitmap bmp = new Bitmap(width, height);
            using (Graphics gr = Graphics.FromImage(bmp))
            {
                // Define target colors.
                Color[] color =
                {
                    //Color.Red, Color.Orange, Color.Yellow,
                    //Color.Green, Color.Blue, Color.Indigo,
                    //Color.Violet,

                    Color.Red, Color.OrangeRed, Color.Yellow,
                    Color.Green, Color.Blue, Color.Indigo,
                    Color.Fuchsia,
                };
                const float scale = 2.0f;

                // Draw.
                for (int i = 0; i < color.Length; i++)
                {
                    // Create the ColorMatrix.
                    ColorMatrix cm = new ColorMatrix(new float[][]
                    {
                        new float[] {color[i].R / 255f * scale, 0, 0, 0, 0},
                        new float[] {0, color[i].G / 255f * scale, 0, 0, 0},
                        new float[] {0, 0, color[i].B / 255f * scale, 0, 0},
                        new float[] {0, 0, 0, 1, 0},
                        new float[] {0, 0, 0, 0, 1},
                    });
                    ImageAttributes attr = new ImageAttributes();
                    attr.SetColorMatrix(cm);

                    // Draw the next part of the image.
                    int x = (int)(i * image.Width / color.Length);
                    Point[] points =
                    {
                        new Point(x, 0),
                        new Point(width, 0),
                        new Point(x, height),
                    };
                    Rectangle rect = new Rectangle(x, 0, width - x, height);
                    gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, attr);
                }
            }
            return bmp;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "鏡像圖片\n";
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = ToMirror(filename);
        }

        private Bitmap ToMirror(string filename)
        {
            Image image = Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            Bitmap bmp = new Bitmap(image);

            //get image dimension
            int width = image.Width;
            int height = image.Height;

            //mirror image
            Bitmap mimg = new Bitmap(width * 2, height);

            for (int y = 0; y < height; y++)
            {
                for (int lx = 0, rx = width * 2 - 1; lx < width; lx++, rx--)
                {
                    //get source pixel value
                    Color p = bmp.GetPixel(lx, y);

                    //set mirror pixel value
                    mimg.SetPixel(lx, y, p);
                    mimg.SetPixel(rx, y, p);
                }
            }
            return mimg;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //模糊處理
            richTextBox1.Text += "模糊處理\n";
            string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            richTextBox1.Text += "PictureToBlur\n";
            pictureBox1.Image = ToBlur(filename);
        }

        private Bitmap ToBlur(string filename)
        {
            Image image = Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap1 = new Bitmap(image);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            for (int j = 0; j < H; j++)
            {
                for (int i = 0; i < W; i++)
                {
                    int ok_cnt = 0;
                    int R = 0;
                    int G = 0;
                    int B = 0;

                    // 檢查相鄰像素, 每個點的鄰居不一樣多, 所以要做不同的平均

                    //自己
                    R += bitmap1.GetPixel(i, j).R;
                    G += bitmap1.GetPixel(i, j).G;
                    B += bitmap1.GetPixel(i, j).B;

                    ok_cnt++;

                    if (j - 1 > 0)       //上
                    {
                        R += bitmap1.GetPixel(i, j - 1).R;
                        G += bitmap1.GetPixel(i, j - 1).G;
                        B += bitmap1.GetPixel(i, j - 1).B;

                        ok_cnt++;
                    }
                    if (j + 1 < H)      //下
                    {
                        R += bitmap1.GetPixel(i, j + 1).R;
                        G += bitmap1.GetPixel(i, j + 1).G;
                        B += bitmap1.GetPixel(i, j + 1).B;
                        ok_cnt++;
                    }
                    if (i - 1 > 0)       //左
                    {
                        R += bitmap1.GetPixel(i - 1, j).R;
                        G += bitmap1.GetPixel(i - 1, j).G;
                        B += bitmap1.GetPixel(i - 1, j).B;
                        ok_cnt++;
                    }
                    if (i + 1 < W)       //右
                    {
                        R += bitmap1.GetPixel(i + 1, j).R;
                        G += bitmap1.GetPixel(i + 1, j).G;
                        B += bitmap1.GetPixel(i + 1, j).B;
                        ok_cnt++;
                    }
                    if ((i - 1 > 0) && (j - 1 > 0))     //左上
                    {
                        R += bitmap1.GetPixel(i - 1, j - 1).R;
                        G += bitmap1.GetPixel(i - 1, j - 1).G;
                        B += bitmap1.GetPixel(i - 1, j - 1).B;
                        ok_cnt++;
                    }
                    if ((i - 1 > 0) && (j + 1 < H)) //左下
                    {
                        R += bitmap1.GetPixel(i - 1, j + 1).R;
                        G += bitmap1.GetPixel(i - 1, j + 1).G;
                        B += bitmap1.GetPixel(i - 1, j + 1).B;
                        ok_cnt++;
                    }
                    if ((i + 1 < W) && (j - 1 > 0))      //右上
                    {
                        R += bitmap1.GetPixel(i + 1, j - 1).R;
                        G += bitmap1.GetPixel(i + 1, j - 1).G;
                        B += bitmap1.GetPixel(i + 1, j - 1).B;
                        ok_cnt++;
                    }
                    if ((i + 1 < W) && (j + 1 < H)) //右下
                    {
                        R += bitmap1.GetPixel(i + 1, j + 1).R;
                        G += bitmap1.GetPixel(i + 1, j + 1).G;
                        B += bitmap1.GetPixel(i + 1, j + 1).B;
                        ok_cnt++;
                    }

                    //平均, 設定個點的像素值
                    bitmap2.SetPixel(i, j, Color.FromArgb((R / ok_cnt), (G / ok_cnt), (B / ok_cnt)));
                }
            }
            return bitmap2;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Sepia 1
            //將圖片轉為 Sepia 效果
            // Display the image converted to sepia tone.
            pictureBox2.Image = ToSepiaTone1(pictureBox1.Image);
        }

        // Convert an image to sepia tone.
        private Bitmap ToSepiaTone1(Image image)
        {
            // Make the ColorMatrix.
            ColorMatrix cm = new ColorMatrix(new float[][]
            {
                new float[] {0.393f, 0.349f, 0.272f, 0, 0},
                new float[] {0.769f, 0.686f, 0.534f, 0, 0},
                new float[] {0.189f, 0.168f, 0.131f, 0, 0},
                new float[] { 0, 0, 0, 1, 0},
                new float[] { 0, 0, 0, 0, 1}
            });
            //ColorMatrix cm = new ColorMatrix(new float[][]
            //{
            //    new float[] {0.300f, 0.066f, 0.300f, 0, 0},
            //    new float[] {0.500f, 0.350f, 0.600f, 0, 0},
            //    new float[] {0.100f, 0.000f, 0.200f, 0, 0},
            //    new float[] { 0, 0, 0, 1, 0},
            //    new float[] { 0, 0, 0, 0, 1}
            //});
            ImageAttributes attributes = new ImageAttributes();
            attributes.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width - 1, 0),
                new Point(0, image.Height - 1),
            };
            Rectangle rect = new Rectangle(0, 0, image.Width, image.Height);

            // Make the result bitmap.
            Bitmap bmp = new Bitmap(image.Width, image.Height);
            using (Graphics gr = Graphics.FromImage(bmp))
            {
                gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, attributes);
            }

            // Return the result.
            return bmp;
        }


        private void button4_Click(object sender, EventArgs e)
        {
            //Sepia 2
            //將圖片轉為 Sepia 效果
            // Display the image converted to sepia tone.
            pictureBox2.Image = ToSepiaTone2(pictureBox1.Image);
        }

        // Convert an image to sepia tone.
        private Bitmap ToSepiaTone2(Image image)
        {
            //將圖片轉為 Sepia 效果
            Bitmap bmp = new Bitmap(image);

            int width = bmp.Width;
            int height = bmp.Height;

            Color p;

            //sepia
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //get pixel value
                    p = bmp.GetPixel(x, y);

                    //extract pixel component ARGB
                    int a = p.A;
                    int r = p.R;
                    int g = p.G;
                    int b = p.B;

                    //calculate temp value
                    int tr = (int)(0.393 * r + 0.769 * g + 0.189 * b);
                    int tg = (int)(0.349 * r + 0.686 * g + 0.168 * b);
                    int tb = (int)(0.272 * r + 0.534 * g + 0.131 * b);

                    //set new RGB value
                    if (tr > 255)
                    {
                        r = 255;
                    }
                    else
                    {
                        r = tr;
                    }

                    if (tg > 255)
                    {
                        g = 255;
                    }
                    else
                    {
                        g = tg;
                    }

                    if (tb > 255)
                    {
                        b = 255;
                    }
                    else
                    {
                        b = tb;
                    }

                    //set the new RGB value in image pixel
                    bmp.SetPixel(x, y, Color.FromArgb(a, r, g, b));
                }
            }
            return bmp;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //單色處理
            richTextBox1.Text += "單色處理\n";
            pictureBox2.Image = ToMonochrome(pictureBox1.Image);
        }


        // Convert an image to monochrome.
        private Bitmap ToMonochrome(Image image)
        {
            // Make the ColorMatrix.
            ColorMatrix cm = new ColorMatrix(new float[][]
            {
                new float[] {0.299f, 0.299f, 0.299f, 0, 0},
                new float[] {0.587f, 0.587f, 0.587f, 0, 0},
                new float[] {0.114f, 0.114f, 0.114f, 0, 0},
                new float[] { 0, 0, 0, 1, 0},
                new float[] { 0, 0, 0, 0, 1}
            });
            ImageAttributes attributes = new ImageAttributes();
            attributes.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width - 1, 0),
                new Point(0, image.Height - 1),
            };
            Rectangle rect = new Rectangle(0, 0, image.Width, image.Height);

            // Make the result bitmap.
            Bitmap bm = new Bitmap(image.Width, image.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, attributes);
            }
            // Return the result.
            return bm;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //單色圖片 1
            // Convert the image into red, green, and blue monochrome.
            Image image = Image.FromFile(filename);
            pictureBox1.Image = ScaleColorComponents(image, 1, 0, 0, 1);//R
            pictureBox2.Image = ScaleColorComponents(image, 0, 1, 0, 1);//G
            ///pictureBox1.Image = ScaleColorComponents(image, 0, 0, 1, 1);//G
        }

        // Scale an image's color components.
        private Bitmap ScaleColorComponents(Image image, float r, float g, float b, float a)
        {
            // Make the ColorMatrix.
            ColorMatrix cm = new ColorMatrix(new float[][]
                {
                    new float[] {r, 0, 0, 0, 0},
                    new float[] {0, g, 0, 0, 0},
                    new float[] {0, 0, b, 0, 0},
                    new float[] {0, 0, 0, a, 0},
                    new float[] {0, 0, 0, 0, 1},
                });
            ImageAttributes attributes = new ImageAttributes();
            attributes.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width - 1, 0),
                new Point(0, image.Height - 1),
            };
            Rectangle rect = new Rectangle(0, 0, image.Width, image.Height);

            // Make the result bitmap.
            Bitmap bm = new Bitmap(image.Width, image.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, attributes);
            }

            // Return the result.
            return bm;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //單色圖片 2
            //製作單色圖片
            show_mono_color_picture();
        }

        private void show_mono_color_picture()
        {
            Bitmap bmp = new Bitmap(filename);

            //load original image in picturebox1
            //pictureBox1.Image = Image.FromFile(filename);

            //get image dimension
            int width = bmp.Width;
            int height = bmp.Height;

            //3 bitmap for red green blue image
            Bitmap rbmp = new Bitmap(bmp);
            Bitmap gbmp = new Bitmap(bmp);
            Bitmap bbmp = new Bitmap(bmp);

            //red green blue image
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //get pixel value
                    Color p = bmp.GetPixel(x, y);

                    //extract ARGB value from p
                    int a = p.A;
                    int r = p.R;
                    int g = p.G;
                    int b = p.B;

                    //set red image pixel
                    rbmp.SetPixel(x, y, Color.FromArgb(a, r, 0, 0));

                    //set green image pixel
                    gbmp.SetPixel(x, y, Color.FromArgb(a, 0, g, 0));

                    //set blue image pixel
                    bbmp.SetPixel(x, y, Color.FromArgb(a, 0, 0, b));
                }
            }

            //load red image in picturebox7
            pictureBox1.Image = rbmp;

            //load green image in picturebox8
            pictureBox2.Image = gbmp;

            //load blue image in picturebox9
            //pictureBox1.Image = bbmp;
        }




        int cnt = 0;
        private void button8_Click(object sender, EventArgs e)
        {
            //百葉窗效果 水平垂直輪流顯示
            if ((cnt % 2) == 0)
            {
                shutter1();
            }
            else
            {
                shutter2();
            }
            cnt++;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            image_processing9(filename);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = image_processing10(filename);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "TBD\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = image_processing12(filename);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            filename = @"C:\_git\vcs\_1.data\______test_files1\_image_processing\isinbaeva.jpg";
            image_processing11(filename);
        }

        /*
        一. 底片效果
        原理: GetPixel方法獲得每一點像素的值, 然後再使用SetPixel方法將取反後的顏色值設置到對應的點.
        */

        //底片效果
        private Bitmap image_processing1(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);
            Color pixel;
            for (int x = 1; x < W; x++)
            {
                for (int y = 1; y < H; y++)
                {
                    int r, g, b;
                    pixel = bitmap1.GetPixel(x, y);
                    r = 255 - pixel.R;
                    g = 255 - pixel.G;
                    b = 255 - pixel.B;
                    bitmap2.SetPixel(x, y, Color.FromArgb(r, g, b));
                }
            }
            return bitmap2;
        }

        /*
        二. 浮雕效果

        原理: 對圖像像素點的像素值分別與相鄰像素點的像素值相減後加上128, 然後將其作為新的像素點的值.

        使圖像產生浮雕的效果，主要通過對圖像像素點的像素值分別與相鄰像素點的像素值相減後加上128，然後將其作為新的像素點的值。
        以浮雕效果顯示圖像主要通過GetPixel方法獲得每一點像素的值，通過SetPixel設置該像素點的像素值。
        */
        //浮雕效果
        private Bitmap image_processing2(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);
            Color pixel1, pixel2;
            for (int x = 0; x < W - 1; x++)
            {
                for (int y = 0; y < H - 1; y++)
                {
                    int r = 0, g = 0, b = 0;
                    pixel1 = bitmap1.GetPixel(x, y);
                    pixel2 = bitmap1.GetPixel(x + 1, y + 1);
                    r = Math.Abs(pixel1.R - pixel2.R + 128);
                    g = Math.Abs(pixel1.G - pixel2.G + 128);
                    b = Math.Abs(pixel1.B - pixel2.B + 128);
                    if (r > 255)
                        r = 255;
                    if (r < 0)
                        r = 0;
                    if (g > 255)
                        g = 255;
                    if (g < 0)
                        g = 0;
                    if (b > 255)
                        b = 255;
                    if (b < 0)
                        b = 0;
                    bitmap2.SetPixel(x, y, Color.FromArgb(r, g, b));
                }
            }
            return bitmap2;
        }

        /*
        三. 黑白效果
        原理: 彩色圖像處理成黑白效果通常有3種算法；
        (1).最大值法: 使每個像素點的 R, G, B 值等於原像素點的 RGB (顏色值) 中最大的一個；
        (2).平均值法: 使用每個像素點的 R,G,B值等於原像素點的RGB值的平均值；
        (3).加權平均值法: 對每個像素點的 R, G, B值進行加權
        ---自認為第三種方法做出來的黑白效果圖像最 "真實".
        */

        //黑白效果
        private Bitmap image_processing3(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Color pixel;
            for (int x = 0; x < W; x++)
            {
                for (int y = 0; y < H; y++)
                {
                    pixel = bitmap1.GetPixel(x, y);
                    int r, g, b, gray = 0;
                    r = pixel.R;
                    g = pixel.G;
                    b = pixel.B;
                    gray = ((int)(0.7 * r) + (int)(0.2 * g) + (int)(0.1 * b));
                    bitmap2.SetPixel(x, y, Color.FromArgb(gray, gray, gray));
                }
            }
            return bitmap2;
        }

        /*
        四. 柔化效果
        原理: 當前像素點與周圍像素點的顏色差距較大時取其平均值.
        */
        //柔化效果
        private Bitmap image_processing4(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Color pixel;
            //高斯模板
            int[] Gauss = { 1, 2, 1, 2, 4, 2, 1, 2, 1 };
            for (int x = 1; x < W - 1; x++)
            {
                for (int y = 1; y < H - 1; y++)
                {
                    int r = 0, g = 0, b = 0;
                    int Index = 0;
                    for (int col = -1; col <= 1; col++)
                        for (int row = -1; row <= 1; row++)
                        {
                            pixel = bitmap1.GetPixel(x + row, y + col);
                            r += pixel.R * Gauss[Index];
                            g += pixel.G * Gauss[Index];
                            b += pixel.B * Gauss[Index];
                            Index++;
                        }
                    r /= 16;
                    g /= 16;
                    b /= 16;
                    //處理顏色值溢出
                    r = r > 255 ? 255 : r;
                    r = r < 0 ? 0 : r;
                    g = g > 255 ? 255 : g;
                    g = g < 0 ? 0 : g;
                    b = b > 255 ? 255 : b;
                    b = b < 0 ? 0 : b;
                    bitmap2.SetPixel(x - 1, y - 1, Color.FromArgb(r, g, b));
                }
            }
            return bitmap2;
        }

        /*
        五.銳化效果
        原理:突出顯示顏色值大(即形成形體邊緣)的像素點.
        */

        //銳化效果
        private Bitmap image_processing5(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Color pixel;
            //拉普拉斯模板
            int[] Laplacian = { -1, -1, -1, -1, 9, -1, -1, -1, -1 };
            for (int x = 1; x < W - 1; x++)
            {
                for (int y = 1; y < H - 1; y++)
                {
                    int r = 0, g = 0, b = 0;
                    int Index = 0;
                    for (int col = -1; col <= 1; col++)
                    {
                        for (int row = -1; row <= 1; row++)
                        {
                            pixel = bitmap1.GetPixel(x + row, y + col); r += pixel.R * Laplacian[Index];
                            g += pixel.G * Laplacian[Index];
                            b += pixel.B * Laplacian[Index];
                            Index++;
                        }
                    }
                    //處理顏色值溢出
                    r = r > 255 ? 255 : r;
                    r = r < 0 ? 0 : r;
                    g = g > 255 ? 255 : g;
                    g = g < 0 ? 0 : g;
                    b = b > 255 ? 255 : b;
                    b = b < 0 ? 0 : b;
                    bitmap2.SetPixel(x - 1, y - 1, Color.FromArgb(r, g, b));
                }
            }
            return bitmap2;
        }

        /*
        六. 霧化效果
        原理: 在圖像中引入一定的隨機值, 打亂圖像中的像素值
        */

        //霧化效果
        private Bitmap image_processing6(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);
            Color pixel;
            for (int x = 1; x < W - 1; x++)
            {
                for (int y = 1; y < H - 1; y++)
                {
                    Random MyRandom = new Random();
                    int k = MyRandom.Next(123456);
                    //像素塊大小
                    int dx = x + k % 19;
                    int dy = y + k % 19;
                    if (dx >= W)
                        dx = W - 1;
                    if (dy >= H)
                        dy = H - 1;
                    pixel = bitmap1.GetPixel(dx, dy);
                    bitmap2.SetPixel(x, y, pixel);
                }
            }
            return bitmap2;
        }

        /*
        七. 光照效果
        原理: 對圖像中的某一范圍內的像素的亮度分別進行處理.
        */

        //光照效果
        private Bitmap image_processing7(string filename)
        {
            Application.DoEvents();

            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);

            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = bitmap1.Clone(new RectangleF(0, 0, W, H), PixelFormat.DontCare);

            //光照中心點
            int cx = W / 2;
            int cy = H / 2;
            //MyCenter圖片中心點，發亮此值會讓強光中心發生偏移
            Point MyCenter = new Point(cx, cy);
            //R強光照射面的半徑，即”光暈”
            int radius = Math.Min(W / 2, H / 2);
            for (int i = W - 1; i >= 1; i--)
            {
                for (int j = H - 1; j >= 1; j--)
                {
                    float MyLength = (float)Math.Sqrt(Math.Pow((i - MyCenter.X), 2) + Math.Pow((j - MyCenter.Y), 2));
                    //如果像素位於”光暈”之內
                    if (MyLength < radius)
                    {
                        Color MyColor = bitmap2.GetPixel(i, j);
                        int R, G, B;
                        //220亮度增加常量，該值越大，光亮度越強
                        float MyPixel = 220.0f * (1.0f - MyLength / radius);
                        R = MyColor.R + (int)MyPixel;
                        R = Math.Max(0, Math.Min(R, 255));
                        G = MyColor.G + (int)MyPixel;
                        G = Math.Max(0, Math.Min(G, 255));
                        B = MyColor.B + (int)MyPixel;
                        B = Math.Max(0, Math.Min(B, 255));
                        //將增亮後的像素值回寫到位圖
                        Color MyNewColor = Color.FromArgb(255, R, G, B);
                        bitmap2.SetPixel(i, j, MyNewColor);
                    }
                }
                //重新繪制圖片, 會有一個光線掃過的效果
                //g.DrawImage(bitmap2, new Rectangle(0, 0, W, H));
            }
            return bitmap2;
        }

        /*
        八.百葉窗效果
        原理:(1).垂直百葉窗效果:
        根據窗口或圖像的高度或寬度和定制的百葉窗顯示條寬度計算百葉窗顯示的條數量 ；
        根據窗口或圖像的高度或寬度定制百葉窗顯示條數量計算百窗顯示的條寬度.
        (2).水平百葉窗效果: 原理同上,只是繪制像素點開始的坐標不同.
        */

        void shutter1()
        {
            try
            {
                Bitmap bitmap1 = (Bitmap)this.pictureBox1.Image.Clone();
                int dw = bitmap1.Width / 30;
                int dh = bitmap1.Height;
                Graphics g = this.pictureBox1.CreateGraphics();
                g.Clear(Color.Gray);
                Point[] MyPoint = new Point[30];
                for (int x = 0; x < 30; x++)
                {
                    MyPoint[x].Y = 0;
                    MyPoint[x].X = x * dw;
                }
                Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);
                for (int i = 0; i < dw; i++)
                {
                    for (int j = 0; j < 30; j++)
                    {
                        for (int k = 0; k < dh; k++)
                        {
                            bitmap2.SetPixel(MyPoint[j].X + i, MyPoint[j].Y + k,
                            bitmap1.GetPixel(MyPoint[j].X + i, MyPoint[j].Y + k));
                        }
                    }
                    this.pictureBox1.Refresh();
                    this.pictureBox1.Image = bitmap2;
                    Thread.Sleep(100);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }

        void shutter2()
        {
            try
            {
                Bitmap bitmap1 = (Bitmap)this.pictureBox1.Image.Clone();
                int dh = bitmap1.Height / 20;   //记录图片的指定高度
                int dw = bitmap1.Width; //记录图片的宽度
                Graphics g = this.pictureBox1.CreateGraphics();
                g.Clear(Color.Gray);
                Point[] MyPoint = new Point[20];    //定义数组
                for (int y = 0; y < 20; y++)    //记录百叶窗各节点的位置
                {
                    MyPoint[y].X = 0;
                    MyPoint[y].Y = y * dh;
                }
                Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height); //实例化Bitmap类
                //通过调用Bitmap对象的SetPixel方法重新设置图像的像素点颜色，从而实现百叶窗效果

                for (int i = 0; i < dh; i++)
                {
                    for (int j = 0; j < 20; j++)
                    {
                        for (int k = 0; k < dw; k++)
                        {
                            bitmap2.SetPixel(MyPoint[j].X + k, MyPoint[j].Y + i, bitmap1.GetPixel(MyPoint[j].X + k, MyPoint[j].Y + i)); //获取当前象素颜色值
                        }
                    }
                    this.pictureBox1.Refresh();
                    this.pictureBox1.Image = bitmap2;
                    Thread.Sleep(100);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }

        /*
        九.馬賽克效果
        原理: 確定圖像的隨機位置點和確定馬賽克塊的大小,然後馬賽克塊圖像覆蓋隨機點即可.
        */

        //馬賽克效果
        private void image_processing9(string filename)
        {
            try
            {
                Bitmap bitmap1 = new Bitmap(filename);
                int W = bitmap1.Width;
                int H = bitmap1.Height;
                Bitmap bitmap2 = new Bitmap(W, H);

                int dw = bitmap1.Width / 50;
                int dh = bitmap1.Height / 50;
                Graphics g = this.pictureBox1.CreateGraphics();
                g.Clear(Color.Gray);
                Point[] MyPoint = new Point[2500];
                for (int x = 0; x < 50; x++)
                    for (int y = 0; y < 50; y++)
                    {
                        MyPoint[x * 50 + y].X = x * dw;
                        MyPoint[x * 50 + y].Y = y * dh;
                    }
                for (int i = 0; i < 10000; i++)
                {
                    Random MyRandom = new Random();
                    int iPos = MyRandom.Next(2500);
                    for (int m = 0; m < dw; m++)
                        for (int n = 0; n < dh; n++)
                        {
                            bitmap2.SetPixel(MyPoint[iPos].X + m, MyPoint[iPos].Y + n, bitmap1.GetPixel(MyPoint[iPos].X + m, MyPoint[iPos].Y + n));
                        }
                    this.pictureBox1.Refresh();
                    this.pictureBox1.Image = bitmap2;
                }
                for (int i = 0; i < 2500; i++)
                    for (int m = 0; m < dw; m++)
                        for (int n = 0; n < dh; n++)
                        {
                            bitmap2.SetPixel(MyPoint[i].X + m, MyPoint[i].Y + n, bitmap1.GetPixel(MyPoint[i].X + m, MyPoint[i].Y + n));
                        }
                this.pictureBox1.Refresh();
                this.pictureBox1.Image = bitmap2;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }

        /*
        十. 油畫效果
        原理: 對圖像中某一范圍內的像素引入隨機值.
        */

        //油畫效果
        private Bitmap image_processing10(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //Bitmap bitmap2 = new Bitmap(W, H);

            //以油畫效果顯示圖像
            Graphics g = this.pictureBox1.CreateGraphics();
            RectangleF rect = new RectangleF(0, 0, W, H);
            Bitmap bitmap2 = bitmap1.Clone(rect, PixelFormat.DontCare);
            //產生隨機數序列
            Random rnd = new Random();
            //取不同的值決定油畫效果的不同程度
            int iModel = 2;
            int i = W - iModel;
            while (i > 1)
            {
                int j = H - iModel;
                while (j > 1)
                {
                    int iPos = rnd.Next(100000) % iModel;
                    //將該點的RGB值設置成附近iModel點之內的任一點
                    Color color = bitmap2.GetPixel(i + iPos, j + iPos);
                    bitmap2.SetPixel(i, j, color);
                    j = j - 1;
                }
                i = i - 1;
            }
            //重新繪制圖像
            g.Clear(Color.White);
            g.DrawImage(bitmap2, new Rectangle(0, 0, W, H));
            return bitmap2;
        }

        /*
        十一: 扭曲效果
        原理: 將圖像縮放為一個非矩形的平等四邊形即可
        */

        //扭曲效果
        private void image_processing11(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            Graphics g = this.pictureBox1.CreateGraphics();

            Size offset = new Size(W++, H++);//設置偏移量
            Rectangle rect = this.pictureBox1.ClientRectangle;
            Point[] points = new Point[3];
            points[0] = new Point(rect.Left + offset.Width, rect.Top + offset.Height);
            points[1] = new Point(rect.Right, rect.Top + offset.Height);
            points[2] = new Point(rect.Left, rect.Bottom - offset.Height);
            g.Clear(Color.White);
            g.DrawImage(bitmap1, points);
        }

        /*
        十二.積木效果
        原理: 對圖像中的各個像素點著重(即加大分像素的顏色值)著色.
        */

        //積木效果
        private Bitmap image_processing12(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //Bitmap bitmap2 = new Bitmap(W, H);

            Graphics g = this.pictureBox1.CreateGraphics();
            //Bitmap bitmap1 = new Bitmap(this.BackgroundImage);
            int i, j, iAvg, iPixel;
            Color myColor, myNewColor;
            RectangleF myRect;
            myRect = new RectangleF(0, 0, W, H);
            Bitmap bitmap2 = bitmap1.Clone(myRect, PixelFormat.DontCare);
            i = 0;
            while (i < W - 1)
            {
                j = 0;
                while (j < H - 1)
                {
                    myColor = bitmap2.GetPixel(i, j);
                    iAvg = (myColor.R + myColor.G + myColor.B) / 3;
                    iPixel = 0;
                    if (iAvg >= 128)
                        iPixel = 255;
                    else
                        iPixel = 0;
                    myNewColor = Color.FromArgb(255, iPixel, iPixel, iPixel);
                    bitmap2.SetPixel(i, j, myNewColor);
                    j = j + 1;
                }
                i = i + 1;
            }
            g.Clear(Color.WhiteSmoke);
            g.DrawImage(bitmap2, new Rectangle(0, 0, W, H));
            return bitmap2;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = image_processing13(filename);
        }

        private void button15_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image;

            //推拉效果顯示圖像
            image = Image.FromFile(filename);
            pictureBox1.Image = image;
            pictureBox1.Size = new Size(image.Width, image.Height - 1);

            try
            {
                Graphics g = this.pictureBox1.CreateGraphics();
                Bitmap bitmap1 = new Bitmap(image);
                g.Clear(this.pictureBox1.BackColor);
                for (int i = 0; i < this.pictureBox1.Height; i++)
                {
                    Rectangle rectangle1 = new Rectangle(0, 0, this.pictureBox1.Width, i);
                    Rectangle rectangle2 = new Rectangle(0, this.pictureBox1.Height - i, this.pictureBox1.Width, i + 1);
                    Bitmap cloneBitmap = bitmap1.Clone(rectangle2, PixelFormat.DontCare);
                    g.DrawImage(cloneBitmap, rectangle1);
                    this.pictureBox1.Show();
                }
            }
            catch { }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //水平交錯效果顯示圖像
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
            pictureBox1.Size = new Size(bitmap1.Width, bitmap1.Height);

            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = LevelInterleaving(bitmap1);
        }

        Bitmap LevelInterleaving(Bitmap bitmap1)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.WhiteSmoke);
            Bitmap bitmap2 = new Bitmap(W, H);
            int i = 0;
            while (i <= W / 2)
            {
                for (int m = 0; m <= H - 1; m++)
                {
                    bitmap2.SetPixel(i, m, bitmap1.GetPixel(i, m));
                }
                for (int n = 0; n <= H - 1; n++)
                {
                    bitmap2.SetPixel(W - i - 1, n, bitmap1.GetPixel(W - i - 1, n));
                }
                i++;
                this.Refresh();
                this.pictureBox1.Image = bitmap2;
                Thread.Sleep(10);
            }
            return bitmap2;
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //垂直交錯效果顯示圖像
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
            pictureBox1.Size = new Size(bitmap1.Width, bitmap1.Height);
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = UprightnessInterleaving(bitmap1);
        }

        Bitmap UprightnessInterleaving(Bitmap bitmap1)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.WhiteSmoke);
            Bitmap bitmap2 = new Bitmap(W, H);
            int i = 0;
            while (i <= H / 2)
            {
                for (int m = 0; m <= W - 1; m++)
                {
                    bitmap2.SetPixel(m, i, bitmap1.GetPixel(m, i));
                }
                for (int n = 0; n <= W - 1; n++)
                {
                    bitmap2.SetPixel(n, H - i - 1, bitmap1.GetPixel(n, H - i - 1));
                }
                i++;
                this.Refresh();
                pictureBox1.Image = bitmap2;
                Thread.Sleep(10);
            }
            return bitmap2;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = image_processing14(filename);
        }

        private Bitmap image_processing14(string filename)
        {
            //圖片的扭曲（Twist）作法
            Bitmap bitmap1 = new Bitmap(filename);

            //參數設定
            System.Random oRandom = new System.Random();
            int iAmplitude = oRandom.Next(5, 10);	//振幅
            int iFrequency = oRandom.Next(30, 60);	//頻率
            //複製一個失真前的Bitmap過來參考
            Bitmap bitmap2 = (Bitmap)bitmap1.Clone();
            for (int y = 0; y < bitmap1.Height; y++)
            {
                for (int x = 0; x < bitmap1.Width; x++)
                {
                    int newX = (int)(x + (iAmplitude * System.Math.Sin(System.Math.PI * y / iFrequency)));
                    int newY = (int)(y + (iAmplitude * System.Math.Cos(System.Math.PI * x / iFrequency)));
                    if (newX < 0 || newX >= bitmap1.Width) newX = 0;
                    if (newY < 0 || newY >= bitmap1.Height) newY = 0;
                    bitmap1.SetPixel(x, y, bitmap2.GetPixel(newX, newY));
                }
            }
            //參考後丟棄，bitmap1為最終圖案
            bitmap2.Dispose();
            return bitmap1;
        }

        private Bitmap image_processing13(string filename)
        {
            return BassoRelievo(new Bitmap(filename));
        }

        Bitmap BassoRelievo(Bitmap bmp)
        {
            try
            {
                for (int i = 0; i < bmp.Width - 1; i++)
                {
                    for (int j = 0; j < bmp.Height - 1; j++)
                    {
                        Color Color1 = bmp.GetPixel(i, j);
                        Color Color2 = bmp.GetPixel(i + 1, j + 1);
                        int red = Math.Abs(Color1.R - Color2.R + 128);
                        int green = Math.Abs(Color1.G - Color2.G + 128);
                        int blue = Math.Abs(Color1.B - Color2.B + 128);
                        //顏色處理
                        if (red > 255) red = 255;
                        if (red < 0) red = 0;

                        if (green > 255) green = 255;
                        if (green < 0) green = 0;

                        if (blue > 255) blue = 255;
                        if (blue < 0) blue = 0;
                        bmp.SetPixel(i, j, Color.FromArgb(red, green, blue));
                    }
                }
            }
            catch { }

            return bmp;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //色階調整
            pictureBox1.Image = image_processing15(filename);
        }

        private Bitmap image_processing15(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = img_color_gradation(bitmap1, 0, 100, 0);
            return bitmap2;
        }

        //色階調整
        public static unsafe Bitmap img_color_gradation(Bitmap src, int r, int g, int b)
        {
            int width = src.Width;
            int height = src.Height;
            Bitmap back = new Bitmap(width, height);
            Rectangle rect = new Rectangle(0, 0, width, height);
            //這種速度最快  
            BitmapData bmpData = src.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);//24位rgb顯示一個像素，即一個像素點3個字節，每個字節是BGR分量。Format32bppRgb是用4個字節表示一個像素  
            byte* ptr = (byte*)(bmpData.Scan0);
            for (int j = 0; j < height; j++)
            {
                for (int i = 0; i < width; i++)
                {
                    //ptr[2]爲r值，ptr[1]爲g值，ptr[0]爲b值  
                    int red = ptr[2] + r; if (red > 255) red = 255; if (red < 0) red = 0;
                    int green = ptr[1] + g; if (green > 255) green = 255; if (green < 0) green = 0;
                    int blue = ptr[0] + b; if (blue > 255) blue = 255; if (blue < 0) blue = 0;
                    back.SetPixel(i, j, Color.FromArgb(red, green, blue));
                    ptr += 3; //Format24bppRgb格式每個像素佔3字節  
                }
                ptr += bmpData.Stride - bmpData.Width * 3;//每行讀取到最後“有用”數據時，跳過未使用空間XX  
            }
            src.UnlockBits(bmpData);
            return back;
        }

        //馬賽克效果1 ST
        private void button20_Click(object sender, EventArgs e)
        {
            //馬賽克效果1
            pictureBox1.Image = image_processing16(filename);
        }

        int borderwidth = 1;
        int mosaicwidth = 3;
        Color bordercolor = Color.FromArgb(211, 172, 158);
        private Bitmap image_processing16(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = CreateMosaicImage(bitmap1);
            return bitmap2;
        }

        //重設大小
        public Bitmap Resize(Bitmap source, Size size)
        {
            int widthskip = source.Width / size.Width;
            int heightskip = source.Height / size.Height;

            Bitmap bmp = new Bitmap(size.Width, size.Height);

            PointBitmap pbmp = new PointBitmap(source);
            PointBitmap newpbmp = new PointBitmap(bmp);

            pbmp.LockBits();
            newpbmp.LockBits();

            for (int height = 0; height < newpbmp.Height; height++)
            {
                for (int width = 0; width < newpbmp.Width; width++)
                {
                    int x = width > 0 ? 1 + (width - 1) * widthskip : 0;
                    int y = height > 0 ? 1 + (height - 1) * heightskip : 0;
                    Color c = pbmp.GetPixel(x, y);
                    newpbmp.SetPixel(width, height, c);
                }
            }

            pbmp.UnlockBits();
            newpbmp.UnlockBits();

            return bmp;
        }

        //生成马赛克图像
        public Bitmap CreateMosaicImage(Bitmap source)
        {
            //计算新图像需要的尺寸
            int widthcount = source.Width / mosaicwidth;
            int heightcount = source.Height / mosaicwidth;

            int newwidth = widthcount * mosaicwidth + (widthcount + 1) * borderwidth;
            int newheight = heightcount * mosaicwidth + (heightcount + 1) * borderwidth;

            Bitmap bmp = new Bitmap(newwidth, newheight);
            source = Resize(source, new Size(widthcount, heightcount));

            PointBitmap sourcepbmp = new PointBitmap(source);
            PointBitmap newpbmp = new PointBitmap(bmp);
            sourcepbmp.LockBits();
            newpbmp.LockBits();

            //绘制背景
            for (int height = 0; height < newpbmp.Height; height++)
            {
                for (int width = 0; width < newpbmp.Width; width++)
                {
                    newpbmp.SetPixel(width, height, bordercolor);
                }
            }

            for (int height = 0; height < sourcepbmp.Height; height++)
            {
                for (int width = 0; width < sourcepbmp.Width; width++)
                {
                    int x = borderwidth * (width + 1) + mosaicwidth * width;
                    int y = borderwidth * (height + 1) + mosaicwidth * height;

                    Color c = sourcepbmp.GetPixel(width, height);

                    for (int k = 0; k < mosaicwidth; k++, y++, x -= mosaicwidth)
                    {
                        for (int l = 0; l < mosaicwidth; l++, x++)
                        {
                            newpbmp.SetPixel(x, y, c);
                        }
                    }
                }
            }
            sourcepbmp.UnlockBits();
            newpbmp.UnlockBits();
            return bmp;
        }
        //馬賽克效果1 SP

        //馬賽克效果2 ST
        private void button21_Click(object sender, EventArgs e)
        {
            //馬賽克效果2
            pictureBox1.Image = image_processing17(filename);
        }

        private Bitmap image_processing17(string filename)
        {
            //C#處理數碼相片之馬賽克的實現
            Bitmap bitmap1 = new Bitmap(filename);
            int val = 10;
            Bitmap bitmap2 = KiMosaic(bitmap1, val);
            return bitmap2;
        }

        //馬賽克算法很簡單，說白了就是把一張圖片分割成若干個val * val像素的小區塊（可能在邊緣有零星的小塊，但不影響整體算法），每個小區塊的顏色都是相同的。
        public static Bitmap KiMosaic(Bitmap b, int val)
        {
            if (b.Equals(null))
            {
                return null;
            }
            int w = b.Width;
            int h = b.Height;
            int stdR, stdG, stdB;
            stdR = 0;
            stdG = 0;
            stdB = 0;
            BitmapData srcData = b.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            unsafe
            {
                byte* p = (byte*)srcData.Scan0.ToPointer();
                for (int y = 0; y < h; y++)
                {
                    for (int x = 0; x < w; x++)
                    {
                        if (y % val == 0)
                        {
                            if (x % val == 0)
                            {
                                stdR = p[2]; stdG = p[1]; stdB = p[0];
                            }
                            else
                            {
                                p[0] = (byte)stdB;
                                p[1] = (byte)stdG;
                                p[2] = (byte)stdR;
                            }
                        }
                        else
                        {
                            // 復制上一行
                            byte* pTemp = p - srcData.Stride;
                            p[0] = (byte)pTemp[0];
                            p[1] = (byte)pTemp[1];
                            p[2] = (byte)pTemp[2];
                        }
                        p += 3;
                    } // end of x
                    p += srcData.Stride - w * 3;
                } // end of y
                b.UnlockBits(srcData);
            }
            return b;
        }
        //馬賽克效果2 SP

        private void button22_Click(object sender, EventArgs e)
        {
            //圖像邊緣提取1
            //圖像邊緣提取
            /*
用到的算法是robert算子，這是一種比較簡單的算法：
f(x,y)=sqrt((g(x,y)-g(x+1,y+1))^2+(g(x+1,y)-g(x,y+1))^2)
*/

            //圖像邊緣提取
            Image_Test();
        }

        private void Image_Test()
        {
            if (pictureBox1.Image != null)
            {
                int W = pictureBox1.Image.Width;
                int H = pictureBox1.Image.Height;
                Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
                Bitmap bitmap2 = new Bitmap(W, H, PixelFormat.Format24bppRgb);
                BitmapData bitmapdata1 = bitmap1.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);  //原圖
                BitmapData bitmapdata2 = bitmap2.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);  //新圖即邊緣圖

                unsafe
                {
                    //首先第一段代碼是提取邊緣，邊緣置為黑色，其他部分置為白色
                    byte* pin_1 = (byte*)(bitmapdata1.Scan0.ToPointer());
                    byte* pin_2 = pin_1 + (bitmapdata1.Stride);
                    byte* pout = (byte*)(bitmapdata2.Scan0.ToPointer());
                    for (int y = 0; y < bitmapdata1.Height - 1; y++)
                    {
                        for (int x = 0; x < bitmapdata1.Width; x++)
                        {
                            //使用robert算子
                            double b = System.Math.Sqrt(((double)pin_1[0] - (double)(pin_2[0] + 3)) * ((double)pin_1[0] - (double)(pin_2[0] + 3)) + ((double)(pin_1[0] + 3) - (double)pin_2[0]) * ((double)(pin_1[0] + 3) - (double)pin_2[0]));
                            double g = System.Math.Sqrt(((double)pin_1[1] - (double)(pin_2[1] + 3)) * ((double)pin_1[1] - (double)(pin_2[1] + 3)) + ((double)(pin_1[1] + 3) - (double)pin_2[1]) * ((double)(pin_1[1] + 3) - (double)pin_2[1]));
                            double r = System.Math.Sqrt(((double)pin_1[2] - (double)(pin_2[2] + 3)) * ((double)pin_1[2] - (double)(pin_2[2] + 3)) + ((double)(pin_1[2] + 3) - (double)pin_2[2]) * ((double)(pin_1[2] + 3) - (double)pin_2[2]));
                            double bgr = b + g + r;//博主一直在糾結要不要除以3，感覺沒差，選阈值的時候調整一下就好了- -

                            if (bgr > 80) //阈值，超過阈值判定為邊緣（選取適當的阈值）
                            {
                                b = 0;
                                g = 0;
                                r = 0;
                            }
                            else
                            {
                                b = 255;
                                g = 255;
                                r = 255;
                            }
                            pout[0] = (byte)(b);
                            pout[1] = (byte)(g);
                            pout[2] = (byte)(r);
                            pin_1 = pin_1 + 3;
                            pin_2 = pin_2 + 3;
                            pout = pout + 3;

                        }
                        pin_1 += bitmapdata1.Stride - bitmapdata1.Width * 3;
                        pin_2 += bitmapdata1.Stride - bitmapdata1.Width * 3;
                        pout += bitmapdata2.Stride - bitmapdata2.Width * 3;
                    }

                    /*
                    //這裡博主加粗了一下線條- -，不喜歡的同學可以刪了這段代碼
                    byte* pin_5 = (byte*)(bitmapdata2.Scan0.ToPointer());
                    for (int y = 0; y < bitmapdata1.Height - 1; y++)
                    {
                        for (int x = 3; x < bitmapdata1.Width; x++)
                        {
                            if (pin_5[0] == 0 && pin_5[1] == 0 && pin_5[2] == 0)
                            {
                                pin_5[-3] = 0;
                                pin_5[-2] = 0;
                                pin_5[-1] = 0;      //邊緣點的前一個像素點置為黑色（注意一定要是遍歷過的像素點）                                                    
                            }
                            pin_5 += 3;

                        }
                        pin_5 += bitmapdata2.Stride - bitmapdata2.Width * 3;
                    }
                    */

                    /*
                    //這段代碼是把原圖和邊緣圖重合
                    byte* pin_3 = (byte*)(bitmapdata1.Scan0.ToPointer());
                    byte* pin_4 = (byte*)(bitmapdata2.Scan0.ToPointer());
                    for (int y = 0; y < bitmapdata1.Height - 1; y++)
                    {
                        for (int x = 0; x < bitmapdata1.Width; x++)
                        {
                            if (pin_4[0] == 255 && pin_4[1] == 255 && pin_4[2] == 255)
                            {
                                pin_4[0] = pin_3[0];
                                pin_4[1] = pin_3[1];
                                pin_4[2] = pin_3[2];
                            }
                            pin_3 += 3;
                            pin_4 += 3;
                        }
                        pin_3 += bitmapdata1.Stride - bitmapdata1.Width * 3;
                        pin_4 += bitmapdata2.Stride - bitmapdata2.Width * 3;
                    }
                    */

                    bitmap1.UnlockBits(bitmapdata1);
                    bitmap2.UnlockBits(bitmapdata2);

                    pictureBox1.Image = bitmap2;
                }
            }
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //圖像邊緣提取2
            //圖像邊緣提取2
            //圖像邊緣提取

            /*
            用到的算法是robert算子，這是一種比較簡單的算法：

            f(x,y)=sqrt((g(x,y)-g(x+1,y+1))^2+(g(x+1,y)-g(x,y+1))^2)

            博主一共寫了三段代碼，第一段是邊緣提取，第二段是線條加粗，第三段是原圖和邊緣圖重合，三段代碼可以放在一起，但為了看得清晰我就把他們分開了。
            */

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            if (this.pictureBox1.Image != null)
            {

                int Height = this.pictureBox1.Image.Height;
                int Width = this.pictureBox1.Image.Width;
                Bitmap bitmap = new Bitmap(Width, Height, PixelFormat.Format24bppRgb);
                Bitmap MyBitmap = (Bitmap)this.pictureBox1.Image;
                BitmapData oldData = MyBitmap.LockBits(new Rectangle(0, 0, Width, Height), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb); //原圖
                BitmapData newData = bitmap.LockBits(new Rectangle(0, 0, Width, Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);  //新圖即邊緣圖
                unsafe
                {
                    //首先第一段代碼是提取邊緣，邊緣置為黑色，其他部分置為白色
                    byte* pin_1 = (byte*)(oldData.Scan0.ToPointer());
                    byte* pin_2 = pin_1 + (oldData.Stride);
                    byte* pout = (byte*)(newData.Scan0.ToPointer());
                    for (int y = 0; y < oldData.Height - 1; y++)
                    {
                        for (int x = 0; x < oldData.Width; x++)
                        {
                            //使用robert算子
                            double b = System.Math.Sqrt(((double)pin_1[0] - (double)(pin_2[0] + 3)) * ((double)pin_1[0] - (double)(pin_2[0] + 3)) + ((double)(pin_1[0] + 3) - (double)pin_2[0]) * ((double)(pin_1[0] + 3) - (double)pin_2[0]));
                            double g = System.Math.Sqrt(((double)pin_1[1] - (double)(pin_2[1] + 3)) * ((double)pin_1[1] - (double)(pin_2[1] + 3)) + ((double)(pin_1[1] + 3) - (double)pin_2[1]) * ((double)(pin_1[1] + 3) - (double)pin_2[1]));
                            double r = System.Math.Sqrt(((double)pin_1[2] - (double)(pin_2[2] + 3)) * ((double)pin_1[2] - (double)(pin_2[2] + 3)) + ((double)(pin_1[2] + 3) - (double)pin_2[2]) * ((double)(pin_1[2] + 3) - (double)pin_2[2]));
                            double bgr = b + g + r;//博主一直在糾結要不要除以3，感覺沒差，選阈值的時候調整一下就好了- -

                            if (bgr > 80) //阈值，超過阈值判定為邊緣（選取適當的阈值）
                            {
                                b = 0;
                                g = 0;
                                r = 0;
                            }
                            else
                            {
                                b = 255;
                                g = 255;
                                r = 255;
                            }
                            pout[0] = (byte)(b);
                            pout[1] = (byte)(g);
                            pout[2] = (byte)(r);
                            pin_1 = pin_1 + 3;
                            pin_2 = pin_2 + 3;
                            pout = pout + 3;

                        }
                        pin_1 += oldData.Stride - oldData.Width * 3;
                        pin_2 += oldData.Stride - oldData.Width * 3;
                        pout += newData.Stride - newData.Width * 3;
                    }

                    //這裡博主加粗了一下線條- -，不喜歡的同學可以刪了這段代碼
                    byte* pin_5 = (byte*)(newData.Scan0.ToPointer());
                    for (int y = 0; y < oldData.Height - 1; y++)
                    {
                        for (int x = 3; x < oldData.Width; x++)
                        {
                            if (pin_5[0] == 0 && pin_5[1] == 0 && pin_5[2] == 0)
                            {
                                pin_5[-3] = 0;
                                pin_5[-2] = 0;
                                pin_5[-1] = 0;      //邊緣點的前一個像素點置為黑色（注意一定要是遍歷過的像素點）                                                    
                            }
                            pin_5 += 3;

                        }
                        pin_5 += newData.Stride - newData.Width * 3;
                    }

                    //這段代碼是把原圖和邊緣圖重合
                    byte* pin_3 = (byte*)(oldData.Scan0.ToPointer());
                    byte* pin_4 = (byte*)(newData.Scan0.ToPointer());
                    for (int y = 0; y < oldData.Height - 1; y++)
                    {
                        for (int x = 0; x < oldData.Width; x++)
                        {
                            if (pin_4[0] == 255 && pin_4[1] == 255 && pin_4[2] == 255)
                            {
                                pin_4[0] = pin_3[0];
                                pin_4[1] = pin_3[1];
                                pin_4[2] = pin_3[2];
                            }
                            pin_3 += 3;
                            pin_4 += 3;
                        }
                        pin_3 += oldData.Stride - oldData.Width * 3;
                        pin_4 += newData.Stride - newData.Width * 3;
                    }
                    //......
                    bitmap.UnlockBits(newData);
                    MyBitmap.UnlockBits(oldData);
                    this.pictureBox1.Image = bitmap;
                }
            }
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //降低解析度

            Bitmap bitmap1 = new Bitmap(filename, true);

            int x, y;

            // Loop through the images pixels to reset color.
            for (x = 0; x < bitmap1.Width; x++)
            {
                for (y = 0; y < bitmap1.Height; y++)
                {
                    Color pixelColor = bitmap1.GetPixel(x, y);
                    //Color newColor = Color.FromArgb(pixelColor.R, 0, 0);
                    //Color newColor = Color.FromArgb(0, pixelColor.G, 0);
                    byte newColor_r = (byte)((pixelColor.R / 20) * 20);
                    byte newColor_g = (byte)((pixelColor.G / 20) * 20);
                    byte newColor_b = (byte)((pixelColor.B / 20) * 20);

                    Color newColor = Color.FromArgb(newColor_r, newColor_g, newColor_b);

                    bitmap1.SetPixel(x, y, newColor);
                }
            }

            // Set the PictureBox to display the image.
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "圖片大小 " + bitmap1.Width.ToString() + " X " + bitmap1.Height.ToString() + "\n";

            // Display the pixel format in Label1.
            richTextBox1.Text += "Pixel format: " + bitmap1.PixelFormat.ToString() + "\n";
        }

        //光暈效果 ST
        public Image pp(PictureBox Pict, int x, int y, int R, float better) //R強光照射面的半徑，即"光暈"
        {
            Bitmap bitmap1 = new Bitmap(Pict.Image, Pict.Image.Width, Pict.Image.Height);//根據圖像實例化Bitmap類

            int W = bitmap1.Width;//獲取圖像的寬度
            int H = bitmap1.Height;//獲取圖像的高度
            //定義一個Bitmap類的復本
            Bitmap Var_SaveBmp = bitmap1.Clone(new RectangleF(0, 0, W, H), PixelFormat.DontCare);
            Point Var_Center = new Point(x, y);//光暈的中心點
            //遍歷圖像中的各象素
            for (int i = W - 1; i >= 1; i--)
            {
                for (int j = H - 1; j >= 1; j--)
                {
                    float Var_Length = (float)Math.Sqrt(Math.Pow((i - Var_Center.X), 2) + Math.Pow((j - Var_Center.Y), 2));//設置光暈的範圍
                    //如果像素位於」光暈」之內
                    if (Var_Length < R)
                    {
                        Color Var_Color = Var_SaveBmp.GetPixel(i, j);
                        int r, g, b;
                        float Var_Pixel = better * (1.0f - Var_Length / R);//設置光亮度的強弱
                        r = Var_Color.R + (int)Var_Pixel;//設置加強後的R值
                        r = Math.Max(0, Math.Min(r, 255));//如果R值不在顏色值的範圍內，對R值進行設置
                        g = Var_Color.G + (int)Var_Pixel;//設置加強後的G值
                        g = Math.Max(0, Math.Min(g, 255));//如果G值不在顏色值的範圍內，對G值進行設置
                        b = Var_Color.B + (int)Var_Pixel;//設置加強後的B值
                        b = Math.Max(0, Math.Min(b, 255));//如果B值不在顏色值的範圍內，對B值進行設置
                        Var_SaveBmp.SetPixel(i, j, Color.FromArgb(255, r, g, b));//將增亮後的像素值回寫到位圖
                    }
                }
            }
            return Var_SaveBmp;
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //光暈效果
            int cx = 50;
            int cy = 50;
            int R = 100;
            pictureBox1.Image = pp(pictureBox1, cx, cy, R, 150F);
        }
        //光暈效果 SP

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {
            //積木效果
            Bitmap bmp = new Bitmap(filename);
            pictureBox1.Image = ToBlock(bmp);
        }

        Bitmap ToBlock(Bitmap bitmap1)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            int W, H, i, j, iAvg, iPixel;
            Color myColor, myNewColor;
            RectangleF myRect;
            W = bitmap1.Width;
            H = bitmap1.Height;
            myRect = new RectangleF(0, 0, W, H);
            Bitmap bitmap = bitmap1.Clone(myRect, System.Drawing.Imaging.PixelFormat.DontCare);
            i = 0;
            while (i < W - 1)
            {
                j = 0;
                while (j < H - 1)
                {
                    myColor = bitmap.GetPixel(i, j);
                    iAvg = (myColor.R + myColor.G + myColor.B) / 3;
                    iPixel = 0;
                    if (iAvg >= 128)
                        iPixel = 255;
                    else
                        iPixel = 0;
                    myNewColor = Color.FromArgb(255, iPixel, iPixel, iPixel);
                    bitmap.SetPixel(i, j, myNewColor);
                    j = j + 1;
                }
                i = i + 1;
            }
            g.Clear(Color.WhiteSmoke);
            g.DrawImage(bitmap, new Rectangle(0, 0, W, H));

            return bitmap;
        }


        private void button29_Click(object sender, EventArgs e)
        {

        }

        private void button30_Click(object sender, EventArgs e)
        {

        }

        private void button31_Click(object sender, EventArgs e)
        {
            //關掉所有控件 
            remove_all_controls();

            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;
            int w = W * 7 / 10;
            int h = H * 7 / 10;
            pictureBox1.Size = new Size(w, h);
            pictureBox1.Location = new Point((W - w) / 2, (H - h) / 2);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            timer1.Enabled = true;
        }

        void remove_all_controls()
        {
            //richTextBox1.Text += "遍歷所有控件\n";
            int i;

            for (i = 0; i < 10; i++)
            {
                foreach (Control con in this.Controls)
                {
                    System.String strControl = con.GetType().ToString();//获得控件的类型
                    System.String strControlName = con.Name.ToString();//获得控件的名称

                    richTextBox1.Text += "Type\t" + strControl + "\tName\t" + strControlName + "\n";

                    if (strControlName == "pictureBox1")
                        continue;
                    if (strControlName == "bt_exit")
                        continue;

                    this.Controls.Remove(con);
                }
            }
        }

        int item = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            item++;
            switch (item)
            {
                case 1: pictureBox1.Image = image_processing1(filename); break;
                case 2: pictureBox1.Image = image_processing2(filename); break;
                case 3: pictureBox1.Image = image_processing3(filename); break;
                case 4: pictureBox1.Image = image_processing4(filename); break;
                case 5: pictureBox1.Image = image_processing5(filename); break;
                case 6: pictureBox1.Image = image_processing6(filename); break;
                case 7: pictureBox1.Image = image_processing7(filename); break;
                //case 8: pictureBox1.Image = image_processing8(filename); break;
                //case 9: pictureBox1.Image = image_processing9(filename); break;
                case 10: pictureBox1.Image = image_processing10(filename); break;
                //case 11: pictureBox1.Image = image_processing11(filename); break;
                case 12: pictureBox1.Image = image_processing12(filename); break;
                case 13: pictureBox1.Image = image_processing13(filename); break;
                case 14: pictureBox1.Image = image_processing14(filename); break;
                case 15: pictureBox1.Image = image_processing15(filename); break;
                case 16: pictureBox1.Image = image_processing16(filename); break;
                case 17: pictureBox1.Image = image_processing17(filename); break;
                case 18: shutter1(); break;
                case 19: shutter2(); break;
                default: break;
            }
            if (item >= 19)
            {
                item = 0;
            }
        }

        private void bt_edge_detection0_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            sw.Reset();
            sw.Start();
            Bitmap bitmap2 = Roberts(bitmap1);
            sw.Stop();
            pictureBox1.Image = bitmap2;
            richTextBox1.Text += "Roberts 耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
        }

        private void bt_edge_detection1_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            sw.Reset();
            sw.Start();
            Bitmap bitmap2 = Sobel(bitmap1);
            sw.Stop();
            pictureBox1.Image = bitmap2;
            richTextBox1.Text += "Sobel 耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
        }

        private void bt_edge_detection2_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            sw.Reset();
            sw.Start();
            Bitmap bitmap2 = Laplace4(bitmap1);
            Bitmap bitmap3 = Laplace8(bitmap1);
            sw.Stop();

            pictureBox1.Image = bitmap2;
            pictureBox1.Image = bitmap3;
            richTextBox1.Text += "Laplace 耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
        }

        private void bt_edge_detection3_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            sw.Reset();
            sw.Start();
            Bitmap bitmap2 = RightBottomEdge(bitmap1);
            sw.Stop();
            pictureBox1.Image = bitmap2;
            richTextBox1.Text += "RightBottomEdge 耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
        }

        private void bt_edge_detection4_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            sw.Reset();
            sw.Start();
            Bitmap bitmap2 = Prewitt(bitmap1);
            sw.Stop();
            pictureBox1.Image = bitmap2;
            richTextBox1.Text += "Prewitt 耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
        }

        private void bt_edge_detection5_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            sw.Reset();
            sw.Start();
            Bitmap bitmap2 = Robinson(bitmap1);
            sw.Stop();
            pictureBox1.Image = bitmap2;
            richTextBox1.Text += "Robinson 耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
        }

        private void bt_edge_detection6_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            sw.Reset();
            sw.Start();
            Bitmap bitmap2 = Kirsch(bitmap1);
            sw.Stop();
            pictureBox1.Image = bitmap2;
            richTextBox1.Text += "Kirsch 耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
        }

        private void bt_edge_detection7_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            sw.Reset();
            sw.Start();
            Bitmap bitmap2 = Smoothed(bitmap1);
            sw.Stop();
            pictureBox1.Image = bitmap2;
            richTextBox1.Text += "Smoothed 耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
        }

        //Roberts算子
        //  gx = f(i,j) - f(i+1,j)
        //  gy = f(i+1,j) - f(i,j+1)
        //  g(i,j) = abs(gx) + abs(gy)
        private Bitmap Roberts(Bitmap bitmap1)
        {
            Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);

            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            for (int i = 0; i < bitmap1.Width - 1; i++)
            {
                for (int j = 0; j < bitmap1.Height - 1; j++)
                {
                    Color c1 = lockBitmap1.GetPixel(i, j);
                    Color c2 = lockBitmap1.GetPixel(i + 1, j);
                    Color c3 = lockBitmap1.GetPixel(i, j + 1);
                    Color c4 = lockBitmap1.GetPixel(i + 1, j + 1);

                    int r = Math.Abs(c1.R - c4.R) + Math.Abs(c2.R - c3.R);
                    int g = Math.Abs(c1.G - c4.G) + Math.Abs(c2.G - c3.G);
                    int b = Math.Abs(c1.B - c4.B) + Math.Abs(c2.B - c3.B);

                    if (r > 255) r = 255;
                    if (g > 255) g = 255;
                    if (b > 255) b = 255;

                    lockBitmap2.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();

            return bitmap2;
        }


        //Sobel算子
        //  gx = f(i-1,j-1) + 2f(i-1,j) + f(i-1,j+1) - f(i+1,j-1) - 2f(i+1,j) - f(i+1,j+1)
        //  gy = f(i-1,j-1) + 2f(i,j-1) + f(i+1,j-1) - f(i-1,j+1) - 2f(i,j+1) - f(i+1,j+1)
        //  g(i,j) = gx + gy
        private Bitmap Sobel(Bitmap bitmap1)
        {
            Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);

            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            for (int i = 1; i < bitmap1.Width - 1; i++)
            {
                for (int j = 1; j < bitmap1.Height - 1; j++)
                {
                    Color c1 = lockBitmap1.GetPixel(i - 1, j - 1);
                    Color c2 = lockBitmap1.GetPixel(i, j - 1);
                    Color c3 = lockBitmap1.GetPixel(i + 1, j - 1);
                    Color c4 = lockBitmap1.GetPixel(i - 1, j);
                    Color c6 = lockBitmap1.GetPixel(i + 1, j);
                    Color c7 = lockBitmap1.GetPixel(i - 1, j + 1);
                    Color c8 = lockBitmap1.GetPixel(i, j + 1);
                    Color c9 = lockBitmap1.GetPixel(i + 1, j + 1);

                    int r1 = c1.R + 2 * c4.R + c7.R - c3.R - 2 * c6.R - c9.R;
                    int r2 = c1.R + 2 * c2.R + c3.R - c7.R - 2 * c8.R - c9.R;
                    int g1 = c1.G + 2 * c4.G + c7.G - c3.G - 2 * c6.G - c9.G;
                    int g2 = c1.G + 2 * c2.G + c3.G - c7.G - 2 * c8.G - c9.G;
                    int b1 = c1.B + 2 * c4.B + c7.B - c3.B - 2 * c6.B - c9.B;
                    int b2 = c1.B + 2 * c2.B + c3.B - c7.B - 2 * c8.B - c9.B;

                    int r = Math.Abs(r1) + Math.Abs(r2);
                    int g = Math.Abs(g1) + Math.Abs(g2);
                    int b = Math.Abs(b1) + Math.Abs(b2);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    lockBitmap2.SetPixel(i, j, Color.FromArgb(r, g, b));
                    //lockBitmap2.SetPixel(i, j, Color.FromArgb(r, r, r));
                }
            }

            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();

            return bitmap2;
        }


        //拉普拉斯算子（四邻域）
        //  g(i,j) = abs(4f(i,j) - f(i,j-1) - f(i,j+1) - f(i-1,j) - f(i+1,j))
        private Bitmap Laplace4(Bitmap bitmap1)
        {
            Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);

            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            for (int i = 1; i < bitmap1.Width - 1; i++)
            {
                for (int j = 1; j < bitmap1.Height - 1; j++)
                {
                    Color c2 = lockBitmap1.GetPixel(i, j - 1);
                    Color c4 = lockBitmap1.GetPixel(i - 1, j);
                    Color c5 = lockBitmap1.GetPixel(i, j);
                    Color c6 = lockBitmap1.GetPixel(i + 1, j);
                    Color c8 = lockBitmap1.GetPixel(i, j + 1);

                    int r = Math.Abs(4 * c5.R - c2.R - c4.R - c6.R - c8.R);
                    int g = Math.Abs(4 * c5.G - c2.G - c4.G - c6.G - c8.G);
                    int b = Math.Abs(4 * c5.B - c2.B - c4.B - c6.B - c8.B);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    lockBitmap2.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();

            return bitmap2;
        }

        private Bitmap Laplace8(Bitmap bitmap1)
        {
            Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);

            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            for (int i = 1; i < bitmap1.Width - 1; i++)
            {
                for (int j = 1; j < bitmap1.Height - 1; j++)
                {
                    Color c1 = lockBitmap1.GetPixel(i - 1, j - 1);
                    Color c2 = lockBitmap1.GetPixel(i, j - 1);
                    Color c3 = lockBitmap1.GetPixel(i + 1, j - 1);
                    Color c4 = lockBitmap1.GetPixel(i - 1, j);
                    Color c5 = lockBitmap1.GetPixel(i, j);
                    Color c6 = lockBitmap1.GetPixel(i + 1, j);
                    Color c7 = lockBitmap1.GetPixel(i - 1, j + 1);
                    Color c8 = lockBitmap1.GetPixel(i, j + 1);
                    Color c9 = lockBitmap1.GetPixel(i + 1, j + 1);

                    int r = Math.Abs(8 * c5.R - c1.R - c2.R - c3.R - c4.R - c6.R - c7.R - c8.R - c9.R);
                    int g = Math.Abs(8 * c5.G - c1.G - c2.G - c3.G - c4.G - c6.G - c7.G - c8.G - c9.G);
                    int b = Math.Abs(8 * c5.B - c1.B - c2.B - c3.B - c4.B - c6.B - c7.B - c8.B - c9.B);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    lockBitmap2.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();

            return bitmap2;
        }


        //右下边缘抽出
        //  g(i,j) = abs(2f(i+1,j) + 2f(i,j+1) - 2f(i,j-1) - 2f(i-1,j));
        private Bitmap RightBottomEdge(Bitmap bitmap1)
        {
            Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);

            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            for (int i = 1; i < bitmap1.Width - 1; i++)
            {
                for (int j = 1; j < bitmap1.Height - 1; j++)
                {
                    Color c2 = lockBitmap1.GetPixel(i, j - 1);
                    Color c4 = lockBitmap1.GetPixel(i - 1, j);
                    Color c6 = lockBitmap1.GetPixel(i + 1, j);
                    Color c8 = lockBitmap1.GetPixel(i, j + 1);

                    int r = 2 * Math.Abs(c6.R + c8.R - c2.R - c4.R);
                    int g = 2 * Math.Abs(c6.G + c8.G - c2.G - c4.G);
                    int b = 2 * Math.Abs(c6.B + c8.B - c2.B - c4.B);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    lockBitmap2.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();

            return bitmap2;
        }


        //Prewitt边缘检测样板算子（方向为右下）
        //  g(i,j) = abs(f(i-1,j-1) + f(i,j-1) + f(i+1,j-1) + f(i-1,j) + f(i-1,j+1) - f(i+1,j) - f(i,j+1) - f(i+1,j+1) - 2f(i,j))
        //
        //      右下              右上
        //  1   1   1           1   -1  -1
        //  1   -2  -1          1   -2  -1
        //  1   -1  -1          1   1   1
        //
        //      上               下
        //  -1  -1  -1          1   1   1
        //  1   -2  1           1   -2  1
        //  1   1   1           -1  -1  -1
        private Bitmap Prewitt(Bitmap bitmap1)
        {
            Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);

            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            for (int i = 1; i < bitmap1.Width - 1; i++)
            {
                for (int j = 1; j < bitmap1.Height - 1; j++)
                {
                    Color c1 = lockBitmap1.GetPixel(i - 1, j - 1);
                    Color c2 = lockBitmap1.GetPixel(i, j - 1);
                    Color c3 = lockBitmap1.GetPixel(i + 1, j - 1);
                    Color c4 = lockBitmap1.GetPixel(i - 1, j);
                    Color c5 = lockBitmap1.GetPixel(i, j);
                    Color c6 = lockBitmap1.GetPixel(i + 1, j);
                    Color c7 = lockBitmap1.GetPixel(i - 1, j + 1);
                    Color c8 = lockBitmap1.GetPixel(i, j + 1);
                    Color c9 = lockBitmap1.GetPixel(i + 1, j + 1);

                    int r = Math.Abs(c1.R + c2.R + c3.R + c4.R + c7.R - c6.R - c8.R - c9.R - 2 * c5.R);
                    int g = Math.Abs(c1.G + c2.G + c3.G + c4.G + c7.G - c6.G - c8.G - c9.G - 2 * c5.R);
                    int b = Math.Abs(c1.B + c2.B + c3.B + c4.B + c7.B - c6.B - c8.B - c9.B - 2 * c5.R);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    lockBitmap2.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();

            return bitmap2;
        }


        //Robinson算子（这里使用第一个）
        //Robinson算子有八个样板，这里列出四个，剩余四个为下面四个的取反
        //
        //  1   2   1               0   1   2
        //  0   0   0               -1  0   1
        //  -1  -2  -1              -2  -1  0
        //
        //  -1  0   1               -2  -1  0
        //  -2  0   2               -1  0   1
        //  -1  0   1               0   -1  2
        private Bitmap Robinson(Bitmap bitmap1)
        {
            Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);

            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            for (int i = 1; i < bitmap1.Width - 1; i++)
            {
                for (int j = 1; j < bitmap1.Height - 1; j++)
                {
                    Color c1 = lockBitmap1.GetPixel(i - 1, j - 1);
                    Color c2 = lockBitmap1.GetPixel(i, j - 1);
                    Color c3 = lockBitmap1.GetPixel(i + 1, j - 1);
                    Color c7 = lockBitmap1.GetPixel(i - 1, j + 1);
                    Color c8 = lockBitmap1.GetPixel(i, j + 1);
                    Color c9 = lockBitmap1.GetPixel(i + 1, j + 1);

                    int r = Math.Abs(c1.R + 2 * c2.R + c3.R - c7.R - 2 * c8.R - c9.R);
                    int g = Math.Abs(c1.G + 2 * c2.G + c3.G - c7.G - 2 * c8.G - c9.G);
                    int b = Math.Abs(c1.B + 2 * c2.B + c3.B - c7.B - 2 * c8.B - c9.B);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    lockBitmap2.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();

            return bitmap2;
        }

        //Kirsch算子（这里使用第一个）
        //Kirsch算子有8个边缘样板，与Prewitt边缘样板类似，这里列出一个
        //
        //  5   5   5
        //  -3  0   -3
        //  -3  -3  -3
        //
        private Bitmap Kirsch(Bitmap bitmap1)
        {
            Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);

            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            for (int i = 1; i < bitmap1.Width - 1; i++)
            {
                for (int j = 1; j < bitmap1.Height - 1; j++)
                {
                    Color c1 = lockBitmap1.GetPixel(i - 1, j - 1);
                    Color c2 = lockBitmap1.GetPixel(i, j - 1);
                    Color c3 = lockBitmap1.GetPixel(i + 1, j - 1);
                    Color c4 = lockBitmap1.GetPixel(i - 1, j);
                    Color c6 = lockBitmap1.GetPixel(i + 1, j);
                    Color c7 = lockBitmap1.GetPixel(i - 1, j + 1);
                    Color c8 = lockBitmap1.GetPixel(i, j + 1);
                    Color c9 = lockBitmap1.GetPixel(i + 1, j + 1);

                    int r = Math.Abs(5 * (c1.R + c2.R + c3.R) - 3 * (c4.R + c6.R + c7.R + c8.R + c9.R));
                    int g = Math.Abs(5 * (c1.G + c2.G + c3.G) - 3 * (c4.G + c6.G + c7.G + c8.G + c9.G));
                    int b = Math.Abs(5 * (c1.B + c2.B + c3.B) - 3 * (c4.B + c6.B + c7.B + c8.B + c9.B));

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    lockBitmap2.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();

            return bitmap2;
        }


        //Smoothed算子
        //  gx = f(i,j) - f(i+1,j)
        //  gy = f(i+1,j) - f(i,j+1)
        //  g(i,j) = abs(gx) + abs(gy)
        private Bitmap Smoothed(Bitmap bitmap1)
        {
            Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);

            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            for (int i = 1; i < bitmap1.Width - 1; i++)
            {
                for (int j = 1; j < bitmap1.Height - 1; j++)
                {
                    Color c1 = lockBitmap1.GetPixel(i - 1, j - 1);
                    Color c2 = lockBitmap1.GetPixel(i, j - 1);
                    Color c3 = lockBitmap1.GetPixel(i + 1, j - 1);
                    Color c4 = lockBitmap1.GetPixel(i - 1, j);
                    Color c6 = lockBitmap1.GetPixel(i + 1, j);
                    Color c7 = lockBitmap1.GetPixel(i - 1, j + 1);
                    Color c8 = lockBitmap1.GetPixel(i, j + 1);
                    Color c9 = lockBitmap1.GetPixel(i + 1, j + 1);

                    int r1 = c3.R + c6.R + c9.R - c1.R - c4.R - c7.R;
                    int r2 = c1.R + c2.R + c3.R - c7.R - c8.R - c9.R;

                    int g1 = c3.G + c6.G + c9.G - c1.G - c4.G - c7.G;
                    int g2 = c1.G + c2.G + c3.G - c7.G - c8.G - c9.G;
                    int b1 = c3.B + c6.B + c9.B - c1.B - c4.B - c7.B;
                    int b2 = c1.B + c2.B + c3.B - c7.B - c8.B - c9.B;

                    int r = Math.Abs(r1) + Math.Abs(r2);
                    int g = Math.Abs(g1) + Math.Abs(g2);
                    int b = Math.Abs(b1) + Math.Abs(b2);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    lockBitmap2.SetPixel(i, j, Color.FromArgb(r, g, b));
                    //lockBitmap2.SetPixel(i, j, Color.FromArgb(r, r, r));
                }
            }

            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();

            return bitmap2;
        }

        private void bt_image_process_p0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "黑白效果\n";
            Bitmap bmp = image_processing3(filename);
            pictureBox1.Image = bmp;

        }

        private void bt_image_process_p1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "底片效果\n";
            Bitmap bmp = image_processing1(filename);
            pictureBox1.Image = bmp;

        }

        private void bt_image_process_p2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "浮雕\n";
            Bitmap bmp = image_processing2(filename);
            pictureBox1.Image = bmp;
        }

        private void bt_image_process_p3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "柔化\n";
            Bitmap bmp = image_processing4(filename);
            pictureBox1.Image = bmp;
        }

        private void bt_image_process_p4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "銳化\n";
            Bitmap bmp = image_processing5(filename);
            pictureBox1.Image = bmp;
        }

        private void bt_image_process_p5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "霧化 TBD\n";
            Bitmap bmp = image_processing6(filename);
            pictureBox1.Image = bmp;
        }

        private void bt_image_process_p6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "光照效果\n";
            Bitmap bmp = image_processing7(filename);
            pictureBox1.Image = bmp;
        }

        private void bt_image_process_p7_Click(object sender, EventArgs e)
        {

        }

        private void bt_image_process_m0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "黑白效果\n";
            Bitmap bmp = GrayImage(filename);
            pictureBox1.Image = bmp;

        }

        private void bt_image_process_m1_Click(object sender, EventArgs e)
        {
            //底片效果（反色）（255-r, 255-g, 255-b）
            richTextBox1.Text += "底片效果\n";
            Bitmap bmp = NegativeImage(filename);
            pictureBox1.Image = bmp;

        }

        private void bt_image_process_m2_Click(object sender, EventArgs e)
        {
            //浮雕：找出附近的像素點r1，abs（r-r2+128）

            richTextBox1.Text += "浮雕\n";
            Bitmap bmp = EmbossmentImage(filename);
            pictureBox1.Image = bmp;

        }

        private void bt_image_process_m3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "柔化\n";
            Bitmap bmp = SoftenImage(filename);
            pictureBox1.Image = bmp;

        }

        private void bt_image_process_m4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "銳化\n";
            Bitmap bmp = SharpenImage(filename);
            pictureBox1.Image = bmp;

        }

        private void bt_image_process_m5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "霧化\n";
            Bitmap bmp = AtomizationImage(filename);
            pictureBox1.Image = bmp;

        }

        private void bt_image_process_m6_Click(object sender, EventArgs e)
        {

        }

        private void bt_image_process_m7_Click(object sender, EventArgs e)
        {

        }


        //黑白效果
        public Bitmap GrayImage(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            Bitmap bitmap2 = new Bitmap(W, H);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);

            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            Color pixel;
            for (int x = 0; x < W; x++)
            {
                for (int y = 0; y < H; y++)
                {
                    pixel = lockBitmap1.GetPixel(x, y);
                    int r, g, b, gray = 0;
                    r = pixel.R;
                    g = pixel.G;
                    b = pixel.B;
                    gray = ((int)(0.3 * r) + (int)(0.59 * g) + (int)(0.11 * b));
                    lockBitmap2.SetPixel(x, y, Color.FromArgb(gray, gray, gray));
                }
            }
            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();
            return bitmap2;
        }

        //底片
        public Bitmap NegativeImage(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            Bitmap bitmap2 = new Bitmap(W, H);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);

            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            Color pixel;
            for (int x = 1; x < W; x++)
            {
                for (int y = 1; y < H; y++)
                {
                    int r, g, b;
                    pixel = lockBitmap1.GetPixel(x, y);
                    r = 255 - pixel.R;
                    g = 255 - pixel.G;
                    b = 255 - pixel.B;
                    lockBitmap2.SetPixel(x, y, Color.FromArgb(r, g, b));
                }
            }
            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();
            return bitmap2;
        }

        //浮雕
        public Bitmap EmbossmentImage(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            Bitmap bitmap2 = new Bitmap(W, H);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);
            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            Color pixel1, pixel2;
            for (int x = 0; x < W - 1; x++)
            {
                for (int y = 0; y < H - 1; y++)
                {
                    int r = 0, g = 0, b = 0;
                    pixel1 = lockBitmap1.GetPixel(x, y);
                    pixel2 = lockBitmap1.GetPixel(x + 1, y + 1);
                    r = Math.Abs(pixel1.R - pixel2.R + 128);
                    g = Math.Abs(pixel1.G - pixel2.G + 128);
                    b = Math.Abs(pixel1.B - pixel2.B + 128);
                    if (r > 255)
                        r = 255;
                    if (r < 0)
                        r = 0;
                    if (g > 255)
                        g = 255;
                    if (g < 0)
                        g = 0;
                    if (b > 255)
                        b = 255;
                    if (b < 0)
                        b = 0;
                    lockBitmap2.SetPixel(x, y, Color.FromArgb(r, g, b));
                }
            }
            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();
            return bitmap2;
        }

        //柔化
        public Bitmap SoftenImage(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            Bitmap bitmap2 = new Bitmap(W, H);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);
            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            Color pixel;
            //高斯模板
            int[] Gauss = { 1, 2, 1, 2, 4, 2, 1, 2, 1 };
            for (int x = 1; x < W - 1; x++)
            {
                for (int y = 1; y < H - 1; y++)
                {
                    int r = 0, g = 0, b = 0;
                    int Index = 0;
                    for (int col = -1; col <= 1; col++)
                    {
                        for (int row = -1; row <= 1; row++)
                        {
                            pixel = lockBitmap1.GetPixel(x + row, y + col);
                            r += pixel.R * Gauss[Index];
                            g += pixel.G * Gauss[Index];
                            b += pixel.B * Gauss[Index];
                            Index++;
                        }
                    }
                    r /= 16;
                    g /= 16;
                    b /= 16;
                    //處理顏色值溢出
                    r = r > 255 ? 255 : r;
                    r = r < 0 ? 0 : r;
                    g = g > 255 ? 255 : g;
                    g = g < 0 ? 0 : g;
                    b = b > 255 ? 255 : b;
                    b = b < 0 ? 0 : b;
                    lockBitmap2.SetPixel(x - 1, y - 1, Color.FromArgb(r, g, b));
                }
            }
            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();
            return bitmap2;
        }

        //銳化
        public Bitmap SharpenImage(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);
            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            //拉普拉斯模板
            int[] Laplacian = { -1, -1, -1, -1, 9, -1, -1, -1, -1 };
            for (int i = 1; i < W - 1; i++)
            {
                for (int j = 1; j < H - 1; j++)
                {
                    int r = 0, g = 0, b = 0;
                    int index = 0;
                    for (int col = -1; col <= 1; col++)
                    {
                        for (int row = -1; row <= 1; row++)
                        {
                            Color color = lockBitmap1.GetPixel(i + row, j + col);
                            r += color.R * Laplacian[index];
                            g += color.G * Laplacian[index];
                            b += color.B * Laplacian[index];
                            index++;
                        }
                    }
                    //處理顏色值溢出
                    r = r > 255 ? 255 : r;
                    r = r < 0 ? 0 : r;
                    g = g > 255 ? 255 : g;
                    g = g < 0 ? 0 : g;
                    b = b > 255 ? 255 : b;
                    b = b < 0 ? 0 : b;
                    lockBitmap2.SetPixel(i - 1, j - 1, Color.FromArgb(r, g, b));
                }
            }
            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();
            return bitmap2;
        }

        //霧化
        public Bitmap AtomizationImage(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            Bitmap bitmap2 = new Bitmap(W, H);

            LockBitmap lockBitmap1 = new LockBitmap(bitmap1);
            LockBitmap lockBitmap2 = new LockBitmap(bitmap2);
            lockBitmap1.LockBits();
            lockBitmap2.LockBits();

            System.Random MyRandom = new Random();
            Color pixel;
            for (int x = 1; x < W - 1; x++)
            {
                for (int y = 1; y < H - 1; y++)
                {
                    int k = MyRandom.Next(123456);
                    //像素塊大小
                    int dx = x + k % 19;
                    int dy = y + k % 19;
                    if (dx >= W)
                        dx = W - 1;
                    if (dy >= H)
                        dy = H - 1;
                    pixel = lockBitmap1.GetPixel(dx, dy);
                    lockBitmap2.SetPixel(x, y, pixel);
                }
            }
            lockBitmap1.UnlockBits();
            lockBitmap2.UnlockBits();
            return bitmap2;
        }

    }

    //指針法
    public class PointBitmap
    {
        Bitmap source = null;
        IntPtr Iptr = IntPtr.Zero;
        BitmapData bitmapData = null;

        public int Depth { get; private set; }
        public int Width { get; private set; }
        public int Height { get; private set; }

        public PointBitmap(Bitmap source)
        {
            this.source = source;
        }

        public void LockBits()
        {
            try
            {
                // Get width and height of bitmap
                Width = source.Width;
                Height = source.Height;

                // get total locked pixels count
                int PixelCount = Width * Height;

                // Create rectangle to lock
                Rectangle rect = new Rectangle(0, 0, Width, Height);

                // get source bitmap pixel format size
                Depth = Bitmap.GetPixelFormatSize(source.PixelFormat);

                // Check if bpp (Bits Per Pixel) is 8, 24, or 32
                if (Depth != 8 && Depth != 24 && Depth != 32)
                {
                    throw new ArgumentException("Only 8, 24 and 32 bpp images are supported.");
                }

                // Lock bitmap and return bitmap data
                bitmapData = source.LockBits(rect, ImageLockMode.ReadWrite,
                                             source.PixelFormat);

                //得到首地址
                unsafe
                {
                    Iptr = bitmapData.Scan0;
                    //二維圖像循環
                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        public void UnlockBits()
        {
            try
            {
                source.UnlockBits(bitmapData);
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        public Color GetPixel(int x, int y)
        {
            unsafe
            {
                byte* ptr = (byte*)Iptr;
                ptr = ptr + bitmapData.Stride * y;
                ptr += Depth * x / 8;
                Color c = Color.Empty;
                if (Depth == 32)
                {
                    int a = ptr[3];
                    int r = ptr[2];
                    int g = ptr[1];
                    int b = ptr[0];
                    c = Color.FromArgb(a, r, g, b);
                }
                else if (Depth == 24)
                {
                    int r = ptr[2];
                    int g = ptr[1];
                    int b = ptr[0];
                    c = Color.FromArgb(r, g, b);
                }
                else if (Depth == 8)
                {
                    int r = ptr[0];
                    c = Color.FromArgb(r, r, r);
                }
                return c;
            }
        }

        public void SetPixel(int x, int y, Color c)
        {
            unsafe
            {
                byte* ptr = (byte*)Iptr;
                ptr = ptr + bitmapData.Stride * y;
                ptr += Depth * x / 8;
                if (Depth == 32)
                {
                    ptr[3] = c.A;
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
                else if (Depth == 24)
                {
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
                else if (Depth == 8)
                {
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
            }
        }
    }


    //內存法
    public class LockBitmap
    {
        Bitmap source = null;
        IntPtr Iptr = IntPtr.Zero;
        BitmapData bitmapData = null;

        public byte[] Pixels { get; set; }
        public int Depth { get; private set; }
        public int Width { get; private set; }
        public int Height { get; private set; }

        public LockBitmap(Bitmap source)
        {
            this.source = source;
        }

        /// <summary>
        /// Lock bitmap data
        /// </summary>
        public void LockBits()
        {
            try
            {
                // Get width and height of bitmap
                Width = source.Width;
                Height = source.Height;

                // get total locked pixels count
                int PixelCount = Width * Height;

                // Create rectangle to lock
                Rectangle rect = new Rectangle(0, 0, Width, Height);

                // get source bitmap pixel format size
                Depth = Bitmap.GetPixelFormatSize(source.PixelFormat);

                // Check if bpp (Bits Per Pixel) is 8, 24, or 32
                if (Depth != 8 && Depth != 24 && Depth != 32)
                {
                    throw new ArgumentException("Only 8, 24 and 32 bpp images are supported.");
                }

                // Lock bitmap and return bitmap data
                bitmapData = source.LockBits(rect, ImageLockMode.ReadWrite,
                                             source.PixelFormat);

                // create byte array to copy pixel values
                int step = Depth / 8;
                Pixels = new byte[PixelCount * step];
                Iptr = bitmapData.Scan0;

                // Copy data from pointer to array
                Marshal.Copy(Iptr, Pixels, 0, Pixels.Length);
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        /// <summary>
        /// Unlock bitmap data
        /// </summary>
        public void UnlockBits()
        {
            try
            {
                // Copy data from byte array to pointer
                Marshal.Copy(Pixels, 0, Iptr, Pixels.Length);

                // Unlock bitmap data
                source.UnlockBits(bitmapData);
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        /// <summary>
        /// Get the color of the specified pixel
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <returns></returns>
        public Color GetPixel(int x, int y)
        {
            Color clr = Color.Empty;

            // Get color components count
            int cCount = Depth / 8;

            // Get start index of the specified pixel
            int i = ((y * Width) + x) * cCount;

            if (i > Pixels.Length - cCount)
                throw new IndexOutOfRangeException();

            if (Depth == 32) // For 32 bpp get Red, Green, Blue and Alpha
            {
                byte b = Pixels[i];
                byte g = Pixels[i + 1];
                byte r = Pixels[i + 2];
                byte a = Pixels[i + 3]; // a
                clr = Color.FromArgb(a, r, g, b);
            }
            if (Depth == 24) // For 24 bpp get Red, Green and Blue
            {
                byte b = Pixels[i];
                byte g = Pixels[i + 1];
                byte r = Pixels[i + 2];
                clr = Color.FromArgb(r, g, b);
            }
            if (Depth == 8)
            // For 8 bpp get color value (Red, Green and Blue values are the same)
            {
                byte c = Pixels[i];
                clr = Color.FromArgb(c, c, c);
            }
            return clr;
        }

        /// <summary>
        /// Set the color of the specified pixel
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <param name="color"></param>
        public void SetPixel(int x, int y, Color color)
        {
            // Get color components count
            int cCount = Depth / 8;

            // Get start index of the specified pixel
            int i = ((y * Width) + x) * cCount;

            if (Depth == 32) // For 32 bpp set Red, Green, Blue and Alpha
            {
                Pixels[i] = color.B;
                Pixels[i + 1] = color.G;
                Pixels[i + 2] = color.R;
                Pixels[i + 3] = color.A;
            }
            if (Depth == 24) // For 24 bpp set Red, Green and Blue
            {
                Pixels[i] = color.B;
                Pixels[i + 1] = color.G;
                Pixels[i + 2] = color.R;
            }
            if (Depth == 8)
            // For 8 bpp set color value (Red, Green and Blue values are the same)
            {
                Pixels[i] = color.B;
            }
        }
    }
}
