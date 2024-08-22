using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for dll

using AForge.Video;
using AForge.Video.DirectShow;  // Video Recording
using AForge.Video.FFMPEG;      //for VideoFileWriter

namespace vcs_Picture2Video
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
            int dx = 120;
            int dy = 50 + 15;

            richTextBox1.Size = new Size(400, 560);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(560, 620);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "圖片轉影片\n";
            Application.DoEvents();

            //vcs最小化錄影
            string filename = "tmp_pic2video.avi";
            int W = 1600;
            int H = 760;
            int fps = 1;
            Bitmap bitmap1;

            //公用變數
            VideoFileWriter writer = new VideoFileWriter();

            //開啟檔案
            writer.Open(filename, W, H, fps);

            for (int i = 0; i < 10; i++)
            {
                filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung1.jpg";
                bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
                writer.WriteVideoFrame(bitmap1);//寫入影格

                filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung2.jpg";
                bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
                writer.WriteVideoFrame(bitmap1);//寫入影格

                filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung3.jpg";
                bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
                writer.WriteVideoFrame(bitmap1);//寫入影格

                filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung4.jpg";
                bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
                writer.WriteVideoFrame(bitmap1);//寫入影格
            }

            //關閉檔案
            writer.Close();

            richTextBox1.Text += "圖片轉影片 OK\n";
        }
    }
}
