using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.Util;
using Emgu.CV.Structure;


namespace My_EMGU_Program
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";

            //Load the Image
            Image<Bgr, Byte> My_Image = new Image<Bgr, byte>(filename);

            //Display the Image
            pictureBox1.Image = My_Image.ToBitmap();
        }
    }
}
