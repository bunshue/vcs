using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_NotifyIcon_ContextMenuStrip
{
    public partial class Form1 : Form
    {
        NotifyIcon notifyIcon1 = new NotifyIcon();
        ContextMenuStrip contextMenuStrip1 = new ContextMenuStrip();
        ToolStripMenuItem toolStripMenuItem1 = new ToolStripMenuItem();
        ToolStripMenuItem toolStripMenuItem2 = new ToolStripMenuItem();

        private Icon icon = new Icon(@"C:\_git\vcs\_2.vcs\______test_files\_material\ims.ico");

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            setup_notifyIcon_contextMenuStrip();

            this.WindowState = FormWindowState.Minimized;
            this.Visible = false;
            this.notifyIcon1.Visible = true;

            //系統托盤動態圖標閃爍圖標 ST
            string filename1 = @"C:\______test_files\_icon\唐.ico";
            string filename2 = @"C:\______test_files\_icon\時.ico";

            Thread t = new Thread(new ParameterizedThreadStart(delegate(object obj)
            {
                Icon icon1 = new Icon(filename1);
                Icon icon2 = new Icon(filename2);
                while (1 == 1)
                {
                    Thread.Sleep(400);
                    if (notifyIcon1.Icon == icon1)
                    {
                        notifyIcon1.Icon = icon2;
                    }
                    else
                    {
                        notifyIcon1.Icon = icon1;
                    }
                }
            }));
            t.Name = " --start tray thread";
            t.IsBackground = true;
            t.Priority = ThreadPriority.Lowest;
            t.Start(null);
            //系統托盤動態圖標閃爍圖標 SP
        }

        void setup_notifyIcon_contextMenuStrip()
        {
            toolStripMenuItem1.Text = "恢復";
            toolStripMenuItem1.Click += new EventHandler(toolStripMenuItem1_Click);

            toolStripMenuItem2.Text = "離開";
            toolStripMenuItem2.Click += new EventHandler(toolStripMenuItem2_Click);


            contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            toolStripMenuItem1,
            toolStripMenuItem2});

            //contextMenuStrip1.Items.Add("AAAAAA");    //不好用

            contextMenuStrip1.Visible = true;

            notifyIcon1.ContextMenuStrip = contextMenuStrip1;
            notifyIcon1.Text = "製作TrayIcon";    //設置系統托盤顯示文字
            notifyIcon1.Visible = true;
            notifyIcon1.Icon = icon;
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            this.Visible = true;
            this.WindowState = FormWindowState.Normal;
            //notifyIcon1.Visible = false;
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        int use_icon = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            //換一個icon

            string filename1 = @"C:\______test_files\_icon\唐.ico";
            string filename2 = @"C:\______test_files\_icon\時.ico";

            if (((use_icon++) % 2) == 0)
            {
                Icon icon1 = new Icon(filename1);
                notifyIcon1.Icon = icon1;
            }
            else
            {
                Icon icon2 = new Icon(filename2);
                notifyIcon1.Icon = icon2;

            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            //任務欄氣泡提示視窗

            //顯示
            this.notifyIcon1.Visible = true;
            this.notifyIcon1.ShowBalloonTip(1000, "当前时间：", DateTime.Now.ToLocalTime().ToString(), ToolTipIcon.Info);


            //關閉
            //this.notifyIcon1.Visible = false;
        }
    }
}

