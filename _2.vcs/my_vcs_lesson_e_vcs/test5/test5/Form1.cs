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
        /// <summary>  

        /// API函數  www.2cto.com

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
            int month = 3;
            int day = 11;
            string result = getAstro(month, day);
            richTextBox1.Text += result + "\n";

        }

        private static String getAstro(int month, int day)
        {
            String[] starArr = {"魔羯座","水瓶座", "雙魚座", "牡羊座",
        "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座" };
            int[] DayArr = { 22, 20, 19, 21, 21, 21, 22, 23, 23, 23, 23, 22 };  // 兩個星座分割日
            int index = month;
            // 所查詢日期在分割日之前，索引-1，否則不變
            if (day < DayArr[month - 1])
            {
                index = index - 1;
            }
            index = index % 12;
            // 返回索引指向的星座string
            return starArr[index];
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


    }
}
