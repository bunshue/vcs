using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for LineCap
using System.Drawing.Imaging;   //for ImageFormat

namespace _vcs_DrawTemplate
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();

            button2.Enabled = false;
            button3.Enabled = false;
            button4.Enabled = false;
            button5.Enabled = false;
            button7.Enabled = false;
            button8.Enabled = false;
            button9.Enabled = false;

            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            p = new Pen(Color.Red, 3);
            sb = new SolidBrush(Color.Red);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            button2.Enabled = true;
            button3.Enabled = true;
            button4.Enabled = true;
            button5.Enabled = true;
            button7.Enabled = true;
            button8.Enabled = true;
            button9.Enabled = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //載入圖片至畫布
            string filename = string.Empty;
            filename = "C:\\______test_files\\bear.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";
            bitmap1 = new Bitmap(filename);

            int width;
            int height;

            width = bitmap1.Width;
            height = bitmap1.Height;

            richTextBox1.Text += "畫布大小 : W = " + width.ToString() + " H = " + height.ToString() + "\n";

            //pictureBox1.Size = new Size(width, height);   //改變圖框大小
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.Image = bitmap1;

            g = Graphics.FromImage(bitmap1);

            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //畫東西
            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));
            g.DrawRectangle(new Pen(Color.Red, 5), new Rectangle(100, 100, 300, 300));

            int width = 200;
            int height = 200;
            Point[] points = new Point[3];
            points[0] = new Point(width / 2, height / 8);
            points[1] = new Point(width * 7 / 8, height * 7 / 8);
            points[2] = new Point(width * 1 / 8, height * 7 / 8);
            g.FillPolygon(sb, points);

            //畫箭頭
            Pen pen = new Pen(Color.FromArgb(255, 0, 0, 255), 8);
            pen.StartCap = LineCap.RoundAnchor;
            pen.EndCap = LineCap.ArrowAnchor;
            g.DrawLine(pen, 100, 100, 300, 300);

            //畫聯結線條
            GraphicsPath path = new GraphicsPath();
            Pen penJoin = new Pen(Color.FromArgb(255, 0, 0, 255), 20);

            path.StartFigure();
            path.AddLine(new Point(50, 200), new Point(100, 200));
            path.AddLine(new Point(100, 200), new Point(100, 250));

            penJoin.LineJoin = LineJoin.Bevel;
            g.DrawPath(penJoin, path);

            //繪製自訂虛線
            float[] dashValues = { 5, 2, 15, 4 };
            Pen greenPen = new Pen(Color.Green, 10);
            greenPen.DashPattern = dashValues;
            g.DrawLine(greenPen, new Point(50, 150), new Point(600, 150));
            
            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //清除畫布
            g.Clear(Color.White);

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //逐點繪圖
            int width = bitmap1.Width;
            int height = bitmap1.Height;
            int xx;
            int yy;
            Color pt;

            //讀取/修改每一的的RGB值
            for (yy = 0; yy < height / 2; yy += 1)
            {
                for (xx = 0; xx < width / 2; xx += 1)
                {
                    pt = bitmap1.GetPixel(xx, yy);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 255 - pt.R, 255 - pt.G, 255 - pt.B));
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    //bitmap1.SetPixel(xx, yy, Color.White);
                }
            }
            pictureBox1.Image = bitmap1;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //儲存圖檔
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\draw_test_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                //string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                //string filename3 = filename + ".png";

                //bitmap1.Save(@filename1, ImageFormat.Jpeg);
                bitmap1.Save(@filename2, ImageFormat.Bmp);
                //bitmap1.Save(@filename3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                //richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                //richTextBox1.Text += "已存檔 : " + filename3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (timer1.Enabled == false)
                timer1.Enabled = true;
            else
                timer1.Enabled = false;
        }

        int x_st = 0;
        int y_st = 0;
        int xx = 0;
        int yy = 0;
        int step = 200;
        Pen pen = new Pen(Color.Blue, 40);
        private void timer1_Tick(object sender, EventArgs e)
        {
            int w = pictureBox1.Width;
            int h = pictureBox1.Height;
            //richTextBox1.Text += "W = " + w.ToString() + " H = " + h.ToString() + "\n";
            if ((xx < (w - 1)) && (yy == 0))
            {
                if (xx == 0)
                {
                    if (pen.Color == Color.Red)
                        pen.Color = Color.Blue;
                    else
                        pen.Color = Color.Red;
                }

                //richTextBox1.Text += "1";
                if (xx < (w - step))
                    xx += step;
                else
                    xx = w - 1;
            }
            else if ((yy < (h - 1)) && (xx == (w - 1)))
            {
                //richTextBox1.Text += "2";
                if (yy < (h - step))
                    yy += step;
                else
                    yy = h - 1;
            }
            else if ((xx > 0) && (yy == (h - 1)))
            {
                //richTextBox1.Text += "3";
                if (xx > step)
                    xx -= step;
                else
                    xx = 0;
            }
            else if ((yy > 0) && (xx == 0))
            {
                //richTextBox1.Text += "4";
                if (yy > step)
                    yy -= step;
                else
                    yy = 0;
            }
            else
            {
                richTextBox1.Text += "xxxxxx\n";
            }

            if (pen.Color == Color.Red)
                pen.Color = Color.Blue;
            else
                pen.Color = Color.Red;


            g.DrawLine(pen, x_st, y_st, xx, yy);
            x_st = xx;
            y_st = yy;

            pictureBox1.Image = bitmap1;



        }

        private void button9_Click(object sender, EventArgs e)
        {
            int i;
            double gamma;

            int[] data_in = new int[256];
            int[] data_out = new int[256];
            Point[] curvePoints = new Point[256];    //一維陣列內有 N 個Point

            Pen gammaPen = new Pen(Color.Red, 2);
            gamma = 2.2;
            //畫出真正的Gamma 2.2曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(gammaPen, curvePoints);   //畫直線

            gammaPen = new Pen(Color.Green, 2);
            gamma = 2.3;
            //畫出真正的Gamma 2.3曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(gammaPen, curvePoints);   //畫直線

            gammaPen = new Pen(Color.Blue, 2);
            gamma = 2.4;
            //畫出真正的Gamma 2.4曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(gammaPen, curvePoints);   //畫直線




            int YST0 = 0x00;
            int YST1 = 0x14;
            int YST2 = 0x22;
            int YST3 = 0x37;
            int YST4 = 0x4B;
            int YST5 = 0x5E;
            int YST6 = 0x6B;
            int YST7 = 0x76;
            int YST8 = 0x82;
            int YST9 = 0x8C;
            int YST10 = 0x9F;
            int YST11 = 0xAB;
            int YST12 = 0xB5;
            int YST13 = 0xCF;
            int YST14 = 0xDE;
            int YST15 = 0xED;

            int YSLP15 = 0x1B;

            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;

                if (data_in[i] <= 4)
                    data_out[i] = YST0 + (YST1 - YST0) * (data_in[i] - 0) / 4;
                else if (data_in[i] <= 8)
                    data_out[i] = YST1 + (YST2 - YST1) * (data_in[i] - 4) / 4;
                else if (data_in[i] <= 16)
                    data_out[i] = YST2 + (YST3 - YST2) * (data_in[i] - 8) / 8;
                else if (data_in[i] <= 32)
                    data_out[i] = YST4 + (YST4 - YST3) * (data_in[i] - 16) / 16;
                else if (data_in[i] <= 40)
                    data_out[i] = YST5 + (YST5 - YST4) * (data_in[i] - 32) / 8;
                else if (data_in[i] <= 48)
                    data_out[i] = YST6 + (YST6 - YST5) * (data_in[i] - 40) / 8;
                else if (data_in[i] <= 56)
                    data_out[i] = YST7 + (YST7 - YST6) * (data_in[i] - 48) / 8;
                else if (data_in[i] <= 64)
                    data_out[i] = YST8 + (YST8 - YST7) * (data_in[i] - 56) / 8;
                else if (data_in[i] <= 72)
                    data_out[i] = YST9 + (YST9 - YST8) * (data_in[i] - 64) / 8;
                else if (data_in[i] <= 80)
                    data_out[i] = YST10 + (YST10 - YST9) * (data_in[i] - 72) / 8;
                else if (data_in[i] <= 96)
                    data_out[i] = YST11 + (YST11 - YST10) * (data_in[i] - 80) / 16;
                else if (data_in[i] <= 112)
                    data_out[i] = YST12 + (YST12 - YST11) * (data_in[i] - 96) / 16;
                else if (data_in[i] <= 144)
                    data_out[i] = YST13 + (YST13 - YST12) * (data_in[i] - 112) / 32;
                else if (data_in[i] <= 176)
                    data_out[i] = YST14 + (YST14 - YST13) * (data_in[i] - 144) / 32;
                else if (data_in[i] <= 208)
                    data_out[i] = YST15 + (YST15 - YST14) * (data_in[i] - 176) / 32;
                else
                    data_out[i] = YST15 + YSLP15 * (data_in[i] - 208) / 64;
            }

            //int YSLP15 = 0x1B;
            //Yst15 + Yslp15 × (data - 208) / 64


            richTextBox1.Text += "In:\n";
            for (i = 0; i < 256; i++)
                richTextBox1.Text += data_in[i].ToString() + " ";
            richTextBox1.Text += "\n";

            richTextBox1.Text += "Out:\n";
            for (i = 0; i < 256; i++)
                richTextBox1.Text += data_out[i].ToString() + " ";
            richTextBox1.Text += "\n";

            pictureBox1.Size = new Size(256 * 3, 256 * 2);   //改變圖框大小

            Pen redPen = new Pen(Color.Red, 3);

            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = data_in[i] * 3;
                //curvePoints[i].Y = H - (int)y1_data[i] - 100;
                //curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + (draw_max - draw_min) / 2000) * 2;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;


                //curvePoints[i].X = i;
                //curvePoints[i].Y = H - (int)y1_data[i] - 100;
                //curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + (draw_max - draw_min) / 2000) * 2;
                //curvePoints[i].Y = 100;

            }

            // Draw lines between original points to screen.
            g.DrawLines(redPen, curvePoints);   //畫直線

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));





            pictureBox1.Image = bitmap1;





        }
    }
}
