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
        static int i = 0;
        private WMPLib.WindowsMediaPlayerClass WC;
        private WMPLib.IWMPMedia MC=null;
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
            if (this.folderBrowserDialog1.ShowDialog()==DialogResult.OK)
            {
                DirectoryInfo dir = new DirectoryInfo(folderBrowserDialog1.SelectedPath);
                GetAllFiles(dir);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {

            if (MC != null)
                this.axWindowsMediaPlayer1.Ctlcontrols.play();
            else
                MessageBox.Show("请添加文件列表");
        }
    }
}