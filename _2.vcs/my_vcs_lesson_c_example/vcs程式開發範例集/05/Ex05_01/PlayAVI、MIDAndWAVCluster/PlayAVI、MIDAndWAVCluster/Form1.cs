using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace PlayAVIMIDAndWAVCluster
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\__RW\_avi\enka.avi";

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Load
            this.axWindowsMediaPlayer1.newMedia(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //Play
            this.axWindowsMediaPlayer1.URL = filename;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Stop
            this.axWindowsMediaPlayer1.close();


            //or
            //this.axWindowsMediaPlayer1.Ctlcontrols.stop();
        }

        private void bt_pause_Click(object sender, EventArgs e)
        {
            if (bt_pause.Text == "暫停")
            {
                this.axWindowsMediaPlayer1.Ctlcontrols.pause();

                bt_pause.Text = "繼續";

            }
            else
            {
                this.axWindowsMediaPlayer1.Ctlcontrols.play();

                bt_pause.Text = "暫停";
            }
        }

        private WMPLib.WindowsMediaPlayerClass c;
        private WMPLib.IWMPMedia m;

        private void bt_info_Click(object sender, EventArgs e)
        {
            c = new WMPLib.WindowsMediaPlayerClass();
            m = c.newMedia(filename);
            richTextBox1.Text += "歌手名:\t" + m.getItemInfo("Author") + "\n" + "歌  名:\t" + m.getItemInfo("Title") + "\n";


        }
    }
}
