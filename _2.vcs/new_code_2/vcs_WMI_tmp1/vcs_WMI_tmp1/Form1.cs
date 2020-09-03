using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Management;


namespace vcs_WMI_tmp1
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

        private void button1_Click(object sender, EventArgs e)
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


        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "獲取CPU序號\t" + GetCPUSerialNumber() + "\n";
            richTextBox1.Text += "獲取主機板序號\t" + GetBIOSSerialNumber() + "\n";
            richTextBox1.Text += "獲取硬碟序號\t" + GetHardDiskSerialNumber() + "\n";
            richTextBox1.Text += "獲取網路卡位址\t" + GetNetCardMACAddress() + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //如何從C＃中的USB閃存驅動器獲取VID/PID？

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

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }



    }
}
