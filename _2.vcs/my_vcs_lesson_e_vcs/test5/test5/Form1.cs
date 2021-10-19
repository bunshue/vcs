using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace test5
{
    public partial class Form1 : Form
    {
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

        string filename = @"C:\______test_files\_mp3\aaaa.mp3";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }


        private void button2_Click(object sender, EventArgs e)
        {
            Play();

        }


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
                if (durLength == "" || durLength == "\0") return 0;
                return (int)(Convert.ToDouble(durLength));
            }
        }





        private void button3_Click(object sender, EventArgs e)
        {
            //pause

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //resume

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //stop
        }


    }
}
