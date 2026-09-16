using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory
using WMPLib;       //for IWMPPlaylist IWMPMedia

namespace vcs_axWindowsMediaPlayer2_new
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Size = new Size(600, 690 - 90);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            axWindowsMediaPlayer1.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            this.Size = new Size(1060, 750);
            this.Text = "vcs_axWindowsMediaPlayer2_new";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            // 加入播放清單

            string mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\01.留戀什路用.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\02.昔日的戀歌.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\03.回鄉的我.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\04.行船人的純情曲.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\05.漂浪之女.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\06.紅燈青燈.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\07.為錢賭生命.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\08.看破愛別人.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\09.戀歌.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\10.悲戀的酒杯.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\11.一卡手指.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\12.人客的要求.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\13.悲情城市.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\14.人生.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\15.看破的愛.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\16.可愛的馬.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc2\01.漂浪之女.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc2\02.哀愁的火車站.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc2\03.男性純情曲.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));
            mp3_filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc2\04.船過水無痕.mp3";
            axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(mp3_filename));

            int len = axWindowsMediaPlayer1.currentPlaylist.count;
            richTextBox1.Text += "222目前播放清單內有 : " + len.ToString() + " 首歌\n";
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.settings.setMode("loop", true);   //循環播放
            axWindowsMediaPlayer1.Ctlcontrols.play();
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            if (axWindowsMediaPlayer1.currentPlaylist == null)
            {
                richTextBox1.Text += "無播放清單\n";
                return;
            }

            int len;
            len = axWindowsMediaPlayer1.currentPlaylist.count;
            richTextBox1.Text += "目前播放清單內有 : " + len.ToString() + " 首歌\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += axWindowsMediaPlayer1.currentPlaylist.Item[i].name + "\t";
                richTextBox1.Text += axWindowsMediaPlayer1.currentPlaylist.Item[i].sourceURL + "\n";
            }

            return;

            //清除播放清單內所有資料
            //axWindowsMediaPlayer1.currentPlaylist.clear();
            //richTextBox1.Text += "目前播放清單內有 : " + len.ToString() + " 首歌\n";

            richTextBox1.Text += "改變檔案位置\n";
            axWindowsMediaPlayer1.currentPlaylist.moveItem(3, 5);

            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += axWindowsMediaPlayer1.currentPlaylist.Item[i].name + "\t";
                richTextBox1.Text += axWindowsMediaPlayer1.currentPlaylist.Item[i].sourceURL + "\n";
            }

            //移除檔案
            //axWindowsMediaPlayer1.currentPlaylist.removeItem(fileinfos[4].filepath + "\\" + fileinfos[4].filename);

            //state if (axWindowsMediaPlayer1.playState == WMPPlayState.wmppsMediaEnded)
            richTextBox1.Text += "state = " + axWindowsMediaPlayer1.playState.ToString() + "\n";
        }

        //------------------------------------------------------------  # 60個

        IWMPPlaylist playlist;
        IWMPMedia media;

        private void button3_Click(object sender, EventArgs e)
        {
            //建立播放清單

            playlist = axWindowsMediaPlayer1.playlistCollection.newPlaylist("myplaylist");

            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\06.紅燈青燈.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\04.行船人的純情曲.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\07.為錢賭生命.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\08.看破愛別人.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\09.戀歌.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\10.悲戀的酒杯.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\11.一卡手指.mp3");
            playlist.appendItem(media);

            axWindowsMediaPlayer1.currentPlaylist = playlist;
            axWindowsMediaPlayer1.Ctlcontrols.play();
        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
            if (playlist == null)
                return;

            richTextBox1.Text += "移除播放清單\n";
            axWindowsMediaPlayer1.playlistCollection.remove(playlist);
            playlist = null;
        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
            if (playlist == null)
                return;
            int len = playlist.count;
            richTextBox1.Text += "目前播放清單內有 : " + len.ToString() + " 首歌\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += playlist.Item[i].sourceURL + "\n";
            }

            richTextBox1.Text += "改變檔案位置\n";
            playlist.moveItem(3, 5);
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
            if (playlist == null)
                return;

            /*      無法直接從播放清單內移除某項
            IWMPMedia to_remove;
            to_remove = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\07.為錢賭生命.mp3");

            playlist.removeItem(to_remove);
            */
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.stop();
        }

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {

            axWindowsMediaPlayer1.settings.setMode("shuffle", true);	//隨機播放
            axWindowsMediaPlayer1.settings.setMode("shuffle", false);	//順序播放
            axWindowsMediaPlayer1.settings.setMode("loop", true);	//循環播放
        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
            if (this.axWindowsMediaPlayer1.currentMedia == null)
            {
                richTextBox1.Text += "無播放檔案\n";
                return;
            }

            string durationString = this.axWindowsMediaPlayer1.currentMedia.durationString;
            richTextBox1.Text += "目前播放這首歌的長度是 : " + durationString + "\n";

            int len = Convert.ToInt32(this.axWindowsMediaPlayer1.currentMedia.duration);
            richTextBox1.Text += "目前播放這首歌的長度是 : " + len.ToString() + " 秒\n";

            int trackBarValue = Convert.ToInt32(this.axWindowsMediaPlayer1.Ctlcontrols.currentPosition);
            richTextBox1.Text += "目前播放位置是 : " + trackBarValue.ToString() + " 秒\n";

            richTextBox1.Text += "目前播放位置是 : " + this.axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {
            //直接播放單一檔案
            string filename = @"D:\vcs\astro\_DATA2\_mp3\陳盈潔_台語精選集6CD\disc3\01.南都夜曲.mp3";
            axWindowsMediaPlayer1.URL = filename;
            axWindowsMediaPlayer1.Ctlcontrols.play();
        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {
            //使用播放清單播放檔案
            string filename = @"D:\vcs\astro\_DATA2\_mp3\陳盈潔_台語精選集6CD\disc3\01.南都夜曲.mp3";
            IWMPMedia media;
            //新增到播放列表
            media = axWindowsMediaPlayer1.newMedia(filename);
            //axWindowsMediaPlayer1.currentPlaylist.insertItem(media);
            axWindowsMediaPlayer1.currentPlaylist.appendItem(media);
        }

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
            //無效
            axWindowsMediaPlayer1.windowlessVideo = false;   //設爲false後雙擊屏幕可以全屏
        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {
            //無效
            axWindowsMediaPlayer1.windowlessVideo = true;   //設爲false後雙擊屏幕可以全屏
        }

        //------------------------------------------------------------  # 60個

        private void button14_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.fullScreen = false; //設播放器全屏播放
        }

        //------------------------------------------------------------  # 60個

        private void button15_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.fullScreen = true; //設播放器全屏播放
        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
            //axWindowsMediaPlayer1設定URL後, 會自動播放
            axWindowsMediaPlayer1.settings.autoStart = true;     //自動播放
        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {
            //axWindowsMediaPlayer1設定URL後, 不會自動播放
            axWindowsMediaPlayer1.settings.autoStart = false;     //自動播放
        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {
            string filename = @"D:\vcs\astro\_DATA2\_mp3\陳盈潔_台語精選集6CD\disc3\01.南都夜曲.mp3";
            axWindowsMediaPlayer1.URL = filename;
        }

        //------------------------------------------------------------  # 60個

        private void button19_Click(object sender, EventArgs e)
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



//axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(fn));
//richTextBox1.Text += "加入播放清單: " + fn + "\n";

