using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FileStream, path
using System.Media;	        //for SoundPlayer

using Microsoft.Win32;    //for RegistryKey
using System.Runtime.InteropServices;   //for DllImport

//using System.Threading; //for thread
using WMPLib;   //for mp3


namespace vcs_test_all_08_Media
{
    public partial class Form1 : Form
    {
        private WMPLib.WindowsMediaPlayer wplayer;// = new WMPLib.WindowsMediaPlayer();
        public Form1()
        {
            InitializeComponent();
            wplayer = new WMPLib.WindowsMediaPlayer();
            trackBar1.Value = wplayer.settings.volume;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\aaaa.mp3";       //一定要有@
            Mp3Info mp3_information;
            byte[] Info = getLast128(filename);
            mp3_information = getMp3Info(Info);

            richTextBox1.Text += "Title : " + mp3_information.Title + "\n";
            richTextBox1.Text += "Artist : " + mp3_information.Artist + "\n";
            richTextBox1.Text += "Album : " + mp3_information.Album + "\n";
            richTextBox1.Text += "Year : " + mp3_information.Year + "\n";

            richTextBox1.Text += "identify : " + mp3_information.identify + "\n";
            richTextBox1.Text += "Comment : " + mp3_information.Comment + "\n";
            richTextBox1.Text += "reserved1 : " + mp3_information.reserved1 + "\n";
            richTextBox1.Text += "reserved2 : " + mp3_information.reserved2 + "\n";
            richTextBox1.Text += "reserved3 : " + mp3_information.reserved3 + "\n";
            richTextBox1.Text += "\n";
        }
        public struct Mp3Info
        {
            public string identify;//TAG，三個位元組
            public string Title;//歌曲名,30個位元組
            public string Artist;//歌手名,30個位元組
            public string Album;//所屬唱片,30個位元組
            public string Year;//年,4個字元
            public string Comment;//注釋,28個位元組
            public char reserved1;//保留位，一個位元組
            public char reserved2;//保留位，一個位元組
            public char reserved3;//保留位，一個位元組
        }

        //所以，我們只要把MP3檔的最後128個位元組分段讀出來並保存到該結構裡就可以了。函式定義如下：
        private byte[] getLast128(string FileName)
        {
            FileStream fs = new FileStream(FileName, FileMode.Open, FileAccess.Read);
            Stream stream = fs;
            stream.Seek(-128, SeekOrigin.End);
            const int seekPos = 128;
            int rl = 0;
            byte[] Info = new byte[seekPos];
            rl = stream.Read(Info, 0, seekPos);
            fs.Close();
            stream.Close();
            return Info;
        }
        //再對上面返回的位元組陣列分段取出，並保存到Mp3Info結構中返回:
        private Mp3Info getMp3Info(byte[] Info)
        {
            Mp3Info mp3Info = new Mp3Info();
            string str = null;
            int i;
            int position = 0;//迴圈的起始值
            int currentIndex = 0;//Info的當前索引值
            //獲取TAG標識(陣列前3個)
            for (i = currentIndex; i < currentIndex + 3; i++)
            {
                str = str + (char)Info[i];
                position++;
            }
            currentIndex = position;
            mp3Info.identify = str;
            //獲取歌名（陣列3-32）
            str = null;
            byte[] bytTitle = new byte[30];//將歌名部分讀到一個單獨的陣列中
            int j = 0;
            for (i = currentIndex; i < currentIndex + 30; i++)
            {
                bytTitle[j] = Info[i];
                position++;
                j++;
            }
            currentIndex = position;
            mp3Info.Title = this.byteToString(bytTitle);
            //獲取歌手名（陣列33-62）
            str = null;
            j = 0;
            byte[] bytArtist = new byte[30];//將歌手名部分讀到一個單獨的陣列中
            for (i = currentIndex; i < currentIndex + 30; i++)
            {
                bytArtist[j] = Info[i];
                position++;
                j++;
            }
            currentIndex = position;
            mp3Info.Artist = this.byteToString(bytArtist);
            //獲取唱片名（陣列63-92）
            str = null;
            j = 0;
            byte[] bytAlbum = new byte[30];//將唱片名部分讀到一個單獨的陣列中
            for (i = currentIndex; i < currentIndex + 30; i++)
            {
                bytAlbum[j] = Info[i];
                position++;
                j++;
            }
            currentIndex = position;
            mp3Info.Album = this.byteToString(bytAlbum);
            //獲取年 （陣列93-96）
            str = null;
            j = 0;
            byte[] bytYear = new byte[4];//將年部分讀到一個單獨的陣列中
            for (i = currentIndex; i < currentIndex + 4; i++)
            {
                bytYear[j] = Info[i];
                position++;
                j++;
            }
            currentIndex = position;
            mp3Info.Year = this.byteToString(bytYear);
            //獲取注釋（陣列97-124）
            str = null;
            j = 0;
            byte[] bytComment = new byte[28];//將注釋部分讀到一個單獨的陣列中
            for (i = currentIndex; i < currentIndex + 25; i++)
            {
                bytComment[j] = Info[i];
                position++;
                j++;
            }
            currentIndex = position;
            mp3Info.Comment = this.byteToString(bytComment);
            //以下獲取保留位（陣列125-127）
            mp3Info.reserved1 = (char)Info[++position];
            mp3Info.reserved2 = (char)Info[++position];
            mp3Info.reserved3 = (char)Info[++position];
            return mp3Info;

        }

