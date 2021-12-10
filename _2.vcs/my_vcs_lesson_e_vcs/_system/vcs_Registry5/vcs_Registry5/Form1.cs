using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Process

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
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

        }

        private void button0_Click(object sender, EventArgs e)
        {
            //獲取安裝軟件和路徑，通過注冊表得到
            richTextBox1.Text += "AAAA\n";
            //獲取安裝軟件和路徑，通過注冊表得到
            using (RegistryKey key = Registry.LocalMachine.OpenSubKey(@"SoftwareMicrosoftWindowsCurrentVersionUninstall", false))
            {
                richTextBox1.Text += "BBBB\n";
                if (key != null)//判斷對象存在
                {
                    richTextBox1.Text += "CCCC\n";
                    foreach (string keyName in key.GetSubKeyNames())//遍歷子項名稱的字符串數組
                    {
                        using (RegistryKey key2 = key.OpenSubKey(keyName, false))//遍歷子項節點
                        {
                            if (key2 != null)
                            {
                                string softwareName = key2.GetValue("DisplayName", "").ToString();//獲取軟件名
                                string installLocation = key2.GetValue("InstallLocation", "").ToString();//獲取安裝路徑
                                richTextBox1.Text += "softwareName : " + softwareName + "\n";
                                richTextBox1.Text += "installLocation : " + installLocation + "\n";
                                if (!string.IsNullOrEmpty(installLocation))
                                {
                                    //將信息添加到ListView控件中
                                    ListViewItem item = new ListViewItem(softwareName);
                                    item.SubItems.Add(installLocation);
                                    //listView1.Items.Add(item);
                                    richTextBox1.Text += "get item : " + item + "\n";
                                }
                            }
                        }
                    }
                }
            }
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

        //獲取程序安裝目錄 ST
        private void button5_Click(object sender, EventArgs e)
        {
            //獲取程序安裝目錄
            //var notepadPath = GetPath("Notepad++");
            var notepadPath = GetPath("Microsoft");
            richTextBox1.Text += "程序名稱：Notepad++ \n 安裝目錄:" + notepadPath + "\n";

            GetAllProcess2();
        }


        /// <summary>
        /// 獲取單個程序的執行目錄
        /// </summary>
        /// <param name="processName"></param>
        /// <returns></returns>
        public static string GetPath(string processName)
        {
            var process = Process.GetProcessesByName(processName);

            var path = string.Empty;//程序路徑
            foreach (var p in process.Where(p => p.MainWindowHandle != IntPtr.Zero))
            {
                path = p.MainModule.FileName;
                break;
            }
            return path;
        }


        /// <summary>
        /// 獲取所有程序的安裝目錄
        /// </summary>
        public void GetAllProcess2()
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
                                    richTextBox1.Text += softwareName + "\t" + installLocation + "\n";
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
