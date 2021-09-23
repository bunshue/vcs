using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using AForge.Video;
using AForge.Video.DirectShow;

namespace vcs_WebCam2
{
    public partial class Form1 : Form
    {
        WebCam webcam;

        private FilterInfoCollection USBWebcams = null;
        int webcam_count = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //離開程式前, 關閉相機
            try
            {
                this.webcam.StopCapture();
            }
            catch (Exception ex)
            {
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //ST

            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //實例化對象

            webcam_count = USBWebcams.Count;

            int i;
            /*
            richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";

            richTextBox1.Text += "USBWebcams.Capacity : " + USBWebcams.Capacity.ToString() + "\n";
            richTextBox1.Text += "USBWebcams.Count : " + USBWebcams.Count.ToString() + "\n";

            for (i = 0; i < webcam_count; i++)
            {
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";
                richTextBox1.Text += "長名 : " + USBWebcams[i].MonikerString + "\n";
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            if (webcam_count > 0)
            {
                i = 0;
                string camera_name = USBWebcams[i].MonikerString;   //長名
                this.webcam = new WebCam(pictureBox1, camera_name, "第 " + (i + 1).ToString() + " 台攝影機");

                /*
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";
                richTextBox1.Text += "長名 : " + USBWebcams[i].MonikerString + "\n";
                */
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //SP
            try
            {
                this.webcam.StopCapture();
            }
            catch (Exception ex)
            {
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";
            int i;
            i = 0;

            richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
            richTextBox1.Text += "cameraName\t" + this.webcam.cameraName.ToString() + "\n";
            richTextBox1.Text += "CamMonitor\t" + this.webcam.ToString() + "\n";
        }
    }
}

