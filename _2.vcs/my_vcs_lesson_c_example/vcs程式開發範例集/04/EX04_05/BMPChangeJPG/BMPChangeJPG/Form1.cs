using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.IO;
using System.Drawing.Imaging;

namespace BMPChangeJPG
{
    public partial class Form1 : Form
    {
        Bitmap bitmap;
        public Form1()
        {
            InitializeComponent();
        }

        private void buttonOpen_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.Filter = "*.bmp|*.bmp";
            openFileDialog.Title = "打開圖像文件";
            openFileDialog.Multiselect = false;
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                if (bitmap != null)
                {
                    bitmap.Dispose();
                }
                string fileName = openFileDialog.FileName;
                bitmap = new Bitmap(fileName);
                if (bitmap.Width > bitmap.Height)
                {
                    pictureBox.Width = panel2.Width;
                    pictureBox.Height = (int)((double)bitmap.Height * panel2.Width / bitmap.Width);
                }
                else
                {
                    pictureBox.Height = panel2.Height;
                    pictureBox.Width = (int)((double)bitmap.Width * panel2.Height / bitmap.Height);
                }
                pictureBox.Image = bitmap;
                FileInfo f = new FileInfo(fileName);
                this.Text = "圖像轉換:" + f.Name;
                this.label1.Text = f.Name;
                buttonConvert.Enabled = true;
            }
        }

        private void buttonConvert_Click(object sender, EventArgs e)
        {
            if (comboBox.SelectedItem == null)
            {
                return;
            }
            else
            {
                SaveFileDialog saveFileDialog = new SaveFileDialog();
                saveFileDialog.Title = "轉化為:";
                saveFileDialog.OverwritePrompt = true;
                saveFileDialog.CheckPathExists = true;
                saveFileDialog.Filter = comboBox.Text + "|" + comboBox.Text;
                if (saveFileDialog.ShowDialog() == DialogResult.OK)
                {
                    string fileName = saveFileDialog.FileName;
                    bitmap.Save(fileName, ImageFormat.Jpeg);
                    FileInfo f = new FileInfo(fileName);
                    this.Text = "圖像轉換:" + f.Name;
                    label1.Text = f.Name;
                }
            }
        }

        private void panel2_Resize(object sender, EventArgs e)
        {
            pictureBox.Top = panel1.Top;
            pictureBox.Left = panel1.Left;
            if (bitmap != null)
            {
                if (bitmap.Width > bitmap.Height)
                {
                    pictureBox.Width = panel2.Width;
                    pictureBox.Height = (int)((double)bitmap.Height * panel2.Width / bitmap.Width);
                }
                else
                {
                    pictureBox.Height = panel2.Height;
                    pictureBox.Width = (int)((double)bitmap.Width * panel2.Height / bitmap.Height);
                }
            }
            else
            {
                pictureBox.Width = panel2.Width;
                pictureBox.Height = panel2.Height;
            }
            pictureBox.Refresh();
        }
    }
}