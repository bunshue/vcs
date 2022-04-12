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

        private void button1_Click(object sender, EventArgs e)
        {
            string foldername = @"C:\______test_files\__pic\_pic_combine";

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
    }
}
