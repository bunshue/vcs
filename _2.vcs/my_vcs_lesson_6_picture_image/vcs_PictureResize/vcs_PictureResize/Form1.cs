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
using System.Drawing.Drawing2D;//for InterpolationMode

namespace vcs_PictureResize
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

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
            textBox1.Text = @"D:\_git\vcs\_1.data\______test_files1\__pic\_scenery";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

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

            int value = trackBar1.Value;

            richTextBox1.Text += "放大倍率 : " + (value * 100 / 10).ToString() + " %\n";

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);
            pictureBox1.Image = image;

            int W1 = image.Width;
            int H1 = image.Height;

            int W2 = W1 * value / 10;
            int H2 = H1 * value / 10;

            Size new_size = new Size(W2, H2);
            pictureBox2.Image = ResizeImage(image, new_size);



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
            //openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
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

        private void button4_Click(object sender, EventArgs e)
        {
            //將資料夾內所有檔案改變大小並存檔
            float scale = float.Parse(textBox2.Text);
            if (scale == 0)
            {
                MessageBox.Show("Scale must not be zero.", "Invalid Scale", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            this.Refresh();

            DirectoryInfo dir_info = new DirectoryInfo(textBox1.Text);
            foreach (FileInfo file_info in dir_info.GetFiles())
            {
                try
                {
                    string ext = file_info.Extension.ToLower();
                    if ((ext == ".bmp") || (ext == ".gif") ||
                        (ext == ".jpg") || (ext == ".jpeg") ||
                        (ext == ".png"))
                    {
                        richTextBox1.Text += "處理檔案 : " + file_info.FullName + "\n";
                        Bitmap bm = new Bitmap(file_info.FullName);

                        Rectangle from_rect = new Rectangle(0, 0, bm.Width, bm.Height);

                        int wid2 = (int)Math.Round(scale * bm.Width);
                        int hgt2 = (int)Math.Round(scale * bm.Height);
                        Bitmap bm2 = new Bitmap(wid2, hgt2);
                        Rectangle dest_rect = new Rectangle(0, 0, wid2, hgt2);
                        using (Graphics gr = Graphics.FromImage(bm2))
                        {
                            gr.InterpolationMode = InterpolationMode.HighQualityBicubic;
                            gr.DrawImage(bm, dest_rect, from_rect, GraphicsUnit.Pixel);
                        }

                        string new_name = file_info.FullName;
                        new_name = new_name.Substring(0, new_name.Length - ext.Length);
                        new_name += "_resized" + ext;
                        SaveImage(bm2, new_name);
                    } // if it's a graphic extension
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error processing file '" +
                        file_info.Name + "'\n" + ex.Message,
                        "Error",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
                }
            } // foreach file_info
            richTextBox1.Text += "處理檔案完成\n";
        }

        // Save the file with the appropriate format.
        public void SaveImage(Image image, string filename)
        {
            string extension = Path.GetExtension(filename);
            switch (extension.ToLower())
            {
                case ".bmp":
                    image.Save(filename, ImageFormat.Bmp);
                    break;
                case ".exif":
                    image.Save(filename, ImageFormat.Exif);
                    break;
                case ".gif":
                    image.Save(filename, ImageFormat.Gif);
                    break;
                case ".jpg":
                case ".jpeg":
                    image.Save(filename, ImageFormat.Jpeg);
                    break;
                case ".png":
                    image.Save(filename, ImageFormat.Png);
                    break;
                case ".tif":
                case ".tiff":
                    image.Save(filename, ImageFormat.Tiff);
                    break;
                default:
                    throw new NotSupportedException("Unknown file extension " + extension);
            }
        }

        /// <summary>
        ///  圖片寬高設定 
        /// </summary>
        /// <param name="imgToResize"></param>
        /// <param name="size"></param>
        /// <returns></returns>
        public Image ResizeImage(Image img_old, Size size)
        {
            int W1 = img_old.Width;
            int H1 = img_old.Height;
            int W2 = size.Width;
            int H2 = size.Height;

            float nPercent = 0;
            float nPercentW = 0;
            float nPercentH = 0;

            //計算寬度的縮放比例
            nPercentW = ((float)W2 / (float)W1);
            //計算高度的縮放比例
            nPercentH = ((float)H2 / (float)H1);

            if (nPercentH < nPercentW)
                nPercent = nPercentH;
            else
                nPercent = nPercentW;

            //期望的寬度
            int W3 = (int)(W1 * nPercent);
            //期望的高度
            int H3 = (int)(H1 * nPercent);

            Bitmap b = new Bitmap(W3, H3);
            Graphics g = Graphics.FromImage((Image)b);
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;
            //繪製圖像
            g.DrawImage(img_old, 0, 0, W3, H3);
            g.Dispose();

            richTextBox1.Text += "W1 = " + W1.ToString() + ", H1 = " + H1.ToString() + "\n";
            richTextBox1.Text += "W2 = " + W2.ToString() + ", H2 = " + H2.ToString() + "\n";
            richTextBox1.Text += "W3 = " + W3.ToString() + ", H3 = " + H3.ToString() + "\n";
            richTextBox1.Text += "PW = " + nPercentW.ToString() + ", PH = " + nPercentH.ToString() + ", P = " + nPercent.ToString() + "\n";

            return (Image)b;
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {

        }

        private void trackBar1_MouseDown(object sender, MouseEventArgs e)
        {

        }

        private void trackBar1_MouseUp(object sender, MouseEventArgs e)
        {
            int value = trackBar1.Value;

            richTextBox1.Text += "放大倍率 : " + (value * 100 / 10).ToString() + " %\n";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);

            int W1 = image.Width;
            int H1 = image.Height;

            int W2 = W1 * value / 10;
            int H2 = H1 * value / 10;

            Size new_size = new Size(W2, H2);
            pictureBox2.Image = ResizeImage(image, new_size);

        }
    }
}
