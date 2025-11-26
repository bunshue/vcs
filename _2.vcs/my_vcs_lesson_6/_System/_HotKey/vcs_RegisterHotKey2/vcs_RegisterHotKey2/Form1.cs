using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                //for Directory
using System.Runtime.InteropServices;   //for dll

namespace vcs_RegisterHotKey2
{
    public partial class Form1 : Form
    {
        private int _X, _Y;
        [StructLayout(LayoutKind.Sequential)]
        private struct ICONINFO
        {
            public bool fIcon;
            public Int32 xHotspot;
            public Int32 yHotspot;
            public IntPtr hbmMask;
            public IntPtr hbmColor;
        }
        [StructLayout(LayoutKind.Sequential)]
        private struct CURSORINFO
        {
            public Int32 cbSize;
            public Int32 flags;
            public IntPtr hCursor;
            public Point ptScreenPos;
        }
        [DllImport("user32.dll", EntryPoint = "GetSystemMetrics")]
        private static extern int GetSystemMetrics(int mVal);
        [DllImport("user32.dll", EntryPoint = "GetCursorInfo")]
        private static extern bool GetCursorInfo(ref CURSORINFO cInfo);
        [DllImport("user32.dll", EntryPoint = "CopyIcon")]
        private static extern IntPtr CopyIcon(IntPtr hIcon);
        [DllImport("user32.dll", EntryPoint = "GetIconInfo")]
        private static extern bool GetIconInfo(IntPtr hIcon, out ICONINFO iInfo);

        //如果函数执行成功，返回值不为0。       
        //如果函数执行失败，返回值为0。要得到扩展错误信息，调用GetLastError。        
        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool RegisterHotKey(
        IntPtr hWnd,                //要定义热键的窗口的句柄            
        int id,                     //定义热键ID（不能与其它ID重复）                       
        KeyModifiers fsModifiers,   //标识热键是否在按Alt、Ctrl、Shift、Windows等键时才会生效         
        Keys vk                     //定义热键的内容            
    );
        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool UnregisterHotKey(
            IntPtr hWnd,                //要取消热键的窗口的句柄            
            int id                      //要取消热键的ID            
        );
        //定义了辅助键的名称（将数字转变为字符以便于记忆，也可去除此枚举而直接使用数值）        
        [Flags()]
        public enum KeyModifiers
        {
            None = 0,
            Alt = 1,
            Ctrl = 2,
            Shift = 4,
            WindowsKey = 8
        }


        string Cursor;
        string foldername = @"C:\dddddddddd";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            RegisterHotKey(Handle, 81, KeyModifiers.Shift, Keys.F); //Shift + F 為快速鍵

            //檢查存圖的資料夾
            if (Directory.Exists(foldername) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(foldername);
                richTextBox1.Text += "已建立一個新資料夾: " + foldername + "\n";
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + foldername + " 已存在，不用再建立\n";
            }
        }

        private Bitmap CaptureNoCursor()//抓取没有鼠标的桌面
        {
            Bitmap _Source = new Bitmap(GetSystemMetrics(0), GetSystemMetrics(1));
            using (Graphics g = Graphics.FromImage(_Source))
            {
                g.CopyFromScreen(0, 0, 0, 0, _Source.Size);
                g.Dispose();
            }
            return _Source;
        }

        private Bitmap CaptureDesktop()//抓取带鼠标的桌面
        {
            try
            {
                int _CX = 0, _CY = 0;
                Bitmap _Source = new Bitmap(GetSystemMetrics(0), GetSystemMetrics(1));
                using (Graphics g = Graphics.FromImage(_Source))
                {

                    g.CopyFromScreen(0, 0, 0, 0, _Source.Size);
                    g.DrawImage(CaptureCursor(ref _CX, ref _CY), _CX, _CY);
                    g.Dispose();
                }
                _X = (800 - _Source.Width) / 2;
                _Y = (600 - _Source.Height) / 2;
                return _Source;
            }
            catch
            {
                return null;
            }
        }

        private Bitmap CaptureCursor(ref int _CX, ref int _CY)
        {
            IntPtr _Icon;
            CURSORINFO _CursorInfo = new CURSORINFO();
            ICONINFO _IconInfo;
            _CursorInfo.cbSize = Marshal.SizeOf(_CursorInfo);
            if (GetCursorInfo(ref _CursorInfo))
            {
                if (_CursorInfo.flags == 0x00000001)
                {
                    _Icon = CopyIcon(_CursorInfo.hCursor);

                    if (GetIconInfo(_Icon, out _IconInfo))
                    {
                        _CX = _CursorInfo.ptScreenPos.X - _IconInfo.xHotspot;
                        _CY = _CursorInfo.ptScreenPos.Y - _IconInfo.yHotspot;
                        return Icon.FromHandle(_Icon).ToBitmap();
                    }
                }
            }
            return null;
        }

        private void Form1_StyleChanged(object sender, EventArgs e)
        {
        }

        public bool flag = true;
        private void 退出ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            UnregisterHotKey(Handle, 81);   //注销Id号为81的热键设定
            flag = false;
            Application.Exit();
        }

        private void Form1_Activated(object sender, EventArgs e)
        {
            RegisterHotKey(Handle, 81, KeyModifiers.Shift, Keys.F);
        }

        private void save_fullscreen_to_local_drive()
        {
            //存成bmp檔
            string filename = "C:\\dddddddddd\\full_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            Bitmap bitmap1;

            //無鼠標存圖
            bitmap1 = CaptureNoCursor();
            
            //有鼠標存圖
            //bitmap1 = CaptureDesktop();

            bitmap1.Save(filename);

            richTextBox1.Text += "全螢幕截圖，存檔檔名：\n" + filename + "\n";
        }

        protected override void WndProc(ref Message m)
        {
            const int WM_HOTKEY = 0x0312;
            //按快捷键     
            switch (m.Msg)
            {
                case WM_HOTKEY:
                    switch (m.WParam.ToInt32())
                    {
                        case 81:    //按下的是Shift+F
                            richTextBox1.Text += "存圖\n";
                            save_fullscreen_to_local_drive();       //全螢幕截圖
                            break;
                    }
                    break;
            }
            base.WndProc(ref m);
        }

        private void notifyIcon1_MouseDoubleClick(object sender, MouseEventArgs e)//双击显示设置窗体
        {
            this.Show();
        }

        private void 设置ToolStripMenuItem_Click(object sender, EventArgs e)//单击设置打开设置窗体
        {
            this.Show();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            UnregisterHotKey(Handle, 81);   //注销Id号为81的热键设定

            this.Hide();
            if (flag == true)
            {
                e.Cancel = true;
            }
        }
    }
}
