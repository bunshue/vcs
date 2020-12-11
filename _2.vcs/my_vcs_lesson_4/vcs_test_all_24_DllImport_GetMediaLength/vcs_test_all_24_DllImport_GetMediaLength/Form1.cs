using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  //for path
using Microsoft.Win32;    //for RegistryKey
using System.Runtime.InteropServices;   //for DllImport

namespace vcs_test_all_24_DllImport_GetMediaLength
{
    public partial class Form1 : Form
    {
        // API 宣告
        [DllImport("winmm.dll", EntryPoint = "mciSendString", CharSet = CharSet.Auto)]
        public static extern int mciSendString(
            string lpstrCommand, string lpstrReturnString,
            int uReturnLength, int hwndCallback);

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = (GetMediaLen(@"C:\______test_files\_wav\WindowsShutdown.wav").ToString() + " 秒");
            //label1.Text = (GetMediaLen(@"C:\______test_files\_mp3\aaaa.mp3").ToString() + " 秒");
            //label1.Text = (GetMediaLen(@"C:\______test_files\[诸神字幕组][TBS][世界遗产][20160124 加德满都谷地].mp4").ToString() + " 秒");
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
   
    }
}
