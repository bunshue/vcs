using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
namespace SnatchDetailsInfoList
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void ButOpen_Click(object sender, EventArgs e)
        {
            this.optFile.ShowDialog();
        }
        private void ButPlay_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.URL = this.optFile.FileName;
        }
        private void ButStop_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.Ctlcontrols.stop();
        }
        private void ButPause_Click(object sender, EventArgs e)
        {
       
            if (this.ButPause.Text == "暂停(&A)")
            {
                this.axWindowsMediaPlayer1.Ctlcontrols.pause();
                this.ButPause.Text = "继续(&A)";
            }
            else
            {
                this.axWindowsMediaPlayer1.Ctlcontrols.play();
                this.ButPause.Text = "暂停(&A)";
            }
        }
        private void Form1_Load(object sender, EventArgs e)
        {
        }
        private WMPLib.WindowsMediaPlayerClass c;
        private WMPLib.IWMPMedia m;

        private void ButInfo_Click(object sender, EventArgs e)
        {
            if (this.optFile.FileName != "optFile")
            {
                c = new WMPLib.WindowsMediaPlayerClass();
                m = c.newMedia(this.optFile.FileName);
                MessageBox.Show("歌手名:" + m.getItemInfo("Author") + "\r\n" + "歌  名:" + m.getItemInfo("Title"));
            }
        }
    }
}