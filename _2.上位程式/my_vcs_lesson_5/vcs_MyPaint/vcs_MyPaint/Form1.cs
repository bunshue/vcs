using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_MyPaint
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        Bitmap bitmap1;
        Bitmap bitmap2;

        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 1;
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            pictureBox2.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 5);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int ccc = 0;
            int xx;
            int yy;

            string filename = "C:\\______test_vcs\\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);
            bitmap2 = new Bitmap(filename);
            pictureBox1.Image = bitmap2;

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
            pictureBox2.Image = bitmap1;
            richTextBox1.Text += "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (bitmap1 != null)
            {
                bitmap1.Save(@"C:\______test_vcs\\my_picture.jpg", ImageFormat.Jpeg);
                bitmap1.Save(@"C:\______test_vcs\\my_picture.bmp", ImageFormat.Bmp);
                bitmap1.Save(@"C:\______test_vcs\\my_picture.png", ImageFormat.Png);
                richTextBox1.Text += "存檔成功\n";
                richTextBox1.Text += "已存檔C:\\______test_vcs\\my_picture.jpg\n";
                richTextBox1.Text += "已存檔C:\\______test_vcs\\my_picture.png\n";
                richTextBox1.Text += "已存檔C:\\______test_vcs\\my_picture.bmp\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            bitmap2 = null;
            pictureBox1.Image = null;
            pictureBox2.Image = null;
            richTextBox1.Clear();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    richTextBox1.Text += "Normal\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
                    pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
                    break;
                case 1:
                    richTextBox1.Text += "AutoSize\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
                    pictureBox2.SizeMode = PictureBoxSizeMode.AutoSize;
                    break;
                case 2:
                    richTextBox1.Text += "CenterImage\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
                    pictureBox2.SizeMode = PictureBoxSizeMode.CenterImage;
                    break;
                case 3:
                    richTextBox1.Text += "StretchImage\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
                    pictureBox2.SizeMode = PictureBoxSizeMode.StretchImage;
                    break;
                case 4:
                    richTextBox1.Text += "Zoom\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                    pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
                    break;
                default:
                    richTextBox1.Text += "xxxxxxxxxx\n";
                    break;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(bitmap1 == null)
                bitmap1 = new Bitmap(pictureBox2.Width, pictureBox2.Height);

            g = Graphics.FromImage(bitmap1);
            g.DrawRectangle(p, 50, 50, 100, 100);
            pictureBox2.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(pictureBox2.Width, pictureBox2.Height);
            g = Graphics.FromImage(bitmap1);
            g.DrawRectangle(p, 0, 0, pictureBox2.Width - 1, pictureBox2.Height - 1);
            pictureBox2.Image = bitmap1;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int xx;
            int yy;
            bitmap1 = new Bitmap(100, 100);
            for (yy = 0; yy < 100; yy++)
            {
                for (xx = 0; xx < 100; xx++)
                {
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                }
            }
            pictureBox2.Image = bitmap1;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(1, 1);
            pictureBox2.Size = new Size(600, 500);
            pictureBox2.Location = new Point(50, 50);

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
            pictureBox2.Size = new Size(width, height);
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
            pictureBox2.Image = bitmap1;

        }
    }
}
