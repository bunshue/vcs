using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.ServiceProcess;//////
namespace DominateComputerService
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //下面的示例使用 ServiceController 類檢查警報器服務是否已停止。如果該服務已停止，此示例將啟動該服務並等待服務狀態設置為 Running。
            //此示例使用 ServiceController 組件在本地計算機上繼續 IIS 管理服務
            //serviceController1.MachineName = ".";
            //serviceController1.ServiceName = "IISAdmin";//Iis 服務
        }
        //開啟IIS服務的狀態
        private void button1_Click(object sender, EventArgs e)
        {
            serviceController1.MachineName = ".";
            serviceController1.ServiceName = "IISAdmin";//Iis 服務
             if (serviceController1.Status == ServiceControllerStatus.Running)
            {
                MessageBox.Show(serviceController1.DisplayName + "  服務正在運行");
                button2.Enabled = false;
                button3.Enabled = false;
                button1.Enabled = false;
                Application.Exit();
            }
            else
            {
                
                serviceController1.Start();
                MessageBox.Show(serviceController1.DisplayName + "  服務已開啟");
                button2.Enabled = false;
                button3.Enabled = false;
                button1.Enabled = false;
                Application.Exit();
            }

        }
        //判斷IIS服務的狀態
        private void button3_Click(object sender, EventArgs e)
        {
            try
            {
                serviceController1.MachineName = ".";
                serviceController1.ServiceName = "IISAdmin";//Iis 服務
                if (serviceController1.Status == ServiceControllerStatus.Running)
                {
                    MessageBox.Show(serviceController1.DisplayName + "  服務已開啟");
                    button2.Enabled = true;
                    button3.Enabled = false;
             
                }
                else
                {
                    MessageBox.Show(serviceController1.DisplayName + "服務已停止");
                    button3.Enabled = false;
                    button1.Enabled = true;
                 
                }
            }
            catch (Exception ee)
            { MessageBox.Show(ee.Message); }

        }
  
        //停止IIS服務的狀態
        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                serviceController1.MachineName = ".";
                serviceController1.ServiceName = "IISAdmin";//Iis 服務
                if (serviceController1.CanStop)
                {
                    serviceController1.Stop();
                    MessageBox.Show(serviceController1.DisplayName + "服務已停止");
                    button2.Enabled = false;
                    button3.Enabled = false;
                    button1.Enabled = false;
                    Application.Exit();
                 }
                else
                {
                    MessageBox.Show(serviceController1.DisplayName + "不可以停止");
                    button2.Enabled = false;
                    button3.Enabled = false;
                    button1.Enabled = false;
                    Application.Exit();
                 
                }
            }
            catch (Exception ee)
                { MessageBox.Show(ee.Message); }
       
        }
    }
}