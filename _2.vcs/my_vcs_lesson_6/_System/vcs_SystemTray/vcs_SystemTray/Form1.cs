using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

/*
WIN32系統托盤程序
程序運行後駐留系統托盤，左鍵呼出，右鍵退出。後續可加右鍵菜單。
注冊系統按鍵WIN+F10,呼出程序。
重寫系統消息，最小化和關閉按鈕隱藏程序
*/

//熱鍵部分已搬出

namespace vcs_SystemTray
{
    public enum HotkeyModifiers
    {
        Alt = 1,
        Ctrl = 2,
        Shift = 4,
        WindowsKey = 8
    }

    public partial class Form1 : Form
    {
        [DllImport("user32.dll")]
        private static extern bool RegisterHotKey(IntPtr hWnd, int id, int modifiers, Keys vk);

        [DllImport("user32.dll")]
        private static extern bool UnregisterHotKey(IntPtr hWnd, int id);

        const int WM_HOTKEY = 0x312;
        const int WM_SYSCOMMAND = 0X112;
        const int SC_MAXMIZE = 0xf030;
        const int SC_MINMIZE = 0xf020;
        const int SC_CLOSE = 0xf060;

        public Form1()
        {
            InitializeComponent();

            NotifyIcon ni = new NotifyIcon() { Icon = this.Icon, Visible = true };

            //RegisterHotKey //熱鍵部分已搬出
            bool bOK = RegisterHotKey(this.Handle, 0, (int)HotkeyModifiers.WindowsKey, Keys.F10);

            this.Closing += delegate
            {
                UnregisterHotKey(this.Handle, 0);
            };

            ni.MouseDown += (sender, e) =>
            {
                if (e.Button == MouseButtons.Left) //系統列 按左鍵
                {
                    this.Activate();
                    this.Visible = true;
                }
                if (e.Button == MouseButtons.Right) //系統列 按右鍵
                {
                    if (DialogResult.Yes == MessageBox.Show("Quit? Realy?", "Quit", MessageBoxButtons.YesNo))
                    {
                        this.Close();
                    }
                }
            };
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case WM_SYSCOMMAND:
                    int code = m.WParam.ToInt32();
                    if (code == SC_CLOSE || code == SC_MINMIZE)
                    {
                        this.Visible = false;
                        return;//Must Prevent WndProc
                    }
                    break; //others, such as SC_MAXMIZE must in WndProc.
                case WM_HOTKEY:
                    this.Text = DateTime.Now.ToString();
                    this.Activate();
                    this.Visible = true;
                    break;
            }
            base.WndProc(ref m);
        }
    }
}
