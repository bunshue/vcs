using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using WMPLib;   //for WindowsMediaPlayerClass

namespace vcs_axWindowsMediaPlayer3_playlist2
{
    public partial class Form1 : Form
    {
        //string foldername = @"D:\vcs\astro\_DATA2\_mp3\陳盈潔_台語精選集6CD\disc1\";
        string foldername = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\陳一郎_紅燈碼頭\";

        private WMPLib.WindowsMediaPlayerClass wmpc;
        private WMPLib.IWMPMedia iwmpm = null;

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

        private void br_clear_listbox_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        public void GetAllFiles(DirectoryInfo dir)
        {
            FileSystemInfo[] fileinfo = dir.GetFileSystemInfos();
            foreach (FileSystemInfo fsInfo in fileinfo)
            {
                if (fsInfo is DirectoryInfo)
                {
                    GetAllFiles((DirectoryInfo)fsInfo);
                }
                else
                {
                    string str = fsInfo.FullName;
                    richTextBox1.Text += "str = " + str + "\n";
                    int b = str.LastIndexOf("\\");
                    string strbbb = str.Substring(b + 1);
                    if (strbbb.Substring(strbbb.Length - 3).ToLower() == "mp3") //只要抓mp3就好
                    {
                        this.listBox1.Items.Add(str.Substring(b + 1));
                        //添加列表
                        wmpc = new WMPLib.WindowsMediaPlayerClass();
                        iwmpm = wmpc.newMedia(str);
                        this.axWindowsMediaPlayer1.currentPlaylist.appendItem(iwmpm);
                        richTextBox1.Text += "add " + str + "\n";
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
            if (button2.Text == "播放")
            {
                if (iwmpm != null)
                {
                    richTextBox1.Text += "播放\n";
                    this.Text = axWindowsMediaPlayer1.Ctlcontrols.currentItem.name;
                    this.axWindowsMediaPlayer1.Ctlcontrols.play();
                    button2.Text = "停止";
                }
                else
                {
                    richTextBox1.Text += "請添加播放清單\n";
                }
            }
            else
            {
                richTextBox1.Text += "停止播放\n";
                this.axWindowsMediaPlayer1.Ctlcontrols.stop();
                button2.Text = "播放";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.Ctlcontrols.next();

            //richTextBox1.Text += this.axWindowsMediaPlayer1.URL + "\n";

            richTextBox1.Text += "下一首\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.name + "\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.sourceURL + "\n";
            this.Text = axWindowsMediaPlayer1.Ctlcontrols.currentItem.name;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.Ctlcontrols.previous();

            //richTextBox1.Text += this.axWindowsMediaPlayer1.URL + "\n";

            richTextBox1.Text += "上一首\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.name + "\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.sourceURL + "\n";
            this.Text = axWindowsMediaPlayer1.Ctlcontrols.currentItem.name;
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            //此時播放清單會被清空
            richTextBox1.Text += "選中第 " + listBox1.SelectedIndex.ToString() + " 首\n";
            /*
            //停止播放
            this.axWindowsMediaPlayer1.Ctlcontrols.stop();
            richTextBox1.Text += "select : " + listBox1.SelectedItem + "\n";

            this.axWindowsMediaPlayer1.URL = foldername + listBox1.SelectedItem;
            richTextBox1.Text += "url : " + this.axWindowsMediaPlayer1.URL + "\n";
            this.axWindowsMediaPlayer1.Ctlcontrols.play();
            */

            //richTextBox1.Text += "目前播放到第 " + this.axWindowsMediaPlayer1.currentPlaylist.Item[
        }

        private void listBox1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            /*  同上
            richTextBox1.Text += "選中第 " + listBox1.SelectedIndex.ToString() + " 首\n";
            //停止播放
            this.axWindowsMediaPlayer1.Ctlcontrols.stop();
            richTextBox1.Text += "select : " + listBox1.SelectedItem + "\n";

            this.axWindowsMediaPlayer1.URL = foldername + listBox1.SelectedItem;
            richTextBox1.Text += "url : " + this.axWindowsMediaPlayer1.URL + "\n";
            this.axWindowsMediaPlayer1.Ctlcontrols.play();
            */
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "info\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.name + "\t";
            richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.sourceURL + "\n";

            //目前再WMP內總共有幾首歌
            //每首歌印出來
            richTextBox1.Text += "count = " + this.axWindowsMediaPlayer1.Controls.Count.ToString() + "\n";

            int count = axWindowsMediaPlayer1.currentPlaylist.count;
            richTextBox1.Text += "播放清單內共有 : " + count.ToString() + " 首歌\n";
            int i;
            for (i = 0; i < count; i++)
            {
                richTextBox1.Text += i.ToString() + "\t";
                richTextBox1.Text += this.axWindowsMediaPlayer1.currentPlaylist.Item[i].name + "\t";
                richTextBox1.Text += this.axWindowsMediaPlayer1.currentPlaylist.Item[i].sourceURL + "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string mp3_filename = @"D:\_git\vcs\_1.data\______test_files1\_mp3\09    都はるみ--裏町人生(後街人生).mp3";

            richTextBox1.Text += "測試使用WindowsMediaPlayerClass\n";
            WindowsMediaPlayerClass wmpc;
            IWMPMedia iwmpm;

            wmpc = new WindowsMediaPlayerClass();
            iwmpm = wmpc.newMedia(mp3_filename);
            richTextBox1.Text += "歌手名:\t" + iwmpm.getItemInfo("Author") + "\n" + "歌  名:\t" + iwmpm.getItemInfo("Title") + "\n";

            /*
            int len = iwmpm.attributeCount;
            richTextBox1.Text += "屬性個數 : " + len.ToString() + " 個\n";

            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += iwmpm.getAttributeName(i) + " : " + iwmpm.getItemInfo(iwmpm.getAttributeName(i)) + "\n";

            }
            richTextBox1.Text += "\n";
            */

            /*
            richTextBox1.Text += "\n";
            richTextBox1.Text += "讀目前正在播放的檔案的屬性資料\n";
            var cm = axWindowsMediaPlayer1.currentMedia;
            int len = cm.attributeCount;
            richTextBox1.Text += "屬性個數 : " + len.ToString() + " 個\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += cm.getAttributeName(i) + " : " + cm.getItemInfo(cm.getAttributeName(i)) + "\n";

            }
            richTextBox1.Text += "\n";
            */

            /*
            richTextBox1.Text += "playlist name : " + axWindowsMediaPlayer1.currentPlaylist.name.ToString() + "\n";
            richTextBox1.Text += "playlist count : " + axWindowsMediaPlayer1.currentPlaylist.count.ToString() + "\n";

            //若正在播放才可以
            richTextBox1.Text += "目前播放 : " + axWindowsMediaPlayer1.Ctlcontrols.currentItem.name + "\n";
            richTextBox1.Text += "目前播放 : " + axWindowsMediaPlayer1.Ctlcontrols.currentItem.sourceURL + "\n";
            */
            //richTextBox1.Text += "attributeCount : " + axWindowsMediaPlayer1.currentPlaylist.attributeCount.ToString() + "\n";  //0

            axWindowsMediaPlayer1.settings.autoStart = true;     //自動播放
            axWindowsMediaPlayer1.Ctlcontrols.play();


            richTextBox1.Text += "name = " + axWindowsMediaPlayer1.Name + "\n";
            richTextBox1.Text += "url =" + axWindowsMediaPlayer1.URL + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "清除播放清單, 同時也會停止播放\n";
            axWindowsMediaPlayer1.currentPlaylist.clear();
        }
    }
}

