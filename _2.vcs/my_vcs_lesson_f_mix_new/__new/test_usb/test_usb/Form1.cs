using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Runtime.InteropServices;

using System.Windows;   //for PresentationSource 需 參考/加入參考/.NET/PresentationCore
using System.Windows.Interop;   //for HwndSource

namespace test_usb
{
    public partial class Form1 : Form
    {
        string panfu = "";
                                    public const int WM_DEVICECHANGE = 0x219;//U盤插入後，OS的底層會自動檢測到，然後向應用程序發送“硬件設備狀態改變“的消息
                                    public const int DBT_DEVICEARRIVAL = 0x8000;  //就是用來表示U盤可用的。一個設備或媒體已被插入一塊，現在可用。
                                    public const int DBT_CONFIGCHANGECANCELED = 0x0019;  //要求更改當前的配置（或取消停靠碼頭）已被取消。
                                    public const int DBT_CONFIGCHANGED = 0x0018;  //當前的配置發生了變化，由於碼頭或取消固定。
                                    public const int DBT_CUSTOMEVENT = 0x8006; //自定義的事件發生。 的Windows NT 4.0和Windows 95：此值不支持。
                                    public const int DBT_DEVICEQUERYREMOVE = 0x8001;  //審批要求刪除一個設備或媒體作品。任何應用程序也不能否認這一要求，並取消刪除。
                                    public const int DBT_DEVICEQUERYREMOVEFAILED = 0x8002;  //請求刪除一個設備或媒體片已被取消。
                                    public const int DBT_DEVICEREMOVECOMPLETE = 0x8004;  //一個設備或媒體片已被刪除。
                                    public const int DBT_DEVICEREMOVEPENDING = 0x8003;  //一個設備或媒體一塊即將被刪除。不能否認的。
                                    public const int DBT_DEVICETYPESPECIFIC = 0x8005;  //一個設備特定事件發生。
                                    public const int DBT_DEVNODES_CHANGED = 0x0007;  //一種設備已被添加到或從系統中刪除。
                                    public const int DBT_QUERYCHANGECONFIG = 0x0017;  //許可是要求改變目前的配置（碼頭或取消固定）。
                                    public const int DBT_USERDEFINED = 0xFFFF;  //此消息的含義是用戶定義的
                                    public const uint GENERIC_READ = 0x80000000;
                                    public const int GENERIC_WRITE = 0x40000000;
                                    public const int FILE_SHARE_READ = 0x1;
                                    public const int FILE_SHARE_WRITE = 0x2;
                                    public const int IOCTL_STORAGE_EJECT_MEDIA = 0x2d4808;

                                                        private IntPtr WndProc(IntPtr hwnd, int msg, IntPtr wParam, IntPtr lParam, ref bool handled)
                                                        {
                                                            if (msg == WM_DEVICECHANGE)
                                                            {
                                                                switch (wParam.ToInt32())
                                                                {
                                                                    case DBT_DEVICEARRIVAL:
                                                                        DriveInfo[] s = DriveInfo.GetDrives();
                                                                        s.Any(t =>
                                                                        {
                                                                            if (t.DriveType == DriveType.Removable)
                                                                            {
                                                                                panfu = t.Name;
                                                                                MessageBox.Show("U盤插入,盤符為：" + t.Name);
                                                                                DirSearch(t.RootDirectory.FullName);
                                                                                return true;
                                                                            }
                                                                            return false;
                                                                        });
                                                                        break;
                                                                    case DBT_DEVICEREMOVECOMPLETE:
                                                                        MessageBox.Show("U盤卸載");
                                                                        break;
                                                                    default:
                                                                        break;
                                                                }
                                                            }
                                                            return IntPtr.Zero;
                                                        }

                                                        private void DirSearch(string path)
                                                        {
                                                            try
                                                            {
                                                                foreach (string f in Directory.GetFiles(path))
                                                                {
                                                                    listView1.Items.Add(f);
                                                                }
                                                                foreach (string d in Directory.GetDirectories(path))
                                                                {
                                                                    DirSearch(d);
                                                                }
                                                            }
                                                            catch (Exception)
                                                            {

                                                                throw;
                                                            }
                                                        }

        [DllImport("kernel32.dll", SetLastError = true, CharSet = CharSet.Auto)]
        private static extern IntPtr CreateFile(
         string lpFileName,
         uint dwDesireAccess,
         uint dwShareMode,
         IntPtr SecurityAttributes,
         uint dwCreationDisposition,
         uint dwFlagsAndAttributes,
         IntPtr hTemplateFile);

        [DllImport("kernel32.dll", ExactSpelling = true, SetLastError = true, CharSet = CharSet.Auto)]
        private static extern bool DeviceIoControl(
            IntPtr hDevice,
            uint dwIoControlCode,
            IntPtr lpInBuffer,
            uint nInBufferSize,
            IntPtr lpOutBuffer,
            uint nOutBufferSize,
            out uint lpBytesReturned,
            IntPtr lpOverlapped
        );

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            /*WPF中處理消息首先要獲取窗口句柄，創建HwndSource對象 通過HwndSource對象添加
 * 消息處理回調函數.HwndSource類: 實現其自己的窗口過程。 創建窗口之後使用 AddHook 
 * 和 RemoveHook 來添加和移除掛鉤，接收所有窗口消息。*/

            HwndSource hwndSource = PresentationSource.FromVisual(this) as HwndSource;//窗口過程
            if (hwndSource != null)
            {
                hwndSource.AddHook(new HwndSourceHook(WndProc));//掛鉤
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //第一個參數filename與普通文件名有所不同，設備驅動的“文件名”(常稱為“設備路徑”)形式固定為“\\.\DeviceName”, 如 string filename = @"\\.\I:";


            richTextBox1.Text += "panfu = " + panfu + "\n";
            return;

            string filename = @"\\.\" + panfu.Remove(2);
            //打開設備，得到設備的句柄handle.
            IntPtr handle = CreateFile(filename, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, IntPtr.Zero, 0x3, 0, IntPtr.Zero);

            // 向目標設備發送設備控制碼，也就是發送命令。IOCTL_STORAGE_EJECT_MEDIA  彈出U盤。
            uint byteReturned;
            bool result = DeviceIoControl(handle, IOCTL_STORAGE_EJECT_MEDIA, IntPtr.Zero, 0, IntPtr.Zero, 0, out byteReturned, IntPtr.Zero);

            MessageBox.Show(result ? "U盤已退出" : "U盤退出失敗");

        }



    }
}
