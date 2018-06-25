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

namespace test_web_cam
{
    public partial class Form1 : Form
    {
        private Capture cap = null;
        public Form1()
        {
            InitializeComponent();
        }

        void Application_Idle(object sender, EventArgs e)
        {
            Image<Bgr, Byte> frame = cap.QueryFrame();
            pictureBox1.Image = frame.ToBitmap();
        
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            cap = new Capture(0);
            Application.Idle += new EventHandler(Application_Idle);
        }
    }
}
