using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace AutomaticPlayImplement
{
    public partial class Form1 : Form
    {
        string foldername = @"D:\vcs\astro\_DATA2\_mp3\陳盈潔_台語精選集6CD\disc1\";

        static int i = 0;
        private WMPLib.WindowsMediaPlayerClass WC;
        private WMPLib.IWMPMedia MC = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        public void GetAllFiles(DirectoryInfo dir)
        {
            this.listBox1.Items.Clear();
            FileSystemInfo[] fileinfo = dir.GetFileSystemInfos();
            foreach (FileSystemInfo i in fileinfo)
            {
                if (i is DirectoryInfo)
                {
                    GetAllFiles((DirectoryInfo)i);
                }
                else
                {
                    string str = i.FullName;
                    int b = str.LastIndexOf("\\");
                    string strbbb = str.Substring(b + 1);
                    if (strbbb.Substring(strbbb.Length - 3) == "mp3")
                    {
                        this.listBox1.Items.Add(str.Substring(b + 1));
                        //添加列表
                        WC = new WMPLib.WindowsMediaPlayerClass();
                        MC = WC.newMedia(str);
                        this.axWindowsMediaPlayer1.currentPlaylist.appendItem(MC);
                    }
                }
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            this.listBox1.Items.Clear();
            DirectoryInfo dir = new DirectoryInfo(foldername);
            GetAllFiles(dir);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //播放
            if (MC != null)
                this.axWindowsMediaPlayer1.Ctlcontrols.play();
            else
                MessageBox.Show("请添加文件列表");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //停止播放
            this.axWindowsMediaPlayer1.Ctlcontrols.stop();
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            /*
            //停止播放
            this.axWindowsMediaPlayer1.Ctlcontrols.stop();
            richTextBox1.Text += "select : " + listBox1.SelectedItem + "\n";

            this.axWindowsMediaPlayer1.URL = foldername + listBox1.SelectedItem;
            richTextBox1.Text += "url : " + this.axWindowsMediaPlayer1.URL + "\n";
            this.axWindowsMediaPlayer1.Ctlcontrols.play();
            */
        }

        private void listBox1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            //停止播放
            this.axWindowsMediaPlayer1.Ctlcontrols.stop();
            richTextBox1.Text += "select : " + listBox1.SelectedItem + "\n";

            this.axWindowsMediaPlayer1.URL = foldername + listBox1.SelectedItem;
            richTextBox1.Text += "url : " + this.axWindowsMediaPlayer1.URL + "\n";
            this.axWindowsMediaPlayer1.Ctlcontrols.play();

        }
    }
}
