using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Diagnostics;
using System.Management;

namespace CPU使用率
{
    public partial class Form1 : Form
    {
        Thread td;
        int mheight = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            CheckForIllegalCrossThreadCalls = false;
            myUser();
        }

        private void CreateImage()
        {
            int i = panel3.Height / 100;
            Bitmap image = new Bitmap(panel3.Width, panel3.Height);
            //建立Graphics類對像
            Graphics g = Graphics.FromImage(image);
            g.Clear(Color.Green);
            SolidBrush mybrush = new SolidBrush(Color.Lime);
            g.FillRectangle(mybrush, 0, panel3.Height - mheight * i, 26, mheight * i);
            panel3.BackgroundImage = image;
        }

        private void myUser()
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("select * from Win32_Processor");
            foreach (ManagementObject myobject in searcher.Get())
            {
                lblCPU.Text = myobject["LoadPercentage"].ToString() + " %";
                label2.Text = lblCPU.Text;
                mheight = Convert.ToInt32(myobject["LoadPercentage"].ToString());
                if (mheight == 100)
                    panel3.Height = 100;
                CreateImage();
            }
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            td = new Thread(new ThreadStart(myUser));
            td.Start();
        }

    }
}

