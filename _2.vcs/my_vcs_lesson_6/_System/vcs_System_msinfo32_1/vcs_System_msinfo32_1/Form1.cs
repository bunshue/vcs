using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;


/*
//下面是經常用的一些win32 的key

// 硬件 

Win32_Processor, // CPU 處理器 

Win32_PhysicalMemory, // 物理內存條 

Win32_Keyboard, // 鍵盤 

Win32_PointingDevice, // 點輸入設備，包括鼠標。 

Win32_FloppyDrive, // 軟盤驅動器 

Win32_DiskDrive, // 硬盤驅動器 

Win32_CDROMDrive, // 光盤驅動器 

Win32_BaseBoard, // 主板 

Win32_BIOS, // BIOS 芯片 

Win32_ParallelPort, // 並口 

Win32_SerialPort, // 串口 

Win32_SerialPortConfiguration, // 串口配置 

Win32_SoundDevice, // 多媒體設置，一般指聲卡。 

Win32_SystemSlot, // 主板插槽 (ISA & PCI & AGP) 

Win32_USBController, // USB 控制器 

Win32_NetworkAdapter, // 網絡適配器 

Win32_NetworkAdapterConfiguration, // 網絡適配器設置 

Win32_Printer, // 打印機 

Win32_PrinterConfiguration, // 打印機設置 

Win32_PrintJob, // 打印機任務 

Win32_TCPIPPrinterPort, // 打印機端口 

Win32_POTSModem, // MODEM 

Win32_POTSModemToSerialPort, // MODEM 端口 

Win32_DesktopMonitor, // 顯示器 

Win32_DisplayConfiguration, // 顯卡 

Win32_DisplayControllerConfiguration, // 顯卡設置 

Win32_VideoController, // 顯卡細節。 

Win32_VideoSettings, // 顯卡支持的顯示模式。 



// 操作系統 

Win32_TimeZone, // 時區 

Win32_SystemDriver, // 驅動程序 

Win32_DiskPartition, // 磁盤分區 

Win32_LogicalDisk, // 邏輯磁盤 

Win32_LogicalDiskToPartition, // 邏輯磁盤所在分區及始末位置。 

Win32_LogicalMemoryConfiguration, // 邏輯內存配置 

Win32_PageFile, // 系統頁文件信息 

Win32_PageFileSetting, // 頁文件設置 

Win32_BootConfiguration, // 系統啟動配置 

Win32_ComputerSystem, // 計算機信息簡要 

Win32_OperatingSystem, // 操作系統信息 

Win32_StartupCommand, // 系統自動啟動程序 

Win32_Service, // 系統安裝的服務 

Win32_Group, // 系統管理組 

Win32_GroupUser, // 系統組帳號 

Win32_UserAccount, // 用戶帳號 

Win32_Process, // 系統進程 

Win32_Thread, // 系統線程 

Win32_Share, // 共享 

Win32_NetworkClient, // 已安裝的網絡客戶端 

Win32_NetworkProtocol, // 已安裝的網絡協議 

*/
namespace vcs_System_msinfo32_1
{
    public partial class Form1 : Form
    {
        bool flag_isLocal = true;
        public class CPUInfoEntity
        {
            #region　屬性
            #region　CPU名稱
            string strCPUName = string.Empty;
            /// <summary>
            /// CPU名稱
            /// </summary>
            public string CPUName
            {
                get { return strCPUName; }
                set { strCPUName = value; }
            }
            #endregion

            #region　CPU序列號
            string strCPUID = string.Empty;
            /// <summary>
            /// CPU序列號
            /// </summary>
            public string CPUID
            {
                get { return strCPUID; }
                set { strCPUID = value; }
            }
            #endregion

            #region　CPU個數
            int nCPUCount = 0;
            /// <summary>
            /// CPU個數
            /// </summary>
            public int CPUCount
            {
                get { return nCPUCount; }
                set { nCPUCount = value; }
            }
            #endregion

            #region　CPU制造商
            string strCPUManufacturer = string.Empty;
            /// <summary>
            /// CPU制造商
            /// </summary>
            public string CPUManufacturer
            {
                get { return strCPUManufacturer; }
                set { strCPUManufacturer = value; }
            }
            #endregion

