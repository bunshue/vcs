using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace SongPlayShroudAegis
{
    public partial class Form1 : Form
    {
        int width = 0, heigh = 0;
        string strpath;
        public Form1()
        {
            InitializeComponent();
            strpath = Environment.SystemDirectory + "\\music";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.timer1.Enabled = true;
            width = this.Width;
            heigh = this.Height;
          
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            ExitWindows();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            try
            {
                drowInfo();
                this.timer1.Interval = new Random().Next(800, 1600);
                string strname = new Random().Next(1, 4).ToString();
                if (this.axWindowsMediaPlayer1.status == "" || this.axWindowsMediaPlayer1.status == "已停止")
                {
                    string strUrl = strpath + "\\" + strname + ".mp3";
                    this.axWindowsMediaPlayer1.URL = strUrl;
                }
            }
            catch(Exception eb)
            {
                timer1.Enabled = false;
                MessageBox.Show(eb.Message);
            }
        }

        private void drowInfo()
        {
            Graphics myGraphics = this.CreateGraphics();
            myGraphics.Clear(Color.Black);
            string strinfo = "歌曲播放螢幕保護";
            int x = new Random().Next(0, width - 250);
            int y = new Random().Next(50, heigh-20);
            myGraphics.DrawString(strinfo, new Font("华文形楷", 16, FontStyle.Bold), new SolidBrush(Color.FromArgb(new Random().Next(50, 255), new Random().Next(70, 255), new Random().Next(36, 255))),x,y);

        }

        private void ExitWindows()
        {
            this.timer1.Enabled = false;
            Application.Exit();
        }

    }
}