using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for MarshalAs

namespace vcs_VideoResolution
{
    public partial class Form1 : Form
    {
        // 映照 DEVMODE 構造
        // 可以參照 DEVMODE構造的指針界說：
        // http://msdn.microsoft.com/en-us/library/windows/desktop/dd183565(v=vs.85).aspx
        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
        public struct DEVMODE
        {
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 32)]
            public string dmDeviceName;

            public short dmSpecVersion;
            public short dmDriverVersion;
            public short dmSize;
            public short dmDriverExtra;
            public int dmFields;
            public int dmPositionX;
            public int dmPositionY;
            public int dmDisplayOrientation;
            public int dmDisplayFixedOutput;
            public short dmColor;
            public short dmDuplex;
            public short dmYResolution;
            public short dmTTOption;
            public short dmCollate;

            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 32)]
            public string dmFormName;

            public short dmLogPixels;
            public short dmBitsPerPel;
            public int dmPelsWidth;
            public int dmPelsHeight;
            public int dmDisplayFlags;
            public int dmDisplayFrequency;
            public int dmICMMethod;
            public int dmICMIntent;
            public int dmMediaType;
            public int dmDitherType;
            public int dmReserved1;
            public int dmReserved2;
            public int dmPanningWidth;
            public int dmPanningHeight;
        };

        // Win32 函數在托管情況下的聲明


        public class NativeMethods
        {
            // 平台挪用的聲名
            [DllImport("user32.dll")]
            public static extern int EnumDisplaySettings(
             string deviceName, int modeNum, ref DEVMODE devMode);
            [DllImport("user32.dll")]
            public static extern int ChangeDisplaySettings(
               ref DEVMODE devMode, int flags);

            // 掌握轉變屏幕分辯率的常量
            public const int ENUM_CURRENT_SETTINGS = -1;
            public const int CDS_UPDATEREGISTRY = 0x01;
            public const int CDS_TEST = 0x02;
            public const int DISP_CHANGE_SUCCESSFUL = 0;
            public const int DISP_CHANGE_RESTART = 1;
            public const int DISP_CHANGE_FAILED = -1;

            // 掌握轉變偏向的常量界說
            public const int DMDO_DEFAULT = 0;
            public const int DMDO_90 = 1;
            public const int DMDO_180 = 2;
            public const int DMDO_270 = 3;
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
            //取得目前的螢幕解析度
            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.AppendText("目前螢幕解析度 : " + W.ToString() + " X " + H.ToString() + "\n");

        }

        // 轉變分辯率
        public void ChangeResolution(int width, int height)
        {
            // 初始化 DEVMODE構造
            DEVMODE devmode = new DEVMODE();
            devmode.dmDeviceName = new String(new char[32]);
            devmode.dmFormName = new String(new char[32]);
            devmode.dmSize = (short)Marshal.SizeOf(devmode);

            if (0 != NativeMethods.EnumDisplaySettings(null, NativeMethods.ENUM_CURRENT_SETTINGS, ref devmode))
            {
                devmode.dmPelsWidth = width;
                devmode.dmPelsHeight = height;

                // 轉變屏幕分辯率
                int iRet = NativeMethods.ChangeDisplaySettings(ref devmode, NativeMethods.CDS_TEST);

                if (iRet == NativeMethods.DISP_CHANGE_FAILED)
                {
                    MessageBox.Show("不克不及履行你的要求", "信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                else
                {
                    iRet = NativeMethods.ChangeDisplaySettings(ref devmode, NativeMethods.CDS_UPDATEREGISTRY);

                    switch (iRet)
                    {
                        // 勝利轉變
                        case NativeMethods.DISP_CHANGE_SUCCESSFUL:
                            {
                                break;
                            }
                        case NativeMethods.DISP_CHANGE_RESTART:
                            {
                                MessageBox.Show("你須要從新啟動電腦設置能力失效", "信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
                                break;
                            }
                        default:
                            {
                                MessageBox.Show("轉變屏幕分辯率掉敗", "信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
                                break;
                            }
                    }
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //設定螢幕解析度1366 X 768
            int w = 1366;
            int h = 768;
            ChangeResolution(w, h);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //設定螢幕解析度1920 X 1080
            int w = 1920;
            int h = 1080;
            ChangeResolution(w, h);
        }
    }
}
