using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_HotKey
{
    public partial class Form1 : Form
    {
        //在類內部聲明兩個API函數,它們的位置和類的成員變量等同
        [System.Runtime.InteropServices.DllImport("user32.dll")] //申明API函數
        public static extern bool RegisterHotKey(
        IntPtr hWnd, // handle to window
        int id, // hot key identifIEr
        uint fsModifiers, // key-modifIEr options
        Keys vk // virtual-key code
        );
        [System.Runtime.InteropServices.DllImport("user32.dll")] //申明API函數
        public static extern bool UnregisterHotKey(
        IntPtr hWnd, // handle to window
        int id // hot key identifIEr
        );

        //定義一個KeyModifIErs的枚舉,以便出現組合鍵
        public enum KeyModifIErs
        {
            None = 0,
            Alt = 1,
            Control = 2,
            Shift = 4,
            Windows = 8
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //注冊了四個熱鍵:
            RegisterHotKey(Handle, 100, 2, Keys.Left);  // 熱鍵一 : Ctrl + 左
            RegisterHotKey(Handle, 200, 2, Keys.Right); // 熱鍵二 : Ctrl + 右
            RegisterHotKey(Handle, 300, 2, Keys.Up);    // 熱鍵三 : Ctrl + 上
            RegisterHotKey(Handle, 400, 2, Keys.Down);  // 熱鍵四 : Ctrl + 下
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //最後別忘了在程序退出時取消熱鍵的注冊
            UnregisterHotKey(Handle, 100); //卸載第1個快捷鍵
            UnregisterHotKey(Handle, 200); //缷載第2個快捷鍵
            UnregisterHotKey(Handle, 300); //卸載第3個快捷鍵
            UnregisterHotKey(Handle, 400); //缷載第4個快捷鍵
        }

        //重寫WndProc()方法，通過監視系統消息，來調用過程
        protected override void WndProc(ref Message m)//監視Windows消息
        {
            const int WM_HOTKEY = 0x0312; //如果m.Msg的值為0x0312那麼表示用戶按下了熱鍵
            switch (m.Msg)
            {
                case WM_HOTKEY:
                    ProcessHotkey(m); //按下熱鍵時調用ProcessHotkey()函數
                    break;
            }
            base.WndProc(ref m); //將系統消息傳遞自父類的WndProc
        }

        //實現ProcessHotkey函數, 按下設定的鍵時調用該函數
        private void ProcessHotkey(Message m)
        {
            IntPtr id = m.WParam; //IntPtr用於表示指針或句柄的平台特定類型
            //MessageBox.Show(id.ToString());
            string sid = id.ToString();
            switch (sid)
            {
                case "100": show_hot_key(100); break;   // 按下熱鍵一 : Ctrl + 左
                case "200": show_hot_key(200); break;   // 按下熱鍵二 : Ctrl + 右
                case "300": show_hot_key(300); break;   // 按下熱鍵三 : Ctrl + 上
                case "400": show_hot_key(400); break;   // 按下熱鍵四 : Ctrl + 下
                default: show_hot_key(999); break;
            }
        }

        void show_hot_key(int key)
        {
            string mesg = string.Empty;
            if (key == 100)
                mesg = "Ctrl + 左";
            else if (key == 200)
                mesg = "Ctrl + 右";
            else if (key == 300)
                mesg = "Ctrl + 上";
            else if (key == 400)
                mesg = "Ctrl + 下";
            else
                mesg = "XXXX";
            label1.Text = "你按了 " + mesg;
            richTextBox1.Text += "你按了 " + mesg + "\n";
        }
    }
}

