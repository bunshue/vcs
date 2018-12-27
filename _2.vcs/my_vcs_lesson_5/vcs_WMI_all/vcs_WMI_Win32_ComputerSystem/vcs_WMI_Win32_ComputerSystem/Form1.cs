using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_ComputerSystem
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n獲取電腦資訊\n";
            richTextBox1.Text += "\nWin32_ComputerSystem\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_ComputerSystem");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "操作系統類型：" + mo["SystemType"] + "\n";
                richTextBox1.Text += "實體記憶體：" + mo["TotalPhysicalMemory"].ToString() + "\n";

                richTextBox1.Text += "PrimaryOwnerName: " + mo["PrimaryOwnerName"] + "\n";
                richTextBox1.Text += "Status: " + mo["Status"] + "\n";
                richTextBox1.Text += "UserName: " + mo["UserName"] + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"] + "\n";
                richTextBox1.Text += "BootupState: " + mo["BootupState"] + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"] + "\n";
                richTextBox1.Text += "Description: " + mo["Description"] + "\n";
                richTextBox1.Text += "Domain: " + mo["Domain"] + "\n";
                richTextBox1.Text += "Manufacturer: " + mo["Manufacturer"] + "\n";
                richTextBox1.Text += "Model: " + mo["Model"] + "\n";
                richTextBox1.Text += "Name: " + mo["Name"] + "\n";
                /* 無資料
                richTextBox1.Text += "aaaaa: " + mo["NameFormat"] + "\n";
                richTextBox1.Text += "aaaaa: " + mo["Workgroup"] + "\n";
                richTextBox1.Text += "aaaaa: " + mo["PrimaryOwnerContact"] + "\n";
                richTextBox1.Text += "aaaaa: " + mo["LastLoadInfo"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["DNSHostName"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["InitialLoadInfo[]"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["Roles[]"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["SystemStartupOptions[]"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["OEMStringArray[]"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["SupportContactDescription[]"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["SystemFamily"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["SystemSKUNumber"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["ChassisSKUNumber"] + "\n";
                */
                richTextBox1.Text += "nnnn: " + mo["AdminPasswordStatus"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["ChassisBootupState"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["CurrentTimeZone"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["DomainRole"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["FrontPanelResetStatus"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["KeyboardPasswordStatus"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["NumberOfLogicalProcessors"].ToString() + "\n";
                richTextBox1.Text += "NumberOfProcessors: " + mo["NumberOfProcessors"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["PauseAfterReset"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["PowerOnPasswordStatus"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["PowerState"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["PowerSupplyState"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["ResetCapability"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["ResetCount"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["ResetLimit"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["SystemStartupDelay"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["SystemStartupSetting"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["ThermalState"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["WakeUpType"].ToString() + "\n";
                /* 無資料
                //richTextBox1.Text += "nnnn: " + mo["OEMLogoBitmap[]"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["PCSystemType"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["BootOptionOnLimit"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["BootOptionOnWatchDog"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["BootStatus[]"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["PCSystemTypeEx"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["PowerManagementCapabilities[]"].ToString() + "\n";
                */

                //richTextBox1.Text += "InstallDate: " + mo["InstallDate"].ToString() + "\n";

            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }
    }
}
