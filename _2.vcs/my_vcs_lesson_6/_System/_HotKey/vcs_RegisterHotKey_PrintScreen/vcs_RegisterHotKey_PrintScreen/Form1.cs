﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                //for Directory
using System.Drawing.Imaging;   //for ImageFormat
using System.Runtime.InteropServices;   //for dll

using System.Diagnostics;   //for Process

namespace vcs_RegisterHotKey_PrintScreen
{
    public partial class Form1 : Form
    {
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
            string Path = @"C:\dddddddddd";
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

        }

        void show_item_location()
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.FormBorderStyle = FormBorderStyle.None;
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            this.Location = new System.Drawing.Point(screenWidth - this.Width - 50, screenHeight - this.Height - 50);
            this.BackColor = Color.Gold;

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

        private void button1_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
            //this.Hide();	//隱藏表單
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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


        //在C#中引用名稱空間System.Runtime.InteropServices;來載入非託管類user32.dll
        /*
        * RegisterHotKey函式原型及說明：
        * BOOL RegisterHotKey(
        * HWND hWnd,   // window to receive hot-key notification
        * int id,   // identifier of hot key
        * UINT fsModifiers, // key-modifier flags
        * UINT vk   // virtual-key code);
        * 引數 id為你自己定義的一個ID值
        * 對一個執行緒來講其值必需在0x0000 - 0xBFFF範圍之內,十進位制為0~49151
        * 對DLL來講其值必需在0xC000 - 0xFFFF 範圍之內,十進位制為49152~65535
        * 在同一程序內該值必須唯一引數 fsModifiers指明與熱鍵聯合使用按鍵
        * 可取值為：MOD_ALT MOD_CONTROL MOD_WIN MOD_SHIFT引數，或數字0為無，1為Alt,2為Control，4為Shift，8為Windows
        * vk指明熱鍵的虛擬鍵碼
        */
        
        /*
        RegisterHotKey的用法
        uint ctrlHotKey = (uint)(KeyModifiers.Alt | KeyModifiers.Ctrl);
        // 註冊熱鍵為Alt+Ctrl+C, "100"為唯一標識熱鍵
        RegisterHotKey(Handle, 100, ctrlHotKey, Keys.A);

        // 解除安裝熱鍵
        UnregisterHotKey(Handle, 100);


         */
    }
}