            #region　當前時鐘頻率
            string strCPUCurrentClockSpeed = string.Empty;
            /// <summary>
            /// 當前時鐘頻率
            /// </summary>
            public string CPUCurrentClockSpeed
            {
                get { return strCPUCurrentClockSpeed; }
                set { strCPUCurrentClockSpeed = value; }
            }
            #endregion

            #region　最大時鐘頻率
            string strCPUMaxClockSpeed = string.Empty;
            /// <summary>
            /// 最大時鐘頻率
            /// </summary>
            public string CPUMaxClockSpeed
            {
                get { return strCPUMaxClockSpeed; }
                set { strCPUMaxClockSpeed = value; }
            }
            #endregion

            #region　外部頻率
            string strCPUExtClock = string.Empty;
            /// <summary>
            /// 外部頻率
            /// </summary>
            public string CPUExtClock
            {
                get { return strCPUExtClock; }
                set { strCPUExtClock = value; }
            }
            #endregion

            #region　當前電壓
            string strCPUCurrentVoltage = string.Empty;
            /// <summary>
            /// 當前電壓
            /// </summary>
            public string CPUCurrentVoltage
            {
                get { return strCPUCurrentVoltage; }
                set { strCPUCurrentVoltage = value; }
            }
            #endregion

            #region　二級緩存
            string strCPUL2CacheSize = string.Empty;
            /// <summary>
            /// 二級緩存
            /// </summary>
            public string CPUL2CacheSize
            {
                get { return strCPUL2CacheSize; }
                set { strCPUL2CacheSize = value; }
            }
            #endregion

            #region　數據帶寬
            string strCPUDataWidth = string.Empty;
            /// <summary>
            /// 數據帶寬
            /// </summary>
            public string CPUDataWidth
            {
                get { return strCPUDataWidth; }
                set { strCPUDataWidth = value; }
            }
            #endregion

            #region　地址帶寬
            string strCPUAddressWidth = string.Empty;
            /// <summary>
            /// 地址帶寬
            /// </summary>
            public string CPUAddressWidth
            {
                get { return strCPUAddressWidth; }
                set { strCPUAddressWidth = value; }
            }
            #endregion

            #region　使用百分比
            float fCPUUsedPercent;
            /// <summary>
            /// 使用百分比
            /// </summary>
            public float CPUUsedPercent
            {
                get { return fCPUUsedPercent; }
                set { fCPUUsedPercent = value; }
            }
            #endregion

            #region　CPU溫度
            double strCPUTemperature;
            /// <summary>
            /// CPU溫度
            /// </summary>
            public double CPUTemperature
            {
                get { return strCPUTemperature; }
                set { strCPUTemperature = value; }
            }
            #endregion

            #region CPU內核
            string strNumberOfCores = "";
            /// <summary>
            /// CPU內核
            /// </summary>
            public string CPUNumberOfCores
            {
                get { return strNumberOfCores; }
                set { strNumberOfCores = value; }
            }
            #endregion

            #region CPU邏輯處理器
            string strNumberOfLogicalProcessors = "";
            /// <summary>
            /// CPU邏輯處理器
            /// </summary>
            public string CPUNumberOfLogicalProcessors
            {
                get { return strNumberOfLogicalProcessors; }
                set { strNumberOfLogicalProcessors = value; }
            }
            #endregion

            #endregion
        }

        public class SystemInfoEntity
        {
            #region　屬性
            #region　OS名稱
            string strOSName = string.Empty;　　//OS名稱
            /// <summary>
            /// OS名稱
            /// </summary>
            public string OSName
            {
                get { return strOSName; }
                set { strOSName = value; }
            }
            #endregion
            #region　OS版本
            string strOSVersion = string.Empty;　　//OS版本
            /// <summary>
            /// OS版本
            /// </summary>
            public string OSVersion
            {
                get { return strOSVersion; }
                set { strOSVersion = value; }
            }
            #endregion
            #region　OS制造商
            string strOSManufacturer = string.Empty;　　//OS制造商
            /// <summary>
            /// OS制造商
            /// </summary>
            public string OSManufacturer
            {
                get { return strOSManufacturer; }
                set { strOSManufacturer = value; }
            }
            #endregion

