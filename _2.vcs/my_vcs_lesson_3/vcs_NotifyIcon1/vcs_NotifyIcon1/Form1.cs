using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_NotifyIcon1
{
    public partial class Form1 : Form
    {
        private Icon icon = new Icon(@"C:\_git\vcs\_2.vcs\______test_files\_material\ims.ico");
        private NotifyIcon notifyIcon1;
        private ContextMenuStrip contextMenuStrip1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            contextMenuStrip1 = new ContextMenuStrip();
            contextMenuStrip1.Items.Add("AAAAAA");
            contextMenuStrip1.Visible = true;

            notifyIcon1 = new NotifyIcon();
            notifyIcon1.ContextMenuStrip = contextMenuStrip1;
            notifyIcon1.Text = "製作TrayIcon";    //設置系統托盤顯示文字
            notifyIcon1.Visible = true;


            //製作閃爍圖標 ST
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
            //製作閃爍圖標 SP
        }
    }
}

