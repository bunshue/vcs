using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

// Libraries needed to work with VideoInputDevices
using AForge.Video;
using AForge.Video.DirectShow;



namespace WebcamSecurity
{
    public partial class MainForm : Form
    {
        // Refrence to cameraMonitors of all 4 cams
        CameraMonitor[] CamMonitor = new CameraMonitor[4];
        // Indexed arrays containing referces to the user interface components
        // so they can be easily accessed later on
        PictureBox[] DisplayReference = new PictureBox[4];
        GroupBox[] camOptions = new GroupBox[4];
        // The Configuration data set where we will store all user options (recording path , etc..)
        Config config;


        public MainForm()
        {
            InitializeComponent();
            // linking the user interface componets to the arrays
            this.DisplayReference[0] = this.Display_Cam1;
            this.DisplayReference[1] = this.Display_Cam2;
            this.DisplayReference[2] = this.Display_Cam3;
            this.DisplayReference[3] = this.Display_Cam4;

            this.camOptions[0] = this.groupBox5;
            this.camOptions[1] = this.groupBox6;
            this.camOptions[2] = this.groupBox7;
            this.camOptions[3] = this.groupBox8;

            this.camOptions[0].Enabled = false;
            this.camOptions[1].Enabled = false;
            this.camOptions[2].Enabled = false;
            this.camOptions[3].Enabled = false;
        }
        // The following method is responsible of saving data (upon exit) to the Config DataSet
        private void SaveOptions()
        {
            try
            {
                // we try to get the option record by key
                DataRow r = this.config.Options.Select("Key = 'Camera1'")[0];
                // then we retrieve the value from the user control
                r[1] = ((!this.MotionDetection1.Checked) ? "0" : "1") +
                    ((!this.AutoRecord1.Checked) ? "0" : "1") +
                    ((!this.BeepOnMotionCheck1.Checked) ? "0" : "1");
            }
            catch (Exception ex) // if somthing goes wrong (ie. Option key is not found)
            {
                // we create a new Option record
                this.config.Options.AddOptionsRow("Camera1",
                    ((!this.MotionDetection1.Checked) ? "0" : "1") +
                    ((!this.AutoRecord1.Checked) ? "0" : "1") +
                    ((!this.BeepOnMotionCheck1.Checked) ? "0" : "1"));
            }
            try
            {
                DataRow r = this.config.Options.Select("Key = 'Camera2'")[0];
                r[1] = ((!this.MotionDetection2.Checked) ? "0" : "1") +
                    ((!this.AutoRecord2.Checked) ? "0" : "1") +
                    ((!this.BeepOnMotionCheck2.Checked) ? "0" : "1");
            }
            catch (Exception ex)
            {
                this.config.Options.AddOptionsRow("Camera2",
                    ((!this.MotionDetection2.Checked) ? "0" : "1") +
                    ((!this.AutoRecord2.Checked) ? "0" : "1") +
                    ((!this.BeepOnMotionCheck2.Checked) ? "0" : "1"));
            }
            try
            {
                DataRow r = this.config.Options.Select("Key = 'Camera3'")[0];
                r[1] = ((!this.MotionDetection3.Checked) ? "0" : "1") +
                    ((!this.AutoRecord3.Checked) ? "0" : "1") +
                    ((!this.BeepOnMotionCheck3.Checked) ? "0" : "1");
            }
            catch (Exception ex)
            {
                this.config.Options.AddOptionsRow("Camera3",
                    ((!this.MotionDetection3.Checked) ? "0" : "1") +
                    ((!this.AutoRecord3.Checked) ? "0" : "1") +
                    ((!this.BeepOnMotionCheck3.Checked) ? "0" : "1"));
            }
            try
            {
                DataRow r = this.config.Options.Select("Key = 'Camera4'")[0];
                r[1] = ((!this.MotionDetection4.Checked) ? "0" : "1") +
                    ((!this.AutoRecord4.Checked) ? "0" : "1") +
                    ((!this.BeepOnMotionCheck4.Checked) ? "0" : "1");
            }
            catch (Exception ex)
            {
                this.config.Options.AddOptionsRow("Camera4",
                    ((!this.MotionDetection4.Checked) ? "0" : "1") +
                    ((!this.AutoRecord4.Checked) ? "0" : "1") +
                    ((!this.BeepOnMotionCheck4.Checked) ? "0" : "1"));
            }
            try
            {
                DataRow r = this.config.Options.Select("Key = 'RECORDINGPATH'")[0];
                r[1] = this.RecordingPathInput.Text;
            }
            catch (Exception ex)
            {
                this.config.Options.AddOptionsRow("RECORDINGPATH", this.RecordingPathInput.Text);
            }
            // finally we write everyting to an xml file
            this.config.WriteXml("..//..//config.xml");
        }
        // The following method is responsible of loading data (upon application load) 
        // from the Config Dataset to the user interface
        private void LoadOptions()
        {
            try
            {
                // we try to get the option by its Key
                DataRow r = this.config.Options.Select("Key = 'Camera1'")[0];
                string option = r[1].ToString();
                // we apply changes to the user interface
                this.MotionDetection1.Checked = (option[0] == '0') ? false : true;
                this.AutoRecord1.Checked = (option[1] == '0') ? false : true;
                this.BeepOnMotionCheck1.Checked = (option[2] == '0') ? false : true;
            }
            catch (Exception ex)
            {
            }

            try
            {
                DataRow r = this.config.Options.Select("Key = 'Camera2'")[0];
                string option = r[1].ToString();
                this.MotionDetection2.Checked = (option[0] == '0') ? false : true;
                this.AutoRecord2.Checked = (option[1] == '0') ? false : true;
                this.BeepOnMotionCheck2.Checked = (option[2] == '0') ? false : true;
            }
            catch (Exception ex)
            {
            }

            try
            {
                DataRow r = this.config.Options.Select("Key = 'Camera3'")[0];
                string option = r[1].ToString();
                this.MotionDetection3.Checked = (option[0] == '0') ? false : true;
                this.AutoRecord3.Checked = (option[1] == '0') ? false : true;
                this.BeepOnMotionCheck3.Checked = (option[2] == '0') ? false : true;
            }
            catch (Exception ex)
            {
            }

            try
            {
                DataRow r = this.config.Options.Select("Key = 'Camera4'")[0];
                string option = r[1].ToString();
                this.MotionDetection4.Checked = (option[0] == '0') ? false : true;
                this.AutoRecord4.Checked = (option[1] == '0') ? false : true;
                this.BeepOnMotionCheck4.Checked = (option[2] == '0') ? false : true;
            }
            catch (Exception ex)
            {
            }
        }

