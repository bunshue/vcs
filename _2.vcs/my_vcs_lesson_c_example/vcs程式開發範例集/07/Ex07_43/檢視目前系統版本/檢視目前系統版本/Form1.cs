using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 檢視目前系統版本
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            OperatingSystem myOS = Environment.OSVersion;
            if (myOS.Version.Major == 5)
            {
                switch (myOS.Version.Minor)
                {
                    case 0:
                        textBox1.Text = "Windows 2000 " + myOS.ServicePack;
                        break;
                    case 1:
                        textBox1.Text = "Windows XP " + myOS.ServicePack;
                        break;
                    case 2:
                        textBox1.Text = "Windows Server 2003 " + " " + myOS.ServicePack;
                        break;
                    default:
                        textBox1.Text = myOS.ToString() + " " + myOS.ServicePack;
                        break;
                }
            }
            else
                textBox1.Text = myOS.VersionString + " " + myOS.ServicePack;
        }
    }
}