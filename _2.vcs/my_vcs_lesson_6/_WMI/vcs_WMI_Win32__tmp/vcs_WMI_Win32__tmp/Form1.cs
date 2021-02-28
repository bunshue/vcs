using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32__tmp
{
    public partial class Form1 : Form
    {
        class USBDeviceInfo
        {
            public USBDeviceInfo(string deviceID, string pnpDeviceID, string description)
            {
                this.DeviceID = deviceID;
                this.PnpDeviceID = pnpDeviceID;
                this.Description = description;
            }
            public string DeviceID { get; private set; }
            public string PnpDeviceID { get; private set; }
            public string Description { get; private set; }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n獲取主機板資訊\n";
            richTextBox1.Text += "\nWin32_BaseBoard\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "主機板製造商：" + mo["Manufacturer"].ToString() + "\n";
                richTextBox1.Text += "產品：" + mo["Product"].ToString() + "\n";
                richTextBox1.Text += "主機板序號：" + mo["SerialNumber"].ToString() + "\n";
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n取得本機的MAC\n";
            richTextBox1.Text += "\nWin32_NetworkAdapterConfiguration\n";   //網絡適配器設置
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if ((bool)mo["IPEnabled"] == true)
                {
                    richTextBox1.Text += "取得本機的MAC：" + mo["MacAddress"].ToString() + "\n";
                }

            }


        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n取得網卡地址\n";
            richTextBox1.Text += "\nWin32_NetworkAdapter\n";   //網絡適配器
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if ((bool)mo["IPEnabled"] == true)
                {
                    richTextBox1.Text += "取得網卡地址：" + mo["MacAddress"].ToString() + "\n";
                }

            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n獲取硬碟序號\n";
            richTextBox1.Text += "\nWin32_DiskDrive\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
            richTextBox1.Text += "硬碟個數：" + mos.Get().Count.ToString() + "\n";
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "硬碟 Model：" + mo["Model"].ToString() + "\n";
                richTextBox1.Text += "硬碟 DeviceID：" + mo["DeviceID"].ToString() + "\n";
                richTextBox1.Text += "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //fail
            richTextBox1.Text += "\n獲取IP位址\n";
            richTextBox1.Text += "\nWin32_NetworkAdapterConfiguration\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if ((bool)mo["IPEnabled"] == true)
                    richTextBox1.Text += "IP " + mo["IpAddress"] + "\n";
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n一些資訊\n";

            richTextBox1.Text += "\n顯卡PNPDeviceID\n";
            richTextBox1.Text += "\nWin32_VideoController\n";
            ManagementObjectSearcher mos1 = new ManagementObjectSearcher("SELECT * FROM Win32_VideoController");
            foreach (ManagementObject mo in mos1.Get())
            {
                richTextBox1.Text += "顯卡PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";
            }


            richTextBox1.Text += "\n聲卡PNPDeviceID\n";
            richTextBox1.Text += "\nWin32_SoundDevice\n";
            ManagementObjectSearcher mos2 = new ManagementObjectSearcher("SELECT * FROM Win32_SoundDevice");
            foreach (ManagementObject mo in mos2.Get())
            {
                richTextBox1.Text += "聲卡PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";
            }

            richTextBox1.Text += "\nCPU版本信息\n";
            richTextBox1.Text += "\nWin32_Processor\n";
            ManagementObjectSearcher mos3 = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos3.Get())
            {
                richTextBox1.Text += "CPU名稱：" + mo["Name"].ToString() + "\n";
                richTextBox1.Text += "CPU版本信息：" + mo["Version"].ToString() + "\n";
                richTextBox1.Text += "CPU製造廠商：" + mo["Manufacturer"].ToString() + "\n";
            }


        }

        private void button7_Click(object sender, EventArgs e)
        {
            //C#.Net 使用WMI取得網路卡資訊
            ManagementObjectSearcher search = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter");
            ManagementObjectCollection collection = search.Get();
            var networkList = from n in collection.Cast<ManagementBaseObject>()
                              select new
                              {
                                  guid = n.GetPropertyValue("GUID"),
                                  name = n.GetPropertyValue("Name"),
                                  mac = n.GetPropertyValue("MACAddress")

                              };
            foreach (var n in networkList)
                richTextBox1.Text += String.Format("{0}{2}{1}{2}{2}", n.name, n.mac, Environment.NewLine);


        }

        private void button10_Click(object sender, EventArgs e)
        {
            //C#.Net 使用WMI取得USB資訊 
            ManagementObjectSearcher search = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub");
            ManagementObjectCollection collection = search.Get();
            var usbList = from u in collection.Cast<ManagementBaseObject>()
                          select new
                          {
                              id = u.GetPropertyValue("DeviceID"),
                              name = u.GetPropertyValue("Name"),
                              status = u.GetPropertyValue("Status"),
                              system = u.GetPropertyValue("SystemName"),
                              caption = u.GetPropertyValue("Caption"),
                              pnp = u.GetPropertyValue("PNPDeviceID"),
                              description = u.GetPropertyValue("Description")
                          };
            foreach (var u in usbList)
            {
                richTextBox1.Text += String.Format("{0}{7}{1}{7}{2}{7}{3}{7}{4}{7}{5}{7}{6}{7}{7}{7}", u.id, u.name, u.status, u.system, u.caption, u.pnp, u.description, Environment.NewLine);
            }



        }

        private void button14_Click(object sender, EventArgs e)
        {
            //用WMI取出作業系統資訊1
            //用WMI取出作業系統資訊
            get_wmi_os_info();
        }

        void get_wmi_os_info()
        {
            // Get and display OS properties.
            ManagementObjectSearcher os_searcher = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem");

            foreach (ManagementObject mobj in os_searcher.Get())
            {
                GetValue(mobj, "BootDevice");
                GetValue(mobj, "BuildNumber");
                GetValue(mobj, "BuildType");
                GetValue(mobj, "Caption");
                GetValue(mobj, "CodeSet");
                GetValue(mobj, "CountryCode");
                GetValue(mobj, "CreationClassName");
                GetValue(mobj, "CSCreationClassName");
                GetValue(mobj, "CSDVersion");
                GetValue(mobj, "CSName");
                GetValue(mobj, "CurrentTimeZone");
                GetValue(mobj, "DataExecutionPrevention_Available");
                GetValue(mobj, "DataExecutionPrevention_32BitApplications");
                GetValue(mobj, "DataExecutionPrevention_Drivers");
                GetValue(mobj, "DataExecutionPrevention_SupportPolicy");
                GetValue(mobj, "Debug");
                GetValue(mobj, "Description");
                GetValue(mobj, "Distributed");
                GetValue(mobj, "EncryptionLevel");
                GetValue(mobj, "ForegroundApplicationBoost");
                GetValue(mobj, "FreePhysicalMemory");
                GetValue(mobj, "FreeSpaceInPagingFiles");
                GetValue(mobj, "FreeVirtualMemory");
                GetValue(mobj, "InstallDate");
                GetValue(mobj, "LargeSystemCache");
                GetValue(mobj, "LastBootUpTime");
                GetValue(mobj, "LocalDateTime");
                GetValue(mobj, "Locale");
                GetValue(mobj, "Manufacturer");
                GetValue(mobj, "MaxNumberOfProcesses");
                GetValue(mobj, "MaxProcessMemorySize");
                GetValue(mobj, "MUILanguages[]");
                GetValue(mobj, "Name");
                GetValue(mobj, "NumberOfLicensedUsers");
                GetValue(mobj, "NumberOfProcesses");
                GetValue(mobj, "NumberOfUsers");
                GetValue(mobj, "OperatingSystemSKU");
                GetValue(mobj, "Organization");
                GetValue(mobj, "OSArchitecture");
                GetValue(mobj, "OSLanguage");
                GetValue(mobj, "OSProductSuite");
                GetValue(mobj, "OSType");
                GetValue(mobj, "OtherTypeDescription");
                GetValue(mobj, "PAEEnabled");
                GetValue(mobj, "PlusProductID");
                GetValue(mobj, "PlusVersionNumber");
                GetValue(mobj, "Primary");
                GetValue(mobj, "ProductType");
                GetValue(mobj, "QuantumLength");
                GetValue(mobj, "QuantumType");
                GetValue(mobj, "RegisteredUser");
                GetValue(mobj, "SerialNumber");
                GetValue(mobj, "ServicePackMajorVersion");
                GetValue(mobj, "ServicePackMinorVersion");
                GetValue(mobj, "SizeStoredInPagingFiles");
                GetValue(mobj, "Status");
                GetValue(mobj, "SuiteMask");
                GetValue(mobj, "SystemDevice");
                GetValue(mobj, "SystemDirectory");
                GetValue(mobj, "SystemDrive");
                GetValue(mobj, "TotalSwapSpaceSize");
                GetValue(mobj, "TotalVirtualMemorySize");
                GetValue(mobj, "TotalVisibleMemorySize");
                GetValue(mobj, "Version");
                GetValue(mobj, "WindowsDirectory");
            }
        }

        // Get a value from the ManagementObject.
        private void GetValue(ManagementObject mobj, string property_name)
        {
            string value;
            try
            {
                value = mobj[property_name].ToString();
            }
            catch (Exception ex)
            {
                value = "*** Error: " + ex.Message;
            }
            richTextBox1.Text += property_name + "\t" + value + "\n";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //用WMI取出作業系統資訊2
            // Display the operating system's name.
            // Get the OS information.
            // For more information from this query, see:
            //      http://msdn.microsoft.com/library/aa394239.aspx
            string os_query = "SELECT * FROM Win32_OperatingSystem";
            ManagementObjectSearcher os_searcher = new ManagementObjectSearcher(os_query);
            foreach (ManagementObject info in os_searcher.Get())
            {
                //lblCaption.Text = info.Properties["Caption"].Value.ToString().Trim();
                //lblVersion.Text = "Version " + info.Properties["Version"].Value.ToString() + " SP " + info.Properties["ServicePackMajorVersion"].Value.ToString() + "." + info.Properties["ServicePackMinorVersion"].Value.ToString();

                richTextBox1.Text += info.Properties["Caption"].Value.ToString().Trim() + "\n";
                richTextBox1.Text += "Version " + info.Properties["Version"].Value.ToString() + " SP " + info.Properties["ServicePackMajorVersion"].Value.ToString() + "." + info.Properties["ServicePackMinorVersion"].Value.ToString() + "\n";
            }

            // Get number of processors.
            // For more information from this query, see:
            //      http://msdn.microsoft.com/library/aa394373.aspx
            string cpus_query = "SELECT * FROM Win32_ComputerSystem";
            ManagementObjectSearcher cpus_searcher = new ManagementObjectSearcher(cpus_query);
            foreach (ManagementObject info in cpus_searcher.Get())
            {
                //lblCpus.Text = info.Properties["NumberOfLogicalProcessors"].Value.ToString() + " processors";

                richTextBox1.Text += info.Properties["NumberOfLogicalProcessors"].Value.ToString() + " processors" + "\n";

            }

            // Get 32- versus 64-bit.
            // For more information from this query, see:
            //      http://msdn.microsoft.com/library/aa394373.aspx
            string proc_query = "SELECT * FROM Win32_Processor";
            ManagementObjectSearcher proc_searcher = new ManagementObjectSearcher(proc_query);
            foreach (ManagementObject info in proc_searcher.Get())
            {
                //lblBits.Text = info.Properties["AddressWidth"].Value.ToString() + "-bit";

                richTextBox1.Text += info.Properties["AddressWidth"].Value.ToString() + "-bit" + "\n";
            }



        }

        private void button16_Click(object sender, EventArgs e)
        {
            //WMI取得系統資訊
            richTextBox1.Text += "獲取CPU序號\t" + GetCPUSerialNumber() + "\n";
            richTextBox1.Text += "獲取主機板序號\t" + GetBIOSSerialNumber() + "\n";
            richTextBox1.Text += "獲取硬碟序號\t" + GetHardDiskSerialNumber() + "\n";
            richTextBox1.Text += "獲取網路卡位址\t" + GetNetCardMACAddress() + "\n";
        }

        //獲取CPU序號
        public string GetCPUSerialNumber()
        {
            try
            {
                ManagementObjectSearcher searcher = new ManagementObjectSearcher("Select * From Win32_Processor");
                string sCPUSerialNumber = "";
                foreach (ManagementObject mo in searcher.Get())
                {
                    sCPUSerialNumber = mo["ProcessorId"].ToString().Trim();
                    break;
                }
                return sCPUSerialNumber;
            }
            catch
            {
                return "";
            }
        }

        //獲取主機板序號
        public string GetBIOSSerialNumber()
        {
            try
            {
                ManagementObjectSearcher searcher = new ManagementObjectSearcher("Select * From Win32_BIOS");
                string sBIOSSerialNumber = "";
                foreach (ManagementObject mo in searcher.Get())
                {
                    sBIOSSerialNumber = mo.GetPropertyValue("SerialNumber").ToString().Trim();
                    break;
                }
                return sBIOSSerialNumber;
            }
            catch
            {
                return "";
            }
        }

        //獲取硬碟序號
        public string GetHardDiskSerialNumber()
        {
            try
            {
                ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
                string sHardDiskSerialNumber = "";
                foreach (ManagementObject mo in searcher.Get())
                {
                    sHardDiskSerialNumber = mo["SerialNumber"].ToString().Trim();
                    break;
                }
                return sHardDiskSerialNumber;
            }
            catch
            {
                return "";
            }
        }

        //獲取網路卡位址
        public string GetNetCardMACAddress()
        {
            try
            {
                ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter WHERE ((MACAddress Is Not NULL) AND (Manufacturer <> 'Microsoft'))");
                string NetCardMACAddress = "";
                foreach (ManagementObject mo in searcher.Get())
                {
                    NetCardMACAddress = mo["MACAddress"].ToString().Trim();
                    break;
                }
                return NetCardMACAddress;
            }
            catch
            {
                return "";
            }
        }


        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Get HDD serial\n";
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            foreach (ManagementObject info in searcher.Get())
            {
                richTextBox1.Text += info["DeviceID"].ToString() + "\t";
                richTextBox1.Text += "Model: " + info["Model"].ToString() + "\t";
                richTextBox1.Text += "Interface: " + info["InterfaceType"].ToString() + "\t";
                richTextBox1.Text += "Serial#: " + info["SerialNumber"].ToString() + "\n";

            }

        }

        private void button17_Click(object sender, EventArgs e)
        {
            var usbDevices = GetUSBDevices();

            foreach (var usbDevice in usbDevices)
            {
                //richTextBox1.Text += "Device ID: {0}, PNP Device ID: {1}, Description: {2}",
                //    usbDevice.DeviceID, usbDevice.PnpDeviceID, usbDevice.Description);

                richTextBox1.Text += "Device ID: " + usbDevice.DeviceID + "\n" + "PNP Device ID" + usbDevice.PnpDeviceID + "\n"
                + "Description: " + usbDevice.Description + "\n\n";

            }

        }

        static List<USBDeviceInfo> GetUSBDevices()
        {
            List<USBDeviceInfo> devices = new List<USBDeviceInfo>();

            ManagementObjectCollection collection;
            using (var searcher = new ManagementObjectSearcher(@"Select * From Win32_USBHub"))
                collection = searcher.Get();

            foreach (var device in collection)
            {
                devices.Add(new USBDeviceInfo(
                (string)device.GetPropertyValue("DeviceID"),
                (string)device.GetPropertyValue("PNPDeviceID"),
                (string)device.GetPropertyValue("Description")
                ));
            }

            collection.Dispose();
            return devices;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //WMI 從C＃中的USB閃存驅動器獲取VID/PID

            // Get all the disk drives 

            ManagementObjectSearcher mosDisks = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            // Loop through each object (disk) retrieved by WMI 

            foreach (ManagementObject moDisk in mosDisks.Get())
            {

                // Add the HDD to the list (use the Model field as the item's caption) 

                comboBox1.Items.Add(moDisk["Model"].ToString());

            }
            if (comboBox1.Items.Count > 0)
                comboBox1.SelectedIndex = 0;


        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Get all the disk drives from WMI that match the Model name selected in the ComboBox 

            ManagementObjectSearcher mosDisks = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive WHERE Model = '" + comboBox1.SelectedItem + "'");

            // Loop through the drives retrieved, although it should normally be only one loop going on here 

            foreach (ManagementObject moDisk in mosDisks.Get())
            {
                // Set all the fields to the appropriate values 

                richTextBox1.Text += "Type: " + moDisk["MediaType"].ToString() + "\n";

                richTextBox1.Text += "Model: " + moDisk["Model"].ToString() + "\n";

                richTextBox1.Text += "Serial: " + moDisk["SerialNumber"].ToString() + "\n";

                richTextBox1.Text += "Interface: " + moDisk["InterfaceType"].ToString() + "\n";

                // The capacity in gigabytes is easily calculated 

                richTextBox1.Text += "Capacity: " + moDisk["Size"].ToString() + " bytes (" + Math.Round(((((double)Convert.ToDouble(moDisk["Size"]) / 1024) / 1024) / 1024), 2) + " GB)" + "\n";

                richTextBox1.Text += "Partitions: " + moDisk["Partitions"].ToString() + "\n";

                richTextBox1.Text += "Signature: " + moDisk["Signature"].ToString() + "\n";

                richTextBox1.Text += "Firmware: " + moDisk["FirmwareRevision"].ToString() + "\n";

                richTextBox1.Text += "Cylinders: " + moDisk["TotalCylinders"].ToString() + "\n";

                richTextBox1.Text += "Sectors: " + moDisk["TotalSectors"].ToString() + "\n";

                richTextBox1.Text += "Heads: " + moDisk["TotalHeads"].ToString() + "\n";

                richTextBox1.Text += "Tracks: " + moDisk["TotalTracks"].ToString() + "\n";

                richTextBox1.Text += "Bytes per Sector: " + moDisk["BytesPerSector"].ToString() + "\n";

                richTextBox1.Text += "Sectors per Track: " + moDisk["SectorsPerTrack"].ToString() + "\n";

                richTextBox1.Text += "Tracks per Cylinder: " + moDisk["TracksPerCylinder"].ToString() + "\n";

            }


        }




    }
}
