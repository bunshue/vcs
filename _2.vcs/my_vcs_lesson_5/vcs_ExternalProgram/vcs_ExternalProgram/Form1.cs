using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//開啟外部程式並內嵌至表單中
//將程序窗口嵌入到任務欄中

using System.Diagnostics;
using System.Runtime.InteropServices;

namespace vcs_ExternalProgram
{
    public partial class Form1 : Form
    {
        Panel panel1 = new Panel();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            panel1.Location = new Point(200, 10);
            panel1.Size = new Size(300, 400);
            //panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            Controls.Add(this.panel1);

            //通過 WIN32 API 實現嵌入程序窗體，win32api

            //string sPath = Environment.GetEnvironmentVariable("windir");//獲取系統變量 windir(windows)    
            const string exe_filename = "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe";
            InsertWindow insertwin = new InsertWindow(panel1, exe_filename);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //想做一個開啟pdf的, 目前無法指名檔案
            const string exe_filename = @"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe";
            string filename = @"C:\______test_files1\__RW\_pdf\note_Linux_workstation.pdf";

            panel1.Location = new Point(200, 10);
            panel1.Size = new Size(300, 400);
            //panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            Controls.Add(this.panel1);

            //通過 WIN32 API 實現嵌入程序窗體，win32api

            //string sPath = Environment.GetEnvironmentVariable("windir");//獲取系統變量 windir(windows)    
            //InsertWindow insertwin = new InsertWindow(panel1, exe_filename + " " + filename);
            InsertWindow insertwin = new InsertWindow(panel1, exe_filename);
        }
    }

    class InsertWindow
    {
        /// <summary>  
        /// 將程序嵌入窗體  
        /// </summary>  
        /// <param name="pW">容器</param>  
        /// <param name="appname">程序名</param>  
        public InsertWindow(Panel pW, string exe_filename)
        {
            this.pan = pW;
            this.LoadEvent(exe_filename);
            pane();
        }

        ~InsertWindow()
        {
            if (process != null)
            {
                process.Dispose();
            }
        }

        #region  函數和變量聲明
        /* 
            * 聲明 Win32 API 
            */

        [DllImport("user32.dll")]
        static extern IntPtr SetParent(IntPtr hWndChild, IntPtr hWndNewParent);

        [DllImport("user32.dll")]
        static extern Int32 GetWindowLong(IntPtr hWnd, Int32 nIndex);

        [DllImport("user32.dll")]
        static extern Int32 SetWindowLong(IntPtr hWnd, Int32 nIndex, Int32 dwNewLong);

        [DllImport("user32.dll")]
        static extern Int32 SetWindowPos(IntPtr hWnd,
            IntPtr hWndInsertAfter,
            Int32 X,
            Int32 Y,
            Int32 cx,
            Int32 cy,
            UInt32 uFlags
        );

        /* 
         * 定義 Win32 常數 
         */
        const Int32 GWL_STYLE = -16;
        const Int32 WS_BORDER = (Int32)0x00800000L;
        const Int32 WS_THICKFRAME = (Int32)0x00040000L;

        const Int32 SWP_NOMOVE = 0x0002;
        const Int32 SWP_NOSIZE = 0x0001;
        const Int32 SWP_NOZORDER = 0x0004;
        const Int32 SWP_FRAMECHANGED = 0x0020;

        const Int32 SW_MAXIMIZE = 3;
        IntPtr HWND_NOTOPMOST = new IntPtr(-2);

        // 目標應用程序的進程.  
        Process process = null;
        #endregion

        #region  容器
        private Panel pan = null;
        public Panel panel1
        {
            set { pan = value; }
            get { return pan; }
        }
        private void pane()
        {
            panel1.Anchor = AnchorStyles.Left | AnchorStyles.Top | AnchorStyles.Right | AnchorStyles.Bottom;
            panel1.Resize += new EventHandler(panel1_Resize);
        }
        private void panel1_Resize(object sender, EventArgs e)
        {
            // 設置目標應用程序的窗體樣式.  

            IntPtr innerWnd = process.MainWindowHandle;
            SetWindowPos(innerWnd, IntPtr.Zero, 0, 0, panel1.ClientSize.Width, panel1.ClientSize.Height, SWP_NOZORDER);
        }
        #endregion

        #region  相應事件
        private void LoadEvent(string exe_filename)
        {
            // 啟動目標應用程序.  
            process = Process.Start(exe_filename);
            process.StartInfo.WindowStyle = ProcessWindowStyle.Hidden; //隱藏  
            // 等待, 直到那個程序已經完全啟動.   
            process.WaitForInputIdle();

            // 目標應用程序的主窗體.  
            IntPtr innerWnd = process.MainWindowHandle;

            // 設置目標應用程序的主窗體的父親(為我們的窗體).  
            SetParent(innerWnd, panel1.Handle);

            // 除去窗體邊框.  
            Int32 wndStyle = GetWindowLong(innerWnd, GWL_STYLE);
            wndStyle &= ~WS_BORDER;
            wndStyle &= ~WS_THICKFRAME;
            SetWindowLong(innerWnd, GWL_STYLE, wndStyle);
            SetWindowPos(innerWnd, IntPtr.Zero, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOZORDER | SWP_FRAMECHANGED);

            // 在Resize事件中更新目標應用程序的窗體尺寸.  
            panel1_Resize(panel1, null);
        }
        #endregion
    }
}

