using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using AForge.Video;
using AForge.Video.DirectShow;

namespace WebcamSecurity
{
    public partial class MainForm : Form
    {
        // Refrence to cameraMonitors of all 4 cams
        CameraMonitor[] CamMonitor = new CameraMonitor[4];  //物件陣列
        // Indexed arrays containing referces to the user interface components
        // so they can be easily accessed later on
        PictureBox[] DisplayReference = new PictureBox[4];

        // the FilterInfoCollection is where we get information about VideoCaptureDevices
        private FilterInfoCollection USBWebcams = null;
        int webcam_count = 0;

        public MainForm()
        {
            InitializeComponent();
            // linking the user interface componets to the arrays
            this.DisplayReference[0] = this.pictureBox1;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int i;
            show_item_location();

            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //實例化對象

            webcam_count = USBWebcams.Count;

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
                this.CamMonitor[i] = new CameraMonitor(this.DisplayReference[i], USBWebcams[i].MonikerString, "Camera" + (i + 1));

                /*
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";
                richTextBox1.Text += "長名 : " + USBWebcams[i].MonikerString + "\n";
                */

                this.CamMonitor[i].RecordingPath = this.RecordingPathInput.Text;
            }
        }

        void show_item_location()
        {
            int W = 640;
            int H = 480;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 50;
            int dy = H + 50;

            pictureBox1.Size = new Size(W, H);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            W = 120;
            H = 30;
            button1.Size = new Size(W, H);

            //W = 640;
            H = 480;
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H + 10);

            richTextBox1.Size = new Size(200, 600);
            richTextBox1.Location = new Point(1000, 50);
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            //離開程式前, 關閉相機(錄影與播放)
            for (int i = 0; i < 4; i++)
            {
                try
                {
                    this.CamMonitor[i].StopRecording();
                    this.CamMonitor[i].StopCapture();
                }
                catch (Exception ex)
                {
                }
            }
        }

        // The Rest is User Interface EventHandling
        private void button1_Click(object sender, EventArgs e)
        {
            if (this.CamMonitor[0].IsRecording)
            {
                this.CamMonitor[0].StopRecording();
                this.CamMonitor[0].forceRecord = false;
                ((Button)sender).Text = "Record";
            }
            else
            {
                this.CamMonitor[0].StartRecording();
                this.CamMonitor[0].forceRecord = true;
                ((Button)sender).Text = "Stop";
            }
        }

        private void toggleOption(int camIndex, int optionIndex, bool value)
        {
            switch (optionIndex)
            {
                case 0:
                    this.CamMonitor[camIndex].MotionDetection = value;
                    break;
                case 1:
                    this.CamMonitor[camIndex].RecordOnMotion = value;
                    break;
                case 2:
                    this.CamMonitor[camIndex].BeepOnMotion = value;
                    break;
            }
        }

        private void MotionDetection1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(0, 0, true);
            }
            else
            {
                this.toggleOption(0, 0, false);
            }
        }

        private void AutoRecord1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(0, 1, true);
            }
            else
            {
                this.toggleOption(0, 1, false);
            }
        }

        private void BeepOnMotionCheck1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(0, 2, true);
            }
            else
            {
                this.toggleOption(0, 2, false);
            }
        }
    }
}
