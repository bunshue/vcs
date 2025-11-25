using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_RegisterHotKey4
{
    public partial class Form1 : Form
    {
        // 定義快捷鍵 ST
        //如果函數執行成功，返回值不為0。       
        //如果函數執行失敗，返回值為0。要得到擴展錯誤信息，調用GetLastError。        
        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool RegisterHotKey(
        IntPtr hWnd,                //要定義熱鍵的窗口的句柄            
        int id,                     //定義熱鍵ID（不能與其它ID重復）                       
        KeyModifiers fsModifiers,   //標識熱鍵是否在按Alt、Ctrl、Shift、Windows等鍵時才會生效         
        Keys vk                     //定義熱鍵的內容            
    );
        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool UnregisterHotKey(
            IntPtr hWnd,                //要取消熱鍵的窗口的句柄            
            int id                      //要取消熱鍵的ID            
        );
        /* 簡易
        [DllImport("user32.dll")]
        private static extern bool RegisterHotKey(IntPtr hWnd, int id, int modifiers, Keys vk);
        [DllImport("user32.dll")]
        private static extern bool UnregisterHotKey(IntPtr hWnd, int id);
        */

        //定義了輔助鍵的名稱（將數字轉變為字符以便于記憶，也可去除此枚舉而直接使用數值）        
        [Flags()]
        public enum KeyModifiers
        {
            None = 0,
            Alt = 1,
            Ctrl = 2,
            Shift = 4,
            WindowsKey = 8
        }
        // 定義快捷鍵 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //註冊熱鍵 ESC
            RegisterHotKey(Handle, 81, KeyModifiers.None, Keys.Escape);

            //註冊熱鍵 Ctrl + F
            //RegisterHotKey(Handle, 81, KeyModifiers.Ctrl, Keys.F); 

            //註冊熱鍵
            RegisterHotKey(Handle, 82, KeyModifiers.WindowsKey, Keys.F10);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            //取消註冊熱鍵
            UnregisterHotKey(Handle, 81);
            UnregisterHotKey(Handle, 82);
        }

        protected override void WndProc(ref Message m)
        {
            const int WM_HOTKEY = 0x0312;
            //按快捷鍵     
            switch (m.Msg)
            {
                case WM_HOTKEY:
                    switch (m.WParam.ToInt32())
                    {
                        case 81:    //按下的是ESC
                            Application.Exit();
                            break;
                        case 82:    //按下的是WIN+F10
                            richTextBox1.Text += "你按了 WIN+F10\n";
                            break;
                    }
                    break;
            }
            base.WndProc(ref m);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {

        }
    }
}
