using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
using System.IO;

namespace vcs_MyPlayer5_MCI
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\_mp3\aaaa.mp3";
        classMci mci = new classMci();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            mci.FileName = filename;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            mci.Play();


        }

        private void button2_Click(object sender, EventArgs e)
        {
            mci.Pause();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            mci.StopT();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Duration : " + mci.Duration + "\n";

            //richTextBox1.Text += "CurrentPosition : " + mci.CurrentPosition + "\n";
        }
    }

    /// <summary>
    /// classMci 的摘要說明。
    /// </summary>
    public class classMci
    {
        public classMci()
        {
            //
            // TODO: 在此處添加構造函數邏輯
            //
        }

        //定義API函數使用的字符串變量
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 260)]
        private string Name = "";
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 128)]
        private string durLength = "";
        [MarshalAs(UnmanagedType.LPTStr, SizeConst = 128)]
        private string TemStr = "";
        int ilong;

        //定義播放狀態枚舉變量
        public enum State
        {
            mPlaying = 1,
            mPause = 2,
            mStop = 3
        };

        //結構變量
        public struct structMCI
        {
            public bool bMut;
            public int iDur;
            public int iPos;
            public int iVol;
            public int iBal;
            public string iName;
            public State state;
        };

        public structMCI mc = new structMCI();
        //取得播放文件屬性
        public string FileName
        {
            get
            {
                return mc.iName;
            }
            set
            {
                //ASCIIEncoding asc = new ASCIIEncoding();
                try
                {
                    TemStr = "";
                    TemStr = TemStr.PadLeft(127, Convert.ToChar(" "));
                    Name = Name.PadLeft(260, Convert.ToChar(" "));
                    mc.iName = value;
                    ilong = APIClass.GetShortPathName(mc.iName, Name, Name.Length);
                    Name = GetCurrPath(Name);
                    //Name = "open " + Convert.ToChar(34) + Name + Convert.ToChar(34) + " alias media";
                    Name = "open " + Convert.ToChar(34) + Name + Convert.ToChar(34) + " alias media";
                    ilong = APIClass.mciSendString("close all", TemStr, TemStr.Length, 0);
                    ilong = APIClass.mciSendString(Name, TemStr, TemStr.Length, 0);
                    ilong = APIClass.mciSendString("set media time format milliseconds", TemStr, TemStr.Length, 0);
                    mc.state = State.mStop;
                }
                catch
                {
                    MessageBox.Show("出錯錯誤!");
                }
            }
        }

        //播放
        public void Play()
        {
            TemStr = "";
            TemStr = TemStr.PadLeft(127, Convert.ToChar(" "));
            APIClass.mciSendString("play media", TemStr, TemStr.Length, 0);
            mc.state = State.mPlaying;
        }

        //停止
        public void StopT()
        {
            TemStr = "";
            TemStr = TemStr.PadLeft(128, Convert.ToChar(" "));
            ilong = APIClass.mciSendString("close media", TemStr, 128, 0);
            ilong = APIClass.mciSendString("close all", TemStr, 128, 0);
            mc.state = State.mStop;
        }

        public void Pause()
        {
            TemStr = "";
            TemStr = TemStr.PadLeft(128, Convert.ToChar(" "));
            ilong = APIClass.mciSendString("pause media", TemStr, TemStr.Length, 0);
            mc.state = State.mPause;
        }

        private string GetCurrPath(string name)
        {
            if (name.Length < 1) return "";
            name = name.Trim();
            name = name.Substring(0, name.Length - 1);
            return name;
        }

        //總時間
        public int Duration
        {
            get
            {
                durLength = "";
                durLength = durLength.PadLeft(128, Convert.ToChar(" "));
                APIClass.mciSendString("status media length", durLength, durLength.Length, 0);
                durLength = durLength.Trim();
                if (durLength == "") return 0;
                return (int)(Convert.ToDouble(durLength) / 1000f);
            }
        }

        //當前時間
        public int CurrentPosition
        {
            get
            {
                durLength = "";
                durLength = durLength.PadLeft(128, Convert.ToChar(" "));
                APIClass.mciSendString("status media position", durLength, durLength.Length, 0);
                mc.iPos = (int)(Convert.ToDouble(durLength) / 1000f);
                return mc.iPos;
            }
        }
    }

    public class APIClass
    {
        [DllImport("kernel32.dll", CharSet = CharSet.Auto)]
        public static extern int GetShortPathName(
         string lpszLongPath,
         string shortFile,
         int cchBuffer
        );
        [DllImport("winmm.dll", EntryPoint = "mciSendString", CharSet = CharSet.Auto)]
        public static extern int mciSendString(
         string lpstrCommand,
         string lpstrReturnString,
         int uReturnLength,
         int hwndCallback
        );
    }
}
