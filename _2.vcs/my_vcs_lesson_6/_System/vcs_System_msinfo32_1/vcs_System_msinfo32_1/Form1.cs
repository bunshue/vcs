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
//下面是经常用的一些win32 的key

// 硬件 

Win32_Processor, // CPU 处理器 

Win32_PhysicalMemory, // 物理内存条 

Win32_Keyboard, // 键盘 

Win32_PointingDevice, // 点输入设备，包括鼠标。 

Win32_FloppyDrive, // 软盘驱动器 

Win32_DiskDrive, // 硬盘驱动器 

Win32_CDROMDrive, // 光盘驱动器 

Win32_BaseBoard, // 主板 

Win32_BIOS, // BIOS 芯片 

Win32_ParallelPort, // 并口 

Win32_SerialPort, // 串口 

Win32_SerialPortConfiguration, // 串口配置 

Win32_SoundDevice, // 多媒体设置，一般指声卡。 

Win32_SystemSlot, // 主板插槽 (ISA & PCI & AGP) 

Win32_USBController, // USB 控制器 

Win32_NetworkAdapter, // 网络适配器 

Win32_NetworkAdapterConfiguration, // 网络适配器设置 

Win32_Printer, // 打印机 

Win32_PrinterConfiguration, // 打印机设置 

Win32_PrintJob, // 打印机任务 

Win32_TCPIPPrinterPort, // 打印机端口 

Win32_POTSModem, // MODEM 

Win32_POTSModemToSerialPort, // MODEM 端口 

Win32_DesktopMonitor, // 显示器 

Win32_DisplayConfiguration, // 显卡 

Win32_DisplayControllerConfiguration, // 显卡设置 

Win32_VideoController, // 显卡细节。 

Win32_VideoSettings, // 显卡支持的显示模式。 



// 操作系统 

Win32_TimeZone, // 时区 

Win32_SystemDriver, // 驱动程序 

Win32_DiskPartition, // 磁盘分区 

Win32_LogicalDisk, // 逻辑磁盘 

Win32_LogicalDiskToPartition, // 逻辑磁盘所在分区及始末位置。 

Win32_LogicalMemoryConfiguration, // 逻辑内存配置 

Win32_PageFile, // 系统页文件信息 

Win32_PageFileSetting, // 页文件设置 

Win32_BootConfiguration, // 系统启动配置 

Win32_ComputerSystem, // 计算机信息简要 

Win32_OperatingSystem, // 操作系统信息 

Win32_StartupCommand, // 系统自动启动程序 

Win32_Service, // 系统安装的服务 

Win32_Group, // 系统管理组 

Win32_GroupUser, // 系统组帐号 

Win32_UserAccount, // 用户帐号 

Win32_Process, // 系统进程 

Win32_Thread, // 系统线程 

Win32_Share, // 共享 

Win32_NetworkClient, // 已安装的网络客户端 

Win32_NetworkProtocol, // 已安装的网络协议 

*/
namespace vcs_System_msinfo32_1
{
    public partial class Form1 : Form
    {
        bool flag_isLocal = true;
        public class CPUInfoEntity
        {
            #region　属性
            #region　CPU名称
            string strCPUName = string.Empty;
            /// <summary>
            /// CPU名称
            /// </summary>
            public string CPUName
            {
                get { return strCPUName; }
                set { strCPUName = value; }
            }
            #endregion

            #region　CPU序列号
            string strCPUID = string.Empty;
            /// <summary>
            /// CPU序列号
            /// </summary>
            public string CPUID
            {
                get { return strCPUID; }
                set { strCPUID = value; }
            }
            #endregion

            #region　CPU个数
            int nCPUCount = 0;
            /// <summary>
            /// CPU个数
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

            #region　当前时钟频率
            string strCPUCurrentClockSpeed = string.Empty;
            /// <summary>
            /// 当前时钟频率
            /// </summary>
            public string CPUCurrentClockSpeed
            {
                get { return strCPUCurrentClockSpeed; }
                set { strCPUCurrentClockSpeed = value; }
            }
            #endregion

            #region　最大时钟频率
            string strCPUMaxClockSpeed = string.Empty;
            /// <summary>
            /// 最大时钟频率
            /// </summary>
            public string CPUMaxClockSpeed
            {
                get { return strCPUMaxClockSpeed; }
                set { strCPUMaxClockSpeed = value; }
            }
            #endregion

