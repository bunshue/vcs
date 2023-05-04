using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_PictureResize
{
    public partial class Form1 : Form
    {
        private Bitmap bitmap1 = null;
        int W_old = 0;
        int H_old = 0;
        float dpix_old = 0;
        float dpiy_old = 0;

        int W_new = 0;
        int H_new = 0;
        float dpix_new = 0;
        float dpiy_new = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files1\\picture1.jpg";

            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);

            W_old = bitmap1.Width;
            H_old = bitmap1.Height;

            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "影像ID\n";
            richTextBox1.Text += "尺寸\t\t" + W_old.ToString() + " x " + H_old.ToString() + "\n";
            richTextBox1.Text += "寬度\t\t" + W_old.ToString() + " 個像素\n";
            richTextBox1.Text += "高度\t\t" + H_old.ToString() + " 個像素\n";

            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                dpix_old = g.DpiX;
                dpiy_old = g.DpiY;
                richTextBox1.Text += "水平解析度\t" + dpix_old.ToString() + " dpi\n";
                richTextBox1.Text += "垂直解析度\t" + dpiy_old.ToString() + " dpi\n";
            }
        }

        public void save_image_to_drive()
        {
            using (Bitmap bm = new Bitmap(W_new, H_new))
            {
                Point[] points =
                    {
                        new Point(0, 0),
                        new Point(W_new, 0),
                        new Point(0, H_new),
                    };
                using (Graphics g = Graphics.FromImage(bm))
                {
                    g.DrawImage(bitmap1, points);
                }
                bm.SetResolution(dpix_new, dpiy_new);


                if (bm != null)
                {
                    string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                    String filename1 = filename + ".jpg";
                    String filename2 = filename + ".bmp";
                    String filename3 = filename + ".png";

                    try
                    {
                        bm.Save(@filename1, ImageFormat.Jpeg);
                        bm.Save(@filename2, ImageFormat.Bmp);
                        bm.Save(@filename3, ImageFormat.Png);

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





        }

        private void button1_Click(object sender, EventArgs e)
        {
            //放大2成
            W_new = W_old * 6 / 5;
            H_new = H_old * 6 / 5;

            dpix_new = dpix_old;
            dpiy_new = dpiy_old;

            save_image_to_drive();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //縮成8成
            W_new = W_old * 4 / 5;
            H_new = H_old * 4 / 5;

            dpix_new = dpix_old;
            dpiy_new = dpiy_old;

            save_image_to_drive();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //解析度變半
            W_new = W_old;
            H_new = H_old;

            dpix_new = dpix_old / 2;
            dpiy_new = dpiy_old / 2;

            save_image_to_drive();

        }


    }
}
