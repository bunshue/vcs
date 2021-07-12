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
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        public void GetAllFiles(DirectoryInfo dir)
        {
            //richTextBox1.Text += "clear 1\n";
            //this.listBox1.Items.Clear();
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
                        richTextBox1.Text += "add " + str + "\n";
                        this.axWindowsMediaPlayer1.currentPlaylist.appendItem(MC);
                    }
                }
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "clear 2\n";
            this.listBox1.Items.Clear();
            DirectoryInfo dir = new DirectoryInfo(foldername);
            GetAllFiles(dir);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "播放\n";
            if (MC != null)
                this.axWindowsMediaPlayer1.Ctlcontrols.play();
            else
                MessageBox.Show("请添加文件列表");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "停止播放\n";
            this.axWindowsMediaPlayer1.Ctlcontrols.stop();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.Ctlcontrols.next();

            //richTextBox1.Text += this.axWindowsMediaPlayer1.URL + "\n";

            richTextBox1.Text += "下一首\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.name + "\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.sourceURL + "\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.Ctlcontrols.previous();

            //richTextBox1.Text += this.axWindowsMediaPlayer1.URL + "\n";

            richTextBox1.Text += "上一首\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.name + "\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.sourceURL + "\n";
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "選中第 " + listBox1.SelectedIndex.ToString() + " 首\n";
            //停止播放
            this.axWindowsMediaPlayer1.Ctlcontrols.stop();
            richTextBox1.Text += "select : " + listBox1.SelectedItem + "\n";

            this.axWindowsMediaPlayer1.URL = foldername + listBox1.SelectedItem;
            richTextBox1.Text += "url : " + this.axWindowsMediaPlayer1.URL + "\n";
            this.axWindowsMediaPlayer1.Ctlcontrols.play();
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

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "info\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.name + "\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.sourceURL + "\n";

            //目前再WMP內總共有幾首歌
            //每首歌印出來
            richTextBox1.Text += "count = " + this.axWindowsMediaPlayer1.Controls.Count.ToString() + "\n";

            int count = this.axWindowsMediaPlayer1.currentPlaylist.count;
            richTextBox1.Text += "播放清單內共有 : " + count.ToString() + " 首歌\n";
            int i;
            for (i = 0; i < count; i++)
            {
                richTextBox1.Text += i.ToString() + "\t";
                richTextBox1.Text += this.axWindowsMediaPlayer1.currentPlaylist.Item[i].name + "\t";
                richTextBox1.Text += this.axWindowsMediaPlayer1.currentPlaylist.Item[i].sourceURL + "\n";
            }
        }
    }
}
