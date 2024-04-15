using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                //for File
using System.Diagnostics;       //for Process
using System.Drawing.Imaging;   //for ImageFormat

namespace _vcs_MakePicture
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        Color foreground_color = Color.Red;
        Color background_color = Color.White;

        string FileName = "";
        string word = "唐";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(foreground_color, 3);
            sb = new SolidBrush(foreground_color);

            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 850;
            y_st = 10;
            groupBox1.Location = new Point(x_st - 10, y_st);
            groupBox1.ClientSize = new Size(65 * 8 + 12, 80);

            x_st = 10;
            y_st = 13;
            dx = 65;
            dy = 65;
            bt0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt5.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt6.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt7.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            bt7.BackgroundImage = Properties.Resources.folder_open;

            //button
            x_st = 850;
            y_st = 100;
            dx = 70;
            dy = 70;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button5.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            button6.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            button7.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            button8.Location = new Point(x_st + dx * 8, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 9, y_st + dy * 0);

            button10.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button13.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button14.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button15.Location = new Point(x_st + dx * 5, y_st + dy * 1);
            button16.Location = new Point(x_st + dx * 6, y_st + dy * 1);
            button17.Location = new Point(x_st + dx * 7, y_st + dy * 1);
            button18.Location = new Point(x_st + dx * 8, y_st + dy * 1);
            button19.Location = new Point(x_st + dx * 9, y_st + dy * 1);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button24.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button25.Location = new Point(x_st + dx * 5, y_st + dy * 2);
            button26.Location = new Point(x_st + dx * 6, y_st + dy * 2);
            button27.Location = new Point(x_st + dx * 7, y_st + dy * 2);
            button28.Location = new Point(x_st + dx * 8, y_st + dy * 2);
            button29.Location = new Point(x_st + dx * 9, y_st + dy * 2);

            button30.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button31.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            button35.Location = new Point(x_st + dx * 5, y_st + dy * 3);
            button36.Location = new Point(x_st + dx * 6, y_st + dy * 3);
            button37.Location = new Point(x_st + dx * 7, y_st + dy * 3);
            button38.Location = new Point(x_st + dx * 8, y_st + dy * 3);
            button39.Location = new Point(x_st + dx * 9, y_st + dy * 3);

            button40.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button41.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button42.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button43.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button44.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            button45.Location = new Point(x_st + dx * 5, y_st + dy * 4);
            button46.Location = new Point(x_st + dx * 6, y_st + dy * 4);
            button47.Location = new Point(x_st + dx * 7, y_st + dy * 4);
            button48.Location = new Point(x_st + dx * 8, y_st + dy * 4);
            button49.Location = new Point(x_st + dx * 9, y_st + dy * 4);

            button50.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button51.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button52.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button53.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button54.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            button55.Location = new Point(x_st + dx * 5, y_st + dy * 5);
            button56.Location = new Point(x_st + dx * 6, y_st + dy * 5);
            button57.Location = new Point(x_st + dx * 7, y_st + dy * 5);
            button58.Location = new Point(x_st + dx * 8, y_st + dy * 5);
            button59.Location = new Point(x_st + dx * 9, y_st + dy * 5);

            button60.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button61.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button62.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button63.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button64.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            button65.Location = new Point(x_st + dx * 5, y_st + dy * 6);
            button66.Location = new Point(x_st + dx * 6, y_st + dy * 6);
            button67.Location = new Point(x_st + dx * 7, y_st + dy * 6);
            button68.Location = new Point(x_st + dx * 8, y_st + dy * 6);
            button69.Location = new Point(x_st + dx * 9, y_st + dy * 6);

            button9.Text = word;

            pictureBox1.Location = new Point(10, 10);

            this.Size = new Size(1570, this.Size.Height);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            richTextBox1.Size = new Size(this.Width - richTextBox1.Location.X - 50, this.Height - richTextBox1.Location.Y - 50 - 50);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;

            //離開按鈕的寫法
            bt_exit_setup();

            //最小化按鈕的寫法
            bt_minimize_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
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

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_minimize_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_minimize = new Button();  // 實例化按鈕
            bt_minimize.Size = new Size(w, h);
            bt_minimize.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            //g.DrawLine(p, 0, 0, w - 1, h - 1);
            //g.DrawLine(p, w - 1, 0, 0, h - 1);
            g.DrawLine(p, w / 4, h / 2 - 1, w * 3 / 4, h / 2 - 1);
            bt_minimize.Image = bmp;

            bt_minimize.Location = new Point(this.ClientSize.Width - bt_minimize.Width * 2 - 2, 0);
            bt_minimize.Click += bt_minimize_Click;     // 加入按鈕事件

            this.Controls.Add(bt_minimize); // 將按鈕加入表單
            bt_minimize.BringToFront();     //移到最上層
        }

        private void bt_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //open
            Point[] points = new Point[3];
            points[0] = new Point(width / 8, height / 8);
            points[1] = new Point(width * 7 / 8, height * 1 / 8);
            points[2] = new Point(width * 1 / 2, height * 7 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //close
            Point[] points = new Point[3];
            points[0] = new Point(width / 2, height / 8);
            points[1] = new Point(width * 7 / 8, height * 7 / 8);
            points[2] = new Point(width * 1 / 8, height * 7 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //play-pause
            Point[] points = new Point[3];
            points[0] = new Point(width / 8, height * 2 / 8);
            points[1] = new Point(width / 2, height / 2);
            points[2] = new Point(width / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            g.FillRectangle(sb, new Rectangle(width / 2, height * 2 / 8, width / 8, height / 2));
            g.FillRectangle(sb, new Rectangle(width / 2 + width * 2 / 8, height * 2 / 8, width / 8, height / 2));
            pictureBox1.Image = bitmap1;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            // stop
            g.FillRectangle(sb, new Rectangle(width / 8, height / 8, width * 6 / 8, height * 6 / 8));

            pictureBox1.Image = bitmap1;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }
            g = Graphics.FromImage(bitmap1);
            p = new Pen(Color.Red, 10);
            g.DrawEllipse(p, new Rectangle(5, 5, width - 12, height - 12));
            Font f;


            int t = 5;
            int z = 20;
            Point point1a = new Point(5 + t, 5 + t + z);
            Point point2a = new Point(5 + 115 - t, 5 + 115 - t - z);
            g.DrawLine(p, point1a, point2a);     // Draw line to screen.

            sb = new SolidBrush(Color.Black);
            f = new Font("Arial", 88);

            g.DrawString("2", f, sb, new PointF(10, 0));

            pictureBox1.Image = bitmap1;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;

            sb = new SolidBrush(Color.Red);
            f = new Font("Arial", 42);

            g.DrawString("VCS", f, sb, new PointF(0, 32));

            pictureBox1.Image = bitmap1;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 256;
            height = 30;
            bitmap1 = new Bitmap(width, height);

            for (yy = 0; yy < height / 3; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), 0, 0));
                    bitmap1.SetPixel(xx, yy + height / 3, Color.FromArgb(255, 0, (xx % 256), 0));
                    bitmap1.SetPixel(xx, yy + height / 3 * 2, Color.FromArgb(255, 0, 0, (xx % 256)));
                }
            }

            g = Graphics.FromImage(bitmap1);

            //g.DrawRectangle(p, new Rectangle(0, 0, width - 1, height - 1));

            pictureBox1.Image = bitmap1;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            // refresh
            p = new Pen(Color.Red, 25);
            p.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            g.DrawArc(p, 20, 20, 90, 90, 25, 335);
            pictureBox1.Image = bitmap1;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //加上標記
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;

            if (bitmap1 == null)
                bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);

            //邊框黑白點
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    if (yy == 0)
                    {
                        if ((xx % 2) == 0)
                            bitmap1.SetPixel(xx, yy, Color.White);
                        else
                            bitmap1.SetPixel(xx, yy, Color.Black);
                    }
                    else if (yy == (height - 1))
                    {
                        if ((xx % 2) == 1)
                            bitmap1.SetPixel(xx, yy, Color.White);
                        else
                            bitmap1.SetPixel(xx, yy, Color.Black);
                    }
                    else if (xx == 0)
                    {
                        if ((yy % 2) == 0)
                            bitmap1.SetPixel(xx, yy, Color.White);
                        else
                            bitmap1.SetPixel(xx, yy, Color.Black);
                    }
                    else if (xx == (width - 1))
                    {
                        if ((yy % 2) == 1)
                            bitmap1.SetPixel(xx, yy, Color.White);
                        else
                            bitmap1.SetPixel(xx, yy, Color.Black);
                    }
                }
            }

            p = new Pen(Color.Blue, 1);
            g.DrawRectangle(p, new Rectangle(width / 8, height / 8, width * 6 / 8, height * 6 / 8));
            g.DrawEllipse(p, new Rectangle(5, 5, width - 12, height - 12));
            pictureBox1.Image = bitmap1;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);


                    //background_color
                }
            }

            g = Graphics.FromImage(bitmap1);

            // record
            g.FillEllipse(sb, new Rectangle(width / 4, height / 4, width / 2, height / 2));

            pictureBox1.Image = bitmap1;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //pause
            g.FillRectangle(sb, new Rectangle(width * 3 / 16, height * 2 / 8, width * 4 / 16, height / 2));
            g.FillRectangle(sb, new Rectangle(width * 9 / 16, height * 2 / 8, width * 4 / 16, height / 2));
            pictureBox1.Image = bitmap1;
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //next
            Point[] points = new Point[3];
            points[0] = new Point(width / 8 + width / 8, height * 2 / 8);
            points[1] = new Point(width / 2 + width / 8, height / 2);
            points[2] = new Point(width / 8 + width / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            g.FillRectangle(sb, new Rectangle(width / 2 + width / 8, height * 2 / 8, width / 8, height / 2));
            pictureBox1.Image = bitmap1;
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //previous
            Point[] points = new Point[3];
            points[0] = new Point(width * 6 / 8, height * 2 / 8);
            points[1] = new Point(width / 8 + width / 8 + width / 8, height / 2);
            points[2] = new Point(width * 6 / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            g.FillRectangle(sb, new Rectangle(width / 8 + width / 8, height * 2 / 8, width / 8, height / 2));
            pictureBox1.Image = bitmap1;
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //open-file
            Point[] points = new Point[3];
            points[0] = new Point(width / 8, height * 5 / 8);
            points[1] = new Point(width / 2, height / 8);
            points[2] = new Point(width * 7 / 8, height * 5 / 8);
            g.FillPolygon(sb, points);

            g.FillRectangle(sb, new Rectangle(width / 8, height * 5 / 8 + height / 16, width * 6 / 8, height / 8));
            pictureBox1.Image = bitmap1;

        }

        private void button24_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //plus
            g.FillRectangle(sb, new Rectangle(width / 8, height * 7 / 16, width * 6 / 8, height * 2 / 16));
            g.FillRectangle(sb, new Rectangle(width * 7 / 16, height / 8, width * 2 / 16, height * 6 / 8));
            pictureBox1.Image = bitmap1;
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //minus
            g.FillRectangle(sb, new Rectangle(width / 8, height * 7 / 16, width * 6 / 8, height * 2 / 16));
            pictureBox1.Image = bitmap1;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //up
            Point[] points = new Point[3];
            points[0] = new Point(width * 4 / 8, height * 2 / 8);
            points[1] = new Point(width * 6 / 8, height * 6 / 8);
            points[2] = new Point(width * 2 / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //down
            Point[] points = new Point[3];
            points[0] = new Point(width * 4 / 8, height * 2 / 8);
            points[1] = new Point(width * 6 / 8, height * 6 / 8);
            points[2] = new Point(width * 2 / 8, height * 6 / 8);

            points[0] = new Point(width * 4 / 8, height * 6 / 8);
            points[1] = new Point(width * 6 / 8, height * 2 / 8);
            points[2] = new Point(width * 2 / 8, height * 2 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //加圓圈
            int width;
            int height;

            width = 128;
            height = 128;

            if (bitmap1 == null)
                bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);

            sb = new SolidBrush(Color.Yellow);

            g.FillEllipse(sb, new Rectangle(width / 8, height / 8, width * 6 / 8, height * 6 / 8));

            sb = new SolidBrush(foreground_color);

            pictureBox1.Image = bitmap1;
        }

        private void button26_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            int W = 640;
            int H = 480;

            int width;
            int height;

            Pen p1;
            Pen p2;

            width = W;
            height = H;

            if (bitmap1 == null)
                bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);

            p1 = new Pen(Color.Black, 1);
            p2 = new Pen(Color.Pink, 1);

            // Draw transparency required on layer 1
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    if ((j > (1.5 * (H >> 3) - 1)) && (j < (H - 1.5 * (H >> 3))))
                    {
                        g.DrawEllipse(p2, i, j, 1, 1); //繪製粉紅色圓點 中段
                    }
                    else
                    {

                        if (j < 1.5 * (H >> 3))
                        { // Top lines
                            if ((i < (1.5 * (H >> 3) - j)) || (i > ((W - 1.5 * (H >> 3)) - 1 + j)))
                            {
                                g.DrawEllipse(p1, i, j, 1, 1); //繪製黑色圓點 上段的左右
                            }
                            else
                            {
                                g.DrawEllipse(p2, i, j, 1, 1); //繪製粉紅色圓點 上段的中間
                            }
                        }
                        else
                        { // Bottom lines
                            if ((i < (j + 1.5 * (H >> 3) - H)) || i > ((W - (1.5 * (H >> 3) - (H - j))) - 1))
                            {
                                g.DrawEllipse(p1, i, j, 1, 1); //繪製黑色圓點 下段的左右
                            }
                            else
                            {
                                g.DrawEllipse(p2, i, j, 1, 1); //繪製粉紅色圓點 下段的中間
                            }
                        }
                    }
                }
            }
            pictureBox1.Image = bitmap1;
        }

        private void button28_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //up
            Point[] points = new Point[3];
            points[0] = new Point(width * 4 / 8, height * 2 / 8);
            points[1] = new Point(width * 6 / 8, height * 6 / 8);
            points[2] = new Point(width * 2 / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //down
            Point[] points = new Point[3];
            points[0] = new Point(width * 4 / 8, height * 2 / 8);
            points[1] = new Point(width * 6 / 8, height * 6 / 8);
            points[2] = new Point(width * 2 / 8, height * 6 / 8);

            points[0] = new Point(width * 4 / 8, height * 6 / 8);
            points[1] = new Point(width * 6 / 8, height * 2 / 8);
            points[2] = new Point(width * 2 / 8, height * 2 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //left
            Point[] points = new Point[3];
            points[0] = new Point(width * 2 / 8, height * 4 / 8);
            points[1] = new Point(width * 6 / 8, height * 2 / 8);
            points[2] = new Point(width * 6 / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;
        }

        private void button30_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //right
            Point[] points = new Point[3];
            points[0] = new Point(width * 2 / 8, height * 2 / 8);
            points[1] = new Point(width * 6 / 8, height * 4 / 8);
            points[2] = new Point(width * 2 / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;
        }

        private void button31_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 7);

            g.DrawRectangle(p, new Rectangle(width * 2 / 8, height * 2 / 8, width * 4 / 8, height * 4 / 8));

            Point pointa;
            Point pointb;

            pointa = new Point(width * 4 / 8, height * 0 / 8);
            pointb = new Point(width * 4 / 8, height * 2 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 4 / 8, height * 6 / 8);
            pointb = new Point(width * 4 / 8, height * 8 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 0 / 8, height * 4 / 8);
            pointb = new Point(width * 2 / 8, height * 4 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 6 / 8, height * 4 / 8);
            pointb = new Point(width * 8 / 8, height * 4 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;
        }

        private void button32_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 7);

            g.DrawRectangle(p, new Rectangle(width * 1 / 8, height * 1 / 8, width * 6 / 8, height * 6 / 8));

            Point pointa;
            Point pointb;

            p = new Pen(background_color, 7);

            pointa = new Point(width * 3 / 8, height * 1 / 8);
            pointb = new Point(width * 5 / 8, height * 1 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 8, height * 3 / 8);
            pointb = new Point(width * 1 / 8, height * 5 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 3 / 8, height * 7 / 8);
            pointb = new Point(width * 5 / 8, height * 7 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 7 / 8, height * 3 / 8);
            pointb = new Point(width * 7 / 8, height * 5 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;
        }

        private void button33_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            // refresh
            p = new Pen(foreground_color, 20);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            p.EndCap = System.Drawing.Drawing2D.LineCap.Round;
            g.DrawArc(p, 20, 20, 90, 90, -45, 180 + 45 + 45);

            Point pointa;
            Point pointb;

            pointa = new Point(width * 4 / 8, height * 1 / 8);
            pointb = new Point(width * 4 / 8, height * 4 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;
        }

        private void button34_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 7);

            g.DrawRectangle(p, new Rectangle(width * 1 / 16, height * 1 / 16, width * 14 / 16, height * 14 / 16));

            Point pointa;
            Point pointb;

            p = new Pen(background_color, 7);

            pointa = new Point(width * 6 / 16, height * 1 / 16);
            pointb = new Point(width * 10 / 16, height * 1 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 16, height * 6 / 16);
            pointb = new Point(width * 1 / 16, height * 10 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 6 / 16, height * 15 / 16);
            pointb = new Point(width * 10 / 16, height * 15 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 15 / 16, height * 6 / 16);
            pointb = new Point(width * 15 / 16, height * 10 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.


            p = new Pen(foreground_color, 7);
            p.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;

            pointa = new Point(width * 5 / 16, height * 5 / 16);
            pointb = new Point(width * 2 / 16, height * 2 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 11 / 16, height * 5 / 16);
            pointb = new Point(width * 14 / 16, height * 2 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 5 / 16, height * 11 / 16);
            pointb = new Point(width * 2 / 16, height * 14 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 11 / 16, height * 11 / 16);
            pointb = new Point(width * 14 / 16, height * 14 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;
        }

        private void button35_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 7);

            g.DrawRectangle(p, new Rectangle(width * 4 / 16, height * 4 / 16, width * 8 / 16, height * 8 / 16));

            Point pointa;
            Point pointb;

            p = new Pen(background_color, 7);

            pointa = new Point(width * 6 / 16, height * 4 / 16);
            pointb = new Point(width * 10 / 16, height * 4 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 4 / 16, height * 6 / 16);
            pointb = new Point(width * 4 / 16, height * 10 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 6 / 16, height * 12 / 16);
            pointb = new Point(width * 10 / 16, height * 12 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 12 / 16, height * 6 / 16);
            pointb = new Point(width * 12 / 16, height * 10 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.


            p = new Pen(foreground_color, 7);
            p.StartCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;

            pointa = new Point(width * 4 / 16 - 5, height * 4 / 16 - 5);
            pointb = new Point(width * 1 / 16, height * 1 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 12 / 16 + 5, height * 4 / 16 - 5);
            pointb = new Point(width * 15 / 16, height * 1 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 4 / 16 - 5, height * 12 / 16 + 5);
            pointb = new Point(width * 1 / 16, height * 15 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 12 / 16 + 5, height * 12 / 16 + 5);
            pointb = new Point(width * 15 / 16, height * 15 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;
        }

        private void button36_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 25);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;

            Point pointa;
            Point pointb;

            pointa = new Point(width * 1 / 4, height * 3 / 16);
            pointb = new Point(width * 1 / 4, height * 7 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 4, height * 3 / 16);
            pointb = new Point(width * 3 / 4, height * 3 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 4, height * 8 / 16);
            pointb = new Point(width * 11 / 16, height * 8 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;
        }

        private void button37_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 25);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;

            Point pointa;
            Point pointb;

            pointa = new Point(width * 3 / 4, height * 3 / 16);
            pointb = new Point(width * 3 / 4, height * 7 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 5 / 16, height * 3 / 16);
            pointb = new Point(width * 3 / 4, height * 3 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 3 / 4, height * 8 / 16);
            pointb = new Point(width * 5 / 16, height * 8 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;
        }

        private void button38_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 25);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;

            Point pointa;
            Point pointb;

            pointa = new Point(width * 1 / 4, height * 3 / 16);
            pointb = new Point(width * 1 / 4, height * 7 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 4, height * 13 / 16);
            pointb = new Point(width * 3 / 4, height * 13 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 4, height * 8 / 16);
            pointb = new Point(width * 11 / 16, height * 8 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;
        }

        private void button39_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 25);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;

            Point pointa;
            Point pointb;

            pointa = new Point(width * 3 / 4, height * 3 / 16);
            pointb = new Point(width * 3 / 4, height * 7 / 8 + 3);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 5 / 16, height * 13 / 16);
            pointb = new Point(width * 3 / 4, height * 13 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 3 / 4, height * 8 / 16);
            pointb = new Point(width * 5 / 16, height * 8 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;
        }

        private void button40_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //cross
            Point pointa;
            Point pointb;

            p = new Pen(foreground_color, 15);

            pointa = new Point(width * 2 / 8, height * 2 / 8);
            pointb = new Point(width * 6 / 8, height * 6 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 6 / 8, height * 2 / 8);
            pointb = new Point(width * 2 / 8, height * 6 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;
        }

        private void button41_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;

            sb = new SolidBrush(Color.Red);
            f = new Font("Arial", 60);

            g.DrawString("C#", f, sb, new PointF(0, 20));

            pictureBox1.Image = bitmap1;
        }

        private void button42_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;

            sb = new SolidBrush(Color.Red);
            f = new Font("Arial", 80);

            g.DrawString("A", f, sb, new PointF(10, 5));

            g.DrawRectangle(p, new Rectangle(width / 8, height / 8, width * 6 / 8, height * 6 / 8));

            pictureBox1.Image = bitmap1;
        }

        private void button43_Click(object sender, EventArgs e)
        {
            //home
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 25);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;


            //close
            Point[] points = new Point[3];
            points[0] = new Point(width / 2, height / 8);
            points[1] = new Point(width * 7 / 8, height * 4 / 8);
            points[2] = new Point(width * 1 / 8, height * 4 / 8);
            g.FillPolygon(sb, points);

            g.FillRectangle(sb, new Rectangle(width * 2 / 8, height * 4 / 8, width * 4 / 8, height * 3 / 8));

            p = new Pen(Color.White, 2);
            g.DrawRectangle(p, new Rectangle(width * 6 / 16, height * 9 / 16, width * 4 / 16, height * 7 / 16));

            pictureBox1.Image = bitmap1;
        }

        private void button44_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;

            sb = new SolidBrush(Color.Red);
            f = new Font("標楷體", 65);

            g.DrawString("詞", f, sb, new PointF(10, 20));

            g.DrawRectangle(p, new Rectangle(width / 8, height / 8, width * 6 / 8, height * 6 / 8));

            pictureBox1.Image = bitmap1;
        }

        private void button45_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;

            int hh = 35;
            f = new Font("Arial", 35);
            sb = new SolidBrush(Color.Red);
            g.DrawString("R", f, sb, new PointF(5, hh));
            sb = new SolidBrush(Color.Green);
            g.DrawString("G", f, sb, new PointF(38, hh));
            sb = new SolidBrush(Color.Blue);
            g.DrawString("B", f, sb, new PointF(76, hh));

            g.DrawRectangle(p, new Rectangle(width / 16, height / 16, width * 14 / 16, height * 14 / 16));

            pictureBox1.Image = bitmap1;
        }

        private void button46_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;

            sb = new SolidBrush(Color.Red);
            f = new Font("Arial", 28);

            g.DrawString("Python", f, sb, new PointF(0, 42));

            pictureBox1.Image = bitmap1;
        }

        private void button47_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //bin2bmp
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), (xx % 256), (xx % 256)));
                }
            }

            g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;
        }

        private void button48_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 256 * 100;
            height = 678;
            bitmap1 = new Bitmap(width, height);

            //bin2bmp
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), (xx % 256), (xx % 256)));
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;
            f = new Font("Arial", 50);
            for (xx = 0; xx < width; xx += 256)
            {
                g.DrawString((xx / 256 + 1).ToString() + "/" + (width / 256).ToString(), f, sb, new PointF(xx, 100));
            }

            g.DrawRectangle(p, new Rectangle(0, 0, width - 1, height - 1));

            pictureBox1.Image = bitmap1;
        }

        private const int ON = 0x00;
        private const int OFF = 0x01;

        void draw_switch(int on_off)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 64;
            bitmap1 = new Bitmap(width, height);

            Color background_color;
            Color foreground_color;
            Color active_color;
            Font f;

            if (on_off == ON)
            {
                background_color = Color.Black;
                foreground_color = Color.LimeGreen;
                active_color = Color.White;
            }
            else
            {
                background_color = Color.Black;
                foreground_color = Color.LimeGreen;
                active_color = Color.White;
            }

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            sb = new SolidBrush(foreground_color);

            g.FillEllipse(sb, new Rectangle(0, 0, width / 2, width / 2));
            g.FillEllipse(sb, new Rectangle(width / 2, 0, width / 2, width / 2));
            g.FillRectangle(sb, new Rectangle(width / 4, 0, width / 2, width / 2));

            sb = new SolidBrush(active_color);

            if (on_off == ON)
                g.FillEllipse(sb, new Rectangle(width / 2 + 2, 0 + 2, width / 2 - 4, width / 2 - 4));
            else
                g.FillEllipse(sb, new Rectangle(0 / 2 + 2, 0 + 2, width / 2 - 4, width / 2 - 4));


            sb = new SolidBrush(active_color);
            f = new Font("Arial", 20);

            if (on_off == ON)
                g.DrawString("ON", f, sb, new PointF(width / 16, height / 4));
            else
                g.DrawString("OFF", f, sb, new PointF(width / 2, height / 4));

            pictureBox1.Image = bitmap1;
        }

        private void button49_Click(object sender, EventArgs e)
        {
            draw_switch(ON);
        }

        private void button50_Click(object sender, EventArgs e)
        {
            draw_switch(OFF);
        }

        private void button51_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 256;
            height = 256;
            bitmap1 = new Bitmap(width, height);

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    if (yy < 256 / 4)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), 0, 0));
                    else if (yy < 256 / 4 * 2)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0, (xx % 256), 0));
                    else if (yy < 256 / 4 * 3)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0, 0, (xx % 256)));
                    else
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), (xx % 256), (xx % 256)));
                }
            }
            g = Graphics.FromImage(bitmap1);

            pictureBox1.Image = bitmap1;
        }

        private void button52_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 200;
            height = 200;
            bitmap1 = new Bitmap(width, height);

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    if (((xx + yy) % 5) == 0)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 255, 255, 255));
                    else
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0, 0, 0));
                }
            }
            g = Graphics.FromImage(bitmap1);

            pictureBox1.Image = bitmap1;
        }

        private void button53_Click(object sender, EventArgs e)
        {
            //正中簡中

            //寫字畫框

            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);



            int dd = 5;
            p = new Pen(Color.SkyBlue, 20);
            g.DrawRectangle(p, new Rectangle(width / 6 + dd, height / 6 + dd, width * 4 / 6 - dd * 2, height * 4 / 6 - dd * 2));

            Font f;
            f = new Font("標楷體", 45);
            sb = new SolidBrush(Color.Red);
            g.DrawString("正中", f, sb, new PointF(-5, 0));
            g.DrawString("簡中", f, sb, new PointF(-5, 128 / 2));

            pictureBox1.Image = bitmap1;
        }

        private void button54_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 500;
            height = 200;
            bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Pink);

            g.FillEllipse(new SolidBrush(Color.Red), new Rectangle(0, 0, 100, 200));
            g.FillEllipse(new SolidBrush(Color.Red), new Rectangle(500 - 100, 0, 100, 200));

            g.FillRectangle(new SolidBrush(Color.Red), new Rectangle(50, 0, 100, 200));
            g.FillRectangle(new SolidBrush(Color.Green), new Rectangle(100, 0, 100, 200));
            g.FillRectangle(new SolidBrush(Color.Pink), new Rectangle(200, 0, 100, 200));
            g.FillRectangle(new SolidBrush(Color.Yellow), new Rectangle(300, 0, 100, 200));
            g.FillRectangle(new SolidBrush(Color.Red), new Rectangle(400, 0, 50, 200));

            Font f;

            sb = new SolidBrush(Color.Blue);
            f = new Font("標楷體", 86);

            g.DrawString("群曜醫電", f, sb, new PointF(0, 50));

            pictureBox1.Image = bitmap1;
        }

        private void button55_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;

            width = 601;
            height = 601;
            bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            int x_st = 100;
            int y_st = 100;
            int dx = 50;
            int dy = 50;

            int i;
            for (i = 0; i <= width; i += dx)
            {
                g.DrawLine(Pens.Black, i, 0, i, height);

            }
            for (i = 0; i <= height; i += dx)
            {
                g.DrawLine(Pens.Black, 0, i, width, i);

            }

            pictureBox1.Image = bitmap1;
        }

        private void button56_Click(object sender, EventArgs e)
        {
            //製作桌布
            //1080p的桌面 Windows是顯示 1920 X 1040  下面的40點是工作列
            //用ACDSee設置桌面 要選 Titled

            int width;
            int height;

            int W = 1920;
            int H = 1040;

            bitmap1 = new Bitmap(W, H);

            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Black);

            int x_st = 0;
            int y_st = 0;
            int dx = 100;
            int dy = 100;

            g.DrawRectangle(Pens.DarkGray, 0, 0, 640, 480);  //外框
            g.DrawRectangle(Pens.DarkGray, 640, 0, 640, 480);  //外框
            g.DrawRectangle(Pens.DarkGray, 640 * 2, 0, 640, 480);  //外框
            g.DrawRectangle(Pens.DarkGray, 0, 480, 640, 480);  //外框
            g.DrawRectangle(Pens.DarkGray, 640, 480, 640, 480);  //外框
            g.DrawRectangle(Pens.DarkGray, 640 * 2, 480, 640, 480);  //外框
            //g.DrawRectangle(Pens.DarkGray, 0, 0, 1280 - 1, 720 - 1);  //外框
            g.DrawRectangle(Pens.Red, 0, 0, W - 1, H - 1);  //外框

            g.DrawLine(Pens.DarkGray, W / 2, 0, W / 2, H);  //畫直線
            g.DrawLine(Pens.DarkGray, 0, 1080 / 2, W, 1080 / 2);    //畫橫線

            Point pt = new Point();

            int i;

            for (i = 0; i <= W; i += dx)
            {
                //g.DrawLine(Pens.DarkGray, i, 0, i, H);  //畫直線
            }
            for (i = 0; i <= H; i += dy)
            {
                //g.DrawLine(Pens.DarkGray, 0, i, W, i);    //畫橫線
            }

            int j;
            SolidBrush b = new SolidBrush(Color.DarkGray);
            for (j = 0; j <= H; j += dx)
            {
                for (i = 0; i <= W; i += dx)
                {
                    pt = new Point(i, j);
                    g.FillRectangle(b, pt.X, pt.Y, 1, 1);
                }
            }

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\SpringBouquet.jpg";
            Bitmap bitmap2 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            g.DrawImage(bitmap2, (W - bitmap2.Width) / 2, (H - bitmap2.Height) / 2, bitmap2.Width, bitmap2.Height);
            //              貼上的位置      貼上的大小 放大縮小用

            Font f;
            f = new Font("標楷體", 60);
            sb = new SolidBrush(Color.Red);
            g.DrawString("Sugar", f, sb, new PointF(W - 250, H - 82));

            pictureBox1.Image = bitmap1;
        }

        private void button57_Click(object sender, EventArgs e)
        {
            //OpenCV測試圖

            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 256;
            height = 300;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    //bitmap1.SetPixel(xx, yy, background_color);
                    if (yy < 100)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), 0x00, 0x00));
                    else if (yy < 200)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x00, (xx % 256), 0x00));
                    else
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x00, 0x00, (xx % 256)));
                }
            }
            pictureBox1.Image = bitmap1;

            string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            bitmap1.Save(@filename, ImageFormat.Bmp);

            richTextBox1.Text += "存檔成功\n";
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        //C#獲取圖片的指定部分
        /// <summary>
        /// 獲取圖片指定部分
        /// </summary>
        /// <param name="filename">圖片路徑</param>
        /// <param name="sx">原始圖片開始截取處的坐標X值</param>
        /// <param name="sy">原始圖片開始截取處的坐標Y值</param>
        /// <param name="sWidth">原始圖片的寬度</param>
        /// <param name="sHeight">原始圖片的高度</param>
        /// <param name="dx">目標圖片開始繪制處的坐標X值(通常為0)</param>
        /// <param name="dy">目標圖片開始繪制處的坐標Y值(通常為0)</param>
        /// <param name="dWidth">目標圖片的寬度</param>
        /// <param name="dHeight">目標圖片的高度</param>
        static Bitmap GetPart(string filename, int sx, int sy, int sWidth, int sHeight, int dx, int dy, int dWidth, int dHeight)
        {
            Image image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(dWidth, dHeight);
            Graphics g = Graphics.FromImage(bitmap1);
            Rectangle rec1 = new Rectangle(new Point(sx, sy), new Size(sWidth, sHeight));//原圖位置
            Rectangle rec2 = new Rectangle(new Point(dx, dy), new Size(dWidth, dHeight));//目標位置

            g.DrawImage(image, rec2, rec1, GraphicsUnit.Pixel);

            return bitmap1;
        }


        private void button58_Click(object sender, EventArgs e)
        {
            //取得圖片的一部分
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\SF0.jpg";

            int dd = 500;
            int sx = 0 + dd * 4;
            int sy = 0;
            int sWidth = 700;
            int sHeight = 735;
            int dx = 0;
            int dy = 0;
            int dWidth = 700;
            int dHeight = 735;

            bitmap1 = GetPart(filename, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);
            pictureBox1.Image = bitmap1;
        }

        private void button59_Click(object sender, EventArgs e)
        {
            //opencv 做 dilate erode 用
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 700;
            height = 700;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, Color.White);
                }
            }

            g = Graphics.FromImage(bitmap1);

            sb = new SolidBrush(Color.Black);
            g.FillRectangle(sb, new Rectangle(100, 100, 500, 500));

            sb = new SolidBrush(Color.White);
            g.FillRectangle(sb, new Rectangle(200, 200, 300, 300));

            sb = new SolidBrush(Color.Black);
            g.FillRectangle(sb, new Rectangle(100, 300, 500, 100));
            g.FillRectangle(sb, new Rectangle(300, 100, 100, 500));

            pictureBox1.Image = bitmap1;
        }


        private void button60_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            Graphics g = Graphics.FromImage(bitmap1);

            int dd = 2;
            p = new Pen(Color.Red, dd);
            g.DrawRectangle(p, new Rectangle(0 + dd / 2, 0 + dd / 2, W - dd, H - dd));

            pictureBox1.Image = bitmap1;

            filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
            String filename1 = filename + ".jpg";

            bitmap1.Save(@filename1, ImageFormat.Jpeg);

            richTextBox1.Text += "存檔成功\n";
            richTextBox1.Text += "已存檔 : " + filename1 + "\n";
        }

        private void button61_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "draw image在圖片的不同地方 做opencv疊合用";

            int W = 640;
            int H = 480;
            Bitmap bitmap1 = new Bitmap(W, H);

            g = Graphics.FromImage(bitmap1);

            int dd = 10;
            p = new Pen(Color.FromArgb(255, 128, 0, 0), 20);
            g.DrawRectangle(p, new Rectangle(dd, dd, W - dd * 2, H - dd * 2));

            dd = 20;
            p = new Pen(Color.FromArgb(255, 255, 0, 0), 20);
            g.DrawRectangle(p, new Rectangle(dd, dd, W - dd * 2, H - dd * 2));

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.bmp";
            Bitmap bitmap2 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            g.DrawImage(bitmap2, 20+100, (H - 400) / 2, bitmap2.Width, bitmap2.Height);
            //              貼上的位置      貼上的大小 放大縮小用

            Font f;
            f = new Font("標楷體", 80);
            sb = new SolidBrush(Color.FromArgb(255, 255, 0, 0));
            g.DrawString("左", f, sb, new PointF(80, 350));

            filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            bitmap1.Save(@filename, ImageFormat.Bmp);

            pictureBox1.Image = bitmap1;
        }

        private void button62_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "draw image在圖片的不同地方 做opencv疊合用";

            int W = 640;
            int H = 480;
            Bitmap bitmap1 = new Bitmap(W, H);

            g = Graphics.FromImage(bitmap1);

            int dd = 10;
            p = new Pen(Color.FromArgb(255, 128, 0, 0), 20);
            g.DrawRectangle(p, new Rectangle(dd, dd, W - dd * 2, H - dd * 2));

            dd = 20;
            p = new Pen(Color.FromArgb(255, 0, 255, 0), 20);
            g.DrawRectangle(p, new Rectangle(dd, dd, W - dd * 2, H - dd * 2));

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture2.jpg";
            Bitmap bitmap2 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            richTextBox1.Text += "W = " + bitmap2.Width.ToString() + ", H = " + bitmap2.Height.ToString() + "\n";
            g.DrawImage(bitmap2, W-20-bitmap2.Width-100, (H - 400) / 2, bitmap2.Width, bitmap2.Height);
            //              貼上的位置      貼上的大小 放大縮小用

            Font f;
            f = new Font("標楷體", 80);
            sb = new SolidBrush(Color.FromArgb(255, 0, 255, 0));
            g.DrawString("右", f, sb, new PointF(80+320, 350));

            filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            bitmap1.Save(@filename, ImageFormat.Bmp);

            pictureBox1.Image = bitmap1;
        }

        private void button63_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "draw image在圖片的不同地方 做opencv疊合用";

            int W = 430;
            int H = 304;
            Bitmap bitmap1 = new Bitmap(W, H);

            g = Graphics.FromImage(bitmap1);

            int dd = 10;
            p = new Pen(Color.FromArgb(255, 128, 0, 0), 20);
            g.DrawRectangle(p, new Rectangle(dd, dd, W - dd * 2, H - dd * 2));

            dd = 20;
            p = new Pen(Color.FromArgb(255, 0, 255, 0), 20);
            g.DrawRectangle(p, new Rectangle(dd, dd, W - dd * 2, H - dd * 2));

            string filename = @"Spyder.bmp";
            Bitmap bitmap2 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            richTextBox1.Text += "W = " + bitmap2.Width.ToString() + ", H = " + bitmap2.Height.ToString() + "\n";
            g.DrawImage(bitmap2, 0, 0, bitmap2.Width, bitmap2.Height);
            //              貼上的位置      貼上的大小 放大縮小用


            int x_st = 20;
            int y_st = 20;
            int dx = 68;
            int dy = 70;
            int w = 50;
            int h = 45;

            //Cyan 0 255 255
            sb = new SolidBrush(Color.FromArgb(255, 0x00, 0xff, 0xff));
            g.FillRectangle(sb, new Rectangle(x_st + dx * 0, y_st + dy * 2, w, h));
            
            //Magenta 255 0 255
            sb = new SolidBrush(Color.FromArgb(255, 0xff, 0x0, 0xff));
            g.FillRectangle(sb, new Rectangle(x_st + dx * 1, y_st + dy * 2, w, h));

            //Yellow 255 255 0
            sb = new SolidBrush(Color.FromArgb(255, 0xff, 0xff, 0x00));
            g.FillRectangle(sb, new Rectangle(x_st + dx * 2, y_st + dy * 2, w, h));

            //R
            sb = new SolidBrush(Color.FromArgb(255, 0xff, 0x00, 0x00));
            g.FillRectangle(sb, new Rectangle(x_st + dx * 3, y_st + dy * 2, w, h));

            //G
            sb = new SolidBrush(Color.FromArgb(255, 0x00, 0xff, 0x00));
            g.FillRectangle(sb, new Rectangle(x_st + dx * 4, y_st + dy * 2, w, h));

            //B
            sb = new SolidBrush(Color.FromArgb(255, 0x00, 0x00, 0xff));
            g.FillRectangle(sb, new Rectangle(x_st + dx * 5, y_st + dy * 2, w, h));

            //White
            sb = new SolidBrush(Color.FromArgb(255, 0xff, 0xff, 0xff));
            g.FillRectangle(sb, new Rectangle(x_st + dx * 0, y_st + dy * 3, w, h));

            //Black
            sb = new SolidBrush(Color.FromArgb(255, 0x00, 0x00, 0x00));
            g.FillRectangle(sb, new Rectangle(x_st + dx * 5, y_st + dy * 3, w, h));



            filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            bitmap1.Save(@filename, ImageFormat.Bmp);

            pictureBox1.Image = bitmap1;

        }

        private void button64_Click(object sender, EventArgs e)
        {
            //RGB 圓形
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 400;
            height = 400;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    bitmap1.SetPixel(xx, yy, Color.Black);
                }
            }

            g = Graphics.FromImage(bitmap1);

            sb = new SolidBrush(Color.Blue);

            g.FillEllipse(sb, 100+70, 50+120, 200, 200);

            pictureBox1.Image = bitmap1;

        }

        private void button65_Click(object sender, EventArgs e)
        {
            //製作logo

            //寫字畫框

            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 400;
            height = 400;
            bitmap1 = new Bitmap(width, height);

            background_color = Color.White;

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);


            int linewidth = 40;
            p = new Pen(Color.Black, linewidth);
            int dd = linewidth / 2;

            g.DrawRectangle(p, new Rectangle(dd, dd, width - linewidth * 1, height - linewidth * 1));

            p = new Pen(Color.Blue, 40);
            dd += linewidth;
            g.DrawRectangle(p, new Rectangle(dd, dd, width - linewidth * 3, height - linewidth * 3));

            p = new Pen(Color.Lime, 40);
            dd += linewidth;
            g.DrawRectangle(p, new Rectangle(dd, dd, width - linewidth * 5, height - linewidth * 5));


            Font f;
            f = new Font("標楷體", 300);
            sb = new SolidBrush(Color.Red);
            g.DrawString("群", f, sb, new PointF(-65,-10));

            pictureBox1.Image = bitmap1;


        }

        private void button66_Click(object sender, EventArgs e)
        {

        }

        private void button67_Click(object sender, EventArgs e)
        {

        }

        private void button68_Click(object sender, EventArgs e)
        {

        }

        private void button69_Click(object sender, EventArgs e)
        {

        }

        private void bt0_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png";
            //openFileDialog1.Filter = "BMP|*.bmp|JPG|*.jpg|PNG|*.png|GIF|*.gif";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                FileName = this.openFileDialog1.FileName.Trim();
                richTextBox1.Text += FileName + "\n";
                pictureBox1.ImageLocation = openFileDialog1.FileName;
            }
        }

        private void bt1_Click(object sender, EventArgs e)
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                bitmap1.Save(@filename1, ImageFormat.Jpeg);
                bitmap1.Save(@filename2, ImageFormat.Bmp);
                bitmap1.Save(@filename3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                richTextBox1.Text += "已存檔 : " + filename3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void bt2_Click(object sender, EventArgs e)
        {
            if (FileName == "")
            {
                richTextBox1.Text += "未選取圖片\n";
                return;
            }
            //圖示中包含的圖片常見尺寸有16×16（小圖示）、32×32、48×48，另外24×24、64×64、128×128也比較常見。
            Size size = new Size(256, 256);
            //獲得原始圖片文件
            using (Bitmap bm = new Bitmap(FileName))
            {
                //從現有的圖像縮小, 為了得到合適的icon文件
                using (Bitmap iconBm = new Bitmap(bm, size))    //硬是把大圖縮成小圖
                {
                    using (Icon icon = Icon.FromHandle(iconBm.GetHicon()))
                    {
                        string icon_filename = Application.StartupPath + "\\ICO_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".ico";
                        using (Stream stream = new System.IO.FileStream(icon_filename, System.IO.FileMode.Create))
                        {
                            icon.Save(stream);
                            richTextBox1.Text += "轉換成功, 路徑是 : " + icon_filename + "\n";
                        }
                    }
                }
            }
        }

        private void bt3_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                richTextBox1.Text += "無圖片資料\n";
                return;
            }

            //圖示中包含的圖片常見尺寸有16×16（小圖示）、32×32、48×48，另外24×24、64×64、128×128也比較常見。
            Size size = new Size(128, 128);
            //獲得原始圖片文件
            //using (Bitmap bm = new Bitmap(FileName))
            {
                //從現有的圖像縮小, 為了得到合適的icon文件
                using (Bitmap iconBm = new Bitmap(bitmap1, size))
                {
                    using (Icon icon = Icon.FromHandle(iconBm.GetHicon()))
                    {
                        string icon_filename = Application.StartupPath + "\\ICO_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".ico";
                        using (Stream stream = new System.IO.FileStream(icon_filename, System.IO.FileMode.Create))
                        {
                            icon.Save(stream);
                            richTextBox1.Text += "轉換成功, 路徑是 : " + icon_filename + "\n";
                        }
                    }
                }
            }
        }

        private void bt4_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                foreground_color = colorDialog1.Color;
                sb = new SolidBrush(foreground_color);
                button18.BackColor = foreground_color;
            }
        }

        private void bt5_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                background_color = colorDialog1.Color;
                button19.BackColor = background_color;
            }
        }

        private void bt6_Click(object sender, EventArgs e)
        {

        }

        private void bt7_Click(object sender, EventArgs e)
        {
            //開啟檔案總管
            Process.Start(Application.StartupPath);
        }

        void draw_camera_status_icon(Color back_color)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128 * 1;
            height = 128 * 1;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    bitmap1.SetPixel(xx, yy, Color.Black);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 7);

            int linewidth = width / 32;
            g.DrawEllipse(new Pen(back_color, linewidth), 0 + linewidth / 2, 0 + linewidth / 2, width - linewidth - 1, height - linewidth - 1);

            sb = new SolidBrush(Color.White);
            g.FillEllipse(sb, 0 + linewidth / 2, 0 + linewidth / 2, width - linewidth - 1, height - linewidth - 1);

            sb = new SolidBrush(back_color);
            g.FillEllipse(sb, 8 + linewidth / 2, 8 + linewidth / 2, width - linewidth - 1 - 16, height - linewidth - 1 - 16);


            //linewidth = 2;
            int dx = 6;
            //int dy = 6;

            sb = new SolidBrush(Color.White);
            Point[] points = new Point[6];
            int x_st = width * 6 / 10 - width / 16;
            int y_st = height * 5 / 10;

            int w = width / 5;
            int h = height / 6;

            dx = width / 12;
            y_st -= h / 2;
            points[0] = new Point(x_st, y_st);
            x_st += w;
            y_st -= w;
            points[1] = new Point(x_st, y_st);
            x_st += dx;
            points[2] = new Point(x_st, y_st);
            y_st += (w * 2 + h);
            points[3] = new Point(x_st, y_st);
            x_st -= dx;
            points[4] = new Point(x_st, y_st);
            x_st -= w;
            y_st -= w;
            points[5] = new Point(x_st, y_st);
            g.FillPolygon(sb, points);

            points = new Point[4];

            x_st = width * 2 / 10 - width / 16; ;
            y_st = height * 5 / 10;

            w = width * 4 / 10 - width / 32;
            h = height * 4 / 10;

            y_st -= h / 2;
            points[0] = new Point(x_st, y_st);
            x_st += w;
            points[1] = new Point(x_st, y_st);
            y_st += h;
            points[2] = new Point(x_st, y_st);
            x_st -= w;
            points[3] = new Point(x_st, y_st);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Color back_color = Color.Lime;

            draw_camera_status_icon(back_color);

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //寫字畫框

            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);



            int dd = 5;
            p = new Pen(Color.SkyBlue, 20);
            g.DrawRectangle(p, new Rectangle(width / 6 + dd, height / 6 + dd, width * 4 / 6 - dd * 2, height * 4 / 6 - dd * 2));

            Font f;
            f = new Font("標楷體", 100);
            sb = new SolidBrush(Color.Red);
            g.DrawString(word, f, sb, new PointF(-29, -7));

            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, Color.Black);
                }
            }

            g = Graphics.FromImage(bitmap1);

            int radius = width * 5 / 10;
            Point center = new Point(width / 2, height / 2);
            FillStar(g, center, radius, Color.Red);

            radius = width * 3 / 10;
            FillStar(g, center, radius, Color.Blue);

            radius = width * 1 / 10;
            FillStar(g, center, radius, Color.White);

            pictureBox1.Image = bitmap1;
        }

        private void FillStar(Graphics g, PointF center, int radius, Color c)
        {
            //FillStar

            PointF[] pt1 = new PointF[5];    //一維陣列內有5個Point, 外圈
            PointF[] pt2 = new PointF[5];    //一維陣列內有5個Point, 內圈
            int angle;

            int i;
            for (i = 0; i < 5; i++)
            {
                angle = -90 + 72 * i;
                pt1[i].X = (int)(radius * Math.Cos(angle * Math.PI / 180));
                pt1[i].Y = (int)(radius * Math.Sin(angle * Math.PI / 180));

                //richTextBox1.Text += "pt1[" + i.ToString() + "].X " + pt1[i].X.ToString() + "\t" + "pt1[" + i.ToString() + "].Y " + pt1[i].Y.ToString() + "\n";
                pt1[i].X += center.X;
                pt1[i].Y += center.Y;
            }

            double radius2;
            radius2 = (double)radius * Math.Sin(18 * Math.PI / 180) / Math.Sin(54 * Math.PI / 180);
            for (i = 0; i < 5; i++)
            {
                angle = 72 * i - 54;
                pt2[i].X = (int)(radius2 * Math.Cos(angle * Math.PI / 180));
                pt2[i].Y = (int)(radius2 * Math.Sin(angle * Math.PI / 180));

                //richTextBox1.Text += "pt2[" + i.ToString() + "].X " + pt2[i].X.ToString() + "\t" + "pt2[" + i.ToString() + "].Y " + pt2[i].Y.ToString() + "\n";
                pt2[i].X += center.X;
                pt2[i].Y += center.Y;
            }
            sb = new SolidBrush(c);

            PointF[] pt3 = new PointF[3];    //一維陣列內有3個Point
            pt3[0] = pt1[0];
            pt3[1] = pt2[1];
            pt3[2] = pt2[3];
            g.FillPolygon(sb, pt3);
            pt3[0] = pt1[1];
            pt3[1] = pt2[2];
            pt3[2] = pt2[4];
            g.FillPolygon(sb, pt3);
            pt3[0] = pt1[2];
            pt3[1] = pt2[3];
            pt3[2] = pt2[0];
            g.FillPolygon(sb, pt3);
            pt3[0] = pt1[3];
            pt3[1] = pt2[4];
            pt3[2] = pt2[1];
            g.FillPolygon(sb, pt3);
            pt3[0] = pt1[4];
            pt3[1] = pt2[0];
            pt3[2] = pt2[2];
            g.FillPolygon(sb, pt3);
        }


        private void button10_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            int W = 1000;
            int H = 400;

            int width;
            int height;

            Pen p1;
            Pen p2;

            width = W;
            height = H;

            if (bitmap1 == null)
                bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            p1 = new Pen(Color.Black, 1);
            p2 = new Pen(Color.Pink, 1);

            Point pointa;
            Point pointb;

            int linewidth = 1;


            for (linewidth = 1; linewidth < 8; linewidth++)
            {
                p = new Pen(Color.Black, linewidth);
                for (j = 0; j < (H - 100); j += 10)
                {
                    pointa = new Point((linewidth - 1) * 100, j);
                    pointb = new Point(linewidth * 100, j);
                    g.DrawLine(p, pointa, pointb);
                }
            }

            for (i = 0; i < W; i += 10)
            {
                p = new Pen(Color.Black, 1);
                pointa = new Point(i, 0);
                pointb = new Point(i, H);
                g.DrawLine(p, pointa, pointb);
            }

            for (i = 0; i < W; i += 5)
            {
                p = new Pen(Color.Black, 1);
                pointa = new Point(i, H - 100);
                pointb = new Point(i, H - 50);
                g.DrawLine(p, pointa, pointb);
            }

            for (i = 0; i < W; i += 3)
            {
                p = new Pen(Color.Black, 1);
                pointa = new Point(i, H - 50);
                pointb = new Point(i, H - 0);
                g.DrawLine(p, pointa, pointb);
            }

            pictureBox1.Image = bitmap1;

        }

        private void button18_Click(object sender, EventArgs e)
        {
            //製作icon
            //一個ICON圖標的轉換程序
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            string icon_filename = Application.StartupPath + "\\ICO_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".ico";
            FileStream fs = new FileStream(icon_filename, FileMode.Create);

            Icon icon = ConvertBitmap2Ico(bitmap1);
            this.Icon = icon;   //顯示出來
            icon.Save(fs);//将Icon保存的指定的输出
            fs.Close();
        }

        /// <summary>
        /// 實現bitmap到ico的轉換
        /// </summary>
        /// <param name="bitmap">原圖</param>
        /// <returns>轉換後的指定大小的圖標</returns>
        private Icon ConvertBitmap2Ico(Bitmap bitmap)
        {
            Size size = new Size(256, 256); //用於保存目標圖標的大小
            Bitmap icoBitmap = new Bitmap(bitmap, size);//創建制定大小的原位圖

            //獲得原位圖的圖標句柄
            IntPtr hIco = icoBitmap.GetHicon();
            //從圖標的指定WINDOWS句柄創建Icon
            Icon icon = Icon.FromHandle(hIco);

            return icon;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //畫在一起
            Bitmap bitmap1 = new Bitmap(1640, 480);
            Color background_color = Color.White;
            Color foreground_color = Color.Red;
            pictureBox1.Image = bitmap1;

            int type = 0;       //種類
            int x_st = 0;     //icon的 位置 X
            int y_st = 0;     //icon的 位置 Y
            int width = 80;     //icon的 寬
            int height = 80;    //icon的 高
            int dx = width + 20;
            int dy = height + 20;

            type = ICON_PLAY_PAUSE;
            x_st = 0;
            y_st = 0;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_STOP;
            x_st += dx;
            y_st = 0;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_PAUSE;
            x_st += dx;
            y_st = 0;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_EMPTY;
            x_st += dx;
            y_st = 0;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_NEXT;
            x_st += dx;
            y_st = 0;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_PREVIOUS;
            x_st += dx;
            y_st = 0;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_PLUS;
            x_st = 0;
            y_st = dy;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_MINUS;
            x_st += dx;
            y_st = dy;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_LEFT;
            x_st += dx;
            y_st = dy;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_RIGHT;
            x_st += dx;
            y_st = dy;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_UP;
            x_st += dx;
            y_st = dy;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_DOWN;
            x_st += dx;
            y_st = dy;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);

            type = ICON_RECORD;
            x_st = 0;
            y_st = dy * 2;
            draw_icon(bitmap1, type, x_st, y_st, width, height, background_color, foreground_color);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;
            int s = 5;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 8);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;

            Point pointa;
            Point pointb;

            pointa = new Point(width * 0 / 4 + 10, height / 3 + s);
            pointb = new Point(width * 4 / 4 - 10, height / 3 - s);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 0 / 4 + 10, height * 2 / 3 + s);
            pointb = new Point(width * 4 / 4 - 10, height * 2 / 3 - s);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 3, height * 0 / 4 + 10);
            pointb = new Point(width * 1 / 3, height * 4 / 4 - 10);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 2 / 3, height * 0 / 4 + 10);
            pointb = new Point(width * 2 / 3, height * 4 / 4 - 10);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            int r = 15;
            int cx;
            int cy;
            p = new Pen(foreground_color, 6);

            cx = width / 6;
            cy = height / 6;
            DrawCircle(g, p, cx, cy, r);

            cx = width * 5 / 6;
            cy = height * 5 / 6;
            DrawCircle(g, p, cx, cy, r);

            cx = width / 6;
            cy = height * 5 / 6;
            DrawCross(g, p, cx, cy, r);

            cx = width * 3 / 6;
            cy = height * 3 / 6;
            DrawCross(g, p, cx, cy, r);

            pictureBox1.Image = bitmap1;
        }

        void DrawCircle(Graphics g, Pen p, int cx, int cy, int r)
        {
            g.DrawEllipse(p, cx - r, cy - r, r * 2, r * 2);
        }

        void DrawCross(Graphics g, Pen p, int cx, int cy, int r)
        {
            //g.DrawEllipse(p, cx - r, cy - r, r * 2, r * 2);
            Point pointa;
            Point pointb;

            pointa = new Point(cx + r, cy - r);
            pointb = new Point(cx - r, cy + r);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(cx - r, cy - r);
            pointb = new Point(cx + r, cy + r);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.
        }

        private const int ICON_EMPTY = 0;   //空白
        private const int ICON_PLAY = 1;   //播放
        private const int ICON_PLAY_PAUSE = 2;   //播放/暫停
        private const int ICON_PAUSE = 3;   //暫停
        private const int ICON_STOP = 4;   //停止
        private const int ICON_NEXT = 5;   //下一首
        private const int ICON_PREVIOUS = 6;   //上一首
        private const int ICON_FASTF = 7;   //快進
        private const int ICON_REVERSEF = 8;   //快退
        private const int ICON_RECORD = 9;   //錄影
        private const int ICON_PLUS = 10;   //加
        private const int ICON_MINUS = 11;   //減
        private const int ICON_UP = 12;   //上
        private const int ICON_DOWN = 13;   //下
        private const int ICON_LEFT = 14;   //左
        private const int ICON_RIGHT = 15;   //右
        private const int ICON_OPEN = 20;   //開啟檔案
        private const int ICON_CLOSE = 21;   //關閉檔案

        void draw_icon(Bitmap bitmap1, int type, int x_st, int y_st, int width, int height, Color background_color, Color foreground_color)
        {
            //畫在一起
            Pen p;
            SolidBrush sb;

            p = new Pen(foreground_color, 3);
            sb = new SolidBrush(foreground_color);

            Graphics g = Graphics.FromImage(bitmap1);

            int xx;
            int yy;
            Point[] points;

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(x_st + xx, y_st + yy, background_color);
                }
            }

            if (type == ICON_PLAY_PAUSE)    //播放/暫停
            {
                points = new Point[3];
                points[0] = new Point(x_st + width / 8, y_st + height * 2 / 8);
                points[1] = new Point(x_st + width / 2, y_st + height / 2);
                points[2] = new Point(x_st + width / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);

                g.FillRectangle(sb, new Rectangle(x_st + width / 2, y_st + height * 2 / 8, width / 8, height / 2));
                g.FillRectangle(sb, new Rectangle(x_st + width / 2 + width * 2 / 8, y_st + height * 2 / 8, width / 8, height / 2));
            }
            else if (type == ICON_STOP)    //停止
            {
                g.FillRectangle(sb, new Rectangle(x_st + width / 8, y_st + height / 8, width * 6 / 8, height * 6 / 8));
            }
            else if (type == ICON_PAUSE)    //暫停
            {
                g.FillRectangle(sb, new Rectangle(x_st + width * 3 / 16, y_st + height * 2 / 8, width * 4 / 16, height / 2));
                g.FillRectangle(sb, new Rectangle(x_st + width * 9 / 16, y_st + height * 2 / 8, width * 4 / 16, height / 2));
            }
            else if (type == ICON_EMPTY)    //空白
            {

            }
            else if (type == ICON_NEXT)    //下一首
            {
                points = new Point[3];
                points[0] = new Point(x_st + width / 8 + width / 8, y_st + height * 2 / 8);
                points[1] = new Point(x_st + width / 2 + width / 8, y_st + height / 2);
                points[2] = new Point(x_st + width / 8 + width / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);

                g.FillRectangle(sb, new Rectangle(x_st + width / 2 + width / 8, y_st + height * 2 / 8, width / 8, height / 2));
            }
            else if (type == ICON_PREVIOUS)    //上一首
            {
                points = new Point[3];
                points[0] = new Point(x_st + width * 6 / 8, y_st + height * 2 / 8);
                points[1] = new Point(x_st + width / 8 + width / 8 + width / 8, y_st + height / 2);
                points[2] = new Point(x_st + width * 6 / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);

                g.FillRectangle(sb, new Rectangle(x_st + width / 8 + width / 8, y_st + height * 2 / 8, width / 8, height / 2));

            }
            else if (type == ICON_PLUS)    //加
            {
                g.FillRectangle(sb, new Rectangle(x_st + width / 8, y_st + height * 7 / 16, width * 6 / 8, height * 2 / 16));
                g.FillRectangle(sb, new Rectangle(x_st + width * 7 / 16, y_st + height / 8, width * 2 / 16, height * 6 / 8));
            }
            else if (type == ICON_MINUS)    //減
            {
                g.FillRectangle(sb, new Rectangle(x_st + width / 8, y_st + height * 7 / 16, width * 6 / 8, height * 2 / 16));
            }
            else if (type == ICON_UP)    //上
            {
                points = new Point[3];
                points[0] = new Point(x_st + width * 4 / 8, y_st + height * 2 / 8);
                points[1] = new Point(x_st + width * 6 / 8, y_st + height * 6 / 8);
                points[2] = new Point(x_st + width * 2 / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);
            }
            else if (type == ICON_DOWN)    //下
            {
                points = new Point[3];
                points[0] = new Point(x_st + width * 4 / 8, y_st + height * 6 / 8);
                points[1] = new Point(x_st + width * 6 / 8, y_st + height * 2 / 8);
                points[2] = new Point(x_st + width * 2 / 8, y_st + height * 2 / 8);
                g.FillPolygon(sb, points);

            }
            else if (type == ICON_LEFT)    //左
            {
                points = new Point[3];
                points[0] = new Point(x_st + width * 2 / 8, y_st + height * 4 / 8);
                points[1] = new Point(x_st + width * 6 / 8, y_st + height * 2 / 8);
                points[2] = new Point(x_st + width * 6 / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);
            }
            else if (type == ICON_RIGHT)    //右
            {
                points = new Point[3];
                points[0] = new Point(x_st + width * 2 / 8, y_st + height * 2 / 8);
                points[1] = new Point(x_st + width * 6 / 8, y_st + height * 4 / 8);
                points[2] = new Point(x_st + width * 2 / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);
            }
            else if (type == ICON_RECORD)    //錄影
            {
                g.FillEllipse(sb, new Rectangle(x_st + width / 4, y_st + height / 4, width / 2, height / 2));
            }
        }
    }
}
