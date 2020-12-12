using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Add a reference to the System.Management.
using System.Management;

namespace vcs_test_all_02
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
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


        private void button2_Click(object sender, EventArgs e)
        {
            // Create the firewall type.
            Type FWManagerType = Type.GetTypeFromProgID("HNetCfg.FwMgr");

            // Use the firewall type to create a firewall manager object.
            dynamic FWManager = Activator.CreateInstance(FWManagerType);

            // Check the status of the firewall.

            if (FWManager.LocalPolicy.CurrentProfile.FirewallEnabled == true)
                richTextBox1.Text += "防火牆已開啟\n";
            else
                richTextBox1.Text += "防火牆未開啟\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // Load the timezone information.
            foreach (TimeZoneInfo info in TimeZoneInfo.GetSystemTimeZones())
            {
                richTextBox1.Text += info + "\n";
            }
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

    }
}
