using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using Emgu.CV;
//using Emgu.CV.Util;
using Emgu.CV.Structure;
using Emgu.Util;
using Emgu.CV.CvEnum;



//using Emgu.CV;
//using Emgu.CV.Structure;
//using Emgu.CV.CvEnum;
using System.Runtime.InteropServices;
using System.Diagnostics;
using Emgu.CV.Util;


namespace _EmguTest1
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Image<Bgr, byte> img;
            img = new Image<Bgr, byte>(filename);
            //imageBox1.Image = img;
            pictureBox1.Image = img.ToBitmap();


            //MCvMat mImg = (MCvMat)Marshal.PtrToStructure(img.Ptr, typeof(MCvMat));
            //byte* ptr = (byte*)mImg.Data.ToPointer();
            
            

        }

        private void button2_Click(object sender, EventArgs e)
        {



        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }
    }
}

