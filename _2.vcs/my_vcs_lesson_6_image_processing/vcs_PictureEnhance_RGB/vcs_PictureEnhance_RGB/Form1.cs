using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace vcs_PictureEnhance_RGB
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\______test_files\ims01.bmp";
        //string filename1 = @"C:\______test_files\color1.bmp";
        //string filename2 = @"C:\______test_files\color2.bmp";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox2.Image = Image.FromFile(filename1);
            pictureBox2.MouseDown += new MouseEventHandler(pictureBox2_MouseDown);
            pictureBox2.MouseMove += new MouseEventHandler(pictureBox2_MouseMove);
            pictureBox2.MouseUp += new MouseEventHandler(pictureBox2_MouseUp);
            pictureBox2.Paint += new PaintEventHandler(pictureBox2_Paint);

            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            int W = 640;
            int H = 480;

            x_st = 10;
            y_st = 10;
            dx = W + 10;
            dy = H + 10;

            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox3.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox4.SizeMode = PictureBoxSizeMode.Normal;

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            dy = 50;
            button1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button3.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            richTextBox1.Size = new Size(500, H * 2 + 10);
            richTextBox1.Location = new Point(x_st + dx * 2 + 100, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void evaluate_bitmap_data(Bitmap bitmap1, int x_st, int y_st, int w, int h, out int R_max, out int R_min, out int G_max, out int G_min, out int B_max, out int B_min)
        {
            int i;
            int j;
            Color pt;

            R_max = 0;
            R_min = 255;
            G_max = 0;
            G_min = 255;
            B_max = 0;
            B_min = 255;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    if (R_max < pt.R)
                        R_max = pt.R;
                    if (G_max < pt.G)
                        G_max = pt.G;
                    if (B_max < pt.B)
                        B_max = pt.B;
                    if (R_min > pt.R)
                        R_min = pt.R;
                    if (G_min > pt.G)
                        G_min = pt.G;
                    if (B_min > pt.B)
                        B_min = pt.B;
                }
            }
            /*
            richTextBox1.Text += "R_max = " + R_max.ToString() + "\tR_min = " + R_min.ToString() + "\n";
            richTextBox1.Text += "G_max = " + G_max.ToString() + "\tG_min = " + G_min.ToString() + "\n";
            richTextBox1.Text += "B_max = " + B_max.ToString() + "\tB_min = " + B_min.ToString() + "\n";
            */
        }

        void enhance_bitmap_data(Bitmap bitmap1, int x_st, int y_st, int w, int h, int R_max, int R_min, int G_max, int G_min, int B_max, int B_min)
        {
            int i;
            int j;
            Color pt;


            int diff_R = R_max - R_min;
            int diff_G = G_max - G_min;
            int diff_B = B_max - B_min;

            if (diff_R == 0)
                diff_R = 1;
            if (diff_G == 0)
                diff_G = 1;
            if (diff_B == 0)
                diff_B = 1;

            float ratio_R = 255 / (float)diff_R;
            float ratio_G = 255 / (float)diff_G;
            float ratio_B = 255 / (float)diff_B;

            /*
            richTextBox1.Text += "ratio_R = " + ratio_R.ToString("F2") + "\n";
            richTextBox1.Text += "ratio_G = " + ratio_G.ToString("F2") + "\n";
            richTextBox1.Text += "ratio_B = " + ratio_B.ToString("F2") + "\n";
            */

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    if (R_max < pt.R)
                        R_max = pt.R;
                    if (G_max < pt.G)
                        G_max = pt.G;
                    if (B_max < pt.B)
                        B_max = pt.B;
                    if (R_min > pt.R)
                        R_min = pt.R;
                    if (G_min > pt.G)
                        G_min = pt.G;
                    if (B_min > pt.B)
                        B_min = pt.B;
                }
            }
            /*
            richTextBox1.Text += "R_max = " + R_max.ToString() + "\tR_min = " + R_min.ToString() + "\n";
            richTextBox1.Text += "G_max = " + G_max.ToString() + "\tG_min = " + G_min.ToString() + "\n";
            richTextBox1.Text += "B_max = " + B_max.ToString() + "\tB_min = " + B_min.ToString() + "\n";
            */
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    int R_new = (int)((pt.R - R_min) * ratio_R);
                    int G_new = (int)((pt.G - G_min) * ratio_G);
                    int B_new = (int)((pt.B - B_min) * ratio_B);


                    bitmap1.SetPixel(x_st + i, y_st + j, Color.FromArgb(255, R_new, G_new, B_new));

                }
            }
        }

        void show_part_image(Bitmap bitmap1, int x_st, int y_st, int w, int h)
        {
            Bitmap bitmap3 = bitmap1.Clone(new Rectangle(x_st, y_st, w, h), PixelFormat.Format32bppArgb);

            pictureBox3.Image = bitmap3;

            if ((w > 640 / 2) || (h > 480 / 2))
            {
                pictureBox4.Image = null;
                return;
            }

            //準備放大兩倍
            richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + ", w = " + w.ToString() + ", h = " + h.ToString() + "\n";

            Bitmap bitmap4 = new Bitmap(w * 2, h * 2);
            int i;
            int j;
            Color p;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    p = bitmap3.GetPixel(i, j);
                    bitmap4.SetPixel(i * 2, j * 2, p);
                    bitmap4.SetPixel(i * 2, j * 2 + 1, p);
                    bitmap4.SetPixel(i * 2 + 1, j * 2, p);
                    bitmap4.SetPixel(i * 2 + 1, j * 2 + 1, p);
                }
            }
            pictureBox4.Image = bitmap4;
        }

        void draw_enhanced_image(int x_st, int y_st, int w, int h)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);

            int R_max = 0;
            int R_min = 255;
            int G_max = 0;
            int G_min = 255;
            int B_max = 0;
            int B_min = 255;

            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            enhance_bitmap_data(bitmap1, x_st, y_st, w, h, R_max, R_min, G_max, G_min, B_max, B_min);
            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = W / 8;
            int y_st = H / 8;
            int w = W * 3 / 4;
            int h = H * 3 / 4;

            int R_max = 0;
            int R_min = 255;
            int G_max = 0;
            int G_min = 255;
            int B_max = 0;
            int B_min = 255;

            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            enhance_bitmap_data(bitmap1, x_st, y_st, w, h, R_max, R_min, G_max, G_min, B_max, B_min);
            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);
            //g.Clear(Color.White);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = 50;
            int y_st = 50;
            int w = W / 2;
            int h = H / 2;

            int R_max = 0;
            int R_min = 255;
            int G_max = 0;
            int G_min = 255;
            int B_max = 0;
            int B_min = 255;

            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            enhance_bitmap_data(bitmap1, x_st, y_st, w, h, R_max, R_min, G_max, G_min, B_max, B_min);
            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);
            //g.Clear(Color.White);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = W / 3;
            int y_st = H / 3;
            int w = W / 3;
            int h = H / 3;

            int R_max = 0;
            int R_min = 255;
            int G_max = 0;
            int G_min = 255;
            int B_max = 0;
            int B_min = 255;

            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            enhance_bitmap_data(bitmap1, x_st, y_st, w, h, R_max, R_min, G_max, G_min, B_max, B_min);
            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;

        }

        private void button4_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);
            //g.Clear(Color.White);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = W / 12;
            int y_st = H / 4;
            int w = W / 10;
            int h = H / 10;

            int R_max = 0;
            int R_min = 255;
            int G_max = 0;
            int G_min = 255;
            int B_max = 0;
            int B_min = 255;

            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            enhance_bitmap_data(bitmap1, x_st, y_st, w, h, R_max, R_min, G_max, G_min, B_max, B_min);
            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;

        }

        private void button5_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);
            //g.Clear(Color.White);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = W / 3;
            int y_st = H / 3 - 50;
            int w = W / 3;
            int h = H / 3;

            int R_max = 0;
            int R_min = 255;
            int G_max = 0;
            int G_min = 255;
            int B_max = 0;
            int B_min = 255;

            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            enhance_bitmap_data(bitmap1, x_st, y_st, w, h, R_max, R_min, G_max, G_min, B_max, B_min);
            evaluate_bitmap_data(bitmap1, x_st, y_st, w, h, out R_max, out R_min, out G_max, out G_min, out B_max, out B_min);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;

        }

        bool flag_pictureBox2_mouse_down = false;
        int pictureBox2_position_x_old = 0;
        int pictureBox2_position_y_old = 0;

        int draw_x_st = 0;
        int draw_y_st = 0;
        int draw_w = 0;
        int draw_h = 0;

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            flag_pictureBox2_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            pictureBox2_position_x_old = e.X;
            pictureBox2_position_y_old = e.Y;
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox2_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox2_position_x_old;
                int dy = e.Y - pictureBox2_position_y_old;

                if (dx > 0)
                {
                    draw_x_st = pictureBox2_position_x_old;
                    draw_w = dx;
                }
                else
                {
                    draw_x_st = e.X;
                    draw_w = -dx;
                }

                if (dy > 0)
                {
                    draw_y_st = pictureBox2_position_y_old;
                    draw_h = dy;
                }
                else
                {
                    draw_y_st = e.Y;
                    draw_h = -dy;
                }

                this.pictureBox2.Invalidate();
                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                //pictureBox2.Location = new Point(pictureBox2.Location.X + dx, pictureBox2.Location.Y + dy);
            }
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pictureBox2_mouse_down = false;
            //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";

            int W = 640;
            int H = 480;

            if ((draw_x_st < 0) || (draw_x_st >= W))
                return;
            if ((draw_y_st < 0) || (draw_y_st >= H))
                return;
            if ((draw_w < 0) || (draw_w > W))
                return;
            if ((draw_h < 0) || (draw_h > H))
                return;
            if (((draw_x_st + draw_w) > W) || ((draw_y_st + draw_h) > H))
                return;

            draw_enhanced_image(draw_x_st, draw_y_st, draw_w, draw_h);
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            //richTextBox1.Text += draw_x_st.ToString() + "\t" + draw_y_st.ToString() + "\t" + draw_w.ToString() + "\t" + draw_h.ToString() + "\n";
            e.Graphics.DrawRectangle(new Pen(Color.Blue, 3), draw_x_st, draw_y_st, draw_w, draw_h);
        }
    }
}

