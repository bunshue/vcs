using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Windows.Forms;
//using System.Threading;
using System.IO;  //for DriveInfo

namespace vcs_DetectUSBDrive
{
    /// 
    /// USB插拔監控類
    /// 

    public class CUSBMonitor
    {
        private delegate void SetTextCallback(string s);
        private List<string> _usbdiskList = new List<string>();
        private ListBox _listbox = null;
        private Form _form = null;

        public CUSBMonitor()
        {
            System.Timers.Timer timer = new System.Timers.Timer(1000);
            timer.Enabled = true;

            // 達到間隔時發生
            timer.Elapsed += new System.Timers.ElapsedEventHandler(TimerList);
            timer.AutoReset = false; // 僅在間隔第一次結束後引發一次          
        }

        public void FillData(Form form, Message m, ListBox listbox)
        {
            _listbox = listbox;
            _form = form;

            try
            {
                if (m.Msg == CWndProMsgConst.WM_DEVICECHANGE) // 系統硬件改變發出的系統消息
                {
                    switch (m.WParam.ToInt32())
                    {
                        case CWndProMsgConst.WM_DEVICECHANGE:
                            break;
                        //設備檢測結束，並且可以使用
                        case CWndProMsgConst.DBT_DEVICEARRIVAL:
                            {
                                ScanUSBDisk();
                                _listbox.Items.Clear();
                                foreach (string str in _usbdiskList)
                                {
                                    _listbox.Items.Add(str);
                                }
                            }
                            break;
                        // 設備卸載或者拔出
                        case CWndProMsgConst.DBT_DEVICEREMOVECOMPLETE:
                            {
                                ScanUSBDisk();
                                _listbox.Items.Clear();
                                foreach (string str in _usbdiskList)
                                {
                                    _listbox.Items.Add(str);
                                }
                            }
                            break;
                        default:
                            break;
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("當前盤不能正確識別，請重新嘗試！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        /// 

        /// 設置USB列表
        /// 

        void TimerList(object sender, System.Timers.ElapsedEventArgs e)
        {
            ScanUSBDisk();
            foreach (string str in _usbdiskList)
            {
                SetText(str);
            }
        }

        /// 

        /// 掃描USB設備
        /// 

        private void ScanUSBDisk()
        {
            _usbdiskList.Clear();
            DriveInfo[] drives = DriveInfo.GetDrives();

            foreach (DriveInfo drive in drives)
            {
                if ((drive.DriveType == DriveType.Removable) && !drive.Name.Substring(0, 1).Equals("A"))
                {
                    try
                    {
                        _usbdiskList.Add(drive.Name);
                    }
                    catch
                    {
                        MessageBox.Show("當前盤不能正確識別，請重新嘗試！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                }
            }
        }

        /// 

        /// 設置List列表
        /// 

        /// 名稱
        public void SetText(string text)
        {
            if (_listbox == null)
                return;

            if (this._listbox.InvokeRequired) // 調用方位於創建控件所在的線程以外的線程中
            {
                if (_listbox.Items.Contains(text))
                    return;

                SetTextCallback d = new SetTextCallback(SetText);
                _form.Invoke(d, new object[] { text });
            }
            else
            {
                if (_listbox.Items.Contains(text))
                    return;

                this._listbox.Items.Add(text);
            }
        }
    }

    /// 

    /// windows消息常量
    /// 

    class CWndProMsgConst
    {
        public const int WM_DEVICECHANGE = 0x219; // 系統硬件改變發出的系統消息
        public const int DBT_DEVICEARRIVAL = 0x8000;// 設備檢測結束，並且可以使用
        public const int DBT_CONFIGCHANGECANCELED = 0x0019;
        public const int DBT_CONFIGCHANGED = 0x0018;
        public const int DBT_CUSTOMEVENT = 0x8006;
        public const int DBT_DEVICEQUERYREMOVE = 0x8001;
        public const int DBT_DEVICEQUERYREMOVEFAILED = 0x8002;
        public const int DBT_DEVICEREMOVECOMPLETE = 0x8004;// 設備卸載或者拔出
        public const int DBT_DEVICEREMOVEPENDING = 0x8003;
        public const int DBT_DEVICETYPEHANGED = 0x0007;
        public const int DBT_QUERYCHANGSPECIFIC = 0x8005;
        public const int DBT_DEVNODES_CECONFIG = 0x0017;
        public const int DBT_USERDEFINED = 0xFFFF;
    }
}
