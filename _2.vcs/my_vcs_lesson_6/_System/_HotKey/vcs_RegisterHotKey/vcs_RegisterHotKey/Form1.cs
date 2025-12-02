using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                //for Directory
using System.Drawing.Imaging;   //for ImageFormat
using System.Runtime.InteropServices;   //for DllImport
using System.Diagnostics;       //for Process

//註冊熱鍵

namespace vcs_RegisterHotKey
{
    public partial class Form1 : Form
    {
        //定義快捷鍵 ST
        //如果函數執行成功，返回值不為0。       
        //如果函數執行失敗，返回值為0。要得到擴展錯誤信息，調用GetLastError。        

        //註冊 RegisterHotKey()
        //在類內部聲明兩個API函數,它們的位置和類的成員變量等同
        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool RegisterHotKey(
        IntPtr hWnd,                //要定義熱鍵的窗口的句柄
        int id,                     //定義熱鍵ID（不能與其它ID重復）
        KeyModifiers fsModifiers,   //標識熱鍵是否在按Alt、Ctrl、Shift、Windows等鍵時才會生效
        Keys vk                     //定義熱鍵的內容
        );

        //取消註冊 UnregisterHotKey()
        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool UnregisterHotKey(
            IntPtr hWnd,                //要取消熱鍵的窗口的句柄            
            int id                      //要取消熱鍵的ID            
        );

        /* tmp
        //註冊 RegisterHotKey()
        //在類內部聲明兩個API函數,它們的位置和類的成員變量等同
        [System.Runtime.InteropServices.DllImport("user32.dll")] //申明API函數
        public static extern bool RegisterHotKey(
        IntPtr hWnd, // handle to window
        int id, // hot key identifier
        uint fsModifiers, // key-modifier options, 指明與熱鍵聯合使用按鍵
            //可取值為：MOD_ALT MOD_CONTROL MOD_WIN MOD_SHIFT引數，或數字0為無，1為Alt,2為Control，4為Shift，8為Windows
        Keys vk // virtual-key code, 指明熱鍵的虛擬鍵碼
        );

        //取消註冊 UnregisterHotKey()
        [System.Runtime.InteropServices.DllImport("user32.dll")] //申明API函數
        public static extern bool UnregisterHotKey(
        IntPtr hWnd, // handle to window
        int id // hot key identifier
        );
        */

        /* 簡易
        [DllImport("user32.dll")]
        private static extern bool RegisterHotKey(IntPtr hWnd, int id, int modifiers, Keys vk);
        [DllImport("user32.dll")]
        private static extern bool UnregisterHotKey(IntPtr hWnd, int id);
        */

        //定義一個KeyModifiers的枚舉,以便出現組合鍵
        //定義了輔助鍵的名稱（將數字轉變為字符以便于記憶，也可去除此枚舉而直接使用數值）
        [Flags()]
        public enum KeyModifiers
        {
            NONE = 0,
            ALT = 1,
            CTRL = 2,
            SHIFT = 4,
            WINDOWS_KEY = 8
        }
        //定義快捷鍵 SP

        //重寫WndProc()方法，通過監視系統消息，來調用過程
        protected override void WndProc(ref Message m)//監視Windows消息
        {
            const int WM_HOTKEY = 0x0312; //如果m.Msg的值為0x0312那麼表示使用者按下了熱鍵
            switch (m.Msg)
            {
                case WM_HOTKEY:
                    switch (m.WParam.ToInt32())
                    {
                        case 11:
                            do_hotkey_11();
                            break;
                        case 22:
                            do_hotkey_22();
                            break;
                        case 33:
                            do_hotkey_33();
                            break;
                        case 44:
                            do_hotkey_44();
                            break;
                        case 55:
                            do_hotkey_55();
                            break;
                        case 91:
                            do_hotkey_91();
                            break;
                        case 92:
                            do_hotkey_92();
                            break;
                        case 93:
                            do_hotkey_93();
                            break;
                        case 94:
                            do_hotkey_94();
                            break;
                        default:
                            break;
                    }
                    break;
                default:
                    break;
            }
            base.WndProc(ref m); //將系統消息傳遞自父類的WndProc
        }

        void do_hotkey_11()
        {
            //按下的是ESC
            richTextBox1.Text += "你按了快捷鍵ID=11\n";
            Application.Exit();
        }

        void do_hotkey_22()
        {
            richTextBox1.Text += "你按了快捷鍵ID=22\n";
            save_fullscreen_to_local_drive();       //全螢幕截圖
        }

        void do_hotkey_33()
        {
            richTextBox1.Text += "你按了快捷鍵ID=33\n";
        }

        void do_hotkey_44()
        {
            //按下的是WIN+F10
            richTextBox1.Text += "你按了快捷鍵ID=44\n";
            richTextBox1.Text += "你按了 WIN+F10\n";
        }

        void do_hotkey_55()
        {
            richTextBox1.Text += "你按了快捷鍵ID=55\n";
            Process.Start(@"C:\WINDOWS\system32\calc.exe");
        }

        void do_hotkey_91()
        {
            richTextBox1.Text += "你按了 Ctrl + 左\n";
        }

        void do_hotkey_92()
        {
            richTextBox1.Text += "你按了 Ctrl + 右\n";
        }

        void do_hotkey_93()
        {
            richTextBox1.Text += "你按了 Ctrl + 上\n";
        }

        void do_hotkey_94()
        {
            richTextBox1.Text += "你按了 Ctrl + 下\n";
        }