            #region SP包版本
            /// <summary>
            /// SP包版本
            /// </summary>
            string strOSCSDVersion = string.Empty;
            public string OSCSDVersion
            {
                get { return strOSCSDVersion; }
                set { strOSCSDVersion = value; }
            }
            #endregion

            #region //Build版本
            string str0SBuildNumber = string.Empty;
            public string OSBuildNumber
            {
                get { return str0SBuildNumber; }
                set { str0SBuildNumber = value; }
            }
            #endregion

            #region　Windows　目錄
            string strWindowsDirectory = string.Empty;
            /// <summary>
            /// Windows　目錄
            /// </summary>
            public string WindowsDirectory
            {
                get { return strWindowsDirectory; }
                set { strWindowsDirectory = value; }
            }
            #endregion
            #region　系統目錄
            string strSystemDirectory = string.Empty;　　//系統目錄
            /// <summary>
            /// 系統目錄
            /// </summary>
            public string SystemDirectory
            {
                get { return strSystemDirectory; }
                set { strSystemDirectory = value; }
            }
            #endregion
            #region　啟動設備
            string strBootDevice = string.Empty;　　//啟動設備
            /// <summary>
            /// //啟動設備
            /// </summary>
            public string BootDevice
            {
                get { return strBootDevice; }
                set { strBootDevice = value; }
            }
            #endregion
            #region　地區
            string strCountry = string.Empty;　　//地區
            /// <summary>
            /// 地區
            /// </summary>
            public string Country
            {
                get { return strCountry; }
                set { strCountry = value; }
            }
            #endregion
            #region　時區
            string strTimeZone = string.Empty;　　//時區
            /// <summary>
            /// 時區
            /// </summary>
            public string TimeZone
            {
                get { return strTimeZone; }
                set { strTimeZone = value; }
            }
            #endregion
            #region　總的物理內存
            string strTotalVisibleMemorySize = string.Empty;　　//總的物理內存
            /// <summary>
            /// 總的物理內存
            /// </summary>
            public string TotalVisibleMemorySize
            {
                get { return strTotalVisibleMemorySize; }
                set { strTotalVisibleMemorySize = value; }
            }
            #endregion
            #region　可用物理內存
            string strFreePhysicalMemory = string.Empty;　　//可用物理內存
            /// <summary>
            /// 可用物理內存
            /// </summary>
            public string FreePhysicalMemory
            {
                get { return strFreePhysicalMemory; }
                set { strFreePhysicalMemory = value; }
            }
            #endregion
            #region　總的虛擬內存
            string strTotalVirtualMemorySize = string.Empty;　　//總的虛擬內存
            /// <summary>
            /// 總的虛擬內存
            /// </summary>
            public string TotalVirtualMemorySize
            {
                get { return strTotalVirtualMemorySize; }
                set { strTotalVirtualMemorySize = value; }
            }
            #endregion
            #region　可用虛擬內存
            string strFreeVirtualMemory = string.Empty;　　//可用虛擬內存
            /// <summary>
            /// 可用虛擬內存
            /// </summary>
            public string FreeVirtualMemory
            {
                get { return strFreeVirtualMemory; }
                set { strFreeVirtualMemory = value; }
            }
            #endregion
            #region　頁面文件大小
            string strSizeStoredInPagingFiles = string.Empty;　　//頁面文件大小
            /// <summary>
            /// 頁面文件大小
            /// </summary>
            public string SizeStoredInPagingFiles
            {
                get { return strSizeStoredInPagingFiles; }
                set { strSizeStoredInPagingFiles = value; }
            }
            #endregion

            #region 可用頁面文件大小
            string strFreeSpaceInPagingFiles = string.Empty;
            /// <summary>
            /// 可用頁面文件大小
            /// </summary>
            public string FreeSpaceInPagingFiles
            {
                get { return strFreeSpaceInPagingFiles; }
                set { strFreeSpaceInPagingFiles = value; }
            }
            #endregion

            #region 頁面文件大小
            string strFileSize = string.Empty;
            /// <summary>
            /// 頁面文件大小
            /// </summary>
            public string FileSize
            {
                get { return strFileSize; }
                set { strFileSize = value; }
            }
            #endregion

