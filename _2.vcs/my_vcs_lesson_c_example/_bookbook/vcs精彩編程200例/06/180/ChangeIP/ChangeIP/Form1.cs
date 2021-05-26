using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Management;

namespace ChangeIP
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ShowInfo();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ManagementBaseObject myInMBO = null;
            ManagementBaseObject myOutMBO = null;
            ManagementClass myMClass = new ManagementClass("Win32_NetworkAdapterConfiguration");
            ManagementObjectCollection myMOCollection = myMClass.GetInstances();
            foreach (ManagementObject MObject in myMOCollection)
            {
                if (!(bool)MObject["IPEnabled"])    //判断网络连接是否可用
                    continue;
                //设置ip地址和子网掩码
                myInMBO = MObject.GetMethodParameters("EnableStatic");
                myInMBO["IPAddress"] = new string[] { textBox1.Text };
                myInMBO["SubnetMask"] = new string[] { textBox2.Text };
                myOutMBO = MObject.InvokeMethod("EnableStatic", myInMBO, null);
                //设置网关地址 
                myInMBO = MObject.GetMethodParameters("SetGateways");
                myInMBO["DefaultIPGateway"] = new string[] { textBox3.Text };
                myOutMBO = MObject.InvokeMethod("SetGateways", myInMBO, null);
                //设置DNS 
                myInMBO = MObject.GetMethodParameters("SetDNSServerSearchOrder");
                myInMBO["DNSServerSearchOrder"] = new string[] { textBox4.Text, textBox5.Text };
                myOutMBO = MObject.InvokeMethod("SetDNSServerSearchOrder", myInMBO, null);
                break;
            }
            ShowInfo();
            MessageBox.Show("IP地址设置成功!");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        #region 显示本地连接信息
        /// <summary>
        /// 显示本地连接信息
        /// </summary>
        public void ShowInfo()
        {
            ManagementClass myMClass = new ManagementClass("Win32_NetworkAdapterConfiguration");
            ManagementObjectCollection myMOCollection = myMClass.GetInstances();
            foreach (ManagementObject MObject in myMOCollection)
            {
                if (!(bool)MObject["IPEnabled"])
                    continue;
                string[] strIP = (string[])MObject["IPAddress"];            //获取IP地址
                string[] strSubnet = (string[])MObject["IPSubnet"];         //获取子网掩码
                string[] strGateway = (string[])MObject["DefaultIPGateway"];//获取默认网关
                string[] strDns = (string[])MObject["DNSServerSearchOrder"];//获取DNS服务器
                textBox1.Text = "";
                //显示IP地址
                foreach (string ip in strIP)
                {
                    if (textBox1.Text.Trim() != "")
                    {
                        textBox1.Text += "," + ip;
                    }
                    else
                    {
                        textBox1.Text = ip;
                    }
                }
                textBox2.Text = "";
                //显示子网掩码
                foreach (string subnet in strSubnet)
                {
                    if (textBox2.Text.Trim() != "")
                    {
                        textBox2.Text += "," + subnet;
                    }
                    else
                    {
                        textBox2.Text = subnet;
                    }
                }
                textBox3.Text = "";
                //显示默认网关
                foreach (string gateway in strGateway)
                {
                    if (textBox3.Text.Trim() != "")
                    {
                        textBox3.Text += "," + gateway;
                    }
                    else
                    {
                        textBox3.Text = gateway;
                    }
                }
                try
                {
                    //显示DNS服务器
                    for (int i = 0; i < strDns.Length; i++)
                    {
                        if (i == 0)
                            textBox4.Text = strDns[i];
                        else
                            textBox5.Text = strDns[i];
                    }
                }
                catch { }
            }
        }
        #endregion
    }
}
