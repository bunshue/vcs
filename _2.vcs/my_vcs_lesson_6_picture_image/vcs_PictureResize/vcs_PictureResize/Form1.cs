using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_PictureResize
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        int flag_operation_mode = 1;    //0 : 空白模式, 1 : 圖片模式

        private Bitmap bitmap1 = null;
        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高

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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

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
            bt_open_file_setup();
            bt_exit_setup();
        }

        private void bt_open_file_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();

            openFileDialog1.Title = "單選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            //openFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            openFileDialog1.InitialDirectory = @"C:\Users\070601\Desktop\ims2\";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //單選
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";

                filename = openFileDialog1.FileName;

                reset_picture();
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        void bt_open_file_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_open_file = new Button();  // 實例化按鈕
            bt_open_file.Size = new Size(w, h);
            bt_open_file.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Blue, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, w / 4, 0, (w - 1) / 2, h - 1);
            g.DrawLine(p, (w - 1) * 3 / 4, 0, (w - 1) / 2, h - 1);
            bt_open_file.Image = bmp;

            bt_open_file.Location = new Point(this.ClientSize.Width - bt_open_file.Width, 0 + h);
            bt_open_file.Click += bt_open_file_Click;     // 加入按鈕事件

            this.Controls.Add(bt_open_file); // 將按鈕加入表單
            bt_open_file.BringToFront();     //移到最上層
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

        void reset_picture()
        {
            if (flag_operation_mode == 0)
            {
                W = pictureBox1.Width;
                H = pictureBox1.Height;
            }
            else if (flag_operation_mode == 1)
            {
                bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
                pictureBox1.Image = bitmap1;
                W = bitmap1.Width;
                H = bitmap1.Height;
                W_old = bitmap1.Width;
                H_old = bitmap1.Height;

                pictureBox1.Width = bitmap1.Width;
                pictureBox1.Height = bitmap1.Height;
            }
            else //test
            {
                W = pictureBox1.Width;
                H = pictureBox1.Height;
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
            richTextBox1.Text += "old, W = " + W_old.ToString() + ", H = " + H_old.ToString() + "\n";
            //縮成8成
            W_new = W_old * 4 / 5;
            H_new = H_old * 4 / 5;

            richTextBox1.Text += "new, W = " + W_new.ToString() + ", H = " + H_new.ToString() + "\n";

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