            #region　外部频率
            string strCPUExtClock = string.Empty;
            /// <summary>
            /// 外部频率
            /// </summary>
            public string CPUExtClock
            {
                get { return strCPUExtClock; }
                set { strCPUExtClock = value; }
            }
            #endregion

            #region　当前电压
            string strCPUCurrentVoltage = string.Empty;
            /// <summary>
            /// 当前电压
            /// </summary>
            public string CPUCurrentVoltage
            {
                get { return strCPUCurrentVoltage; }
                set { strCPUCurrentVoltage = value; }
            }
            #endregion

            #region　二级缓存
            string strCPUL2CacheSize = string.Empty;
            /// <summary>
            /// 二级缓存
            /// </summary>
            public string CPUL2CacheSize
            {
                get { return strCPUL2CacheSize; }
                set { strCPUL2CacheSize = value; }
            }
            #endregion

            #region　数据带宽
            string strCPUDataWidth = string.Empty;
            /// <summary>
            /// 数据带宽
            /// </summary>
            public string CPUDataWidth
            {
                get { return strCPUDataWidth; }
                set { strCPUDataWidth = value; }
            }
            #endregion

            #region　地址带宽
            string strCPUAddressWidth = string.Empty;
            /// <summary>
            /// 地址带宽
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

            #region　CPU温度
            double strCPUTemperature;
            /// <summary>
            /// CPU温度
            /// </summary>
            public double CPUTemperature
            {
                get { return strCPUTemperature; }
                set { strCPUTemperature = value; }
            }
            #endregion

            #region CPU内核
            string strNumberOfCores = "";
            /// <summary>
            /// CPU内核
            /// </summary>
            public string CPUNumberOfCores
            {
                get { return strNumberOfCores; }
                set { strNumberOfCores = value; }
            }
            #endregion

            #region CPU逻辑处理器
            string strNumberOfLogicalProcessors = "";
            /// <summary>
            /// CPU逻辑处理器
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
            #region　属性
            #region　OS名称
            string strOSName = string.Empty;　　//OS名称
            /// <summary>
            /// OS名称
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

            #region　Windows　目录
            string strWindowsDirectory = string.Empty;
            /// <summary>
            /// Windows　目录
            /// </summary>
            public string WindowsDirectory
            {
                get { return strWindowsDirectory; }
                set { strWindowsDirectory = value; }
            }
            #endregion
            #region　系统目录
            string strSystemDirectory = string.Empty;　　//系统目录
            /// <summary>
            /// 系统目录
            /// </summary>
            public string SystemDirectory
            {
                get { return strSystemDirectory; }
                set { strSystemDirectory = value; }
            }
            #endregion
            #region　启动设备
            string strBootDevice = string.Empty;　　//启动设备
            /// <summary>
            /// //启动设备
            /// </summary>
            public string BootDevice
            {
                get { return strBootDevice; }
                set { strBootDevice = value; }
            }
            #endregion
            #region　地区
            string strCountry = string.Empty;　　//地区
            /// <summary>
            /// 地区
            /// </summary>
            public string Country
            {
                get { return strCountry; }
                set { strCountry = value; }
            }
            #endregion
            #region　时区
            string strTimeZone = string.Empty;　　//时区
            /// <summary>
            /// 时区
            /// </summary>
            public string TimeZone
            {
                get { return strTimeZone; }
                set { strTimeZone = value; }
            }
            #endregion
            #region　总的物理内存
            string strTotalVisibleMemorySize = string.Empty;　　//总的物理内存
            /// <summary>
            /// 总的物理内存
            /// </summary>
            public string TotalVisibleMemorySize
            {
                get { return strTotalVisibleMemorySize; }
                set { strTotalVisibleMemorySize = value; }
            }
            #endregion
            #region　可用物理内存
            string strFreePhysicalMemory = string.Empty;　　//可用物理内存
            /// <summary>
            /// 可用物理内存
            /// </summary>
            public string FreePhysicalMemory
            {
                get { return strFreePhysicalMemory; }
                set { strFreePhysicalMemory = value; }
            }
            #endregion
            #region　总的虚拟内存
            string strTotalVirtualMemorySize = string.Empty;　　//总的虚拟内存
            /// <summary>
            /// 总的虚拟内存
            /// </summary>
            public string TotalVirtualMemorySize
            {
                get { return strTotalVirtualMemorySize; }
                set { strTotalVirtualMemorySize = value; }
            }
            #endregion
            #region　可用虚拟内存
            string strFreeVirtualMemory = string.Empty;　　//可用虚拟内存
            /// <summary>
            /// 可用虚拟内存
            /// </summary>
            public string FreeVirtualMemory
            {
                get { return strFreeVirtualMemory; }
                set { strFreeVirtualMemory = value; }
            }
            #endregion
            #region　页面文件大小
            string strSizeStoredInPagingFiles = string.Empty;　　//页面文件大小
            /// <summary>
            /// 页面文件大小
            /// </summary>
            public string SizeStoredInPagingFiles
            {
                get { return strSizeStoredInPagingFiles; }
                set { strSizeStoredInPagingFiles = value; }
            }
            #endregion

