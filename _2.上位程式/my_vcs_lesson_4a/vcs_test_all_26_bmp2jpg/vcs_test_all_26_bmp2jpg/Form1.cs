using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_test_all_26_bmp2jpg
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Bitmap bitmap;
        string save_jpg_filename = null;
        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "*.bmp|*.bmp";
            ofd.Title = "打開bmp檔案";
            ofd.Multiselect = false;
            if (ofd.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "開啟檔案: " + ofd.FileName + ", 並顯示之\n";
                if (bitmap != null)
                    bitmap.Dispose();
                string filename = ofd.FileName;
                bitmap = new Bitmap(filename);
                pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                pictureBox1.Image = bitmap;
            }
            else
                richTextBox1.Text += "未選取檔案\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SaveFileDialog sfd = new SaveFileDialog();
            sfd.Title = "轉成jpg檔案";
            sfd.OverwritePrompt = true;
            sfd.CheckPathExists = true;
            sfd.Filter = "*.jpg|*.jpg";
            if (sfd.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "儲存檔案: " + sfd.FileName + "\n";
                save_jpg_filename = sfd.FileName;
            }
            else
                richTextBox1.Text += "未選取檔案\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (save_jpg_filename == null)
            {
                richTextBox1.Text += "未指定jpg檔，不能轉換\n";
                return;
            }
                
            if (bitmap != null)
            {
                bitmap.Save(save_jpg_filename, ImageFormat.Jpeg);
                richTextBox1.Text += "轉換完成\n";
            }
            else
                richTextBox1.Text += "無BMP檔，不能轉換\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            bitmap.Dispose();
            bitmap = null;
            pictureBox1.Image = null;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            save_jpg_filename = null;
        }
    }
}