        // the FilterInfoCollection is where we get information about VideoCaptureDevices
        private FilterInfoCollection webcam;

        // When the form loads
        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            // an instance of FilterInfoCollection is created to fetch available VideoCaptureDevices
            webcam = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            // we create our CameraMonitors
            for (int i = 0; i < webcam.Count && i < 4; i++)
            {
                this.CamMonitor[i] = new CameraMonitor(this.DisplayReference[i], webcam[i].MonikerString, "Camera" + (i + 1));
                // Enable the user controls coressponding to the CameraMonitor
                this.camOptions[i].Enabled = true;
            }

            // we try to load Options from the xml file saved previously
            this.config = new Config();

            try
            {
                config.ReadXml("..//..//config.xml");
                // we fetch the recording path from the DataSet
                DataRow result = config.Options.Select("Key = 'RECORDINGPATH'")[0];
                this.RecordingPathInput.Text = result[1].ToString();
            }
            catch (Exception ex)
            {
                // if the recording path is not set previously by the user
                // this code below will prompt the user to set it
                FolderBrowserDialog folder = new FolderBrowserDialog();
                while (folder.SelectedPath == "")
                {
                    folder.ShowDialog();
                }
                if (folder.SelectedPath != "")
                {
                    this.RecordingPathInput.Text = folder.SelectedPath;
                }
            }

            // load the options the the user interface
            LoadOptions();

            // set the recording path to the exising CameraMonitors
            for (int i = 0; i < 4; i++)
            {
                try
                {
                    this.CamMonitor[i].RecordingPath = this.RecordingPathInput.Text;
                }
                catch (NullReferenceException ex)
                {
                }
            }
        }

        void show_item_location()
        {
            int W = 640 * 9 / 10;
            int H = 480 * 9 / 10;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 50;
            int dy = H + 50;

            Display_Cam1.Size = new Size(W, H);
            Display_Cam2.Size = new Size(W, H);
            Display_Cam3.Size = new Size(W, H);
            Display_Cam4.Size = new Size(W, H);

            Display_Cam1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            Display_Cam2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            Display_Cam3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            Display_Cam4.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            W = 120;
            H = 30;
            RecordButton1.Size = new Size(W, H);
            RecordButton2.Size = new Size(W, H);
            RecordButton3.Size = new Size(W, H);
            RecordButton4.Size = new Size(W, H);

            //W = 640 * 9 / 10;
            H = 480 * 9 / 10;
            RecordButton1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H + 10);
            RecordButton2.Location = new Point(x_st + dx * 1, y_st + dy * 0 + H + 10);
            RecordButton3.Location = new Point(x_st + dx * 0, y_st + dy * 1 + H + 10);
            RecordButton4.Location = new Point(x_st + dx * 1, y_st + dy * 1 + H + 10);