            #region 可用页面文件大小
            string strFreeSpaceInPagingFiles = string.Empty;
            /// <summary>
            /// 可用页面文件大小
            /// </summary>
            public string FreeSpaceInPagingFiles
            {
                get { return strFreeSpaceInPagingFiles; }
                set { strFreeSpaceInPagingFiles = value; }
            }
            #endregion

            #region 页面文件大小
            string strFileSize = string.Empty;
            /// <summary>
            /// 页面文件大小
            /// </summary>
            public string FileSize
            {
                get { return strFileSize; }
                set { strFileSize = value; }
            }
            #endregion

            #region 页面文件
            string strFileName = string.Empty;
            /// <summary>
            /// 页面文件大小
            /// </summary>
            public string FileName
            {
                get { return strFileName; }
                set { strFileName = value; }
            }
            #endregion
            #endregion

        }


        public class ComputerInfoEntity
        {
            //系统名称:Name
            private string strName = string.Empty;
            /// <summary>
            /// 系统名称
            /// </summary>
            public string ComputerSystemName
            {
                get { return strName; }
                set { strName = value; }
            }
            //系统制造商:Manufacturer
            private string strManufacturer = string.Empty;
            /// <summary>
            /// 系统制造商
            /// </summary>
            public string ComputerManufacturer
            {
                get { return strManufacturer; }
                set { strManufacturer = value; }
            }

            //系统模式:Model
            private string strModel = string.Empty;
            /// <summary>
            /// 系统模式
            /// </summary>
            public string ComputerSystemModel
            {
                get { return strModel; }
                set { strModel = value; }
            }

            //系统类型:SystemType
            private string strType = string.Empty;
            /// <summary>
            /// 系统类型
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
            #region 总的物理内存
            string strTotalVisibleMemorySize = string.Empty;  //总的物理内存
            public string TotalVisibleMemorySize
            {
                get { return strTotalVisibleMemorySize; }
                set { strTotalVisibleMemorySize = value; }
            }
            #endregion

            #region 可用物理内存
            string strFreePhysicalMemory = string.Empty;  //可用物理内存

            public string FreePhysicalMemory
            {
                get { return strFreePhysicalMemory; }
                set { strFreePhysicalMemory = value; }
            }
            #endregion

            #region 总的虚拟内存
            string strTotalVirtualMemorySize = string.Empty;  //总的虚拟内存

            public string TotalVirtualMemorySize
            {
                get { return strTotalVirtualMemorySize; }
                set { strTotalVirtualMemorySize = value; }
            }
            #endregion

            #region 可用虚拟内存
            string strFreeVirtualMemory = string.Empty;  //可用虚拟内存

            public string FreeVirtualMemory
            {
                get { return strFreeVirtualMemory; }
                set { strFreeVirtualMemory = value; }
            }
            #endregion

            #region 页面文件大小
            string strSizeStoredInPagingFiles = string.Empty;  //页面文件大小

            public string SizeStoredInPagingFiles
            {
                get { return strSizeStoredInPagingFiles; }
                set { strSizeStoredInPagingFiles = value; }
            }
            #endregion

            #region 可用页面文件大小
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





