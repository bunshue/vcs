using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace TailorAnimation
{
    public partial class Form1 : Form
    {
        string strPath;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            strPath = Application.StartupPath.Substring(0,Application.StartupPath.Substring(0, Application.StartupPath.LastIndexOf("\\")).LastIndexOf("\\"));
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            pictureBox1.Image = Image.FromFile(strPath + @"\image\1.jpg");
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Random r = new Random();
            pictureBox1.Image = Image.FromFile(strPath + @"\image\" + r.Next(1,5) + ".jpg");
        }
    }
}