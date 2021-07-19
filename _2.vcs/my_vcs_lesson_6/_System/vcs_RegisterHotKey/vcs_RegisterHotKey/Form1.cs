using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Runtime.InteropServices;

namespace vcs_RegisterHotKey
{
    public partial class Form1 : Form
    {
        //定義快捷鍵 ST
        //如果函數執行成功，返回值不为0。       
        //如果函數執行失敗，返回值为0。要得到扩展错误信息，调用GetLastError。        

        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool RegisterHotKey(
        IntPtr hWnd,                //要定义热键的窗口的句柄   handle to window
        int id,                     //定义热键ID（不能与其它ID重复） hot key identifier
        KeyModifiers fsModifiers,   //标识热键是否在按Alt、Ctrl、Shift、Windows等键时才会生效 key-modifier options
        Keys vk                     //定义热键的内容   virtual-key code
        );

        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool UnregisterHotKey(
            IntPtr hWnd,                //要取消热键的窗口的句柄            
            int id                      //要取消热键的ID            
        );

        //定义了辅助键的名称（将数字转变为字符以便于记忆，也可去除此枚举而直接使用数值）        
        [Flags()]
        public enum KeyModifiers
        {
            NONE = 0,
            ALT = 1,
            CONTROL = 2,
            SHIFT = 4,
            WINDOWS_KEY = 8
        }
        //定義快捷鍵 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "測試快捷鍵範例" + Environment.NewLine + "Shift + F"+ Environment.NewLine + "Ctrl + P 全螢幕截圖"+ Environment.NewLine + "Alt + Ctrl + C";
            label2.Text = "";
            label3.Text = "";

            //註冊快捷鍵	  快捷鍵ID        輔助鍵      快捷鍵內容, 以 快捷鍵內容 為準
            RegisterHotKey(Handle, 70, KeyModifiers.SHIFT, Keys.F); // Shift + F
            RegisterHotKey(Handle, 88, KeyModifiers.CONTROL, Keys.P); // Ctrl + P 全螢幕截圖

            KeyModifiers ctrlHotKey = KeyModifiers.ALT | KeyModifiers.CONTROL;
            RegisterHotKey(Handle, 100, ctrlHotKey, Keys.C);    // 註冊熱鍵為Alt+Ctrl+C, "100"為唯一標識熱鍵
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            UnregisterHotKey(Handle, 70);   // 注销Id号为70的热键设定
            UnregisterHotKey(Handle, 88);   // 注销Id号为88的热键设定
            UnregisterHotKey(Handle, 100);  // 解除安裝熱鍵
        }

        protected override void WndProc(ref Message m)
        {
            //如果m.Msg的值為0x0312那麼表示使用者按下了熱鍵
            const int WM_HOTKEY = 0x0312;   // = 786
            switch (m.Msg)
            {
                case WM_HOTKEY:
                    label2.Text = "你按了 : " + m.Msg + "   " + m.WParam.ToInt32();
                    switch (m.WParam.ToInt32())
                    {
                        case 70:
                            label2.Text = "你按了 " + m.WParam.ToInt32() + " 號熱鍵";
                            //this.TopMost = true;
                            break;
                        case 88:
                            label2.Text = "你按了 " + m.WParam.ToInt32() + " 號熱鍵";
                            save_fullscreen_to_local_drive();       //全螢幕截圖
                            //this.TopMost = true;
                            break;
                        case 100:
                            label2.Text = "你按了 " + m.WParam.ToInt32() + " 號熱鍵";
                            //this.TopMost = true;
                            break;
                        default:
                            label2.Text = "XXXX你按了 " + m.WParam.ToInt32() + " 號熱鍵";
                            //this.TopMost = true;
                            break;
                    }
                    break;
                default:
                    break;
            }
            base.WndProc(ref m);
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

                label3.Text = "全螢幕截圖，存檔檔名：" + filename;
            }
        }
    }
}

