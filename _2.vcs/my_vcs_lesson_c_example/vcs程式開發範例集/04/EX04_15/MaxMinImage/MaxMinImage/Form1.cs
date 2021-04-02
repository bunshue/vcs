using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace MaxMinImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        Image myImage;
        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";
            openFileDialog1.ShowDialog();
            myImage = System.Drawing.Image.FromFile(openFileDialog1.FileName);
            pictureBox1.Image = myImage;
            pictureBox1.Height = myImage.Height;
            pictureBox1.Width = myImage.Width;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                pictureBox1.Height = Convert.ToInt32(myImage.Height * Convert.ToSingle(textBox1.Text.Trim()));
                pictureBox1.Width = Convert.ToInt32(myImage.Width * Convert.ToSingle(textBox1.Text.Trim()));
            }
            catch { }
        }
    }
}