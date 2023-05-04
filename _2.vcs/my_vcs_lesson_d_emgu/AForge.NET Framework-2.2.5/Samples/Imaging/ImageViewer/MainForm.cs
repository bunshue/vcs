using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;

using AForge.Imaging.Formats;

namespace ImageViewer
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files1\elephant.jpg";

            try
            {
                ImageInfo imageInfo = null;

                pictureBox.Image = ImageDecoder.DecodeFromFile(filename, out imageInfo);

                propertyGrid.SelectedObject = imageInfo;
                propertyGrid.ExpandAllGridItems();

                richTextBox1.Text += "Number of bits per image's pixel : " + imageInfo.BitsPerPixel.ToString() + "\n";
                richTextBox1.Text += "Frame's index : " + imageInfo.FrameIndex.ToString() + "\n";
                richTextBox1.Text += "W : " + imageInfo.Width.ToString() + "\n";
                richTextBox1.Text += "H : " + imageInfo.Height.ToString() + "\n";
                richTextBox1.Text += "Total frames in the image : " + imageInfo.TotalFrames.ToString() + "\n";
            }
            catch (NotSupportedException ex)
            {
                MessageBox.Show("Image format is not supported: " + ex.Message, "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (ArgumentException ex)
            {
                MessageBox.Show("Invalid image: " + ex.Message, "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch
            {
                MessageBox.Show("Failed loading the image", "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
