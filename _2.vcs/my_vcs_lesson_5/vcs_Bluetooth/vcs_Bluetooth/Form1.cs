using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;
using System.Runtime.InteropServices;

namespace vcs_Bluetooth
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

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Size = new Size(610, 690);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1070, 750);
            this.Text = "vcs_Bluetooth";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "查詢藍芽裝置, 使用 WMI 查詢 PNP 裝置\n";

            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_PnPEntity WHERE Name LIKE '%Bluetooth%'");

            int count = 0;
            foreach (ManagementObject obj in searcher.Get())
            {
                richTextBox1.Text += "全部 :\n" + obj.GetText(TextFormat.Mof) + "\n";  // 全部

                string name = obj["Name"] != null ? obj["Name"].ToString() : "(未知名稱)";
                string deviceId = obj["DeviceID"] != null ? obj["DeviceID"].ToString() : "(未知ID)";

                richTextBox1.Text += "名稱: " + name + "\n";
                richTextBox1.Text += "ID: " + deviceId + "\n";
                richTextBox1.Text += "Caption: " + obj["Caption"] + "\n";
                richTextBox1.Text += "Description: " + obj["Description"] + "\n";
                richTextBox1.Text += "Name: " + obj["Name"] + "\n";
                richTextBox1.Text += "DeviceID: " + obj["DeviceID"] + "\n";
                richTextBox1.Text += "HardwareID: " + obj["HardwareID"] + "\n";
                richTextBox1.Text += "PNPDeviceID: " + obj["PNPDeviceID"] + "\n";
                richTextBox1.Text += "ClassGuid: " + obj["ClassGuid".ToString()] + "\n";
                richTextBox1.Text += "Manufacturer: " + obj["Manufacturer".ToString()] + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個
                count++;
            }
            richTextBox1.Text += "找到的藍芽裝置數量: " + count + "\n";
        }

        //------------------------------------------------------------  # 60個

        // 常數
        private const int DIGCF_PRESENT = 0x00000002;
        private const int DIGCF_ALLCLASSES = 0x00000004;

        // 結構
        [StructLayout(LayoutKind.Sequential)]
        private struct SP_DEVINFO_DATA
        {
            public int cbSize;
            public Guid ClassGuid;
            public int DevInst;
            public IntPtr Reserved;
        }

        // P/Invoke 宣告
        [DllImport("setupapi.dll", CharSet = CharSet.Auto)]
        private static extern IntPtr SetupDiGetClassDevs(
            IntPtr ClassGuid,
            IntPtr Enumerator,
            IntPtr hwndParent,
            int Flags);

        [DllImport("setupapi.dll", CharSet = CharSet.Auto)]
        private static extern bool SetupDiEnumDeviceInfo(
            IntPtr DeviceInfoSet,
            int MemberIndex,
            ref SP_DEVINFO_DATA DeviceInfoData);

        [DllImport("setupapi.dll", CharSet = CharSet.Auto)]
        private static extern bool SetupDiGetDeviceRegistryProperty(
            IntPtr DeviceInfoSet,
            ref SP_DEVINFO_DATA DeviceInfoData,
            int Property,
            out int PropertyRegDataType,
            byte[] PropertyBuffer,
            int PropertyBufferSize,
            out int RequiredSize);

        [DllImport("setupapi.dll")]
        private static extern bool SetupDiDestroyDeviceInfoList(IntPtr DeviceInfoSet);

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "查詢藍芽裝置, 使用 SetupDi API 方法\n";

            IntPtr hDevInfo = SetupDiGetClassDevs(IntPtr.Zero, IntPtr.Zero, IntPtr.Zero, DIGCF_PRESENT | DIGCF_ALLCLASSES);

            if (hDevInfo == IntPtr.Zero)
            {
                richTextBox1.Text += "無法取得裝置資訊。\n";
                return;
            }

            SP_DEVINFO_DATA devInfoData = new SP_DEVINFO_DATA();
            devInfoData.cbSize = Marshal.SizeOf(devInfoData);

            int index = 0;
            int count = 0;

            while (SetupDiEnumDeviceInfo(hDevInfo, index, ref devInfoData))
            {
                index++;

                const int SPDRP_DEVICEDESC = 0x00000000;  // 取得裝置名稱
                int regType;
                byte[] buffer = new byte[1024];
                int requiredSize;

                if (SetupDiGetDeviceRegistryProperty(hDevInfo, ref devInfoData, SPDRP_DEVICEDESC, out regType, buffer, buffer.Length, out requiredSize))
                {
                    string deviceName = Encoding.Unicode.GetString(buffer, 0, requiredSize - 2);

                    if (deviceName.Contains("Bluetooth"))
                    {
                        richTextBox1.Text += "裝置: " + deviceName + "\n";
                        count++;
                    }
                }
            }

            SetupDiDestroyDeviceInfoList(hDevInfo);

            richTextBox1.Text += "\n找到的藍芽裝置數量: " + count + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "查詢藍芽裝置, 含 HID/Audio\n";

            IntPtr hDevInfo = SetupDiGetClassDevs(IntPtr.Zero, IntPtr.Zero, IntPtr.Zero, DIGCF_PRESENT | DIGCF_ALLCLASSES);

            if (hDevInfo == IntPtr.Zero)
            {
                richTextBox1.Text += "無法取得裝置資訊。";
                return;
            }

            SP_DEVINFO_DATA devInfoData = new SP_DEVINFO_DATA();
            devInfoData.cbSize = Marshal.SizeOf(devInfoData);

            int index = 0;
            int count = 0;

            while (SetupDiEnumDeviceInfo(hDevInfo, index, ref devInfoData))
            {
                index++;

                const int SPDRP_DEVICEDESC = 0x00000000;  // 取得裝置名稱
                const int SPDRP_HARDWAREID = 0x00000001;  // 取得硬體 ID（通常藍芽裝置會包含 BTH 字樣）

                int regType;
                byte[] buffer = new byte[1024];
                int requiredSize;

                string deviceName = "";
                string hardwareId = "";

                // 取得裝置名稱
                if (SetupDiGetDeviceRegistryProperty(hDevInfo, ref devInfoData, SPDRP_DEVICEDESC, out regType, buffer, buffer.Length, out requiredSize))
                {
                    deviceName = Encoding.Unicode.GetString(buffer, 0, requiredSize - 2);
                }

                // 取得硬體 ID
                if (SetupDiGetDeviceRegistryProperty(hDevInfo, ref devInfoData, SPDRP_HARDWAREID, out regType, buffer, buffer.Length, out requiredSize))
                {
                    hardwareId = Encoding.Unicode.GetString(buffer, 0, requiredSize - 2);
                }

                // 判斷是否為藍芽裝置 (名稱或硬體 ID 包含 Bluetooth)
                if (!string.IsNullOrEmpty(deviceName) && (deviceName.Contains("Bluetooth") || hardwareId.Contains("BTH")))
                {
                    richTextBox1.Text += "裝置名稱: " + deviceName + "\n";
                    richTextBox1.Text += "硬體ID: " + hardwareId + "\n";
                    richTextBox1.Text += "------------------------------\n";  // 30個
                    count++;
                }
            }

            SetupDiDestroyDeviceInfoList(hDevInfo);

            richTextBox1.Text += "\n找到的藍芽相關裝置數量: " + count + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


/*
差異與效果
WMI 方法：		    只能抓到部分藍芽裝置（通常是控制器）。
SetupDi API 方法：	能列出所有裝置，包含 HID、音訊、驅動程式等，只要名稱裡有「Bluetooth」就會顯示。
這樣就能更接近裝置管理員顯示的數量。

*/

