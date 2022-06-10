using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_2D_Matrix
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }


        int COLUMN = 360 + 1 + 360;
        int ROW = 360 + 1 + 360;

        void draw_contour(int cx, int cy)
        {
            int i, j;
            //                                  R   C
            double[,] brightness = new double[ROW, COLUMN];    //Row = 19, Column = 8
            int[,] brightness2 = new int[ROW, COLUMN];    //Row = 19, Column = 8

            //richTextBox1.Text += "assign value\n";

            double stepx = 360.0 / ((COLUMN - 1) / 2);
            double stepy = 360.0 / ((ROW - 1) / 2);

            double max = 0;
            double min = 100;
            double vv = 0;

            //richTextBox1.Text += "stepx = " + stepx.ToString() + "\tstepy = " + stepy.ToString() + "\n";

            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COLUMN; i++)
                {
                    vv = F1(i - cx, j - cy);

                    brightness[j, i] = vv;
                    if (vv > max)
                        max = vv;
                    else if (vv < min)
                        min = vv;

                    //對應到0~255
                    brightness2[j, i] = (int)((vv + 2.0) * 64);
                    if (brightness2[j, i] == 256)
                    {
                        brightness2[j, i] = 255;
                    }
                    brightness2[j, i] = (brightness2[j, i] / 5) * 5;
                }
            }
            //richTextBox1.Text += "max = " + max.ToString() + "\tmin = " + min.ToString() + "\n";

            /*
            richTextBox1.Text += "print value\n";
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    richTextBox1.Text += gray[j, i].ToString("D2") + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            /*
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    //richTextBox1.Text += brightness[j, i].ToString("D2") + "\t";
                    //richTextBox1.Text += brightness[j, i].ToString() + "\t";
                    richTextBox1.Text += ((int)(brightness[j, i] * 100)).ToString("D2") + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            //逐點製作圖檔

            Bitmap bitmap1 = new Bitmap(COLUMN, ROW);

            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COLUMN; i++)
                {
                    if (((i % 100) == 0) && ((j % 50) == 0))
                    {
                        //bitmap1.SetPixel(i, j, Color.Red);
                        brightness2[j, i] = 255;
                    }
                    bitmap1.SetPixel(i, j, Color.FromArgb(255, (byte)(brightness2[j, i]), (byte)(brightness2[j, i]), (byte)(brightness2[j, i])));
                }
            }

            /*
            Graphics g = Graphics.FromImage(bitmap1);
            Pen p = new Pen(Color.Red, 5);
            Point point1a = new Point(0, 360);
            Point point2a = new Point(720, 360);
            g.DrawLine(p, point1a, point2a);

            point1a = new Point(360, 0);
            point2a = new Point(360, 720);
            g.DrawLine(p, point1a, point2a);
            */

            pictureBox1.Image = bitmap1;
            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            draw_contour(cx, cy);
        }

        int dd = 20;
        int cx = 360;
        int cy = 360;
        private void timer1_Tick(object sender, EventArgs e)
        {
            cx += dd;
            cy += dd;
            if (cx > 721)
                cx = dd;
            if (cy > 721)
                cy = dd;
            draw_contour(cx, cy);
        }

        private double F1(int x, int y)
        {
            return cosd(x) + cosd(y);   //z=cox(x) + cos(y)
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Graphics g;
            Pen p;
            SolidBrush sb;
            Bitmap bitmap1;

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;



            g.Clear(Color.White);
            int[,] gray = new int[31, 23];

            gray[0, 0] = 8;
            gray[1, 0] = 7;
            gray[2, 0] = 8;
            gray[3, 0] = 10;
            gray[4, 0] = 27;
            gray[5, 0] = 85;
            gray[6, 0] = 126;
            gray[7, 0] = 134;
            gray[8, 0] = 138;
            gray[9, 0] = 140;
            gray[10, 0] = 142;
            gray[11, 0] = 143;
            gray[12, 0] = 144;
            gray[13, 0] = 144;
            gray[14, 0] = 146;
            gray[15, 0] = 146;
            gray[16, 0] = 146;
            gray[17, 0] = 146;
            gray[18, 0] = 145;
            gray[19, 0] = 144;
            gray[20, 0] = 141;
            gray[21, 0] = 140;
            gray[22, 0] = 138;
            gray[23, 0] = 135;
            gray[24, 0] = 130;
            gray[25, 0] = 98;
            gray[26, 0] = 28;
            gray[27, 0] = 9;
            gray[28, 0] = 7;
            gray[29, 0] = 8;
            gray[30, 0] = 9;
            gray[0, 1] = 7;
            gray[1, 1] = 8;
            gray[2, 1] = 11;
            gray[3, 1] = 36;
            gray[4, 1] = 105;
            gray[5, 1] = 130;
            gray[6, 1] = 135;
            gray[7, 1] = 139;
            gray[8, 1] = 142;
            gray[9, 1] = 144;
            gray[10, 1] = 146;
            gray[11, 1] = 147;
            gray[12, 1] = 149;
            gray[13, 1] = 150;
            gray[14, 1] = 151;
            gray[15, 1] = 151;
            gray[16, 1] = 151;
            gray[17, 1] = 150;
            gray[18, 1] = 149;
            gray[19, 1] = 148;
            gray[20, 1] = 146;
            gray[21, 1] = 144;
            gray[22, 1] = 142;
            gray[23, 1] = 139;
            gray[24, 1] = 136;
            gray[25, 1] = 131;
            gray[26, 1] = 96;
            gray[27, 1] = 25;
            gray[28, 1] = 9;
            gray[29, 1] = 7;
            gray[30, 1] = 8;
            gray[0, 2] = 7;
            gray[1, 2] = 9;
            gray[2, 2] = 31;
            gray[3, 2] = 107;
            gray[4, 2] = 130;
            gray[5, 2] = 135;
            gray[6, 2] = 139;
            gray[7, 2] = 143;
            gray[8, 2] = 145;
            gray[9, 2] = 148;
            gray[10, 2] = 150;
            gray[11, 2] = 151;
            gray[12, 2] = 153;
            gray[13, 2] = 154;
            gray[14, 2] = 155;
            gray[15, 2] = 155;
            gray[16, 2] = 155;
            gray[17, 2] = 154;
            gray[18, 2] = 154;
            gray[19, 2] = 152;
            gray[20, 2] = 150;
            gray[21, 2] = 149;
            gray[22, 2] = 147;
            gray[23, 2] = 144;
            gray[24, 2] = 140;
            gray[25, 2] = 136;
            gray[26, 2] = 130;
            gray[27, 2] = 92;
            gray[28, 2] = 26;
            gray[29, 2] = 9;
            gray[30, 2] = 7;
            gray[0, 3] = 8;
            gray[1, 3] = 18;
            gray[2, 3] = 91;
            gray[3, 3] = 127;
            gray[4, 3] = 134;
            gray[5, 3] = 139;
            gray[6, 3] = 142;
            gray[7, 3] = 145;
            gray[8, 3] = 148;
            gray[9, 3] = 151;
            gray[10, 3] = 153;
            gray[11, 3] = 154;
            gray[12, 3] = 156;
            gray[13, 3] = 157;
            gray[14, 3] = 158;
            gray[15, 3] = 157;
            gray[16, 3] = 158;
            gray[17, 3] = 157;
            gray[18, 3] = 157;
            gray[19, 3] = 156;
            gray[20, 3] = 154;
            gray[21, 3] = 152;
            gray[22, 3] = 150;
            gray[23, 3] = 147;
            gray[24, 3] = 143;
            gray[25, 3] = 139;
            gray[26, 3] = 134;
            gray[27, 3] = 128;
            gray[28, 3] = 97;
            gray[29, 3] = 22;
            gray[30, 3] = 7;
            gray[0, 4] = 11;
            gray[1, 4] = 59;
            gray[2, 4] = 122;
            gray[3, 4] = 131;
            gray[4, 4] = 136;
            gray[5, 4] = 141;
            gray[6, 4] = 145;
            gray[7, 4] = 148;
            gray[8, 4] = 151;
            gray[9, 4] = 153;
            gray[10, 4] = 155;
            gray[11, 4] = 156;
            gray[12, 4] = 158;
            gray[13, 4] = 159;
            gray[14, 4] = 159;
            gray[15, 4] = 159;
            gray[16, 4] = 159;
            gray[17, 4] = 159;
            gray[18, 4] = 159;
            gray[19, 4] = 158;
            gray[20, 4] = 157;
            gray[21, 4] = 155;
            gray[22, 4] = 152;
            gray[23, 4] = 149;
            gray[24, 4] = 146;
            gray[25, 4] = 142;
            gray[26, 4] = 138;
            gray[27, 4] = 132;
            gray[28, 4] = 125;
            gray[29, 4] = 66;
            gray[30, 4] = 10;
            gray[0, 5] = 26;
            gray[1, 5] = 105;
            gray[2, 5] = 126;
            gray[3, 5] = 133;
            gray[4, 5] = 138;
            gray[5, 5] = 143;
            gray[6, 5] = 146;
            gray[7, 5] = 150;
            gray[8, 5] = 152;
            gray[9, 5] = 155;
            gray[10, 5] = 156;
            gray[11, 5] = 158;
            gray[12, 5] = 159;
            gray[13, 5] = 160;
            gray[14, 5] = 161;
            gray[15, 5] = 161;
            gray[16, 5] = 161;
            gray[17, 5] = 161;
            gray[18, 5] = 160;
            gray[19, 5] = 160;
            gray[20, 5] = 158;
            gray[21, 5] = 156;
            gray[22, 5] = 154;
            gray[23, 5] = 152;
            gray[24, 5] = 148;
            gray[25, 5] = 143;
            gray[26, 5] = 139;
            gray[27, 5] = 133;
            gray[28, 5] = 127;
            gray[29, 5] = 107;
            gray[30, 5] = 22;
            gray[0, 6] = 62;
            gray[1, 6] = 119;
            gray[2, 6] = 127;
            gray[3, 6] = 134;
            gray[4, 6] = 139;
            gray[5, 6] = 144;
            gray[6, 6] = 147;
            gray[7, 6] = 151;
            gray[8, 6] = 154;
            gray[9, 6] = 156;
            gray[10, 6] = 157;
            gray[11, 6] = 159;
            gray[12, 6] = 160;
            gray[13, 6] = 161;
            gray[14, 6] = 162;
            gray[15, 6] = 162;
            gray[16, 6] = 162;
            gray[17, 6] = 162;
            gray[18, 6] = 162;
            gray[19, 6] = 161;
            gray[20, 6] = 159;
            gray[21, 6] = 157;
            gray[22, 6] = 156;
            gray[23, 6] = 153;
            gray[24, 6] = 149;
            gray[25, 6] = 145;
            gray[26, 6] = 141;
            gray[27, 6] = 135;
            gray[28, 6] = 129;
            gray[29, 6] = 122;
            gray[30, 6] = 51;
            gray[0, 7] = 94;
            gray[1, 7] = 120;
            gray[2, 7] = 128;
            gray[3, 7] = 135;
            gray[4, 7] = 140;
            gray[5, 7] = 145;
            gray[6, 7] = 148;
            gray[7, 7] = 152;
            gray[8, 7] = 154;
            gray[9, 7] = 156;
            gray[10, 7] = 158;
            gray[11, 7] = 159;
            gray[12, 7] = 161;
            gray[13, 7] = 162;
            gray[14, 7] = 164;
            gray[15, 7] = 166;
            gray[16, 7] = 166;
            gray[17, 7] = 165;
            gray[18, 7] = 164;
            gray[19, 7] = 162;
            gray[20, 7] = 161;
            gray[21, 7] = 159;
            gray[22, 7] = 155;
            gray[23, 7] = 153;
            gray[24, 7] = 149;
            gray[25, 7] = 147;
            gray[26, 7] = 141;
            gray[27, 7] = 135;
            gray[28, 7] = 130;
            gray[29, 7] = 123;
            gray[30, 7] = 80;
            gray[0, 8] = 108;
            gray[1, 8] = 121;
            gray[2, 8] = 129;
            gray[3, 8] = 136;
            gray[4, 8] = 141;
            gray[5, 8] = 146;
            gray[6, 8] = 149;
            gray[7, 8] = 153;
            gray[8, 8] = 155;
            gray[9, 8] = 156;
            gray[10, 8] = 158;
            gray[11, 8] = 160;
            gray[12, 8] = 162;
            gray[13, 8] = 165;
            gray[14, 8] = 168;
            gray[15, 8] = 169;
            gray[16, 8] = 168;
            gray[17, 8] = 168;
            gray[18, 8] = 167;
            gray[19, 8] = 164;
            gray[20, 8] = 161;
            gray[21, 8] = 160;
            gray[22, 8] = 157;
            gray[23, 8] = 153;
            gray[24, 8] = 149;
            gray[25, 8] = 145;
            gray[26, 8] = 140;
            gray[27, 8] = 135;
            gray[28, 8] = 129;
            gray[29, 8] = 124;
            gray[30, 8] = 100;
            gray[0, 9] = 111;
            gray[1, 9] = 121;
            gray[2, 9] = 130;
            gray[3, 9] = 136;
            gray[4, 9] = 142;
            gray[5, 9] = 146;
            gray[6, 9] = 150;
            gray[7, 9] = 153;
            gray[8, 9] = 155;
            gray[9, 9] = 157;
            gray[10, 9] = 158;
            gray[11, 9] = 160;
            gray[12, 9] = 163;
            gray[13, 9] = 168;
            gray[14, 9] = 169;
            gray[15, 9] = 171;
            gray[16, 9] = 170;
            gray[17, 9] = 169;
            gray[18, 9] = 168;
            gray[19, 9] = 166;
            gray[20, 9] = 162;
            gray[21, 9] = 160;
            gray[22, 9] = 158;
            gray[23, 9] = 154;
            gray[24, 9] = 150;
            gray[25, 9] = 147;
            gray[26, 9] = 143;
            gray[27, 9] = 137;
            gray[28, 9] = 132;
            gray[29, 9] = 126;
            gray[30, 9] = 114;
            gray[0, 10] = 112;
            gray[1, 10] = 121;
            gray[2, 10] = 129;
            gray[3, 10] = 136;
            gray[4, 10] = 142;
            gray[5, 10] = 146;
            gray[6, 10] = 150;
            gray[7, 10] = 152;
            gray[8, 10] = 155;
            gray[9, 10] = 157;
            gray[10, 10] = 158;
            gray[11, 10] = 160;
            gray[12, 10] = 164;
            gray[13, 10] = 168;
            gray[14, 10] = 171;
            gray[15, 10] = 172;
            gray[16, 10] = 172;
            gray[17, 10] = 169;
            gray[18, 10] = 167;
            gray[19, 10] = 166;
            gray[20, 10] = 163;
            gray[21, 10] = 160;
            gray[22, 10] = 158;
            gray[23, 10] = 154;
            gray[24, 10] = 152;
            gray[25, 10] = 148;
            gray[26, 10] = 143;
            gray[27, 10] = 139;
            gray[28, 10] = 133;
            gray[29, 10] = 126;
            gray[30, 10] = 118;
            gray[0, 11] = 111;
            gray[1, 11] = 121;
            gray[2, 11] = 129;
            gray[3, 11] = 135;
            gray[4, 11] = 141;
            gray[5, 11] = 145;
            gray[6, 11] = 149;
            gray[7, 11] = 151;
            gray[8, 11] = 154;
            gray[9, 11] = 156;
            gray[10, 11] = 158;
            gray[11, 11] = 159;
            gray[12, 11] = 164;
            gray[13, 11] = 168;
            gray[14, 11] = 170;
            gray[15, 11] = 172;
            gray[16, 11] = 171;
            gray[17, 11] = 169;
            gray[18, 11] = 167;
            gray[19, 11] = 166;
            gray[20, 11] = 162;
            gray[21, 11] = 160;
            gray[22, 11] = 158;
            gray[23, 11] = 155;
            gray[24, 11] = 152;
            gray[25, 11] = 148;
            gray[26, 11] = 144;
            gray[27, 11] = 138;
            gray[28, 11] = 132;
            gray[29, 11] = 126;
            gray[30, 11] = 118;
            gray[0, 12] = 111;
            gray[1, 12] = 120;
            gray[2, 12] = 128;
            gray[3, 12] = 135;
            gray[4, 12] = 140;
            gray[5, 12] = 145;
            gray[6, 12] = 148;
            gray[7, 12] = 150;
            gray[8, 12] = 153;
            gray[9, 12] = 155;
            gray[10, 12] = 157;
            gray[11, 12] = 158;
            gray[12, 12] = 162;
            gray[13, 12] = 166;
            gray[14, 12] = 168;
            gray[15, 12] = 170;
            gray[16, 12] = 170;
            gray[17, 12] = 167;
            gray[18, 12] = 166;
            gray[19, 12] = 165;
            gray[20, 12] = 161;
            gray[21, 12] = 159;
            gray[22, 12] = 157;
            gray[23, 12] = 155;
            gray[24, 12] = 151;
            gray[25, 12] = 148;
            gray[26, 12] = 144;
            gray[27, 12] = 138;
            gray[28, 12] = 131;
            gray[29, 12] = 124;
            gray[30, 12] = 117;
            gray[0, 13] = 110;
            gray[1, 13] = 120;
            gray[2, 13] = 127;
            gray[3, 13] = 134;
            gray[4, 13] = 139;
            gray[5, 13] = 144;
            gray[6, 13] = 147;
            gray[7, 13] = 150;
            gray[8, 13] = 152;
            gray[9, 13] = 155;
            gray[10, 13] = 156;
            gray[11, 13] = 157;
            gray[12, 13] = 158;
            gray[13, 13] = 163;
            gray[14, 13] = 165;
            gray[15, 13] = 166;
            gray[16, 13] = 166;
            gray[17, 13] = 166;
            gray[18, 13] = 165;
            gray[19, 13] = 162;
            gray[20, 13] = 159;
            gray[21, 13] = 158;
            gray[22, 13] = 156;
            gray[23, 13] = 151;
            gray[24, 13] = 148;
            gray[25, 13] = 145;
            gray[26, 13] = 142;
            gray[27, 13] = 138;
            gray[28, 13] = 131;
            gray[29, 13] = 124;
            gray[30, 13] = 116;
            gray[0, 14] = 110;
            gray[1, 14] = 119;
            gray[2, 14] = 127;
            gray[3, 14] = 133;
            gray[4, 14] = 139;
            gray[5, 14] = 143;
            gray[6, 14] = 147;
            gray[7, 14] = 149;
            gray[8, 14] = 151;
            gray[9, 14] = 153;
            gray[10, 14] = 154;
            gray[11, 14] = 155;
            gray[12, 14] = 156;
            gray[13, 14] = 159;
            gray[14, 14] = 162;
            gray[15, 14] = 163;
            gray[16, 14] = 164;
            gray[17, 14] = 163;
            gray[18, 14] = 161;
            gray[19, 14] = 159;
            gray[20, 14] = 157;
            gray[21, 14] = 156;
            gray[22, 14] = 153;
            gray[23, 14] = 150;
            gray[24, 14] = 147;
            gray[25, 14] = 144;
            gray[26, 14] = 141;
            gray[27, 14] = 136;
            gray[28, 14] = 130;
            gray[29, 14] = 123;
            gray[30, 14] = 115;
            gray[0, 15] = 109;
            gray[1, 15] = 118;
            gray[2, 15] = 125;
            gray[3, 15] = 132;
            gray[4, 15] = 138;
            gray[5, 15] = 142;
            gray[6, 15] = 145;
            gray[7, 15] = 148;
            gray[8, 15] = 150;
            gray[9, 15] = 152;
            gray[10, 15] = 153;
            gray[11, 15] = 154;
            gray[12, 15] = 155;
            gray[13, 15] = 156;
            gray[14, 15] = 157;
            gray[15, 15] = 158;
            gray[16, 15] = 158;
            gray[17, 15] = 158;
            gray[18, 15] = 158;
            gray[19, 15] = 157;
            gray[20, 15] = 156;
            gray[21, 15] = 153;
            gray[22, 15] = 151;
            gray[23, 15] = 149;
            gray[24, 15] = 146;
            gray[25, 15] = 143;
            gray[26, 15] = 139;
            gray[27, 15] = 134;
            gray[28, 15] = 129;
            gray[29, 15] = 122;
            gray[30, 15] = 113;
            gray[0, 16] = 107;
            gray[1, 16] = 116;
            gray[2, 16] = 124;
            gray[3, 16] = 131;
            gray[4, 16] = 136;
            gray[5, 16] = 140;
            gray[6, 16] = 144;
            gray[7, 16] = 146;
            gray[8, 16] = 148;
            gray[9, 16] = 150;
            gray[10, 16] = 152;
            gray[11, 16] = 153;
            gray[12, 16] = 154;
            gray[13, 16] = 154;
            gray[14, 16] = 154;
            gray[15, 16] = 155;
            gray[16, 16] = 156;
            gray[17, 16] = 156;
            gray[18, 16] = 156;
            gray[19, 16] = 155;
            gray[20, 16] = 154;
            gray[21, 16] = 152;
            gray[22, 16] = 149;
            gray[23, 16] = 148;
            gray[24, 16] = 145;
            gray[25, 16] = 141;
            gray[26, 16] = 138;
            gray[27, 16] = 133;
            gray[28, 16] = 127;
            gray[29, 16] = 119;
            gray[30, 16] = 106;
            gray[0, 17] = 104;
            gray[1, 17] = 114;
            gray[2, 17] = 122;
            gray[3, 17] = 128;
            gray[4, 17] = 134;
            gray[5, 17] = 138;
            gray[6, 17] = 142;
            gray[7, 17] = 144;
            gray[8, 17] = 147;
            gray[9, 17] = 148;
            gray[10, 17] = 150;
            gray[11, 17] = 151;
            gray[12, 17] = 152;
            gray[13, 17] = 153;
            gray[14, 17] = 153;
            gray[15, 17] = 153;
            gray[16, 17] = 153;
            gray[17, 17] = 153;
            gray[18, 17] = 153;
            gray[19, 17] = 152;
            gray[20, 17] = 151;
            gray[21, 17] = 150;
            gray[22, 17] = 148;
            gray[23, 17] = 146;
            gray[24, 17] = 143;
            gray[25, 17] = 140;
            gray[26, 17] = 136;
            gray[27, 17] = 131;
            gray[28, 17] = 124;
            gray[29, 17] = 116;
            gray[30, 17] = 95;
            gray[0, 18] = 97;
            gray[1, 18] = 111;
            gray[2, 18] = 119;
            gray[3, 18] = 126;
            gray[4, 18] = 131;
            gray[5, 18] = 136;
            gray[6, 18] = 139;
            gray[7, 18] = 142;
            gray[8, 18] = 144;
            gray[9, 18] = 146;
            gray[10, 18] = 148;
            gray[11, 18] = 148;
            gray[12, 18] = 150;
            gray[13, 18] = 150;
            gray[14, 18] = 151;
            gray[15, 18] = 151;
            gray[16, 18] = 151;
            gray[17, 18] = 151;
            gray[18, 18] = 151;
            gray[19, 18] = 150;
            gray[20, 18] = 149;
            gray[21, 18] = 147;
            gray[22, 18] = 146;
            gray[23, 18] = 143;
            gray[24, 18] = 140;
            gray[25, 18] = 136;
            gray[26, 18] = 133;
            gray[27, 18] = 129;
            gray[28, 18] = 122;
            gray[29, 18] = 114;
            gray[30, 18] = 77;
            gray[0, 19] = 74;
            gray[1, 19] = 107;
            gray[2, 19] = 115;
            gray[3, 19] = 122;
            gray[4, 19] = 128;
            gray[5, 19] = 132;
            gray[6, 19] = 136;
            gray[7, 19] = 140;
            gray[8, 19] = 141;
            gray[9, 19] = 143;
            gray[10, 19] = 144;
            gray[11, 19] = 145;
            gray[12, 19] = 147;
            gray[13, 19] = 148;
            gray[14, 19] = 148;
            gray[15, 19] = 148;
            gray[16, 19] = 149;
            gray[17, 19] = 148;
            gray[18, 19] = 148;
            gray[19, 19] = 147;
            gray[20, 19] = 146;
            gray[21, 19] = 145;
            gray[22, 19] = 143;
            gray[23, 19] = 141;
            gray[24, 19] = 137;
            gray[25, 19] = 134;
            gray[26, 19] = 130;
            gray[27, 19] = 125;
            gray[28, 19] = 119;
            gray[29, 19] = 110;
            gray[30, 19] = 43;
            gray[0, 20] = 34;
            gray[1, 20] = 99;
            gray[2, 20] = 111;
            gray[3, 20] = 118;
            gray[4, 20] = 123;
            gray[5, 20] = 129;
            gray[6, 20] = 133;
            gray[7, 20] = 136;
            gray[8, 20] = 139;
            gray[9, 20] = 139;
            gray[10, 20] = 140;
            gray[11, 20] = 141;
            gray[12, 20] = 143;
            gray[13, 20] = 145;
            gray[14, 20] = 145;
            gray[15, 20] = 146;
            gray[16, 20] = 145;
            gray[17, 20] = 145;
            gray[18, 20] = 145;
            gray[19, 20] = 144;
            gray[20, 20] = 143;
            gray[21, 20] = 141;
            gray[22, 20] = 140;
            gray[23, 20] = 137;
            gray[24, 20] = 134;
            gray[25, 20] = 131;
            gray[26, 20] = 127;
            gray[27, 20] = 121;
            gray[28, 20] = 115;
            gray[29, 20] = 89;
            gray[30, 20] = 15;
            gray[0, 21] = 11;
            gray[1, 21] = 69;
            gray[2, 21] = 104;
            gray[3, 21] = 112;
            gray[4, 21] = 119;
            gray[5, 21] = 124;
            gray[6, 21] = 129;
            gray[7, 21] = 132;
            gray[8, 21] = 134;
            gray[9, 21] = 135;
            gray[10, 21] = 136;
            gray[11, 21] = 137;
            gray[12, 21] = 139;
            gray[13, 21] = 140;
            gray[14, 21] = 141;
            gray[15, 21] = 142;
            gray[16, 21] = 142;
            gray[17, 21] = 142;
            gray[18, 21] = 142;
            gray[19, 21] = 140;
            gray[20, 21] = 139;
            gray[21, 21] = 138;
            gray[22, 21] = 136;
            gray[23, 21] = 134;
            gray[24, 21] = 131;
            gray[25, 21] = 127;
            gray[26, 21] = 122;
            gray[27, 21] = 116;
            gray[28, 21] = 109;
            gray[29, 21] = 42;
            gray[30, 21] = 8;
            gray[0, 22] = 6;
            gray[1, 22] = 22;
            gray[2, 22] = 87;
            gray[3, 22] = 106;
            gray[4, 22] = 113;
            gray[5, 22] = 118;
            gray[6, 22] = 123;
            gray[7, 22] = 127;
            gray[8, 22] = 130;
            gray[9, 22] = 130;
            gray[10, 22] = 132;
            gray[11, 22] = 133;
            gray[12, 22] = 135;
            gray[13, 22] = 136;
            gray[14, 22] = 137;
            gray[15, 22] = 137;
            gray[16, 22] = 137;
            gray[17, 22] = 138;
            gray[18, 22] = 137;
            gray[19, 22] = 137;
            gray[20, 22] = 135;
            gray[21, 22] = 134;
            gray[22, 22] = 131;
            gray[23, 22] = 129;
            gray[24, 22] = 126;
            gray[25, 22] = 122;
            gray[26, 22] = 117;
            gray[27, 22] = 111;
            gray[28, 22] = 74;
            gray[29, 22] = 12;
            gray[30, 22] = 5;

            /*
            for (j = 0; j < 11; j++)
            {
                for (i = 0; i < 15; i++)
                {
                    richTextBox1.Text += gray[i, j].ToString() + " ";
                }
                richTextBox1.Text += "\n";
            }
            */

            int dd = 20;
            int xx;
            int yy;
            int width = dd * 31;
            int height = dd * 23;

            pictureBox1.Size = new Size(width, height);
            bitmap1 = new Bitmap(width, height);

            byte aa = 255;
            byte rr = 0;
            byte gg = 0;
            byte bb = 0;

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //Color p = Color.FromName("SlateBlue");
                    /*
                    Color p ;
                    p.A = (byte)(xx % 255);
                    p.R = (byte)(xx % 127 + 127);
                    p.G = (byte)(xx % 127);
                    p.B = (byte)(xx % 63);
                    */


                    //獲取像素的ＲＧＢ顏色值
                    //srcColor = srcBitmap.GetPixel(x, y);
                    //byte temp = (byte)(srcColor.R * .299 + srcColor.G * .587 + srcColor.B * .114);

                    //byte temp = (byte)((byte)(xx % 255) + (byte)(xx % 127 + 127) + (byte)(xx % 63));

                    //設置像素的ＲＧＢ顏色值
                    rr = (byte)gray[xx / dd, yy / dd];
                    gg = (byte)gray[xx / dd, yy / dd];
                    bb = (byte)gray[xx / dd, yy / dd];
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                }
            }
            pictureBox1.Image = bitmap1;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Graphics g;
            Pen p;
            SolidBrush sb;
            Bitmap bitmap1;

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;


            int i, j;

            int[] awb_r = new int[225];
            int[] awb_b = new int[225];

            awb_r[0] = 1301; awb_b[0] = 1971;//right_left_point_cnt[0]=0;down_up_point_cnt[0]=0;awb_block[0]=32;	//for vcs2b
            awb_r[1] = 1302; awb_b[1] = 1963;//right_left_point_cnt[1]=0;down_up_point_cnt[1]=0;awb_block[1]=32;	//for vcs2b
            awb_r[2] = 1302; awb_b[2] = 1964;//right_left_point_cnt[2]=0;down_up_point_cnt[2]=0;awb_block[2]=32;	//for vcs2b
            awb_r[3] = 1305; awb_b[3] = 1959;//right_left_point_cnt[3]=0;down_up_point_cnt[3]=0;awb_block[3]=32;	//for vcs2b
            awb_r[4] = 1293; awb_b[4] = 1958;//right_left_point_cnt[4]=0;down_up_point_cnt[4]=0;awb_block[4]=32;	//for vcs2b
            awb_r[5] = 1293; awb_b[5] = 1958;//right_left_point_cnt[5]=0;down_up_point_cnt[5]=0;awb_block[5]=32;	//for vcs2b
            awb_r[6] = 1291; awb_b[6] = 1954;//right_left_point_cnt[6]=0;down_up_point_cnt[6]=0;awb_block[6]=32;	//for vcs2b
            awb_r[7] = 1287; awb_b[7] = 1896;//right_left_point_cnt[7]=0;down_up_point_cnt[7]=0;awb_block[7]=32;	//for vcs2b
            awb_r[8] = 1285; awb_b[8] = 1950;//right_left_point_cnt[8]=0;down_up_point_cnt[8]=0;awb_block[8]=32;	//for vcs2b
            awb_r[9] = 1284; awb_b[9] = 1947;//right_left_point_cnt[9]=0;down_up_point_cnt[9]=0;awb_block[9]=32;	//for vcs2b
            awb_r[10] = 1286; awb_b[10] = 1945;//right_left_point_cnt[10]=0;down_up_point_cnt[10]=0;awb_block[10]=32;	//for vcs2b
            awb_r[11] = 1291; awb_b[11] = 1947;//right_left_point_cnt[11]=0;down_up_point_cnt[11]=0;awb_block[11]=32;	//for vcs2b
            awb_r[12] = 1286; awb_b[12] = 1953;//right_left_point_cnt[12]=0;down_up_point_cnt[12]=0;awb_block[12]=32;	//for vcs2b
            awb_r[13] = 1289; awb_b[13] = 1964;//right_left_point_cnt[13]=0;down_up_point_cnt[13]=0;awb_block[13]=32;	//for vcs2b
            awb_r[14] = 1287; awb_b[14] = 1973;//right_left_point_cnt[14]=0;down_up_point_cnt[14]=0;awb_block[14]=32;	//for vcs2b
            awb_r[15] = 1304; awb_b[15] = 1962;//right_left_point_cnt[15]=0;down_up_point_cnt[15]=0;awb_block[15]=32;	//for vcs2b
            awb_r[16] = 1308; awb_b[16] = 1965;//right_left_point_cnt[16]=0;down_up_point_cnt[16]=0;awb_block[16]=32;	//for vcs2b
            awb_r[17] = 1312; awb_b[17] = 1961;//right_left_point_cnt[17]=0;down_up_point_cnt[17]=0;awb_block[17]=32;	//for vcs2b
            awb_r[18] = 1301; awb_b[18] = 1959;//right_left_point_cnt[18]=0;down_up_point_cnt[18]=0;awb_block[18]=32;	//for vcs2b
            awb_r[19] = 1298; awb_b[19] = 1953;//right_left_point_cnt[19]=0;down_up_point_cnt[19]=0;awb_block[19]=32;	//for vcs2b
            awb_r[20] = 1294; awb_b[20] = 1957;//right_left_point_cnt[20]=0;down_up_point_cnt[20]=0;awb_block[20]=32;	//for vcs2b
            awb_r[21] = 1295; awb_b[21] = 1951;//right_left_point_cnt[21]=0;down_up_point_cnt[21]=0;awb_block[21]=32;	//for vcs2b
            awb_r[22] = 1292; awb_b[22] = 1947;//right_left_point_cnt[22]=0;down_up_point_cnt[22]=0;awb_block[22]=32;	//for vcs2b
            awb_r[23] = 1292; awb_b[23] = 1940;//right_left_point_cnt[23]=0;down_up_point_cnt[23]=0;awb_block[23]=32;	//for vcs2b
            awb_r[24] = 1291; awb_b[24] = 1943;//right_left_point_cnt[24]=0;down_up_point_cnt[24]=0;awb_block[24]=32;	//for vcs2b
            awb_r[25] = 1293; awb_b[25] = 1937;//right_left_point_cnt[25]=0;down_up_point_cnt[25]=0;awb_block[25]=32;	//for vcs2b
            awb_r[26] = 1293; awb_b[26] = 1948;//right_left_point_cnt[26]=0;down_up_point_cnt[26]=0;awb_block[26]=32;	//for vcs2b
            awb_r[27] = 1289; awb_b[27] = 1954;//right_left_point_cnt[27]=0;down_up_point_cnt[27]=0;awb_block[27]=32;	//for vcs2b
            awb_r[28] = 1290; awb_b[28] = 1958;//right_left_point_cnt[28]=0;down_up_point_cnt[28]=0;awb_block[28]=32;	//for vcs2b
            awb_r[29] = 1291; awb_b[29] = 1972;//right_left_point_cnt[29]=0;down_up_point_cnt[29]=0;awb_block[29]=32;	//for vcs2b
            awb_r[30] = 1306; awb_b[30] = 1959;//right_left_point_cnt[30]=0;down_up_point_cnt[30]=0;awb_block[30]=32;	//for vcs2b
            awb_r[31] = 1310; awb_b[31] = 1960;//right_left_point_cnt[31]=0;down_up_point_cnt[31]=0;awb_block[31]=32;	//for vcs2b
            awb_r[32] = 1302; awb_b[32] = 1960;//right_left_point_cnt[32]=0;down_up_point_cnt[32]=0;awb_block[32]=32;	//for vcs2b
            awb_r[33] = 1298; awb_b[33] = 1896;//right_left_point_cnt[33]=0;down_up_point_cnt[33]=0;awb_block[33]=32;	//for vcs2b
            awb_r[34] = 1298; awb_b[34] = 1957;//right_left_point_cnt[34]=0;down_up_point_cnt[34]=0;awb_block[34]=32;	//for vcs2b
            awb_r[35] = 1295; awb_b[35] = 1951;//right_left_point_cnt[35]=0;down_up_point_cnt[35]=0;awb_block[35]=32;	//for vcs2b
            awb_r[36] = 1302; awb_b[36] = 1953;//right_left_point_cnt[36]=0;down_up_point_cnt[36]=0;awb_block[36]=32;	//for vcs2b
            awb_r[37] = 1296; awb_b[37] = 1942;//right_left_point_cnt[37]=0;down_up_point_cnt[37]=0;awb_block[37]=32;	//for vcs2b
            awb_r[38] = 1294; awb_b[38] = 1934;//right_left_point_cnt[38]=0;down_up_point_cnt[38]=0;awb_block[38]=32;	//for vcs2b
            awb_r[39] = 1293; awb_b[39] = 1935;//right_left_point_cnt[39]=0;down_up_point_cnt[39]=0;awb_block[39]=32;	//for vcs2b
            awb_r[40] = 1293; awb_b[40] = 1935;//right_left_point_cnt[40]=0;down_up_point_cnt[40]=0;awb_block[40]=32;	//for vcs2b
            awb_r[41] = 1280; awb_b[41] = 1896;//right_left_point_cnt[41]=0;down_up_point_cnt[41]=0;awb_block[41]=32;	//for vcs2b
            awb_r[42] = 1286; awb_b[42] = 1952;//right_left_point_cnt[42]=0;down_up_point_cnt[42]=0;awb_block[42]=32;	//for vcs2b
            awb_r[43] = 1290; awb_b[43] = 1952;//right_left_point_cnt[43]=0;down_up_point_cnt[43]=0;awb_block[43]=32;	//for vcs2b
            awb_r[44] = 1288; awb_b[44] = 1963;//right_left_point_cnt[44]=0;down_up_point_cnt[44]=0;awb_block[44]=32;	//for vcs2b
            awb_r[45] = 1312; awb_b[45] = 1953;//right_left_point_cnt[45]=0;down_up_point_cnt[45]=0;awb_block[45]=32;	//for vcs2b
            awb_r[46] = 1298; awb_b[46] = 1953;//right_left_point_cnt[46]=0;down_up_point_cnt[46]=0;awb_block[46]=32;	//for vcs2b
            awb_r[47] = 1298; awb_b[47] = 1954;//right_left_point_cnt[47]=0;down_up_point_cnt[47]=0;awb_block[47]=32;	//for vcs2b
            awb_r[48] = 1300; awb_b[48] = 1965;//right_left_point_cnt[48]=0;down_up_point_cnt[48]=0;awb_block[48]=32;	//for vcs2b
            awb_r[49] = 1300; awb_b[49] = 1954;//right_left_point_cnt[49]=0;down_up_point_cnt[49]=0;awb_block[49]=32;	//for vcs2b
            awb_r[50] = 1301; awb_b[50] = 1950;//right_left_point_cnt[50]=0;down_up_point_cnt[50]=0;awb_block[50]=32;	//for vcs2b
            awb_r[51] = 1308; awb_b[51] = 1949;//right_left_point_cnt[51]=0;down_up_point_cnt[51]=0;awb_block[51]=32;	//for vcs2b
            awb_r[52] = 1301; awb_b[52] = 1925;//right_left_point_cnt[52]=0;down_up_point_cnt[52]=0;awb_block[52]=32;	//for vcs2b
            awb_r[53] = 1291; awb_b[53] = 1927;//right_left_point_cnt[53]=0;down_up_point_cnt[53]=0;awb_block[53]=32;	//for vcs2b
            awb_r[54] = 1285; awb_b[54] = 1928;//right_left_point_cnt[54]=0;down_up_point_cnt[54]=0;awb_block[54]=32;	//for vcs2b
            awb_r[55] = 1280; awb_b[55] = 1925;//right_left_point_cnt[55]=0;down_up_point_cnt[55]=0;awb_block[55]=32;	//for vcs2b
            awb_r[56] = 1294; awb_b[56] = 1934;//right_left_point_cnt[56]=0;down_up_point_cnt[56]=0;awb_block[56]=32;	//for vcs2b
            awb_r[57] = 1280; awb_b[57] = 1896;//right_left_point_cnt[57]=0;down_up_point_cnt[57]=0;awb_block[57]=32;	//for vcs2b
            awb_r[58] = 1291; awb_b[58] = 1955;//right_left_point_cnt[58]=0;down_up_point_cnt[58]=0;awb_block[58]=32;	//for vcs2b
            awb_r[59] = 1287; awb_b[59] = 1956;//right_left_point_cnt[59]=0;down_up_point_cnt[59]=0;awb_block[59]=32;	//for vcs2b
            awb_r[60] = 1308; awb_b[60] = 1947;//right_left_point_cnt[60]=0;down_up_point_cnt[60]=0;awb_block[60]=32;	//for vcs2b
            awb_r[61] = 1296; awb_b[61] = 1946;//right_left_point_cnt[61]=0;down_up_point_cnt[61]=0;awb_block[61]=32;	//for vcs2b
            awb_r[62] = 1303; awb_b[62] = 1969;//right_left_point_cnt[62]=0;down_up_point_cnt[62]=0;awb_block[62]=32;	//for vcs2b
            awb_r[63] = 1301; awb_b[63] = 1953;//right_left_point_cnt[63]=0;down_up_point_cnt[63]=0;awb_block[63]=32;	//for vcs2b
            awb_r[64] = 1302; awb_b[64] = 1947;//right_left_point_cnt[64]=0;down_up_point_cnt[64]=0;awb_block[64]=32;	//for vcs2b
            awb_r[65] = 1308; awb_b[65] = 1946;//right_left_point_cnt[65]=0;down_up_point_cnt[65]=0;awb_block[65]=32;	//for vcs2b
            awb_r[66] = 1308; awb_b[66] = 1896;//right_left_point_cnt[66]=0;down_up_point_cnt[66]=0;awb_block[66]=32;	//for vcs2b
            awb_r[67] = 1297; awb_b[67] = 1928;//right_left_point_cnt[67]=0;down_up_point_cnt[67]=0;awb_block[67]=32;	//for vcs2b
            awb_r[68] = 1287; awb_b[68] = 1925;//right_left_point_cnt[68]=0;down_up_point_cnt[68]=0;awb_block[68]=32;	//for vcs2b
            awb_r[69] = 1286; awb_b[69] = 1924;//right_left_point_cnt[69]=0;down_up_point_cnt[69]=0;awb_block[69]=32;	//for vcs2b
            awb_r[70] = 1231; awb_b[70] = 1930;//right_left_point_cnt[70]=0;down_up_point_cnt[70]=0;awb_block[70]=32;	//for vcs2b
            awb_r[71] = 1227; awb_b[71] = 1925;//right_left_point_cnt[71]=0;down_up_point_cnt[71]=0;awb_block[71]=32;	//for vcs2b
            awb_r[72] = 1227; awb_b[72] = 1939;//right_left_point_cnt[72]=0;down_up_point_cnt[72]=0;awb_block[72]=32;	//for vcs2b
            awb_r[73] = 1228; awb_b[73] = 1935;//right_left_point_cnt[73]=0;down_up_point_cnt[73]=0;awb_block[73]=32;	//for vcs2b
            awb_r[74] = 1242; awb_b[74] = 1896;//right_left_point_cnt[74]=0;down_up_point_cnt[74]=0;awb_block[74]=32;	//for vcs2b
            awb_r[75] = 1249; awb_b[75] = 1934;//right_left_point_cnt[75]=0;down_up_point_cnt[75]=0;awb_block[75]=32;	//for vcs2b
            awb_r[76] = 1250; awb_b[76] = 1942;//right_left_point_cnt[76]=0;down_up_point_cnt[76]=0;awb_block[76]=32;	//for vcs2b
            awb_r[77] = 1254; awb_b[77] = 1942;//right_left_point_cnt[77]=0;down_up_point_cnt[77]=0;awb_block[77]=32;	//for vcs2b
            awb_r[78] = 1253; awb_b[78] = 1946;//right_left_point_cnt[78]=0;down_up_point_cnt[78]=0;awb_block[78]=32;	//for vcs2b
            awb_r[79] = 1249; awb_b[79] = 1940;//right_left_point_cnt[79]=0;down_up_point_cnt[79]=0;awb_block[79]=32;	//for vcs2b
            awb_r[80] = 1248; awb_b[80] = 1931;//right_left_point_cnt[80]=0;down_up_point_cnt[80]=0;awb_block[80]=32;	//for vcs2b
            awb_r[81] = 1249; awb_b[81] = 1931;//right_left_point_cnt[81]=0;down_up_point_cnt[81]=0;awb_block[81]=32;	//for vcs2b
            awb_r[82] = 1243; awb_b[82] = 1929;//right_left_point_cnt[82]=0;down_up_point_cnt[82]=0;awb_block[82]=32;	//for vcs2b
            awb_r[83] = 1235; awb_b[83] = 1917;//right_left_point_cnt[83]=0;down_up_point_cnt[83]=0;awb_block[83]=32;	//for vcs2b
            awb_r[84] = 1235; awb_b[84] = 1926;//right_left_point_cnt[84]=0;down_up_point_cnt[84]=0;awb_block[84]=32;	//for vcs2b
            awb_r[85] = 1231; awb_b[85] = 1923;//right_left_point_cnt[85]=0;down_up_point_cnt[85]=0;awb_block[85]=32;	//for vcs2b
            awb_r[86] = 1226; awb_b[86] = 1935;//right_left_point_cnt[86]=0;down_up_point_cnt[86]=0;awb_block[86]=32;	//for vcs2b
            awb_r[87] = 1223; awb_b[87] = 1938;//right_left_point_cnt[87]=0;down_up_point_cnt[87]=0;awb_block[87]=32;	//for vcs2b
            awb_r[88] = 1222; awb_b[88] = 1935;//right_left_point_cnt[88]=0;down_up_point_cnt[88]=0;awb_block[88]=32;	//for vcs2b
            awb_r[89] = 1230; awb_b[89] = 1937;//right_left_point_cnt[89]=0;down_up_point_cnt[89]=0;awb_block[89]=32;	//for vcs2b
            awb_r[90] = 1251; awb_b[90] = 1932;//right_left_point_cnt[90]=0;down_up_point_cnt[90]=0;awb_block[90]=32;	//for vcs2b
            awb_r[91] = 1255; awb_b[91] = 1940;//right_left_point_cnt[91]=0;down_up_point_cnt[91]=0;awb_block[91]=32;	//for vcs2b
            awb_r[92] = 1252; awb_b[92] = 1940;//right_left_point_cnt[92]=0;down_up_point_cnt[92]=0;awb_block[92]=32;	//for vcs2b
            awb_r[93] = 1251; awb_b[93] = 1934;//right_left_point_cnt[93]=0;down_up_point_cnt[93]=0;awb_block[93]=32;	//for vcs2b
            awb_r[94] = 1249; awb_b[94] = 1936;//right_left_point_cnt[94]=0;down_up_point_cnt[94]=0;awb_block[94]=32;	//for vcs2b
            awb_r[95] = 1247; awb_b[95] = 1925;//right_left_point_cnt[95]=0;down_up_point_cnt[95]=0;awb_block[95]=32;	//for vcs2b
            awb_r[96] = 1244; awb_b[96] = 1919;//right_left_point_cnt[96]=0;down_up_point_cnt[96]=0;awb_block[96]=32;	//for vcs2b
            awb_r[97] = 1241; awb_b[97] = 1923;//right_left_point_cnt[97]=0;down_up_point_cnt[97]=0;awb_block[97]=32;	//for vcs2b
            awb_r[98] = 1236; awb_b[98] = 1917;//right_left_point_cnt[98]=0;down_up_point_cnt[98]=0;awb_block[98]=32;	//for vcs2b
            awb_r[99] = 1235; awb_b[99] = 1924;//right_left_point_cnt[99]=0;down_up_point_cnt[99]=0;awb_block[99]=32;	//for vcs2b
            awb_r[100] = 1228; awb_b[100] = 1936;//right_left_point_cnt[100]=0;down_up_point_cnt[100]=0;awb_block[100]=32;	//for vcs2b
            awb_r[101] = 1223; awb_b[101] = 1932;//right_left_point_cnt[101]=0;down_up_point_cnt[101]=0;awb_block[101]=32;	//for vcs2b
            awb_r[102] = 1223; awb_b[102] = 1941;//right_left_point_cnt[102]=0;down_up_point_cnt[102]=0;awb_block[102]=32;	//for vcs2b
            awb_r[103] = 1224; awb_b[103] = 1931;//right_left_point_cnt[103]=0;down_up_point_cnt[103]=0;awb_block[103]=32;	//for vcs2b
            awb_r[104] = 1229; awb_b[104] = 1937;//right_left_point_cnt[104]=0;down_up_point_cnt[104]=0;awb_block[104]=32;	//for vcs2b
            awb_r[105] = 1251; awb_b[105] = 1930;//right_left_point_cnt[105]=0;down_up_point_cnt[105]=0;awb_block[105]=32;	//for vcs2b
            awb_r[106] = 1256; awb_b[106] = 1935;//right_left_point_cnt[106]=0;down_up_point_cnt[106]=0;awb_block[106]=32;	//for vcs2b
            awb_r[107] = 1254; awb_b[107] = 1935;//right_left_point_cnt[107]=0;down_up_point_cnt[107]=0;awb_block[107]=32;	//for vcs2b
            awb_r[108] = 1249; awb_b[108] = 1932;//right_left_point_cnt[108]=0;down_up_point_cnt[108]=0;awb_block[108]=32;	//for vcs2b
            awb_r[109] = 1249; awb_b[109] = 1925;//right_left_point_cnt[109]=0;down_up_point_cnt[109]=0;awb_block[109]=32;	//for vcs2b
            awb_r[110] = 1243; awb_b[110] = 1914;//right_left_point_cnt[110]=0;down_up_point_cnt[110]=0;awb_block[110]=32;	//for vcs2b
            awb_r[111] = 1251; awb_b[111] = 1896;//right_left_point_cnt[111]=0;down_up_point_cnt[111]=0;awb_block[111]=32;	//for vcs2b
            awb_r[112] = 1240; awb_b[112] = 1915;//right_left_point_cnt[112]=0;down_up_point_cnt[112]=0;awb_block[112]=32;	//for vcs2b
            awb_r[113] = 1242; awb_b[113] = 1926;//right_left_point_cnt[113]=0;down_up_point_cnt[113]=0;awb_block[113]=32;	//for vcs2b
            awb_r[114] = 1238; awb_b[114] = 1936;//right_left_point_cnt[114]=0;down_up_point_cnt[114]=0;awb_block[114]=32;	//for vcs2b
            awb_r[115] = 1229; awb_b[115] = 1940;//right_left_point_cnt[115]=0;down_up_point_cnt[115]=0;awb_block[115]=32;	//for vcs2b
            awb_r[116] = 1225; awb_b[116] = 1930;//right_left_point_cnt[116]=0;down_up_point_cnt[116]=0;awb_block[116]=32;	//for vcs2b
            awb_r[117] = 1223; awb_b[117] = 1933;//right_left_point_cnt[117]=0;down_up_point_cnt[117]=0;awb_block[117]=32;	//for vcs2b
            awb_r[118] = 1225; awb_b[118] = 1934;//right_left_point_cnt[118]=0;down_up_point_cnt[118]=0;awb_block[118]=32;	//for vcs2b
            awb_r[119] = 1230; awb_b[119] = 1931;//right_left_point_cnt[119]=0;down_up_point_cnt[119]=0;awb_block[119]=32;	//for vcs2b
            awb_r[120] = 1256; awb_b[120] = 1940;//right_left_point_cnt[120]=0;down_up_point_cnt[120]=0;awb_block[120]=32;	//for vcs2b
            awb_r[121] = 1256; awb_b[121] = 1935;//right_left_point_cnt[121]=0;down_up_point_cnt[121]=0;awb_block[121]=32;	//for vcs2b
            awb_r[122] = 1252; awb_b[122] = 1934;//right_left_point_cnt[122]=0;down_up_point_cnt[122]=0;awb_block[122]=32;	//for vcs2b
            awb_r[123] = 1249; awb_b[123] = 1931;//right_left_point_cnt[123]=0;down_up_point_cnt[123]=0;awb_block[123]=32;	//for vcs2b
            awb_r[124] = 1254; awb_b[124] = 1930;//right_left_point_cnt[124]=0;down_up_point_cnt[124]=0;awb_block[124]=32;	//for vcs2b
            awb_r[125] = 1248; awb_b[125] = 1896;//right_left_point_cnt[125]=0;down_up_point_cnt[125]=0;awb_block[125]=32;	//for vcs2b
            awb_r[126] = 1249; awb_b[126] = 1925;//right_left_point_cnt[126]=0;down_up_point_cnt[126]=0;awb_block[126]=32;	//for vcs2b
            awb_r[127] = 1238; awb_b[127] = 1913;//right_left_point_cnt[127]=0;down_up_point_cnt[127]=0;awb_block[127]=32;	//for vcs2b
            awb_r[128] = 1239; awb_b[128] = 1922;//right_left_point_cnt[128]=0;down_up_point_cnt[128]=0;awb_block[128]=32;	//for vcs2b
            awb_r[129] = 1236; awb_b[129] = 1925;//right_left_point_cnt[129]=0;down_up_point_cnt[129]=0;awb_block[129]=32;	//for vcs2b
            awb_r[130] = 1229; awb_b[130] = 1933;//right_left_point_cnt[130]=0;down_up_point_cnt[130]=0;awb_block[130]=32;	//for vcs2b
            awb_r[131] = 1227; awb_b[131] = 1936;//right_left_point_cnt[131]=0;down_up_point_cnt[131]=0;awb_block[131]=32;	//for vcs2b
            awb_r[132] = 1228; awb_b[132] = 1928;//right_left_point_cnt[132]=0;down_up_point_cnt[132]=0;awb_block[132]=32;	//for vcs2b
            awb_r[133] = 1231; awb_b[133] = 1930;//right_left_point_cnt[133]=0;down_up_point_cnt[133]=0;awb_block[133]=32;	//for vcs2b
            awb_r[134] = 1232; awb_b[134] = 1929;//right_left_point_cnt[134]=0;down_up_point_cnt[134]=0;awb_block[134]=32;	//for vcs2b
            awb_r[135] = 1257; awb_b[135] = 1935;//right_left_point_cnt[135]=0;down_up_point_cnt[135]=0;awb_block[135]=32;	//for vcs2b
            awb_r[136] = 1254; awb_b[136] = 1932;//right_left_point_cnt[136]=0;down_up_point_cnt[136]=0;awb_block[136]=32;	//for vcs2b
            awb_r[137] = 1251; awb_b[137] = 1933;//right_left_point_cnt[137]=0;down_up_point_cnt[137]=0;awb_block[137]=32;	//for vcs2b
            awb_r[138] = 1249; awb_b[138] = 1896;//right_left_point_cnt[138]=0;down_up_point_cnt[138]=0;awb_block[138]=32;	//for vcs2b
            awb_r[139] = 1249; awb_b[139] = 1924;//right_left_point_cnt[139]=0;down_up_point_cnt[139]=0;awb_block[139]=32;	//for vcs2b
            awb_r[140] = 1249; awb_b[140] = 1925;//right_left_point_cnt[140]=0;down_up_point_cnt[140]=0;awb_block[140]=32;	//for vcs2b
            awb_r[141] = 1245; awb_b[141] = 1926;//right_left_point_cnt[141]=0;down_up_point_cnt[141]=0;awb_block[141]=32;	//for vcs2b
            awb_r[142] = 1243; awb_b[142] = 1917;//right_left_point_cnt[142]=0;down_up_point_cnt[142]=0;awb_block[142]=32;	//for vcs2b
            awb_r[143] = 1240; awb_b[143] = 1923;//right_left_point_cnt[143]=0;down_up_point_cnt[143]=0;awb_block[143]=32;	//for vcs2b
            awb_r[144] = 1237; awb_b[144] = 1916;//right_left_point_cnt[144]=0;down_up_point_cnt[144]=0;awb_block[144]=32;	//for vcs2b
            awb_r[145] = 1238; awb_b[145] = 1933;//right_left_point_cnt[145]=0;down_up_point_cnt[145]=0;awb_block[145]=32;	//for vcs2b
            awb_r[146] = 1239; awb_b[146] = 1931;//right_left_point_cnt[146]=0;down_up_point_cnt[146]=0;awb_block[146]=32;	//for vcs2b
            awb_r[147] = 1239; awb_b[147] = 1930;//right_left_point_cnt[147]=0;down_up_point_cnt[147]=0;awb_block[147]=32;	//for vcs2b
            awb_r[148] = 1234; awb_b[148] = 1936;//right_left_point_cnt[148]=0;down_up_point_cnt[148]=0;awb_block[148]=32;	//for vcs2b
            awb_r[149] = 1233; awb_b[149] = 1925;//right_left_point_cnt[149]=0;down_up_point_cnt[149]=0;awb_block[149]=32;	//for vcs2b
            awb_r[150] = 1257; awb_b[150] = 1953;//right_left_point_cnt[150]=0;down_up_point_cnt[150]=0;awb_block[150]=32;	//for vcs2b
            awb_r[151] = 1253; awb_b[151] = 1942;//right_left_point_cnt[151]=0;down_up_point_cnt[151]=0;awb_block[151]=32;	//for vcs2b
            awb_r[152] = 1253; awb_b[152] = 1940;//right_left_point_cnt[152]=0;down_up_point_cnt[152]=0;awb_block[152]=32;	//for vcs2b
            awb_r[153] = 1249; awb_b[153] = 1946;//right_left_point_cnt[153]=0;down_up_point_cnt[153]=0;awb_block[153]=32;	//for vcs2b
            awb_r[154] = 1250; awb_b[154] = 1921;//right_left_point_cnt[154]=0;down_up_point_cnt[154]=0;awb_block[154]=32;	//for vcs2b
            awb_r[155] = 1247; awb_b[155] = 1919;//right_left_point_cnt[155]=0;down_up_point_cnt[155]=0;awb_block[155]=32;	//for vcs2b
            awb_r[156] = 1251; awb_b[156] = 1918;//right_left_point_cnt[156]=0;down_up_point_cnt[156]=0;awb_block[156]=32;	//for vcs2b
            awb_r[157] = 1242; awb_b[157] = 1912;//right_left_point_cnt[157]=0;down_up_point_cnt[157]=0;awb_block[157]=32;	//for vcs2b
            awb_r[158] = 1244; awb_b[158] = 1927;//right_left_point_cnt[158]=0;down_up_point_cnt[158]=0;awb_block[158]=32;	//for vcs2b
            awb_r[159] = 1239; awb_b[159] = 1916;//right_left_point_cnt[159]=0;down_up_point_cnt[159]=0;awb_block[159]=32;	//for vcs2b
            awb_r[160] = 1243; awb_b[160] = 1931;//right_left_point_cnt[160]=0;down_up_point_cnt[160]=0;awb_block[160]=32;	//for vcs2b
            awb_r[161] = 1242; awb_b[161] = 1925;//right_left_point_cnt[161]=0;down_up_point_cnt[161]=0;awb_block[161]=32;	//for vcs2b
            awb_r[162] = 1242; awb_b[162] = 1937;//right_left_point_cnt[162]=0;down_up_point_cnt[162]=0;awb_block[162]=32;	//for vcs2b
            awb_r[163] = 1236; awb_b[163] = 1925;//right_left_point_cnt[163]=0;down_up_point_cnt[163]=0;awb_block[163]=32;	//for vcs2b
            awb_r[164] = 1236; awb_b[164] = 1931;//right_left_point_cnt[164]=0;down_up_point_cnt[164]=0;awb_block[164]=32;	//for vcs2b
            awb_r[165] = 1256; awb_b[165] = 1941;//right_left_point_cnt[165]=0;down_up_point_cnt[165]=0;awb_block[165]=32;	//for vcs2b
            awb_r[166] = 1249; awb_b[166] = 1896;//right_left_point_cnt[166]=0;down_up_point_cnt[166]=0;awb_block[166]=32;	//for vcs2b
            awb_r[167] = 1247; awb_b[167] = 1896;//right_left_point_cnt[167]=0;down_up_point_cnt[167]=0;awb_block[167]=32;	//for vcs2b
            awb_r[168] = 1249; awb_b[168] = 1945;//right_left_point_cnt[168]=0;down_up_point_cnt[168]=0;awb_block[168]=32;	//for vcs2b
            awb_r[169] = 1249; awb_b[169] = 1924;//right_left_point_cnt[169]=0;down_up_point_cnt[169]=0;awb_block[169]=32;	//for vcs2b
            awb_r[170] = 1248; awb_b[170] = 1919;//right_left_point_cnt[170]=0;down_up_point_cnt[170]=0;awb_block[170]=32;	//for vcs2b
            awb_r[171] = 1251; awb_b[171] = 1925;//right_left_point_cnt[171]=0;down_up_point_cnt[171]=0;awb_block[171]=32;	//for vcs2b
            awb_r[172] = 1248; awb_b[172] = 1919;//right_left_point_cnt[172]=0;down_up_point_cnt[172]=0;awb_block[172]=32;	//for vcs2b
            awb_r[173] = 1243; awb_b[173] = 1913;//right_left_point_cnt[173]=0;down_up_point_cnt[173]=0;awb_block[173]=32;	//for vcs2b
            awb_r[174] = 1246; awb_b[174] = 1925;//right_left_point_cnt[174]=0;down_up_point_cnt[174]=0;awb_block[174]=32;	//for vcs2b
            awb_r[175] = 1242; awb_b[175] = 1919;//right_left_point_cnt[175]=0;down_up_point_cnt[175]=0;awb_block[175]=32;	//for vcs2b
            awb_r[176] = 1246; awb_b[176] = 1932;//right_left_point_cnt[176]=0;down_up_point_cnt[176]=0;awb_block[176]=32;	//for vcs2b
            awb_r[177] = 1243; awb_b[177] = 1927;//right_left_point_cnt[177]=0;down_up_point_cnt[177]=0;awb_block[177]=32;	//for vcs2b
            awb_r[178] = 1244; awb_b[178] = 1948;//right_left_point_cnt[178]=0;down_up_point_cnt[178]=0;awb_block[178]=32;	//for vcs2b
            awb_r[179] = 1243; awb_b[179] = 1896;//right_left_point_cnt[179]=0;down_up_point_cnt[179]=0;awb_block[179]=32;	//for vcs2b
            awb_r[180] = 1254; awb_b[180] = 1968;//right_left_point_cnt[180]=0;down_up_point_cnt[180]=0;awb_block[180]=32;	//for vcs2b
            awb_r[181] = 1250; awb_b[181] = 1963;//right_left_point_cnt[181]=0;down_up_point_cnt[181]=0;awb_block[181]=32;	//for vcs2b
            awb_r[182] = 1251; awb_b[182] = 1896;//right_left_point_cnt[182]=0;down_up_point_cnt[182]=0;awb_block[182]=32;	//for vcs2b
            awb_r[183] = 1248; awb_b[183] = 1935;//right_left_point_cnt[183]=0;down_up_point_cnt[183]=0;awb_block[183]=32;	//for vcs2b
            awb_r[184] = 1246; awb_b[184] = 1924;//right_left_point_cnt[184]=0;down_up_point_cnt[184]=0;awb_block[184]=32;	//for vcs2b
            awb_r[185] = 1246; awb_b[185] = 1915;//right_left_point_cnt[185]=0;down_up_point_cnt[185]=0;awb_block[185]=32;	//for vcs2b
            awb_r[186] = 1249; awb_b[186] = 1920;//right_left_point_cnt[186]=0;down_up_point_cnt[186]=0;awb_block[186]=32;	//for vcs2b
            awb_r[187] = 1249; awb_b[187] = 1913;//right_left_point_cnt[187]=0;down_up_point_cnt[187]=0;awb_block[187]=32;	//for vcs2b
            awb_r[188] = 1249; awb_b[188] = 1917;//right_left_point_cnt[188]=0;down_up_point_cnt[188]=0;awb_block[188]=32;	//for vcs2b
            awb_r[189] = 1249; awb_b[189] = 1930;//right_left_point_cnt[189]=0;down_up_point_cnt[189]=0;awb_block[189]=32;	//for vcs2b
            awb_r[190] = 1250; awb_b[190] = 1924;//right_left_point_cnt[190]=0;down_up_point_cnt[190]=0;awb_block[190]=32;	//for vcs2b
            awb_r[191] = 1254; awb_b[191] = 1896;//right_left_point_cnt[191]=0;down_up_point_cnt[191]=0;awb_block[191]=32;	//for vcs2b
            awb_r[192] = 1245; awb_b[192] = 1931;//right_left_point_cnt[192]=0;down_up_point_cnt[192]=0;awb_block[192]=32;	//for vcs2b
            awb_r[193] = 1243; awb_b[193] = 1932;//right_left_point_cnt[193]=0;down_up_point_cnt[193]=0;awb_block[193]=32;	//for vcs2b
            awb_r[194] = 1242; awb_b[194] = 1938;//right_left_point_cnt[194]=0;down_up_point_cnt[194]=0;awb_block[194]=32;	//for vcs2b
            awb_r[195] = 1251; awb_b[195] = 1960;//right_left_point_cnt[195]=0;down_up_point_cnt[195]=0;awb_block[195]=32;	//for vcs2b
            awb_r[196] = 1253; awb_b[196] = 1896;//right_left_point_cnt[196]=0;down_up_point_cnt[196]=0;awb_block[196]=32;	//for vcs2b
            awb_r[197] = 1251; awb_b[197] = 1959;//right_left_point_cnt[197]=0;down_up_point_cnt[197]=0;awb_block[197]=32;	//for vcs2b
            awb_r[198] = 1248; awb_b[198] = 1947;//right_left_point_cnt[198]=0;down_up_point_cnt[198]=0;awb_block[198]=32;	//for vcs2b
            awb_r[199] = 1245; awb_b[199] = 1931;//right_left_point_cnt[199]=0;down_up_point_cnt[199]=0;awb_block[199]=32;	//for vcs2b
            awb_r[200] = 1244; awb_b[200] = 1927;//right_left_point_cnt[200]=0;down_up_point_cnt[200]=0;awb_block[200]=32;	//for vcs2b
            awb_r[201] = 1251; awb_b[201] = 1919;//right_left_point_cnt[201]=0;down_up_point_cnt[201]=0;awb_block[201]=32;	//for vcs2b
            awb_r[202] = 1253; awb_b[202] = 1918;//right_left_point_cnt[202]=0;down_up_point_cnt[202]=0;awb_block[202]=32;	//for vcs2b
            awb_r[203] = 1248; awb_b[203] = 1928;//right_left_point_cnt[203]=0;down_up_point_cnt[203]=0;awb_block[203]=32;	//for vcs2b
            awb_r[204] = 1255; awb_b[204] = 1920;//right_left_point_cnt[204]=0;down_up_point_cnt[204]=0;awb_block[204]=32;	//for vcs2b
            awb_r[205] = 1250; awb_b[205] = 1928;//right_left_point_cnt[205]=0;down_up_point_cnt[205]=0;awb_block[205]=32;	//for vcs2b
            awb_r[206] = 1252; awb_b[206] = 1932;//right_left_point_cnt[206]=0;down_up_point_cnt[206]=0;awb_block[206]=32;	//for vcs2b
            awb_r[207] = 1245; awb_b[207] = 1935;//right_left_point_cnt[207]=0;down_up_point_cnt[207]=0;awb_block[207]=32;	//for vcs2b
            awb_r[208] = 1247; awb_b[208] = 1945;//right_left_point_cnt[208]=0;down_up_point_cnt[208]=0;awb_block[208]=32;	//for vcs2b
            awb_r[209] = 1244; awb_b[209] = 1949;//right_left_point_cnt[209]=0;down_up_point_cnt[209]=0;awb_block[209]=32;	//for vcs2b
            awb_r[210] = 1249; awb_b[210] = 1962;//right_left_point_cnt[210]=0;down_up_point_cnt[210]=0;awb_block[210]=32;	//for vcs2b
            awb_r[211] = 1247; awb_b[211] = 1973;//right_left_point_cnt[211]=0;down_up_point_cnt[211]=0;awb_block[211]=32;	//for vcs2b
            awb_r[212] = 1252; awb_b[212] = 1952;//right_left_point_cnt[212]=0;down_up_point_cnt[212]=0;awb_block[212]=32;	//for vcs2b
            awb_r[213] = 1253; awb_b[213] = 1954;//right_left_point_cnt[213]=0;down_up_point_cnt[213]=0;awb_block[213]=32;	//for vcs2b
            awb_r[214] = 1252; awb_b[214] = 1940;//right_left_point_cnt[214]=0;down_up_point_cnt[214]=0;awb_block[214]=32;	//for vcs2b
            awb_r[215] = 1249; awb_b[215] = 1933;//right_left_point_cnt[215]=0;down_up_point_cnt[215]=0;awb_block[215]=32;	//for vcs2b
            awb_r[216] = 1250; awb_b[216] = 1896;//right_left_point_cnt[216]=0;down_up_point_cnt[216]=0;awb_block[216]=32;	//for vcs2b
            awb_r[217] = 1255; awb_b[217] = 1922;//right_left_point_cnt[217]=0;down_up_point_cnt[217]=0;awb_block[217]=32;	//for vcs2b
            awb_r[218] = 1248; awb_b[218] = 1926;//right_left_point_cnt[218]=0;down_up_point_cnt[218]=0;awb_block[218]=32;	//for vcs2b
            awb_r[219] = 1248; awb_b[219] = 1933;//right_left_point_cnt[219]=0;down_up_point_cnt[219]=0;awb_block[219]=32;	//for vcs2b
            awb_r[220] = 1253; awb_b[220] = 1931;//right_left_point_cnt[220]=0;down_up_point_cnt[220]=0;awb_block[220]=32;	//for vcs2b
            awb_r[221] = 1248; awb_b[221] = 1930;//right_left_point_cnt[221]=0;down_up_point_cnt[221]=0;awb_block[221]=32;	//for vcs2b
            awb_r[222] = 1249; awb_b[222] = 1941;//right_left_point_cnt[222]=0;down_up_point_cnt[222]=0;awb_block[222]=32;	//for vcs2b
            awb_r[223] = 1245; awb_b[223] = 1948;//right_left_point_cnt[223]=0;down_up_point_cnt[223]=0;awb_block[223]=32;	//for vcs2b
            awb_r[224] = 1247; awb_b[224] = 1896;//right_left_point_cnt[224]=0;down_up_point_cnt[224]=0;awb_block[224]=32;	//for vcs2b

            g.Clear(Color.White);
            int[,] gray = new int[15, 15];

            for (i = 0; i < 225; i++)
            {
                gray[i % 15, i / 15] = awb_b[i];
            }

            for (j = 0; j < 15; j++)
            {
                for (i = 0; i < 15; i++)
                {
                    richTextBox1.Text += gray[i, j].ToString() + " ";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";

            int max = gray[0, 0];
            int min = gray[0, 0];
            int diff = 0;
            int center = gray[7, 7];
            double mean = 0;

            for (j = 0; j < 15; j++)
            {
                for (i = 0; i < 15; i++)
                {
                    if (max < gray[i, j])
                        max = gray[i, j];
                    if (min > gray[i, j])
                        min = gray[i, j];
                }
            }

            diff = max - min;
            mean = (max + min) / 2.0;

            richTextBox1.Text += "max = " + max.ToString() + "\n";
            richTextBox1.Text += "min = " + min.ToString() + "\n";
            richTextBox1.Text += "diff = " + diff.ToString() + "\n";
            richTextBox1.Text += "center = " + center.ToString() + "\n";
            richTextBox1.Text += "mean = " + mean.ToString() + "\n";

            /*
            //使用測試陣列
            max = 255;
            min = 0;
            gray = new int[15, 15];

            richTextBox1.Text += "assign value\n";
            for (j = 0; j < 15; j++)
            {
                for (i = 0; i < 15; i++)
                {
                    //gray[j, i] = j * 15 + i;
                    gray[j, i] = j * 10 + i * 0;
                    //gray[j, i] = i * 10;
                }
            }
            */

            int ROW = gray.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = gray.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int length = gray.Length;//獲取整個二維陣列的長度，即所有元 的個數
            richTextBox1.Text += "ROW = " + ROW.ToString() + "\n";
            richTextBox1.Text += "COL = " + COL.ToString() + "\n";
            richTextBox1.Text += "length = " + length.ToString() + "\n";

            richTextBox1.Text += "before\n";
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    richTextBox1.Text += (gray[j, i] - min).ToString("D3") + "  ";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";


            int k;
            int avg;
            int tap = 2;

            richTextBox1.Text += "smoothing...\ttap = " + tap.ToString() + "\n";

            //水平filter
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < (COL - (tap - 1)); i++)
                {
                    avg = 0;
                    for (k = 0; k < tap; k++)
                    {
                        avg += gray[j, i + k];
                    }
                    avg /= tap;

                    gray[j, i] = avg;
                }
            }

            //垂直filter
            for (j = 0; j < COL; j++)
            {
                for (i = 0; i < (ROW - (tap - 1)); i++)
                {
                    avg = 0;
                    for (k = 0; k < tap; k++)
                    {
                        avg += gray[i + k, j];
                        //richTextBox1.Text += "use " + gray[j, i + k].ToString() + " ";
                    }
                    avg /= tap;

                    gray[i, j] = avg;

                }
            }

            richTextBox1.Text += "after\n";
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    richTextBox1.Text += (gray[j, i] - min).ToString("D3") + "  ";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";


            double ratio = (double)255 / (max - min);

            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            int dd = 40;
            int xx;
            int yy;
            int width = 15 * dd;
            int height = 15 * dd;

            bitmap1 = new Bitmap(width, height);

            byte aa = 255;
            byte rr = 0;
            byte gg = 0;
            byte bb = 0;

            //ratio = 1;

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //Color p = Color.FromName("SlateBlue");
                    /*
                    Color p ;
                    p.A = (byte)(xx % 255);
                    p.R = (byte)(xx % 127 + 127);
                    p.G = (byte)(xx % 127);
                    p.B = (byte)(xx % 63);
                    */


                    //獲取像素的ＲＧＢ顏色值
                    //srcColor = srcBitmap.GetPixel(x, y);
                    //byte temp = (byte)(srcColor.R * .299 + srcColor.G * .587 + srcColor.B * .114);

                    //byte temp = (byte)((byte)(xx % 255) + (byte)(xx % 127 + 127) + (byte)(xx % 63));

                    //設置像素的ＲＧＢ顏色值
                    rr = (byte)((gray[xx / dd, yy / dd] - min) * ratio);
                    gg = (byte)((gray[xx / dd, yy / dd] - min) * ratio);
                    bb = (byte)((gray[xx / dd, yy / dd] - min) * ratio);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                    if (((xx % dd) == 0) && ((yy % dd) == 0))
                    {
                        richTextBox1.Text += rr.ToString("D3") + "  ";
                    }
                }
                //richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            pictureBox1.Image = bitmap1;


        }
    }
}

