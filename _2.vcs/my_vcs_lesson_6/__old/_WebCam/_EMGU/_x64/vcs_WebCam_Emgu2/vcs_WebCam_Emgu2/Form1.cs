using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.CV.Structure;

namespace vcs_WebCam_Emgu2
{
    public partial class Form1 : Form
    {
        private Capture cap1 = null;
        private Capture cap2 = null;
        private Capture cap3 = null;
        private Capture cap4 = null;

        public Form1()
        {
            InitializeComponent();
        }

        void Application_Idle(object sender, EventArgs e)
        {
            Image<Bgr, Byte> image1 = cap1.QueryFrame(); // 去query該畫面
            Image<Bgr, Byte> image2 = cap2.QueryFrame(); // 去query該畫面
            Image<Bgr, Byte> image3 = cap3.QueryFrame(); // 去query該畫面
            Image<Bgr, Byte> image4 = cap4.QueryFrame(); // 去query該畫面

            pictureBox1.Image = image1.ToBitmap(); // 把畫面轉換成bitmap型態，在餵給pictureBox元件
            pictureBox2.Image = image2.ToBitmap(); // 把畫面轉換成bitmap型態，在餵給pictureBox元件
            pictureBox3.Image = image3.ToBitmap(); // 把畫面轉換成bitmap型態，在餵給pictureBox元件
            pictureBox4.Image = image4.ToBitmap(); // 把畫面轉換成bitmap型態，在餵給pictureBox元件
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            cap1 = new Capture(1);
            cap2 = new Capture(1);
            cap3 = new Capture(1);
            cap4 = new Capture(1);
            cap2.FlipHorizontal = true;
            cap3.FlipVertical = true;
            cap4.FlipHorizontal = true;
            cap4.FlipVertical = true;

            //richTextBox1.Text += "width = " + cap1.Width.ToString() + "\n";
            //richTextBox1.Text += "height = " + cap1.Height.ToString() + "\n";
            Application.Idle += new EventHandler(Application_Idle);
        }
    }
}