        private RegisterHotKeyClass RegisterHotKey1 = new RegisterHotKeyClass();
        private RegisterHotKeyClass RegisterHotKey2 = new RegisterHotKeyClass();

        void Register_HotKey_Function1()
        {
            save_fullscreen_to_local_drive();       //全螢幕截圖

            //顯示訊息
            //this.Show();
            this.WindowState = FormWindowState.Normal;
            this.TopMost = true;
            Application.DoEvents(); //為了顯示出來
            System.Threading.Thread.Sleep(1000);
            //this.Hide();
            this.WindowState = FormWindowState.Minimized;
            this.TopMost = false;
        }

        void Register_HotKey_Function2()
        {
            Process.Start(@"C:\WINDOWS\system32\calc.exe");
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //註冊快捷鍵	    快捷鍵ID     輔助鍵      快捷鍵內容
            RegisterHotKey(Handle, 11, KeyModifiers.NONE, Keys.Escape); // ESC
            RegisterHotKey(Handle, 22, KeyModifiers.CTRL, Keys.P); // Ctrl + P 全螢幕截圖
            RegisterHotKey(Handle, 33, KeyModifiers.SHIFT, Keys.F); // Shift + F            
            RegisterHotKey(Handle, 44, KeyModifiers.WINDOWS_KEY, Keys.F10);

            //組合鍵  ALT + CTRL + C
            KeyModifiers ctrlHotKey = KeyModifiers.ALT | KeyModifiers.CTRL;
            RegisterHotKey(Handle, 55, ctrlHotKey, Keys.C);

            RegisterHotKey(Handle, 91, KeyModifiers.CTRL, Keys.Left);  // 熱鍵一 : Ctrl + 左
            RegisterHotKey(Handle, 92, KeyModifiers.CTRL, Keys.Right); // 熱鍵二 : Ctrl + 右
            RegisterHotKey(Handle, 93, KeyModifiers.CTRL, Keys.Up);    // 熱鍵三 : Ctrl + 上
            RegisterHotKey(Handle, 94, KeyModifiers.CTRL, Keys.Down);  // 熱鍵四 : Ctrl + 下

            //按 PrintScreen 全螢幕截圖

            richTextBox1.Text += "測試快捷鍵範例\nPrintScreen 全螢幕截圖\n";
            RegisterHotKey1.Keys = Keys.PrintScreen;
            RegisterHotKey1.ModKey = RegisterHotKeyClass.KeyModifiers.NONE;
            RegisterHotKey1.WindowHandle = this.Handle;
            RegisterHotKey1.HotKey += new RegisterHotKeyClass.HotKeyPass(Register_HotKey_Function1);
            RegisterHotKey1.StarHotKey();

            /*  目前不能做到依照不同的快捷鍵做不同的事
            RegisterHotKey2.Keys = Keys.C;
            RegisterHotKey2.ModKey = RegisterHotKeyClass.KeyModifiers.CONTROL | RegisterHotKeyClass.KeyModifiers.ALT;
            RegisterHotKey2.WindowHandle = this.Handle;
            RegisterHotKey2.HotKey += new RegisterHotKeyClass.HotKeyPass(Register_HotKey_Function2);
            RegisterHotKey2.StarHotKey();
            */

            //檢查存圖的資料夾
            string Path = @"C:\dddddddddd_tmp";
            if (Directory.Exists(Path) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(Path);
                richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //取消註冊快捷鍵
            UnregisterHotKey(Handle, 11);
            UnregisterHotKey(Handle, 22);
            UnregisterHotKey(Handle, 33);
            UnregisterHotKey(Handle, 44);
            UnregisterHotKey(Handle, 55);

            UnregisterHotKey(Handle, 91);
            UnregisterHotKey(Handle, 92);
            UnregisterHotKey(Handle, 93);
            UnregisterHotKey(Handle, 94);
        }

        void show_item_location()
        {
            bt_ok.Location = new Point(210, 50);

            richTextBox1.Text += "註冊快捷鍵 ESC => 離開\n";
            richTextBox1.Text += "註冊快捷鍵 Ctrl + P 全螢幕截圖\n";
            richTextBox1.Text += "註冊快捷鍵 Alt + Ctrl + C 計算機\n";
            richTextBox1.Text += "Shift + F\n";
            richTextBox1.Text += "註冊快捷鍵 WIN + F10\n";

            richTextBox1.Dock = DockStyle.Fill;
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(300, 300);
            this.FormBorderStyle = FormBorderStyle.None;
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            this.Location = new Point(screenWidth - this.Width - 50, screenHeight - this.Height - 50);

            bt_exit_setup();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 40; //設定按鈕大小 W
            int h = 40; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_ok_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
            //this.Hide();	//隱藏表單
        }

        void save_fullscreen_to_local_drive()
        {
            //全螢幕截圖
            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;

            using (Bitmap bitmap1 = new Bitmap(W, H))
            {
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    //             擷取螢幕位置起點  自建bmp的位置起點     擷取大小
                    g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(W, H));
                    //richTextBox1.Text += "W = " + W.ToString() + "\n";
                    //richTextBox1.Text += "H = " + H.ToString() + "\n";
                }
                //存成bmp檔
                String filename = "C:\\dddddddddd\\full_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                bitmap1.Save(filename, ImageFormat.Bmp);
                richTextBox1.Text += "全螢幕截圖，存檔檔名：\n" + filename + "\n";
            }
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
