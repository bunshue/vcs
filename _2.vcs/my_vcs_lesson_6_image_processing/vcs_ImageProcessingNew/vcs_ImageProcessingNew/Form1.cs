using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Imaging;   //for BitmapData

namespace vcs_ImageProcessingNew
{
    public partial class Form1 : Form
    {
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\ims_image_20230921_155302.bmp";
        string filename = @"C:\_git\vcs\_1.data\______test_files1\ims01.bmp";

        private Bitmap bitmap1 = null;  //原圖
        private Bitmap bitmap2 = null;  //從原圖修改過的

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        private int w = 0;  //擷取圖的寬
        private int h = 0;  //擷取圖的高
        int x_st = 0;   //擷取開始x
        int y_st = 0;   //擷取開始y

        private int brightness_max = 0;
        private int brightness_min = 0;
        private int brightness_avg = 0;
        private double brightness_sd = 0;
        private float brightness_ratio = 0;
        private int brightness_max_mod = 0;
        private int brightness_min_mod = 0;
        private float brightness_ratio_mod = 0;

        int[] brightness_data = new int[256];

        int max = 255;
        int min = 0;

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

        public static RGB YUVToRGB(YUV yuv)
        {
            double r = yuv.Y + 1.4075 * (yuv.V - 128);
            double g = yuv.Y - 0.3455 * (yuv.U - 128) - (0.7169 * (yuv.V - 128));
            double b = yuv.Y + 1.7790 * (yuv.U - 128);
            if (r > 255)
                r = 255;
            if (g > 255)
                g = 255;
            if (b > 255)
                b = 255;
            if (r < 0)
                r = 0;
            if (g < 0)
                g = 0;
            if (b < 0)
                b = 0;

            return new RGB((byte)r, (byte)g, (byte)b);
        }