        //上面程式用到下面的方法：
        /// <summary>
        /// 將位元組陣列轉換成字串
        /// </summary>
        /// <param name = "b">位元組陣列</param>
        /// <returns>返回轉換後的字串</returns>
        private string byteToString(byte[] b)
        {
            //Encoding enc = Encoding.GetEncoding("GB2312");
            Encoding enc = Encoding.GetEncoding("BIG5");
            string str = enc.GetString(b);
            str = str.Substring(0, str.IndexOf('\0') >= 0 ? str.IndexOf('\0') : str.Length);//去掉無用字元
            return str;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //法一
            //直接使用 System.Media.SoundPlayer 類別 播放.wav檔
            //System.Media.SoundPlayer sp = new System.Media.SoundPlayer(@"C:\______test_files\WindowsShutdown.wav");

            //法二, 直接使用 System.Media.SoundPlayer 類別
            //System.Media.SoundPlayer sp = new System.Media.SoundPlayer();
            //sp.SoundLocation = @"F:\_______mp3_ALL_all1\_mp3_0_中英日語文\《遥远的绝响--配乐朗诵余秋雨作品(共4篇)》.赵忠祥.[wav]\02.都江堰.wav";

            //法三
            //using System.Media;
            //SoundPlayer sp = new SoundPlayer(@"C:\______test_files\WindowsShutdown.wav");
            //sp.Play(); // 撥放

            //法四
            System.Media.SoundPlayer player = new System.Media.SoundPlayer();
            player.SoundLocation = @"C:\______test_files\start.wav";
            player.Play();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //法一
            //直接使用 System.Media.SoundPlayer 類別
            System.Media.SoundPlayer sp = new System.Media.SoundPlayer(@"C:\______test_files\WindowsShutdown.wav");

            //法二
            //System.Media.SoundPlayer sp = new System.Media.SoundPlayer();
            //sp.SoundLocation = @"F:\_______mp3_ALL_all1\_mp3_0_中英日語文\《遥远的绝响--配乐朗诵余秋雨作品(共4篇)》.赵忠祥.[wav]\02.都江堰.wav";

            sp.Stop(); // 停止
        }

        int number = 0;
        private void button3_Click(object sender, EventArgs e)
        {
            //播放系統預設的音效
            switch (number)
            {
                case 0:
                    System.Media.SystemSounds.Beep.Play();
                    richTextBox1.Text += "Beep\n";
                    break;
                case 1:
                    System.Media.SystemSounds.Asterisk.Play();
                    richTextBox1.Text += "Asterisk\n";
                    break;
                case 2:
                    System.Media.SystemSounds.Exclamation.Play();
                    richTextBox1.Text += "Exclamation\n";
                    break;
                case 3:
                    System.Media.SystemSounds.Hand.Play();
                    richTextBox1.Text += "Hand\n";
                    break;
                case 4:
                    System.Media.SystemSounds.Question.Play();
                    richTextBox1.Text += "Question\n";
                    break;
                default:
                    System.Media.SystemSounds.Beep.Play();
                    richTextBox1.Text += "Beep\n";
                    break;
            }
            number++;
            if (number > 4)
                number = 0;
        }


        // API 宣告
        [DllImport("winmm.dll", EntryPoint = "mciSendString", CharSet = CharSet.Auto)]
        public static extern int mciSendString(
            string lpstrCommand, string lpstrReturnString,
            int uReturnLength, int hwndCallback);

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += (GetMediaLen(@"C:\______test_files\WindowsShutdown.wav").ToString() + " 秒\n");
            //richTextBox1.Text += (GetMediaLen(@"C:\aaaa.mp3").ToString() + " 秒");
            //richTextBox1.Text += (GetMediaLen(@"F:\_______VIDEO_ALL_all1\[诸神字幕组][TBS][世界遗产][20160124 加德满都谷地].mp4").ToString() + " 秒");
        }

