using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;

namespace vcs_CombinePicture2
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

        private void button1_Click(object sender, EventArgs e)
        {
            //把多個圖片合成為一個圖片
            const string foldername = @"C:\______test_files\_pic_combine";

            //const string folderPath = @"C:\______test_files\_pic_combine";
            var images = new DirectoryInfo(foldername).GetFiles("*.jpg", SearchOption.TopDirectoryOnly);

            CombineImages(images, ImageMergeOrientation.Horizontal);
            CombineImages(images, ImageMergeOrientation.Vertical);
        }
    }
}