        //获取CPU参数
        /// <summary>
        /// 获取CPU参数
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
                    //获取Win32_Processor这个类的所有实例
                    moCollection = mClass.GetInstances();

                }
                //表示远程
                else
                {
                    //设定通过WMI要查询的内容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_Processor");
                    //WQL语句，设定的WMI查询内容和WMI的操作范围，检索WMI对象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //异步调用WMI查询
                    moCollection = Searcher.Get();
                }
                //循环
                if (moCollection != null)
                {
                    //foreach,cpu可能有多个

                    foreach (ManagementObject mObject in moCollection)
                    {
                        CPUInfoEntity cpuInfo = new CPUInfoEntity();
                        cpuInfo.CPUCount = moCollection.Count;
                        cpuInfo.CPUName = mObject["Name"].ToString();　//获取CPU名称
                        cpuInfo.CPUID = mObject["ProcessorId"].ToString();　//获取　CPU　ID
                        cpuInfo.CPUManufacturer = mObject["Manufacturer"].ToString();　//获取CPU制造商
                        cpuInfo.CPUCurrentClockSpeed = mObject["CurrentClockSpeed"].ToString();　//获取当前时钟频率
                        cpuInfo.CPUMaxClockSpeed = mObject["MaxClockSpeed"] == null ? string.Empty :
                            mObject["MaxClockSpeed"].ToString();　//获取最大时钟频率
                        cpuInfo.CPUExtClock = mObject["ExtClock"] == null ? string.Empty :
                            mObject["ExtClock"].ToString();　//获取外部频率
                        cpuInfo.CPUCurrentVoltage = mObject["CurrentVoltage"] == null ? string.Empty :
                            mObject["CurrentVoltage"].ToString();　//获取当前电压
                        cpuInfo.CPUL2CacheSize = mObject["L2CacheSize"] == null ? string.Empty :
                            mObject["L2CacheSize"].ToString();　//获取二级缓存
                        cpuInfo.CPUDataWidth = mObject["DataWidth"] == null ? string.Empty :
                            mObject["DataWidth"].ToString();　//获取数据带宽
                        cpuInfo.CPUAddressWidth = mObject["AddressWidth"] == null ? string.Empty :
                            mObject["AddressWidth"].ToString();　//获取地址带宽
                        cpuInfo.CPUNumberOfCores = mObject["NumberOfCores"] == null ? string.Empty :
                            mObject["NumberOfCores"].ToString(); //内核
                        cpuInfo.CPUNumberOfLogicalProcessors = mObject["NumberOfLogicalProcessors"] == null ? string.Empty :
                            mObject["NumberOfLogicalProcessors"].ToString();    //逻辑处理器
                        cpuInfo.CPUUsedPercent = mObject["LoadPercentage"] == null ? 0 : float.Parse(mObject["LoadPercentage"].ToString());
                        //加入进去
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


        //获取操作系统参数
        /// <summary>
        /// 获取操作系统参数
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
                    //获取Win32_Processor这个类的所有实例
                    moCollection = mClass.GetInstances();

                }
                //表示远程
                else
                {
                    //设定通过WMI要查询的内容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_OperatingSystem");
                    //WQL语句，设定的WMI查询内容和WMI的操作范围，检索WMI对象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //异步调用WMI查询
                    moCollection = Searcher.Get();
                }
                //循环
                if (moCollection != null)
                {
                    //foreach

                    foreach (ManagementObject mObject in moCollection)
                    {

                        systemInfoList.OSName = mObject["Caption"].ToString();　　//获取OS　名称
                        systemInfoList.OSManufacturer = mObject["Manufacturer"].ToString();　　//获取　OS　制造商
                        systemInfoList.Country = mObject["CountryCode"].ToString();　　//地区
                        systemInfoList.OSName = mObject["CSName"].ToString();　　//获取系统名称
                        systemInfoList.WindowsDirectory = mObject["WindowsDirectory"].ToString();　　//获取Windows　目录
                        systemInfoList.SystemDirectory = mObject["SystemDirectory"].ToString();　　//获取系统目录
                        systemInfoList.BootDevice = mObject["BootDevice"].ToString();　　//获取启动设备
                        systemInfoList.OSVersion = mObject["Version"].ToString();//获取版本
                        systemInfoList.OSCSDVersion = mObject["CSDVersion"].ToString();//获取SP
                        systemInfoList.OSBuildNumber = mObject["BuildNumber"].ToString();//获取builderNumber
                        systemInfoList.TotalVisibleMemorySize = ((ulong)mObject["TotalVisibleMemorySize"] / 1024.0 / 1024).ToString("#0.00") + "G";　　//获取总的物理内存
                        systemInfoList.FreePhysicalMemory = ((ulong)mObject["FreePhysicalMemory"] / 1024.0 / 1024).ToString("#0.00") + "G";　　//获取可用物理内存
                        systemInfoList.TotalVirtualMemorySize = ((ulong)mObject["TotalVirtualMemorySize"] / 1024.0 / 1024).ToString("#0.00") + "G";　　　//获取总的虚拟内存
                        systemInfoList.FreeVirtualMemory = ((ulong)mObject["FreeVirtualMemory"] / 1024.0 / 1024).ToString("#0.00") + "G";　　//获取可用虚拟内存
                        systemInfoList.SizeStoredInPagingFiles = ((ulong)mObject["SizeStoredInPagingFiles"] / 1024.0 / 1024).ToString("#0.00") + "G";　　//获取页面文件大小


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


        //获取时间区域
        /// <summary>
        /// 获取时间区域
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
                    //获取Win32_Processor这个类的所有实例
                    moCollection = mClass.GetInstances();

                }
                //表示远程
                else
                {
                    //设定通过WMI要查询的内容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_TimeZone");
                    //WQL语句，设定的WMI查询内容和WMI的操作范围，检索WMI对象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //ManagementObjectSearcher searcher = new ManagementObjectSearcher("Select SerialNumber From Win32_BIOS");

                    //异步调用WMI查询
                    moCollection = Searcher.Get();
                }
                //循环
                if (moCollection != null)
                {
                    //foreach

                    foreach (ManagementObject mObject in moCollection)
                    {

                        systemInfoList.OSName = mObject["StandardName"].ToString();　　//时区


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

        //获取页面文件
        /// <summary>
        /// 获取页面文件
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
                    //获取Win32_Processor这个类的所有实例
                    moCollection = mClass.GetInstances();

                }
                //表示远程
                else
                {
                    //设定通过WMI要查询的内容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_PageFile");
                    //WQL语句，设定的WMI查询内容和WMI的操作范围，检索WMI对象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //异步调用WMI查询
                    moCollection = Searcher.Get();
                }
                //循环
                if (moCollection != null)
                {
                    //foreach

                    foreach (ManagementObject mObject in moCollection)
                    {

                        long FileSize = mObject["FileSize"] == null ?
                            0 : long.Parse(mObject["FileSize"].ToString());//页面文件大小
                        //计算
                        systemInfoList.FileSize = (FileSize / 1024 / 1024).ToString("#0.00") + "G";
                        systemInfoList.FileName = mObject["Name"].ToString();　　//页面文件

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

        //获取BIOS信息
        /// <summary>
        /// 获取BIOS信息
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
                    //获取Win32_Processor这个类的所有实例
                    moCollection = mClass.GetInstances();

                }
                //表示远程
                else
                {
                    //设定通过WMI要查询的内容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_BIOS");
                    //WQL语句，设定的WMI查询内容和WMI的操作范围，检索WMI对象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //异步调用WMI查询
                    moCollection = Searcher.Get();
                }
                //循环
                if (moCollection != null)
                {
                    //foreach

                    foreach (ManagementObject mObject in moCollection)
                    {
                        BIOSInfoList.BIOSReleaseDate = mObject["ReleaseDate"] == null ? string.Empty :
                           getDateTimeFromDmtfDate(mObject["ReleaseDate"].ToString());　　//时间

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
        


        //获取计算机信息
        /// <summary>
        /// 获取计算机信息
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
                    //获取Win32_Processor这个类的所有实例
                    moCollection = mClass.GetInstances();

                }
                //表示远程
                else
                {
                    //设定通过WMI要查询的内容
                    ObjectQuery Query = new ObjectQuery("select * from Win32_ComputerSystem");
                    //WQL语句，设定的WMI查询内容和WMI的操作范围，检索WMI对象集合
                    ManagementObjectSearcher Searcher = new ManagementObjectSearcher(Query);
                    //异步调用WMI查询
                    moCollection = Searcher.Get();
                }
                //循环
                if (moCollection != null)
                {

                    //foreach
                    foreach (ManagementObject mObject in moCollection)
                    {

                        ComputerInfoList.ComputerSystemName = mObject["Name"].ToString();//系统名称
                        ComputerInfoList.ComputerManufacturer = mObject["Manufacturer"].ToString();//系统制造商
                        ComputerInfoList.ComputerSystemModel = mObject["Model"].ToString();//系统模式
                        ComputerInfoList.ComputerSystemType = mObject["SystemType"].ToString();//系统类型


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
