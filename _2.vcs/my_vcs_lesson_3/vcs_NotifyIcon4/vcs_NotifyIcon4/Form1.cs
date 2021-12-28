using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_NotifyIcon4
{
    public partial class Form1 : Form
    {
        NotifyIcon notifyIcon1 = new NotifyIcon();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename1 = @"C:\______test_files\_icon\唐.ico";
            string filename2 = @"C:\______test_files\_icon\時.ico";

            notifyIcon1.Icon = new System.Drawing.Icon(filename1);
            notifyIcon1.Icon = new System.Drawing.Icon(filename2);
            //设置鼠标放在托盘图标上面的文字
            notifyIcon1.Text = "心语托盘图标";
            notifyIcon1.Visible = true;

            Thread t = new Thread(new ParameterizedThreadStart(delegate(object obj)
            {
                Icon icon1 = new System.Drawing.Icon(filename1);
                Icon icon2 = new System.Drawing.Icon(filename2);
                while (1 == 1)
                {

                    Thread.Sleep(400);
                    if (notifyIcon1.Icon == (icon1))
                        notifyIcon1.Icon = icon2;
                    else
                        notifyIcon1.Icon = icon1;
                }
            }));
            t.Name = " --start tray thread";
            t.IsBackground = true;
            t.Priority = ThreadPriority.Lowest;
            t.Start(null);
        }
    }
}
