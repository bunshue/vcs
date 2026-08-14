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

namespace vcs_WebCam5_Article
{
    public partial class MainForm : Form
    {
        WebCam CamMonitor;

        private FilterInfoCollection USBWebcams = null;
        int webcam_count = 0;

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
            richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";

            int i;
            /*

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
                CamMonitor = new WebCam(pictureBox1, camera_name, "第1台攝影機");

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
            button2.Location = new Point(1000, 10);

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
                    CamMonitor.StopRecording();
                    CamMonitor.StopCapture();
                }
                catch (Exception ex)
                {
                }
            }
        }

        // The Rest is User Interface EventHandling
        private void button1_Click(object sender, EventArgs e)
        {
            if (CamMonitor.IsRecording)
            {
                CamMonitor.StopRecording();
                CamMonitor.forceRecord = false;
                ((Button)sender).Text = "Record";
            }
            else
            {
                CamMonitor.StartRecording();
                CamMonitor.forceRecord = true;
                ((Button)sender).Text = "Stop";
            }
        }

        private void toggleOption(int optionIndex, bool value)
        {
            switch (optionIndex)
            {
                case 0:
                    CamMonitor.MotionDetection = value;
                    break;
                case 1:
                    CamMonitor.RecordOnMotion = value;
                    break;
                case 2:
                    CamMonitor.BeepOnMotion = value;
                    break;
            }
        }

        private void MotionDetection1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(0, true);
            }
            else
            {
                this.toggleOption(0, false);
            }
        }

        private void AutoRecord1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(1, true);
            }
            else
            {
                this.toggleOption(1, false);
            }
        }

        private void BeepOnMotionCheck1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(2, true);
            }
            else
            {
                this.toggleOption(2, false);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

