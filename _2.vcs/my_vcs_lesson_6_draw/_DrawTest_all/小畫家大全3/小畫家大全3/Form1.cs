using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace 小畫家大全3
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        //SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();

            show_item_location();
            comboBox1.SelectedIndex = 1;
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 3);
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 800;
            y_st = 10;
            dx = 120;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            button3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            button22.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 8);

            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            pictureBox1.Location = new Point(10, 150);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //指定畫布大小
            pictureBox1.Width = 640;
            pictureBox1.Height = 480;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int xx;
            int yy;
            bitmap1 = new Bitmap(300, 300);
            for (yy = 0; yy < 300; yy++)
            {
                for (xx = 0; xx < 300; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0xff, 64, 64));
                }
            }
            pictureBox1.Image = bitmap1;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
                bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 50, 50, 100, 100);

            g.DrawRectangle(p, 200, 200, 100, 100);

            g.DrawEllipse(p, 50, 50, 100, 100);
            p = new Pen(Color.Blue, 5);
            g.DrawEllipse(p, 100, 100, 100, 100);


            pictureBox1.Image = bitmap1;


        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    richTextBox1.Text += "Normal\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
                    break;
                case 1:
                    richTextBox1.Text += "AutoSize\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
                    break;
                case 2:
                    richTextBox1.Text += "CenterImage\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
                    break;
                case 3:
                    richTextBox1.Text += "StretchImage\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
                    break;
                case 4:
                    richTextBox1.Text += "Zoom\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                    break;
                default:
                    richTextBox1.Text += "xxxxxxxxxx\n";
                    break;
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(600, 500);
            pictureBox1.Location = new Point(10, 10);

            int i;
            int xx;
            int yy;
            int width = 600;
            int height = 500;
            byte[,] rgb = new byte[30, 3];

            /*
            var random = new Random();

            for (i = 0; i < 100; i++)
            {
                //richTextBox1.Text += random.Next(3).ToString() + "  ";

            }
            */

            for (i = 0; i < 30; i++)
            {
                int rrr;
                int ggg;
                int bbb;

                rrr = (i % 27) / 9;
                ggg = ((i % 27) % 9) / 3;
                bbb = (i % 27) % 3;

                if (rrr == 0)
                    rrr = 0;
                else
                    rrr = (byte)(128 * rrr - 1);
                if (ggg == 0)
                    ggg = 0;
                else
                    ggg = (byte)(128 * ggg - 1);
                if (bbb == 0)
                    bbb = 0;
                else
                    bbb = (byte)(128 * bbb - 1);

                if (rrr > 255)
                    rrr = 255;
                if (ggg > 255)
                    ggg = 255;
                if (bbb > 255)
                    bbb = 255;

                rgb[i, 0] = (byte)rrr;
                rgb[i, 1] = (byte)ggg;
                rgb[i, 2] = (byte)bbb;
            }
            for (i = 0; i < 30; i++)
            {
                richTextBox1.Text += rgb[i, 0].ToString("X2") + " " + rgb[i, 1].ToString("X2") + " " + rgb[i, 2].ToString("X2");
                if ((i % 4) == 3)
                {
                    richTextBox1.Text += "\n";
                }
                else if ((i % 2) == 1)
                {
                    richTextBox1.Text += "   ";
                }
                else
                    richTextBox1.Text += "  ";
            }
            richTextBox1.Text += "\n";
            for (i = 0; i < 30; i++)
            {
                richTextBox1.Text += (((rgb[i, 0] + 1) / 128) << 8 | ((rgb[i, 1] + 1) / 128) << 4 | ((rgb[i, 2] + 1) / 128)).ToString("X3");
                if ((i % 6) == 5)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += "  ";
            }
            richTextBox1.Text += "\n";
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
                    /*
                    if ((xx % 100) == 0)
                    {
                        if ((yy % 100) == 0)
                        {
                            int rrr = random.Next(3);
                            int ggg = random.Next(3);
                            int bbb = random.Next(3);

                            if (rrr == 0)
                                rr = 0;
                            else
                                rr = (byte)(128 * rrr - 1);

                            if (ggg == 0)
                                ggg = 0;
                            else
                                gg = (byte)(128 * ggg - 1);

                            if (bbb == 0)
                                bb = 0;
                            else
                                bb = (byte)(128 * bbb - 1);

                            richTextBox1.Text += "rrr = " + rrr.ToString() + " ggg = " + ggg.ToString() + " bbb = " + bbb.ToString() + "\t";
                            richTextBox1.Text += "xx = " + xx.ToString() + " yy = " + yy.ToString() + " rr = " + rr.ToString() + " gg = " + gg.ToString() + " bb = " + bb.ToString() + "\n";
                        
                        }
                    }
                    */

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
                    rr = (byte)rgb[xx / 100 + (yy / 100) * 6, 0];
                    gg = (byte)rgb[xx / 100 + (yy / 100) * 6, 1];
                    bb = (byte)rgb[xx / 100 + (yy / 100) * 6, 2];
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                }
            }
            pictureBox1.Image = bitmap1;

        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void button25_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void button26_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            pictureBox1.Location = new Point(0, 200);

            g = this.CreateGraphics();
            int w = 550;
            int h = 170;

            DrawTest(g, w, h);


        }

        private void button22_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(550, 170);
            pictureBox1.Location = new Point(50, 50);

            g = pictureBox1.CreateGraphics();
            int w = pictureBox1.ClientSize.Width;
            int h = pictureBox1.ClientSize.Height;

            DrawTest(g, w, h);

        }

        private void DrawTest(Graphics g, int w, int h)
        {

            g.DrawRectangle(p, 0, 0, w - 1, h - 1);
            Rectangle rect = new Rectangle(0, 0, w - 1, h - 1);
            g.DrawEllipse(p, rect);

            p = new Pen(Color.FromArgb(255, 0, 123, 0), 5);
            Point px1 = new Point(w / 10, h / 2);
            Point px2 = new Point(w * 9 / 10, h / 2);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);

            p = new Pen(Brushes.Green, 3);
            Point[] points = new Point[7];
            points[0] = new Point(w / 2, 10);
            points[1] = new Point(0, h - 10);
            points[2] = new Point(w / 4, h - 10);
            points[3] = new Point(w / 4, h - 10 - 30);
            points[4] = new Point(w * 3 / 4, h - 10 - 30);
            points[5] = new Point(w * 3 / 4, h - 10);
            points[6] = new Point(w, h - 10);
            g.DrawPolygon(p, points);

            richTextBox1.Text += "w = " + w.ToString() + "\n";
            richTextBox1.Text += "h = " + h.ToString() + "\n";

            p = new Pen(Color.Blue, 3);
            g.DrawRectangle(p, 0, 0, w - 1, h - 1);
            g.DrawRectangle(p, 0, 0, w - 1 - 50, h - 1 - 50);
            g.DrawRectangle(p, 0, 0, w - 1 - 100, h - 1 - 100);

            //Brush b = new SolidBrush(Color.Blue);
            Brush b = new SolidBrush(Color.FromArgb(30, 0, 123, 0));
            g.FillRectangle(b, w / 4, 50, w / 2, 50);

        }

        private void button24_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            g = this.CreateGraphics();
            g.Clear(Color.Gray);
            g = pictureBox1.CreateGraphics();
            g.Clear(Color.Gray);
        }

        /*
        int x_old = 0;
        int y_old = 0;

        bool flag_eraser_mode = false;
        bool enable_erase = false;
        */

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            /*
            if (checkBox1.Checked == true)
            {
                flag_eraser_mode = true;
                pictureBox1.Visible = false;

                g = this.CreateGraphics();
                p = new Pen(Color.Red, 6);
            }
            else
            {
                flag_eraser_mode = false;
                pictureBox1.Visible = true;
            }
            */
        }

    }
}
