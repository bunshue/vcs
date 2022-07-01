using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for LinearGradientBrush, GraphicsPath, GraphicsState
using System.Drawing.Text;      //for TextRenderingHint

namespace vcs_Draw1
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        Font f;

        bool flag_print_mouse_cursor = false;

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

            pictureBox_uac.Image = UacStuff.GetUacShieldImage();
            // Add the shield to a button.
            UacStuff.AddShieldToButton(button29);

            DrawPictureBoxText();
        }

        protected override void OnPaintBackground(PaintEventArgs e)
        {
            int x_st = this.ClientRectangle.X;
            int y_st = this.ClientRectangle.Y;
            int W = this.ClientRectangle.Width;
            int H = this.ClientRectangle.Height;

            e.Graphics.FillRectangle(new SolidBrush(Color.White), x_st, y_st, W, H);

            e.Graphics.DrawEllipse(new Pen(Color.Green, 10), x_st + W - 500, y_st + H - 150, 300, 100);

            e.Graphics.DrawString("OnPaintBackground", new Font("標楷體", 30), new SolidBrush(Color.Red), 50, y_st + H - 90);
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

            pictureBox_uac.Location = new Point(x_st + dx * 0 - 100, y_st + dy * 0);
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

            button50.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button51.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button52.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button53.Location = new Point(x_st + dx * 3, y_st + dy * 10);
            button54.Location = new Point(x_st + dx * 4, y_st + dy * 10);

            button55.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            button56.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            button57.Location = new Point(x_st + dx * 2, y_st + dy * 11);
            button58.Location = new Point(x_st + dx * 3, y_st + dy * 11);
            button59.Location = new Point(x_st + dx * 4, y_st + dy * 11);

            bt_eraser.Location = new Point(x_st + dx * 2, y_st + dy * 12);
            bt_reset.Location = new Point(x_st + dx * 3, y_st + dy * 12);
            bt_save.Location = new Point(x_st + dx * 4, y_st + dy * 12);

            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            checkBox1.Location = new Point(x_st + dx * 1, y_st + dy * 12);

            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y + 80);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            pictureBox1.Location = new Point(20, 20);

            y_st = 800;
            panel1.Size = new Size(200, 100);
            panel1.Location = new Point(850, y_st);
            //panel1.BackColor = Color.Lime;

            pictureBox_text.Location = new Point(50, y_st + 150 - 30);

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
            SolidBrush sb = new SolidBrush(c);

            // Fill the circle
            g.FillEllipse(sb, new RectangleF(center.X - radius, center.Y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            sb.Dispose();
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
            //繪圖圖形的Contains功能
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawRectangle(Pens.Red, 100, 100, 150, 150);
            Rectangle rec = new Rectangle(100, 100, 150, 150);
            Point pt1 = new Point(180, 180);
            Point pt2 = new Point(280, 280);
            g.FillEllipse(Brushes.Green, pt1.X, pt1.Y, 20, 20);
            g.FillEllipse(Brushes.Red, pt2.X, pt2.Y, 20, 20);

            if (rec.Contains(pt1))
            {
                richTextBox1.Text += "pt1 在 rec 之內\n";
            }
            else
            {
                richTextBox1.Text += "pt1 在 rec 之外\n";
            }

            if (rec.Contains(pt2))
            {
                richTextBox1.Text += "pt2 在 rec 之內\n";
            }
            else
            {
                richTextBox1.Text += "pt2 在 rec 之外\n";
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            open_new_file();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
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
            pictureBox1.Location = new Point(20, 20);

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
            pictureBox1.Location = new Point(20, 20);

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
            pictureBox1.Location = new Point(20, 20);

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

            richTextBox1.Text += "反鋸齒功能\n";
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

            richTextBox1.Text += "有 無 Smoothing 比較\n";
            using (Font the_font = new Font("Times New Roman", 16))
            {
                // Draw without smoothing.
                int x = 30, y = 240;
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
                y = 240;
                g.DrawString("有 Smoothing", the_font, Brushes.Blue, x, y);
                y += 50;
                g.DrawImage(Properties.Resources.Smiley100x100, x, y, 50, 50);
                y += 100;
                g.DrawEllipse(Pens.Red, x, y, 100, 50);
            }

            //畫示意圖
            string filename = @"C:\______test_files\_material\AntiAlias.jpg";
            //讀檔 至 Image 影像
            Image img = Image.FromFile(filename); // 產生一個Image物件
            //畫出來
            g.DrawImage(img, 300, 380, img.Width / 2, img.Height / 2);

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
            Brush bb = new SolidBrush(Color.Red);
            string ct = "小熊家族";

            int x = bitmap1.Width - 200;
            int y = bitmap1.Height - 50;

            g.DrawString(ct, f, b, x, y);
            g.DrawString(ct, f, bb, x - 1, y - 1);
            g.DrawString(ct, f, bb, x - 1, y + 1);
            g.DrawString(ct, f, bb, x + 1, y - 1);
            g.DrawString(ct, f, bb, x + 1, y + 1);
            g.DrawString(ct, f, b, x, y);

            pictureBox1.Image = bitmap1;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            int width = 1920;
            int height = 1080;

            richTextBox1.Text += "FullHD點圖 ST\n";

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(20, 20);

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

            richTextBox1.Text += "FullHD點圖 SP\n";
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
            pictureBox1.Location = new Point(20, 20);

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
            pictureBox1.Location = new Point(20, 20);
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
            pictureBox1.Location = new Point(20, 20);

            pictureBox1.Image = bitmap1;
            richTextBox1.Text += "\n";

            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化
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

            if (flag_print_mouse_cursor == true)
            {
                Graphics myGraphics = this.CreateGraphics();
                Cursor.Draw(myGraphics, new Rectangle(e.X, e.Y, 10, 10));
            }
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
            if (button19.Text == "在Form上印出滑鼠游標形狀")
            {
                flag_print_mouse_cursor = true;
                this.Cursor = Cursors.Hand;
                button19.Text = "停止印出滑鼠游標形狀";
            }
            else
            {
                flag_print_mouse_cursor = false;
                this.Cursor = Cursors.Default;
                button19.Text = "在Form上印出滑鼠游標形狀";
            }
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
            //畫貝茲線
            Graphics g = this.pictureBox1.CreateGraphics();
            Pen p = new Pen(Color.Red, 5);
            float startX = 50.0F;
            float startY = 80.0F;
            float controlX1 = 150.0F;
            float controlY1 = 20.0F;
            float controlX2 = 230.0F;
            float controlY2 = 50.0F;
            float endX = 190.0F;
            float endY = 80.0F;
            g.DrawBezier(p, startX, startY, controlX1, controlY1, controlX2, controlY2, endX, endY);
            //4個Point點分別表示起始點、第一個控制點、第二個控制點和結束點。
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //DrawCurve

            pictureBox1.Size = new Size(500, 500);

            Graphics g = this.pictureBox1.CreateGraphics();
            Pen p1 = new Pen(Color.Red, 2);
            Pen p2 = new Pen(Color.Green, 2);
            Pen p3 = new Pen(Color.Blue, 2);
            Pen p4 = new Pen(Color.Gold, 2);
            Pen p5 = new Pen(Color.Black, 2);
            Point pt1 = new Point(200, 100);
            Point pt2 = new Point(300, 100);
            Point pt3 = new Point(400, 200);
            Point pt4 = new Point(300, 300);
            Point pt5 = new Point(200, 300);
            Point pt6 = new Point(100, 200);
            Point[] pts = { pt1, pt2, pt3, pt4, pt5, pt6 };
            g.DrawCurve(p1, pts, 1.0F); //使用tension
            g.DrawCurve(p2, pts);   //不使用tension
            g.DrawPolygon(p3, pts);

            g.DrawLines(p4, pts);
        }

        private void button26_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }
            DrawSmileImage(g);
        }

        private void DrawSmileImage(Graphics g)
        {
            Rectangle rect;

            rect = new Rectangle(10, 10, 80, 80);
            g.FillEllipse(Brushes.LightGreen, rect);
            g.DrawEllipse(Pens.Green, rect);

            rect = new Rectangle(40, 40, 20, 30);
            g.FillEllipse(Brushes.LightBlue, rect);
            g.DrawEllipse(Pens.Blue, rect);

            rect = new Rectangle(25, 30, 50, 50);
            g.DrawArc(Pens.Red, rect, 20, 140);

            rect = new Rectangle(25, 25, 15, 20);
            g.FillEllipse(Brushes.White, rect);
            g.DrawEllipse(Pens.Black, rect);
            rect = new Rectangle(30, 30, 10, 10);
            g.FillEllipse(Brushes.Black, rect);

            rect = new Rectangle(60, 25, 15, 20);
            g.FillEllipse(Brushes.White, rect);
            g.DrawEllipse(Pens.Black, rect);
            rect = new Rectangle(65, 30, 10, 10);
            g.FillEllipse(Brushes.Black, rect);
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
            int x_st = 1000;
            int y_st = 100;

            Graphics g = e.Graphics; //創建畫板,這裡的畫板是由Form提供的.
            Pen p = new Pen(Color.Blue, 2);//定義了一個藍色,寬度為的畫筆
            g.DrawLine(p, x_st + 10, y_st + 10, x_st + 110, y_st + 110);//在畫板上畫直線,起始坐標為(10,10),終點坐標為(110,110)   //平移 (1000,100)
            g.DrawRectangle(p, x_st + 10, y_st + 10, 100, 100);//在畫板上畫矩形,起始坐標為(10,10),寬為100, 高為100
            g.DrawEllipse(p, x_st + 10, y_st + 10, 100, 100);//在畫板上畫橢圓,起始坐標為(10,10),外接矩形的寬為100, 高為100

            // Make a rectangle.
            Rectangle rect1 = new Rectangle(20, 20, this.ClientSize.Width - 40, this.ClientSize.Height - 40);

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
                e.Graphics.DrawRectangle(the_pen, rectf.X, rectf.Y, rectf.Width, rectf.Height);

                the_pen.Color = Color.Blue;
                the_pen.Width = 1;
                e.Graphics.DrawRectangle(the_pen, rect2);
            }

            //表單底部畫字 ST
            // Transform.
            e.Graphics.ScaleTransform(1.5f, 1.5f, MatrixOrder.Append);
            e.Graphics.RotateTransform(25, MatrixOrder.Append);
            e.Graphics.TranslateTransform(80, 30, MatrixOrder.Append);

            x_st = 260;
            y_st = 0;
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
            Bitmap bm = new Bitmap(pictureBox_text.ClientSize.Width, pictureBox_text.ClientSize.Height);
            using (Graphics g = Graphics.FromImage(bm))
            {
                g.Clear(Color.White);

                // Don't use TextRenderingHint.AntiAliasGridFit.
                g.TextRenderingHint = TextRenderingHint.AntiAlias;

                // Make a font to use.
                using (Font font = new Font("Times New Roman", 16, FontStyle.Regular))
                {
                    // Draw the text.
                    DrawTextInBoxes(g, font, 4, 4,
                        "When in the course of human events it " +
                        "becomes necessary for the quick brown " +
                        "fox to jump over the lazy dog...");
                }
            }

            // Display the result.
            pictureBox_text.Image = bm;
        }

        // Draw a sample and its name.
        private void DrawIconSample(Graphics g, ref int x, int y, Icon ico, string ico_name)
        {
            g.DrawIconUnstretched(ico, new Rectangle(x, y, ico.Width, ico.Height));
            int text_y = y + (int)(ico.Height - g.MeasureString(ico_name, this.Font).Height) / 2;
            g.DrawString(ico_name, this.Font, Brushes.Black, x + ico.Width + 5, text_y);
            x += column_width;
        }

        // Draw a long string with boxes around each character.
        private void DrawTextInBoxes(Graphics g, Font font, float start_x, float start_y, string text)
        {
            // Measure the characters.
            List<RectangleF> rects = MeasureCharacters(g, font, text);

            for (int i = 0; i < text.Length; i++)
            {
                g.DrawRectangle(Pens.Red, start_x + rects[i].Left, start_y + rects[i].Top, rects[i].Width, rects[i].Height);
            }
            g.DrawString(text, font, Brushes.Blue, start_x, start_y);
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
        private List<RectangleF> MeasureCharactersInWord(Graphics gr, Font font, string text)
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
                Region[] regions = gr.MeasureCharacterRanges(text, font, this.ClientRectangle, string_format);

                // Convert the regions into rectangles.
                foreach (Region region in regions)
                {
                    result.Add(region.GetBounds(gr));
                }
            }
            return result;
        }
        #endregion

        private void button29_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "就是 Button 上的 UAC圖示\n";
        }

        private void button30_Click(object sender, EventArgs e)
        {
            //clone範例
            /*
            在Bitmap中可以找到

            Clone（）方法，該方法有三個重載方法。
            Clone（）
            Clone（Rectangle， PixelFormat）
            Clone（RectangleF， PixelFormat）
            */

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = new Bitmap(filename);

            Bitmap bitmap2 = (Bitmap)bitmap1.Clone();

            int w = bitmap1.Width;
            int h = bitmap1.Height;
            Rectangle rect = new Rectangle(w / 2, h / 2, w / 2, h / 2);

            //Bitmap bitmap3 = (Bitmap)bitmap1.Clone(rect, PixelFormat.Format32bppArgb);    //same
            Bitmap bitmap3 = (Bitmap)bitmap1.Clone(rect, bitmap1.PixelFormat);

            pictureBox1.Image = bitmap3;
        }

        private void button31_Click(object sender, EventArgs e)
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
        private void DrawOnSegment(Graphics g, PointF start_point, PointF end_point, string txt, bool text_above_segment)
        {
            int start_ch = 0;

            g.DrawLine(Pens.Green, start_point, end_point);
            DrawTextOnSegment(g, Brushes.Blue, this.Font, txt, ref start_ch, ref start_point, end_point, text_above_segment);
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

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
            //在Button上畫圖
            richTextBox1.Text += "在Button上畫圖, 要改buttonXX_Paint()\n";
        }

        private void button34_Paint(object sender, PaintEventArgs e)
        {
            int W = button34.Width;
            int H = button34.Height;
            //e.Graphics.FillRectangle(new SolidBrush(Color.White), x_st, y_st, W, H);
            e.Graphics.FillRectangle(new SolidBrush(Color.Pink), 0, 0, W, H);

            Pen p = new Pen(Color.Red, 6);
            e.Graphics.DrawRectangle(p, 0, 0, W - 0, H - 0);

            e.Graphics.DrawString("在Button上畫圖", new Font("標楷體", 11), new SolidBrush(Color.Blue), 5, 15);
        }

        private void button35_Click(object sender, EventArgs e)
        {
            //透明色測試
            richTextBox1.Text += "R = " + Color.Transparent.R.ToString() + "\n";
            richTextBox1.Text += "G = " + Color.Transparent.G.ToString() + "\n";
            richTextBox1.Text += "B = " + Color.Transparent.B.ToString() + "\n";
            richTextBox1.Text += "A = " + Color.Transparent.A.ToString() + "\n";
            richTextBox1.Text += "A2 = " + Color.Red.A.ToString() + "\n";


            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            g = Graphics.FromImage(bitmap1);



            //清空畫布並用透明色填充
            //g.Clear(Color.Transparent);


            Color c1 = Color.FromArgb(255, 255, 0, 0);
            SolidBrush sb1 = new SolidBrush(c1);
            g.FillRectangle(sb1, 50, 50, 100, 100);

            Color c2 = Color.FromArgb(255, 0, 255, 0);
            SolidBrush sb2 = new SolidBrush(c2);
            g.FillRectangle(sb2, 100, 50, 100, 100);


            Color c3 = Color.FromArgb(255, 255, 0, 0);
            SolidBrush sb3 = new SolidBrush(c3);
            g.FillRectangle(sb3, 50, 200, 100, 100);

            Color c4 = Color.FromArgb(128, 0, 255, 0);
            SolidBrush sb4 = new SolidBrush(c4);
            g.FillRectangle(sb4, 100, 200, 100, 100);


            //g.FillRectangle(Brushes.Blue, 00, 320, 600, 50);
            //g.FillRectangle(Brushes.Blue, 00, 420, 600, 50);
            /*
            int i;
            int w = 40;
            for (i = 0; i < 13; i++)
            {
            Color c5 = Color.FromArgb(255, 20 * i, 0, 0);
            SolidBrush sb5 = new SolidBrush(c5);
            g.FillRectangle(sb5, 50 + w * i, 300, w, 100);

            }
            for (i = 0; i < 13; i++)
            {
            Color c5 = Color.FromArgb(20 * i, 255, 0, 0);
            SolidBrush sb5 = new SolidBrush(c5);
            g.FillRectangle(sb5, 50 + w * i, 400, w, 100);

            }
            */

            Color c6 = Color.FromArgb(200, 255, 255, 255);
            SolidBrush sb5 = new SolidBrush(c6);
            g.FillRectangle(sb5, 300, 100, 100, 100);


            //g.DrawString("格子裏", new Font("黑體", 20), new SolidBrush(c6), 200, 100);
            g.DrawString("格子裏", new Font("黑體", 20), new SolidBrush(Color.Black), 200, 100);


            g.DrawRectangle(Pens.Red, 100, 100, 100, 100);
            
            
            pictureBox1.Image = bitmap1;

        }

        private void button36_Click(object sender, EventArgs e)
        {
            //Rectangle的交集與聯集

            Graphics g = pictureBox1.CreateGraphics();

            Rectangle rect1 = new Rectangle(30, 30, 150, 150);
            g.FillRectangle(Brushes.Green, rect1); //綠色矩形區塊 固定 畫綠色

            Rectangle rect2 = new Rectangle(120, 120, 150, 150);
            g.FillRectangle(Brushes.Red, rect2); //紅色矩形區塊 依滑鼠位置變化 畫紅色

            Rectangle union = Rectangle.Union(rect1, rect2); //聯集區域
            g.DrawRectangle(Pens.Black, union);                   //聯集 畫 黑色框

            Rectangle intersect = Rectangle.Intersect(rect1, rect2); //交集區域
            g.FillRectangle(Brushes.Yellow, intersect);    //交集 畫黃色
        }

        private void button37_Click(object sender, EventArgs e)
        {
        }

        private void button38_Click(object sender, EventArgs e)
        {
            //為此Button畫陰影
            int len = 7;    //陰影長度
            Graphics ag = this.CreateGraphics();
            for (int i = 0; i < len; i++)
            {
                Point p1 = new Point();
                p1.X = button38.Left - i;
                p1.Y = button38.Top + button38.Height + i;
                Point p2 = new Point();
                p2.X = button38.Left + button38.Width + i;
                p2.Y = button38.Top + button38.Height + i;
                ag.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }
            for (int i = 0; i < len; i++)
            {
                Point p1 = new Point();
                p1.X = button38.Left + button38.Width + i;
                p1.Y = button38.Top - i;
                Point p2 = new Point();
                p2.X = button38.Left + button38.Width + i;
                p2.Y = button38.Top + button38.Height + i;
                ag.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }
        }

        private void button39_Click(object sender, EventArgs e)
        {
            //為此Button畫投影
            int len = 7;    //投影長度
            Graphics ag = this.CreateGraphics();
            for (int i = 0; i < len; i++)
            {
                Point p1 = new Point();
                p1.X = button39.Left - i;
                p1.Y = button39.Top;
                Point p2 = new Point();
                p2.X = button39.Left + i;
                p2.Y = button39.Top + button39.Height + i;
                ag.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }
            for (int i = 0; i < len; i++)
            {
                Point p1 = new Point();
                p1.X = button39.Left - i;
                p1.Y = button39.Top - i;
                Point p2 = new Point();
                p2.X = button39.Left + button39.Width + i;
                p2.Y = button39.Top + i;
                ag.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }
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
            Point center = new Point(100, 100);
            DrawStar(g, center, radius, linewidth, Color.Red);
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
            Point center = new Point(100, 100);
            FillStar(g, center, radius, Color.Red);
            pictureBox1.Image = bitmap1;
        }

        //基本畫圖1
        private void button45_Click(object sender, EventArgs e)
        {
            int W = 1100;
            int H = 750;
            if (bitmap1 == null)
            {
                open_new_file();
            }
            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
            pictureBox1.Location = new Point(20, 20);

            //基本畫圖

            p = new Pen(Color.Green, 3);
            sb = new SolidBrush(Color.Blue);
            f = new Font("Times New Roman", 14);

            Rectangle rec;
            Rectangle[] recs;

            int x_st = 20;
            int y_st = 20;
            int dx = 100;
            int dy = 80;
            int w = 80;
            int h = 60;

            //空長方形
            x_st = 20;
            y_st = 20;
            g.DrawString("DrawRectangle", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            g.DrawRectangle(p, x_st, y_st, w, h);

            x_st += dx;
            rec = new Rectangle(x_st, y_st, w, h);
            g.DrawRectangle(p, rec);

            x_st += dx;
            g.DrawRectangle(new Pen(Color.Lime), new Rectangle(x_st, y_st, w, h));


            //填滿長方形
            x_st = W / 2;
            y_st = 20;
            g.DrawString("FillRectangle", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            g.FillRectangle(sb, x_st, y_st, w, h);

            x_st += dx;
            rec = new Rectangle(x_st, y_st, w, h);
            g.FillRectangle(sb, rec);

            x_st += dx;
            g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x_st, y_st, w, h));


            //空長方形多個
            x_st = 20;
            y_st = 20;
            y_st += dy;
            g.DrawString("DrawRectangles", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            recs = new Rectangle[4] {
	            new Rectangle(x_st+0, y_st+0, 50, 80),
	            new Rectangle(x_st+60, y_st+0, 80, 60),
	            new Rectangle(x_st+60+90, y_st+0, 100, 75),
	            new Rectangle(x_st+60+90+110, y_st+0, 50, 70)
            };
            g.DrawRectangles(p, recs);


            //填滿長方形多個
            x_st = W / 2;
            y_st = 20;
            y_st += dy;
            g.DrawString("FillRectangles", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            recs = new Rectangle[4] {
	            new Rectangle(x_st+0, y_st+0, 50, 80),
	            new Rectangle(x_st+60, y_st+0, 80, 60),
	            new Rectangle(x_st+60+90, y_st+0, 100, 75),
	            new Rectangle(x_st+60+90+110, y_st+0, 50, 70)
            };
            g.FillRectangles(sb, recs);


            //空橢圓形
            x_st = 20;
            y_st = 20;
            y_st += dy * 2;
            g.DrawString("DrawEllipse", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            g.DrawEllipse(p, x_st, y_st, w, h);

            x_st += dx;
            rec = new Rectangle(x_st, y_st, w, h);
            g.DrawEllipse(p, rec);

            x_st += dx;
            g.DrawEllipse(new Pen(Color.Lime), new Rectangle(x_st, y_st, w, h));


            //填滿橢圓形
            x_st = W / 2;
            y_st = 20;
            y_st += dy * 2;
            g.DrawString("FillEllipse", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            g.FillEllipse(sb, x_st, y_st, w, h);

            x_st += dx;
            rec = new Rectangle(x_st, y_st, w, h);
            g.FillEllipse(sb, rec);

            x_st += dx;
            g.FillEllipse(new SolidBrush(Color.Lime), new Rectangle(x_st, y_st, w, h));


            //空多邊形
            x_st = 20;
            y_st = 20;
            y_st += dy * 3;
            g.DrawString("DrawPolygon", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;

            Point[] points1 = new Point[3];
            points1[0] = new Point(x_st + 0, y_st + 0);
            points1[1] = new Point(x_st + 0, y_st + 50);
            points1[2] = new Point(x_st + 100, y_st + 50);
            g.DrawPolygon(p, points1);

            x_st += dx;
            Point[] points2 = { 
                new Point(x_st+0, y_st+0),
                new Point(x_st+200, y_st+20),
                new Point(x_st+200, y_st+60),
                new Point(x_st+150, y_st+20),
                new Point(x_st+20, y_st+60) };
            g.DrawPolygon(Pens.Red, points2);


            //填滿多邊形
            x_st = W / 2;
            y_st = 20;
            y_st += dy * 3;
            g.DrawString("FillPolygon", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;

            Point[] points3 = new Point[3];
            points3[0] = new Point(x_st + 0, y_st + 0);
            points3[1] = new Point(x_st + 0, y_st + 50);
            points3[2] = new Point(x_st + 100, y_st + 50);
            g.FillPolygon(sb, points3);

            x_st += dx;
            Point[] points4 = { 
                new Point(x_st+0, y_st+0),
                new Point(x_st+200, y_st+20),
                new Point(x_st+200, y_st+60),
                new Point(x_st+150, y_st+20),
                new Point(x_st+20, y_st+60) };
            g.FillPolygon(new SolidBrush(Color.Red), points4);

            //空派形
            x_st = 20;
            y_st = 20;
            y_st += dy * 4;
            g.DrawString("DrawPie", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            g.DrawPie(p, x_st, y_st, w, h, 0, 30);

            x_st += dx;
            g.DrawPie(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h), 180, 30);

            x_st += dx / 2;
            g.DrawPie(p, x_st, y_st, w, h, 0, -30);

            x_st += dx;
            g.DrawPie(p, x_st, y_st - 20, w, w, 40, 280);


            //填滿派形
            x_st = W / 2;
            y_st = 20;
            y_st += dy * 4;
            g.DrawString("FillPie", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            g.FillPie(sb, x_st, y_st, w, h, 0, 30);

            x_st += dx;
            g.FillPie(new SolidBrush(Color.Red), new Rectangle(x_st, y_st, w, h), 180, 30);

            x_st += dx / 2;
            g.FillPie(sb, x_st, y_st, w, h, 0, -30);

            x_st += dx;
            g.FillPie(sb, x_st, y_st - 20, w, w, 40, 280);


            //畫分佈餅圖
            x_st = W - 180;
            y_st = H - 180;
            int r = 100;
            Brush bb = new SolidBrush(Color.Navy);
            g.FillPie(bb, x_st, y_st, r, r, 0, 90);
            //畫個Pie，顏色是Pink,位置的x、y在50，大小為r*r，角度為從0度開始，畫90度

            bb = new SolidBrush(Color.Green);
            g.FillPie(bb, x_st, y_st, r, r, 90, 135);
            //畫個Pie，顏色是Green,位置大小同上，角度為接著從90度開始，畫135度

            bb = new SolidBrush(Color.Purple);
            g.FillPie(bb, x_st, y_st, r, r, 225, 135);
            //畫個Pie，顏色是Purple,位置大小同上，角度為接著從90+135=225度開始 畫135度
            //如此，這3個pie就會合成一個圓


            //畫直線
            x_st = 20;
            y_st = 20;
            y_st += dy * 5;
            g.DrawString("DrawLine", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            Point point1a = new Point(x_st, y_st);
            Point point2a = new Point(x_st + 100, y_st + 50);
            g.DrawLine(p, point1a, point2a);

            Point point3a = new Point(x_st, y_st + 50);
            Point point4a = new Point(x_st + 100, y_st);
            g.DrawLine(p, point3a, point4a);


            //畫直線連線與曲線
            x_st += dx * 3 / 2;

            g.DrawString("DrawLines", f, new SolidBrush(Color.Red), new PointF(x_st, y_st));
            g.DrawString("DrawCurve", f, new SolidBrush(Color.Green), new PointF(x_st, y_st + 50));

            x_st += dx;
            // Create points that define curve.
            Point point0 = new Point(x_st + 0, y_st + 0);
            Point point1 = new Point(x_st + 50, y_st + 150);
            Point point2 = new Point(x_st + 100, y_st - 50);
            Point point3 = new Point(x_st + 150, y_st + 120);
            Point point4 = new Point(x_st + 200, y_st - 20);
            Point point5 = new Point(x_st + 250, y_st + 150);
            Point point6 = new Point(x_st + 300, y_st - 20);
            Point point7 = new Point(x_st + 350, y_st + 50);
            Point point8 = new Point(x_st + 400, y_st + 0);
            Point point9 = new Point(x_st + 450, y_st + 150);
            Point point10 = new Point(x_st + 500, y_st + 0);
            Point point11 = new Point(x_st + 550, y_st + 150);
            Point point12 = new Point(x_st + 600, y_st + 50);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12 };

            Pen redPen = new Pen(Color.Red, 3); // Create pens.
            g.DrawLines(redPen, curvePoints);   //畫直線

            Pen greenPen = new Pen(Color.Green, 3); // Create pens.
            g.DrawCurve(greenPen, curvePoints); //畫曲線

            x_st = 670;
            y_st = 530;
            g.DrawString("Sine", f, new SolidBrush(Color.Red), new PointF(x_st, y_st));

            /*
            Point[] pts = new Point[90];
            double yy;
            int i;
            for (i = 0; i < 90; i++)
            {
                yy = Math.Sin(Math.PI * i * 4 / 180) * 50;
                pts[i].X = x_st + (int)i * 1;
                pts[i].Y = y_st + (int)yy;
                //richTextBox1.Text += "x= " + pts[i].X.ToString() + " y = " + pts[i].Y.ToString() + "\n";
            }
            p = new Pen(Color.Navy, 3);
            g.DrawCurve(p, pts);
            */

            //畫三角函數
            int omega = 60;  //angular frequency
            Point[] pts = new Point[360 / omega + 1];    //一維Point陣列內有100個Point
            int i;
            int amplitude = 50;
            for (i = 0; i <= 360 / omega; i++)
            {
                pts[i].X = x_st + i * omega / 3;
                pts[i].Y = y_st - (int)(amplitude * Math.Sin(i * omega * Math.PI / 180));   //Y反相
                g.FillEllipse(Brushes.Black, pts[i].X - 3, pts[i].Y - 3, 6, 6); //畫點
            }
            g.DrawLines(new Pen(Brushes.Red, 1), pts);      //畫直線, 直接把Point陣列畫出來
            g.DrawCurve(new Pen(Brushes.Blue, 1), pts);     //畫曲線, 直接把Point陣列畫出來


            //各種連線
            x_st = 50;
            y_st = 20;
            y_st += dy * 6;
            w = 100;
            h = 100;

            Point[] pa = { new Point(x_st, y_st), new Point(x_st, y_st + h), new Point(x_st + w, y_st + h), new Point(x_st + w, y_st), new Point(x_st + w * 2, y_st), new Point(x_st + w * 2, y_st + h), new Point(x_st + w * 3, y_st + h / 2) };

            p = new Pen(Color.Red, 5);
            g.DrawLines(p, pa);  //陣列的連線

            p = new Pen(Color.LightCoral, 1);
            for (float k = 0; k < 1.5; k += 0.4F)
            {
                g.DrawCurve(p, pa, k);  //DrawCurve 加上 屈度
            }

            p = new Pen(Color.Red, 1);
            g.DrawCurve(p, pa);     ////DrawCurve 預設屈度

            p = new Pen(Color.Yellow, 1);
            g.DrawClosedCurve(p, pa);       //頭尾相連 加上 屈度


            //畫弧線
            x_st = 20;
            y_st = 20;
            y_st += dy * 8;
            g.DrawString("DrawArc", f, sb, new PointF(x_st, y_st));

            y_st -= dy / 2;

            x_st += dx * 1;
            p = new Pen(Color.Red, 5);
            g.DrawEllipse(p, x_st, y_st, 150, 100);
            g.DrawArc(new Pen(Color.Blue, 10), new Rectangle(x_st, y_st, 150, 100), 0, 135);

            x_st += dx * 2;
            p = new Pen(Color.Red, 5);
            g.DrawEllipse(p, x_st, y_st, 150, 100);
            p = new Pen(Color.Blue, 10);
            p.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            g.DrawArc(p, x_st, y_st, 150, 100, 0, 135);

            x_st += dx * 2;
            p = new Pen(Color.Red, 5);
            g.DrawEllipse(p, x_st, y_st, 150, 100);
            p = new Pen(Color.Blue, 10);
            p.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            g.DrawArc(p, x_st, y_st, 150, 100, 0, -135);


            //畫字
            // Create string to draw.
            String drawString = "各種畫圖範例";

            // Create font and brush.
            Font drawFont = new Font("標楷體", 36, FontStyle.Italic | FontStyle.Underline | FontStyle.Strikeout);
            SolidBrush drawBrush = new SolidBrush(Color.Navy);

            // Create point for upper-left corner of drawing.
            PointF drawPoint = new PointF(W - 400, H - 70);

            // Draw string to screen.
            g.DrawString(drawString, drawFont, drawBrush, drawPoint);

            drawPoint = new PointF(W - 400, H - 70 - 50);
            g.DrawString(drawString, new Font("標楷體", 24, FontStyle.Bold | FontStyle.Italic), new SolidBrush(Color.Navy), drawPoint);
            //畫字就比較簡單了，會產生一個標楷體，24的大小，粗加斜，顏色為bb，位置在drawPoint


            //貼圖
            g.DrawString("貼圖", new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(W - 80, 30));
            Bitmap bmp = new Bitmap(@"C:\______test_files\__pic\_ball\red-ball-icon.png");
            for (y_st = 60; y_st < H; y_st += 80)
            {
                g.DrawImage(bmp, W - 75, y_st);
            }

            // 剛好等寬畫滿邊框
            p = new Pen(Color.Green, 10);
            g.DrawRectangle(p, 0 + p.Width / 2, 0 + p.Width / 2, bitmap1.Width - p.Width, bitmap1.Height - p.Width);
        }

        //基本畫圖2
        private void button46_Click(object sender, EventArgs e)
        {
            int W = 1100;
            int H = 750;
            if (bitmap1 == null)
            {
                open_new_file();
            }
            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
            pictureBox1.Location = new Point(20, 20);

            //基本畫圖

            p = new Pen(Color.Green, 3);
            sb = new SolidBrush(Color.Blue);
            f = new Font("Times New Roman", 14);

            //Rectangle rec;
            //Rectangle[] recs;

            int x_st = 20;
            int y_st = 20;
            int dx = 100;
            int dy = 80;
            int w = 80;
            int h = 60;



            //貝茲線
            x_st = 20;
            y_st = 20;
            g.DrawString("DrawBezier", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;

            Point[] points = new Point[4];
            points[0] = new Point(x_st + 0, y_st + 0);
            points[1] = new Point(x_st + 0, y_st + h);
            points[2] = new Point(x_st + w * 2, y_st + h);
            points[3] = new Point(x_st + w * 2, y_st + 0);

            g.DrawBezier(new Pen(Color.Black), points[0], points[1], points[2], points[3]);
            g.DrawLines(Pens.Red, points);

            for (int i = 0; i < 4; i++)
            {
                points[i] = new Point(points[i].X + dx * 2, points[i].Y);
            }
            g.DrawBeziers(new Pen(Color.Black), points);
            g.DrawLines(Pens.Red, points);



            //組合路徑
            x_st = 20;
            y_st = 20;
            y_st += dy;
            g.DrawString("DrawPath", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;

            GraphicsPath gp1 = new GraphicsPath();
            gp1.AddLine(new Point(x_st + 0, y_st + 0), new Point(x_st + w, y_st + h));
            gp1.AddLine(new Point(x_st + 0, y_st + h), new Point(x_st + w, y_st + 0));
            gp1.AddRectangle(new Rectangle(x_st + w, y_st - 10, w, h));
            p = new Pen(Color.Red, 3);
            g.DrawPath(new Pen(Color.Red), gp1);

            x_st += dx * 2;
            gp1.Reset();
            gp1.AddLine(x_st + 0, y_st + 0, x_st + 50, y_st + 50);
            gp1.AddEllipse(x_st + 50, y_st + 0, 100, 100);
            gp1.AddBezier(x_st + 50 + 100, y_st + 50, x_st + 200, 0, x_st + 300, 180, x_st + 400, 20);
            p = new Pen(Color.Green, 3);
            g.DrawPath(p, gp1);


            x_st += dx * 3;
            GraphicsPath gp2 = new GraphicsPath();  // Create a GraphicsPath object.

            Point[] pa = {
                    new Point(x_st+0, y_st+0), 
                    new Point(x_st+0, y_st+100), 
                    new Point(x_st+100, y_st+100),
                    new Point(x_st+100, y_st+0)
                                   };

            gp2.AddArc(x_st + 100, y_st + 0, 100, 100, 180, 180);
            gp2.StartFigure();
            gp2.AddCurve(pa);
            gp2.AddPie(x_st + 100 + 50, y_st + 0, 100, 100, 40, 110);
            g.DrawPath(p, gp2);

            //填滿組合路徑
            x_st = 20;
            y_st = 20;
            y_st += dy * 2;
            g.DrawString("FillPath", f, sb, new PointF(x_st, y_st));


            GraphicsPath gp3 = new GraphicsPath();  // Create a GraphicsPath object.
            // Set up all the string parameters.
            String drawString = "FillPath加入文字範例";
            FontFamily family = new FontFamily("Times New Roman");
            int fontStyle = (int)FontStyle.Italic;
            int emSize = 26;
            PointF pt = new PointF(x_st + dx, y_st);
            StringFormat format = StringFormat.GenericDefault;
            // Add the string to the path.
            gp3.AddString(drawString, family, fontStyle, emSize, pt, format);
            //Draw the path to the screen.
            g.FillPath(Brushes.Black, gp3);

            y_st += dy / 2;
            //g.DrawString("FillPath", f, sb, new PointF(x_st, y_st));

            x_st += dx;

            GraphicsPath gp4 = new GraphicsPath();
            gp4.AddLine(new Point(x_st + 10, y_st + 10), new Point(x_st + 60, y_st + 60));
            gp4.AddLine(new Point(x_st + 60, y_st + 10), new Point(x_st + 10, y_st + 60));
            gp4.AddRectangle(new Rectangle(x_st + 10, y_st + 10, 50, 50));
            g.FillPath(new SolidBrush(Color.Blue), gp4);



            //畫多個Rectangles
            x_st = 20;
            y_st = 20;
            y_st += dy * 4;
            g.DrawString("畫多個Rectangles", f, sb, new PointF(x_st, y_st - 25));

            Rectangle[] R = new Rectangle[20];
            for (int i = 0; i < R.Length; i++)
            {
                //R[i] = new Rectangle(0 + 30 * i, 0 + 30 * i);
                R[i] = new Rectangle(x_st + i * 10, y_st + i * 5, i * 30, i * 15);
            }
            g.DrawRectangles(new Pen(Brushes.Red, 2), R);


        }

        private void button47_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

            //畫多邊形與五角星星

            Point[] pt = new Point[5];  // 五個點

            int Cx = this.pictureBox1.ClientSize.Width / 2;  // 中心點
            int Cy = this.pictureBox1.ClientSize.Height / 2;
            int D = (int)(Math.Min(this.pictureBox1.ClientSize.Width, this.pictureBox1.ClientSize.Height) / 2) - 10; // 半徑
            double Theta = -Math.PI / 2.0; // 角度

            int i;
            for (i = 0; i < 5; i++)
            {
                pt[i].X = Cx + (int)(D * Math.Cos(Theta));
                pt[i].Y = Cy + (int)(D * Math.Sin(Theta));
                Theta += Math.PI * 2.0 / 5.0;  // 五邊形
                //Theta += 2 * Math.PI * 2.0 / 5.0; // 五角星星
            }
            g.DrawPolygon(Pens.Black, pt); // 繪出多邊形

            for (i = 0; i < 5; i++)
            {
                pt[i].X = Cx + (int)(D * Math.Cos(Theta));
                pt[i].Y = Cy + (int)(D * Math.Sin(Theta));
                //Theta += Math.PI * 2.0 / 5.0;  // 五邊形
                Theta += 2 * Math.PI * 2.0 / 5.0; // 五角星星
            }
            g.DrawPolygon(Pens.Red, pt); // 繪出多邊形
        }

        private void button48_Click(object sender, EventArgs e)
        {
        }

        bool flag_eraser = false;
        private void bt_eraser_Click(object sender, EventArgs e)
        {
            if (flag_eraser == true)
            {
                flag_eraser = false;
                bt_eraser.BackColor = BackColor;
            }
            else
            {
                flag_eraser = true;
                bt_eraser.BackColor = Color.Red;
            }
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {

        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
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

        int flag_mouse_down = 0;    //給erase用
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = 1;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if ((flag_eraser == true) && (flag_mouse_down == 1))
            {
                sb = new SolidBrush(BackColor);
                g.FillEllipse(sb, e.X - 10, e.Y - 10, 20, 20);
                pictureBox1.Image = bitmap1;
            }

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = 0;
        }

        private void button49_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

        }

        private void button50_Click(object sender, EventArgs e)
        {
        }

        private void button51_Click(object sender, EventArgs e)
        {
        }

        private void button52_Click(object sender, EventArgs e)
        {
        }

        private void button53_Click(object sender, EventArgs e)
        {
        }

        private void button54_Click(object sender, EventArgs e)
        {
        }

        int show_position = 1;
        private void button55_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
                //製作圖面的標記文字
                string filename = "C:\\______test_files\\picture1.jpg";
                bitmap1 = new Bitmap(filename);
                g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
                pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中
            }

            Font f = new Font("標楷體", 24, FontStyle.Bold);

            pictureBox1.Image = SetBadge(pictureBox1, "牡丹亭", f, show_position);//呼叫自定義方法
            show_position++;  //設定文字的顯示位置
            if (show_position > 6)
            {
                show_position = 1;
            }
        }

        public Image SetBadge(PictureBox Pict, String Str, Font font, int place)
        {
            Image Var_Image = Pict.Image;//根據圖片實例化Image類
            int Var_FontSize = (int)font.Size;//取得字體大小
            bool Var_isSetFont = false;//判斷目前文字是否超出圖片的大小
            int Var_W = Var_Image.Width;//取得圖片的寬度
            int Var_H = Var_Image.Height;//取得圖片的高度
            int Var_StrX = 0;//記錄文字的X位置
            int Var_StrY = 0;//記錄文字的Y位置

            Bitmap Var_bmp = new Bitmap(Var_W, Var_H);//實例化Image類
            Bitmap Var_SaveBmp = new Bitmap(Var_Image);//實例化Image類
            Graphics g = Graphics.FromImage(Var_bmp);//用指定的Bitmap實例化Graphics
            Graphics tem_Graphics = Graphics.FromImage(Var_Image);//用指定的Bitmap實例化Graphics
            SizeF Var_Size = new SizeF(Var_W, Var_H);//實例化SizeF類
            Font tem_Font = font;//取得文字的設定文字
            g.Clear(Color.White);//清空圖片
            while (Var_isSetFont == false)//如果文字超出圖片的大小
            {
                //設定文字的文字
                tem_Font = new Font(font.Name, Var_FontSize, font.Bold ? FontStyle.Bold : FontStyle.Regular);
                Var_Size = g.MeasureString(Str, tem_Font);//對文字進行測量
                if (Var_Size.Width < Var_bmp.Width - 10)//如果文字的寬度沒有超出圖片
                {
                    if (Var_Size.Height < Var_bmp.Height - 10)//如果文字的高度沒有超出圖片
                        Var_isSetFont = true;//不減小文字的大小
                }
                else
                    Var_FontSize = Var_FontSize - 1;//文字的字體大小減1
            }
            switch (place)//選擇文字的顯示位置
            {
                case 1://右下角
                    {
                        Var_StrX = (int)(Var_bmp.Width - Var_Size.Width - 3);//設定文字的X座標值
                        Var_StrY = (int)(Var_bmp.Height - Var_Size.Height);//設定文字的Y座標值
                        break;
                    }
                case 2://右上角
                    {
                        Var_StrX = (int)(Var_bmp.Width - Var_Size.Width - 3);
                        Var_StrY = 1;
                        break;
                    }
                case 3://左下角
                    {
                        Var_StrX = 1;
                        Var_StrY = (int)(Var_bmp.Height - Var_Size.Height);
                        break;
                    }
                case 4://左上角
                    {
                        Var_StrX = 1;
                        Var_StrY = 1;
                        break;
                    }
                case 5://頂局中
                    {
                        Var_StrX = (int)(Var_bmp.Width - Var_Size.Width - 2) / 2;
                        Var_StrY = 1;
                        break;
                    }
                case 6://底局中
                    {
                        Var_StrX = (int)(Var_bmp.Width - Var_Size.Width - 2) / 2;
                        Var_StrY = (int)(Var_bmp.Height - Var_Size.Height);
                        break;
                    }

            }
            g.DrawString(Str, tem_Font, new SolidBrush(Color.Black), Var_StrX, Var_StrY);//繪製前景色為黑色的文字
            int tem_Become = 40;//設定文字的變色深度
            //搜尋圖片的所有象素
            for (int x = 1; x < Var_bmp.Width; x++)
            {
                for (int y = 1; y < Var_bmp.Height; y++)
                {
                    int tem_a, tem_r, tem_g, tem_b, tem_r1, tem_g1, tem_b1;//定義變數
                    if (Var_bmp.GetPixel(x, y).ToArgb() == Color.Black.ToArgb())//如果目前象素的顏色為黑色
                    {
                        tem_a = Var_SaveBmp.GetPixel(x, y).A;//取得目前象素的alpha份量值
                        tem_r = Var_SaveBmp.GetPixel(x, y).R;//取得目前象素的R色值
                        tem_g = Var_SaveBmp.GetPixel(x, y).G;//取得目前象素的G色值
                        tem_b = Var_SaveBmp.GetPixel(x, y).B;//取得目前象素的B色值
                        tem_r1 = tem_r;//臨時儲存R色值
                        tem_g1 = tem_g;//臨時儲存G色值
                        tem_b1 = tem_b;//臨時儲存B色值
                        //根據加深後的圖片背景顯示文字
                        if (tem_b + tem_Become < 255)//如果B色值加上目前深度小於255
                            tem_b = tem_b + 255;//B色值加上深度值
                        if (tem_g + tem_Become < 255)
                            tem_g = tem_g + 255;
                        if (tem_r + tem_Become < 255)
                            tem_r = tem_r + 255;
                        if (tem_r1 - tem_Become > 0)//如果B色值加上目前深度大於0
                            tem_r1 = tem_r1 - tem_Become;//B色值減去深度值
                        if (tem_g1 - tem_Become > 0)
                            tem_g1 = tem_g1 - tem_Become;
                        if (tem_b1 - tem_Become > 0)
                            tem_b1 = tem_b1 - tem_Become;
                        tem_Graphics.DrawEllipse(new Pen(new SolidBrush(Color.Black)), x, y + 1, 3, 3);//繪製文字的陰影
                        //以深後的圖片背景顯示文字
                        tem_Graphics.DrawEllipse(new Pen(new SolidBrush(Color.FromArgb(tem_a, tem_r1, tem_g1, tem_b1))), x, y, 1, 1);
                    }
                }
            }
            return Var_Image;
        }

        private void button56_Click(object sender, EventArgs e)
        {
            //去背效果1

            if (bitmap1 == null)
            {
                open_new_file();
            }

            pictureBox1.BackColor = Color.Pink;

            string filename = @"C:\______test_files\__pic\_angry_bird\thumb-1920-283652.jpg";

            GraphicsUnit units = GraphicsUnit.Pixel;

            Bitmap bmp1 = new Bitmap(filename);
            Bitmap bmp2 = new Bitmap(filename);

            //bmp2 做 去背景
            bmp2.MakeTransparent(Color.White);  //MakeTransparent 用法, bmp2 去背景, 可以多重去背, 連續寫即可
            //bmp2.MakeTransparent(Color.Black);  //MakeTransparent 用法, bmp2 去背景, 可以多重去背, 連續寫即可

            Rectangle destRect1 = new Rectangle(30, 30, bmp1.Width / 5, bmp1.Height / 5);
            Rectangle destRect2 = new Rectangle(30, 200, bmp2.Width / 5, bmp2.Height / 5);

            g.DrawRectangle(new Pen(Color.Yellow, 10), 100, 100, 300, 300);


            SolidBrush sb = new SolidBrush(Color.Purple);
            Font f = new Font("標楷體", 20);

            g.DrawImage(bmp1, destRect1, 0, 0, bmp1.Width, bmp1.Height, units);
            g.DrawString("沒去背", f, sb, new PointF(destRect1.X + bmp1.Width / 5, destRect1.Y + 50));


            g.DrawImage(bmp2, destRect2, 0, 0, bmp2.Width, bmp2.Height, units);
            g.DrawString("有去背", f, sb, new PointF(destRect2.X + bmp2.Width / 5, destRect2.Y + 50));
        }

        private void button57_Click(object sender, EventArgs e)
        {
            //去背效果2
            //MakeTransparent 用法

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = new Bitmap(filename);
            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + ", H = " + bitmap1.Height.ToString() + "\n";

            int x_st = 50;
            int y_st = 50;
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            pictureBox1.Size = new Size(W * 2 + 150, H + 100);
            pictureBox1.BackColor = Color.Pink;

            Application.DoEvents();

            GraphicsUnit units = GraphicsUnit.Pixel;

            // Create parallelogram for drawing image.
            Point ulCorner = new Point(x_st + 0, y_st);
            Point urCorner = new Point(x_st + W, y_st);
            Point llCorner = new Point(x_st + 0, y_st + H);
            Point[] destPara = { ulCorner, urCorner, llCorner };

            // Create rectangle for source image.
            Rectangle srcRect = new Rectangle(0, 0, W, H);

            Graphics g = pictureBox1.CreateGraphics();

            g.DrawImage((Image)bitmap1, destPara, srcRect, units);

            Application.DoEvents();

            bitmap1.MakeTransparent(Color.White);
            g.DrawImage((Image)bitmap1, new Point(x_st + W + 10, y_st));

            g.DrawString("MakeTransparent 用法, 指名將白色變成透明", new Font("標楷體", 20), new SolidBrush(Color.Navy), 10, 10);
        }

        private void button58_Click(object sender, EventArgs e)
        {
            open_new_file();

            int dy = 150;

            //MakeTransparent 功能

            string filename = @"C:\______test_files\__pic\lion.bmp";

            richTextBox1.Text += "無 MakeTransparent\n";
            Bitmap bmp1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            g.DrawImage(bmp1, 0, 0, bmp1.Width, bmp1.Height);



            richTextBox1.Text += "有 MakeTransparent\n";
            Bitmap bmp2 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            //bmp2.MakeTransparent();    //沒寫就是預設的     程式碼會讓系統預設透明色彩透明
            bmp2.MakeTransparent(Color.White);//將圖片白色部分透明化, 將此 Bitmap 的指定色彩變為透明。

            g.DrawImage(bmp2, 0, dy, bmp2.Width, bmp2.Height);


            richTextBox1.Text += "有 MakeTransparent 指名某點顏色變透明\n";
            Bitmap bmp3 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            Color backColor = bmp3.GetPixel(20, 80);   //選取圖片邊緣的一個點的顏色當成背景色
            bmp3.MakeTransparent(backColor); //將此背景色設定為透明
            g.DrawImage(bmp3, 0, dy * 2, bmp3.Width, bmp3.Height);

            g.DrawString("無 MakeTransparent", new Font("標楷體", 20), new SolidBrush(Color.Navy), 0, bmp1.Height - 30);
            g.DrawString("有 MakeTransparent", new Font("標楷體", 20), new SolidBrush(Color.Navy), 0, dy + bmp2.Height - 30);
            g.DrawString("有 MakeTransparent 指名某點顏色變透明", new Font("標楷體", 20), new SolidBrush(Color.Navy), 0, dy * 2 + bmp3.Height - 30);

            pictureBox1.Image = bitmap1;
        }

        private void button59_Click(object sender, EventArgs e)
        {
        }
    }
}

