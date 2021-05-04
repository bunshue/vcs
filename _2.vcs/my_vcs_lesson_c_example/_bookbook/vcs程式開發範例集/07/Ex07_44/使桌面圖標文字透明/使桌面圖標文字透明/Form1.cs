using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace 使桌面圖標文字透明
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        [DllImport("user32.dll")]
        public static extern int GetDesktopWindow();

        [DllImport("user32.dll")]
        public static extern int FindWindowEx(int hWnd1, int hWnd2, string lpsz1, string lpsz2);

        [DllImport("user32.dll")]
        public static extern int SendMessage(int hwnd, int wMsg, int wParam, uint lParam);

        [DllImport("user32.dll")]
        public static extern int InvalidateRect(int hwnd, ref Rectangle lpRect, bool bErase);

        private const int wMsg1 = 0x1026;
        private const int wMsg2 = 0x1024;
        private const uint lParam1 = 0xffffffff;
        private const uint lParam2 = 0x00ffffff;
        Rectangle lpRect = new Rectangle(0,0,0,0);

        private void button1_Click(object sender, EventArgs e)
        {
            int hwnd;
            hwnd = GetDesktopWindow();
            hwnd = FindWindowEx(hwnd, 0, "Progman", null);
            hwnd = FindWindowEx(hwnd, 0, "SHELLDLL_DefView", null);
            hwnd = FindWindowEx(hwnd, 0, "SysListView32", null);
            SendMessage(hwnd, wMsg1, 0, lParam1);
            SendMessage(hwnd, wMsg2, 0, lParam2);
            InvalidateRect(hwnd, ref lpRect, true);
            MessageBox.Show("設定成功！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}