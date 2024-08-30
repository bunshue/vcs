using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Threading;
using System.Diagnostics;   //for Stopwatch

using AForge.Video.FFMPEG;      //for VideoFileWriter

using System.Drawing.Drawing2D;

using System.Drawing.Imaging;   //for PixelFormat

using AviFile;

namespace vcs_VideoFileWriter
{
    public partial class Form1 : Form
    {
        private const int BORDER = 10;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
        }

        void show_item_location()
        {
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = 140 + 50;
            int dy = 50 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 640);
            richTextBox1.Location = new Point(x_st + dx * 3 + 90, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 700);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void drawMessage(Bitmap bitmap1)
        {
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bmp = vcs_VideoFileWriter.Properties.Resources.logo;
            Graphics g;
            g = Graphics.FromImage(bitmap1);
            g.DrawRectangle(new Pen(Color.Red, 10), 50, 50, W - 50 * 2, H - 50 * 2);    //draw boundary
            g.DrawString("台東之旅", new Font("標楷體", 30), new SolidBrush(Color.Navy), new PointF(W - 50 - 240, H - 50 - 50));
            g.DrawImage(bmp, W - 50 - 70, H - 50 - 50 - 30, bmp.Width / 4, bmp.Height / 4);

            //原圖貼上
            //               貼上位置x      貼上位置y      貼上大小W            貼上大小H
            //g.DrawImage(bmp, x_st + dx * 0, y_st + dy * 0, bmp.Width * 12 / 10, bmp.Height * 12 / 10);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //圖片轉影片 same
            richTextBox1.Text += "圖片轉影片\n";
            Application.DoEvents();

            //vcs最小化錄影
            string filename = "tmp_video_writer0.avi";
            int W = 1600;
            int H = 760;
            int fps = 1;

            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung1.jpg";
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung2.jpg";
            string filename3 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung3.jpg";
            string filename4 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung4.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap2 = (Bitmap)Bitmap.FromFile(filename2);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap3 = (Bitmap)Bitmap.FromFile(filename3);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap4 = (Bitmap)Bitmap.FromFile(filename4);	//Bitmap.FromFile出來的是Image格式

            drawMessage(bitmap1);
            drawMessage(bitmap2);
            drawMessage(bitmap3);
            drawMessage(bitmap4);

            //公用變數
            VideoFileWriter writer = new VideoFileWriter();

            //開啟檔案
            writer.Open(filename, W, H, fps);

            for (int i = 0; i < 10; i++)
            {
                writer.WriteVideoFrame(bitmap1);//寫入影格
                writer.WriteVideoFrame(bitmap2);//寫入影格
                writer.WriteVideoFrame(bitmap3);//寫入影格
                writer.WriteVideoFrame(bitmap4);//寫入影格
            }

            //關閉檔案
            writer.Close();

            richTextBox1.Text += "圖片轉影片 OK\n";

        }
    }
}
