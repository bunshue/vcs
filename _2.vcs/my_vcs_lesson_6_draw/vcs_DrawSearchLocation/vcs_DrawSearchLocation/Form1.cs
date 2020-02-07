using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_DrawSearchLocation
{
    public partial class Form1 : Form
    {
        private const int ROUND = 50;

        Graphics g;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
            pictureBox1.Image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            //g = pictureBox1.CreateGraphics(); same
            g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String filename = string.Empty;

            int width;
            int height;

            filename = Application.StartupPath + "\\ims_image.bmp";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);

            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            width = bitmap1.Width;
            height = bitmap1.Height;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.Image = bitmap1;

            g = Graphics.FromImage(bitmap1);

            pictureBox1.Image = bitmap1;

            int x_st;
            int y_st;
            int ww;
            int hh;
            int WW = 640;
            int HH = 480;
            int awb_window_size = 200;     //AWB window size width, height

            int[] right_left_point_cnt = new int[ROUND];
            int[] down_up_point_cnt = new int[ROUND];
            int[] awb_block = new int[ROUND];

            right_left_point_cnt[0] = -15; down_up_point_cnt[0] = 65; awb_block[0] = 32;	//for vcs
            right_left_point_cnt[1] = -10; down_up_point_cnt[1] = -55; awb_block[1] = 32;	//for vcs
            right_left_point_cnt[2] = -10; down_up_point_cnt[2] = -55; awb_block[2] = 32;	//for vcs
            right_left_point_cnt[3] = -15; down_up_point_cnt[3] = 65; awb_block[3] = 32;	//for vcs
            right_left_point_cnt[4] = -15; down_up_point_cnt[4] = 65; awb_block[4] = 32;	//for vcs
            right_left_point_cnt[5] = -15; down_up_point_cnt[5] = 65; awb_block[5] = 32;	//for vcs
            right_left_point_cnt[6] = 50; down_up_point_cnt[6] = -30; awb_block[6] = 32;	//for vcs
            right_left_point_cnt[7] = -15; down_up_point_cnt[7] = 65; awb_block[7] = 32;	//for vcs
            right_left_point_cnt[8] = -15; down_up_point_cnt[8] = -50; awb_block[8] = 28;	//for vcs
            right_left_point_cnt[9] = -10; down_up_point_cnt[9] = -50; awb_block[9] = 28;	//for vcs
            right_left_point_cnt[10] = -15; down_up_point_cnt[10] = 65; awb_block[10] = 32;	//for vcs
            right_left_point_cnt[11] = 55; down_up_point_cnt[11] = -30; awb_block[11] = 28;	//for vcs
            right_left_point_cnt[12] = -15; down_up_point_cnt[12] = 65; awb_block[12] = 32;	//for vcs
            right_left_point_cnt[13] = -15; down_up_point_cnt[13] = 65; awb_block[13] = 32;	//for vcs
            right_left_point_cnt[14] = 50; down_up_point_cnt[14] = -30; awb_block[14] = 28;	//for vcs
            right_left_point_cnt[15] = 50; down_up_point_cnt[15] = -30; awb_block[15] = 32;	//for vcs
            right_left_point_cnt[16] = -15; down_up_point_cnt[16] = 65; awb_block[16] = 32;	//for vcs
            right_left_point_cnt[17] = 50; down_up_point_cnt[17] = -30; awb_block[17] = 28;	//for vcs
            right_left_point_cnt[18] = -15; down_up_point_cnt[18] = 65; awb_block[18] = 32;	//for vcs
            right_left_point_cnt[19] = -15; down_up_point_cnt[19] = 65; awb_block[19] = 32;	//for vcs
            right_left_point_cnt[20] = -15; down_up_point_cnt[20] = 65; awb_block[20] = 32;	//for vcs
            right_left_point_cnt[21] = -15; down_up_point_cnt[21] = 65; awb_block[21] = 32;	//for vcs
            right_left_point_cnt[22] = -10; down_up_point_cnt[22] = -55; awb_block[22] = 32;	//for vcs
            right_left_point_cnt[23] = -15; down_up_point_cnt[23] = 65; awb_block[23] = 32;	//for vcs
            right_left_point_cnt[24] = -10; down_up_point_cnt[24] = -55; awb_block[24] = 32;	//for vcs
            right_left_point_cnt[25] = 50; down_up_point_cnt[25] = -30; awb_block[25] = 32;	//for vcs
            right_left_point_cnt[26] = 50; down_up_point_cnt[26] = -30; awb_block[26] = 32;	//for vcs
            right_left_point_cnt[27] = -15; down_up_point_cnt[27] = 65; awb_block[27] = 32;	//for vcs
            right_left_point_cnt[28] = -15; down_up_point_cnt[28] = 65; awb_block[28] = 32;	//for vcs
            right_left_point_cnt[29] = 50; down_up_point_cnt[29] = -30; awb_block[29] = 28;	//for vcs
            right_left_point_cnt[30] = 60; down_up_point_cnt[30] = 65; awb_block[30] = 32;	//for vcs
            right_left_point_cnt[31] = -15; down_up_point_cnt[31] = 65; awb_block[31] = 32;	//for vcs
            right_left_point_cnt[32] = -15; down_up_point_cnt[32] = 65; awb_block[32] = 32;	//for vcs
            right_left_point_cnt[33] = -10; down_up_point_cnt[33] = -55; awb_block[33] = 32;	//for vcs
            right_left_point_cnt[34] = -15; down_up_point_cnt[34] = 65; awb_block[34] = 32;	//for vcs
            right_left_point_cnt[35] = 50; down_up_point_cnt[35] = -30; awb_block[35] = 32;	//for vcs
            right_left_point_cnt[36] = -30; down_up_point_cnt[36] = -55; awb_block[36] = 32;	//for vcs
            right_left_point_cnt[37] = -15; down_up_point_cnt[37] = 65; awb_block[37] = 32;	//for vcs
            right_left_point_cnt[38] = 50; down_up_point_cnt[38] = -30; awb_block[38] = 28;	//for vcs
            right_left_point_cnt[39] = 60; down_up_point_cnt[39] = -55; awb_block[39] = 28;	//for vcs
            right_left_point_cnt[40] = 50; down_up_point_cnt[40] = -30; awb_block[40] = 32;	//for vcs
            right_left_point_cnt[41] = -15; down_up_point_cnt[41] = 65; awb_block[41] = 32;	//for vcs
            right_left_point_cnt[42] = 50; down_up_point_cnt[42] = -30; awb_block[42] = 28;	//for vcs
            right_left_point_cnt[43] = -15; down_up_point_cnt[43] = 65; awb_block[43] = 32;	//for vcs
            right_left_point_cnt[44] = -10; down_up_point_cnt[44] = -50; awb_block[44] = 28;	//for vcs
            right_left_point_cnt[45] = -10; down_up_point_cnt[45] = -55; awb_block[45] = 32;	//for vcs
            right_left_point_cnt[46] = 50; down_up_point_cnt[46] = -30; awb_block[46] = 32;	//for vcs
            right_left_point_cnt[47] = 50; down_up_point_cnt[47] = -30; awb_block[47] = 32;	//for vcs
            right_left_point_cnt[48] = -15; down_up_point_cnt[48] = 65; awb_block[48] = 32;	//for vcs
            right_left_point_cnt[49] = -10; down_up_point_cnt[49] = -55; awb_block[49] = 32;	//for vcs

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, 640 - 1, 480 - 1));

            x_st = WW / 2 - awb_window_size / 2;
            y_st = HH / 2 - awb_window_size / 2;

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, awb_window_size, awb_window_size));

            int i;
            for (i = 0; i < ROUND; i++)
            {
                ww = awb_block[i];
                hh = awb_block[i];

                x_st = WW / 2 - ww / 2 + right_left_point_cnt[i];
                y_st = HH / 2 - hh / 2 + down_up_point_cnt[i];

                g.DrawRectangle(new Pen(Color.Red, 1), new Rectangle(x_st, y_st, ww, hh));
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (bitmap1 != null)
            {
                //filename = Application.StartupPath + "\\ims_image.bmp";
                String file = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                //String file1 = file + ".jpg";
                String file2 = file + ".bmp";
                //String file3 = file + ".png";

                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(@file2, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + file2 + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";

        }
    }
}
