using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_2_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            notifyIcon1.Icon = new Icon(@"c:\Vista_icons_06.ico");
            notifyIcon1.BalloonTipIcon = ToolTipIcon.Info;
            notifyIcon1.BalloonTipTitle = "NotifyIcon範例程式";
            notifyIcon1.BalloonTipText = "雙擊圖示，秀出應用程式";
            notifyIcon1.Text = "程式碼的撰寫詳書中說明";

            // 執行後，即出現在工作列
            notifyIcon1.ShowBalloonTip(1000);
        }

        private void notifyIcon1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (this.WindowState == FormWindowState.Minimized)
                this.WindowState = FormWindowState.Normal;

            this.Activate();
        }

        private void notifyIcon1_MouseClick(object sender, MouseEventArgs e)
        {
            // 滑鼠點擊後，才會出現
            notifyIcon1.ShowBalloonTip(
                1000,
                "我的應用程式", 
                "雙擊圖示，秀出應用程式",
                ToolTipIcon.Info
                );
        }
    }
}
