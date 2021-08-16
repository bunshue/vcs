using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WebCamPictureBox_Sample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (this.webCamPictureBox1.TestConnect())
            {
                MessageBox.Show("WebCam connect state is ok");
            }
            else
            {
                MessageBox.Show("WebCam connect state is error");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
			this.webCamPictureBox1.Start();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.webCamPictureBox1.Stop();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.webCamPictureBox2.Image = this.webCamPictureBox1.Image;
        }
      
        private void button5_Click(object sender, EventArgs e)
        {
            SaveFileDialog sf = new SaveFileDialog();
            sf.Filter = "πœ¿…|*.bmp";
            if (sf.ShowDialog() == DialogResult.OK)
            {
                this.webCamPictureBox1.Image.Save(sf.FileName );
            }
        }

        private void webCamPictureBox1_WebCamConnectStateChanged(object sender, EventArgs e)
        {
            this.toolStripStatusLabel2.Text = this.webCamPictureBox1.IsStarted ? "Start" : "Stop"; 
        }
    }
}