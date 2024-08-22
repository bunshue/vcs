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

namespace vcs_WebCam_AForge2_Record4
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection USBWebcams = null;

        private bool flag_recording = false; //判斷是否啟動錄影的旗標

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int BORDER = 10;

        public Bitmap bitmap1 = null;

        // output video resolution info
        bool isResolutionSet = false;
        int Width = 0;
        int Height = 0;

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
            int W = 640;
            int H = 480;
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = 140 + 50;
            int dy = 50 + 15;

            pictureBox1.Size = new Size(W, H);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Image = vcs_WebCam_AForge2_Record4.Properties.Resources.ims_logo_720x480;

            richTextBox1.Size = new Size(300, 560);
            richTextBox1.Location = new Point(x_st + dx * 3 + 90, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            groupBox1.Size = new Size(380, 70);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H + BORDER);

            bt_record_stop.Enabled = false;
            this.Size = new Size(1000, 620);
            x_st = 10;
            y_st = 20;
            dx = 90;
            dy = 28;
            dy = 40;

            bt_record_start.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_record_stop.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_exit.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            richTextBox1.BringToFront();
            bt_clear.BringToFront();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_record_start_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "測試圖片轉影片\n";

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

            //filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
            //C:\_git\vcs\_1.data\______test_files1\__pic\_scenery




        }

        private void bt_record_stop_Click(object sender, EventArgs e)
        {
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
