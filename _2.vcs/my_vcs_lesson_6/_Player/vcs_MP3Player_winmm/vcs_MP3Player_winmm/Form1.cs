using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Runtime.InteropServices;

using Microsoft.Win32;  //for Registry

namespace vcs_MP3Player_winmm
{
    public partial class Form1 : Form
    {
        /*  same
        // API 宣告
        [DllImport("winmm.dll", EntryPoint = "mciSendString", CharSet = CharSet.Auto)]
        public static extern int mciSendString(string lpstrCommand, string lpstrReturnString, int uReturnLength, int hwndCallback);
        */

        //winmm.dll播放在window下播放MP3短路徑沒有任何問題，如果是長路徑必須把長路徑轉化成DOS下的短路徑表示方法才能正常播放。

        /*
        [DllImport("kernel32.dll ", CharSet = CharSet.Auto)]

        public static extern int GetShortPathName([MarshalAs(UnmanagedType.LPTStr)] string path,[MarshalAs(UnmanagedType.LPTStr)] StringBuilder shortPath,int shortPathLength);

        StringBuilder shortMusicPath = new StringBuilder(80);

        int result = GetShortPathName(mymp3list[0], shortMusicPath, shortMusicPath.Capacity);

        string s = shortMusicPath.ToString();

        GetShortPathName參數說明：1、MP3路徑；2、返回的短路徑；3、內存中文本最大長度。
        */

        /// <summary>  
        /// API函數
        /// </summary>

        [DllImport("winmm.dll", EntryPoint = "mciSendString", CharSet = CharSet.Auto)]
        private static extern int mciSendString(
        string lpstrCommand,
        string lpstrReturnString,
        int uReturnLength,
        int hwndCallback
        );

        string filename = @"D:\_git\vcs\_1.data\______test_files1\_mp3\aaaa.mp3";

        /// <summary>  

        /// 播放音樂 

        /// </summary>

        public void Play()
        {
            string tmepstr = "";

            tmepstr = tmepstr.PadLeft(128, Convert.ToChar(" "));

            mciSendString("close all", "", 0, 0);

            mciSendString("open " + filename + " alias media", tmepstr, tmepstr.Length, 0); mciSendString("play media", "", 0, 0);
        }


        /// <summary>  
        /// 暫停 
        /// </summary>
        public void Pause()
        {
            mciSendString("pause media", "", 0, 0);
        }

        /// <summary>  
        /// 停止 
        /// </summary>
        public void Stop()
        {
            mciSendString("close media", "", 0, 0);
        }

        /// <summary>  
        /// 繼續播放 
        /// </summary>

        public void Resume()
        {
            string TemStr = "";
            TemStr = TemStr.PadLeft(128, Convert.ToChar(" "));
            mciSendString("resume media", TemStr, TemStr.Length, 0);
        }

        //獲取音樂長度
        public int GetMusicLength
        {
            get
            {
                string durLength = "";
                durLength = durLength.PadLeft(128, Convert.ToChar(" "));
                mciSendString("status media length", durLength, durLength.Length, 0);
                durLength = durLength.Trim();
                if (durLength == "" || durLength == "\0")
                {
                    return 0;
                }
                return (int)(Convert.ToDouble(durLength));
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Play();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Pause();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Resume();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Stop();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //取得媒體長度
            int len = GetMusicLength;
            richTextBox1.Text += "長度 : " + len.ToString() + " 毫秒\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //richTextBox1.Text += (GetMediaLen(@"D:\_git\vcs\_1.data\______test_files1\_wav\WindowsShutdown.wav").ToString() + " 秒\n");
            //richTextBox1.Text += (GetMediaLen(@"D:\_git\vcs\_1.data\______test_files1\_mp3\aaaa.mp3").ToString() + " 秒");
            //richTextBox1.Text += (GetMediaLen(@"F:\_______VIDEO_ALL_all1\[诸神字幕组][TBS][世界遗产][20160124 加德满都谷地].mp4").ToString() + " 秒");

            string filename = @"D:\_git\vcs\_1.data\______test_files1\_mp3\aaaa.mp3";
            long len = GetMediaLen(filename);
            richTextBox1.Text += "檔案 : " + filename + ", 長度 : " + len.ToString() + " 秒\n";

            filename = @"D:\_git\vcs\_1.data\______test_files1\_wav\WindowsShutdown.wav";
            len = GetMediaLen(filename);
            richTextBox1.Text += "檔案 : " + filename + ", 長度 : " + len.ToString() + " 秒\n";
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
                    if (!string.IsNullOrEmpty(tm))
                    {
                        RetVal = Convert.ToInt64(tm) / 1000;
                    }
                }
                mciSendString("close Media", null, 0, 0);
            }
            return RetVal;
        }
    }
}

