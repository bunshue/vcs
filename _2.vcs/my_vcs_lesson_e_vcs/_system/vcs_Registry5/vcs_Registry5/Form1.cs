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
