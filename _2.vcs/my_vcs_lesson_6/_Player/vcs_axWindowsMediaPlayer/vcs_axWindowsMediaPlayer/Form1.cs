using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Path

/*  sugar
使用AxWindowsMediaPlayer播放多媒體

加入工具箱

工具箱/滑鼠右鍵/選擇項目/
/COM 元件 頁籤 /勾選Windows Media Player(wmp.dll)	/ 確定


會發現工具箱多了個Windows Media Player的控制項
就是 axWindowsMediaPlayer

*/

/* old
//使用WMP播放音樂檔
//參考/加入參考/COM/Windows Media Player 1.0 wmp.dll

//WMPLib.WindowsMediaPlayer player = new WMPLib.WindowsMediaPlayer();
*/

/* old
參考:
C#利用AxWindowsMediaPlayer播放mp3
http://kikilala-tw.blogspot.com/2009/09/caxwindowsmediaplayermp3.html

工具箱/所有Windows Form，右鍵，選擇項目 選COM元件，選Windows Media Player wmp.dll，
工具箱就會出現Windows Media Player控件
*/



/*  old

工具箱/右鍵/選擇項目/COM元件/選Windows Media Player

工具箱的通用控制項會出現 Windows Media Player

參考內會出現AxWMPLib和WMPLib, 不用保留bin/Debug內的dll

*/

/* network radio old
參考/加入參考/ 選擇 AxInterop.WMPLib.dll 和 Interop.WMPLib.dll

點選兩個dll的屬性
內嵌Interop型別 改 False
複製到本機 改 True
*/



