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
    // Main form's class
    public partial class MainForm : Form
    {
        // Class constructor
        public MainForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog.InitialDirectory = @"C:\______test_files\";
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    ImageInfo imageInfo = null;

                    pictureBox.Image = ImageDecoder.DecodeFromFile(openFileDialog.FileName, out imageInfo);

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
}
