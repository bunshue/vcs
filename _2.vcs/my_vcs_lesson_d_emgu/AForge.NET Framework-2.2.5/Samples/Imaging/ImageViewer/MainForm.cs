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
            string filename = @"C:\______test_files\elephant.jpg";

            try
            {
                ImageInfo imageInfo = null;

                pictureBox.Image = ImageDecoder.DecodeFromFile(filename, out imageInfo);

                propertyGrid.SelectedObject = imageInfo;
                propertyGrid.ExpandAllGridItems();
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
