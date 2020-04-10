using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_DiskDrive
{
    public partial class Form1 : Form
    {
        List<string> HardDriveDeviceID = new List<string>();

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
            richTextBox1.Text += "\n獲取全部硬碟資訊\n";
            richTextBox1.Text += "\nWin32_DiskDrive\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "\n\n==========================================================";
                richTextBox1.Text += "\n";

                richTextBox1.Text += "Description: " + (mo["Description"]) + "\n";
                richTextBox1.Text += "Name: " + (mo["Name"]) + "\n";
                richTextBox1.Text += "Model: " + (mo["Model"]) + "\n";
                richTextBox1.Text += "DeviceID: " + (mo["DeviceId"]) + "\n";
                richTextBox1.Text += "BytesPerSector: " + (mo["BytesPerSector".ToString()]) + "\n";
                richTextBox1.Text += "Size: " + (mo["Size".ToString()]) + "\n";
                richTextBox1.Text += "InterfaceType: " + (mo["InterfaceType"]) + "\n";
                richTextBox1.Text += "PNPDeviceID: " + (mo["PNPDeviceID"]) + "\n";
                //richTextBox1.Text += "SerialNumber " + (mo["SerialNumber"]) + "\n";

                richTextBox1.Text += "Manufacturer: " + (mo["Manufacturer"]) + "\n";

                richTextBox1.Text += "CapabilityDescriptions: " + (mo["CapabilityDescriptions"]) + "\n";
                richTextBox1.Text += "Caption: " + (mo["Caption"]) + "\n";
                richTextBox1.Text += "CompressionMethod: " + (mo["CompressionMethod"]) + "\n";
                richTextBox1.Text += "CreationClassName: " + (mo["CreationClassName"]) + "\n";
                richTextBox1.Text += "SystemCreationClassName: " + (mo["SystemCreationClassName"]) + "\n";
                richTextBox1.Text += "SystemName: " + (mo["SystemName"]) + "\n";
                richTextBox1.Text += "ErrorDescription: " + (mo["ErrorDescription"]) + "\n";
                richTextBox1.Text += "ErrorMethodology: " + (mo["ErrorMethodology"]) + "\n";
                //richTextBox1.Text += "FirmwareRevision: " + (mo["FirmwareRevision"]) + "\n";
                richTextBox1.Text += "MediaType: " + (mo["MediaType"]) + "\n";
                richTextBox1.Text += "Status: " + (mo["Status"]) + "\n";

                richTextBox1.Text += "Index: " + (mo["Index".ToString()]) + "\n";
                richTextBox1.Text += "LastErrorCode: " + (mo["LastErrorCode".ToString()]) + "\n";
                richTextBox1.Text += "Partitions: " + (mo["Partitions".ToString()]) + "\n";
                richTextBox1.Text += "SectorsPerTrack: " + (mo["SectorsPerTrack".ToString()]) + "\n";
                richTextBox1.Text += "Signature: " + (mo["Signature".ToString()]) + "\n";
                richTextBox1.Text += "CYLINDER: " + (mo["TotalCylinders".ToString()]) + "\n";
                richTextBox1.Text += "HEAD: : " + (mo["TotalHeads".ToString()]) + "\n";
                richTextBox1.Text += "SECTOR: " + (mo["TotalSectors".ToString()]) + "\n";
                richTextBox1.Text += "TRACK: " + (mo["TotalTracks".ToString()]) + "\n";
                richTextBox1.Text += "TracksPerCylinder: " + (mo["TracksPerCylinder".ToString()]) + "\n";

                richTextBox1.Text += "Availability: " + (mo["Availability".ToString()]) + "\n";
                //richTextBox1.Text += "Capabilities: " + (mo["Capabilities[]".ToString()]) + "\n";
                richTextBox1.Text += "ConfigManagerErrorCode: " + (mo["ConfigManagerErrorCode".ToString()]) + "\n";
                richTextBox1.Text += "DefaultBlockSize: " + (mo["DefaultBlockSize".ToString()]) + "\n";
                richTextBox1.Text += "MaxBlockSize: " + (mo["MaxBlockSize".ToString()]) + "\n";
                richTextBox1.Text += "MaxMediaSize: " + (mo["MaxMediaSize".ToString()]) + "\n";
                richTextBox1.Text += "MinBlockSize: " + (mo["MinBlockSize".ToString()]) + "\n";
                richTextBox1.Text += "NumberOfMediaSupported: " + (mo["NumberOfMediaSupported".ToString()]) + "\n";
                //richTextBox1.Text += "PowerManagementCapabilities: " + (mo["PowerManagementCapabilities[]".ToString()]) + "\n";
                richTextBox1.Text += "SCSIBus: " + (mo["SCSIBus".ToString()]) + "\n";
                richTextBox1.Text += "SCSILogicalUnit: " + (mo["SCSILogicalUnit".ToString()]) + "\n";
                richTextBox1.Text += "SCSIPort: " + (mo["SCSIPort".ToString()]) + "\n";
                richTextBox1.Text += "SCSITargetId: " + (mo["SCSITargetId".ToString()]) + "\n";
                richTextBox1.Text += "StatusInfo: " + (mo["StatusInfo".ToString()]) + "\n";

                richTextBox1.Text += "InstallDate: " + (mo["InstallDate".ToString()]) + "\n";

                richTextBox1.Text += "MediaLoaded: " + (mo["MediaLoaded".ToString()]) + "\n";
                richTextBox1.Text += "ErrorCleared: " + (mo["ErrorCleared".ToString()]) + "\n";
                richTextBox1.Text += "ConfigManagerUserConfig: " + (mo["ConfigManagerUserConfig".ToString()]) + "\n";
                richTextBox1.Text += "PowerManagementSupported: " + (mo["PowerManagementSupported".ToString()]) + "\n";
                richTextBox1.Text += "NeedsCleaning: " + (mo["NeedsCleaning".ToString()]) + "\n";


                richTextBox1.Text += "\n";
                richTextBox1.Text += "DiskPartition: ";
                richTextBox1.Text += "\n";


                foreach (ManagementObject b in mo.GetRelated("Win32_DiskPartition"))    //磁碟分區
                {
                    richTextBox1.Text += "\t";
                    richTextBox1.Text += b["Name"];
                    richTextBox1.Text += "\n";

                    richTextBox1.Text += "Caption: " + b["Caption"] + "\n";
                    richTextBox1.Text += "CreationClassName: " + b["CreationClassName"] + "\n";
                    richTextBox1.Text += "Description: " + b["Description"] + "\n";
                    richTextBox1.Text += "DeviceID: " + b["DeviceID"] + "\n";
                    richTextBox1.Text += "SystemCreationClassName: " + b["SystemCreationClassName"] + "\n";
                    richTextBox1.Text += "SystemName: " + b["SystemName"] + "\n";
                    richTextBox1.Text += "Type: " + b["Type"] + "\n";

                    richTextBox1.Text += "Index: " + (b["Index".ToString()]) + "\n";
                    richTextBox1.Text += "DiskIndex: " + (b["DiskIndex".ToString()]) + "\n";
                    richTextBox1.Text += "BlockSize: " + (b["BlockSize".ToString()]) + "\n";
                    richTextBox1.Text += "NumberOfBlocks: " + (b["NumberOfBlocks".ToString()]) + "\n";
                    richTextBox1.Text += "Size: " + (b["Size".ToString()]) + "\n";
                    richTextBox1.Text += "Bootable: " + (b["Bootable".ToString()]) + "\n";
                    richTextBox1.Text += "BootPartition: " + (b["BootPartition".ToString()]) + "\n";
                    richTextBox1.Text += "PrimaryPartition: " + (b["PrimaryPartition".ToString()]) + "\n";
                    richTextBox1.Text += "StartingOffset: " + (b["StartingOffset".ToString()]) + "\n";


                    foreach (ManagementBaseObject c in b.GetRelated("Win32_LogicalDisk"))   //邏輯磁碟
                    {
                        richTextBox1.Text += "\t";
                        richTextBox1.Text += "LogicalDisk: ";
                        richTextBox1.Text += "\t";
                        richTextBox1.Text += c["Name"];
                        richTextBox1.Text += "\n" + "\t";

                        richTextBox1.Text += "SystemCreationClassName: " + c["SystemCreationClassName"] + "\n" + "\t";
                        richTextBox1.Text += "SystemName: " + c["SystemName"] + "\n" + "\t";
                        richTextBox1.Text += "VolumeName: " + c["VolumeName"] + "\n" + "\t";
                        richTextBox1.Text += "VolumeSerialNumber: " + c["VolumeSerialNumber"] + "\n" + "\t";
                        richTextBox1.Text += "CreationClassName: " + c["CreationClassName"] + "\n" + "\t";
                        richTextBox1.Text += "Description: " + c["Description"] + "\n" + "\t";
                        richTextBox1.Text += "DeviceID: " + c["DeviceID"] + "\n" + "\t";
                        richTextBox1.Text += "FileSystem: " + c["FileSystem"] + "\n" + "\t";
                        richTextBox1.Text += "Caption: " + c["Caption"] + "\n" + "\t";
                        richTextBox1.Text += "DriveType: " + c["DriveType".ToString()] + "\n" + "\t";
                        richTextBox1.Text += "FreeSpace: " + c["FreeSpace".ToString()] + "\n" + "\t";
                        richTextBox1.Text += "MaximumComponentLength: " + c["MaximumComponentLength".ToString()] + "\n" + "\t";
                        richTextBox1.Text += "MediaType: " + c["MediaType".ToString()] + "\n" + "\t";
                        richTextBox1.Text += "Size: " + c["Size".ToString()];
                    }

                    richTextBox1.Text += "\n";
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n獲取單一硬碟資訊\n";
            richTextBox1.Text += "\nWin32_DiskDrive\n";

            UInt32 diskNumber = 0;
            String physicalName = ("\\\\.\\PHYSICALDRIVE" + diskNumber).Replace("\\", "\\\\");
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive WHERE DeviceID = \"" + physicalName + "\"");
            
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "\n\n==========================================================";
                richTextBox1.Text += "\n";

                richTextBox1.Text += "Description: " + (mo["Description"]) + "\n";
                richTextBox1.Text += "Name: " + (mo["Name"]) + "\n";
                richTextBox1.Text += "Model: " + (mo["Model"]) + "\n";
                richTextBox1.Text += "DeviceID: " + (mo["DeviceId"]) + "\n";
                richTextBox1.Text += "BytesPerSector: " + (mo["BytesPerSector".ToString()]) + "\n";
                richTextBox1.Text += "Size: " + (mo["Size".ToString()]) + "\n";
                richTextBox1.Text += "InterfaceType: " + (mo["InterfaceType"]) + "\n";
                richTextBox1.Text += "PNPDeviceID: " + (mo["PNPDeviceID"]) + "\n";
                //richTextBox1.Text += "SerialNumber " + (mo["SerialNumber"]) + "\n";

                richTextBox1.Text += "Manufacturer: " + (mo["Manufacturer"]) + "\n";

                richTextBox1.Text += "CapabilityDescriptions: " + (mo["CapabilityDescriptions"]) + "\n";
                richTextBox1.Text += "Caption: " + (mo["Caption"]) + "\n";
                richTextBox1.Text += "CompressionMethod: " + (mo["CompressionMethod"]) + "\n";
                richTextBox1.Text += "CreationClassName: " + (mo["CreationClassName"]) + "\n";
                richTextBox1.Text += "SystemCreationClassName: " + (mo["SystemCreationClassName"]) + "\n";
                richTextBox1.Text += "SystemName: " + (mo["SystemName"]) + "\n";
                richTextBox1.Text += "ErrorDescription: " + (mo["ErrorDescription"]) + "\n";
                richTextBox1.Text += "ErrorMethodology: " + (mo["ErrorMethodology"]) + "\n";
                //richTextBox1.Text += "FirmwareRevision: " + (mo["FirmwareRevision"]) + "\n";
                richTextBox1.Text += "MediaType: " + (mo["MediaType"]) + "\n";
                richTextBox1.Text += "Status: " + (mo["Status"]) + "\n";

                richTextBox1.Text += "Index: " + (mo["Index".ToString()]) + "\n";
                richTextBox1.Text += "LastErrorCode: " + (mo["LastErrorCode".ToString()]) + "\n";
                richTextBox1.Text += "Partitions: " + (mo["Partitions".ToString()]) + "\n";
                richTextBox1.Text += "SectorsPerTrack: " + (mo["SectorsPerTrack".ToString()]) + "\n";
                richTextBox1.Text += "Signature: " + (mo["Signature".ToString()]) + "\n";
                richTextBox1.Text += "CYLINDER: " + (mo["TotalCylinders".ToString()]) + "\n";
                richTextBox1.Text += "HEAD: : " + (mo["TotalHeads".ToString()]) + "\n";
                richTextBox1.Text += "SECTOR: " + (mo["TotalSectors".ToString()]) + "\n";
                richTextBox1.Text += "TRACK: " + (mo["TotalTracks".ToString()]) + "\n";
                richTextBox1.Text += "TracksPerCylinder: " + (mo["TracksPerCylinder".ToString()]) + "\n";

                richTextBox1.Text += "Availability: " + (mo["Availability".ToString()]) + "\n";
                //richTextBox1.Text += "Capabilities: " + (mo["Capabilities[]".ToString()]) + "\n";
                richTextBox1.Text += "ConfigManagerErrorCode: " + (mo["ConfigManagerErrorCode".ToString()]) + "\n";
                richTextBox1.Text += "DefaultBlockSize: " + (mo["DefaultBlockSize".ToString()]) + "\n";
                richTextBox1.Text += "MaxBlockSize: " + (mo["MaxBlockSize".ToString()]) + "\n";
                richTextBox1.Text += "MaxMediaSize: " + (mo["MaxMediaSize".ToString()]) + "\n";
                richTextBox1.Text += "MinBlockSize: " + (mo["MinBlockSize".ToString()]) + "\n";
                richTextBox1.Text += "NumberOfMediaSupported: " + (mo["NumberOfMediaSupported".ToString()]) + "\n";
                //richTextBox1.Text += "PowerManagementCapabilities: " + (mo["PowerManagementCapabilities[]".ToString()]) + "\n";
                richTextBox1.Text += "SCSIBus: " + (mo["SCSIBus".ToString()]) + "\n";
                richTextBox1.Text += "SCSILogicalUnit: " + (mo["SCSILogicalUnit".ToString()]) + "\n";
                richTextBox1.Text += "SCSIPort: " + (mo["SCSIPort".ToString()]) + "\n";
                richTextBox1.Text += "SCSITargetId: " + (mo["SCSITargetId".ToString()]) + "\n";
                richTextBox1.Text += "StatusInfo: " + (mo["StatusInfo".ToString()]) + "\n";

                richTextBox1.Text += "InstallDate: " + (mo["InstallDate".ToString()]) + "\n";

                richTextBox1.Text += "MediaLoaded: " + (mo["MediaLoaded".ToString()]) + "\n";
                richTextBox1.Text += "ErrorCleared: " + (mo["ErrorCleared".ToString()]) + "\n";
                richTextBox1.Text += "ConfigManagerUserConfig: " + (mo["ConfigManagerUserConfig".ToString()]) + "\n";
                richTextBox1.Text += "PowerManagementSupported: " + (mo["PowerManagementSupported".ToString()]) + "\n";
                richTextBox1.Text += "NeedsCleaning: " + (mo["NeedsCleaning".ToString()]) + "\n";


                richTextBox1.Text += "\n";
                richTextBox1.Text += "DiskPartition: ";
                richTextBox1.Text += "\n";


                foreach (ManagementObject b in mo.GetRelated("Win32_DiskPartition"))    //磁碟分區
                {
                    richTextBox1.Text += "\t";
                    richTextBox1.Text += b["Name"];
                    richTextBox1.Text += "\n";

                    richTextBox1.Text += "Caption: " + b["Caption"] + "\n";
                    richTextBox1.Text += "CreationClassName: " + b["CreationClassName"] + "\n";
                    richTextBox1.Text += "Description: " + b["Description"] + "\n";
                    richTextBox1.Text += "DeviceID: " + b["DeviceID"] + "\n";
                    richTextBox1.Text += "SystemCreationClassName: " + b["SystemCreationClassName"] + "\n";
                    richTextBox1.Text += "SystemName: " + b["SystemName"] + "\n";
                    richTextBox1.Text += "Type: " + b["Type"] + "\n";

                    richTextBox1.Text += "Index: " + (b["Index".ToString()]) + "\n";
                    richTextBox1.Text += "DiskIndex: " + (b["DiskIndex".ToString()]) + "\n";
                    richTextBox1.Text += "BlockSize: " + (b["BlockSize".ToString()]) + "\n";
                    richTextBox1.Text += "NumberOfBlocks: " + (b["NumberOfBlocks".ToString()]) + "\n";
                    richTextBox1.Text += "Size: " + (b["Size".ToString()]) + "\n";
                    richTextBox1.Text += "Bootable: " + (b["Bootable".ToString()]) + "\n";
                    richTextBox1.Text += "BootPartition: " + (b["BootPartition".ToString()]) + "\n";
                    richTextBox1.Text += "PrimaryPartition: " + (b["PrimaryPartition".ToString()]) + "\n";
                    richTextBox1.Text += "StartingOffset: " + (b["StartingOffset".ToString()]) + "\n";


                    foreach (ManagementBaseObject c in b.GetRelated("Win32_LogicalDisk"))   //邏輯磁碟
                    {
                        richTextBox1.Text += "\t";
                        richTextBox1.Text += "LogicalDisk: ";
                        richTextBox1.Text += "\t";
                        richTextBox1.Text += c["Name"];
                        richTextBox1.Text += "\n" + "\t";

                        richTextBox1.Text += "SystemCreationClassName: " + c["SystemCreationClassName"] + "\n" + "\t";
                        richTextBox1.Text += "SystemName: " + c["SystemName"] + "\n" + "\t";
                        richTextBox1.Text += "VolumeName: " + c["VolumeName"] + "\n" + "\t";
                        richTextBox1.Text += "VolumeSerialNumber: " + c["VolumeSerialNumber"] + "\n" + "\t";
                        richTextBox1.Text += "CreationClassName: " + c["CreationClassName"] + "\n" + "\t";
                        richTextBox1.Text += "Description: " + c["Description"] + "\n" + "\t";
                        richTextBox1.Text += "DeviceID: " + c["DeviceID"] + "\n" + "\t";
                        richTextBox1.Text += "FileSystem: " + c["FileSystem"] + "\n" + "\t";
                        richTextBox1.Text += "Caption: " + c["Caption"] + "\n" + "\t";
                        richTextBox1.Text += "DriveType: " + c["DriveType".ToString()] + "\n" + "\t";
                        richTextBox1.Text += "FreeSpace: " + c["FreeSpace".ToString()] + "\n" + "\t";
                        richTextBox1.Text += "MaximumComponentLength: " + c["MaximumComponentLength".ToString()] + "\n" + "\t";
                        richTextBox1.Text += "MediaType: " + c["MediaType".ToString()] + "\n" + "\t";
                        richTextBox1.Text += "Size: " + c["Size".ToString()];
                    }

                    richTextBox1.Text += "\n";
                }
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n獲取全部硬碟資訊\n";
            richTextBox1.Text += "\nWin32_DiskDrive\n";
            comboBox1.Items.Clear();
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "==========================================================\n";
                richTextBox1.Text += "DeviceID: " + (mo["DeviceID"]) + "\n";
                richTextBox1.Text += "Model: " + (mo["Model"]) + "\n";
                richTextBox1.Text += "Size: " + (mo["Size".ToString()]) + "\n";
                comboBox1.Items.Add(mo["Model"]);
                HardDriveDeviceID.Add((mo["DeviceID"].ToString()));
            }
            richTextBox1.Text += "==========================================================\n";
            comboBox1.SelectedIndex = 0;

        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "comboBox1.SelectedIndex = " + comboBox1.SelectedIndex.ToString() + "\n";

            if (comboBox1.SelectedIndex < 0)
            {
                richTextBox1.Text += "未選取硬碟\n";
                return;
            }
            else
            {
                String physicalName = HardDriveDeviceID[comboBox1.SelectedIndex].Replace("\\", "\\\\");
                ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive WHERE DeviceID = \"" + physicalName + "\"");

                foreach (ManagementObject mo in mos.Get())
                {
                    richTextBox1.Text += "\n硬碟資訊: \n";
                    richTextBox1.Text += "==========================================================\n";
                    richTextBox1.Text += "DeviceID: " + (mo["DeviceID"]) + "\n";
                    richTextBox1.Text += "Model: " + (mo["Model"]) + "\n";
                    richTextBox1.Text += "Size: " + (mo["Size".ToString()]) + "\n";
                    richTextBox1.Text += "InterfaceType: " + (mo["InterfaceType"]) + "\n";
                    richTextBox1.Text += "MediaType: " + (mo["MediaType"]) + "\n";

                    richTextBox1.Text += "\n磁碟分區: \n";
                    foreach (ManagementObject b in mo.GetRelated("Win32_DiskPartition"))    //磁碟分區
                    {
                        richTextBox1.Text += "----------------------------------------------------------\n";
                        richTextBox1.Text += "\t";
                        richTextBox1.Text += b["Name"];
                        richTextBox1.Text += "\n";

                        richTextBox1.Text += "Caption: " + b["Caption"] + "\n";
                        richTextBox1.Text += "DeviceID: " + b["DeviceID"] + "\n";
                        richTextBox1.Text += "Type: " + b["Type"] + "\n";

                        richTextBox1.Text += "Index: " + (b["Index".ToString()]) + "\n";
                        richTextBox1.Text += "NumberOfBlocks: " + (b["NumberOfBlocks".ToString()]) + "\n";
                        richTextBox1.Text += "Size: " + (b["Size".ToString()]) + "\n";

                        richTextBox1.Text += "\n邏輯磁碟: \n";
                        foreach (ManagementBaseObject c in b.GetRelated("Win32_LogicalDisk"))   //邏輯磁碟
                        {
                            richTextBox1.Text += "\t";
                            richTextBox1.Text += "LogicalDisk: ";
                            richTextBox1.Text += "\t";
                            richTextBox1.Text += c["Name"];
                            richTextBox1.Text += "\n" + "\t";

                            richTextBox1.Text += "VolumeName: " + c["VolumeName"] + "\n" + "\t";
                            richTextBox1.Text += "VolumeSerialNumber: " + c["VolumeSerialNumber"] + "\n" + "\t";
                            richTextBox1.Text += "DeviceID: " + c["DeviceID"] + "\n" + "\t";
                            richTextBox1.Text += "FileSystem: " + c["FileSystem"] + "\n" + "\t";
                            richTextBox1.Text += "DriveType: " + c["DriveType".ToString()] + "\n" + "\t";
                            richTextBox1.Text += "FreeSpace: " + c["FreeSpace".ToString()] + "\n" + "\t";
                            richTextBox1.Text += "MediaType: " + c["MediaType".ToString()] + "\n" + "\t";
                            richTextBox1.Text += "Size: " + c["Size".ToString()] + "\n";
                        }
                        richTextBox1.Text += "----------------------------------------------------------\n";

                        richTextBox1.Text += "\n";
                    }
                }
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n取得所有的邏輯磁碟區：\n";
            comboBox2.Items.Clear();
            ManagementObjectSearcher mos2 = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");
            foreach (ManagementObject mo in mos2.Get())
            {
                richTextBox1.Text += mo["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo["VolumeSerialNumber"] + "\n";
                comboBox2.Items.Add(mo["Name"]);
            }
            comboBox2.SelectedIndex = 0;
        }
    }
}
