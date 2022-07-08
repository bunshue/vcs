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
using System.Runtime.InteropServices;   //for dll
using System.Diagnostics;       //for Process

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

        bool flag_show_mesg = false;
        protected override void WndProc(ref Message m)
        {
            //如果m.Msg的值為0x0312那麼表示使用者按下了熱鍵
            const int WM_HOTKEY = 0x0312;   // = 786
            switch (m.Msg)
            {
                case WM_HOTKEY:
                    //label2.Text = "你按了 : " + m.Msg + "   " + m.WParam.ToInt32();
                    switch (m.WParam.ToInt32())
                    {
                        case 70:
                            //label2.Text = "你按了 " + m.WParam.ToInt32() + " 號熱鍵";
                            //this.TopMost = true;
                            break;
                        case 88:
                            //label2.Text = "你按了 " + m.WParam.ToInt32() + " 號熱鍵";
                            save_fullscreen_to_local_drive();       //全螢幕截圖
                            flag_show_mesg = true;
                            break;
                        case 100:
                            //label2.Text = "你按了 " + m.WParam.ToInt32() + " 號熱鍵";
                            Process.Start(@"C:\WINDOWS\system32\calc.exe");
                            flag_show_mesg = false;

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
            base.WndProc(ref m);

            if (flag_show_mesg == true)
            {
                flag_show_mesg = false;
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
            RegisterHotKey(Handle, 88, KeyModifiers.CONTROL, Keys.P); // Ctrl + P 全螢幕截圖

            KeyModifiers ctrlHotKey = KeyModifiers.ALT | KeyModifiers.CONTROL;
            RegisterHotKey(Handle, 100, ctrlHotKey, Keys.C);    // 註冊熱鍵為Alt+Ctrl+C, "100"為唯一標識熱鍵

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
            UnregisterHotKey(Handle, 70);   // 注销Id号为70的热键设定
            UnregisterHotKey(Handle, 88);   // 注销Id号为88的热键设定
            UnregisterHotKey(Handle, 100);  // 解除安裝熱鍵
        }

        void show_item_location()
        {
            richTextBox1.Text += "測試快捷鍵範例\n";
            richTextBox1.Text += "Shift + F\n";
            richTextBox1.Text += "Ctrl + P 全螢幕截圖\n";
            richTextBox1.Text += "Alt + Ctrl + C 計算機\n";

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
                string filename = "C:\\dddddddddd\\full_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
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
}

