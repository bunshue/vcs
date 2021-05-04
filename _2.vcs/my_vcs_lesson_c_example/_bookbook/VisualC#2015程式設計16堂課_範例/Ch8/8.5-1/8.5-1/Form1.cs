using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void sizeMenu_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (sizeMenu.Text == "Normal")
                pictureBox.SizeMode = PictureBoxSizeMode.Normal;
            else if (sizeMenu.Text == "StretchImage")
                pictureBox.SizeMode = PictureBoxSizeMode.StretchImage;
            else if (sizeMenu.Text == "AutoSize")
                pictureBox.SizeMode = PictureBoxSizeMode.AutoSize;
            else if (sizeMenu.Text == "CenterImage")
                pictureBox.SizeMode = PictureBoxSizeMode.CenterImage;
            else if (sizeMenu.Text == "Zoom")
                pictureBox.SizeMode = PictureBoxSizeMode.Zoom;
        }

        private void fileButton_Click(object sender, EventArgs e)
        {
            if (fileDialog.ShowDialog() == DialogResult.OK)
                pictureBox.ImageLocation = fileDialog.FileName;

        }

    }
}
