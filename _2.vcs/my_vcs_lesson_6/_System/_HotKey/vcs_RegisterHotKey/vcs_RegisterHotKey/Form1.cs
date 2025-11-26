using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//using System.IO;                //for Directory
//using System.Drawing.Imaging;   //for ImageFormat
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
                        case 11:    //按下的是ESC
                            richTextBox1.Text += "你按了快捷鍵ID=11\n";
                            Application.Exit();
                            break;
                        case 22:
                            richTextBox1.Text += "你按了快捷鍵ID=22\n";
                            //save_fullscreen_to_local_drive();       //全螢幕截圖
                            break;
                        case 33:
                            richTextBox1.Text += "你按了快捷鍵ID=33\n";
                            break;
                        case 44:    //按下的是WIN+F10
                            richTextBox1.Text += "你按了快捷鍵ID=44\n";
                            richTextBox1.Text += "你按了 WIN+F10\n";
                            break;
                        case 51:
                            richTextBox1.Text += "你按了 Ctrl + 左\n";
                            break;
                        case 52:
                            richTextBox1.Text += "你按了 Ctrl + 右\n";
                            break;
                        case 53:
                            richTextBox1.Text += "你按了 Ctrl + 上\n";
                            break;
                        case 54:
                            richTextBox1.Text += "你按了 Ctrl + 下\n";
                            break;
                        case 66:
                            richTextBox1.Text += "你按了快捷鍵ID=66\n";
                            Process.Start(@"C:\WINDOWS\system32\calc.exe");
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

            RegisterHotKey(Handle, 51, KeyModifiers.CTRL, Keys.Left);  // 熱鍵一 : Ctrl + 左
            RegisterHotKey(Handle, 52, KeyModifiers.CTRL, Keys.Right); // 熱鍵二 : Ctrl + 右
            RegisterHotKey(Handle, 53, KeyModifiers.CTRL, Keys.Up);    // 熱鍵三 : Ctrl + 上
            RegisterHotKey(Handle, 54, KeyModifiers.CTRL, Keys.Down);  // 熱鍵四 : Ctrl + 下

            //組合鍵  ALT + CTRL + C
            KeyModifiers ctrlHotKey = KeyModifiers.ALT | KeyModifiers.CTRL;
            RegisterHotKey(Handle, 66, ctrlHotKey, Keys.C);
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //取消註冊快捷鍵
            UnregisterHotKey(Handle, 11);
            UnregisterHotKey(Handle, 22);
            UnregisterHotKey(Handle, 33);
            UnregisterHotKey(Handle, 44);
            UnregisterHotKey(Handle, 66);

            UnregisterHotKey(Handle, 51);
            UnregisterHotKey(Handle, 52);
            UnregisterHotKey(Handle, 53);
            UnregisterHotKey(Handle, 54);
        }

        void show_item_location()
        {
            richTextBox1.Text += "測試快捷鍵範例\n";
            richTextBox1.Text += "Shift + F\n";
            richTextBox1.Text += "註冊快捷鍵 Ctrl + P 全螢幕截圖\n";
            richTextBox1.Text += "註冊快捷鍵 Alt + Ctrl + C 計算機\n";
            richTextBox1.Text += "註冊快捷鍵 ESC => 離開\n";
            richTextBox1.Text += "註冊快捷鍵 WIN + F10\n";

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.FormBorderStyle = FormBorderStyle.None;
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            this.Location = new Point(screenWidth - this.Width - 50, screenHeight - this.Height - 50);
            this.BackColor = Color.Gold;
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
}
