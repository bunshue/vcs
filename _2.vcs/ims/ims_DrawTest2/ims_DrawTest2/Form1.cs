using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace ims_DrawTest2
{
    public partial class Form1 : Form
    {
        private const int ROUND = 50;
        double[] awb_r = new double[ROUND];
        double[] awb_b = new double[ROUND];
        int[] right_left_point_cnt = new int[ROUND];
        int[] down_up_point_cnt = new int[ROUND];
        int[] awb_block = new int[ROUND];

        private const int BORDER_W = 5;     //5% border
        private const int BORDER_H = 5;     //5% border
        private const int STEP = 20;        //one step in y-axis

        Graphics g;
        Bitmap bitmap1;

        double awb_r_avg = 0;
        double awb_r_max = 0;
        double awb_r_min = 0;

        double awb_b_avg = 0;
        double awb_b_max = 0;
        double awb_b_min = 0;

        int W = 0;
        int H = 0;

        int w = 0;
        int h = 0;

        int ratio_x;
        int ratio_y;
        double y_max = 0;
        double y_min = 0;
        double y_range = 0;

        int offset_x = 0;
        int offset_y = 0;

        public Form1()
        {
            InitializeComponent();
            pictureBox1.Image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            //g = pictureBox1.CreateGraphics(); same
            g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            init_parameters();
        }

        void init_parameters()
        {
            awb_r[0] = 1559; awb_b[0] = 1469; right_left_point_cnt[0] = -35; down_up_point_cnt[0] = -65; awb_block[0] = 16;	//for vcs
            awb_r[1] = 1536; awb_b[1] = 1406; right_left_point_cnt[1] = -30; down_up_point_cnt[1] = -60; awb_block[1] = 16;	//for vcs
            awb_r[2] = 1551; awb_b[2] = 1463; right_left_point_cnt[2] = -35; down_up_point_cnt[2] = -65; awb_block[2] = 20;	//for vcs
            awb_r[3] = 1546; awb_b[3] = 1464; right_left_point_cnt[3] = -35; down_up_point_cnt[3] = -65; awb_block[3] = 20;	//for vcs
            awb_r[4] = 1549; awb_b[4] = 1458; right_left_point_cnt[4] = -35; down_up_point_cnt[4] = -65; awb_block[4] = 20;	//for vcs
            awb_r[5] = 1531; awb_b[5] = 1415; right_left_point_cnt[5] = -30; down_up_point_cnt[5] = -60; awb_block[5] = 16;	//for vcs
            awb_r[6] = 1551; awb_b[6] = 1455; right_left_point_cnt[6] = -35; down_up_point_cnt[6] = -65; awb_block[6] = 20;	//for vcs
            awb_r[7] = 1554; awb_b[7] = 1456; right_left_point_cnt[7] = -35; down_up_point_cnt[7] = -65; awb_block[7] = 20;	//for vcs
            awb_r[8] = 1548; awb_b[8] = 1458; right_left_point_cnt[8] = -35; down_up_point_cnt[8] = -65; awb_block[8] = 20;	//for vcs
            awb_r[9] = 1546; awb_b[9] = 1464; right_left_point_cnt[9] = -35; down_up_point_cnt[9] = -65; awb_block[9] = 20;	//for vcs
            awb_r[10] = 1547; awb_b[10] = 1457; right_left_point_cnt[10] = -35; down_up_point_cnt[10] = -65; awb_block[10] = 20;	//for vcs
            awb_r[11] = 1548; awb_b[11] = 1460; right_left_point_cnt[11] = -35; down_up_point_cnt[11] = -65; awb_block[11] = 20;	//for vcs
            awb_r[12] = 1550; awb_b[12] = 1459; right_left_point_cnt[12] = -35; down_up_point_cnt[12] = -65; awb_block[12] = 20;	//for vcs
            awb_r[13] = 1547; awb_b[13] = 1463; right_left_point_cnt[13] = -35; down_up_point_cnt[13] = -65; awb_block[13] = 20;	//for vcs
            awb_r[14] = 1555; awb_b[14] = 1461; right_left_point_cnt[14] = -35; down_up_point_cnt[14] = -65; awb_block[14] = 20;	//for vcs
            awb_r[15] = 1549; awb_b[15] = 1457; right_left_point_cnt[15] = -35; down_up_point_cnt[15] = -65; awb_block[15] = 20;	//for vcs
            awb_r[16] = 1551; awb_b[16] = 1455; right_left_point_cnt[16] = -35; down_up_point_cnt[16] = -65; awb_block[16] = 20;	//for vcs
            awb_r[17] = 1543; awb_b[17] = 1463; right_left_point_cnt[17] = -35; down_up_point_cnt[17] = -65; awb_block[17] = 20;	//for vcs
            awb_r[18] = 1552; awb_b[18] = 1452; right_left_point_cnt[18] = -35; down_up_point_cnt[18] = -65; awb_block[18] = 20;	//for vcs
            awb_r[19] = 1544; awb_b[19] = 1469; right_left_point_cnt[19] = -35; down_up_point_cnt[19] = -65; awb_block[19] = 20;	//for vcs
            awb_r[20] = 1531; awb_b[20] = 1405; right_left_point_cnt[20] = -30; down_up_point_cnt[20] = -60; awb_block[20] = 16;	//for vcs
            awb_r[21] = 1548; awb_b[21] = 1460; right_left_point_cnt[21] = -35; down_up_point_cnt[21] = -65; awb_block[21] = 20;	//for vcs
            awb_r[22] = 1550; awb_b[22] = 1462; right_left_point_cnt[22] = -35; down_up_point_cnt[22] = -65; awb_block[22] = 20;	//for vcs
            awb_r[23] = 1532; awb_b[23] = 1457; right_left_point_cnt[23] = -30; down_up_point_cnt[23] = -70; awb_block[23] = 28;	//for vcs
            awb_r[24] = 1544; awb_b[24] = 1427; right_left_point_cnt[24] = -40; down_up_point_cnt[24] = -80; awb_block[24] = 20;	//for vcs
            awb_r[25] = 1530; awb_b[25] = 1408; right_left_point_cnt[25] = -30; down_up_point_cnt[25] = -60; awb_block[25] = 16;	//for vcs
            awb_r[26] = 1545; awb_b[26] = 1463; right_left_point_cnt[26] = -35; down_up_point_cnt[26] = -65; awb_block[26] = 20;	//for vcs
            awb_r[27] = 1545; awb_b[27] = 1464; right_left_point_cnt[27] = -35; down_up_point_cnt[27] = -65; awb_block[27] = 20;	//for vcs
            awb_r[28] = 1548; awb_b[28] = 1458; right_left_point_cnt[28] = -35; down_up_point_cnt[28] = -65; awb_block[28] = 20;	//for vcs
            awb_r[29] = 1545; awb_b[29] = 1467; right_left_point_cnt[29] = -35; down_up_point_cnt[29] = -65; awb_block[29] = 20;	//for vcs
            awb_r[30] = 1532; awb_b[30] = 1406; right_left_point_cnt[30] = -30; down_up_point_cnt[30] = -60; awb_block[30] = 16;	//for vcs
            awb_r[31] = 1529; awb_b[31] = 1435; right_left_point_cnt[31] = -30; down_up_point_cnt[31] = -65; awb_block[31] = 20;	//for vcs
            awb_r[32] = 1547; awb_b[32] = 1461; right_left_point_cnt[32] = -35; down_up_point_cnt[32] = -65; awb_block[32] = 20;	//for vcs
            awb_r[33] = 1547; awb_b[33] = 1457; right_left_point_cnt[33] = -35; down_up_point_cnt[33] = -65; awb_block[33] = 20;	//for vcs
            awb_r[34] = 1547; awb_b[34] = 1459; right_left_point_cnt[34] = -35; down_up_point_cnt[34] = -65; awb_block[34] = 20;	//for vcs
            awb_r[35] = 1545; awb_b[35] = 1465; right_left_point_cnt[35] = -35; down_up_point_cnt[35] = -65; awb_block[35] = 20;	//for vcs
            awb_r[36] = 1547; awb_b[36] = 1463; right_left_point_cnt[36] = -35; down_up_point_cnt[36] = -65; awb_block[36] = 20;	//for vcs
            awb_r[37] = 1545; awb_b[37] = 1455; right_left_point_cnt[37] = -35; down_up_point_cnt[37] = -65; awb_block[37] = 20;	//for vcs
            awb_r[38] = 1547; awb_b[38] = 1461; right_left_point_cnt[38] = -35; down_up_point_cnt[38] = -65; awb_block[38] = 20;	//for vcs
            awb_r[39] = 1551; awb_b[39] = 1457; right_left_point_cnt[39] = -35; down_up_point_cnt[39] = -65; awb_block[39] = 20;	//for vcs
            awb_r[40] = 1542; awb_b[40] = 1457; right_left_point_cnt[40] = -35; down_up_point_cnt[40] = -65; awb_block[40] = 20;	//for vcs
            awb_r[41] = 1524; awb_b[41] = 1435; right_left_point_cnt[41] = -30; down_up_point_cnt[41] = -65; awb_block[41] = 20;	//for vcs
            awb_r[42] = 1533; awb_b[42] = 1429; right_left_point_cnt[42] = -30; down_up_point_cnt[42] = -65; awb_block[42] = 20;	//for vcs
            awb_r[43] = 1550; awb_b[43] = 1463; right_left_point_cnt[43] = -35; down_up_point_cnt[43] = -65; awb_block[43] = 20;	//for vcs
            awb_r[44] = 1546; awb_b[44] = 1457; right_left_point_cnt[44] = -35; down_up_point_cnt[44] = -65; awb_block[44] = 20;	//for vcs
            awb_r[45] = 1542; awb_b[45] = 1460; right_left_point_cnt[45] = -35; down_up_point_cnt[45] = -65; awb_block[45] = 20;	//for vcs
            awb_r[46] = 1546; awb_b[46] = 1462; right_left_point_cnt[46] = -35; down_up_point_cnt[46] = -65; awb_block[46] = 20;	//for vcs
            awb_r[47] = 1529; awb_b[47] = 1437; right_left_point_cnt[47] = -30; down_up_point_cnt[47] = -65; awb_block[47] = 20;	//for vcs
            awb_r[48] = 1551; awb_b[48] = 1447; right_left_point_cnt[48] = -35; down_up_point_cnt[48] = -65; awb_block[48] = 20;	//for vcs
            awb_r[49] = 1528; awb_b[49] = 1412; right_left_point_cnt[49] = -30; down_up_point_cnt[49] = -60; awb_block[49] = 16;	//for vcs

            awb_r_avg = awb_r.Average();
            awb_r_max = awb_r.Max();
            awb_r_min = awb_r.Min();

            awb_b_avg = awb_b.Average();
            awb_b_max = awb_b.Max();
            awb_b_min = awb_b.Min();

            W = pictureBox1.Width;
            H = pictureBox1.Height;

            w = W * (100 - BORDER_W * 2) / 100;
            h = H * (100 - BORDER_H * 2) / 100;

            y_max = Math.Max(awb_r_max, awb_b_max);
            y_min = Math.Min(awb_r_min, awb_b_min);

            if (((int)y_max % STEP) != 0)
                y_max = (double)(((int)y_max / STEP + 1) * STEP);

            if (((int)y_min % STEP) != 0)
                y_min = (double)(((int)y_min / STEP) * STEP);

            y_range = y_max - y_min;
            y_range = y_max - y_min;

            ratio_x = (int)((double)w / ROUND);
            ratio_y = (int)((double)h / y_range);

            offset_x = W * BORDER_W / 100;
            offset_y = H * BORDER_H / 100;

            richTextBox1.Text += "awb_r average = " + awb_r_avg.ToString() + "\n";
            richTextBox1.Text += "awb_r max = " + awb_r_max.ToString() + "\n";
            richTextBox1.Text += "awb_r min = " + awb_r_min.ToString() + "\n";

            richTextBox1.Text += "awb_b average = " + awb_b_avg.ToString() + "\n";
            richTextBox1.Text += "awb_b max = " + awb_b_max.ToString() + "\n";
            richTextBox1.Text += "awb_b min = " + awb_b_min.ToString() + "\n";

            richTextBox1.Text += "pictureBox width W = " + W.ToString() + "\n";
            richTextBox1.Text += "pictureBox height H = " + H.ToString() + "\n";
            richTextBox1.Text += "pictureBox draw width w = " + w.ToString() + "\n";
            richTextBox1.Text += "pictureBox draw height h = " + h.ToString() + "\n";

            richTextBox1.Text += "y_max = " + y_max.ToString() + "\n";
            richTextBox1.Text += "y_min = " + y_min.ToString() + "\n";
            richTextBox1.Text += "y_range = " + y_range.ToString() + "\n";

            richTextBox1.Text += "ratio_x = " + ratio_x.ToString() + "\n";
            richTextBox1.Text += "ratio_y = " + ratio_y.ToString() + "\n";

            richTextBox1.Text += "offset_x = " + offset_x.ToString() + "\n";
            richTextBox1.Text += "offset_y = " + offset_y.ToString() + "\n";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_test_result();
        }

        void show_test_result()
        {

            int width;
            int height;

            bitmap1 = new Bitmap(W, H);

            width = bitmap1.Width;
            height = bitmap1.Height;

            richTextBox1.Text += "W = " + width.ToString() + " H = " + height.ToString() + "\n";

            //pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.Image = bitmap1;

            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

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

            /*
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


                g.DrawString(searchinfos[i].cnt.ToString(), new Font("標楷體", 10), new SolidBrush(Color.Red), new PointF(x_st_string, y_st_string));

                g.DrawLine(new Pen(Color.Red, 1), x_st_old, y_st_old, x_st_string+5, y_st_string + 10);

            }
            */
            DrawXY();
            DrawGrid();
            //DrawTick();

            int i;

            Point[] pt_r = new Point[ROUND];    //一維陣列內有 ROUND 個Point
            Point[] pt_b = new Point[ROUND];    //一維陣列內有 ROUND 個Point

            for (i = 0; i < ROUND; i++)
            {
                pt_r[i].X = offset_x + ratio_x * (i + 1);
                pt_r[i].Y = (int)(H - (offset_y + (awb_r[i] - y_min) * ratio_y));
                pt_b[i].X = offset_x + ratio_x * (i + 1);
                pt_b[i].Y = (int)(H - (offset_y + (awb_b[i] - y_min) * ratio_y));
            }

            g.DrawLines(new Pen(Brushes.Red, 3), pt_r);
            g.DrawLines(new Pen(Brushes.Blue, 3), pt_b);

            double sd_r;
            sd_r = SD(awb_r);
            richTextBox1.Text += "awb_r SD = " + sd_r.ToString() + "\n";

            double sd_b;
            sd_b = SD(awb_b);
            richTextBox1.Text += "awb_b SD = " + sd_b.ToString() + "\n";

            int x_st;
            int y_st;
            int x_sp;
            int y_sp;

            x_st = offset_x;
            y_st = (int)((H - offset_y) - ((awb_r_avg - y_min)) * ratio_y);
            x_sp = offset_x + w;
            y_sp = y_st;
            g.DrawLine(new Pen(Color.DarkRed, 1), x_st, y_st, x_sp, y_sp);

            y_st = (int)((H - offset_y) - ((awb_b_avg - y_min)) * ratio_y);
            y_sp = y_st;
            g.DrawLine(new Pen(Color.DarkBlue, 1), x_st, y_st, x_sp, y_sp);

            y_st = (int)((H - offset_y) - ((awb_r_avg + sd_r - y_min)) * ratio_y);    //+1 SD
            y_sp = y_st;
            g.DrawLine(new Pen(Color.Red, 1), x_st, y_st, x_sp, y_sp);

            y_st = (int)((H - offset_y) - ((awb_r_avg - sd_r - y_min)) * ratio_y);    //-1 SD
            y_sp = y_st;
            g.DrawLine(new Pen(Color.Red, 1), x_st, y_st, x_sp, y_sp);

            y_st = (int)((H - offset_y) - ((awb_b_avg + sd_b - y_min)) * ratio_y);    //+1 SD
            y_sp = y_st;
            g.DrawLine(new Pen(Color.Blue, 1), x_st, y_st, x_sp, y_sp);

            y_st = (int)((H - offset_y) - ((awb_b_avg - sd_b - y_min)) * ratio_y);    //-1 SD
            y_sp = y_st;
            g.DrawLine(new Pen(Color.Blue, 1), x_st, y_st, x_sp, y_sp);

            /*
            y_st = (int)(H - ((awb_b_avg - y_min)) * ratio_y - offset_y);
            y_sp = y_st;
            g.DrawLine(new Pen(Color.Blue, 1), x_st, y_st, x_sp, y_sp);
            */

            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //show_test_result();
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

        private void DrawXY()//画X轴Y轴
        {
            Point px1 = new Point(this.pictureBox1.Width * BORDER_W / 100, this.pictureBox1.Height * (100 - BORDER_H) / 100);
            Point px2 = new Point(this.pictureBox1.Width * (100 - BORDER_W) / 100, this.pictureBox1.Height * (100 - BORDER_H) / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            Point py1 = new Point(this.pictureBox1.Width * BORDER_W / 100, this.pictureBox1.Height * (100 - BORDER_H) / 100);
            Point py2 = new Point(this.pictureBox1.Width * BORDER_W / 100, this.pictureBox1.Height * BORDER_H / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
        }

        private void DrawGrid_X()    //grid on x, 水平格線
        {
            int i;
            int x1;
            int x2;
            int y1;
            int y2;

            for (i = ((int)y_min + STEP); i <= (int)y_max; i += STEP)
            {
                x1 = offset_x;
                y1 = H - (offset_y + (i - (int)y_min) * ratio_y);

                richTextBox1.Text += "i = " + i.ToString() + " ";
                richTextBox1.Text += "y = " + y1.ToString() + "\n";

                x2 = offset_x + w;
                y2 = y1;
                Point px1 = new Point(x1, y1);
                Point px2 = new Point(x2, y2);
                g.DrawLine(new Pen(Brushes.Pink, 1), px1, px2);
            }

        }

        private void DrawGrid_Y()    //grid on y, 垂直格線
        {
            int i;
            int x1;
            int x2;
            int y1;
            int y2;

            for (i = 0; i < ROUND; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\n";

                if ((i % 5) == 4)
                {
                    x1 = offset_x + ratio_x * (i + 1);
                    y1 = H - offset_y;
                    x2 = x1;
                    y2 = H - offset_y - h;

                    Point px1 = new Point(x1, y1);
                    Point px2 = new Point(x2, y2);
                    g.DrawLine(new Pen(Brushes.Pink, 1), px1, px2);
                }
            }
        }

        private void DrawGrid()    //grid on
        {
            DrawGrid_X();   //水平格線
            DrawGrid_Y();   //垂直格線
        }

        private void DrawTick_X()    //tick on x
        {
            int i;
            int x1;
            int x2;
            int y1;
            int y2;

            for (i = 0; i < ROUND; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\n";
                if ((i % 5) == 4)   //Major tick
                {
                    x1 = offset_x + ratio_x * (i + 1);
                    y1 = H - offset_y;
                    x2 = x1;
                    y2 = H - offset_y - 40;
                    Point px1 = new Point(x1, y1);
                    Point px2 = new Point(x2, y2);
                    g.DrawLine(new Pen(Brushes.DeepPink, 3), px1, px2);
                }
                else      //Minor tick
                {
                    x1 = offset_x + ratio_x * (i + 1);
                    y1 = H - offset_y;
                    x2 = x1;
                    y2 = H - offset_y - 20;
                    Point px1 = new Point(x1, y1);
                    Point px2 = new Point(x2, y2);
                    g.DrawLine(new Pen(Brushes.Pink, 1), px1, px2);
                }
            }


        }

        private void DrawTick_Y()    //tick on y
        {
            int i;
            int x1;
            int x2;
            int y1;
            int y2;


            //richTextBox1.Text += "h = " + h.ToString() + ", cnt = " + (h / 100).ToString() + "\n";
            for (i = 1; i <= h / 100; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\n";
                x1 = offset_x;
                y1 = H - offset_y - i * 100;
                x2 = offset_x + 50;
                y2 = y1;
                Point px1 = new Point(x1, y1);
                Point px2 = new Point(x2, y2);
                g.DrawLine(new Pen(Brushes.Pink, 1), px1, px2);
            }

        }


        private void DrawTick()    //tick on
        {
            DrawTick_X();
            DrawTick_Y();
        }





    }
}
