using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;
namespace 遠程服務控制
{
    public partial class Form1 : Form
    {
        private string strPath;
        private ManagementClass managementClass;
        public Form1()
        {
            InitializeComponent();
        }
        // 驗證是否能連接到遠程計算機
　　　　public static bool ConnectValidate(string host,string userName,string password)
　　　　 { 
            ConnectionOptions connectionOptions = new ConnectionOptions();
            ManagementScope managementScope=new ManagementScope();
            try
　　　　　　　{
　　　　　　　    connectionOptions.Username = userName;
　　　　　　　    connectionOptions.Password = password;
　　　　　　　    managementScope = new ManagementScope( "\\\\" +host+ "\\root\\cimv2",connectionOptions) ;
　　　　　　　　  managementScope.Connect();
　　　　　　　}
　　　　　　　catch
　　　　　　　{
　　　　　　　}
　　　　　　　return managementScope.IsConnected;
　　　　 }
        //建立遠程連接
        public void ServiceManager(string host, string userName, string password)
        {
            this.strPath = "\\\\" + host + "\\root\\cimv2:Win32_Service";
            this.managementClass = new ManagementClass(strPath);
            if (userName != null && userName.Length > 0)
            {
                ConnectionOptions connectionOptions = new ConnectionOptions();
                connectionOptions.Username = userName;
                connectionOptions.Password = password;
                ManagementScope managementScope = new ManagementScope("\\\\" + host + "\\root\\cimv2", connectionOptions);
                this.managementClass.Scope = managementScope;
            }
        } 
　　　　// 取得所連接的計算機的所有服務數據
　　　　public string [,] GetServiceList()
　　　　 {
　　　　　　　string [,] services = new string [this.managementClass.GetInstances().Count,4];
　　　　　　　int i = 0;
　　　　　　　foreach(ManagementObject mo in this.managementClass.GetInstances())
　　　　　　　{
　　　　　　　　　 services[i,0] = (string)mo["Name"];
　　　　　　　　　 services[i,1] = (string)mo["DisplayName"];
　　　　　　　　　 services[i,2] = (string)mo["State"];
　　　　　　　　　 services[i,3] = (string)mo["StartMode"];
　　　　　　　　　 i++;
　　　　　　　}
　　　　　　　return services;
　　　　 }
　　　　// 開啟指定的服務
　　　　public string StartService(string serviceName)
　　　　 {
　　　　　　　string strRst = null;
　　　　　　　ManagementObject mo = this.managementClass.CreateInstance();
　　　　　　　mo.Path = new ManagementPath(this.strPath+".Name=\""+serviceName+"\"");
　　　　　　　try
　　　　　　　{
　　　　　　　　　 if((string)mo["State"]=="Stopped")
　　　　　　　　　　　 mo.InvokeMethod("StartService",null);
　　　　　　　}
　　　　　　　catch(ManagementException e)
　　　　　　　{
　　　　　　　　　 strRst =e.Message; 
　　　　　　　}
　　　　　　　return strRst;
　　　　 }
　　　　// 停止指定的服務
        public string StopService(string serviceName)
            {
                string strRst = null;
                ManagementObject mo = this.managementClass.CreateInstance();
                mo.Path = new ManagementPath(this.strPath+".Name=\""+serviceName+"\"");
                try
                    {
                    //判斷是否可以停止
                        if((bool)mo["AcceptStop"])//(string)mo["State"]=="Running"
                        mo.InvokeMethod("StopService",null);
                    }
                catch(ManagementException e)
                    {
                        strRst =e.Message; 
                    }
                return strRst;
            }

        private void Form2_Load(object sender, EventArgs e)
        {
           
        }

        private void ShowInfo(string strip,string strnames,string strpwd)
        {
            this.listBox1.Items.Clear();
            this.listBox2.Items.Clear();
            if (ConnectValidate(strip, strnames, strpwd))
            {
                try
                {
                    ServiceManager(strip, strnames, strpwd);
                    string[,] strname = GetServiceList();
                    for (int i = 0; i < strname.Length; i++)
                    {
                        if (strname[i, 2] == "Running")
                        {
                            this.listBox1.Items.Add(strname[i, 0]);
                        }
                        else
                        {
                            this.listBox2.Items.Add(strname[i, 0]);
                        }
                    }
                }
                catch { }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            ShowInfo(this.textBox4.Text, this.textBox2.Text, this.textBox3.Text);
            this.button1.Enabled = true;
            this.button2.Enabled = true;
        }

        private void listBox1_Click(object sender, EventArgs e)
        {
            this.textBox1.Text = listBox1.Text;
            this.button2.Enabled = true;
            this.button1.Enabled = false;
        }

        private void listBox2_Click(object sender, EventArgs e)
        {
            this.textBox1.Text = listBox2.Text;
            this.button1.Enabled = true;
            this.button2.Enabled = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            StartService(this.textBox1.Text);
            MessageBox.Show("OK");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            StopService(this.textBox1.Text);
            MessageBox.Show("OK");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (ConnectValidate(this.textBox4.Text, this.textBox2.Text, this.textBox3.Text))
            {
                
                ShowInfo(this.textBox4.Text, this.textBox2.Text, this.textBox3.Text);
                this.groupBox3.Enabled = true;
                MessageBox.Show("連接成功！！！");

            }
            else
            {
                MessageBox.Show("連接失敗請重新輸入正確訊息！！！");
            }
            
        }

    }
}