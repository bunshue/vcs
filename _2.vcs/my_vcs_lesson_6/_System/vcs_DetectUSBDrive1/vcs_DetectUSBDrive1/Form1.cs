using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //DriveInfo

namespace vcs_DetectUSBDrive1
{
    //[C#]偵測是否有卸除式存放裝置插入，使用 WndProc 方法與 DriveInfo 類別
    /*
    WndProc 用來處理 Windows 訊息。在這裡，我們使用到三個訊息
    WM_DEVICECHANGE Message : 電腦硬體裝置改變時產生的訊息
    DBT_DEVICEARRIVAL Event : 裝置插入並且可以使用時，產生的系統訊息
    DBT_DEVICEREMOVECOMPLETE Event : 裝置卸載或移除時產生的系統訊息
    */

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        protected override void WndProc(ref Message m)
        {
            const int WM_DEVICECHANGE = 0x219;
            const int DBT_DEVICEARRIVAL = 0x8000;
            const int DBT_DEVICEREMOVECOMPLETE = 0x8004;

            object ojb = new object();
            try
            {
                if (m.Msg == WM_DEVICECHANGE)       //電腦硬體裝置改變時產生的訊息
                {
                    switch (m.WParam.ToInt32())
                    {
                        case WM_DEVICECHANGE:
                            richTextBox1.Text += "WM_DEVICECHANGE\n";
                            break;
                        case DBT_DEVICEARRIVAL:     //裝置插入並且可以使用時，產生的系統訊息
                            richTextBox1.Text += "DBT_DEVICEARRIVAL\t\t裝置插入並且可以使用\n";
                            DeviceChange();
                            break;
                        case DBT_DEVICEREMOVECOMPLETE:      //裝置卸載或移除時產生的系統訊息
                            richTextBox1.Text += "DBT_DEVICEREMOVECOMPLETE\t\t裝置卸載或移除\n";
                            DeviceChange();
                            break;
                        default:
                            break;
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            base.WndProc(ref m);
        }

        private void DeviceChange()
        {
            foreach (DriveInfo di in DriveInfo.GetDrives())
            {
                if (di.DriveType == DriveType.Removable)
                {
                    richTextBox1.Text += "偵測到  " + di.Name + "  抽取式存放裝置\n";
                }
            }
        }
    }
}