namespace vcs_axWindowsMediaPlayer
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\enka.avi";
        //string filename = "C:\\______test_files\\_mp3\\07    都はろみ--妻戀道中(他鄉思妻兒).mp3";

        //用來儲存音樂檔案的全路徑
        List<string> listSong = new List<string>();
        bool flag_playing = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label3.Text = "";
            //axWindowsMediaPlayer1.Dock = DockStyle.Fill;     //填滿整個表單
            axWindowsMediaPlayer1.settings.volume = 50;
            //axWindowsMediaPlayer1.settings.autoStart = false;             //設定不自動播放, 預設是自動播放

            //axWindowsMediaPlayer1.URL = @"C:\______test_files\_mp3\16.監獄風雲.mp3";
            axWindowsMediaPlayer1.settings.rate = 1;    //播放速度
            //axWindowsMediaPlayer1.settings.getMode("loop"); //useless


            trackBar1.Minimum = 0;                                          //設定音量調整Bar最小值為最小音量值(0)
            trackBar1.Maximum = 100;                                        //設定音量調整Bar最大值為最大音量值(100)
            trackBar1.Value = axWindowsMediaPlayer1.settings.volume;        //設定音量調整Bar目前值為目前音量值
            label1.Text = "音量 : " + trackBar1.Value.ToString();

            timer1.Enabled = true;
            listBox1.SelectedIndex = -1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //開啟多檔
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Title = "請選擇檔案";
            ofd.Multiselect = true;
            //ofd.InitialDirectory = @"D:\vcs\astro\_DATA2\_mp3\";
            ofd.InitialDirectory = @"C:\______test_files";
            ofd.Filter = "音樂檔案|*.wav|mp3檔案|*.mp3|所有檔案|*.*";
            //ofd.Filter = "mp3文件|*.mp3|wav文件|*.wav|wma文件|*.wma|wmv文件|*.wmv|所有格式|*.*";

            ofd.FilterIndex = 3;
            ofd.ShowDialog();
            //獲得我們在資料夾中選擇所有檔案的全路徑
            string[] path = ofd.FileNames;
            for (int i = 0; i < path.Length; i++)
            {
                //將音樂檔案的檔名載入到ListBox中
                listBox1.Items.Add(Path.GetFileName(path[i]));
                //將音樂檔案的全路徑儲存到泛型集合中
                listSong.Add(path[i]);
            }
            listBox1.SelectedIndex = 0;
            flag_playing = false;

            /*  播放單一檔案
            //表單標題顯示檔案路徑
            this.Text = "播放檔案 : \t" + filename;
            //axWindowsMediaPlayer1播放開檔對話方塊所選擇的檔案
            axWindowsMediaPlayer1.URL = filename;   //開啟檔案
            trackBar2.Maximum = (int)axWindowsMediaPlayer1.currentMedia.duration;          //設定播放位置調整Bar最大值
            */

            /*
            //一次加入到播放清單
            axWindowsMediaPlayer1.currentPlaylist = axWindowsMediaPlayer1.newPlaylist("播放列表", "");
            foreach (string fn in ofd.FileNames)
            {
                axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(fn));
                richTextBox1.Text += "加入播放清單: " + fn + "\n";
            }
            */

            //加入單一檔案 沒效
            //axWindowsMediaPlayer1.newMedia(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            /*
            axWindowsMediaPlayer1.Ctlcontrols.play();　　　　//開始播放
            richTextBox1.Text += "播放\n";
            */


            if (listBox1.SelectedIndex == -1)
                return;

            if (button2.Text == "播放")
            {
                if (flag_playing == false)
                {
                    axWindowsMediaPlayer1.URL = listSong[listBox1.SelectedIndex];   //開啟檔案
                    //表單標題顯示檔案路徑
                    this.Text = "播放檔案 : \t" + listSong[listBox1.SelectedIndex];
                }

                axWindowsMediaPlayer1.Ctlcontrols.play();
                button2.Text = "暫停";
                flag_playing = true;

                int balance = axWindowsMediaPlayer1.settings.balance;
                richTextBox1.Text += "balane = " + balance.ToString();
                trackBar3.Value = balance;

                timer1.Enabled = true;
            }
            else
            {
                axWindowsMediaPlayer1.Ctlcontrols.pause();        //暫停撥放
                button2.Text = "播放";
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.pause();　　　　//暫停播放
            richTextBox1.Text += "暫停\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {

            if (listBox1.SelectedIndex == -1)
                return;

            richTextBox1.Text += "停止\n";
            axWindowsMediaPlayer1.Ctlcontrols.stop();         //停止播放
            //axWindowsMediaPlayer1.close();    //停止播放 same

            flag_playing = false;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.previous();　　//播放上一段
            richTextBox1.Text += "播放上一段\n";

            /*
            if (listBox1.SelectedIndex == -1)
                return;

            // 獲得當前選中歌曲的索引
            int index = listBox1.SelectedIndex;
            index--;
            if (index < 0)
            {
                index = listBox1.Items.Count - 1;
            }
            //將重新改變後的索引重新的賦值給當前選中項
            listBox1.SelectedIndex = index;
            axWindowsMediaPlayer1.URL = listSong[index];
            axWindowsMediaPlayer1.Ctlcontrols.play();
            */
        }

        private void button6_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.next(); 　　　 //播放下一段
            richTextBox1.Text += "播放下一段\n";

            /*
            if (listBox1.SelectedIndex == -1)
                return;

            int index = listBox1.SelectedIndex;
            index++;
            if (index == listBox1.Items.Count)
            {
                index = 0;
            }
            listBox1.SelectedIndex = index;
            axWindowsMediaPlayer1.URL = listSong[index];
            axWindowsMediaPlayer1.Ctlcontrols.play();
            */
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (axWindowsMediaPlayer1.settings.mute == false)
            {
                axWindowsMediaPlayer1.settings.mute = true;
                button7.Text = "恢復";
            }
            else
            {
                axWindowsMediaPlayer1.settings.mute = false;
                button7.Text = "靜音";
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (axWindowsMediaPlayer1.currentMedia == null)
                return;

            axWindowsMediaPlayer1.Ctlcontrols.currentPosition = 0;      //移動播放位置到最前面
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            //音量控制
            axWindowsMediaPlayer1.settings.volume = trackBar1.Value;      //改變音量大小

            label1.Text = "音量 : " + trackBar1.Value.ToString();
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {

        }

        private void trackBar2_MouseDown(object sender, MouseEventArgs e)
        {
            if (axWindowsMediaPlayer1.currentMedia == null)
                return;

            timer1.Enabled = false;
        }

        private void trackBar2_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void trackBar2_MouseUp(object sender, MouseEventArgs e)
        {
            if (axWindowsMediaPlayer1.currentMedia == null)
                return;

            timer1.Enabled = true;
            //播放位置
            axWindowsMediaPlayer1.Ctlcontrols.currentPosition = trackBar2.Value;          //改變播放位置
            label3.Text = axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + " / " + axWindowsMediaPlayer1.currentMedia.durationString + " " + (axWindowsMediaPlayer1.Ctlcontrols.currentPosition / axWindowsMediaPlayer1.currentMedia.duration).ToString("P0");
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (axWindowsMediaPlayer1.currentMedia == null)
                return;

            trackBar2.Minimum = 0;
            trackBar2.Maximum = (int)axWindowsMediaPlayer1.currentMedia.duration;          //設定撥放位置調整Bar最大值
            trackBar2.Value = (int)axWindowsMediaPlayer1.Ctlcontrols.currentPosition;

            //richTextBox1.Text += axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";
            //richTextBox1.Text += axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + "\n";

            label3.Text = axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + " / " + axWindowsMediaPlayer1.currentMedia.durationString + " " + (axWindowsMediaPlayer1.Ctlcontrols.currentPosition / axWindowsMediaPlayer1.currentMedia.duration).ToString("P0");


            progressBar1.Value = MediaGetPosition();
            if (WMPLib.WMPPlayState.wmppsPlaying == axWindowsMediaPlayer1.playState)
            {
                //richTextBox1.Text += axWindowsMediaPlayer1.Ctlcontrols.currentPositionString;
            }
            else
            {
                timer1.Enabled = false;
                //richTextBox1.Text += "00:00";
                button2.Text = "播放";
            }
        }

        public int MediaGetPosition()
        {
            int ret = 0;
            if (WMPLib.WMPPlayState.wmppsPlaying != axWindowsMediaPlayer1.playState)
            {
                return ret;
            }
            double curPos = axWindowsMediaPlayer1.Ctlcontrols.currentPosition;
            double totalLen = axWindowsMediaPlayer1.currentMedia.duration;
            ret = (int)((curPos / totalLen) * 100);
            //richTextBox1.Text += "ret = " + ret.ToString() + "\n";
            return ret;
        }

        private void bt_info_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex == -1)
                return;

            if (axWindowsMediaPlayer1.currentMedia == null)
                return;

            //axWindowsMediaPlayer1.Ctlcontrols.fastForward();  //快進
            //axWindowsMediaPlayer1.Ctlcontrols.fastReverse();    //快退 似無效
            //測試

            /*
            //加速
            richTextBox1.Text += "current rate = " + axWindowsMediaPlayer1.settings.rate.ToString() + "\n";
            axWindowsMediaPlayer1.settings.rate += 0.1;
            richTextBox1.Text += "new rate = " + axWindowsMediaPlayer1.settings.rate.ToString() + "\n";
            */

            /* no work
            axWindowsMediaPlayer1.URL = "https://www.youtube.com/watch?v=rjZksEz4kp0&t=337s";
            axWindowsMediaPlayer1.Ctlcontrols.play();　　　　//開始播放
            */

            richTextBox1.Text += "attributeCount:\t" + axWindowsMediaPlayer1.currentMedia.attributeCount.ToString() + "\n";
            richTextBox1.Text += "duration:\t" + axWindowsMediaPlayer1.currentMedia.duration.ToString() + "\n";
            richTextBox1.Text += "durationString:\t" + axWindowsMediaPlayer1.currentMedia.durationString + "\n";
            richTextBox1.Text += "name:\t" + axWindowsMediaPlayer1.currentMedia.name + "\n";
            richTextBox1.Text += "sourceURL:\t" + axWindowsMediaPlayer1.currentMedia.sourceURL + "\n";

            richTextBox1.Text += "currentPosition:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";
            richTextBox1.Text += "currentPositionString:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + "\n";
            richTextBox1.Text += "currentMarker:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentMarker.ToString() + "\n";

            richTextBox1.Text += "playCount:\t" + axWindowsMediaPlayer1.settings.playCount.ToString() + "\n";

            //info
            //axWindowsMediaPlayer1
            richTextBox1.Text += "status:\t" + axWindowsMediaPlayer1.status + "\n";
            richTextBox1.Text += "playState:\t" + axWindowsMediaPlayer1.playState + "\n";
            richTextBox1.Text += "URL:\t" + axWindowsMediaPlayer1.URL + "\n";
            richTextBox1.Text += "versionInfo:\t" + axWindowsMediaPlayer1.versionInfo + "\n";
            richTextBox1.Text += "windowlessVideo:\t" + axWindowsMediaPlayer1.windowlessVideo + "\n";
            richTextBox1.Text += "uiMode:\t" + axWindowsMediaPlayer1.uiMode + "\n";


            //axWindowsMediaPlayer1.settings
            richTextBox1.Text += "show baseURL = " + axWindowsMediaPlayer1.settings.baseURL + "\n";
            richTextBox1.Text += "show balance = " + axWindowsMediaPlayer1.settings.balance.ToString() + "\n";
            richTextBox1.Text += "show rate = " + axWindowsMediaPlayer1.settings.rate.ToString() + "\n";
            richTextBox1.Text += "show volume = " + axWindowsMediaPlayer1.settings.volume.ToString() + "\n";
            richTextBox1.Text += "show playCount = " + axWindowsMediaPlayer1.settings.playCount.ToString() + "\n";
            richTextBox1.Text += "show mute = " + axWindowsMediaPlayer1.settings.mute.ToString() + "\n";
            richTextBox1.Text += "show currentPlaylist.count = " + axWindowsMediaPlayer1.currentPlaylist.count.ToString() + "\n";
            //richTextBox1.Text += "show baseURL = " + axWindowsMediaPlayer1.currentPlaylist.Item.name + "\n";
            richTextBox1.Text += "show currentPlaylist.name = " + axWindowsMediaPlayer1.currentPlaylist.name + "\n";
            richTextBox1.Text += "show URL = " + axWindowsMediaPlayer1.URL + "\n";
            richTextBox1.Text += "show currentPosition = " + axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";
            richTextBox1.Text += "show currentItem.duration = " + axWindowsMediaPlayer1.Ctlcontrols.currentItem.duration.ToString() + "\n";
            richTextBox1.Text += "show currentMedia.duration = " + axWindowsMediaPlayer1.currentMedia.duration.ToString() + "\n";
            richTextBox1.Text += "播放位置用字串顯示：" + axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + "\n";

            //axWindowsMediaPlayer1.currentMedia
            richTextBox1.Text += "获取当前媒体信息\n";
            richTextBox1.Text += "Title:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Title") + "\n";
            richTextBox1.Text += "Author:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Author") + "\n";
            richTextBox1.Text += "Artist:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Artist") + "\n";
            richTextBox1.Text += "Genre:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Genre") + "\n";
            richTextBox1.Text += "WM/Genre:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("WM/Genre") + "\n";
            richTextBox1.Text += "Copyright:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Copyright") + "\n";
            richTextBox1.Text += "Description:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Description") + "\n";
            richTextBox1.Text += "持續時間:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Duration") + " 秒\n";
            richTextBox1.Text += "檔案大小:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("FileSize") + " Bytes\n";
            richTextBox1.Text += "檔案類型:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("FileType") + "\n";
            richTextBox1.Text += "sourceURL:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("sourceURL") + "\n";
            richTextBox1.Text += "header : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("header") + "\n";
            richTextBox1.Text += "album : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("album") + "\n";
            richTextBox1.Text += "year : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("year") + "\n";
            richTextBox1.Text += "comment : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("comment") + "\n";
            richTextBox1.Text += "track : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("track") + "\n";
            richTextBox1.Text += "zero-byte : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("zero-byte") + "\n";

            richTextBox1.Text += "currentPositionString:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + "\n";
            richTextBox1.Text += "currentPosition:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";
            richTextBox1.Text += "currentMarker:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentMarker.ToString() + "\n";
            richTextBox1.Text += "currentItem:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentItem.ToString() + "\n";

            richTextBox1.Text += "媒體長度:\t" + axWindowsMediaPlayer1.currentMedia.duration.ToString() + " 秒\n";
            richTextBox1.Text += "影像寬度:\t" + axWindowsMediaPlayer1.currentMedia.imageSourceWidth.ToString() + "\n";
            richTextBox1.Text += "影像高度:\t" + axWindowsMediaPlayer1.currentMedia.imageSourceHeight.ToString() + "\n";
            richTextBox1.Text += "Name:\t" + axWindowsMediaPlayer1.currentMedia.name + "\n";
            richTextBox1.Text += "全螢幕:\t" + axWindowsMediaPlayer1.fullScreen.ToString() + "\n";
            richTextBox1.Text += "播放器寬:\t" + axWindowsMediaPlayer1.Width.ToString() + "\n";
            richTextBox1.Text += "播放器高:\t" + axWindowsMediaPlayer1.Height.ToString() + "\n";
            richTextBox1.Text += "播放器名:\t" + axWindowsMediaPlayer1.Name + "\n";
            richTextBox1.Text += "聲量:\t" + axWindowsMediaPlayer1.settings.volume.ToString() + "\n";
            richTextBox1.Text += "URL:\t" + axWindowsMediaPlayer1.URL + "\n";
            richTextBox1.Text += "版本:\t" + axWindowsMediaPlayer1.versionInfo + "\n";
            //richTextBox1.Text += "XXXXXc:\t" + axWindowsMediaPlayer1.windowlessVideo + "\n";
            //richTextBox1.Text += "XXXXX:\t" + axWindowsMediaPlayer1.Ctlcontrols.isAvailable.ToString() + "\n";

            int W = axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceWidth;
            int H = axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceHeight;
            richTextBox1.Text += "W : " + W.ToString() + "\n";
            richTextBox1.Text += "H : " + H.ToString() + "\n";
            if (W == 0)
            {
                axWindowsMediaPlayer1.Visible = false;
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            string radio_url = @"http://live.leanstream.co/ICRTFM-MP3?args=tunein_mp3";

            try
            {
                axWindowsMediaPlayer1.URL = radio_url; //设置WindowsMediaPlayer的URL
            }
            catch (Exception ex)//捕获异常
            {
                MessageBox.Show(ex.Message);//显示异常信息
            }
        }

        private void trackBar3_Scroll(object sender, EventArgs e)
        {
            int balance =trackBar3.Value;
            if ((balance <= 100) && (balance >= -100))
            {
                axWindowsMediaPlayer1.settings.balance = balance;
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.fullScreen = true;   //全螢幕
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //快進
            axWindowsMediaPlayer1.Ctlcontrols.currentPosition += 20;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //快退
            axWindowsMediaPlayer1.Ctlcontrols.currentPosition -= 20;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //快轉
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //慢轉
        }

        private void button15_Click(object sender, EventArgs e)
        {
            int W = axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceWidth;
            int H = axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceHeight;
            richTextBox1.Text += "W : " + W.ToString() + "\n";
            richTextBox1.Text += "H : " + H.ToString() + "\n";
            if (W == 0)
            {
                axWindowsMediaPlayer1.Visible = false;
            }

            axWindowsMediaPlayer1.Width = axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceWidth;
            axWindowsMediaPlayer1.Height = axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceHeight;
            richTextBox1.Text += "設定1:1畫面\n";

            /*  設定任意大小
            axWindowsMediaPlayer1.Width = 800;
            axWindowsMediaPlayer1.Height = 800;
            */
        }
    }
}

