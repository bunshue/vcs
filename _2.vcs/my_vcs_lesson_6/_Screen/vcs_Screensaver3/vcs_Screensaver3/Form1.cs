using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

//移除舊的AxInterop.WMPLib.dll 和 Interop.WMPLib.dll
//參考/加入參考/ 選擇 dll / AxInterop.WMPLib.dll 和 Interop.WMPLib.dll
//Interop.WMPLib.dll的屬性的內嵌Interop型別 改成false

namespace vcs_Screensaver3
{
    public partial class Form1 : Form
    {
        int W = 0;
        int H = 0;
        string foldername = @"C:\_git\vcs\_1.data\______test_files1\_mp3b";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Enabled = true;
            W = this.Width;
            H = this.Height;
            label2.Text = "";   //for debug
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
            Application.Exit();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            try
            {
                drowInfo();
                this.timer1.Interval = new Random().Next(800, 1600);
                string strname = new Random().Next(1, 4).ToString();
                label1.Text += strname + "  ";
                if (this.axWindowsMediaPlayer1.status == "" || this.axWindowsMediaPlayer1.status == "已停止")
                {
                    string strUrl = foldername + "\\" + strname + ".mp3";
                    this.axWindowsMediaPlayer1.URL = strUrl;
                    label1.Text += strUrl + " ";
                }
            }
            catch (Exception eb)
            {
                timer1.Enabled = false;
                MessageBox.Show(eb.Message);
            }
        }

        private void drowInfo()
        {
            Graphics g = this.CreateGraphics();
            g.Clear(Color.Black);
            string show_message = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
            int x = new Random().Next(0, W - 350);
            int y = new Random().Next(50, H - 120);
            g.DrawString(show_message, new Font("標楷體", 30, FontStyle.Bold), new SolidBrush(Color.FromArgb(new Random().Next(50, 255), new Random().Next(70, 255), new Random().Next(36, 255))), x, y);
            //label2.Text = "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
        }
    }
}
