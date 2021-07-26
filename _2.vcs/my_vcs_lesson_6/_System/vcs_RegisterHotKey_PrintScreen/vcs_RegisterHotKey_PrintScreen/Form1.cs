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
        private RegisterHotKeyClass RegisterHotKey = new RegisterHotKeyClass();

        void _Regis_HotKey()
        {
            save_fullscreen_to_local_drive();       //全螢幕截圖
            //this.Show();
            this.WindowState = FormWindowState.Normal;
            Application.DoEvents(); //為了顯示出來
            System.Threading.Thread.Sleep(1000);
            //this.Hide();
            this.WindowState = FormWindowState.Minimized;
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "測試快捷鍵範例" + Environment.NewLine + "PrintScreen 全螢幕截圖";
            label2.Text = "";
            label3.Text = "";

            RegisterHotKey.Keys = Keys.PrintScreen;
            RegisterHotKey.ModKey = 0;
            RegisterHotKey.WindowHandle = this.Handle;
            RegisterHotKey.HotKey += new RegisterHotKeyClass.HotKeyPass(_Regis_HotKey);
            RegisterHotKey.StarHotKey();

            this.FormBorderStyle = FormBorderStyle.None;
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            this.Location = new System.Drawing.Point(screenWidth - this.Width - 50, screenHeight - this.Height - 50);
            this.BackColor = Color.Gold;
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

                label3.Text = "全螢幕截圖，存檔檔名：\n" + filename;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
            //this.Hide();	//隱藏表單
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }

    public class RegisterHotKeyClass
    {
        private IntPtr m_WindowHandle = IntPtr.Zero;
        private KeyModifiers m_ModKey = KeyModifiers.CONTROL;
        private Keys m_Keys = Keys.A;
        private int m_WParam = 10000;
        private bool Star = false;
        private HotKeyWndProc m_HotKeyWnd = new HotKeyWndProc();

        public IntPtr WindowHandle
        {
            get { return m_WindowHandle; }
            set { if (Star)return; m_WindowHandle = value; }
        }
        public KeyModifiers ModKey
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
            if (HotKey != null)
            {
                HotKey();
            }
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
                    if (m_HotKeyPass != null)
                    {
                        m_HotKeyPass.Invoke();
                    }
                }
                base.WndProc(ref m);
            }
        }

        public enum KeyModifiers
        {
            NONE = 0,
            ALT = 1,
            CONTROL = 2,
            SHIFT = 4,
            WINDOWS_KEY = 8
        }

        [DllImport("user32.dll")]
        public static extern bool RegisterHotKey(IntPtr wnd, int id, KeyModifiers mode, Keys vk);

        [DllImport("user32.dll")]
        public static extern bool UnregisterHotKey(IntPtr wnd, int id);
    }
}
