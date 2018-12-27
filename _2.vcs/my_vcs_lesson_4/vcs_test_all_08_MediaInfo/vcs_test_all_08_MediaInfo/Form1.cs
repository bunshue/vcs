using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using MediaInfoNET;

namespace vcs_test_all_08_MediaInfo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //MediaFile mp4File = new MediaFile(@"C:\____手機來的圖\__影片\Lock_Mode.mp4");
            MediaFile mp4File = new MediaFile(@"C:\______test_vcs\aaaa.mp3");
            richTextBox1.Text += "File Name : " + mp4File.Name + "\n";
            richTextBox1.Text += "FileSize : "   + mp4File.FileSize.ToString() + " Bytes\n";
            richTextBox1.Text += "FrameCount : " + mp4File.FrameCount.ToString() + "\n";
            richTextBox1.Text += "StreamCount : " + mp4File.StreamCount.ToString() + "\n";

            richTextBox1.Text += "File : " + mp4File.File + "\n";
            richTextBox1.Text += "ParentFolder : " + mp4File.ParentFolder + "\n";
            richTextBox1.Text += "Extension : " + mp4File.Extension + "\n";
            richTextBox1.Text += "Description : \n" + mp4File.Description + "\n\n";
            richTextBox1.Text += "Title : " + mp4File.Title + "\n";
            richTextBox1.Text += "Capacity : " + mp4File.Text.Capacity.ToString() +"\n";
            
            richTextBox1.Text += "\n";

            //General
            richTextBox1.Text += "Format : " + mp4File.General.Format + "\n";
            richTextBox1.Text += "Duration : " + mp4File.General.DurationString + "\n";
            richTextBox1.Text += "Bitrate : " + mp4File.General.Bitrate.ToString() + "\n";

            richTextBox1.Text += "CodecID : " + mp4File.General.CodecID + "\n";
            richTextBox1.Text += "Description : " + mp4File.General.Description + "\n";
            richTextBox1.Text += "DurationMillis : " + mp4File.General.DurationMillis.ToString() + "\n";
            richTextBox1.Text += "DurationString : " + mp4File.General.DurationString + "\n";
            richTextBox1.Text += "DurationStringAccurate : " + mp4File.General.DurationStringAccurate + "\n";
            richTextBox1.Text += "Extension : " + mp4File.General.Extension + "\n";
            richTextBox1.Text += "Format : " + mp4File.General.Format + "\n";
            richTextBox1.Text += "FormatID : " + mp4File.General.FormatID + "\n";


            richTextBox1.Text += "ID : " + mp4File.General.ID.ToString() + "\n";
            richTextBox1.Text += "StreamSize : " + mp4File.General.StreamSize.ToString() + "\n";
            richTextBox1.Text += "StreamType : " + mp4File.General.StreamType + "\n";


            //Info
            if (mp4File.MediaInfo_Available == true)
            {
                richTextBox1.Text += "MediaInfo_Available = true, info:\n";
                richTextBox1.Text += mp4File.MediaInfo_Text + "\n\n";
            }
            else
            {
                richTextBox1.Text += "MediaInfo_Available = false\n";
            
            }

            if (mp4File.InfoAvailable == true)
            {
                richTextBox1.Text += "InfoAvailable = true, info\n";
                richTextBox1.Text += "Info:\n" + mp4File.Info_Text + "\n\n";
            }
            else
            {
                richTextBox1.Text += "InfoAvailable = false\n";
            }

            richTextBox1.Text += "Audio Count: " + mp4File.Audio.Count.ToString() + "\n";
            richTextBox1.Text += "Video Count: " + mp4File.Video.Count.ToString() + "\n";

            if (mp4File.Audio.Count > 0)
            {
                richTextBox1.Text += "\n";
                richTextBox1.Text += "Audio ---------------------------------" + "\n";
                richTextBox1.Text += "\n";
                richTextBox1.Text += "Format : " + mp4File.Audio[0].Format + "\n";
                richTextBox1.Text += "Bitrate : " + mp4File.Audio[0].Bitrate.ToString() + "\n";
                richTextBox1.Text += "Channels : " + mp4File.Audio[0].Channels.ToString() + "\n";
                richTextBox1.Text += "Sampling : " + mp4File.Audio[0].SamplingRate.ToString() + "\n";
            }

            if (mp4File.Video.Count > 0)
            {
                richTextBox1.Text += "\n";
                richTextBox1.Text += "Video ---------------------------------" + "\n";
                richTextBox1.Text += "\n";
                richTextBox1.Text += "Format : " + mp4File.Video[0].Format + "\n";
                richTextBox1.Text += "Bit rate : " + mp4File.Video[0].Bitrate.ToString() + "\n";
                richTextBox1.Text += "Frame rate : " + mp4File.Video[0].FrameRate.ToString() + "\n";
                richTextBox1.Text += "Frame size : " + mp4File.Video[0].FrameSize.ToString() + "\n";
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
