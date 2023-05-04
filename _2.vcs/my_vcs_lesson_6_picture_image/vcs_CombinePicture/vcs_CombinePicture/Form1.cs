using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory
using System.Drawing.Imaging;   //for ImageFormat

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

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string foldername = @"C:\______test_files1\__pic\_animals";

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
            using (Graphics gr = Graphics.FromImage(bm))
            {
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
            string foldername = @"C:\______test_files1\__pic\_animals";

            var images = new DirectoryInfo(foldername).GetFiles("*.jpg", SearchOption.TopDirectoryOnly);

            CombineImages(images, ImageMergeOrientation.Horizontal);
            CombineImages(images, ImageMergeOrientation.Vertical);
        }
    }
}