        // 取得多媒體檔案長度
        private long GetMediaLen(string File)
        {
            long RetVal = 0;
            string key = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\MCI Extensions";
            RegistryKey RegKey = Registry.LocalMachine.OpenSubKey(key);
            string FileExt = Path.GetExtension(File).Replace(".", "");
            string tp = RegKey.GetValue(FileExt, "MPEGVideo").ToString();
            RegKey.Close();

            string tm = new string((char)0, 128);
            if (mciSendString("open \"" + File + "\" type " + tp + " alias Media", null, 0, 0) == 0)
            {
                if (mciSendString("status Media length", tm, tm.Length, 0) == 0)
                {
                    tm = tm.Trim((char)0);
                    if (!string.IsNullOrEmpty(tm)) RetVal = Convert.ToInt64(tm) / 1000;
                }
                mciSendString("close Media", null, 0, 0);
            }
            return RetVal;
        }

        //參考/加入參考/COM 選W indows Media Player (wmp.dll)
        //using WMPLib;
        private void button5_Click(object sender, EventArgs e)
        {
            wplayer.URL = @"C:\______test_files\bbbb.mp3";
            wplayer.settings.setMode("loop", true);
            wplayer.controls.play();
            timer1.Enabled = true;
            richTextBox1.Text += wplayer.currentMedia.getItemInfo("Title") + "\n";
            richTextBox1.Text += "Title: " + wplayer.currentMedia.getItemInfo("Title") + "\n";
            richTextBox1.Text += "Author: " + wplayer.currentMedia.getItemInfo("Author") + "\n";
            richTextBox1.Text += "Copyright: " + wplayer.currentMedia.getItemInfo("Copyright") + "\n";
            richTextBox1.Text += "Description: " + wplayer.currentMedia.getItemInfo("Description") + "\n";
            richTextBox1.Text += "Duration: " + wplayer.currentMedia.getItemInfo("Duration").ToString() + " Sec\n";
            richTextBox1.Text += "FileSize: " + wplayer.currentMedia.getItemInfo("FileSize").ToString() + "\n";
            richTextBox1.Text += "FileType: " + wplayer.currentMedia.getItemInfo("FileType").ToString() + "\n";
            richTextBox1.Text += "sourceURL: " + wplayer.currentMedia.getItemInfo("sourceURL").ToString() + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            wplayer.controls.stop();
            timer1.Enabled = false;
            progressBar1.Value = 0;
            trackBar2.Value = 0;
        }

        public int MediaGetPosition()
        {
            int ret = 0;
            if (WMPLib.WMPPlayState.wmppsPlaying != wplayer.playState)
            {
                return ret;
            }
            double curPos = wplayer.controls.currentPosition;
            double totalLen = wplayer.currentMedia.duration;
            ret = (int)((curPos / totalLen) * 1000);
            //richTextBox1.Text += "curPos = " + curPos.ToString() + "\n";
            //richTextBox1.Text += "totalLen = " + totalLen.ToString() + "\n";
            //richTextBox1.Text += "ret = " + ret.ToString() + "\n";
            return ret;
        }  

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (WMPLib.WMPPlayState.wmppsPlaying != wplayer.playState)
            {
                return;
            }
            int position = MediaGetPosition();
            progressBar1.Value = position;
            trackBar2.Value = position;
            if (WMPLib.WMPPlayState.wmppsPlaying == wplayer.playState)
            {
                label1.Text = wplayer.controls.currentPositionString + " / " + wplayer.currentMedia.durationString;
            }
            else
            {
                label1.Text = "00:00" + " / " + wplayer.currentMedia.durationString;
                timer1.Enabled = false;
            }  
        }

        private void button7_Click(object sender, EventArgs e)
        {
            wplayer.controls.pause();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            wplayer.controls.play();
            timer1.Enabled = true;
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            wplayer.settings.volume = trackBar1.Value;
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            if (WMPLib.WMPPlayState.wmppsPlaying != wplayer.playState)
            {
                trackBar2.Value = 0;
                return;
            }
            int position = (int)(trackBar2.Value * wplayer.currentMedia.duration / 1000);
            wplayer.controls.pause();
            wplayer.controls.currentPosition = position;
            wplayer.controls.play();
        }
  
    }
}
