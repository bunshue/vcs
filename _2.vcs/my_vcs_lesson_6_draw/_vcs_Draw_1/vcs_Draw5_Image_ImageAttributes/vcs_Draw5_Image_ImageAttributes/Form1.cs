using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;  // for ColorMatrix, ImageAttributes
using System.Drawing.Drawing2D;  // for SmoothingMode

namespace vcs_Draw5_Image_ImageAttributes
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1;
        Graphics g;
        bool flag_color_matrix_valid = true;
        int W = 800;
        int H = 700;
        string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";

        // 色彩調整矩陣 標準
        float[][] matrix =
        {
            new float[] {1, 0, 0, 0, 0},
            new float[] {0, 1, 0, 0, 0},
            new float[] {0, 0, 1, 0, 0},
            new float[] {0, 0, 0, 1, 0},
            new float[] {0, 0, 0, 0, 1}
        };

        // 色彩調整矩陣 標準
        float[][] matrix_identity =
        {
            new float[] {1, 0, 0, 0, 0},
            new float[] {0, 1, 0, 0, 0},
            new float[] {0, 0, 1, 0, 0},
            new float[] {0, 0, 0, 1, 0},
            new float[] {0, 0, 0, 0, 1}
        };

        // 色彩調整矩陣 Sepia
        float[][] matrix_sepia =
        {
            //           紅對紅00 紅對綠01 紅對藍02
            new float[] {0.393f,  0.349f,  0.272f,  0, 0},  // 紅
            //           綠對紅10 綠對綠11 綠對藍12
            new float[] {0.769f,  0.686f,  0.534f,  0, 0},  // 綠
            //           藍對紅20 藍對綠21 藍對藍22
            new float[] {0.189f,  0.168f,  0.131f,  0, 0},  // 藍
            new float[] {0,       0,       0,       1, 0},
            new float[] {0,       0,       0,       0, 1},
        };

        // 色彩調整矩陣 灰階1
        float[][] matrix_gray =
        {
            new float[] {0.299f, 0.299f, 0.299f, 0, 0},
            new float[] {0.587f, 0.587f, 0.587f, 0, 0},
            new float[] {0.114f, 0.114f, 0.114f, 0, 0},
            new float[] {0,      0,      0,      1, 0},
            new float[] {0,      0,      0,      0, 1}
        };

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //指定畫布大小
            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.SmoothingMode = SmoothingMode.HighQuality;

            pictureBox2.Image = Image.FromFile(filename);
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
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

            pictureBox1.Size = new Size(W, H);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 300);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y);

            pictureBox2.Size = new Size(300, H / 2);
            pictureBox2.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;

            richTextBox1.Size = new Size(300, H / 2);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0 + H / 2 + 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            int xx = x_st + dx * 2;
            int yy = y_st + dy * 0;
            dx = 80 + 10;
            dy = 36 + 20;
            int dd = 20;
            lb_cm00.Location = new Point(xx + dx * 0, yy + dy * 0);
            lb_cm01.Location = new Point(xx + dx * 1, yy + dy * 0);
            lb_cm02.Location = new Point(xx + dx * 2, yy + dy * 0);
            lb_cm03.Location = new Point(xx + dx * 3, yy + dy * 0);
            lb_cm04.Location = new Point(xx + dx * 4, yy + dy * 0);
            lb_cm10.Location = new Point(xx + dx * 0, yy + dy * 1);
            lb_cm11.Location = new Point(xx + dx * 1, yy + dy * 1);
            lb_cm12.Location = new Point(xx + dx * 2, yy + dy * 1);
            lb_cm13.Location = new Point(xx + dx * 3, yy + dy * 1);
            lb_cm14.Location = new Point(xx + dx * 4, yy + dy * 1);
            lb_cm20.Location = new Point(xx + dx * 0, yy + dy * 2);
            lb_cm21.Location = new Point(xx + dx * 1, yy + dy * 2);
            lb_cm22.Location = new Point(xx + dx * 2, yy + dy * 2);
            lb_cm23.Location = new Point(xx + dx * 3, yy + dy * 2);
            lb_cm24.Location = new Point(xx + dx * 4, yy + dy * 2);
            lb_cm30.Location = new Point(xx + dx * 0, yy + dy * 3);
            lb_cm31.Location = new Point(xx + dx * 1, yy + dy * 3);
            lb_cm32.Location = new Point(xx + dx * 2, yy + dy * 3);
            lb_cm33.Location = new Point(xx + dx * 3, yy + dy * 3);
            lb_cm34.Location = new Point(xx + dx * 4, yy + dy * 3);
            lb_cm40.Location = new Point(xx + dx * 0, yy + dy * 4);
            lb_cm41.Location = new Point(xx + dx * 1, yy + dy * 4);
            lb_cm42.Location = new Point(xx + dx * 2, yy + dy * 4);
            lb_cm43.Location = new Point(xx + dx * 3, yy + dy * 4);
            lb_cm44.Location = new Point(xx + dx * 4, yy + dy * 4);

            tb_cm00.Location = new Point(xx + dx * 0, yy + dy * 0 + dd);
            tb_cm01.Location = new Point(xx + dx * 1, yy + dy * 0 + dd);
            tb_cm02.Location = new Point(xx + dx * 2, yy + dy * 0 + dd);
            tb_cm03.Location = new Point(xx + dx * 3, yy + dy * 0 + dd);
            tb_cm04.Location = new Point(xx + dx * 4, yy + dy * 0 + dd);
            tb_cm10.Location = new Point(xx + dx * 0, yy + dy * 1 + dd);
            tb_cm11.Location = new Point(xx + dx * 1, yy + dy * 1 + dd);
            tb_cm12.Location = new Point(xx + dx * 2, yy + dy * 1 + dd);
            tb_cm13.Location = new Point(xx + dx * 3, yy + dy * 1 + dd);
            tb_cm14.Location = new Point(xx + dx * 4, yy + dy * 1 + dd);
            tb_cm20.Location = new Point(xx + dx * 0, yy + dy * 2 + dd);
            tb_cm21.Location = new Point(xx + dx * 1, yy + dy * 2 + dd);
            tb_cm22.Location = new Point(xx + dx * 2, yy + dy * 2 + dd);
            tb_cm23.Location = new Point(xx + dx * 3, yy + dy * 2 + dd);
            tb_cm24.Location = new Point(xx + dx * 4, yy + dy * 2 + dd);
            tb_cm30.Location = new Point(xx + dx * 0, yy + dy * 3 + dd);
            tb_cm31.Location = new Point(xx + dx * 1, yy + dy * 3 + dd);
            tb_cm32.Location = new Point(xx + dx * 2, yy + dy * 3 + dd);
            tb_cm33.Location = new Point(xx + dx * 3, yy + dy * 3 + dd);
            tb_cm34.Location = new Point(xx + dx * 4, yy + dy * 3 + dd);
            tb_cm40.Location = new Point(xx + dx * 0, yy + dy * 4 + dd);
            tb_cm41.Location = new Point(xx + dx * 1, yy + dy * 4 + dd);
            tb_cm42.Location = new Point(xx + dx * 2, yy + dy * 4 + dd);
            tb_cm43.Location = new Point(xx + dx * 3, yy + dy * 4 + dd);
            tb_cm44.Location = new Point(xx + dx * 4, yy + dy * 4 + dd);

            bt_cm_apply.Location = new Point(xx + dx * 5, yy + dy * 0 + dd);
            bt_cm_reset.Location = new Point(xx + dx * 5, yy + dy * 1 + dd);
            bt_brightness.Location = new Point(xx + dx * 5, yy + dy * 2 + dd);
            bt_gray.Location = new Point(xx + dx * 5, yy + dy * 3 + dd);
            bt_sepia.Location = new Point(xx + dx * 5, yy + dy * 4 + dd);
            bt_alpha.Location = new Point(xx + dx * 6, yy + dy * 2 + dd);

            groupBox1.Size = new Size(120, 150);
            groupBox1.Location = new Point(xx + dx * 7 + 80, yy + dy * 0);

            y_st = 20;
            dy = 30;
            radioButton0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            radioButton1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            radioButton2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            radioButton3.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            this.Size = new Size(1600, 880);
            this.Text = "vcs_Draw5_Image_ImageAttributes";

            lb_cm00.Text = "紅對紅00";
            lb_cm01.Text = "紅對綠01";
            lb_cm02.Text = "紅對藍02";
            lb_cm03.Text = "x";
            lb_cm04.Text = "x";
            lb_cm10.Text = "綠對紅10";
            lb_cm11.Text = "綠對綠11";
            lb_cm12.Text = "綠對藍12";
            lb_cm13.Text = "x";
            lb_cm14.Text = "x";
            lb_cm20.Text = "藍對紅20";
            lb_cm21.Text = "藍對綠21";
            lb_cm22.Text = "藍對藍22";
            lb_cm23.Text = "x";
            lb_cm24.Text = "x";
            lb_cm30.Text = "紅平移比";
            lb_cm31.Text = "綠平移比";
            lb_cm32.Text = "藍平移比";
            lb_cm33.Text = "全體Alpha(0~1)";
            lb_cm34.Text = "x";
            lb_cm40.Text = "紅平移比";
            lb_cm41.Text = "綠平移比";
            lb_cm42.Text = "藍平移比";
            lb_cm43.Text = "x";
            lb_cm44.Text = "x";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            int W = 640;
            int H = 480;
            Bitmap bitmap1 = new Bitmap(W, H);

            //string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_game\airplane.bmp";
            pictureBox2.Image = Image.FromFile(filename);

            Bitmap bmp = new Bitmap(filename);

            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Pink);

            //使用 color matrix, 設定 Alpha = 0.5
            ColorMatrix cm = new ColorMatrix();
            //print_ColorMatrix(cm);
            cm.Matrix33 = 0.5f;  // 設定Alpha = 0.5
            //cm.Matrix33 = 1.0f;  // 設定Alpha = 0.5
            //print_ColorMatrix(cm);

            ImageAttributes ia = new ImageAttributes();

            ia.SetColorMatrix(cm);

            // Make pixels that are the same color as the
            // one in the upper left transparent.
            // bmp.MakeTransparent(bmp.GetPixel(5, 60));  // 設定邊角點的顏色為透明色

            // 貼上使用CM轉換過的影像
            g.DrawImage(bmp, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;
        }

        float alpha = 0f;
        private void button1_Click(object sender, EventArgs e)
        {
            //透明度

            alpha += 0.1f;
            if (alpha > 1)
                alpha = 0;

            g.Clear(Color.Pink);
            //使用 color matrix
            ColorMatrix cm = new ColorMatrix();
            cm.Matrix33 = alpha; // 透明度
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm);

            // 貼上使用CM轉換過的影像
            Bitmap bmp = new Bitmap(filename);
            g.DrawImage(bmp, new Rectangle(0, 0, W, H), 0, 0, W, H, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用Alpha

            float t = 0.60f; //transparency;

            // 色彩調整矩陣 透明度
            float[][] matrix =
            {
                new float[] {1, 0, 0, 0, 0},
                new float[] {0, 1, 0, 0, 0},
                new float[] {0, 0, 1, 0, 0},
                new float[] {0, 0, 0, t, 0},  // Matrix33 Alpha
                new float[] {0, 0, 0, 0, 1},
            };

            do_color_matrix(matrix);
        }

        void do_color_matrix(float[][] matrix)
        {
            g.Clear(Color.White);

            //貼上無調整的影像(大圖)
            string filename0 = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            Bitmap bmp0 = new Bitmap(filename0);
            g.DrawImage(bmp0, 0, 0, bmp0.Width, bmp0.Height);

            //小圖
            string filename = @"D:\_git\vcs\_1.data\______test_files1\_material\ims3.bmp";
            Bitmap bmp = new Bitmap(filename);
            bmp.MakeTransparent(bmp.GetPixel(10, 10));  // 設定邊角點的顏色為透明色

            //使用 color matrix
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm);

            //貼上有調整的影像
            // 貼上使用CM轉換過的影像
            g.DrawImage(bmp, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //測試 ColorMatrix

            // 色彩調整矩陣 透明度 20%
            float[][] matrix =
            {
                new float[] {1, 0, 0, 0,    0},
                new float[] {0, 1, 0, 0,    0},
                new float[] {0, 0, 1, 0,    0},
                new float[] {0, 0, 0, 0.2f, 0},  // Matrix33 Alpha
                new float[] {0, 0, 0, 0,    1}
            };
            //使用 color matrix
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            pictureBox2.Image = Image.FromFile(filename);

            Bitmap bmp = new Bitmap(filename);

            g.DrawRectangle(Pens.Red, 100, 100, 100, 100);
            g.DrawImage(bmp, 0, 0, bmp.Width / 2, bmp.Height / 2);

            Rectangle dest2 = new Rectangle(0, 300, bmp.Width / 2, bmp.Height / 2);
            // 貼上使用CM轉換過的影像
            g.DrawImage(bmp, dest2, 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //彩虹化圖片28
            string filename = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Graphics gr = Graphics.FromImage(bitmap2);
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
                float[][] matrix =
                {
                    new float[] {color[i].R / 255f * scale, 0, 0, 0, 0},
                    new float[] {0, color[i].G / 255f * scale, 0, 0, 0},
                    new float[] {0, 0, color[i].B / 255f * scale, 0, 0},
                    new float[] {0, 0, 0, 1, 0},
                    new float[] {0, 0, 0, 0, 1},
                };
                //使用 color matrix
                ColorMatrix cm = new ColorMatrix(matrix);
                ImageAttributes ia = new ImageAttributes();
                ia.SetColorMatrix(cm);

                // Draw the next part of the image.
                int x = (int)(i * bitmap1.Width / color.Length);
                Point[] points =
                {
                    new Point(x, 0),
                    new Point(W, 0),
                    new Point(x, H),
                };
                Rectangle rect = new Rectangle(x, 0, W - x, H);
                // 貼上使用CM轉換過的影像
                gr.DrawImage(bitmap1, points, rect, GraphicsUnit.Pixel, ia);

                //改用, 免用points rect
                //g.DrawImage(bmp, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);
            }
            pictureBox1.Image = bitmap2;
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (get_color_matrix() == false)
            {
                richTextBox1.Text += "取得CM失敗\n";
                return;
            }
            else
            {
                richTextBox1.Text += "取得CM OK\n";
            }
            print_color_matrix(matrix);
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }


        public struct RGB
        {
            private byte _r;
            private byte _g;
            private byte _b;

            public RGB(byte r, byte g, byte b)
            {
                this._r = r;
                this._g = g;
                this._b = b;
            }

            public byte R
            {
                get { return this._r; }
                set { this._r = value; }
            }

            public byte G
            {
                get { return this._g; }
                set { this._g = value; }
            }

            public byte B
            {
                get { return this._b; }
                set { this._b = value; }
            }

            public bool Equals(RGB rgb)
            {
                return (this.R == rgb.R) && (this.G == rgb.G) && (this.B == rgb.B);
            }
        }

        public struct YUV
        {
            private double _y;
            private double _u;
            private double _v;

            public YUV(double y, double u, double v)
            {
                this._y = y;
                this._u = u;
                this._v = v;
            }

            public double Y
            {
                get { return this._y; }
                set { this._y = value; }
            }

            public double U
            {
                get { return this._u; }
                set { this._u = value; }
            }

            public double V
            {
                get { return this._v; }
                set { this._v = value; }
            }

            public bool Equals(YUV yuv)
            {
                return (this.Y == yuv.Y) && (this.U == yuv.U) && (this.V == yuv.V);
            }
        }

        public static YUV RGBToYUV(RGB rgb)
        {
            double y = rgb.R * .299000 + rgb.G * .587000 + rgb.B * .114000;
            double u = rgb.R * -.168736 + rgb.G * -.331264 + rgb.B * .500000 + 128;
            double v = rgb.R * .500000 + rgb.G * -.418688 + rgb.B * -.081312 + 128;

            return new YUV(y, u, v);
        }

        Bitmap measure_gray_scale(Bitmap bmp)
        {
            int w = 40;
            int h = 40;
            int W = w * 16;
            int H = h * 16;

            int[] Y = new int[256];

            for (int i = 0; i < 256; i++)
            {
                int x_st = i * 2;
                int y_st = 100;

                Color p = bmp.GetPixel(x_st, y_st);
                RGB pp = new RGB(p.R, p.G, p.B);
                YUV yyy = new YUV();
                yyy = RGBToYUV(pp);
                Y[i] = (int)yyy.Y;
            }
            /*
            for (int i = 0; i < 256; i++)
            {
                richTextBox1.Text += Y[i].ToString("D3");
                if (i % 16 == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                {
                    richTextBox1.Text += " ";
                }
            }
            */
            Point[] curvePoints = new Point[256];    //一維陣列內有 256 個Point

            for (int i = 0; i < 256; i++)
            {
                curvePoints[i].X = i;
                curvePoints[i].Y = 255 - Y[i];
            }

            Bitmap b = new Bitmap(256 + 10, 256 + 10);
            Graphics g = Graphics.FromImage(b);
            g.DrawLines(Pens.Red, curvePoints);   //畫直線
            g.DrawRectangle(Pens.Green, 0, 0, 256, 256);

            return b;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            // ImageAttributes SetGamma
            // ImageAttributes 測試 Gamma
            // 使用 ImageAttributes 設定 gamma 值

            int BORDER = 10;
            int W = 512 + BORDER + 256 + BORDER;
            int H = 256 * 3 + BORDER * 3;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Pink);

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\gray1.bmp";
            Bitmap bmp = new Bitmap(filename);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //原圖
            int x_st = 0;
            int y_st = 0;
            g.DrawImage(bmp, x_st, y_st, bmp.Width, bmp.Height);
            Bitmap b1 = measure_gray_scale(bmp);
            x_st = 512 + BORDER;
            g.DrawImage(b1, x_st, y_st, b1.Width, b1.Height);
            g.DrawString("Gamma = 1", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(20, 20));

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //經過Gamma處理, gamma = 0.6
            float gamma = 0.6f;  // 0 ~ 2.5, 1.0為不變
            richTextBox1.Text += "Gamma = " + gamma.ToString() + "\n";

            ImageAttributes ia = new ImageAttributes();
            ia.SetGamma(gamma);

            x_st = 0;
            y_st = 256 + BORDER;
            g.DrawImage(bmp, new Rectangle(x_st, y_st, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);
            g.DrawString("Gamma = " + gamma.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + 20, y_st + 20));

            //量測的範圍
            Rectangle rect = new Rectangle(x_st, y_st, bmp.Width, bmp.Height);
            Bitmap b2 = measure_gray_scale(bitmap1.Clone(rect, PixelFormat.Format32bppArgb));
            x_st = 512 + BORDER;
            g.DrawImage(b2, x_st, y_st, b2.Width, b2.Height);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //經過Gamma處理, gamma = 2.2
            gamma = 2.2f;  // 0 ~ 2.5, 1.0為不變
            richTextBox1.Text += "Gamma = " + gamma.ToString() + "\n";

            ia = new ImageAttributes();
            ia.SetGamma(gamma);

            x_st = 0;
            y_st = 256 + BORDER + 256 + BORDER;
            g.DrawImage(bmp, new Rectangle(x_st, y_st, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);
            g.DrawString("Gamma = " + gamma.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + 20, y_st + 20));

            //量測的範圍
            rect = new Rectangle(x_st, y_st, bmp.Width, bmp.Height);
            Bitmap b3 = measure_gray_scale(bitmap1.Clone(rect, PixelFormat.Format32bppArgb));
            x_st = 512 + BORDER;
            g.DrawImage(b3, x_st, y_st, b3.Width, b3.Height);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            pictureBox1.Size = new Size(800, 520);
            pictureBox1.Image = bitmap1;
            richTextBox1.Text += pictureBox1.Size.ToString() + "\n";
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //ImageAttributes SetGamma
            //gamma 0 ~ 2.5, [0 <-明- 1 -暗-> 2]
            float gamma = 2.2f;
            richTextBox1.Text += "Gamma = " + gamma.ToString() + "\n";

            Bitmap bmp = new Bitmap(filename);

            ImageAttributes ia = new ImageAttributes();
            ia.SetGamma(gamma, ColorAdjustType.Bitmap);

            g.DrawImage(bmp, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;

        }

        int cutoff_value = 0;
        private void button12_Click(object sender, EventArgs e)
        {
            // 兩色中間設為透明

            pictureBox1.BackColor = Color.Lime;

            richTextBox1.Text += "亮度 " + cutoff_value.ToString() + " 到 " + (cutoff_value + 20).ToString() + ", 設定為透明\n";

            //string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\gray1.bmp";

            Bitmap bmp = new Bitmap(filename);

            //低顏色
            Color low_color = Color.FromArgb(cutoff_value, cutoff_value, cutoff_value);
            //高顏色
            //Color high_color = Color.FromArgb(255, 255, 255);
            Color high_color = Color.FromArgb(cutoff_value + 20, cutoff_value + 20, cutoff_value + 20);

            ImageAttributes ia = new ImageAttributes();
            ia.SetColorKey(low_color, high_color);

            g.Clear(Color.Pink);

            Rectangle dst_rect = new Rectangle(0, 0, bmp.Width, bmp.Height);
            g.DrawImage(bmp, dst_rect, 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;

            cutoff_value += 20;
            if (cutoff_value > 235)
            {
                cutoff_value = 0;
            }
        }

        float threshold = 0.3f;  // 0 ~ 1.0
        private void button13_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "threshold = " + threshold.ToString() + "\n";

            threshold += 0.06f;
            if (threshold > 1.0f)
            {
                threshold = 0.01f;
            }

            Bitmap bmp = new Bitmap(filename);

            ImageAttributes ia = new ImageAttributes();
            ia.SetThreshold(threshold);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(bmp.Width, 0),
                new Point(0, bmp.Height),
            };
            Rectangle rect = new Rectangle(0, 0, bmp.Width, bmp.Height);

            g.Clear(Color.Pink);

            g.DrawImage(bmp, points, rect, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;
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

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            return;

            //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\color_chart.bmp";
            string filename = "dddd.bmp";
            Bitmap image = new Bitmap(filename);
            int width = image.Width;
            int height = image.Height;
            float degrees = 90f;
            double r = degrees * System.Math.PI / 180; // degrees to radians

            float[][] matrix =
            {
                new float[] {(float)System.Math.Cos(r),   (float)System.Math.Sin(r),   0,  0,  0},
                new float[] {(float)-System.Math.Sin(r),  (float)-System.Math.Cos(r),  0,  0,  0},
                new float[] {0,  0,  1,  0,  0},
                new float[] {0,  0,  0,  1,  0},
                new float[] {0,  0,  0,  0,  1}
            };
            //使用 color matrix
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);

            richTextBox1.Text += "pt = " + image.GetPixel(50,50).ToString()+"\n";

            e.Graphics.DrawImage(image, 10, 10, width, height);

            // 貼上使用CM轉換過的影像
            e.Graphics.DrawImage(
               image,
               new Rectangle(10, 300, width, height),  // destination rectangle 
                0, 0,        // upper-left corner of source rectangle 
                width,       // width of source rectangle
                height,      // height of source rectangle
                GraphicsUnit.Pixel,
               ia);
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            //指定畫布大小
            pictureBox1.Size = new Size(W, H);
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            pictureBox2.Image = Image.FromFile(filename);
        }

        bool get_color_matrix()
        {
            flag_color_matrix_valid = false;

            float cm00 = 0;
            float cm01 = 0;
            float cm02 = 0;
            float cm03 = 0;
            float cm04 = 0;
            float cm10 = 0;
            float cm11 = 0;
            float cm12 = 0;
            float cm13 = 0;
            float cm14 = 0;
            float cm20 = 0;
            float cm21 = 0;
            float cm22 = 0;
            float cm23 = 0;
            float cm24 = 0;
            float cm30 = 0;
            float cm31 = 0;
            float cm32 = 0;
            float cm33 = 0;
            float cm34 = 0;
            float cm40 = 0;
            float cm41 = 0;
            float cm42 = 0;
            float cm43 = 0;
            float cm44 = 0;
            bool conversionSuccessfu00 = float.TryParse(tb_cm00.Text, out cm00);  // out為必須
            if (conversionSuccessfu00 == true)
            {
                //richTextBox1.Text += "得到cm00 : " + cm00 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm00\n";
                return false;
            }
            bool conversionSuccessfu01 = float.TryParse(tb_cm01.Text, out cm01);  // out為必須
            if (conversionSuccessfu01 == true)
            {
                //richTextBox1.Text += "得到cm01 : " + cm01 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm01\n";
                return false;
            }
            bool conversionSuccessfu02 = float.TryParse(tb_cm02.Text, out cm02);  // out為必須
            if (conversionSuccessfu02 == true)
            {
                //richTextBox1.Text += "得到cm02 : " + cm02 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm02\n";
                return false;
            }
            bool conversionSuccessfu03 = float.TryParse(tb_cm03.Text, out cm03);  // out為必須
            if (conversionSuccessfu03 == true)
            {
                //richTextBox1.Text += "得到cm03 : " + cm03 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm03\n";
                return false;
            }
            bool conversionSuccessfu04 = float.TryParse(tb_cm04.Text, out cm04);  // out為必須
            if (conversionSuccessfu04 == true)
            {
                //richTextBox1.Text += "得到cm04 : " + cm04 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm04\n";
                return false;
            }
            bool conversionSuccessfu10 = float.TryParse(tb_cm10.Text, out cm10);  // out為必須
            if (conversionSuccessfu10 == true)
            {
                //richTextBox1.Text += "得到cm10 : " + cm10 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm10\n";
                return false;
            }
            bool conversionSuccessfu11 = float.TryParse(tb_cm11.Text, out cm11);  // out為必須
            if (conversionSuccessfu11 == true)
            {
                //richTextBox1.Text += "得到cm11 : " + cm11 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm11\n";
                return false;
            }
            bool conversionSuccessfu12 = float.TryParse(tb_cm12.Text, out cm12);  // out為必須
            if (conversionSuccessfu12 == true)
            {
                //richTextBox1.Text += "得到cm12 : " + cm12 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm12\n";
                return false;
            }
            bool conversionSuccessfu13 = float.TryParse(tb_cm13.Text, out cm13);  // out為必須
            if (conversionSuccessfu13 == true)
            {
                //richTextBox1.Text += "得到cm13 : " + cm13 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm13\n";
                return false;
            }
            bool conversionSuccessfu14 = float.TryParse(tb_cm14.Text, out cm14);  // out為必須
            if (conversionSuccessfu14 == true)
            {
                //richTextBox1.Text += "得到cm14 : " + cm14 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm14\n";
                return false;
            }
            bool conversionSuccessfu20 = float.TryParse(tb_cm20.Text, out cm20);  // out為必須
            if (conversionSuccessfu20 == true)
            {
                //richTextBox1.Text += "得到cm20 : " + cm20 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm20\n";
                return false;
            }
            bool conversionSuccessfu21 = float.TryParse(tb_cm21.Text, out cm21);  // out為必須
            if (conversionSuccessfu21 == true)
            {
                //richTextBox1.Text += "得到cm21 : " + cm21 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm21\n";
                return false;
            }
            bool conversionSuccessfu22 = float.TryParse(tb_cm22.Text, out cm22);  // out為必須
            if (conversionSuccessfu22 == true)
            {
                //richTextBox1.Text += "得到cm22 : " + cm22 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm22\n";
                return false;
            }
            bool conversionSuccessfu23 = float.TryParse(tb_cm23.Text, out cm23);  // out為必須
            if (conversionSuccessfu23 == true)
            {
                //richTextBox1.Text += "得到cm23 : " + cm23 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm23\n";
                return false;
            }
            bool conversionSuccessfu24 = float.TryParse(tb_cm24.Text, out cm24);  // out為必須
            if (conversionSuccessfu24 == true)
            {
                //richTextBox1.Text += "得到cm24 : " + cm24 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm24\n";
                return false;
            }
            bool conversionSuccessfu30 = float.TryParse(tb_cm30.Text, out cm30);  // out為必須
            if (conversionSuccessfu30 == true)
            {
                //richTextBox1.Text += "得到cm30 : " + cm30 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm30\n";
                return false;
            }
            bool conversionSuccessfu31 = float.TryParse(tb_cm31.Text, out cm31);  // out為必須
            if (conversionSuccessfu31 == true)
            {
                //richTextBox1.Text += "得到cm31 : " + cm31 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm31\n";
                return false;
            }
            bool conversionSuccessfu32 = float.TryParse(tb_cm32.Text, out cm32);  // out為必須
            if (conversionSuccessfu32 == true)
            {
                //richTextBox1.Text += "得到cm32 : " + cm32 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm32\n";
                return false;
            }
            bool conversionSuccessfu33 = float.TryParse(tb_cm33.Text, out cm33);  // out為必須
            if (conversionSuccessfu33 == true)
            {
                //richTextBox1.Text += "得到cm33 : " + cm33 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm33\n";
                return false;
            }
            bool conversionSuccessfu34 = float.TryParse(tb_cm34.Text, out cm34);  // out為必須
            if (conversionSuccessfu34 == true)
            {
                //richTextBox1.Text += "得到cm34 : " + cm34 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm34\n";
                return false;
            }
            bool conversionSuccessfu40 = float.TryParse(tb_cm40.Text, out cm40);  // out為必須
            if (conversionSuccessfu40 == true)
            {
                //richTextBox1.Text += "得到cm40 : " + cm40 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm40\n";
                return false;
            }
            bool conversionSuccessfu41 = float.TryParse(tb_cm41.Text, out cm41);  // out為必須
            if (conversionSuccessfu41 == true)
            {
                //richTextBox1.Text += "得到cm41 : " + cm41 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm41\n";
                return false;
            }
            bool conversionSuccessfu42 = float.TryParse(tb_cm42.Text, out cm42);  // out為必須
            if (conversionSuccessfu42 == true)
            {
                //richTextBox1.Text += "得到cm42 : " + cm42 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm42\n";
                return false;
            }
            bool conversionSuccessfu43 = float.TryParse(tb_cm43.Text, out cm43);  // out為必須
            if (conversionSuccessfu43 == true)
            {
                //richTextBox1.Text += "得到cm43 : " + cm43 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm43\n";
                return false;
            }
            bool conversionSuccessfu44 = float.TryParse(tb_cm44.Text, out cm44);  // out為必須
            if (conversionSuccessfu44 == true)
            {
                //richTextBox1.Text += "得到cm44 : " + cm44 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗 cm44\n";
                return false;
            }

            matrix = new float[][] 
            {
                //           紅對紅00 紅對綠01 紅對藍02
                new float[] {cm00,    cm01,    cm02,    cm03,   cm04},  // 紅
                //           綠對紅10 綠對綠11 綠對藍12
                new float[] {cm10,    cm11,    cm12,    cm13,   cm14},  // 綠
                //           藍對紅20 藍對綠21 藍對藍22
                new float[] {cm20,    cm21,    cm22,    cm23,   cm24},  // 藍
                new float[] {cm30,    cm31,    cm32,    cm33,   cm34},  // Alpha
                new float[] {cm40,    cm41,    cm42,    cm43,   cm44}
            };
            flag_color_matrix_valid = true;
            return flag_color_matrix_valid;
        }

        void print_ColorMatrix(ColorMatrix cm)
        {
            richTextBox1.Text += cm.Matrix00.ToString() + "\t" + cm.Matrix01.ToString() + "\t" + cm.Matrix02.ToString() + "\t" + cm.Matrix03.ToString() + "\t" + cm.Matrix04.ToString() + "\n";
            richTextBox1.Text += cm.Matrix10.ToString() + "\t" + cm.Matrix11.ToString() + "\t" + cm.Matrix12.ToString() + "\t" + cm.Matrix13.ToString() + "\t" + cm.Matrix14.ToString() + "\n";
            richTextBox1.Text += cm.Matrix20.ToString() + "\t" + cm.Matrix21.ToString() + "\t" + cm.Matrix22.ToString() + "\t" + cm.Matrix23.ToString() + "\t" + cm.Matrix24.ToString() + "\n";
            richTextBox1.Text += cm.Matrix30.ToString() + "\t" + cm.Matrix31.ToString() + "\t" + cm.Matrix32.ToString() + "\t" + cm.Matrix33.ToString() + "\t" + cm.Matrix34.ToString() + "\n";
            richTextBox1.Text += cm.Matrix40.ToString() + "\t" + cm.Matrix41.ToString() + "\t" + cm.Matrix42.ToString() + "\t" + cm.Matrix43.ToString() + "\t" + cm.Matrix44.ToString() + "\n";
        }

        void print_color_matrix(float[][] matrix)
        {
            if (flag_color_matrix_valid == false)
            {
                richTextBox1.Text += "無 color matrix, 離開\n";
                return;
            }
            else
            {
                richTextBox1.Text += "取得CM OK, CM :\n";
                richTextBox1.Text += matrix[0][0] + "\t" + matrix[0][1] + "\t" + matrix[0][2] + "\t" + matrix[0][3] + "\t" + matrix[0][4] + "\n";
                richTextBox1.Text += matrix[1][0] + "\t" + matrix[1][1] + "\t" + matrix[1][2] + "\t" + matrix[1][3] + "\t" + matrix[1][4] + "\n";
                richTextBox1.Text += matrix[2][0] + "\t" + matrix[2][1] + "\t" + matrix[2][2] + "\t" + matrix[2][3] + "\t" + matrix[2][4] + "\n";
                richTextBox1.Text += matrix[3][0] + "\t" + matrix[3][1] + "\t" + matrix[3][2] + "\t" + matrix[3][3] + "\t" + matrix[3][4] + "\n";
                richTextBox1.Text += matrix[4][0] + "\t" + matrix[4][1] + "\t" + matrix[4][2] + "\t" + matrix[4][3] + "\t" + matrix[4][4] + "\n";
            }
        }

        private void bt_cm_apply_Click(object sender, EventArgs e)
        {
            apply_color_matrix();
        }

        void apply_color_matrix()
        {
            if (get_color_matrix() == false)
            {
                richTextBox1.Text += "取得CM失敗\n";
                return;
            }
            else
            {
                richTextBox1.Text += "取得CM OK\n";
            }

            pictureBox2.Image = Image.FromFile(filename);
            print_color_matrix(matrix);

            //使用 color matrix
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            //ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);same
            //ia.SetColorMatrices(cm, null);//same
            ia.SetGamma(0.6f);
            ia.SetColorMatrix(cm);

            g.Clear(Color.Pink);
            // 貼上使用CM轉換過的影像
            Bitmap bmp = new Bitmap(filename);
            g.DrawImage(bmp, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);
            pictureBox1.Image = bitmap1;
        }

        void load_color_matrix(float[][] matrix)
        {
            tb_cm00.Text = matrix[0][0].ToString();
            tb_cm01.Text = matrix[0][1].ToString();
            tb_cm02.Text = matrix[0][2].ToString();
            tb_cm03.Text = matrix[0][3].ToString();
            tb_cm04.Text = matrix[0][4].ToString();
            tb_cm10.Text = matrix[1][0].ToString();
            tb_cm11.Text = matrix[1][1].ToString();
            tb_cm12.Text = matrix[1][2].ToString();
            tb_cm13.Text = matrix[1][3].ToString();
            tb_cm14.Text = matrix[1][4].ToString();
            tb_cm20.Text = matrix[2][0].ToString();
            tb_cm21.Text = matrix[2][1].ToString();
            tb_cm22.Text = matrix[2][2].ToString();
            tb_cm23.Text = matrix[2][3].ToString();
            tb_cm24.Text = matrix[2][4].ToString();
            tb_cm30.Text = matrix[3][0].ToString();
            tb_cm31.Text = matrix[3][1].ToString();
            tb_cm32.Text = matrix[3][2].ToString();
            tb_cm33.Text = matrix[3][3].ToString();
            tb_cm34.Text = matrix[3][4].ToString();
            tb_cm40.Text = matrix[4][0].ToString();
            tb_cm41.Text = matrix[4][1].ToString();
            tb_cm42.Text = matrix[4][2].ToString();
            tb_cm43.Text = matrix[4][3].ToString();
            tb_cm44.Text = matrix[4][4].ToString();
        }

        private void bt_cm_reset_Click(object sender, EventArgs e)
        {
            load_color_matrix(matrix_identity);
            apply_color_matrix();
        }

        float brightness = 0.05f;
        private void bt_brightness_Click(object sender, EventArgs e)
        {
            load_color_matrix(matrix_identity);

            tb_cm40.Text = brightness.ToString();
            tb_cm41.Text = brightness.ToString();
            tb_cm42.Text = brightness.ToString();

            brightness += 0.05f;
            if (brightness > 0.3f)
            {
                brightness = -0.3f;
            }

            //調整亮度, 也可以同時調整 cm00 cm11 cm22 三原色的縮放比例
        }

        private void bt_gray_Click(object sender, EventArgs e)
        {
            load_color_matrix(matrix_gray);
            apply_color_matrix();
        }

        private void bt_sepia_Click(object sender, EventArgs e)
        {
            load_color_matrix(matrix_sepia);
            apply_color_matrix();
        }

        float transparency = 0.3f;
        private void bt_alpha_Click(object sender, EventArgs e)
        {
            load_color_matrix(matrix_identity);

            //float t = 0.60f; //Transparency
            tb_cm33.Text = transparency.ToString();
            transparency += 0.3f;
            if (transparency > 1.6)
            {
                transparency = 0.3f;
            }
        }

        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton0.Checked == true)
            {
                filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";
            }
            else if (radioButton1.Checked == true)
            {
                filename = @"D:\_git\vcs\_1.data\______test_files1\colorbar2.bmp";
            }
            else if (radioButton2.Checked == true)
            {
                filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            }
            else if (radioButton3.Checked == true)
            {
                filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            }
            else
            {
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


/*
            Image tmp = Image.FromFile(filename);

            this.pictureBox1.Image = Image.FromFile(filename);

            Graphics g = Graphics.FromImage(tmp);
            Rectangle destRect = new Rectangle(0, 0, tmp.Width, tmp.Height);
            g.DrawImage(tmp, destRect, 0, 0, tmp.Width, tmp.Height, GraphicsUnit.Pixel, attr);
            this.pictureBox1.Image = (Image)tmp.Clone();
*/
/*
            // Sepia 公式
            //int R = (int)(0.393 * p.R + 0.769 * p.G + 0.189 * p.B);
            //int G = (int)(0.349 * p.R + 0.686 * p.G + 0.168 * p.B);
            //int B = (int)(0.272 * p.R + 0.534 * p.G + 0.131 * p.B);

            // 色彩調整矩陣 Sepia 效果
            float[][] matrix =
            {
                //           紅對紅00 紅對綠01 紅對藍02
                new float[] {0.393f,  0.349f,  0.272f,  0, 0},  // 紅
                //           綠對紅10 綠對綠11 綠對藍12
                new float[] {0.769f,  0.686f,  0.534f,  0, 0},  // 綠
                //           藍對紅20 藍對綠21 藍對藍22
                new float[] {0.189f,  0.168f,  0.131f,  0, 0},  // 藍
                new float[] {0,       0,       0,       1, 0},
                new float[] {0,       0,       0,       0, 1}
            };
*/


/* 解釋
            ImageAttributes ia = new ImageAttributes();  // ImageAttributes 類別的多個方法會使用色彩矩陣來調整影像色彩
            ia.SetColorMatrix(cm);  // 設定預設分類的色彩調整矩陣
*/

// color matrix
// 定義含有 RGBA 空間座標的 5 x 5 矩陣
// (R, G, B, A, 1) 乘上 此矩陣

/*
            //建立 ColorMatrix，並將其 Matrix 位置設定為 1.75，強調影像的紅色元件。
            ColorMatrix cm = new ColorMatrix();
            print_ColorMatrix(cm);
            // Red
            cm.Matrix00 = 1.75f;
            // Green
            cm.Matrix11 = 1.00f;
            // Blue
            cm.Matrix22 = 1.00f;
            // alpha
            cm.Matrix33 = 1.00f;
            // w
            cm.Matrix44 = 1.00f;
            print_ColorMatrix(cm);
*/
