using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File
using System.Drawing.Imaging;   //for ImageFormat

using System.Diagnostics;               //for Stopwatch
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_ReadWrite_BMP_PNG
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
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
            dx = 200 + 5;
            dy = 60 + 5;

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

            pictureBox1.Size = new Size(500, 640);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Size = new Size(500, 640);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1460, 700);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {

        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            int ww = 256;
            int hh = 300;
            int size = ww * hh * 4 + 0x36;
            int h_res = 0x0EC4;
            int v_res = 0x0EC4;

            byte[] data = new byte[size];

            for (i = 0; i < size; i++)
            {
                data[i] = 0;
            }
            data[0] = (byte)'B';
            data[1] = (byte)'M';
            data[2] = (byte)(size % 256);
            data[3] = (byte)((size / 256) % 256);
            data[4] = (byte)((size / 256 / 256) % 256);
            data[5] = (byte)((size / 256 / 256) % 256);
            data[10] = 0x36;
            data[14] = 0x28;

            data[18] = (byte)(ww % 256);
            data[19] = (byte)((ww / 256) % 256);
            data[20] = (byte)((ww / 256 / 256) % 256);
            data[21] = (byte)((ww / 256 / 256) % 256);

            data[22] = (byte)(hh % 256);
            data[23] = (byte)((hh / 256) % 256);
            data[24] = (byte)((hh / 256 / 256) % 256);
            data[25] = (byte)((hh / 256 / 256) % 256);

            data[26] = 0x01;
            data[28] = 0x20;

            data[38] = (byte)(h_res % 256);
            data[39] = (byte)((h_res / 256) % 256);
            data[40] = (byte)((h_res / 256 / 256) % 256);
            data[41] = (byte)((h_res / 256 / 256) % 256);

            data[42] = (byte)(v_res % 256);
            data[43] = (byte)((v_res / 256) % 256);
            data[44] = (byte)((v_res / 256 / 256) % 256);
            data[45] = (byte)((v_res / 256 / 256) % 256);

            for (j = 0; j < hh; j++)
            {
                for (i = 0; i < ww; i++)
                {
                    if (j < hh / 20)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0xCC;    //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 0xBB;    //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 0xAA;    //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;       //A
                    }
                    else if (j < hh / 10)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = (byte)i;    //B
                        data[54 + ww * 4 * j + i * 4 + 1] = (byte)i;    //G
                        data[54 + ww * 4 * j + i * 4 + 2] = (byte)i;    //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;       //A
                    }
                    else if (j < hh / 3)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 0;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = (byte)i;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else if (j < hh / 3 * 2)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0;
                        data[54 + ww * 4 * j + i * 4 + 1] = (byte)i;
                        data[54 + ww * 4 * j + i * 4 + 2] = 0;
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;
                    }
                    else
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = (byte)i;
                        data[54 + ww * 4 * j + i * 4 + 1] = 0;
                        data[54 + ww * 4 * j + i * 4 + 2] = 0;
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;
                    }
                }
            }

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            //寫資料
            File.WriteAllBytes(filename, data);
            richTextBox1.Text += "\n製作BMP檔\t" + filename + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_bmp\vcs_ReadWrite_BMP.bmp";

            //讀取資料
            byte[] data = File.ReadAllBytes(filename);
            richTextBox1.Text += "\n讀取BMP檔\t" + filename + "\n";
            richTextBox1.Text += "長度 = " + data.Length.ToString() + " 拜\n";

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */
            int i;
            for (i = 0; i < 0x36; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");
                if ((i % 32) == 31)
                {
                    richTextBox1.Text += "\n";
                }
                else if ((i % 4) == 3)
                {
                    richTextBox1.Text += "  ";
                }
            }
            richTextBox1.Text += "\n";

            int ww;
            int hh;
            int size;// = ww * hh * 4 + 0x36;
            int h_res;  // = 0x0EC4;
            int v_res;  // = 0x0EC4;

            if ((data[0] != 'B') || (data[1] != 'M'))
            {
                richTextBox1.Text += "非BMP檔";
                return;
            }

            size = data[2] + data[3] * 256 + data[4] * 256 * 256 + data[5] * 256 * 256 * 256;

            //data[10] = 0x36;
            //data[14] = 0x28;

            ww = data[18] + data[19] * 256 + data[20] * 256 * 256 + data[21] * 256 * 256 * 256;
            hh = data[22] + data[23] * 256 + data[24] * 256 * 256 + data[25] * 256 * 256 * 256;

            //data[26] = 0x01;
            //data[28] = 0x20;

            h_res = data[38] + data[39] * 256 + data[40] * 256 * 256 + data[41] * 256 * 256 * 256;
            v_res = data[42] + data[43] * 256 + data[44] * 256 * 256 + data[45] * 256 * 256 * 256;

            richTextBox1.Text += "ww = " + ww.ToString() + " hh = " + hh.ToString() + "\n";

            Image img = Image.FromFile(filename);

            richTextBox1.Text += "W : " + img.Width.ToString() + "\n";
            richTextBox1.Text += "H : " + img.Height.ToString() + "\n";
            richTextBox1.Text += "size : " + img.Size.Width.ToString() + " X " + img.Size.Height.ToString() + "\n";
            richTextBox1.Text += "P W : " + img.PhysicalDimension.Width.ToString() + "\n";
            richTextBox1.Text += "P H : " + img.PhysicalDimension.Height.ToString() + "\n";
            pictureBox1.Image = img;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            int ww = 256 * 6 + 48;
            int hh = 300;
            int size = ww * hh * 4 + 0x36;
            int h_res = 0x0EC4;
            int v_res = 0x0EC4;

            byte[] data = new byte[size];

            for (i = 0; i < size; i++)
            {
                data[i] = 0;
            }
            data[0] = (byte)'B';
            data[1] = (byte)'M';
            data[2] = (byte)(size % 256);
            data[3] = (byte)((size / 256) % 256);
            data[4] = (byte)((size / 256 / 256) % 256);
            data[5] = (byte)((size / 256 / 256) % 256);
            data[10] = 0x36;
            data[14] = 0x28;

            data[18] = (byte)(ww % 256);
            data[19] = (byte)((ww / 256) % 256);
            data[20] = (byte)((ww / 256 / 256) % 256);
            data[21] = (byte)((ww / 256 / 256) % 256);

            data[22] = (byte)(hh % 256);
            data[23] = (byte)((hh / 256) % 256);
            data[24] = (byte)((hh / 256 / 256) % 256);
            data[25] = (byte)((hh / 256 / 256) % 256);

            data[26] = 0x01;
            data[28] = 0x20;

            data[38] = (byte)(h_res % 256);
            data[39] = (byte)((h_res / 256) % 256);
            data[40] = (byte)((h_res / 256 / 256) % 256);
            data[41] = (byte)((h_res / 256 / 256) % 256);

            data[42] = (byte)(v_res % 256);
            data[43] = (byte)((v_res / 256) % 256);
            data[44] = (byte)((v_res / 256 / 256) % 256);
            data[45] = (byte)((v_res / 256 / 256) % 256);

            for (j = 0; j < hh; j++)
            {
                for (i = 0; i < ww; i++)
                {
                    data[54 + ww * 4 * j + i * 4 + 0] = (byte)(i / 6);    //B
                    data[54 + ww * 4 * j + i * 4 + 1] = (byte)(i / 6);    //G
                    data[54 + ww * 4 * j + i * 4 + 2] = (byte)(i / 6);    //R
                    data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;       //A
                }
            }

            for (j = 0; j < hh; j++)
            {
                for (i = 0; i < ww; i++)
                {
                    if ((j == 0) || (j == (hh - 1)))
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 0;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 255;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else if ((i == 0) || (i == (ww - 1)))
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 0;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 255;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else if ((i % 48) == 47)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 0;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 255;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else if (i > 256 * 6)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 255;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 255;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 255;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = (byte)((i / 6) / 8 * 8);    //B
                        data[54 + ww * 4 * j + i * 4 + 1] = (byte)((i / 6) / 8 * 8);    //G
                        data[54 + ww * 4 * j + i * 4 + 2] = (byte)((i / 6) / 8 * 8);    //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;       //A
                    }
                }
            }

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            //寫資料
            File.WriteAllBytes(filename, data);
            richTextBox1.Text += "\n製作BMP檔\t" + filename + "\n";

            return;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Graphics g;
            Pen p;
            SolidBrush sb;
            Bitmap bitmap1;
            string FileName = "";
            Color foreground_color = Color.Red;
            Color background_color = Color.White;

            p = new Pen(foreground_color, 3);
            sb = new SolidBrush(foreground_color);


            openFileDialog1.Filter = "圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png";
            //openFileDialog1.Filter = "BMP|*.bmp|JPG|*.jpg|PNG|*.png|GIF|*.gif";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                FileName = this.openFileDialog1.FileName.Trim();
                richTextBox1.Text += FileName + "\n";
                pictureBox1.ImageLocation = openFileDialog1.FileName;
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";

                return;
            }

            int width;
            int height;

            //string filename = @"D:\_git\vcs\_1.data\______test_files1\step2.png";
            ///richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(FileName);
            //bitmap1 = new Bitmap(pictureBox1.Image);

            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            width = bitmap1.Width;
            height = bitmap1.Height;

            //pictureBox1.Size = new Size(1, 1);
            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);

            g = Graphics.FromImage(bitmap1);

            int xx;
            int yy;
            int ss;

            Font f;
            f = new Font("Arial", 15);
            for (xx = 0; xx < width; xx += 48)
            {
                ss = (xx / 48) * 8;
                if (ss == 256)
                    ss = 255;
                g.DrawString(ss.ToString(), f, sb, new PointF(xx, 20));
            }

            //g.DrawRectangle(p, new Rectangle(0, 0, width - 1, height - 1));

            pictureBox1.Image = bitmap1;

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
            {
                richTextBox1.Text += "無圖可存\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int width = 160;
            int i;
            int j;
            int ww = width * 8;
            int hh = 300;
            int size = ww * hh * 4 + 0x36;
            int h_res = 0x0EC4;
            int v_res = 0x0EC4;

            byte[] data = new byte[size];

            for (i = 0; i < size; i++)
            {
                data[i] = 0;
            }
            data[0] = (byte)'B';
            data[1] = (byte)'M';
            data[2] = (byte)(size % 256);
            data[3] = (byte)((size / 256) % 256);
            data[4] = (byte)((size / 256 / 256) % 256);
            data[5] = (byte)((size / 256 / 256) % 256);
            data[10] = 0x36;
            data[14] = 0x28;

            data[18] = (byte)(ww % 256);
            data[19] = (byte)((ww / 256) % 256);
            data[20] = (byte)((ww / 256 / 256) % 256);
            data[21] = (byte)((ww / 256 / 256) % 256);

            data[22] = (byte)(hh % 256);
            data[23] = (byte)((hh / 256) % 256);
            data[24] = (byte)((hh / 256 / 256) % 256);
            data[25] = (byte)((hh / 256 / 256) % 256);

            data[26] = 0x01;
            data[28] = 0x20;

            data[38] = (byte)(h_res % 256);
            data[39] = (byte)((h_res / 256) % 256);
            data[40] = (byte)((h_res / 256 / 256) % 256);
            data[41] = (byte)((h_res / 256 / 256) % 256);

            data[42] = (byte)(v_res % 256);
            data[43] = (byte)((v_res / 256) % 256);
            data[44] = (byte)((v_res / 256 / 256) % 256);
            data[45] = (byte)((v_res / 256 / 256) % 256);

            for (j = 0; j < hh; j++)
            {
                for (i = 0; i < ww; i++)
                {
                    if (i < width * 1)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 255;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 255;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 255;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else if (i < width * 2)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 255;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 255;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else if (i < width * 3)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 255;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 255;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 0;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else if (i < width * 4)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 255;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 0;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else if (i < width * 5)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 255;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 0;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 255;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else if (i < width * 6)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 0;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 255;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else if (i < width * 7)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 255;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 0;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 0;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 0;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 0;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                }
            }

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            //寫資料
            File.WriteAllBytes(filename, data);
            richTextBox1.Text += "\n製作BMP檔\t" + filename + "\n";

            return;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Bitmap bitmap;
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\bear.bmp";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\bear.bmp.jpg";
            bitmap = new Bitmap(filename1);
            richTextBox1.Text += "width = " + bitmap.Width.ToString() + "\n";
            richTextBox1.Text += "height = " + bitmap.Height.ToString() + "\n";
            bitmap.Save(filename2, ImageFormat.Jpeg);
            richTextBox1.Text += filename1 + " to " + filename2 + "轉換完成\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //???????
            string filename = @"D:\_git\vcs\_1.data\______test_files1\test_ReadAllBytes.bmp";

            byte[] bmp_data = new byte[256];
            FileStream fs = new FileStream(filename, FileMode.Open);

            int len = (int)fs.Length;
            richTextBox1.Text += "\nlength = " + fs.Length.ToString() + "\n";

            if (len > 256)
                len = 256;

            fs.Read(bmp_data, 0, len);

            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += bmp_data[i].ToString("X2");
                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";
            }
            // 關閉檔案。
            fs.Close();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\test_ReadAllBytes.bmp";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\test_WriteAllBytes.bmp";

            //讀取資料
            byte[] data_read = File.ReadAllBytes(filename1);
            richTextBox1.Text += "讀取檔案" + filename1 + "\t";
            richTextBox1.Text += "len = " + data_read.Length.ToString() + "\n";

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            //修改資料
            for (int i = 54; i < data_read.Length; i++)
            {
                /*
                if (data_read[i] == 0xCC)
                    data_read[i] = 0xFF;
                */
                data_read[i] = (byte)(255 - (int)data_read[i]);
            }

            //寫資料
            File.WriteAllBytes(filename2, data_read);
            richTextBox1.Text += "寫成檔案" + filename2 + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //二進位讀檔 PNG
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_png\vcs_ReadWrite_PNG.png";
            FileStream fs = File.OpenRead(filename); //OpenRead[二進位讀檔]
            int filelength = 0;
            filelength = (int)fs.Length; //獲得檔長度
            richTextBox1.Text += "len = 0x" + filelength.ToString("X6") + " = " + filelength.ToString() + "\n";

            filelength = 8;
            Byte[] w = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(w, 0, filelength); //按位元組流讀取

            int i;

            for (i = 0; i < filelength; i++)
            {
                richTextBox1.Text += w[i].ToString("X2");
                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";

            for (i = 1; i < 4; i++)
            {
                //richTextBox1.Text += image[i].ToString("C");
                richTextBox1.Text += (char)w[i];

            }
            richTextBox1.Text += "\n";

            filelength = 24;
            w = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(w, 0, filelength); //按位元組流讀取
            fs.Close();

            for (i = 0; i < filelength; i++)
            {
                richTextBox1.Text += w[i].ToString("X2");
                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";
            }

            richTextBox1.Text += "\n";

            for (i = 4; i < 8; i++)
            {
                //richTextBox1.Text += image[i].ToString("C");
                richTextBox1.Text += (char)w[i];
            }
            richTextBox1.Text += "\n";

            int datasize;
            int width;
            int height;
            int bit_depth;
            int color_type;
            int compression_method;
            int filter_method;
            int interlace_method;

            for (i = 1; i < 4; i++)
            {
                //richTextBox1.Text += image[i].ToString("C");
                richTextBox1.Text += (char)w[i];
            }

            /*
            datasize = w[8] << 24 | w[9] << 16 | w[10] << 8 | w[11];
            width = w[16] << 24 | w[17] << 16 | w[18] << 8 | w[19];
            height = w[20] << 24 | w[21] << 16 | w[22] << 8 | w[23];
            bit_depth = w[24];
            color_type = w[25];
            compression_method = w[26];
            filter_method = w[27];
            interlace_method = w[28];
            */
            datasize = w[0] << 24 | w[1] << 16 | w[2] << 8 | w[3];
            width = w[8] << 24 | w[9] << 16 | w[10] << 8 | w[11];
            height = w[12] << 24 | w[13] << 16 | w[14] << 8 | w[15];
            bit_depth = w[16];
            color_type = w[17];
            compression_method = w[18];
            filter_method = w[19];
            interlace_method = w[20];

            richTextBox1.Text += "datasize : " + datasize.ToString() + "\n";
            richTextBox1.Text += "W : " + width.ToString() + "\n";
            richTextBox1.Text += "H : " + height.ToString() + "\n";
            richTextBox1.Text += "bit_depth : " + bit_depth.ToString() + "\n";
            richTextBox1.Text += "color_type : " + color_type.ToString() + "\n";
            richTextBox1.Text += "compression_method : " + compression_method.ToString() + "\n";
            richTextBox1.Text += "filter_method : " + filter_method.ToString() + "\n";
            richTextBox1.Text += "interlace_method : " + interlace_method.ToString() + "\n";


            //顯示圖片
            fs = File.OpenRead(filename); //OpenRead[二進位讀檔]
            System.Drawing.Image result = System.Drawing.Image.FromStream(fs);
            fs.Close();
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = result;


            //讀前面256拜
            fs = File.OpenRead(filename); //OpenRead[二進位讀檔]

            filelength = 256;
            w = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(w, 0, filelength); //按位元組流讀取
            fs.Close();

            for (i = 0; i < filelength; i++)
            {
                //richTextBox1.Text += w[i].ToString("X2");

                if (((w[i] >= '0') && (w[i] <= '9')) || ((w[i] >= 'A') && (w[i] <= 'Z')) || ((w[i] >= 'a') && (w[i] <= 'z')))
                {
                    richTextBox1.Text += (char)w[i];
                }
                else
                    richTextBox1.Text += ".";

                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";
            }
            fs.Close();
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
