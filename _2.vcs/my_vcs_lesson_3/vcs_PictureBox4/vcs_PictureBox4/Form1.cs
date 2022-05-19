using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureBox4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取圖檔
            string filename = @"C:\______test_files\bear.jpg";

            Image myImage = System.Drawing.Image.FromFile(filename);
            pictureBox1.Image = myImage;
            pictureBox1.Height = myImage.Height;
            pictureBox1.Width = myImage.Width;
        }
    }
}
