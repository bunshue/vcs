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

namespace vcs_WebCam_AForge1
{
    public partial class MainForm : Form
    {
        CameraMonitor[] CamMonitor = new CameraMonitor[4];  //物件陣列

        private FilterInfoCollection USBWebcams = null;
        int webcam_count = 0;
        private const int BORDER = 30;

        public MainForm()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //檢查錄影存檔的資料夾
            string Path = @"C:\dddddddddd";
            if (Directory.Exists(Path) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(Path);
                richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";
            }

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
                this.CamMonitor[i] = new CameraMonitor(pictureBox1, camera_name, "第 " + (i + 1).ToString() + " 台攝影機");

                /*
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";
                richTextBox1.Text += "長名 : " + USBWebcams[i].MonikerString + "\n";
                */
            }
        }

        void show_item_location()
        {
            int W = 640;
            int H = 480;
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = W + 50;
            int dy = H + 50;

            pictureBox1.Size = new Size(W, H);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            W = 120;
            H = 30;
            button1.Size = new Size(W, H);

            //W = 640;
            H = 480;
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H + BORDER);
            button2.Location = new Point(1000, BORDER);

            richTextBox1.Size = new Size(200, 600);
            richTextBox1.Location = new Point(1000, 70);
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

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";
            int i;
            i = 0;

            richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
            richTextBox1.Text += "IsRecording\t" + this.CamMonitor[i].IsRecording.ToString() + "\n";
            richTextBox1.Text += "cameraName\t" + this.CamMonitor[i].cameraName.ToString() + "\n";
            richTextBox1.Text += "CamMonitor\t" + this.CamMonitor[i].ToString() + "\n";
            richTextBox1.Text += "BeepOnMotion\t" + this.CamMonitor[i].BeepOnMotion.ToString() + "\n";
        }
    }
}

