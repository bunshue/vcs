using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace ims_DrawTest1
{
    public partial class Form1 : Form
    {
        private const int ROUND = 50;
        int[] right_left_point_cnt = new int[ROUND];
        int[] down_up_point_cnt = new int[ROUND];
        int[] awb_block = new int[ROUND];
        int[] useless = new int[ROUND];

        Graphics g;
        Bitmap bitmap1;

        int x_st_string;
        int y_st_string;
        int x_st_old;
        int y_st_old;

        public class MySearchInfo
        {
            public int x;
            public int y;
            public int wh;
            public int cnt;
            public MySearchInfo(int x,int y,int wh,int c)
            {
                this.x = x;
                this.y = y;
                this.wh = wh;
                this.cnt = c;
            }
        }

        //不用宣告長度的陣列(Array)
        // 宣告searchinfos 為List
        // 以下List 裡為MyFileInfo 型態
        List<MySearchInfo> searchinfos = new List<MySearchInfo>();

        public class MyDrawStringInfo
        {
            public int x;
            public int y;
            public MyDrawStringInfo(int x, int y)
            {
                this.x = x;
                this.y = y;
            }
        }

        //不用宣告長度的陣列(Array)
        // 宣告drawed 為List
        // 以下List 裡為MyFileInfo 型態
        List<MyDrawStringInfo> drawed = new List<MyDrawStringInfo>();


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

        public Form1()
        {
            InitializeComponent();
            pictureBox1.Image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            //g = pictureBox1.CreateGraphics(); same
            g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);

            right_left_point_cnt[0] = -10; down_up_point_cnt[0] = 65; awb_block[0] = 32;	//for vcs
            right_left_point_cnt[1] = -10; down_up_point_cnt[1] = 65; awb_block[1] = 28;	//for vcs
            right_left_point_cnt[2] = -10; down_up_point_cnt[2] = 65; awb_block[2] = 32;	//for vcs
            right_left_point_cnt[3] = -10; down_up_point_cnt[3] = 65; awb_block[3] = 28;	//for vcs
            right_left_point_cnt[4] = -10; down_up_point_cnt[4] = 65; awb_block[4] = 32;	//for vcs
            right_left_point_cnt[5] = -10; down_up_point_cnt[5] = 65; awb_block[5] = 28;	//for vcs
            right_left_point_cnt[6] = -10; down_up_point_cnt[6] = 65; awb_block[6] = 32;	//for vcs
            right_left_point_cnt[7] = -15; down_up_point_cnt[7] = 65; awb_block[7] = 32;	//for vcs
            right_left_point_cnt[8] = -10; down_up_point_cnt[8] = 65; awb_block[8] = 32;	//for vcs
            right_left_point_cnt[9] = -10; down_up_point_cnt[9] = 65; awb_block[9] = 32;	//for vcs
            right_left_point_cnt[10] = -10; down_up_point_cnt[10] = 65; awb_block[10] = 32;	//for vcs
            right_left_point_cnt[11] = -10; down_up_point_cnt[11] = 65; awb_block[11] = 28;	//for vcs
            right_left_point_cnt[12] = -10; down_up_point_cnt[12] = 65; awb_block[12] = 28;	//for vcs
            right_left_point_cnt[13] = -10; down_up_point_cnt[13] = 65; awb_block[13] = 28;	//for vcs
            right_left_point_cnt[14] = -10; down_up_point_cnt[14] = 70; awb_block[14] = 28;	//for vcs
            right_left_point_cnt[15] = -10; down_up_point_cnt[15] = 65; awb_block[15] = 32;	//for vcs
            right_left_point_cnt[16] = -10; down_up_point_cnt[16] = 70; awb_block[16] = 28;	//for vcs
            right_left_point_cnt[17] = -10; down_up_point_cnt[17] = 65; awb_block[17] = 32;	//for vcs
            right_left_point_cnt[18] = -10; down_up_point_cnt[18] = 65; awb_block[18] = 28;	//for vcs
            right_left_point_cnt[19] = -10; down_up_point_cnt[19] = 65; awb_block[19] = 28;	//for vcs
            right_left_point_cnt[20] = -10; down_up_point_cnt[20] = 65; awb_block[20] = 28;	//for vcs
            right_left_point_cnt[21] = -10; down_up_point_cnt[21] = 65; awb_block[21] = 28;	//for vcs
            right_left_point_cnt[22] = -10; down_up_point_cnt[22] = 65; awb_block[22] = 32;	//for vcs
            right_left_point_cnt[23] = -10; down_up_point_cnt[23] = 65; awb_block[23] = 28;	//for vcs
            right_left_point_cnt[24] = -10; down_up_point_cnt[24] = 65; awb_block[24] = 32;	//for vcs
            right_left_point_cnt[25] = -10; down_up_point_cnt[25] = 70; awb_block[25] = 28;	//for vcs
            right_left_point_cnt[26] = -10; down_up_point_cnt[26] = 65; awb_block[26] = 32;	//for vcs
            right_left_point_cnt[27] = -10; down_up_point_cnt[27] = 65; awb_block[27] = 28;	//for vcs
            right_left_point_cnt[28] = -10; down_up_point_cnt[28] = 65; awb_block[28] = 28;	//for vcs
            right_left_point_cnt[29] = -10; down_up_point_cnt[29] = 65; awb_block[29] = 28;	//for vcs
            right_left_point_cnt[30] = -10; down_up_point_cnt[30] = 65; awb_block[30] = 32;	//for vcs
            right_left_point_cnt[31] = -10; down_up_point_cnt[31] = 65; awb_block[31] = 28;	//for vcs
            right_left_point_cnt[32] = -10; down_up_point_cnt[32] = 65; awb_block[32] = 28;	//for vcs
            right_left_point_cnt[33] = -10; down_up_point_cnt[33] = 65; awb_block[33] = 28;	//for vcs
            right_left_point_cnt[34] = -10; down_up_point_cnt[34] = 65; awb_block[34] = 28;	//for vcs
            right_left_point_cnt[35] = -10; down_up_point_cnt[35] = 65; awb_block[35] = 28;	//for vcs
            right_left_point_cnt[36] = -10; down_up_point_cnt[36] = 65; awb_block[36] = 28;	//for vcs
            right_left_point_cnt[37] = -10; down_up_point_cnt[37] = 65; awb_block[37] = 32;	//for vcs
            right_left_point_cnt[38] = -10; down_up_point_cnt[38] = 65; awb_block[38] = 28;	//for vcs
            right_left_point_cnt[39] = -10; down_up_point_cnt[39] = 65; awb_block[39] = 28;	//for vcs
            right_left_point_cnt[40] = -10; down_up_point_cnt[40] = 65; awb_block[40] = 28;	//for vcs
            right_left_point_cnt[41] = -10; down_up_point_cnt[41] = 65; awb_block[41] = 28;	//for vcs
            right_left_point_cnt[42] = -10; down_up_point_cnt[42] = 65; awb_block[42] = 28;	//for vcs
            right_left_point_cnt[43] = -10; down_up_point_cnt[43] = 65; awb_block[43] = 32;	//for vcs
            right_left_point_cnt[44] = -10; down_up_point_cnt[44] = 65; awb_block[44] = 32;	//for vcs
            right_left_point_cnt[45] = -10; down_up_point_cnt[45] = 65; awb_block[45] = 32;	//for vcs
            right_left_point_cnt[46] = -10; down_up_point_cnt[46] = 70; awb_block[46] = 28;	//for vcs
            right_left_point_cnt[47] = -10; down_up_point_cnt[47] = 65; awb_block[47] = 28;	//for vcs
            right_left_point_cnt[48] = -10; down_up_point_cnt[48] = 65; awb_block[48] = 28;	//for vcs
            right_left_point_cnt[49] = -10; down_up_point_cnt[49] = 65; awb_block[49] = 28;	//for vcs

            searchinfos.Clear();
            drawed.Clear();

            for (int i = 0; i < ROUND; i++)
            {
                useless[i] = 0;
            }

            check_search_location_data();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String filename = string.Empty;

            int width;
            int height;

            filename = "C:\\______test_files\\ims_image.bmp";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);

            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            width = bitmap1.Width;
            height = bitmap1.Height;

            //pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.Image = bitmap1;

            g = Graphics.FromImage(bitmap1);

            pictureBox1.Image = bitmap1;

            int x_st;
            int y_st;
            int ww;
            int hh;
            int WW = 640;
            int HH = 480;
            int awb_window_size = 200;     //AWB window size width, height


            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, 640 - 1, 480 - 1));

            x_st = WW / 2 - awb_window_size / 2;
            y_st = HH / 2 - awb_window_size / 2;

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, awb_window_size, awb_window_size));

            int i;
            /*
            for (i = 0; i < ROUND; i++)
            {
                ww = awb_block[i];
                hh = awb_block[i];

                x_st = WW / 2 - ww / 2 + right_left_point_cnt[i];
                y_st = HH / 2 - hh / 2 + down_up_point_cnt[i];

                g.DrawRectangle(new Pen(Color.Red, 1), new Rectangle(x_st, y_st, ww, hh));

                g.DrawString(i.ToString()+",", new Font("標楷體", 8), new SolidBrush(Color.Red), new PointF(x_st - 20 + i*12, y_st - 20));
            }
            */
            int dd = ROUND / 5;
            int wide;
            for (i = 0; i < searchinfos.Count; i++)
            {
                richTextBox1.Text += "draw i = " + i.ToString() + ", cnt = " + searchinfos[i].cnt.ToString() + "\n";
                ww = searchinfos[i].wh;
                hh = searchinfos[i].wh;

                x_st = WW / 2 - ww / 2 + searchinfos[i].x;
                y_st = HH / 2 - hh / 2 + searchinfos[i].y;

                wide = searchinfos[i].cnt / dd;
                if (wide == 0)
                    wide++;

                g.DrawRectangle(new Pen(Color.Red, wide), new Rectangle(x_st, y_st, ww, hh));
                x_st_old = x_st;
                y_st_old = y_st;

                x_st_string = x_st + ww / 2 - 5;
                y_st_string = y_st - 10 - i * 8;

                richTextBox1.Text += "before x = " + x_st_string.ToString() + ", y = " + y_st_string.ToString() + "\n";

                find_draw_string_location();

                richTextBox1.Text += "after  x = " + x_st_string.ToString() + ", y = " + y_st_string.ToString() + "\n";

                g.DrawString(searchinfos[i].cnt.ToString(), new Font("標楷體", 10), new SolidBrush(Color.Red), new PointF(x_st_string, y_st_string));

                g.DrawLine(new Pen(Color.Red, 1), x_st_old, y_st_old, x_st_string+5, y_st_string + 10);

            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (bitmap1 != null)
            {
                //filename = Application.StartupPath + "\\ims_image.bmp";
                String file = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                //String file1 = file + ".jpg";
                String file2 = file + ".bmp";
                //String file3 = file + ".png";

                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(@file2, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + file2 + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";

        }

        void check_search_location_data()
        {
            int i;
            int j;
            for (i = 0; i < ROUND; i++)
            {
                for (j = i + 1; j < ROUND; j++)
                {
                    if (useless[i] != -1)
                    {
                        //richTextBox1.Text += "compare i = " + i.ToString() + ", j = " + j.ToString() + "\n";
                        if ((right_left_point_cnt[i] == right_left_point_cnt[j]) && (down_up_point_cnt[i] == down_up_point_cnt[j]) && (awb_block[i] == awb_block[j]))
                        {
                            //richTextBox1.Text += "X";
                            useless[i]++;
                            useless[j] = -1;
                        }
                        else
                        {

                        }
                    }
                }
            }

            for (i = 0; i < ROUND; i++)
            {
                //richTextBox1.Text += useless[i].ToString() + " ";
                if (useless[i] != -1)
                {
                    //richTextBox1.Text += "add, i = " + i.ToString() + "\n";
                    searchinfos.Add(new MySearchInfo(right_left_point_cnt[i], down_up_point_cnt[i], awb_block[i], (useless[i] + 1)));
                }

            }
            //richTextBox1.Text += "\n";


            richTextBox1.Text += "cnt = " + searchinfos.Count.ToString() + "\n";

        }

        void find_draw_string_location()
        {
            int i;
            int w = 24;
            int h = 12;

            bool flag_conflict_x = true;
            bool flag_conflict_y = true;

            //g.DrawString(searchinfos[i].cnt.ToString() + ",", new Font("標楷體", 10), new SolidBrush(Color.Red), new PointF(x_st + ww / 2 - 5, y_st - 10 - i * 8));

            //richTextBox1.Text += "x_st_string = " + x_st_string.ToString() + ", y_st_string = " + y_st_string.ToString() + "\n";

            if (drawed.Count == 0)
            {
                richTextBox1.Text += "111111111111111111111\n";
                drawed.Add(new MyDrawStringInfo(x_st_string, y_st_string));
                return;
            }

            while ((flag_conflict_x == true) || (flag_conflict_y == true))
            {

                for (i = 0; i < drawed.Count; i++)
                {
                    //richTextBox1.Text += "i = " + i.ToString() + ", x = " + drawed[i].x.ToString() + ", y = " + drawed[i].y.ToString() + ", y_st_string = " + y_st_string.ToString() + "\n";

                    int x_left = x_st_string;
                    int x_right = x_st_string + w;
                    int y_top = y_st_string;
                    int y_down = y_st_string + h;

                    if ((x_left > drawed[i].x) && (x_left < (drawed[i].x + w)))
                    {
                        //richTextBox1.Text += "Inside 1\n";
                        flag_conflict_x = true;
                    }
                    else if ((x_right > drawed[i].x) && (x_right < (drawed[i].x + w)))
                    {
                        //richTextBox1.Text += "Inside 2\n";
                        flag_conflict_x = true;
                    }
                    else if ((y_top > drawed[i].y) && (y_top < (drawed[i].y + h)))
                    {
                        //richTextBox1.Text += "Inside 3\n";
                        flag_conflict_y = true;
                    }
                    else if ((y_down > drawed[i].y) && (y_down < (drawed[i].y + h)))
                    {
                        //richTextBox1.Text += "Inside 4\n";
                        flag_conflict_y = true;
                    }
                    else
                    {
                        //richTextBox1.Text += "Outside\n";
                        flag_conflict_x = false;
                        flag_conflict_y = false;
                    }

                    if (flag_conflict_x == true)
                    {
                        x_st_string--;
                    }
                    if (flag_conflict_y == true)
                    {
                        y_st_string--;
                    }


                }
            }
            drawed.Add(new MyDrawStringInfo(x_st_string, y_st_string));

        }

        private void button3_Click(object sender, EventArgs e)
        {
            String filename = string.Empty;

            int width;
            int height;

            filename = "C:\\______test_files\\ims_image.bmp";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);

            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            width = bitmap1.Width;
            height = bitmap1.Height;

            //pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.Image = bitmap1;

            g = Graphics.FromImage(bitmap1);

            pictureBox1.Image = bitmap1;

            int ww = 640;
            int hh = 480;

            g.DrawRectangle(new Pen(Color.Red, 10), new Rectangle(0, 0, 640 - 1, 480 - 1));

            int i;
            int j;

            Color pt;

            int brightness_new = 0;
            int brightness_old = 0;

            for (j = 0; j < hh; j++)
            {
                for (i = 0; i < ww; i++)
                {
                    pt = bitmap1.GetPixel(i, j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    brightness_new = (int)yyy.Y;


                    if (Math.Abs(brightness_new - brightness_old) > 20)
                    {
                        bitmap1.SetPixel(i, j, Color.FromArgb(255, 0, 0));
                    }
                    else
                    {
                        //保持不變
                    }
                    brightness_old = brightness_new;
                }
            }
        }
    }
}