            #region 頁面文件
            string strFileName = string.Empty;
            /// <summary>
            /// 頁面文件大小
            /// </summary>
            public string FileName
            {
                get { return strFileName; }
                set { strFileName = value; }
            }
            #endregion
            #endregion

        }


        //計算機系統信息
        public class ComputerInfoEntity
        {
            //系統名稱:Name
            private string strName = string.Empty;
            /// <summary>
            /// 系統名稱
            /// </summary>
            public string ComputerSystemName
            {
                get { return strName; }
                set { strName = value; }
            }
            //系統制造商:Manufacturer
            private string strManufacturer = string.Empty;
            /// <summary>
            /// 系統制造商
            /// </summary>
            public string ComputerManufacturer
            {
                get { return strManufacturer; }
                set { strManufacturer = value; }
            }

            //系統模式:Model
            private string strModel = string.Empty;
            /// <summary>
            /// 系統模式
            /// </summary>
            public string ComputerSystemModel
            {
                get { return strModel; }
                set { strModel = value; }
            }

            //系統類型:SystemType
            private string strType = string.Empty;
            /// <summary>
            /// 系統類型
            /// </summary>
            public string ComputerSystemType
            {
                get { return strType; }
                set { strType = value; }
            }
        }


        public class BIOSInfoEntity
        {

            //BIOS版本
            private string strBIOSVersion = string.Empty;
            /// <summary>
            /// BIOS版本
            /// </summary>
            public string BIOSVersion
            {
                get { return strBIOSVersion; }
                set { strBIOSVersion = value; }
            }
            //日期
            private string strBIOSReleaseDate = string.Empty;
            /// <summary>
            /// 日期
            /// </summary>
            public string BIOSReleaseDate
            {
                get { return strBIOSReleaseDate; }
                set { strBIOSReleaseDate = value; }
            }
            //SMBIOS
            private string strSMBIOS = string.Empty;
            /// <summary>
            /// SMBIOS
            /// </summary>
            public string SMBIOS
            {
                get { return strSMBIOS; }
                set { strSMBIOS = value; }
            }
        }


        public class MemoryInfoEntity
        {
            #region 總的物理內存
            string strTotalVisibleMemorySize = string.Empty;  //總的物理內存
            public string TotalVisibleMemorySize
            {
                get { return strTotalVisibleMemorySize; }
                set { strTotalVisibleMemorySize = value; }
            }
            #endregion

            #region 可用物理內存
            string strFreePhysicalMemory = string.Empty;  //可用物理內存

            public string FreePhysicalMemory
            {
                get { return strFreePhysicalMemory; }
                set { strFreePhysicalMemory = value; }
            }
            #endregion

            #region 總的虛擬內存
            string strTotalVirtualMemorySize = string.Empty;  //總的虛擬內存

            public string TotalVirtualMemorySize
            {
                get { return strTotalVirtualMemorySize; }
                set { strTotalVirtualMemorySize = value; }
            }
            #endregion

            #region 可用虛擬內存
            string strFreeVirtualMemory = string.Empty;  //可用虛擬內存

            public string FreeVirtualMemory
            {
                get { return strFreeVirtualMemory; }
                set { strFreeVirtualMemory = value; }
            }
            #endregion

            #region 頁面文件大小
            string strSizeStoredInPagingFiles = string.Empty;  //頁面文件大小

            public string SizeStoredInPagingFiles
            {
                get { return strSizeStoredInPagingFiles; }
                set { strSizeStoredInPagingFiles = value; }
            }
            #endregion

            #region 可用頁面文件大小
            string strFreeSpaceInPagingFiles = string.Empty;

            public string FreeSpaceInPagingFiles
            {
                get { return strFreeSpaceInPagingFiles; }
                set { strFreeSpaceInPagingFiles = value; }
            }
            #endregion
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }





