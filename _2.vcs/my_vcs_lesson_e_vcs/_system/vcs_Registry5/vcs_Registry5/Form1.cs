using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//C#實現在注冊表中保存信息
//最近做的項目需要在注冊表中記錄一些用戶設置，方便在程序下次啟動時讀取設置，應用上次用戶保存的設置，挺簡單的。

using Microsoft.Win32;  //for Registry

namespace vcs_Registry5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 存值
            RegistryStorage.SaveBeforeExit(PageVisibility.Hide);
            // 取值
            PageVisibility visibility = RegistryStorage.OpenAfterStart();



            // 存值
            RegistryStorage.SaveBeforeExit(PageVisibility.Visible);
            // 取值
            visibility = RegistryStorage.OpenAfterStart();



        }

        private void button2_Click(object sender, EventArgs e)
        {
            //獲取所有程序的安裝目錄
            GetAllProcess();
        }

        /// <summary>
        /// 獲取所有程序的安裝目錄
        /// </summary>
        public static void GetAllProcess()
        {
            const string Uninstall = @"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall";
            using (var registryKey = Registry.LocalMachine.OpenSubKey(Uninstall, false))
            {
                if (registryKey != null)//判斷對象存在
                {
                    foreach (var keyName in registryKey.GetSubKeyNames())//遍歷子項名稱的字符串數組
                    {
                        using (var key = registryKey.OpenSubKey(keyName, false))//遍歷子項節點
                        {
                            if (key != null)
                            {
                                var softwareName = key.GetValue("DisplayName", "").ToString();//獲取軟件名
                                var installLocation = key.GetValue("InstallLocation", "").ToString();//獲取安裝路徑

                                if (!string.IsNullOrEmpty(installLocation))
                                {
                                    Console.WriteLine(softwareName);
                                    Console.WriteLine(installLocation);
                                    Console.WriteLine();
                                }
                            }
                        }
                    }
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //獲取網關和IP
            getxx();
            richTextBox1.Text += "獲取網關和IP\n";
        }


        //獲取網關和IP
        private void getxx()
        {
            RegistryKey start = Registry.LocalMachine;
            RegistryKey cardServiceName, networkKey;
            string networkcardKey = @"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkCards";
            string serviceKey = @"SYSTEM\CurrentControlSet\Services\";
            string networkcardKeyName, deviceName;
            string deviceServiceName, serviceName;
            RegistryKey serviceNames = start.OpenSubKey(networkcardKey);
            if (serviceNames == null)
            {
                MessageBox.Show("Bad registry key");
                return;
            }
            string[] networkCards = serviceNames.GetSubKeyNames();
            serviceNames.Close();
            foreach (string keyName in networkCards)
            {
                networkcardKeyName = networkcardKey + "\\" + keyName;
                cardServiceName = start.OpenSubKey(networkcardKeyName);
                if (cardServiceName == null)
                {
                    MessageBox.Show(networkcardKeyName);
                    return;
                }
                deviceServiceName = (string)cardServiceName.GetValue("ServiceName");
                deviceName = (string)cardServiceName.GetValue("Description");
                MessageBox.Show(deviceName);
                serviceName = serviceKey + deviceServiceName + "\\Parameters\\Tcpip";
                networkKey = start.OpenSubKey(serviceName);
                if (networkKey == null)
                {
                    //。。。。。。
                }
                else
                {
                    string[] ipaddresses = (string[])networkKey.GetValue("IPAddress");
                    string[] defaultGateways = (string[])networkKey.GetValue("DefaultGateway");

                    string[] subnetmasks = (string[])networkKey.GetValue("SubnetMask");
                    foreach (string ipaddress in ipaddresses)
                    {
                        MessageBox.Show(ipaddress);
                    }
                    foreach (string subnetmask in subnetmasks)
                    {
                        //。。。。。。
                    }
                    foreach (string defaultGateway in defaultGateways)
                    {
                        MessageBox.Show(defaultGateway);
                    }
                    networkKey.Close();
                }
            }
            start.Close();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //ReadRegistryKey
            //用C#去讀取特定位置的Refistry Key
            string result = ReadRegistryKey("Software\\AIMTest"); //直接給string的Registry路徑即可
            richTextBox1.Text += "result : \t" + result + "\n";
        }

        public string ReadRegistryKey(string RegKey)
        {
            //讀取Registry Key位置

            RegistryKey RegK = Registry.LocalMachine.OpenSubKey(RegKey);
            //讀取Registry Key String"test"裡面的值
            string RegT = (string)RegK.GetValue("test");
            //Show Registry Key值，檢查讀取的值是否正確
            MessageBox.Show(RegT);
            return RegT;
        }
    }

    public class RegistryStorage
    {
        public static PageVisibility OpenAfterStart()
        {
            Microsoft.Win32.RegistryKey registryKey;
            PageVisibility visibility = PageVisibility.Visible;

            // HKCU\Software\RegeditStorage
            registryKey = Microsoft.Win32.Registry.CurrentUser.OpenSubKey(@"Software\RegistryStorage");
            if (registryKey != null)
            {
                visibility = (string)registryKey.GetValue("PageVisibility") == PageVisibility.Hide.ToString() ?
                    PageVisibility.Hide : PageVisibility.Visible;
                registryKey.Close();
            }

            return visibility;
        }

        public static void SaveBeforeExit(PageVisibility visibility)
        {
            Microsoft.Win32.RegistryKey registryKey;

            // HKCU\Software\RegeditStorage
            registryKey = Microsoft.Win32.Registry.CurrentUser.CreateSubKey(@"Software\RegistryStorage");
            registryKey.SetValue("PageVisibility", visibility.ToString());
            registryKey.Close();
        }
    }

    public enum PageVisibility
    {
        Visible,
        Hide
    }
}
