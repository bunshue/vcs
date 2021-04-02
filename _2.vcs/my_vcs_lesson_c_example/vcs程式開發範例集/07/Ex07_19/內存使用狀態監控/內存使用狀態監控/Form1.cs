using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Microsoft.VisualBasic.Devices;

namespace 內存使用狀態監控
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Computer myComputer = new Computer();
            textBox1.Text = Convert.ToString(myComputer.Info.TotalPhysicalMemory / 1024 / 1024);
            textBox2.Text = Convert.ToString(myComputer.Info.AvailablePhysicalMemory / 1024 / 1024);
            textBox3.Text = Convert.ToString(myComputer.Info.TotalVirtualMemory / 1024 / 1024);
            textBox4.Text = Convert.ToString(myComputer.Info.AvailableVirtualMemory / 1024 / 1024);
            timer1.Interval = 100;
            Form1_Load(sender, e);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Start();
        }
    }
}