        //獲取CPU參數
        /// <summary>
        /// 獲取CPU參數
        /// </summary>
        /// <returns></returns>
        public List<CPUInfoEntity> GetCPUInfo()
        {
            //返回值
            List<CPUInfoEntity> cpuInfoList = new List<CPUInfoEntity>();

            try
            {
                //值
                ManagementObjectCollection moCollection = null;
                //如果是本地
                if (flag_isLocal)
                {
                    ManagementClass mClass = new ManagementClass("Win32_Processor");
                    //獲取Win32_Processor這個類的所有實例
                    moCollection = mClass.GetInstances();

                }
                //表示遠程
                else
                {
                    //設定通過WMI要查詢的內容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_Processor");
                    //WQL語句，設定的WMI查詢內容和WMI的操作范圍，檢索WMI對象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //異步調用WMI查詢
                    moCollection = Searcher.Get();
                }
                //循環
                if (moCollection != null)
                {
                    //foreach,cpu可能有多個

                    foreach (ManagementObject mObject in moCollection)
                    {
                        CPUInfoEntity cpuInfo = new CPUInfoEntity();
                        cpuInfo.CPUCount = moCollection.Count;
                        cpuInfo.CPUName = mObject["Name"].ToString();　//獲取CPU名稱
                        cpuInfo.CPUID = mObject["ProcessorId"].ToString();　//獲取　CPU　ID
                        cpuInfo.CPUManufacturer = mObject["Manufacturer"].ToString();　//獲取CPU制造商
                        cpuInfo.CPUCurrentClockSpeed = mObject["CurrentClockSpeed"].ToString();　//獲取當前時鐘頻率
                        cpuInfo.CPUMaxClockSpeed = mObject["MaxClockSpeed"] == null ? string.Empty :
                            mObject["MaxClockSpeed"].ToString();　//獲取最大時鐘頻率
                        cpuInfo.CPUExtClock = mObject["ExtClock"] == null ? string.Empty :
                            mObject["ExtClock"].ToString();　//獲取外部頻率
                        cpuInfo.CPUCurrentVoltage = mObject["CurrentVoltage"] == null ? string.Empty :
                            mObject["CurrentVoltage"].ToString();　//獲取當前電壓
                        cpuInfo.CPUL2CacheSize = mObject["L2CacheSize"] == null ? string.Empty :
                            mObject["L2CacheSize"].ToString();　//獲取二級緩存
                        cpuInfo.CPUDataWidth = mObject["DataWidth"] == null ? string.Empty :
                            mObject["DataWidth"].ToString();　//獲取數據帶寬
                        cpuInfo.CPUAddressWidth = mObject["AddressWidth"] == null ? string.Empty :
                            mObject["AddressWidth"].ToString();　//獲取地址帶寬
                        cpuInfo.CPUNumberOfCores = mObject["NumberOfCores"] == null ? string.Empty :
                            mObject["NumberOfCores"].ToString(); //內核
                        cpuInfo.CPUNumberOfLogicalProcessors = mObject["NumberOfLogicalProcessors"] == null ? string.Empty :
                            mObject["NumberOfLogicalProcessors"].ToString();    //邏輯處理器
                        cpuInfo.CPUUsedPercent = mObject["LoadPercentage"] == null ? 0 : float.Parse(mObject["LoadPercentage"].ToString());
                        //加入進去
                        cpuInfoList.Add(cpuInfo);
                        //

                    }

                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
            //
            return cpuInfoList;
        }


        //獲取操作系統參數
        /// <summary>
        /// 獲取操作系統參數
        /// </summary>
        /// <returns></returns>
        public SystemInfoEntity GetSystemInfo()
        {
            //返回值
            SystemInfoEntity systemInfoList = new SystemInfoEntity();

            try
            {
                //值
                ManagementObjectCollection moCollection = null;
                //如果是本地
                if (flag_isLocal)
                {
                    ManagementClass mClass = new ManagementClass("Win32_OperatingSystem");
                    //獲取Win32_Processor這個類的所有實例
                    moCollection = mClass.GetInstances();

                }
                //表示遠程
                else
                {
                    //設定通過WMI要查詢的內容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_OperatingSystem");
                    //WQL語句，設定的WMI查詢內容和WMI的操作范圍，檢索WMI對象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //異步調用WMI查詢
                    moCollection = Searcher.Get();
                }
                //循環
                if (moCollection != null)
                {
                    //foreach

                    foreach (ManagementObject mObject in moCollection)
                    {

                        systemInfoList.OSName = mObject["Caption"].ToString();　　//獲取OS　名稱
                        systemInfoList.OSManufacturer = mObject["Manufacturer"].ToString();　　//獲取　OS　制造商
                        systemInfoList.Country = mObject["CountryCode"].ToString();　　//地區
                        systemInfoList.OSName = mObject["CSName"].ToString();　　//獲取系統名稱
                        systemInfoList.WindowsDirectory = mObject["WindowsDirectory"].ToString();　　//獲取Windows　目錄
                        systemInfoList.SystemDirectory = mObject["SystemDirectory"].ToString();　　//獲取系統目錄
                        systemInfoList.BootDevice = mObject["BootDevice"].ToString();　　//獲取啟動設備
                        systemInfoList.OSVersion = mObject["Version"].ToString();//獲取版本
                        systemInfoList.OSCSDVersion = mObject["CSDVersion"].ToString();//獲取SP
                        systemInfoList.OSBuildNumber = mObject["BuildNumber"].ToString();//獲取builderNumber
                        systemInfoList.TotalVisibleMemorySize = ((ulong)mObject["TotalVisibleMemorySize"] / 1024.0 / 1024).ToString("#0.00") + "G";　　//獲取總的物理內存
                        systemInfoList.FreePhysicalMemory = ((ulong)mObject["FreePhysicalMemory"] / 1024.0 / 1024).ToString("#0.00") + "G";　　//獲取可用物理內存
                        systemInfoList.TotalVirtualMemorySize = ((ulong)mObject["TotalVirtualMemorySize"] / 1024.0 / 1024).ToString("#0.00") + "G";　　　//獲取總的虛擬內存
                        systemInfoList.FreeVirtualMemory = ((ulong)mObject["FreeVirtualMemory"] / 1024.0 / 1024).ToString("#0.00") + "G";　　//獲取可用虛擬內存
                        systemInfoList.SizeStoredInPagingFiles = ((ulong)mObject["SizeStoredInPagingFiles"] / 1024.0 / 1024).ToString("#0.00") + "G";　　//獲取頁面文件大小


                    }

                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
            //
            return systemInfoList;
        }


        //獲取時間區域
        /// <summary>
        /// 獲取時間區域
        /// </summary>
        /// <returns></returns>
        public SystemInfoEntity GetTimeZoneInfo()
        {
            //返回值
            SystemInfoEntity systemInfoList = new SystemInfoEntity();

            try
            {
                //值
                ManagementObjectCollection moCollection = null;
                //如果是本地
                if (flag_isLocal)
                {
                    ManagementClass mClass = new ManagementClass("Win32_TimeZone");
                    //獲取Win32_Processor這個類的所有實例
                    moCollection = mClass.GetInstances();

                }
                //表示遠程
                else
                {
                    //設定通過WMI要查詢的內容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_TimeZone");
                    //WQL語句，設定的WMI查詢內容和WMI的操作范圍，檢索WMI對象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //ManagementObjectSearcher searcher = new ManagementObjectSearcher("Select SerialNumber From Win32_BIOS");

                    //異步調用WMI查詢
                    moCollection = Searcher.Get();
                }
                //循環
                if (moCollection != null)
                {
                    //foreach

                    foreach (ManagementObject mObject in moCollection)
                    {

                        systemInfoList.OSName = mObject["StandardName"].ToString();　　//時區


                    }

                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
            //
            return systemInfoList;
        }

        //獲取頁面文件
        /// <summary>
        /// 獲取頁面文件
        /// </summary>
        /// <returns></returns>
        public SystemInfoEntity GetPageFileInfo()
        {
            //返回值
            SystemInfoEntity systemInfoList = new SystemInfoEntity();

            try
            {
                //值
                ManagementObjectCollection moCollection = null;
                //如果是本地
                if (flag_isLocal)
                {
                    ManagementClass mClass = new ManagementClass("Win32_PageFile");
                    //獲取Win32_Processor這個類的所有實例
                    moCollection = mClass.GetInstances();

                }
                //表示遠程
                else
                {
                    //設定通過WMI要查詢的內容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_PageFile");
                    //WQL語句，設定的WMI查詢內容和WMI的操作范圍，檢索WMI對象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //異步調用WMI查詢
                    moCollection = Searcher.Get();
                }
                //循環
                if (moCollection != null)
                {
                    //foreach

                    foreach (ManagementObject mObject in moCollection)
                    {

                        long FileSize = mObject["FileSize"] == null ?
                            0 : long.Parse(mObject["FileSize"].ToString());//頁面文件大小
                        //計算
                        systemInfoList.FileSize = (FileSize / 1024 / 1024).ToString("#0.00") + "G";
                        systemInfoList.FileName = mObject["Name"].ToString();　　//頁面文件

                    }

                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
            //
            return systemInfoList;
        }

        //獲取BIOS信息
        /// <summary>
        /// 獲取BIOS信息
        /// </summary>
        /// <returns></returns>
        public BIOSInfoEntity GetBIOSInfo()
        {
            //返回值
            BIOSInfoEntity BIOSInfoList = new BIOSInfoEntity();

            try
            {
                //值
                ManagementObjectCollection moCollection = null;
                //如果是本地
                if (flag_isLocal)
                {
                    ManagementClass mClass = new ManagementClass("Win32_BIOS");
                    //獲取Win32_Processor這個類的所有實例
                    moCollection = mClass.GetInstances();

                }
                //表示遠程
                else
                {
                    //設定通過WMI要查詢的內容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_BIOS");
                    //WQL語句，設定的WMI查詢內容和WMI的操作范圍，檢索WMI對象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //異步調用WMI查詢
                    moCollection = Searcher.Get();
                }
                //循環
                if (moCollection != null)
                {
                    //foreach

                    foreach (ManagementObject mObject in moCollection)
                    {
                        BIOSInfoList.BIOSReleaseDate = mObject["ReleaseDate"] == null ? string.Empty :
                           getDateTimeFromDmtfDate(mObject["ReleaseDate"].ToString());　　//時間

                        BIOSInfoList.BIOSVersion = mObject["Manufacturer"].ToString();　　//Manufacturer

                        BIOSInfoList.SMBIOS = mObject["SMBIOSBIOSVersion"].ToString();　　//SMBIOSBIOSVersion
                    }

                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
            //
            return BIOSInfoList;
        }

        private static string getDmtfFromDateTime(DateTime dateTime)
        {
            return ManagementDateTimeConverter.ToDmtfDateTime(dateTime);
        }

        private static string getDmtfFromDateTime(string dateTime)
        {
            DateTime dateTimeValue = Convert.ToDateTime(dateTime);
            return getDmtfFromDateTime(dateTimeValue);
        }

        private static string getDateTimeFromDmtfDate(string dateTime)
        {
            return ManagementDateTimeConverter.ToDateTime(dateTime).ToString();
        }



        //獲取計算機信息
        /// <summary>
        /// 獲取計算機信息
        /// </summary>
        /// <returns></returns>
        public ComputerInfoEntity GetComputerInfo()
        {
            //返回值
            ComputerInfoEntity ComputerInfoList = new ComputerInfoEntity();

            try
            {
                //值
                ManagementObjectCollection moCollection = null;
                //如果是本地
                if (flag_isLocal)
                {
                    ManagementClass mClass = new ManagementClass("Win32_ComputerSystem");
                    //獲取Win32_Processor這個類的所有實例
                    moCollection = mClass.GetInstances();

                }
                //表示遠程
                else
                {
                    //設定通過WMI要查詢的內容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_ComputerSystem");
                    //WQL語句，設定的WMI查詢內容和WMI的操作范圍，檢索WMI對象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //異步調用WMI查詢
                    moCollection = Searcher.Get();
                }
                //循環
                if (moCollection != null)
                {

                    //foreach
                    foreach (ManagementObject mObject in moCollection)
                    {

                        ComputerInfoList.ComputerSystemName = mObject["Name"].ToString();//系統名稱
                        ComputerInfoList.ComputerManufacturer = mObject["Manufacturer"].ToString();//系統制造商
                        ComputerInfoList.ComputerSystemModel = mObject["Model"].ToString();//系統模式
                        ComputerInfoList.ComputerSystemType = mObject["SystemType"].ToString();//系統類型


                    }

                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
            //
            return ComputerInfoList;
        }




    }
}
