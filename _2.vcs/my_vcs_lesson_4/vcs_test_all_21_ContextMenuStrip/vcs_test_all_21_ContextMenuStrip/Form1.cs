using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_21_ContextMenuStrip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\picture1.jpg";

            //same
            //Image img = Image.FromFile(filename);
            //pictureBox1.Image = img;

            //same
            //pictureBox1.Image = Image.FromFile(filename); //載入圖檔，由檔案

            //same
            //Bitmap bitmap1 = new Bitmap(filename);
            //pictureBox1.Image = bitmap1;

            //same
            //Image img = Bitmap.FromFile(filename);
            //pictureBox1.Image = img;

            //same
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            //pictureBox1.Image = bitmap1;

            //same
            pictureBox1.Image = new Bitmap(filename);

            //pictureBox1.ImageLocation = filename;   //可顯示圖片 但無法抓出圖片的相關資訊

            int width = pictureBox1.Image.Width;
            int height = pictureBox1.Image.Height;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Size = new Size(width, height);

            this.Text = "在圖上按右鍵測試ContextMenuStrip";
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            //檢查滑鼠右鍵
            if (e.Button == MouseButtons.Right)
            {
                // Display the context menu.
                ShowContextMenu(e.Location);
            }
            return;
        }

        // Prepare the context menu and display it.
        private void ShowContextMenu(Point location)
        {
            // Display the context menu.
            contextMenuStrip1.Show(pictureBox1, location);
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem1.Text + "\n";
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem2.Text + "\n";
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem3.Text + "\n";
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem4.Text + "\n";
        }

        private void toolStripMenuItem5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem5.Text + "\n";
        }

        private void toolStripMenuItem6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem6.Text + "\n";
        }

        private void toolStripMenuItem7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem7.Text + "\n";
        }
    }
}
