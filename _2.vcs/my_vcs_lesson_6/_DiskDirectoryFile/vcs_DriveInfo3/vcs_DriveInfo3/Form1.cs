using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport, StructLayout

namespace vcs_DriveInfo3
{
    public partial class Form1 : Form
    {
        [DllImport("kernel32.dll")]
        private static extern bool GetDiskFreeSpaceEx(string lpDirectoryName, out ulong lpFreeBytesAvailable, out ulong lpTotalNumberOfBytes, out ulong lpTotalNumberOfFreeBytes);

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
            y_st = 12;
            dx = 200 + 10;
            dy = 50 + 10;

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

            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Size = new Size(450, 600);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(700, 700);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            ulong freesize;
            freesize = GetFreeSpace("C");
            richTextBox1.Text += "磁碟C剩餘空間: " + freesize.ToString() + " bytes\n";
            freesize = GetFreeSpace("D");
            richTextBox1.Text += "磁碟D剩餘空間: " + freesize.ToString() + " bytes\n";
            freesize = GetFreeSpace("G");
            richTextBox1.Text += "磁碟G剩餘空間: " + freesize.ToString() + " bytes\n";
        }

        /// <summary>
        /// 取得磁碟剩餘空間
        /// </summary>
        /// <param name="driveDirectoryName">驅動器名</param>
        /// <returns>剩餘空間</returns>
        private static ulong GetFreeSpace(string driveDirectoryName)
        {
            ulong freeBytesAvailable, totalNumberOfBytes, totalNumberOfFreeBytes;
            if (!driveDirectoryName.EndsWith(":\\"))
            {
                driveDirectoryName += ":\\";
            }
            GetDiskFreeSpaceEx(driveDirectoryName, out freeBytesAvailable, out totalNumberOfBytes, out totalNumberOfFreeBytes);
            return freeBytesAvailable;
        }

        //------------------------------------------------------------

        [DllImport("kernel32.dll", EntryPoint = "GetDiskFreeSpaceEx")]
        public static extern int GetDiskFreeSpaceEx(string lpDirectoryName, out long lpFreeBytesAvailable, out long lpTotalNumberOfBytes, out long lpTotalNumberOfFreeBytes);
        private void button1_Click(object sender, EventArgs e)
        {
            //取得本機或網路磁碟機的磁碟訊息, 選擇磁碟或目錄
            FolderBrowserDialog fbd = new FolderBrowserDialog();
            if (fbd.ShowDialog() == DialogResult.OK)
            {
                long fb, ftb, tfb;
                string str = fbd.SelectedPath;
                richTextBox1.Text += "path : " + str + "\n";
                if (GetDiskFreeSpaceEx(str, out fb, out ftb, out tfb) != 0)
                {
                    string strfb = Convert.ToString(fb / 1024 / 1024 / 1024) + " G";
                    string strftb = Convert.ToString(ftb / 1024 / 1024 / 1024) + " G";
                    string strtfb = Convert.ToString(tfb / 1024 / 1024 / 1024) + " G";
                    richTextBox1.Text += "總空間" + strfb + "\n";
                    richTextBox1.Text += "可用空間" + strftb + "\n";
                    richTextBox1.Text += "總剩餘空間" + strtfb + "\n";
                }
                else
                {
                    MessageBox.Show("NO");
                }
            }
        }

        //------------------------------------------------------------

