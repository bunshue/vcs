using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for Directory
using System.Drawing.Imaging;  // for ImageFormat
using System.Drawing.Drawing2D;  // for GraphicsPath

namespace vcs_CombinePicture
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);


            pictureBox1.Size = new Size(830, 690);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);





            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1390, 750);
            this.Text = "vcs_CombinePicture";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals";

            richTextBox1.Text += "撈出資料夾 " + foldername + " 內所有圖片檔案合併\n";

            // Get the picture files in the source directory.
            List<string> files = new List<string>();
            foreach (string filename in Directory.GetFiles(foldername))
            {
                int pos = filename.LastIndexOf('.');
                string extension = filename.Substring(pos).ToLower();
                if ((extension == ".bmp") ||
                    (extension == ".jpg") ||
                    (extension == ".jpeg") ||
                    (extension == ".png") ||
                    (extension == ".tif") ||
                    (extension == ".tiff") ||
                    (extension == ".gif"))
                    files.Add(filename);
            }

            int num_images = files.Count;
            if (num_images == 0)
            {
                Cursor = Cursors.Default;
                MessageBox.Show("Selected 0 files");
                return;
            }

            // Load the images.
            Bitmap[] images = new Bitmap[files.Count];
            for (int i = 0; i < num_images; i++)
            {
                images[i] = new Bitmap(files[i]);
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 張圖\t" + files[i] + "\n";
            }

            // Find the largest width and height.
            int max_wid = 0;
            int max_hgt = 0;
            for (int i = 0; i < num_images; i++)
            {
                if (max_wid < images[i].Width) max_wid = images[i].Width;
                if (max_hgt < images[i].Height) max_hgt = images[i].Height;
            }

            // Make the result bitmap.
            int num_cols = int.Parse(textBox1.Text);
            int num_rows = int.Parse(textBox2.Text);

            richTextBox1.Text += "最初 C = " + num_cols.ToString() + ", R = " + num_rows.ToString() + "\n";

            if (num_images <= num_cols)
            {
                num_cols = num_images;
                num_rows = 1;
            }

            if ((num_images / num_cols) < num_rows)
            {
                num_rows = num_images / num_cols;
                if ((num_images % num_cols) > 0)
                    num_rows += 1;
            }

            richTextBox1.Text += "決定 C = " + num_cols.ToString() + ", R = " + num_rows.ToString() + "\n";

            int margin = int.Parse(textBox3.Text);
            int wid = max_wid * num_cols + margin * (num_cols - 1);
            int hgt = max_hgt * num_rows + margin * (num_rows - 1);

            richTextBox1.Text += "W = " + wid.ToString() + "\n";
            richTextBox1.Text += "H = " + hgt.ToString() + "\n";

            Bitmap bm = new Bitmap(wid, hgt);

            // Place the images on it.
            Graphics gr = Graphics.FromImage(bm);
            //gr.Clear(picBackground.BackColor);

            int x = 0;
            int y = 0;
            for (int i = 0; i < num_images; i++)
            {
                gr.DrawImage(images[i], x, y);
                x += max_wid + margin;
                if (x >= wid)
                {
                    y += max_hgt + margin;
                    x = 0;
                }
            }

            // Save the result.
            //存檔
            if (bm != null)
            {
                string filename0 = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename0 + ".jpg";
                String filename2 = filename0 + ".bmp";
                String filename3 = filename0 + ".png";


                bm.Save(@filename1, ImageFormat.Jpeg);
                bm.Save(@filename2, ImageFormat.Bmp);
                bm.Save(@filename3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                richTextBox1.Text += "已存檔 : " + filename3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";


        }


        enum ImageMergeOrientation
        {
            Horizontal,
            Vertical
        }

        private void CombineImages(FileInfo[] files, ImageMergeOrientation mergeType = ImageMergeOrientation.Vertical)
        {
            //change the location to store the final image.
            // URL：http://www.bianceng.cn/Programming/csharp/201410/45751.htm
            var imgs = files.Select(f => Image.FromFile(f.FullName));

            var finalWidth = mergeType == ImageMergeOrientation.Horizontal ?
                imgs.Sum(img => img.Width) :
                imgs.Max(img => img.Width);

            var finalHeight = mergeType == ImageMergeOrientation.Vertical ?
                imgs.Sum(img => img.Height) :
                imgs.Max(img => img.Height);

            var bitmap1 = new Bitmap(finalWidth, finalHeight);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(SystemColors.AppWorkspace);

            var width = finalWidth;
            var height = finalHeight;
            var nIndex = 0;
            foreach (FileInfo file in files)
            {
                Image img = Image.FromFile(file.FullName);
                if (nIndex == 0)
                {
                    g.DrawImage(img, new Point(0, 0));
                    nIndex++;
                    width = img.Width;
                    height = img.Height;
                }
                else
                {
                    switch (mergeType)
                    {
                        case ImageMergeOrientation.Horizontal:
                            g.DrawImage(img, new Point(width, 0));
                            width += img.Width;
                            break;
                        case ImageMergeOrientation.Vertical:
                            g.DrawImage(img, new Point(0, height));
                            height += img.Height;
                            break;
                        default:
                            throw new ArgumentOutOfRangeException("mergeType");
                    }
                }
                img.Dispose();
            }
            g.Dispose();

            string filename = string.Empty;
            if (mergeType == ImageMergeOrientation.Vertical)
            {
                filename = Application.StartupPath + "\\vertical_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            }
            else
            {
                filename = Application.StartupPath + "\\horizontal_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            }

            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(filename, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
            bitmap1.Dispose();
        }


        private void button2_Click(object sender, EventArgs e)
        {
            //把多個圖片合成為一個圖片
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals";

            var images = new DirectoryInfo(foldername).GetFiles("*.jpg", SearchOption.TopDirectoryOnly);

            CombineImages(images, ImageMergeOrientation.Horizontal);
            CombineImages(images, ImageMergeOrientation.Vertical);
        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
            //合併圖

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z01.jpg";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z02.jpg";
            string filename3 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z03.jpg";
            string filename4 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z04.jpg";
            string filename5 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z05.jpg";
            string filename6 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z06.jpg";
            string filename7 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z07.jpg";
            string filename8 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z08.jpg";
            string filename9 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z09.jpg";
            string filename10 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z10.jpg";
            string filename11 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z11.jpg";
            string filename12 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\z12.jpg";

            // 假設有公司 logo 與名稱
            //string[] logos = { "samsung.png", "google.png", "apple.png" };
            //string[] names = { "Samsung 三星", "Google 谷歌", "Apple 蘋果" };

            string[] names = { "鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬" };

            //string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals"; // logo 圖片所在資料夾
            //string[] files = Directory.GetFiles(foldername, "*.png");
            string[] files = {
                                 filename1, filename2, filename3, filename4,
                                 filename5, filename6, filename7, filename8,
                                 filename9, filename10, filename11, filename12
                             };

            int cols = 4;
            int rows = (int)Math.Ceiling(files.Length / (double)cols);
            int cellWidth = 200, cellHeight = 150;
            int width = cols * cellWidth;
            int height = rows * cellHeight;

            Bitmap bmp = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(bmp);
            g.Clear(Color.White);
            g.SmoothingMode = SmoothingMode.AntiAlias;
            Font font = new Font("Segoe UI", 16, FontStyle.Bold);
            StringFormat sf = new StringFormat { Alignment = StringAlignment.Center };

            for (int i = 0; i < files.Length; i++)
            {
                int col = i % cols;
                int row = i / cols;
                int x = col * cellWidth;
                int y = row * cellHeight;

                // 背景格
                Brush b = new SolidBrush(Color.FromArgb(240, 240, 240));
                g.FillRoundedRectangle(b, new Rectangle(x + 10, y + 10, cellWidth - 20, cellHeight - 20), 20);

                // 載入 logo
                Image logo = Image.FromFile(files[i]);
                g.DrawImage(logo, x + 30, y + 20, 140, 80);

                // 顯示檔名（不含副檔名）
                //string name = Path.GetFileNameWithoutExtension(files[i]);
                g.DrawString(names[i], font, Brushes.Black, new RectangleF(x, y + cellHeight - 40, cellWidth, 40), sf);
            }
            bmp.Save("tmp_組合圖1.png");
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
            //載入資料夾下的所有圖檔，垂直合併成一圖
            //載入資料夾下的所有圖檔，垂直合併成一圖

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_scenery";
            string[] files = Directory.GetFiles(foldername, "*.jpg");

            richTextBox1.Text += "共找到 : " + files.Length.ToString() + " 個檔案\n";

            int N = files.Length;

            int cellWidth = 200;
            int cellHeight = 150;
            int width = cellWidth * 1;
            int height = cellHeight * N;

            Bitmap bmp = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(bmp);
            g.Clear(Color.White);
            g.SmoothingMode = SmoothingMode.AntiAlias;
            Font font = new Font("Segoe UI", 16, FontStyle.Bold);
            StringFormat sf = new StringFormat { Alignment = StringAlignment.Center };

            for (int i = 0; i < files.Length; i++)
            {
                int row = i;
                int x = 0;
                int y = row * cellHeight;

                Image logo = Image.FromFile(files[i]);
                //g.DrawImage(logo, x + 30, y + 20, 140, 80);
                g.DrawImage(logo, x, y, cellWidth, cellHeight);
            }
            bmp.Save("tmp_組合圖2.png");
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }
    }

    public static class GraphicsExtensions
    {
        public static void FillRoundedRectangle(this Graphics g, Brush brush, Rectangle rect, int radius)
        {
            GraphicsPath path = new GraphicsPath();
            path.AddArc(rect.X, rect.Y, radius, radius, 180, 90);
            path.AddArc(rect.Right - radius, rect.Y, radius, radius, 270, 90);
            path.AddArc(rect.Right - radius, rect.Bottom - radius, radius, radius, 0, 90);
            path.AddArc(rect.X, rect.Bottom - radius, radius, radius, 90, 90);
            path.CloseFigure();
            g.FillPath(brush, path);
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

