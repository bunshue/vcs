using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace LookImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void 開啟ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";
            openFileDialog1.ShowDialog();
            Image myImage = System.Drawing.Image.FromFile(openFileDialog1.FileName);
            pictureBox1.Image = myImage;
            pictureBox1.Height = myImage.Height;
            pictureBox1.Width = myImage.Width;
            textBox1.Text = openFileDialog1.FileName.Substring(openFileDialog1.FileName.LastIndexOf("\\") + 1,
                openFileDialog1.FileName.LastIndexOf(".") - openFileDialog1.FileName.LastIndexOf("\\")-1);
            textBox2.Text=openFileDialog1.FileName.Substring(openFileDialog1.FileName.LastIndexOf(".") + 1, 
                openFileDialog1.FileName.Length - openFileDialog1.FileName.LastIndexOf(".") - 1);
        }

        private void 退出ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}