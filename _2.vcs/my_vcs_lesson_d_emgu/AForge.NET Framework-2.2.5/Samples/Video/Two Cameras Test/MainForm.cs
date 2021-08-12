// Two Cameras Test sample application
// AForge.NET framework
// http://www.aforgenet.com/framework/
//
// Copyright © AForge.NET, 2006-2011
// contacts@aforgenet.com
//

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;

using AForge.Video;
using AForge.Video.DirectShow;

namespace TwoCamerasTest
{
    public partial class MainForm : Form
    {
        // list of video devices
        FilterInfoCollection videoDevices;
        public MainForm()
        {
            InitializeComponent();
        }



        private void MainForm_Load(object sender, EventArgs e)
        {

            // show device list
            try
            {
                // enumerate video devices
                videoDevices = new FilterInfoCollection(FilterCategory.VideoInputDevice);

                richTextBox1.Text += "取得device count : " + videoDevices.Count.ToString() + "\n";

                if (videoDevices.Count == 0)
                {
                    throw new Exception();
                }

                for (int i = 1, n = videoDevices.Count; i <= n; i++)
                {
                    string cameraName = i + " : " + videoDevices[i - 1].Name;

                    camera1Combo.Items.Add(cameraName);

                    richTextBox1.Text += "i = " + i.ToString() + "\t" + cameraName + "\n";
                }
                camera1Combo.SelectedIndex = 0;
            }
            catch
            {
                startButton.Enabled = false;

                camera1Combo.Items.Add("No cameras found");

                camera1Combo.SelectedIndex = 0;

                camera1Combo.Enabled = false;
            }
        }

        // On form closing
        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            StopCameras();
        }

        // On "Start" button click
        private void startButton_Click(object sender, EventArgs e)
        {
            StartCameras();

            startButton.Enabled = false;
            stopButton.Enabled = true;
        }

        // On "Stop" button click
        private void stopButton_Click(object sender, EventArgs e)
        {
            StopCameras();

            startButton.Enabled = true;
            stopButton.Enabled = false;

        }

        // Start cameras
        private void StartCameras()
        {
            // create first video source
            VideoCaptureDevice videoSource1 = new VideoCaptureDevice(videoDevices[camera1Combo.SelectedIndex].MonikerString);

            videoSource1.DesiredFrameRate = 10;
            videoSourcePlayer1.VideoSource = videoSource1;
            videoSourcePlayer1.Start();
        }

        // Stop cameras
        private void StopCameras()
        {
            videoSourcePlayer1.SignalToStop();

            videoSourcePlayer1.WaitForStop();
        }
    }
}

