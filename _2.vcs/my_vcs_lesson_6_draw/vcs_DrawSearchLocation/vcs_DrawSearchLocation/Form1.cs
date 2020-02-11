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
        private const int ROUND = 30;

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


            right_left_point_cnt[0] = -10; down_up_point_cnt[0] = 65; awb_block[0] = 32;	//for vcs
            right_left_point_cnt[1] = -10; down_up_point_cnt[1] = 65; awb_block[1] = 32;	//for vcs
            right_left_point_cnt[2] = -10; down_up_point_cnt[2] = 65; awb_block[2] = 32;	//for vcs
            right_left_point_cnt[3] = -10; down_up_point_cnt[3] = 65; awb_block[3] = 32;	//for vcs
            right_left_point_cnt[4] = -10; down_up_point_cnt[4] = 65; awb_block[4] = 32;	//for vcs
            right_left_point_cnt[5] = -10; down_up_point_cnt[5] = 65; awb_block[5] = 32;	//for vcs
            right_left_point_cnt[6] = -10; down_up_point_cnt[6] = 65; awb_block[6] = 32;	//for vcs
            right_left_point_cnt[7] = -10; down_up_point_cnt[7] = 65; awb_block[7] = 32;	//for vcs
            right_left_point_cnt[8] = -15; down_up_point_cnt[8] = 65; awb_block[8] = 32;	//for vcs
            right_left_point_cnt[9] = -10; down_up_point_cnt[9] = 65; awb_block[9] = 32;	//for vcs
            right_left_point_cnt[10] = -10; down_up_point_cnt[10] = 65; awb_block[10] = 32;	//for vcs
            right_left_point_cnt[11] = -10; down_up_point_cnt[11] = 65; awb_block[11] = 32;	//for vcs
            right_left_point_cnt[12] = -10; down_up_point_cnt[12] = 65; awb_block[12] = 32;	//for vcs
            right_left_point_cnt[13] = -10; down_up_point_cnt[13] = 65; awb_block[13] = 32;	//for vcs
            right_left_point_cnt[14] = -10; down_up_point_cnt[14] = 65; awb_block[14] = 32;	//for vcs
            right_left_point_cnt[15] = -10; down_up_point_cnt[15] = 65; awb_block[15] = 32;	//for vcs
            right_left_point_cnt[16] = -10; down_up_point_cnt[16] = 65; awb_block[16] = 32;	//for vcs
            right_left_point_cnt[17] = -15; down_up_point_cnt[17] = 65; awb_block[17] = 32;	//for vcs
            right_left_point_cnt[18] = -10; down_up_point_cnt[18] = 65; awb_block[18] = 32;	//for vcs
            right_left_point_cnt[19] = -10; down_up_point_cnt[19] = 65; awb_block[19] = 32;	//for vcs
            right_left_point_cnt[20] = -10; down_up_point_cnt[20] = 65; awb_block[20] = 28;	//for vcs
            right_left_point_cnt[21] = -10; down_up_point_cnt[21] = 65; awb_block[21] = 32;	//for vcs
            right_left_point_cnt[22] = -10; down_up_point_cnt[22] = 65; awb_block[22] = 28;	//for vcs
            right_left_point_cnt[23] = -10; down_up_point_cnt[23] = 65; awb_block[23] = 32;	//for vcs
            right_left_point_cnt[24] = -10; down_up_point_cnt[24] = 65; awb_block[24] = 32;	//for vcs
            right_left_point_cnt[25] = -10; down_up_point_cnt[25] = 65; awb_block[25] = 32;	//for vcs
            right_left_point_cnt[26] = -10; down_up_point_cnt[26] = 65; awb_block[26] = 32;	//for vcs
            right_left_point_cnt[27] = -10; down_up_point_cnt[27] = 65; awb_block[27] = 32;	//for vcs
            right_left_point_cnt[28] = -10; down_up_point_cnt[28] = 65; awb_block[28] = 32;	//for vcs
            right_left_point_cnt[29] = -10; down_up_point_cnt[29] = 65; awb_block[29] = 32;	//for vcs


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

                g.DrawString(i.ToString(), new Font("標楷體", 16), new SolidBrush(Color.Red), new PointF(x_st + 100, y_st + hh + 10 + i * 12 - 200));
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
