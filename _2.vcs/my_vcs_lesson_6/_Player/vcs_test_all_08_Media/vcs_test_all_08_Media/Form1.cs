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