            panel1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Size = new Size(panel1.Size.Width + 100, panel1.Size.Height);
            richTextBox1.Location = new Point(x_st + dx * 2 + panel1.Size.Width + 50, y_st + dy * 0);
        }

        // this method will stop recording and running cameras 
        // also save the options to an xml file
        private void StopCameras(object sender, FormClosingEventArgs e)
        {
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
            // save options to an  xml file
            this.SaveOptions();
        }

        // Method for changing the record path
        private void ChangeRecordingPath(object sender, EventArgs e)
        {
            // prompt the user with a FolderBrowserDialog
            FolderBrowserDialog folderBrowserDialog1 = new FolderBrowserDialog();
            folderBrowserDialog1.SelectedPath = @"C:\______test_files";
            folderBrowserDialog1.ShowDialog();

            if (folderBrowserDialog1.SelectedPath != "")
            {
                this.RecordingPathInput.Text = folderBrowserDialog1.SelectedPath;
                // Load the selected path to the Config DataSet
                try
                {
                    DataRow r = this.config.Options.Select("Key = 'RECORDINGPATH'")[0];
                    r[1] = this.RecordingPathInput.Text;
                }
                catch (Exception ex)
                {
                    this.config.Options.AddOptionsRow("RECORDINGPATH", this.RecordingPathInput.Text);
                }
                // update the recording path to the exising CameraMonitors
                for (int i = 0; i < 4; i++)
                {
                    try
                    {
                        this.CamMonitor[i].RecordingPath = this.RecordingPathInput.Text;
                    }
                    catch (NullReferenceException ex)
                    {
                    }
                }
            }
        }

        // The Rest is User Interface EventHandling
        private void RecordButton1_Click(object sender, EventArgs e)
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

        private void RecordButton2_Click(object sender, EventArgs e)
        {
            if (this.CamMonitor[1].IsRecording)
            {
                this.CamMonitor[1].StopRecording();
                this.CamMonitor[1].forceRecord = false;
                ((Button)sender).Text = "Record";
            }
            else
            {
                this.CamMonitor[1].StartRecording();
                this.CamMonitor[1].forceRecord = true;
                ((Button)sender).Text = "Stop";
            }
        }
        private void RecordButton3_Click(object sender, EventArgs e)
        {
            if (this.CamMonitor[2].IsRecording)
            {
                this.CamMonitor[2].StopRecording();
                this.CamMonitor[2].forceRecord = false;
                ((Button)sender).Text = "Record";
            }
            else
            {
                this.CamMonitor[2].StartRecording();
                this.CamMonitor[2].forceRecord = true;
                ((Button)sender).Text = "Stop";
            }
        }
        private void RecordButton4_Click(object sender, EventArgs e)
        {
            if (this.CamMonitor[3].IsRecording)
            {
                this.CamMonitor[3].StopRecording();
                this.CamMonitor[3].forceRecord = false;
                ((Button)sender).Text = "Record";
            }
            else
            {
                this.CamMonitor[3].StartRecording();
                this.CamMonitor[3].forceRecord = true;
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

        private void MotionDetection2_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(1, 0, true);
            }
            else
            {
                this.toggleOption(1, 0, false);
            }
        }

        private void MotionDetection3_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(2, 0, true);
            }
            else
            {
                this.toggleOption(2, 0, false);
            }
        }

        private void MotionDetection4_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(3, 0, true);
            }
            else
            {
                this.toggleOption(3, 0, false);
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

        private void AutoRecord2_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(1, 1, true);
            }
            else
            {
                this.toggleOption(1, 1, false);
            }
        }

        private void AutoRecord3_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(2, 1, true);
            }
            else
            {
                this.toggleOption(2, 1, false);
            }
        }

        private void AutoRecord4_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(3, 1, true);
            }
            else
            {
                this.toggleOption(3, 1, false);
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

        private void BeepOnMotionCheck2_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(1, 2, true);
            }
            else
            {
                this.toggleOption(1, 2, false);
            }
        }

        private void BeepOnMotionCheck3_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(2, 2, true);
            }
            else
            {
                this.toggleOption(2, 2, false);
            }
        }

        private void BeepOnMotionCheck4_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(3, 2, true);
            }
            else
            {
                this.toggleOption(3, 2, false);
            }
        }
    }
}