        void get_brigheness_data(Bitmap bitmap1, int x_st, int y_st, int w, int h)
        {
            richTextBox1.Text += "x_st = " + x_st.ToString() + "\ty_st = " + y_st.ToString() + "\tw = " + w.ToString() + "\th = " + h.ToString() + "\n";
            brightness_data = new int[256];

            int i;
            int j;
            Color pt;
            int total_points = 0;
            double total_brightness = 0;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    total_brightness += yyy.Y;

                    int y = (int)Math.Round(yyy.Y); //四捨五入

                    if (y > 255)
                        y = 255;
                    if (y < 0)
                        y = 0;

                    brightness_data[y]++;
                    total_points++;

                    /*
                    if (j == 10)
                    {
                        richTextBox1.Text += y.ToString() + " ";
                        if ((i % 16) == 15)
                        {
                            richTextBox1.Text += "\n";
                        }
                    }
                    */
                }
                //richTextBox1.Text += "\n";
            }
            //richTextBox1.Text += "\n";
            richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";
            richTextBox1.Text += "總亮度 " + total_brightness.ToString() + "\n";
            richTextBox1.Text += "平均亮度 " + (total_brightness / total_points).ToString() + "\n";
        }

        int draw_x_st = 200;
        int draw_y_st = 200;
        int draw_w = 10;
        int draw_h = 10;

        void measure_brightness()
        {
            x_st = draw_x_st;
            y_st = draw_y_st;
            w = draw_w;
            h = draw_h;

            //量測原圖 bitmap1

            get_brigheness_data(bitmap1, x_st, y_st, w, h);

            int i;
            int most = 0;
            int brightness_st = 0;
            int brightness_sp = 0;
            int total_points = 0;
            double total_brightness = 0;
            for (i = 0; i < 256; i++)
            {
                total_points += brightness_data[i];
                total_brightness += i * brightness_data[i];
                //richTextBox1.Text += brightness_data[i].ToString() + " ";
                if (brightness_data[i] > most)
                    most = brightness_data[i];
                /*
                if (brightness_data[i] == 0)
                    brightness_data[i] = 5;
                */
                if ((brightness_data[i] > 0) && (brightness_st == 0))
                {
                    brightness_st = i;
                }
                if (brightness_data[i] > 0)
                {
                    brightness_sp = i;
                }
            }
            richTextBox1.Text += "\n最多 " + most.ToString() + "\n";
            richTextBox1.Text += "亮度範圍 : " + brightness_st.ToString() + " 到 " + brightness_sp.ToString() + "\n";
            richTextBox1.Text += "亮差 : " + (brightness_sp - brightness_st).ToString() + "\n";

            richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";
            richTextBox1.Text += "總亮度 " + total_brightness.ToString() + "\n";
            richTextBox1.Text += "平均亮度 " + (total_brightness / total_points).ToString() + "\n";


            //一維陣列用法：
            double[] sd_num = new double[total_points];

            int index = 0;
            int j = 0;
            Color pt;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    sd_num[index] = yyy.Y;
                    index++;
                }
            }

            //return;

            double sd = SD(sd_num);
            //richTextBox1.Text += "標準差 " + sd.ToString("F2") + "\n";
            brightness_sd = sd;

            int average_brightness = (int)Math.Round(total_brightness / total_points); //四捨五入
            //richTextBox1.Text += "平均亮度 " + average_brightness.ToString() + "\n";
            brightness_avg = average_brightness;

            int ww = 480 * 2 - 10;
            int hh1 = 300;
            int hh2 = 256;
            Bitmap bmp4 = new Bitmap(ww, hh1 * 2 + 100);
            Graphics g4 = Graphics.FromImage(bmp4);
            g4.Clear(Color.Pink);
            Pen p = new Pen(Color.Blue, 2);

            double ratio = 0;
            ratio = (double)hh2 / most;
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < 256; i++)
            {
                g4.FillRectangle(Brushes.Red, i * 2, hh2 - (float)(brightness_data[i] * ratio), 2, (float)(brightness_data[i] * ratio));
            }

            //return;

            g4.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh1 - 2);
            g4.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh2 - 2);

            p = new Pen(Color.Yellow, 3);
            g4.DrawLine(p, average_brightness * 2, 0, average_brightness * 2, hh2 - 2);
            g4.DrawLine(p, brightness_st * 2, 0, brightness_st * 2, hh2 - 2);
            g4.DrawLine(p, brightness_sp * 2, 0, brightness_sp * 2, hh2 - 2);

            Brush b = new SolidBrush(Color.FromArgb(33, Color.RoyalBlue.R, Color.RoyalBlue.G, Color.RoyalBlue.B));

            g4.FillRectangle(b, min * 2, 0, (max - min) * 2, hh1);

            Font f = new Font("標楷體", 20);

            if ((min >= 0) && (min <= 103))
            {
                g4.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(min * 2, hh2));
            }
            else if (min < 0)
            {
                g4.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(0, hh2));
            }
            else
            {
                g4.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(103 * 2, hh2));
            }

            if ((max <= 255) && (max >= 152))
            {
                g4.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(max * 2 - 50, hh2));

                g4.DrawString(brightness_st.ToString(), f, new SolidBrush(Color.Yellow), new PointF(brightness_st * 2 - 25, hh2));
                g4.DrawString(brightness_sp.ToString(), f, new SolidBrush(Color.Yellow), new PointF(brightness_sp * 2 - 25, hh2));
                g4.DrawString(average_brightness.ToString(), f, new SolidBrush(Color.Yellow), new PointF(average_brightness * 2 - 25, hh2));
            }
            else if (max > 255)
            {
                g4.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(512 - 50, hh2));
            }
            else
            {
                g4.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(152 * 2 - 50, hh2));
            }

            //return;

            int y_min = 0;
            int y_max = 0;
            FindYMaxYMin(brightness_data, out y_min, out y_max);
            //richTextBox1.Text += "M = " + y_max.ToString() + "\t" + "m = " + y_min.ToString() + "\n";

            int dy = 22;
            g4.DrawString("Max = " + y_max.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 0);
            g4.DrawString("min = " + y_min.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 1);
            g4.DrawString("most = " + most.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 2);
            g4.DrawString("最亮 : " + brightness_sp.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 3);
            g4.DrawString("最暗 : " + brightness_st.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 4);
            g4.DrawString("亮差 : " + (brightness_sp - brightness_st).ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 5);
            g4.DrawString("平均 : " + average_brightness.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 6);
            g4.DrawString("SD : " + sd.ToString("F2"), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 7);

            float rr_sp = 2.0f;
            bool flag_modify_boundary_sp = true;
            if ((brightness_sp - average_brightness) < sd * rr_sp)
            {
                g4.DrawString("YMax太近", new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 8);
                flag_modify_boundary_sp = false;
            }

            float rr_st = 3.0f;
            bool flag_modify_boundary_st = true;
            if ((average_brightness - brightness_st) < sd * rr_st)
            {
                g4.DrawString("YMin太近", new Font("標楷體", 18), new SolidBrush(Color.Navy), 512 + 100, 10 + dy * 8);
                flag_modify_boundary_st = false;
            }

            g4.DrawString(((int)Math.Round((average_brightness - sd * rr_st))).ToString() + " " +
                average_brightness.ToString() + " " +
                ((int)Math.Round((average_brightness + sd * rr_sp))).ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 9);

            /*
            if ((flag_modify_boundary_sp == false) || (cb_modify.Checked == false))
            {
                g4.DrawString("亮場未調整", new Font("標楷體", 13), new SolidBrush(Color.Red), 512 + 105, 10 + dy * 10);
            }

            if ((flag_modify_boundary_st == false) || (cb_modify.Checked == false))
            {
                g4.DrawString("暗場未調整", new Font("標楷體", 13), new SolidBrush(Color.Red), 512, 10 + dy * 10);
            }
            */

            richTextBox1.Text += "dddddd";
            //return;

            int boundary_st = (int)Math.Round(average_brightness - sd * rr_st);
            int boundary_sp = (int)Math.Round(average_brightness + sd * rr_sp);

            b = new SolidBrush(Color.FromArgb(30, Color.Lime.R, Color.Lime.G, Color.Lime.B));
            g4.FillRectangle(b, boundary_st * 2, 0 + 0, (boundary_sp - boundary_st) * 2, hh2 - 0 - 0);
            g4.DrawRectangle(Pens.Lime, boundary_st * 2, 0 + 0, (boundary_sp - boundary_st) * 2, hh2 - 0 - 0);
            //g4.DrawLine(Pens.Lime, boundary_st * 2, 0, boundary_st * 2, hh2);
            //g4.DrawLine(Pens.Lime, boundary_sp * 2, 0, boundary_sp * 2, hh2);

            int width = 40;
            b = new SolidBrush(Color.FromArgb(30, Color.Lime.R, Color.Lime.G, Color.Lime.B));
            g4.FillRectangle(b, 750, 0, width, 256);
            g4.FillRectangle(b, 800, 0, width, 256);
            g4.FillRectangle(b, 850, 0, width, 256);

            g4.DrawRectangle(Pens.Red, 750, hh2 - brightness_sp, width, brightness_sp - brightness_st);


            //richTextBox1.Text += "brightness data :\n";
            //printArrayData(brightness_data);
            int mm = brightness_data.Max();
            //richTextBox1.Text += "mm = " + mm.ToString() + "\n";
            float rr = mm / (float)width;
            for (i = 0; i < 256; i++)
            {
                g4.DrawLine(Pens.Red, 750, hh2 - i, 750 + (int)(brightness_data[i] / rr), hh2 - i);

            }

            richTextBox1.Text += "eeeee\n";
            //return;

            Point[] curvePoints = new Point[256];    //一維陣列內有 256 個Point
            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = 750 + (int)(brightness_data[i] / rr);
                curvePoints[i].Y = hh2 - i;
            }
            // Draw lines between original points to screen.
            g4.DrawLines(Pens.Yellow, curvePoints);   //畫直線
            // Draw curve to screen.
            //g4.DrawCurve(Pens.Yellow, curvePoints); //畫曲線

            //再把標準差範圍畫出來

            richTextBox1.Text += "brightness_st = " + brightness_st.ToString() + "\n";
            richTextBox1.Text += "brightness_sp = " + brightness_sp.ToString() + "\n";
            richTextBox1.Text += "brightness_min = " + brightness_min.ToString() + "\n";
            richTextBox1.Text += "brightness_max = " + brightness_max.ToString() + "\n";
            richTextBox1.Text += "brightness_avg = " + brightness_avg.ToString() + "\n";
            richTextBox1.Text += "brightness_sd = " + brightness_sd.ToString() + "\n";
            richTextBox1.Text += "brightness_ratio = " + brightness_ratio.ToString("F2") + "\n";

            richTextBox1.Text += "brightness_min_mod = " + brightness_min_mod.ToString() + "\n";
            richTextBox1.Text += "brightness_max_mod = " + brightness_max_mod.ToString() + "\n";
            richTextBox1.Text += "brightness_ratio_mod = " + brightness_ratio_mod.ToString("F2") + "\n";

            g4.DrawRectangle(Pens.Red, 800, hh2 - brightness_max_mod, width, brightness_max_mod - brightness_min_mod);
            g4.DrawLine(Pens.Red, 800, hh2 - brightness_avg, 800 + width, hh2 - brightness_avg);


            richTextBox1.Text += "eeeee2222\n";


            pictureBox2.Image = bmp4;
        }


        void FindYMaxYMin(int[] array, out int y_min, out int y_max)
        {
            int i;
            int len = array.Length;
            y_min = int.MaxValue;
            y_max = int.MinValue;
            for (i = 0; i < len; i++)
            {
                if (y_min > array[i])
                {
                    y_min = array[i];
                }
                if (y_max < array[i])
                {
                    y_max = array[i];
                }
            }
        }

        /// <summary> 
        /// 標準差(StandardDifference) 
        /// </summary> 
        /// <param name="val"></param> 
        /// <returns></returns> 
        public double SD(double[] a)
        {
            int len;
            double avg;
            double sd;
            int i;

            len = a.Length;
            avg = a.Average();
            if (len <= 1)
            {
                sd = 0;
                richTextBox1.Text += "SD = " + sd.ToString() + "\n";
                return sd;
            }

            richTextBox1.Text += "len = " + len.ToString() + "\n";
            richTextBox1.Text += "average = " + avg.ToString() + "\n";
            sd = 0;
            for (i = 0; i < len; i++)
            {
                sd += Math.Pow((a[i] - avg), 2);
            }
            sd /= (len - 1);
            sd = Math.Sqrt(sd);

            return sd;
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

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
            dx = 170;
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
        }

        private void button0_Click(object sender, EventArgs e)
        {
            measure_brightness();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            //讀取圖檔, 先放在Bitmap裏
            //string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename = @"C:\_git\vcs\_1.data\______test_files1\ims01.bmp";
            //string filename = "pic_original2.bmp";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            /* 畫色塊
            Graphics g = Graphics.FromImage(bitmap1);

            g.FillRectangle(new SolidBrush(Color.Red), 50, 100, 50, 50);
            g.FillRectangle(new SolidBrush(Color.Lime), 50, 100+70, 50, 50);
            g.FillRectangle(new SolidBrush(Color.Blue), 50, 100+140, 50, 50);
            */

            int i;
            int j;
            Color pt;
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    pt = bitmap1.GetPixel(i, j);



                    RGB pp = new RGB(pt.R, pt.G, pt.B);

                    byte r = pp.R;
                    byte g = pp.G;
                    byte b = pp.B;

                    Color cc = Color.FromArgb(255, g, b, b);

                    bitmap1.SetPixel(i, j, cc);

                }
            }
            //bitmap1.Save("pic_modify3.bmp", ImageFormat.Bmp);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //白色轉為透明
            //C#將圖片白色背景設置為透明
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);
            Bitmap bitmap1 = new Bitmap(image);
            bitmap1.MakeTransparent(Color.White);
            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //圖像截取
            //圖像截取

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Rectangle sr = new Rectangle(80, 60, 400, 400);//要截取的矩形區域
            Rectangle dr = new Rectangle(0, 0, 200, 200);//要顯示到Form的矩形區域
            g.DrawImage(bitmap1, dr, sr, GraphicsUnit.Pixel);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //改變圖像大小
            //改變圖像大小

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            // 改變圖像大小使用低質量的模式
            g.InterpolationMode = InterpolationMode.NearestNeighbor;

            g.DrawImage(bitmap1, new Rectangle(10, 10, 120, 120), // source rectangle
            new Rectangle(0, 0, W, H), // destination rectangle
            GraphicsUnit.Pixel);

            // 使用高質量模式
            //g.CompositingQuality = CompositingQuality.HighSpeed;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;

            g.DrawImage(bitmap1, new Rectangle(130, 10, 120, 120), new Rectangle(0, 0, W, H), GraphicsUnit.Pixel);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //重設大小
            //重設大小
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = ResizeImage(bitmap1, new Size(bitmap1.Width / 2, bitmap1.Height / 2));
            pictureBox1.Image = bitmap2;

        }

        //重設大小
        public Bitmap ResizeImage(Bitmap bmp, Size size)
        {
            Bitmap newbmp = new Bitmap(size.Width, size.Height);
            using (Graphics g = Graphics.FromImage(newbmp))
            {
                g.DrawImage(bmp, new Rectangle(Point.Empty, size));
            }
            return newbmp;
        }



        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
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
    }
}

