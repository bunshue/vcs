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
namespace 得到本机MAC地址
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
          ManagementObjectSearcher nisc = new ManagementObjectSearcher("select * from Win32_NetworkAdapterConfiguration");
          foreach(ManagementObject   nic   in   nisc.Get())   
          {   
            if(Convert.ToBoolean(nic["ipEnabled"])   ==   true)   
            {
                this.label2.Text=Convert.ToString(nic["MACAddress"]);
            
            }   
          }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.Exit();
        }
    }
}