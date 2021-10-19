using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Process

using Microsoft.Win32;  //for Registry
namespace tree
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

        //獲取程序安裝目錄
        private void button1_Click(object sender, EventArgs e)
        {
            //var notepadPath = GetPath("Notepad++");
            var notepadPath = GetPath("Microsoft");
            richTextBox1.Text += "程序名稱：Notepad++ \n 安裝目錄:" + notepadPath + "\n";

            GetAllProcess();
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
        public void GetAllProcess()
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

        private void button2_Click(object sender, EventArgs e)
        {
            //TBD

            //C#中利用process類調用外部程序以及執行dos命令
            //string result = RunCmd("cmd");
            //richTextBox1.Text += result + "\n";

        }

        /*
        C#中的Process類可方便的調用外部程序，所以我們可以通過調用cmd.exe程序

        加入參數 "/c " 要執行的命令來執行一個DOS命令

        （/c代表執行參數指定的命令後關閉cmd.exe /k參數則不關閉cmd.exe）
        */

        private string RunCmd(string command)
        {
            //實例一個Process類，啟動一個獨立進程
            Process p = new Process();

            //Process類有一個StartInfo屬性，這個是ProcessStartInfo類，包括了一些屬性和方法，下面我們用到了他的幾個屬性：

            p.StartInfo.FileName = "cmd.exe"; //設定程序名
            //p.StartInfo.Arguments = "/c " command; //設定程式執行參數
            p.StartInfo.UseShellExecute = false; //關閉Shell的使用
            p.StartInfo.RedirectStandardInput = true; //重定向標準輸入
            p.StartInfo.RedirectStandardOutput = true; //重定向標準輸出
            p.StartInfo.RedirectStandardError = true; //重定向錯誤輸出
            p.StartInfo.CreateNoWindow = true; //設置不顯示窗口

            p.Start(); //啟動

            //p.StandardInput.WriteLine(command); //也可以用這種方式輸入要執行的命令
            //p.StandardInput.WriteLine("exit"); //不過要記得加上Exit要不然下一行程式執行的時候會當機
            return p.StandardOutput.ReadToEnd(); //從輸出流取得命令執行結果
        }
    }
}


