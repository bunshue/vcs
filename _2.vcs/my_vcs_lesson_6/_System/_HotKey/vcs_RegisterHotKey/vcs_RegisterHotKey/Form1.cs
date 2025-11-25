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
                    //ProcessHotkey(m); //按下熱鍵時調用ProcessHotkey()函數 取代以下switch-case
                    //label2.Text = "你按了 : " + m.Msg + "   " + m.WParam.ToInt32();
                    switch (m.WParam.ToInt32())
                    {
                        case 70:
                            //label2.Text = "你按了 " + m.WParam.ToInt32() + " 號熱鍵";
                            //this.TopMost = true;
                            break;
                        case 88:
                            //label2.Text = "你按了 " + m.WParam.ToInt32() + " 號熱鍵";
                            //save_fullscreen_to_local_drive();       //全螢幕截圖
                            break;
                        case 100:
                            //label2.Text = "你按了 " + m.WParam.ToInt32() + " 號熱鍵";
                            Process.Start(@"C:\WINDOWS\system32\calc.exe");

                            break;
                        case 181:    //按下的是ESC
                            Application.Exit();
                            break;
                        case 183:    //按下的是WIN+F10
                            richTextBox1.Text += "你按了 WIN+F10\n";
                            break;
                        default:
                            //label2.Text = "XXXX你按了 " + m.WParam.ToInt32() + " 號熱鍵";
                            //this.TopMost = true;
                            break;
                    }
                    break;
                default:
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
                case "333": richTextBox1.Text += "你按了 Alt+Ctrl+C\n"; break;
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
            //label2.Text = "你按了 " + mesg;
            richTextBox1.Text += "你按了 " + mesg + "\n";
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //註冊快捷鍵	  快捷鍵ID        輔助鍵      快捷鍵內容, 以 快捷鍵內容 為準
            RegisterHotKey(Handle, 70, KeyModifiers.SHIFT, Keys.F); // Shift + F
            RegisterHotKey(Handle, 88, KeyModifiers.CTRL, Keys.P); // Ctrl + P 全螢幕截圖

            KeyModifiers ctrlHotKey = KeyModifiers.ALT | KeyModifiers.CTRL;
            RegisterHotKey(Handle, 100, ctrlHotKey, Keys.C);    // 註冊熱鍵為Alt+Ctrl+C, "100"為唯一標識熱鍵

            //註冊熱鍵 ESC
            RegisterHotKey(Handle, 181, KeyModifiers.NONE, Keys.Escape);

            //註冊熱鍵 Ctrl + F
            //RegisterHotKey(Handle, 182, KeyModifiers.CTRL, Keys.F); 

            //註冊熱鍵
            RegisterHotKey(Handle, 183, KeyModifiers.WINDOWS_KEY, Keys.F10);



            /*
            //註冊了四個熱鍵:
            RegisterHotKey(Handle, 100, 2, Keys.Left);  // 熱鍵一 : Ctrl + 左
            RegisterHotKey(Handle, 200, 2, Keys.Right); // 熱鍵二 : Ctrl + 右
            RegisterHotKey(Handle, 300, 2, Keys.Up);    // 熱鍵三 : Ctrl + 上
            RegisterHotKey(Handle, 400, 2, Keys.Down);  // 熱鍵四 : Ctrl + 下

            // TBD
            uint ctrlHotKey = (uint)(KeyModifiers.Alt | KeyModifiers.Ctrl);
            // 註冊熱鍵為Alt+Ctrl+C, "333"為唯一標識熱鍵
            RegisterHotKey(Handle, 333, ctrlHotKey, Keys.A);

            string mesg = "註冊了四個熱鍵\n熱鍵一 : Ctrl + 左\n熱鍵二 : Ctrl + 右\n熱鍵三 : Ctrl + 上\n熱鍵四 : Ctrl + 下\n";
            label1.Text = "你按了 " + mesg;
            label2.Text = "";
            */
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            UnregisterHotKey(Handle, 70);   // 注销Id号为70的热键设定
            UnregisterHotKey(Handle, 88);   // 注销Id号为88的热键设定
            UnregisterHotKey(Handle, 100);  // 解除安裝熱鍵

            //取消註冊熱鍵
            UnregisterHotKey(Handle, 181);
            UnregisterHotKey(Handle, 183);

            /*
            //在程序退出時取消熱鍵的註冊
            UnregisterHotKey(Handle, 100); //卸載第1個快捷鍵, 解除安裝熱鍵
            UnregisterHotKey(Handle, 200); //缷載第2個快捷鍵
            UnregisterHotKey(Handle, 300); //卸載第3個快捷鍵
            UnregisterHotKey(Handle, 400); //缷載第4個快捷鍵
            UnregisterHotKey(Handle, 333); //缷載第5個快捷鍵
            */
        }

        void show_item_location()
        {
            richTextBox1.Text += "測試快捷鍵範例\n";
            richTextBox1.Text += "Shift + F\n";
            richTextBox1.Text += "Ctrl + P 全螢幕截圖\n";
            richTextBox1.Text += "Alt + Ctrl + C 計算機\n";

            richTextBox1.Text += "按ESC離開\n";
            richTextBox1.Text += "注冊系統按鍵ESC\n";
            richTextBox1.Text += "注冊系統按鍵WIN+F10\n";

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.FormBorderStyle = FormBorderStyle.None;
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            this.Location = new System.Drawing.Point(screenWidth - this.Width - 50, screenHeight - this.Height - 50);
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

