using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
參考/加入參考/ 選擇 AxInterop.WMPLib.dll 和 Interop.WMPLib.dll

點選兩個dll的屬性
內嵌Interop型別 改 False
複製到本機 改 True
*/

namespace vcs_NetworkRadio
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string radio_url = @"http://live.leanstream.co/ICRTFM-MP3?args=tunein_mp3";

            try
            {
                this.axWindowsMediaPlayer1.URL = radio_url; //设置WindowsMediaPlayer的URL
            }
            catch (Exception ex)//捕获异常
            {
                MessageBox.Show(ex.Message);//显示异常信息
            }


        }

    }
}