        //取得硬碟資訊 ST
        // TBD [DllImport("kernel32.dll", EntryPoint = "GetDiskFreeSpaceEx")]
        // TBD public static extern int GetDiskFreeSpaceEx(string lpDirectoryName, out long lpFreeBytesAvailable, out long lpTotalNumberOfBytes, out long lpTotalNumberOfFreeBytes);

        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionTBGBMBKB(Int64 size)
        {
            if (size < 0)
                return "不合法的數值";
            else if (size / TB >= 1024)//如果目前Byte的值大於等於1024TB
                return "無法表示";
            else if (size / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(size / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (size / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(size / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (size / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(size / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (size / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(size / (float)KB, 2)).ToString() + " KB";//將其轉換成KB
            else
                return size.ToString() + " Byte";//顯示Byte值
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //取得硬碟資訊
            //取得硬碟資訊
            long fb, ftb, tfb;
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__RW\_excel";

            //this.textBox4.Text = foldername;
            richTextBox1.Text += "get : " + foldername + "\n";
            if (GetDiskFreeSpaceEx(foldername, out fb, out ftb, out tfb) != 0)
            {
                richTextBox1.Text += "磁碟總容量：" + ByteConversionTBGBMBKB(Convert.ToInt64(ftb)) + "\n";
                richTextBox1.Text += "可用磁碟空間：" + ByteConversionTBGBMBKB(Convert.ToInt64(fb)) + "\n";
                richTextBox1.Text += "磁碟剩餘空間：" + ByteConversionTBGBMBKB(Convert.ToInt64(tfb)) + "\n";
            }
            else
            {
                MessageBox.Show("NO");
            }
        }
        //取得硬碟資訊 SP

        //------------------------------------------------------------


        private void button3_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------

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
            //僅有類別, 還不會用

            IDE ide = new IDE();
        }
    }

    //讀硬盤序列號
    public class IDE
    {
        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
        internal struct IDSECTOR
        {
            public ushort wGenConfig;
            public ushort wNumCyls;
            public ushort wReserved;
            public ushort wNumHeads;
            public ushort wBytesPerTrack;
            public ushort wBytesPerSector;
            public ushort wSectorsPerTrack;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
            public ushort[] wVendorUnique;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 20)]
            public string sSerialNumber;
            public ushort wBufferType;
            public ushort wBufferSize;
            public ushort wECCSize;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 8)]
            public string sFirmwareRev;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 40)]
            public string sModelNumber;
            public ushort wMoreVendorUnique;
            public ushort wDoubleWordIO;
            public ushort wCapabilitIEs;
            public ushort wReserved1;
            public ushort wPIOTiming;
            public ushort wDMATiming;
            public ushort wBS;
            public ushort wNumCurrentCyls;
            public ushort wNumCurrentHeads;
            public ushort wNumCurrentSectorsPerTrack;
            public uint ulCurrentSectorCapacity;
            public ushort wMultSectorStuff;
            public uint ulTotalAddressableSectors;
            public ushort wSingleWordDMA;
            public ushort wMultiWordDMA;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 128)]
            public byte[] bReserved;
        }

        [StructLayout(LayoutKind.Sequential)]
        internal struct DRIVERSTATUS
        {
            public byte bDriverError;
            public byte bIDEStatus;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
            public byte[] bReserved;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
            public uint[] dwReserved;
        }

        [StructLayout(LayoutKind.Sequential)]
        internal struct SENDCMDOUTPARAMS
        {
            public uint cBufferSize;
            public DRIVERSTATUS DriverStatus;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 513)]
            public byte[] bBuffer;
        }

        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
        internal struct SRB_IO_CONTROL
        {
            public uint HeaderLength;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 8)]
            public string Signature;
            public uint Timeout;
            public uint ControlCode;
            public uint ReturnCode;
            public uint Length;
        }

        [StructLayout(LayoutKind.Sequential)]
        internal struct IDEREGS
        {
            public byte bFeaturesReg;
            public byte bSectorCountReg;
            public byte bSectorNumberReg;
            public byte bCylLowReg;
            public byte bCylHighReg;
            public byte bDriveHeadReg;
            public byte bCommandReg;
            public byte bReserved;
        }

        [StructLayout(LayoutKind.Sequential)]
        internal struct SENDCMDINPARAMS
        {
            public uint cBufferSize;
            public IDEREGS irDriveRegs;
            public byte bDriveNumber;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
            public byte[] bReserved;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
            public uint[] dwReserved;
            public byte bBuffer;
        }

        [StructLayout(LayoutKind.Sequential)]
        internal struct GETVERSIONOUTPARAMS
        {
            public byte bVersion;
            public byte bRevision;
            public byte bReserved;
            public byte bIDEDeviceMap;
            public uint fCapabilitIEs;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
            public uint[] dwReserved; // For future use.
        }

        [DllImport("kernel32.dll")]
        private static extern int CloseHandle(uint hObject);

        [DllImport("kernel32.dll")]
        private static extern int DeviceIoControl(uint hDevice,
        uint dwIoControlCode,
        ref SENDCMDINPARAMS lpInBuffer,
        int nInBufferSize,
        ref SENDCMDOUTPARAMS lpOutBuffer,
        int nOutBufferSize,
        ref uint lpbytesReturned,
        int lpOverlapped);

        [DllImport("kernel32.dll")]
        private static extern int DeviceIoControl(uint hDevice,
        uint dwIoControlCode,
        int lpInBuffer,
        int nInBufferSize,
        ref GETVERSIONOUTPARAMS lpOutBuffer,
        int nOutBufferSize,
        ref uint lpbytesReturned,
        int lpOverlapped);

        [DllImport("kernel32.dll")]
        private static extern uint CreateFile(string lpFileName,
        uint dwDesiredAccess,
        uint dwShareMode,
        int lpSecurityAttributes,
        uint dwCreationDisposition,
        uint dwFlagsAndAttributes,
        int hTemplateFile);

        private const uint GENERIC_READ = 0x80000000;
        private const uint GENERIC_WRITE = 0x40000000;
        private const uint FILE_SHARE_READ = 0x00000001;
        private const uint FILE_SHARE_WRITE = 0x00000002;
        private const uint OPEN_EXISTING = 3;
        private const uint INVALID_HANDLE_VALUE = 0xffffffff;
        private const uint DFP_GET_VERSION = 0x00074080;
        private const int IDE_ATAPI_IDENTIFY = 0xA1; // Returns ID sector for ATAPI.
        private const int IDE_ATA_IDENTIFY = 0xEC; // Returns ID sector for ATA.
        private const int IDENTIFY_BUFFER_SIZE = 512;
        private const uint DFP_RECEIVE_DRIVE_DATA = 0x0007c088;

        public static string Read(byte drive)
        {
            OperatingSystem os = Environment.OSVersion;
            if (os.Platform != PlatformID.Win32NT) throw new NotSupportedException("僅支持WindowsNT/2000/XP");
            //我沒有NT4，請哪位大大測試一下NT4下能不能用
            //if (os.Version.Major < 5) throw new NotSupportedException("僅支持WindowsNT/2000/XP");

            string driveName = "\\\\.\\PhysicalDrive" + drive.ToString();
            uint device = CreateFile(driveName,
            GENERIC_READ | GENERIC_WRITE,
            FILE_SHARE_READ | FILE_SHARE_WRITE,
            0, OPEN_EXISTING, 0, 0);
            if (device == INVALID_HANDLE_VALUE) return "";
            GETVERSIONOUTPARAMS verPara = new GETVERSIONOUTPARAMS();
            uint bytRv = 0;

            if (0 != DeviceIoControl(device, DFP_GET_VERSION,
            0, 0, ref verPara, Marshal.SizeOf(verPara),
            ref bytRv, 0))
            {
                if (verPara.bIDEDeviceMap > 0)
                {
                    byte bIDCmd = (byte)(((verPara.bIDEDeviceMap >> drive & 0x10) != 0) ? IDE_ATAPI_IDENTIFY : IDE_ATA_IDENTIFY);
                    SENDCMDINPARAMS scip = new SENDCMDINPARAMS();
                    SENDCMDOUTPARAMS scop = new SENDCMDOUTPARAMS();

                    scip.cBufferSize = IDENTIFY_BUFFER_SIZE;
                    scip.irDriveRegs.bFeaturesReg = 0;
                    scip.irDriveRegs.bSectorCountReg = 1;
                    scip.irDriveRegs.bCylLowReg = 0;
                    scip.irDriveRegs.bCylHighReg = 0;
                    scip.irDriveRegs.bDriveHeadReg = (byte)(0xA0 | ((drive & 1) << 4));
                    scip.irDriveRegs.bCommandReg = bIDCmd;
                    scip.bDriveNumber = drive;

                    if (0 != DeviceIoControl(device, DFP_RECEIVE_DRIVE_DATA,
                    ref scip, Marshal.SizeOf(scip), ref scop,
                    Marshal.SizeOf(scop), ref bytRv, 0))
                    {
                        StringBuilder s = new StringBuilder();
                        for (int i = 20; i < 40; i += 2)
                        {
                            s.Append((char)(scop.bBuffer[i + 1]));
                            s.Append((char)scop.bBuffer[i]);
                        }
                        CloseHandle(device);
                        return s.ToString().Trim();
                    }
                }
            }
            CloseHandle(device);
            return "";
        }
    }
}
