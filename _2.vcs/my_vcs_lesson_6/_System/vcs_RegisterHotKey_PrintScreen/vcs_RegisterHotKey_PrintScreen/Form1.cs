using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Runtime.InteropServices;   //for dll

namespace vcs_RegisterHotKey_PrintScreen
{
    public partial class Form1 : Form
    {
        private RegisterHotKeyClass _RegisKey = new RegisterHotKeyClass();

        void _Regis_HotKey()
        {
            save_fullscreen_to_local_drive();       //全螢幕截圖
        } 

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "測試快捷鍵範例" + Environment.NewLine + "PrintScreen 全螢幕截圖";

            _RegisKey.Keys = Keys.PrintScreen;
            _RegisKey.ModKey = 0;
            _RegisKey.WindowHandle = this.Handle;
            _RegisKey.HotKey += new RegisterHotKeyClass.HotKeyPass(_Regis_HotKey);
            _RegisKey.StarHotKey();

        }

        void save_fullscreen_to_local_drive()
        {
            //全螢幕截圖
            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;

            using (Bitmap bmp = new Bitmap(W, H))
            {
                using (Graphics g = Graphics.FromImage(bmp))
                {
                    g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(W, H));
                    //richTextBox1.Text += "W = " + W.ToString() + "\n";
                    //richTextBox1.Text += "H = " + H.ToString() + "\n";
                }
                //存成bmp檔
                String filename = "C:\\dddddddddd\\full_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                bmp.Save(filename, ImageFormat.Bmp);

                //richTextBox1.Text += "全螢幕截圖，存檔檔名：" + filename + "\n";
            }
        }

    }

    public class RegisterHotKeyClass
    {
        private IntPtr m_WindowHandle = IntPtr.Zero;
        private MODKEY m_ModKey = MODKEY.MOD_CONTROL;
        private Keys m_Keys = Keys.A;
        private int m_WParam = 10000;
        private bool Star = false;
        private HotKeyWndProc m_HotKeyWnd = new HotKeyWndProc();

        public IntPtr WindowHandle
        {
            get { return m_WindowHandle; }
            set { if (Star)return; m_WindowHandle = value; }
        }
        public MODKEY ModKey
        {
            get { return m_ModKey; }
            set { if (Star)return; m_ModKey = value; }
        }
        public Keys Keys
        {
            get { return m_Keys; }
            set { if (Star)return; m_Keys = value; }
        }
        public int WParam
        {
            get { return m_WParam; }
            set { if (Star)return; m_WParam = value; }
        }

        public void StarHotKey()
        {
            if (m_WindowHandle != IntPtr.Zero)
            {
                if (!RegisterHotKey(m_WindowHandle, m_WParam, m_ModKey, m_Keys))
                {
                    throw new Exception("");
                }
                try
                {
                    m_HotKeyWnd.m_HotKeyPass = new HotKeyPass(KeyPass);
                    m_HotKeyWnd.m_WParam = m_WParam;
                    m_HotKeyWnd.AssignHandle(m_WindowHandle);
                    Star = true;
                }
                catch
                {
                    StopHotKey();
                }
            }
        }
        private void KeyPass()
        {
            if (HotKey != null) HotKey();
        }
        public void StopHotKey()
        {
            if (Star)
            {
                if (!UnregisterHotKey(m_WindowHandle, m_WParam))
                {
                    throw new Exception("");
                }
                Star = false;
                m_HotKeyWnd.ReleaseHandle();
            }
        }


        public delegate void HotKeyPass();
        public event HotKeyPass HotKey;


        private class HotKeyWndProc : NativeWindow
        {
            public int m_WParam = 10000;
            public HotKeyPass m_HotKeyPass;
            protected override void WndProc(ref Message m)
            {
                if (m.Msg == 0x0312 && m.WParam.ToInt32() == m_WParam)
                {
                    if (m_HotKeyPass != null) m_HotKeyPass.Invoke();
                }

                base.WndProc(ref m);
            }
        }

        public enum MODKEY
        {
            MOD_ALT = 0x0001,
            MOD_CONTROL = 0x0002,
            MOD_SHIFT = 0x0004,
            MOD_WIN = 0x0008,
        }

        [DllImport("user32.dll")]
        public static extern bool RegisterHotKey(IntPtr wnd, int id, MODKEY mode, Keys vk);

        [DllImport("user32.dll")]
        public static extern bool UnregisterHotKey(IntPtr wnd, int id);
    }

}
