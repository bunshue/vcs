using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_Win32_DiskDrive
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
            // 抓取硬碟&USB儲存裝置磁碟代號
            using (ManagementClass devs = new ManagementClass(@"Win32_Diskdrive"))
            {
                ManagementObjectCollection moc = devs.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    richTextBox1.Text += "==========================================================\n";
                    richTextBox1.Text += "Description: ";
                    richTextBox1.Text += mo["Description"] + "\n";
                    richTextBox1.Text += "Name: ";
                    richTextBox1.Text += mo["Name"] + "\n";
                }
                richTextBox1.Text += "==========================================================\n";

                foreach (ManagementObject mo in moc)
                {
                    richTextBox1.Text += "==========================================================";
                    richTextBox1.Text += "Description: " + mo["Description"] + "\n";
                    richTextBox1.Text += "Name: " + mo["Name"] + "\n";
                    richTextBox1.Text += "Model: " + mo["Model"] + "\n";
                    richTextBox1.Text += "DeviceID: " + mo["DeviceId"] + "\n";
                    richTextBox1.Text += "BytesPerSector: " + mo["BytesPerSector".ToString()] + "\n";
                    richTextBox1.Text += "Size: " + mo["Size".ToString()] + "\n";
                    richTextBox1.Text += "InterfaceType: " + mo["InterfaceType"] + "\n";
                    richTextBox1.Text += "PNPDeviceID: " + mo["PNPDeviceID"] + "\n";
                    //richTextBox1.Text += "bbbbbb ";
                    // + mo["SerialNumber"] + "\n";
                    //richTextBox1.Text += "Manufacturer: " + mo["Manufacturer"] + "\n";

                    richTextBox1.Text += "CapabilityDescriptions: " + mo["CapabilityDescriptions"] + "\n";
                    richTextBox1.Text += "Caption: " + mo["Caption"] + "\n";
                    richTextBox1.Text += "CompressionMethod: " + mo["CompressionMethod"] + "\n";
                    richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"] + "\n";
                    richTextBox1.Text += "SystemCreationClassName: " + mo["SystemCreationClassName"] + "\n";
                    richTextBox1.Text += "SystemName: " + mo["SystemName"] + "\n";
                    richTextBox1.Text += "ErrorDescription: " + mo["ErrorDescription"] + "\n";
                    richTextBox1.Text += "ErrorMethodology: " + mo["ErrorMethodology"] + "\n";
                    //richTextBox1.Text += "FirmwareRevision: " + mo["FirmwareRevision"] + "\n";
                    richTextBox1.Text += "MediaType: " + mo["MediaType"] + "\n";
                    richTextBox1.Text += "Status: " + mo["Status"] + "\n";

                    richTextBox1.Text += "Index: " + mo["Index".ToString()] + "\n";
                    richTextBox1.Text += "LastErrorCode: " + mo["LastErrorCode".ToString()] + "\n";
                    richTextBox1.Text += "MediaLoaded: " + mo["MediaLoaded".ToString()] + "\n";
                    richTextBox1.Text += "Partitions: " + mo["Partitions".ToString()] + "\n";
                    richTextBox1.Text += "SectorsPerTrack: " + mo["SectorsPerTrack".ToString()] + "\n";
                    richTextBox1.Text += "Signature: " + mo["Signature".ToString()] + "\n";
                    richTextBox1.Text += "CYLINDER: " + mo["TotalCylinders".ToString()] + "\n";
                    richTextBox1.Text += "HEAD: : " + mo["TotalHeads".ToString()] + "\n";
                    richTextBox1.Text += "SECTOR: " + mo["TotalSectors".ToString()] + "\n";
                    richTextBox1.Text += "TRACK: " + mo["TotalTracks".ToString()] + "\n";
                    richTextBox1.Text += "TracksPerCylinder: " + mo["TracksPerCylinder".ToString()] + "\n";

                    richTextBox1.Text += "DiskPartition: ";
                    foreach (ManagementObject b in mo.GetRelated("Win32_DiskPartition"))
                    {
                        richTextBox1.Text += "Name: " + b["Name"] + "\n";
                        richTextBox1.Text += "Caption: " + b["Caption"] + "\n";
                        richTextBox1.Text += "CreationClassName: " + b["CreationClassName"] + "\n";
                        richTextBox1.Text += "Description: " + b["Description"] + "\n";
                        richTextBox1.Text += "DeviceID: " + b["DeviceID"] + "\n";
                        richTextBox1.Text += "SystemCreationClassName: " + b["SystemCreationClassName"] + "\n";
                        richTextBox1.Text += "SystemName: " + b["SystemName"] + "\n";
                        richTextBox1.Text += "Type: " + b["Type"] + "\n";

                        richTextBox1.Text += "Index: " + b["Index".ToString()] + "\n";
                        richTextBox1.Text += "DiskIndex: " + b["DiskIndex".ToString()] + "\n";
                        richTextBox1.Text += "BlockSize: " + b["BlockSize".ToString()] + "\n";
                        richTextBox1.Text += "NumberOfBlocks: " + b["NumberOfBlocks".ToString()] + "\n";
                        richTextBox1.Text += "Size: " + b["Size".ToString()] + "\n";
                        richTextBox1.Text += "Bootable: " + b["Bootable".ToString()] + "\n";
                        richTextBox1.Text += "BootPartition: " + b["BootPartition".ToString()] + "\n";
                        richTextBox1.Text += "PrimaryPartition: " + b["PrimaryPartition".ToString()] + "\n";
                        richTextBox1.Text += "StartingOffset: " + b["StartingOffset".ToString()] + "\n";

                        foreach (ManagementBaseObject c in b.GetRelated("Win32_LogicalDisk"))
                        {
                            richTextBox1.Text += "LogicalDisk: " + c["Name"] + "\n";
                            richTextBox1.Text += "SystemCreationClassName: " + c["SystemCreationClassName"] + "\n";
                            richTextBox1.Text += "SystemName: " + c["SystemName"] + "\n";
                            richTextBox1.Text += "VolumeName: " + c["VolumeName"] + "\n";
                            richTextBox1.Text += "VolumeSerialNumber: " + c["VolumeSerialNumber"] + "\n";
                            richTextBox1.Text += "CreationClassName: " + c["CreationClassName"] + "\n";
                            richTextBox1.Text += "Description: " + c["Description"] + "\n";
                            richTextBox1.Text += "DeviceID: " + c["DeviceID"] + "\n";
                            richTextBox1.Text += "FileSystem: " + c["FileSystem"] + "\n";
                            richTextBox1.Text += "Caption: " + c["Caption"] + "\n";
                            richTextBox1.Text += "DriveType: " + c["DriveType".ToString()] + "\n";
                            richTextBox1.Text += "FreeSpace: " + c["FreeSpace".ToString()] + "\n";
                            richTextBox1.Text += "MaximumComponentLength: " + c["MaximumComponentLength".ToString()] + "\n";
                            richTextBox1.Text += "MediaType: " + c["MediaType".ToString()] + "\n";
                            richTextBox1.Text += "Size: " + c["Size".ToString()] + "\n";
                        }
                    }
                }
            }
        }
    }
}
