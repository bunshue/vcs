using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyPlayer3
{
    public partial class MediaInfo : Form
    {
        string data_from_form1 = string.Empty;

        AxWMPLib.AxWindowsMediaPlayer axWindowsMediaPlayer1;

        void Init_WMP()
        {
            this.axWindowsMediaPlayer1 = new AxWMPLib.AxWindowsMediaPlayer();
            this.axWindowsMediaPlayer1.Enabled = true;
            //this.axWindowsMediaPlayer1.Location = new System.Drawing.Point(0, 400);
            //this.axWindowsMediaPlayer1.Name = "axWindowsMediaPlayer1";
            //this.axWindowsMediaPlayer1.Size = new System.Drawing.Size(800, 500);
            //this.axWindowsMediaPlayer1.TabIndex = 2;
            //this.axWindowsMediaPlayer1.Visible = false;   //fail
            //this.axWindowsMediaPlayer1.StatusChange += new EventHandler(axWindowsMediaPlayer1_StatusChange);
            this.Controls.Add(this.axWindowsMediaPlayer1);
        }

        public MediaInfo(string data1)
        {
            InitializeComponent();
            data_from_form1 = data1;
            richTextBox1.Text += data1;
        }

        private void MediaInfo_Load(object sender, EventArgs e)
        {
            Init_WMP();
            richTextBox1.Text += "AAAAAAAAAAAAAAAAAAA";

            string mp3_filename = @"D:\_git\vcs\_1.data\______test_files1\_mp3\16.監獄風雲.mp3";
            axWindowsMediaPlayer1.Visible = false;
            axWindowsMediaPlayer1.URL = mp3_filename;




        }
    }
}

