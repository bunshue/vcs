using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for LinearGradientBrush
using System.Drawing.Text;      //for TextRenderingHint

namespace vcs_Draw1
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
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.ResizeRedraw = true;

            show_item_location();
            comboBox1.SelectedIndex = 1;
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 3);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            pictureBox_uac.Image = UacStuff.GetUacShieldImage();
            // Add the shield to a button.
            UacStuff.AddShieldToButton(button29);

            DrawPictureBoxText();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1240;
            y_st = 40;
            dx = 130;
            dy = 50;

            pictureBox_uac.Location = new Point(x_st + dx * 0-100, y_st + dy * 0);
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            button5.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button7.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button8.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 4, y_st + dy * 1);

            button10.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button12.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button14.Location = new Point(x_st + dx * 4, y_st + dy * 2);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button18.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 4, y_st + dy * 3);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button23.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button24.Location = new Point(x_st + dx * 4, y_st + dy * 4);

            button25.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button28.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button29.Location = new Point(x_st + dx * 4, y_st + dy * 5);

            button30.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button31.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button34.Location = new Point(x_st + dx * 4, y_st + dy * 6);

            button35.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button36.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button37.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button39.Location = new Point(x_st + dx * 4, y_st + dy * 7);

            button40.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button41.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button42.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button43.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button44.Location = new Point(x_st + dx * 4, y_st + dy * 8);

            button45.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button46.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button47.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button48.Location = new Point(x_st + dx * 3, y_st + dy * 9);
            button49.Location = new Point(x_st + dx * 4, y_st + dy * 9);

            bt_save.Location = new Point(x_st + dx * 3, y_st + dy * 11);
            bt_exit.Location = new Point(x_st + dx * 4, y_st + dy * 11);

            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            checkBox1.Location = new Point(x_st + dx * 1, y_st + dy * 12);

            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y + 80);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            pictureBox1.Location = new Point(40, 40);

            panel2.Size = new Size(750, 100);
            panel2.Location = new Point(50, 570);
            panel2.BackColor = Color.Pink;


            pictureBox_text.Location = new Point(50, 570 + 120);
        }

        private void DrawPoint(Graphics g, PointF pt, Color c_out, Color c_in, int radius)
        {
            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c_out, 1);
            SolidBrush b = new SolidBrush(c_in);
            //Brush b = new Brush(c_in);

            // Draw the circle
            g.FillEllipse(b, pt.X - radius, pt.Y - radius, radius * 2, radius * 2);
            g.DrawEllipse(p, pt.X - radius, pt.Y - radius, radius * 2, radius * 2);
            //Dispose of the pen.
            p.Dispose();
        }

        private void DrawCircle(Graphics g, PointF center, int radius, int linewidth, Color c)
        {
            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c, linewidth);
            richTextBox1.Text += "draw circle\n";
            // Draw the circle
            g.DrawEllipse(p, center.X - radius, center.Y - radius, radius * 2, radius * 2);
            //Dispose of the pen.
            p.Dispose();
        }

        private void FillCircle(Graphics g, PointF center, int radius, Color c)
        {
            SolidBrush newBrush = new SolidBrush(c);

            // Fill the circle
            g.FillEllipse(newBrush, new RectangleF(center.X - radius, center.Y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            newBrush.Dispose();
        }

        private void DrawStar(Graphics g, PointF center, int radius, int linewidth, Color c)
        {
            //DrawStar

            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c, linewidth);

            PointF[] pt = new PointF[6];    //一維陣列內有6個Point
            int angle;

            int i;
            for (i = 0; i < 6; i++)
            {
                angle = -90 + 144 * i;
                pt[i].X = (int)(radius * Math.Cos(angle * Math.PI / 180));
                pt[i].Y = (int)(radius * Math.Sin(angle * Math.PI / 180));

                //richTextBox1.Text += "pt[" + i.ToString() + "].X " + pt[i].X.ToString() + "\t" + "pt[" + i.ToString() + "].Y " + pt[i].Y.ToString() + "\n";
                pt[i].X += center.X;
                pt[i].Y += center.Y;
            }
            g.DrawLines(new Pen(Brushes.Red, linewidth), pt);

            //Dispose of the pen.
            p.Dispose();
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

        private void DrawGrid()
        {
            int i;
            p = new Pen(Color.Navy, 1);
            for (i = 0; i < 7; i++)
            {
                g.DrawLine(p, 0, i * 100, pictureBox1.ClientSize.Width - 1, i * 100);
            }
            for (i = 0; i < 7; i++)
            {
                g.DrawLine(p, new Point(i * 100, 0), new Point(i * 100, pictureBox1.ClientSize.Height - 1));
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            open_new_file();
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
            {
                open_new_file();
            }

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 50, 50, 100, 100);

            g.DrawRectangle(p, 130, 110, 100, 130);

            g.DrawEllipse(p, 50, 50, 100, 100);

            p = new Pen(Color.Blue, 5);
            g.DrawEllipse(p, 200, 30, 60, 60);

            p = new Pen(Color.Green, 10);
            g.DrawRectangle(p, 0 + p.Width / 2, 0 + p.Width / 2, bitmap1.Width - p.Width, bitmap1.Height - p.Width);

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

        private void button11_Click(object sender, EventArgs e)
        {
            int width;
            int height;

            string filename = "C:\\______test_files\\picture1.jpg";

            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);

            richTextBox1.Text += "檔案大小 W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            width = bitmap1.Width;
            height = bitmap1.Height;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);

            pictureBox1.Image = bitmap1;
            richTextBox1.Text += "\n";

            SolidBrush sb;
            Font f;
            sb = new SolidBrush(Color.Purple);
            f = new Font("Times New Roman", 30);
            //f = new Font("標楷體", 20);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            //g.DrawRectangle(p, 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);
            //g.DrawRectangle(p, 100, 100, bitmap1.Width - 1 - 200, bitmap1.Height - 1 - 200);

            p = new Pen(Color.Purple, 5);

            /*
            g.DrawLine(p, 0, bitmap1.Height / 2, bitmap1.Width - 1, bitmap1.Height / 2);
            g.DrawLine(p, bitmap1.Width / 2, 0, bitmap1.Width / 2, bitmap1.Height - 1);
            g.DrawString("Sugar", f, sb, new PointF(bitmap1.Width - 75, bitmap1.Height / 2 - 35));
            g.DrawString("Sugar", f, sb, new PointF(bitmap1.Width - 75, bitmap1.Height / 1 - 35));
            */

            g.DrawString("Sugar", f, sb, new PointF(bitmap1.Width - 210, bitmap1.Height / 1 - 150));

            pictureBox1.Image = bitmap1;


            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            //存檔
            save_image_to_drive();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            int width;
            int height;

            string filename = "C:\\______test_files\\step2.png";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);
            //pictureBox1.Image = bitmap2;

            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            width = bitmap1.Width;
            height = bitmap1.Height;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.Image = bitmap1;

        }

        private void button13_Click(object sender, EventArgs e)
        {
            SolidBrush sb;
            Font f;

            sb = new SolidBrush(Color.Blue);
            //f = new Font("標楷體", 20);
            f = new Font("標楷體", 16);

            if (bitmap1 == null)
            {
                open_new_file();
            }

            sb = new SolidBrush(Color.Red);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            //g.FillRectangle(sb, 75, 75, 200, 75);

            //g.DrawString("內視鏡時效已過", f, sb, new PointF(70.0F, 110.0F));
            //g.DrawString("請更換", f, sb, new PointF(240.0F, 200.0F));

            //g.DrawString("內視鏡時效已過", f, sb, new PointF(120.0F, 70.0F));
            //g.DrawString("請更換", f, sb, new PointF(270.0F, 160.0F));
            //g.DrawString("相機非全新且不同", f, sb, new PointF(90.0F, 250.0F));

            f = new Font("標楷體", 24);
            g.DrawString("主機電池失效", f, sb, new PointF(60.0F, 90.0F));
            g.DrawString("請更換與校時", f, sb, new PointF(60.0F, 200.0F));

            //f = new Font("標楷體", 12);
            //g.DrawString("(使用<30分，累計關機>30分)", f, sb, new PointF(40.0F, 290.0F));

            pictureBox1.Image = bitmap1;

        }

        private void button14_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                richTextBox1.Text += "尚未開啟圖片\n";
                return;
            }

            int ccc = 0;
            int xx;
            int yy;

            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            Color rr = Color.Red;
            Color gg = Color.Green;
            Color bb = Color.Blue;

            richTextBox1.Text += "R : " + rr.A.ToString("X2") + rr.R.ToString("X2") + rr.G.ToString("X2") + rr.B.ToString("X2") + "\n";
            richTextBox1.Text += "G : " + gg.A.ToString("X2") + gg.R.ToString("X2") + gg.G.ToString("X2") + gg.B.ToString("X2") + "\n";
            richTextBox1.Text += "B : " + bb.A.ToString("X2") + bb.R.ToString("X2") + bb.G.ToString("X2") + bb.B.ToString("X2") + "\n";

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    if ((yy % 120) == 0)
                    {
                        bitmap1.SetPixel(xx, yy, rr);
                    }
                    else if ((yy % 120) == 30)
                    {
                        bitmap1.SetPixel(xx, yy, gg);
                    }
                    else if ((yy % 120) == 60)
                    {
                        bitmap1.SetPixel(xx, yy, bb);
                    }
                    else if ((yy % 120) == 90)
                    {
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0, 0, 0));
                    }

                    ccc++;
                    if ((ccc % 30000) == 0)
                    {
                        Color p = bitmap1.GetPixel(xx, yy);
                        //richTextBox1.Text += p.ToString() + " ";
                        richTextBox1.Text += p.A.ToString("X2") + p.R.ToString("X2") + p.G.ToString("X2") + p.B.ToString("X2") + " ";

                    }

                }
            }
            pictureBox1.Image = bitmap1;
            richTextBox1.Text += "\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
            int width;
            int height;

            string filename = "C:\\______test_files\\sample.png";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);
            //pictureBox1.Image = bitmap2;

            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            width = bitmap1.Width;
            height = bitmap1.Height;

            //pictureBox1.Size = new Size(1, 1);
            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);


            pictureBox1.Image = bitmap1;
            richTextBox1.Text += "\n";


            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化


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

        private void button6_Click(object sender, EventArgs e)
        {
            int width = 1920;
            int height = 1080;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);

            bitmap1 = new Bitmap(width, height);

            int xx;
            int yy;
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(30, 0x11, 0x33, 0x55));
                }
            }

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, width - 1, height - 1);

            g.DrawRectangle(p, 50, 50, width - 100 - 1, height - 100 - 1);

            g.DrawRectangle(p, 100, 100, width - 200 - 1, height - 200 - 1);

            SolidBrush sb;
            Font f;
            sb = new SolidBrush(Color.Blue);
            f = new Font("標楷體", 36);


            g.DrawString("1920 X 1080", f, sb, new PointF(width - 500, height - 300));

            pictureBox1.Image = bitmap1;

            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化



        }

        private void button7_Click(object sender, EventArgs e)
        {
            int ww = 1000;
            int hh = 500;
            int dd = ww / 5;
            pictureBox1.Size = new Size(ww, hh);
            pictureBox1.Location = new Point(10, 10);

            //逐點製作圖檔
            int xx;
            int yy;
            bitmap1 = new Bitmap(ww, hh);
            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    if ((xx / dd) < 1)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0xff, 0x00, 0x00));
                    else if ((xx / dd) < 2)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x00, 0xff, 0x00));
                    else if ((xx / dd) < 3)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x00, 0x00, 0xff));
                    else if ((xx / dd) < 4)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x00, 0x00, 0x00));
                    else if ((xx / dd) < 5)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0xff, 0xff, 0xff));
                    else
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                }
            }

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            for (int i = 0; i < 5; i++)
            {
                if (i == 3)
                    sb = new SolidBrush(Color.White);
                else
                    sb = new SolidBrush(Color.Black);

                g.FillEllipse(sb, dd * i + dd / 2, 100, 10, 10);
            }

            Font f = new Font("標楷體", 100);
            sb = new SolidBrush(Color.White);
            g.DrawString("ims", f, sb, new PointF(80, 300));

            pictureBox1.Image = bitmap1;


        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            Font f = new Font("標楷體", 20);
            SolidBrush sb = new SolidBrush(Color.Purple);

            Point p1 = new Point(10, 100);
            Point p2 = new Point(590, 120);
            Pen p = new Pen(Color.Red, 5);
            g.DrawLine(p, p1, p2);
            g.DrawString("反鋸齒功能\t關閉", f, sb, new PointF(170, 70));

            g.SmoothingMode = SmoothingMode.AntiAlias;  //反鋸齒功能

            Point p3 = new Point(10, 100 + 100);
            Point p4 = new Point(590, 100 + 120);
            g.DrawLine(p, p3, p4);
            g.DrawString("反鋸齒功能\t打開", f, sb, new PointF(170, 170));

            pictureBox1.Image = bitmap1;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap("C:\\______test_files\\bear.jpg");
            Bitmap bitmap2 = new Bitmap("C:\\______test_files\\__RW\\_png\\vcs_ReadWrite_PNG.png");

            //將圖２貼到圖１左上角
            Graphics g = Graphics.FromImage(bitmap1);   //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawImage(bitmap2, 0, 0);

            //在圖１之右下角輸出文字
            Font f = new Font("Brush Script MT", 24, FontStyle.Italic);
            Brush b = new SolidBrush(Color.White);
            Brush bb = new SolidBrush(Color.Black);
            string ct = "小熊家族";

            int x = bitmap1.Width - 200;
            int y = bitmap1.Height - 50;

            g.DrawString(ct, f, b, x, y);
            g.DrawString(ct, f, bb, x - 1, y - 1);
            g.DrawString(ct, f, bb, x - 1, y + 1);
            g.DrawString(ct, f, bb, x + 1, y - 1);
            g.DrawString(ct, f, bb, x + 1, y + 1);
            g.DrawString(ct, f, b, x, y);

            //存檔
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

        private void button10_Click(object sender, EventArgs e)
        {
            int width = 1920;
            int height = 1080;

            richTextBox1.Text += "FullHD點圖 ST\n";

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);

            bitmap1 = new Bitmap(width, height);

            var random = new Random();
            int xx;
            int yy;
            int rr;
            int gg;
            int bb;
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    rr = random.Next(0, 256);
                    gg = random.Next(0, 256);
                    bb = random.Next(0, 256);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(0xFF, (rr) % 256, (gg) % 256, (bb) % 256));
                }
            }

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, width - 1, height - 1);

            g.DrawRectangle(p, 50, 50, width - 100 - 1, height - 100 - 1);

            g.DrawRectangle(p, 100, 100, width - 200 - 1, height - 200 - 1);

            /*
            SolidBrush sb;
            Font f;
            sb = new SolidBrush(Color.Blue);
            f = new Font("標楷體", 36);


            g.DrawString("1920 X 1080", f, sb, new PointF(width - 500, height - 300));
            */

            pictureBox1.Image = bitmap1;

            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            //存檔
            save_image_to_drive();

            richTextBox1.Text += "FullHD點圖 SP\n";

        }

        private void button16_Click(object sender, EventArgs e)
        {
            int LAYER0_WIDTH = 1920;
            //int LAYER0_HEIGHT = 1080;
            int LAYER1_WIDTH = 1216;
            int LAYER1_HEIGHT = 912;
            //int LAYER2_WIDTH = 640;
            //int LAYER2_HEIGHT = 480;
            //int LAYER3_WIDTH = 1920;
            //int LAYER3_HEIGHT = 1080;
            int BORDER_X = 16;
            int BORDER_Y = 16;

            int LAYER1_START_X = (LAYER0_WIDTH - LAYER1_WIDTH - BORDER_X);
            int LAYER1_START_Y = BORDER_Y;

            //int WIDTH1 = 150;		//for ID NO, NAME
            //int WIDTH2 = 370;		//for Doraemon, 9/3/2112
            //int WIDTH3 = 430;		//for SN : 2DCF-XXXXXX
            //int WIDTH4 = 180;
            //int WIDTH5 = 80;	//for Sun, Mon
            int THICK1 = 40;

            int x;
            int y;
            SolidBrush sb;
            Font f;
            sb = new SolidBrush(Color.Black);
            f = new Font("Times New Roman", 20);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            g.FillRectangle(sb, 0, 0, 500, 800);


            //在指定位置畫上一圖
            // Create image.
            //Image newImage = Image.FromFile(@"C:\______test_files\step3.png");

            string filename = "C:\\______test_files\\step3.png";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            Bitmap bitmap3 = new Bitmap(filename);

            richTextBox1.Text += "W = " + bitmap3.Width.ToString() + " H = " + bitmap3.Height.ToString() + "\n";

            // Create coordinates for upper-left corner of image.
            int dx = 228;
            int dy = 264;

            // Draw image to screen.
            g.DrawImage(bitmap3, LAYER1_START_X + dx, LAYER1_START_Y + dy, bitmap3.Width, bitmap3.Height);

            sb = new SolidBrush(Color.White);

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 0;
            g.DrawString("ID NO:", f, sb, new PointF(x, y));


            x = BORDER_X;
            y = BORDER_Y + THICK1 * 1;
            g.DrawString("NAME:", f, sb, new PointF(x, y));

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 3;
            g.DrawString("SEX:", f, sb, new PointF(x, y));

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 4;
            g.DrawString("AGE:", f, sb, new PointF(x, y));

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 5;
            g.DrawString("Birthday:", f, sb, new PointF(x, y));


            x = BORDER_X;
            y = BORDER_Y + THICK1 * 7;
            g.DrawString("12/28/2018 Fri", f, sb, new PointF(x, y));


            x = BORDER_X;
            y = BORDER_Y + THICK1 * 8;
            g.DrawString("16:33:32", f, sb, new PointF(x, y));

            p = new Pen(Color.Gray, 5);

            g.DrawRectangle(p, LAYER1_START_X, LAYER1_START_Y, LAYER1_WIDTH - 1, LAYER1_HEIGHT - 1);

            p = new Pen(Color.Blue, 5);

            int R = 170;

            Point[] myPointArray = { 
                new Point(LAYER1_START_X + R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + R),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X + R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X, BORDER_Y + R)
                                   };
            g.DrawPolygon(p, myPointArray);

            p = new Pen(Color.Red, 5);

            R = 250;

            Point[] myPointArray2 = { 
                new Point(LAYER1_START_X + R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + R),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X + R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X, BORDER_Y + R)
                                   };
            g.DrawPolygon(p, myPointArray2);


            p = new Pen(Color.Red, 5);
            g.DrawArc(p, LAYER1_START_X, LAYER1_START_Y, R * 2, R * 2, 180, 90);
            g.DrawArc(p, LAYER1_START_X + LAYER1_WIDTH - R * 2, LAYER1_START_Y, R * 2, R * 2, 270, 90);
            g.DrawArc(p, LAYER1_START_X, LAYER1_START_Y + LAYER1_HEIGHT - R * 2, R * 2, R * 2, 90, 90);
            g.DrawArc(p, LAYER1_START_X + LAYER1_WIDTH - R * 2, LAYER1_START_Y + LAYER1_HEIGHT - R * 2, R * 2, R * 2, 0, 90);


            R = 350;
            p = new Pen(Color.Yellow, 5);
            g.DrawArc(p, LAYER1_START_X, LAYER1_START_Y, R * 2, R * 2, 180, 90);
            g.DrawArc(p, LAYER1_START_X + LAYER1_WIDTH - R * 2, LAYER1_START_Y, R * 2, R * 2, 270, 90);
            g.DrawArc(p, LAYER1_START_X, LAYER1_START_Y + LAYER1_HEIGHT - R * 2, R * 2, R * 2, 90, 90);
            g.DrawArc(p, LAYER1_START_X + LAYER1_WIDTH - R * 2, LAYER1_START_Y + LAYER1_HEIGHT - R * 2, R * 2, R * 2, 0, 90);

            Point[] myPointArray3 = { 
                new Point(LAYER1_START_X + R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + R),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X + R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X, BORDER_Y + R)
                                   };
            g.DrawPolygon(p, myPointArray3);


            //SolidBrush sb;
            //Font f;
            sb = new SolidBrush(Color.Blue);
            f = new Font("標楷體", 20);


            g.DrawString("0          170    200    250", f, sb, new PointF(LAYER1_START_X - 10, BORDER_Y + LAYER1_HEIGHT + 15));


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


        private void button17_Click(object sender, EventArgs e)
        {
            //TBD
            //畫布塗黑左上1/4
            int pic_width = pictureBox1.Width;
            int pic_height = pictureBox1.Height;
            bitmap1 = new Bitmap(pic_width / 2, pic_height / 2);
            pictureBox1.Image = bitmap1;
            //pictureBox1.BackColor = Color.Black;
        }

        private void button25_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            p = new Pen(Color.Red, 5);

            g.DrawRectangle(p, 0 + p.Width / 2, 0 + p.Width / 2, bitmap1.Width - p.Width, bitmap1.Height - p.Width);

            pictureBox1.Image = bitmap1;


            richTextBox1.Text += "平移坐標軸至指定座標(100, 100) 然後畫一線\n";
            g.TranslateTransform(100, 100);
            g.DrawLine(p, 0, 0, 100, 0);
            g.ResetTransform();

            richTextBox1.Text += "平移坐標軸至指定座標(200, 200) 然後再進行旋轉座標畫線\n";
            g.TranslateTransform(200, 200);
            for (int i = 0; i < 8; i++)
            {
                //g.RotateTransform(45);
                g.RotateTransform(10);//旋轉指定的角度
                g.DrawLine(p, 0, 0, 100, 0);
            }
            g.Dispose();
        }

        private void button26_Click(object sender, EventArgs e)
        {
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

            panel1.Size = new Size(550, 170);
            panel1.Location = new Point(50, 250);

            g = pictureBox1.CreateGraphics();
            int w = pictureBox1.ClientSize.Width;
            int h = pictureBox1.ClientSize.Height;

            DrawTest(g, w, h);
        }

        private void button23_Click(object sender, EventArgs e)
        {
            panel1.Size = new Size(550, 170);
            panel1.Location = new Point(50, 50);

            g = panel1.CreateGraphics();
            int w = panel1.ClientSize.Width;
            int h = panel1.ClientSize.Height;

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
            if (bitmap1 == null)
            {
                open_new_file();
            }

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            p = new Pen(Color.Red, 5);

            g.DrawRectangle(p, 0 + p.Width / 2, 0 + p.Width / 2, bitmap1.Width - p.Width, bitmap1.Height - p.Width);

            pictureBox1.Image = bitmap1;


            richTextBox1.Text += "轉變坐標軸角度\n";

            for (int i = 0; i <= 90; i += 10)
            {
                g.RotateTransform(i);//旋轉指定的角度
                g.DrawLine(p, 0, 0, 500, 0);    //畫一條線
                g.ResetTransform();//恢復坐標軸坐標 回 0 度
            }

            p = new Pen(Color.Blue, 2);
            g.RotateTransform(20);//旋轉指定的角度
            g.DrawLine(p, 0, 0, 500, 0);    //畫一條線
            g.ResetTransform();//恢復坐標軸坐標 回 0 度

            g.RotateTransform(30);//旋轉指定的角度
            g.DrawLine(p, 0, 0, 500, 0);    //畫一條線
            g.ResetTransform();//恢復坐標軸坐標 回 0 度

            g.Dispose();
        }

        private void button18_Click(object sender, EventArgs e)
        {
            int w = button18.ClientSize.Width;
            int h = button18.ClientSize.Height;
            g = button18.CreateGraphics();
            g.DrawEllipse(p, 0, 0, w - 1, h - 1);
        }

        int x_old = 0;
        int y_old = 0;

        bool flag_eraser_mode = false;
        bool enable_erase = false;

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                flag_eraser_mode = true;
                pictureBox1.Visible = false;
                panel1.Visible = false;

                g = this.CreateGraphics();
                p = new Pen(Color.Red, 6);
            }
            else
            {
                flag_eraser_mode = false;
                pictureBox1.Visible = true;
                panel1.Visible = true;
            }
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Mouse Down\n";
            enable_erase = true;

            x_old = e.X;
            y_old = e.Y;
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Mouse Up\n";
            enable_erase = false;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            //this.Text = e.X.ToString() + ", " + e.Y.ToString();
            this.Text = String.Format("X：{0}, Y：{1}", e.X, e.Y);    //格式化字串

            if ((flag_eraser_mode == true) && (enable_erase == true))
            {
                sb = new SolidBrush(Color.Red);
                //g.FillEllipse(sb, e.X, e.Y, 10, 10);

                g.DrawLine(new Pen(Color.Red, 10), x_old, y_old, e.X, e.Y);

                x_old = e.X;
                y_old = e.Y;
            }
        }

        private void button19_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                richTextBox1.Text += "尚未開啟圖片\n";
                return;
            }

            Bitmap bmp = new Bitmap(@"C:\______test_files\red-ball-icon.png");
            g.DrawImage(bmp, 180, 20);


            pictureBox1.Image = bitmap1;
        }

        private void button20_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\bear.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);
            this.ClientSize = bitmap1.Size;
            //this.Size = bitmap1.Size;
            //g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g = this.CreateGraphics();
            g.DrawImage(bitmap1, 0, 0);

            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            //pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中

            /*
            bitmap1 = new Bitmap(@"C:\______test_files\bear.jpg");
            Draw = Graphics.FromImage(bmp);
            this.Size = bmp.Size;
            g = this.CreateGraphics();
            g.DrawImage(bmp, 0, 0);
            */
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            //另法
            //bitmap1 = null;
            //pictureBox1.Image = null;

            richTextBox1.Clear();
            g = this.CreateGraphics();
            g.Clear(Color.Gray);
            g = panel1.CreateGraphics();
            g.Clear(Color.Gray);
            g = pictureBox1.CreateGraphics();
            g.Clear(Color.Gray);
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void open_new_file()
        {
            richTextBox1.Text += "開啟一個 640 X 480 的空畫布\n";
            //指定畫布大小
            pictureBox1.Width = 640;
            pictureBox1.Height = 480;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
            return;
        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {
            GradientColor(e);
        }

        //抽取成一個方法實現漸變色,在Paint中引用
        private void GradientColor(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            Color FColor = Color.Green;
            Color TColor = Color.Yellow;

            Brush b = new LinearGradientBrush(this.ClientRectangle, FColor, TColor, LinearGradientMode.ForwardDiagonal);

            g.FillRectangle(b, this.ClientRectangle);

            /*
             * Horizontal = 0　　　　　　摘要:指定從左到右的漸變。
             * 
             * Vertical = 1　　　　　　　摘要: 指定從上到下的漸變。
             * 
             * ForwardDiagonal = 2　　  摘要:指定從左上到右下的漸變。
             * 
             * BackwardDiagonal = 3　　 摘要:指定從右上到左下的漸變。
             */
        }

        //The Paint Event Handler
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            try
            {
                // Draw the selection rectangle.
                using (Pen pen = new Pen(Color.Red, 2))
                {
                    //Rectangle rect = SelectionRectangle(true);
                    e.Graphics.DrawRectangle(pen, 0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);

                    pen.Color = Color.Green;
                    pen.DashPattern = new float[] { 5, 5 };
                    e.Graphics.DrawRectangle(pen, 5, 5, pictureBox1.Size.Width - 10, pictureBox1.Size.Height - 10);
                }
            }
            catch
            {
            }
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //DrawLines 直接使用 List
            List<PointF> points = new List<PointF>();

            // Make the Bitmap.
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            Bitmap bm = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bm);
            g.SmoothingMode = SmoothingMode.AntiAlias;  //反鋸齒

            // Draw the graph.
            Pen graph_pen = new Pen(Color.Blue, 1);

            // Loop over x values to generate points.
            for (float x = 0; x < W; x += 5)
            {
                float y = (float)(H / 2 * Math.Sin(x / 25)) + H / 2;
                points.Add(new PointF(x, y));
            }

            if (points.Count > 1)
            {
                //transform
                for (int i = 0; i < points.Count; i++)
                {
                    points[i] = new PointF(points[i].X, H - points[i].Y);
                }
                g.DrawLines(graph_pen, points.ToArray());
            }
            // Display the result.
            pictureBox1.Image = bm;

        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // Make a rectangle.
            Rectangle rect1 = new Rectangle(20, 20,
                this.ClientSize.Width - 40,
                this.ClientSize.Height - 40);

            // Convert to RectangleF.
            RectangleF rectf = rect1;

            // Convert back to Rectangle.
            Rectangle rect2 = Rectangle.Round(rectf);
            //Rectangle rect2 = Rectangle.Truncate(rectf);

            // Draw them.
            using (Pen the_pen = new Pen(Color.Red, 20))
            {
                e.Graphics.DrawRectangle(the_pen, rect1);

                the_pen.Color = Color.Lime;
                the_pen.Width = 10;
                e.Graphics.DrawRectangle(the_pen,
                    rectf.X, rectf.Y, rectf.Width, rectf.Height);

                the_pen.Color = Color.Blue;
                the_pen.Width = 1;
                e.Graphics.DrawRectangle(the_pen, rect2);
            }



            //表單底部畫字 ST
            // Transform.
            e.Graphics.ScaleTransform(1.5f, 1.5f, MatrixOrder.Append);
            e.Graphics.RotateTransform(25, MatrixOrder.Append);
            e.Graphics.TranslateTransform(80, 30, MatrixOrder.Append);

            int x_st = 260;
            int y_st = 0;
            // Make a font.
            using (Font the_font = new Font("Times New Roman", 40, FontStyle.Regular, GraphicsUnit.Pixel))
            {
                // See how big the text will be when drawn.
                string the_text = "群曜醫電股份有限公司";
                SizeF text_size = e.Graphics.MeasureString(the_text, the_font);

                // Draw a rectangle and two ellipses.
                e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
                e.Graphics.DrawRectangle(Pens.Blue, x_st, y_st, text_size.Width, text_size.Height);
                e.Graphics.DrawEllipse(Pens.Red, x_st - 3, y_st - 3, 6, 6);
                e.Graphics.DrawEllipse(Pens.Green, text_size.Width - 3, text_size.Height - 3, 6, 6);

                // Draw the text.
                e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                e.Graphics.DrawString(the_text, the_font, Brushes.Brown, x_st, y_st);
            }
            //表單底部畫字 SP

        }

        // Draw samples.
        private const int column_width = 150;
        private const int row_height = 50;

        private void button28_Click(object sender, EventArgs e)
        {
            Graphics g = this.CreateGraphics();
            int x = 520;
            int y = 50;
            DrawIconSample(g, ref x, y, SystemIcons.Application, "Application");
            DrawIconSample(g, ref x, y, SystemIcons.Asterisk, "Asterisk");
            DrawIconSample(g, ref x, y, SystemIcons.Error, "Error");
            x = 520;
            y += 40;
            DrawIconSample(g, ref x, y, SystemIcons.Exclamation, "Exclamation");
            DrawIconSample(g, ref x, y, SystemIcons.Hand, "Hand");
            DrawIconSample(g, ref x, y, SystemIcons.Information, "Information");
            x = 520;
            y += row_height;
            DrawIconSample(g, ref x, y, SystemIcons.Question, "Question");
            DrawIconSample(g, ref x, y, SystemIcons.Shield, "Shield");
            DrawIconSample(g, ref x, y, SystemIcons.Warning, "Warning");
            x = 520;
            y += 40;
            DrawIconSample(g, ref x, y, SystemIcons.WinLogo, "WinLogo");
        }

        #region pictureBox_text
        // Draw the text.
        void DrawPictureBoxText()
        {
            // Make a Bitmap to hold the text.
            Bitmap bm = new Bitmap(
                pictureBox_text.ClientSize.Width,
                pictureBox_text.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.White);

                // Don't use TextRenderingHint.AntiAliasGridFit.
                gr.TextRenderingHint = TextRenderingHint.AntiAlias;

                // Make a font to use.
                using (Font font = new Font("Times New Roman", 16, FontStyle.Regular))
                {
                    // Draw the text.
                    DrawTextInBoxes(gr, font, 4, 4,
                        "When in the course of human events it " +
                        "becomes necessary for the quick brown " +
                        "fox to jump over the lazy dog...");
                }
            }

            // Display the result.
            pictureBox_text.Image = bm;
        }

        // Draw a sample and its name.
        private void DrawIconSample(Graphics gr, ref int x, int y, Icon ico, string ico_name)
        {
            gr.DrawIconUnstretched(ico, new Rectangle(x, y, ico.Width, ico.Height));
            int text_y = y + (int)(ico.Height - gr.MeasureString(ico_name, this.Font).Height) / 2;
            gr.DrawString(ico_name, this.Font, Brushes.Black, x + ico.Width + 5, text_y);
            x += column_width;
        }

        // Draw a long string with boxes around each character.
        private void DrawTextInBoxes(Graphics gr, Font font,
            float start_x, float start_y, string text)
        {
            // Measure the characters.
            List<RectangleF> rects = MeasureCharacters(gr, font, text);

            for (int i = 0; i < text.Length; i++)
            {
                gr.DrawRectangle(Pens.Red,
                    start_x + rects[i].Left, start_y + rects[i].Top,
                    rects[i].Width, rects[i].Height);
            }
            gr.DrawString(text, font, Brushes.Blue, start_x, start_y);
        }

        // Measure the characters in the string.
        private List<RectangleF> MeasureCharacters(Graphics gr, Font font, string text)
        {
            List<RectangleF> results = new List<RectangleF>();

            // The X location for the next character.
            float x = 0;

            // Get the character sizes 31 characters at a time.
            for (int start = 0; start < text.Length; start += 32)
            {
                // Get the substring.
                int len = 32;
                if (start + len >= text.Length) len = text.Length - start;
                string substring = text.Substring(start, len);

                // For debugging.
                // Console.WriteLine(substring);

                // Measure the characters.
                List<RectangleF> rects = MeasureCharactersInWord(gr, font, substring);

                // Remove lead-in for the first character.
                if (start == 0) x += rects[0].Left;

                // For debugging.
                // Console.WriteLine(rects[0].Left);

                // Save all but the last rectangle.
                for (int i = 0; i < rects.Count + 1 - 1; i++)
                {
                    RectangleF new_rect = new RectangleF(
                        x, rects[i].Top,
                        rects[i].Width, rects[i].Height);
                    results.Add(new_rect);

                    // Move to the next character's X position.
                    x += rects[i].Width;
                }
            }

            // Return the results.
            return results;
        }

        // Measure the characters in a string with
        // no more than 32 characters.
        private List<RectangleF> MeasureCharactersInWord(
            Graphics gr, Font font, string text)
        {
            List<RectangleF> result = new List<RectangleF>();

            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Near;
                string_format.LineAlignment = StringAlignment.Near;
                string_format.Trimming = StringTrimming.None;
                string_format.FormatFlags = StringFormatFlags.MeasureTrailingSpaces;

                CharacterRange[] ranges = new CharacterRange[text.Length];
                for (int i = 0; i < text.Length; i++)
                {
                    ranges[i] = new CharacterRange(i, 1);
                }
                string_format.SetMeasurableCharacterRanges(ranges);

                // Find the character ranges.
                RectangleF rect = new RectangleF(0, 0, 10000, 100);
                Region[] regions =
                    gr.MeasureCharacterRanges(
                        text, font, this.ClientRectangle,
                        string_format);

                // Convert the regions into rectangles.
                foreach (Region region in regions)
                    result.Add(region.GetBounds(gr));
            }
            return result;
        }
        #endregion

        private void button30_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                richTextBox1.Text += "尚未開啟檔案\n";
                return;
            }

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            Point[] pts =
            {
                new Point(W / 2, 0),    //上
                new Point(W, H / 2),    //右
                new Point(W / 2, H),    //下
                new Point(0, H / 2),    //左
            };
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.DrawPolygon(Pens.Blue, pts);

            Point[] pts2 =
            {
                new Point(W / 2, H/6),
                new Point(W, H / 2),
                new Point(W / 2, H*5/6),
                new Point(0, H / 2),
            };
            g.FillPolygon(new SolidBrush(Color.Red), pts2);

            sb = new SolidBrush(Color.Purple);
            g.FillPolygon(sb, pts2);

            p = new Pen(Color.Red, 5);
            g.DrawPolygon(p, pts2);

            pictureBox1.Image = bitmap1;
        }

        private void button31_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            using (Font the_font = new Font("Times New Roman", 16))
            {
                // Draw without smoothing.
                int x = 30, y = 30;
                g.TextRenderingHint = TextRenderingHint.SingleBitPerPixelGridFit;
                g.DrawString("無 Smoothing", the_font, Brushes.Blue, x, y);
                y += 50;
                g.DrawImage(Properties.Resources.Smiley100x100, x, y, 50, 50);
                y += 100;
                g.DrawEllipse(Pens.Red, x, y, 100, 50);

                // Draw with smoothing.
                g.SmoothingMode = SmoothingMode.AntiAlias;
                g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                g.InterpolationMode = InterpolationMode.High;

                x = 180;
                y = 30;
                g.DrawString("有 Smoothing", the_font, Brushes.Blue, x, y);
                y += 50;
                g.DrawImage(Properties.Resources.Smiley100x100, x, y, 50, 50);
                y += 100;
                g.DrawEllipse(Pens.Red, x, y, 100, 50);
            }
            pictureBox1.Image = bitmap1;
        }

        private void button40_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

            Font f = new Font("標楷體", 16);
            SolidBrush sb = new SolidBrush(Color.Blue);
            Point pt = new Point();

            for (int size = 1; size <= 10; size++)
            {
                pt = new Point(100, 42 * size);
                g.DrawString(size.ToString(), f, sb, pt);

                pt = new Point(200, 42 * size);
                DrawPoint(g, pt, Color.Red, Color.Pink, 10);
            }
            pictureBox1.Image = bitmap1;
        }

        private void button41_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

            richTextBox1.Text += "畫一些空心圓\n";

            int radius = 80;
            int linewidth = 10;
            Point pt = new Point();

            pt = new Point(80, 80);
            DrawCircle(g, pt, radius, linewidth, Color.Red);

            pt = new Point(160, 160);
            DrawCircle(g, pt, radius, linewidth, Color.Green);

            pt = new Point(240, 240);
            DrawCircle(g, pt, radius, linewidth, Color.Blue);
            pictureBox1.Image = bitmap1;
        }

        private void button42_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

            richTextBox1.Text += "畫一些實心圓\n";

            int radius = 80;
            Point pt = new Point();

            pt = new Point(80 + 160, 80);
            FillCircle(g, pt, radius, Color.Red);

            pt = new Point(160 + 160, 160);
            FillCircle(g, pt, radius, Color.Green);

            pt = new Point(240 + 160, 240);
            FillCircle(g, pt, radius, Color.Blue);
            pictureBox1.Image = bitmap1;
        }

        private void button43_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

            richTextBox1.Text += "畫一些空心星形\n";

            int radius = 80;
            int linewidth = 5;
            Point pt = new Point();

            pt = new Point(100, 100);
            DrawStar(g, pt, radius, linewidth, Color.Red);
            pictureBox1.Image = bitmap1;
        }

        private void button44_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

            richTextBox1.Text += "畫一些實心星形\n";

            int radius = 80;
            Point pt = new Point();

            pt = new Point(100, 100);
            FillStar(g, pt, radius, Color.Red);
            pictureBox1.Image = bitmap1;
        }

        private void button35_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            //漸層色1
            // Define a brush with two points and their colors.
            using (LinearGradientBrush br = new LinearGradientBrush(new Point(10, 10), new Point(140, 50), Color.Red, Color.White))
            {
                g.FillRectangle(br, 10, 10, 125, 50);
                g.DrawRectangle(Pens.Black, 10, 10, 125, 50);
            }

            // Define a brush with a Rectangle, colors, and gradient mode.
            Rectangle rect = new Rectangle(145, 10, 125, 50);
            using (LinearGradientBrush br = new LinearGradientBrush(rect, Color.Blue, Color.White, LinearGradientMode.ForwardDiagonal))
            {
                g.FillRectangle(br, rect);
                g.DrawRectangle(Pens.Black, rect);
            }

            // Define a gradient with more than 2 colors.
            rect = new Rectangle(10, 70, 260, 50);
            using (LinearGradientBrush br = new LinearGradientBrush(rect, Color.Blue, Color.White, 0f))
            {
                // Create a ColorBlend object. Note that you
                // must initialize it before you save it in the
                // brush's InterpolationColors property.
                ColorBlend colorBlend = new ColorBlend();
                colorBlend.Colors = new Color[] 
                {
                    Color.Red,
                    Color.Orange,
                    Color.Yellow,
                    Color.Lime,
                    Color.Blue,
                    Color.Indigo,
                    Color.Violet,
                };
                colorBlend.Positions = new float[]
                {
                    0f, 1/6f, 2/6f, 3/6f, 4/6f, 5/6f, 1f
                };
                br.InterpolationColors = colorBlend;

                g.FillRectangle(br, rect);
                g.DrawRectangle(Pens.Black, rect);
            }

            //漸層色2
            //用漸變色填充
            //LinearGradientBrush：使用沿漸變混合的兩種顏色進行繪制
            rect = new Rectangle(0, 0, 500, 100);//定義矩形,參數為起點橫縱坐標以及其長和寬
            rect.Location = new Point(50, 300);
            LinearGradientBrush b = new LinearGradientBrush(rect, Color.Red, Color.Black, LinearGradientMode.Horizontal);
            g.FillRectangle(b, rect);

            //漸層色3
            int intLocation, intHeight;//定义两个int型的变量intLocation、intHeight 
            intLocation = this.ClientRectangle.Location.Y;//为变量intLocation赋值
            intHeight = this.ClientRectangle.Height / 200;//为变量intHeight赋值

            for (int i = 255; i >= 0; i--)
            {
                Color color = new Color();
                color = Color.FromArgb(1, i, 100);
                SolidBrush SBrush = new SolidBrush(color);
                Pen p = new Pen(SBrush, 1);
                g.DrawLine(p, 400, 30 + i, 500, 30 + i);
            }

            pictureBox1.Image = bitmap1;
        }

        private void button36_Click(object sender, EventArgs e)
        {

        }

        //在線的上下畫字
        private void button32_Click(object sender, EventArgs e)
        {
            // Draw some text along a line segment.
            Graphics g = pictureBox1.CreateGraphics();
            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.InterpolationMode = InterpolationMode.High;

            // Draw some text along some line segments.
            DrawOnSegment(g, new PointF(20, 20), new PointF(330, 150), "This is some text above a line segment.", true);
            DrawOnSegment(g, new PointF(20, 20), new PointF(330, 150), "This is some text below a line segment.", false);

            DrawOnSegment(g, new PointF(330, 200), new PointF(20, 120), "This is some text above a line segment.", true);
            DrawOnSegment(g, new PointF(330, 200), new PointF(20, 120), "This is some text below a line segment.", false);
        }

        // Draw some text.
        private void DrawOnSegment(Graphics gr, PointF start_point, PointF end_point, string txt, bool text_above_segment)
        {
            int start_ch = 0;

            gr.DrawLine(Pens.Green, start_point, end_point);
            DrawTextOnSegment(gr, Brushes.Blue, this.Font, txt,
                ref start_ch, ref start_point, end_point, text_above_segment);
        }

        // Draw some text along a line segment.
        // Leave char_num pointing to the next character to be drawn.
        // Leave start_point holding the last point used.
        private void DrawTextOnSegment(Graphics gr, Brush brush, Font font, string txt, ref int first_ch, ref PointF start_point, PointF end_point, bool text_above_segment)
        {
            float dx = end_point.X - start_point.X;
            float dy = end_point.Y - start_point.Y;
            float dist = (float)Math.Sqrt(dx * dx + dy * dy);
            dx /= dist;
            dy /= dist;

            // See how many characters will fit.
            int last_ch = first_ch;
            while (last_ch < txt.Length)
            {
                string test_string = txt.Substring(first_ch, last_ch - first_ch + 1);
                if (gr.MeasureString(test_string, font).Width > dist)
                {
                    // This is one too many characters.
                    last_ch--;
                    break;
                }
                last_ch++;
            }
            if (last_ch < first_ch) return;
            if (last_ch >= txt.Length) last_ch = txt.Length - 1;
            string chars_that_fit = txt.Substring(first_ch, last_ch - first_ch + 1);

            // Rotate and translate to position the characters.
            GraphicsState state = gr.Save();
            if (text_above_segment)
            {
                gr.TranslateTransform(0, -gr.MeasureString(chars_that_fit, font).Height, MatrixOrder.Append);
            }
            float angle = (float)(180 * Math.Atan2(dy, dx) / Math.PI);
            gr.RotateTransform(angle, MatrixOrder.Append);
            gr.TranslateTransform(start_point.X, start_point.Y, MatrixOrder.Append);

            // Draw the characters that fit.
            gr.DrawString(chars_that_fit, font, brush, 0, 0);

            // Restore the saved state.
            gr.Restore(state);

            // Update first_ch and start_point.
            first_ch = last_ch + 1;
            float text_width = gr.MeasureString(chars_that_fit, font).Width;
            start_point = new PointF(start_point.X + dx * text_width, start_point.Y + dy * text_width);
        }

        //在曲線的上下畫字
        private void button33_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();

            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.InterpolationMode = InterpolationMode.High;

            // Draw some text along some paths.
            GraphicsPath path = new GraphicsPath();
            path.AddArc(new RectangleF(40, 40, 320, 220), 180, 180);
            g.DrawPath(Pens.Green, path);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, true);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, false);

            path = new GraphicsPath();
            path.AddArc(new RectangleF(40, 50, 320, 220), 0, 180);
            g.DrawPath(Pens.Red, path);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, true);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, false);
        }

        // Draw some text along a GraphicsPath.
        private void DrawTextOnPath(Graphics gr, Brush brush, Font font, string txt, GraphicsPath path, bool text_above_path)
        {
            // Make a copy so we don't mess up the original.
            path = (GraphicsPath)path.Clone();

            // Flatten the path into segments.
            path.Flatten();

            // Draw characters.
            int start_ch = 0;
            PointF start_point = path.PathPoints[0];
            for (int i = 1; i < path.PointCount; i++)
            {
                PointF end_point = path.PathPoints[i];
                DrawTextOnSegment2(gr, brush, font, txt, ref start_ch,
                    ref start_point, end_point, text_above_path);
                if (start_ch >= txt.Length) break;
            }
        }

        // Draw some text along a line segment.
        // Leave char_num pointing to the next character to be drawn.
        // Leave start_point holding the coordinates of the last point used.
        private void DrawTextOnSegment2(Graphics gr, Brush brush, Font font, string txt, ref int first_ch, ref PointF start_point, PointF end_point, bool text_above_segment)
        {
            float dx = end_point.X - start_point.X;
            float dy = end_point.Y - start_point.Y;
            float dist = (float)Math.Sqrt(dx * dx + dy * dy);
            dx /= dist;
            dy /= dist;

            // See how many characters will fit.
            int last_ch = first_ch;
            while (last_ch < txt.Length)
            {
                string test_string = txt.Substring(first_ch, last_ch - first_ch + 1);
                if (gr.MeasureString(test_string, font).Width > dist)
                {
                    // This is one too many characters.
                    last_ch--;
                    break;
                }
                last_ch++;
            }
            if (last_ch < first_ch) return;
            if (last_ch >= txt.Length) last_ch = txt.Length - 1;
            string chars_that_fit = txt.Substring(first_ch, last_ch - first_ch + 1);

            // Rotate and translate to position the characters.
            GraphicsState state = gr.Save();
            if (text_above_segment)
            {
                gr.TranslateTransform(0,
                    -gr.MeasureString(chars_that_fit, font).Height,
                    MatrixOrder.Append);
            }
            float angle = (float)(180 * Math.Atan2(dy, dx) / Math.PI);
            gr.RotateTransform(angle, MatrixOrder.Append);
            gr.TranslateTransform(start_point.X, start_point.Y, MatrixOrder.Append);

            // Draw the characters that fit.
            gr.DrawString(chars_that_fit, font, brush, 0, 0);

            // Restore the saved state.
            gr.Restore(state);

            // Update first_ch and start_point.
            first_ch = last_ch + 1;
            float text_width = gr.MeasureString(chars_that_fit, font).Width;
            start_point = new PointF(
                start_point.X + dx * text_width,
                start_point.Y + dy * text_width);

        }




    }
}
