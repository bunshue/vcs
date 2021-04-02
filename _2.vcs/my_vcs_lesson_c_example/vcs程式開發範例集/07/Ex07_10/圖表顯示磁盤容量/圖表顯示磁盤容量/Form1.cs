using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Management;
using System.IO;

namespace 圖表顯示磁盤容量
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject disk in searcher.Get())
            {
                comboBox1.Items.Add(disk["Name"].ToString());
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DriveInfo dinfo = new DriveInfo(comboBox1.Text);
            float tsize = dinfo.TotalSize;
            float fsize = dinfo.TotalFreeSpace;
            Graphics graphics = this.CreateGraphics();
            graphics.Clear(Color.White);
            Pen pen1 = new Pen(Color.Red);
            Brush brush1 = new SolidBrush(Color.WhiteSmoke);
            Brush brush2 = new SolidBrush(Color.LimeGreen);
            Brush brush3 = new SolidBrush(Color.RoyalBlue);
            Font font1 = new Font("Courier New", 16, FontStyle.Bold);
            Font font2 = new Font("細明體", 9);
            graphics.DrawString("磁盤容量分析", font1, brush2, new Point(60, 50));
            float angle1 = Convert.ToSingle((360 * (Convert.ToSingle(fsize / 100000000000) / Convert.ToSingle(tsize / 100000000000))));
            float angle2 = Convert.ToSingle((360 * (Convert.ToSingle((tsize - fsize) / 100000000000) / Convert.ToSingle(tsize / 100000000000))));
            graphics.FillPie(brush2, 60, 80, 150, 150, 0, angle1);
            graphics.FillPie(brush3, 60, 80, 150, 150, angle1, angle2);
            graphics.DrawRectangle(pen1, 30, 235, 200, 50);
            graphics.FillRectangle(brush2, 35, 245, 20, 10);
            graphics.DrawString("磁盤剩餘容量:" + dinfo.TotalFreeSpace / 1000 + "KB", font2, brush2, 55, 245);
            graphics.FillRectangle(brush3, 35, 265, 20, 10);
            graphics.DrawString("磁盤已用容量:" + (dinfo.TotalSize - dinfo.TotalFreeSpace) / 1000 + "KB", font2, brush3, 55, 265);
        }
    }
}