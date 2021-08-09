using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_WebCam_Capture
{
    public partial class Form1 : Form
    {
        WebCam webcam;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            webcam = new WebCam();
            webcam.InitializeWebCam(ref pictureBox1, ref richTextBox1);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            webcam.Start();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            webcam.Stop();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            webcam.Continue();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = pictureBox1.Image;

            if (pictureBox2.Image != null)
            {
                string filename = Application.StartupPath + "\\image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                Helper.SaveImageCapture(filename, pictureBox2.Image);
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            webcam.ResolutionSetting();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            webcam.AdvanceSetting();
        }
    }
}

