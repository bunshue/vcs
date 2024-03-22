using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

namespace vcs_PictureResize3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery";
        }

        // Process the files in the selected directory.
        private void button1_Click(object sender, EventArgs e)
        {
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
                    throw new NotSupportedException(                        "Unknown file extension " + extension);
            }
        }
    }
}
