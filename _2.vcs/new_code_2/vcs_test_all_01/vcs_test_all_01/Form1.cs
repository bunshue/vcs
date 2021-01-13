using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//參考 / 加入參考 / .NET  System.Management

using System.Management;

using System.Net.NetworkInformation;

using System.IO;    //for Stream
using System.Net;   //for WebClient

using System.Collections;   //for IEnumerable

namespace vcs_test_all_01
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
            x_st = 12;
            y_st = 140;
            dx = 180;
            dy = 60;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            button16.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button19.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 7);
        }

        private void button0_Click(object sender, EventArgs e)
        {
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

        private void button1_Click(object sender, EventArgs e)
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

        private void button2_Click(object sender, EventArgs e)
        {
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

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics; //創建畫板,這裡的畫板是由Form提供的.
            Pen p = new Pen(Color.Blue, 2);//定義了一個藍色,寬度為的畫筆
            g.DrawLine(p, 10, 10, 100, 100);//在畫板上畫直線,起始坐標為(10,10),終點坐標為(100,100)
            g.DrawRectangle(p, 10, 10, 100, 100);//在畫板上畫矩形,起始坐標為(10,10),寬為,高為
            g.DrawEllipse(p, 10, 10, 100, 100);//在畫板上畫橢圓,起始坐標為(10,10),外接矩形的寬為,高為

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


        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {
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


    }
}
