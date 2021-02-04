using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

namespace vcs_PictureBox4b_Orient
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Restore the saved file name.
        private void Form1_Load(object sender, EventArgs e)
        {
            txtFile.Text = Properties.Settings.Default.Filename;
        }

        // Save the current file name.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.Filename = txtFile.Text;
            Properties.Settings.Default.Save();
        }

        // Let the user select a file.
        private void btnPickFile_Click(object sender, EventArgs e)
        {
            ofdFile.FileName = txtFile.Text;
            if (ofdFile.ShowDialog() == DialogResult.OK)
            {
                txtFile.Text = ofdFile.FileName;
                picOriginal.Image = null;
                picOrientation.Image = null;
                lblOrientation.Text = "";
                richTextBox1.Text += "\n";
            }
        }

        // Open the file and read its orientation information.
        private void btnOpen_Click(object sender, EventArgs e)
        {
            if (txtFile.Text.Length == 0)
                return;

            // Open the file.
            Bitmap bm = new Bitmap(txtFile.Text);
            picOriginal.Image = bm;

            // Get the PropertyItems property from image.
            ExifStuff.ExifOrientations orientation = ExifStuff.ImageOrientation(bm);
            lblOrientation.Text = orientation.ToString();
            richTextBox1.Text += orientation.ToString() + "\n";
            picOrientation.Image = ExifStuff.OrientationImage(orientation);


        }
    }
}
