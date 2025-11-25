using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;
using System.Runtime.InteropServices;

using Microsoft.Win32;

namespace vcs_System_Hook1
{
    public partial class Form1 : Form
    {
        [DllImport("user32")]
        public static extern bool BlockInput(bool isBlock);
        [DllImport(@"native.dll", EntryPoint = "FuckSysKey")]
        private extern static bool FuckSysKey(bool enAble);

        public void BlockKeyAndMouse(bool b)
        {
            BlockInput(b);
            FuckSysKey(b);//鎖定ctrl+alt+del
        }

        public delegate int HookProc(int nCode, int wParam, IntPtr lParam);
        static int hHook = 0;
        public const int WH_KEYBOARD_LL = 13; // ESC

        //LowLevel鍵盤截獲，如果是WH_KEYBOARD＝2，並不能對系統鍵盤截取，Acrobat Reader會在你截取之前獲得鍵盤。
        HookProc KeyBoardHookProcedure;

        //鍵盤Hook結構函數
        [StructLayout(LayoutKind.Sequential)]
        public class KeyBoardHookStruct
        {
            public int vkCode;
            public int scanCode;
            public int flags;
            public int time;
            public int dwExtraInfo;
        }

        //設置鉤子
        [DllImport("user32.dll")]
        public static extern int SetWindowsHookEx(int idHook, HookProc lpfn, IntPtr hInstance, int threadId);
        [DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
        //抽掉鉤子
        public static extern bool UnhookWindowsHookEx(int idHook);
        [DllImport("user32.dll")]
        //調用下一個鉤子
        public static extern int CallNextHookEx(int idHook, int nCode, int wParam, IntPtr lParam);

        [DllImport("kernel32.dll")]
        public static extern int GetCurrentThreadId();

        [DllImport("kernel32.dll")]
        public static extern IntPtr GetModuleHandle(string name);

        public void Hook_Start()
        {
            richTextBox1.Text += "安裝鍵盤鉤子\n";
            // 安裝鍵盤鉤子
            if (hHook == 0)
            {
                KeyBoardHookProcedure = new HookProc(KeyBoardHookProc);

                //hHook = SetWindowsHookEx(2,
                //            KeyBoardHookProcedure,
                //          GetModuleHandle(Process.GetCurrentProcess().MainModule.ModuleName), GetCurrentThreadId());

                hHook = SetWindowsHookEx(WH_KEYBOARD_LL,
                          KeyBoardHookProcedure,
                        GetModuleHandle(Process.GetCurrentProcess().MainModule.ModuleName), 0);

                //如果設置鉤子失敗.
                if (hHook == 0)
                {
                    Hook_Clear();
                    //throw new Exception("設置Hook失敗!");
                }
            }
        }

        //取消鉤子事件
        public void Hook_Clear()
        {
            richTextBox1.Text += "取消鍵盤鉤子\n";
            bool retKeyboard = true;
            if (hHook != 0)
            {
                retKeyboard = UnhookWindowsHookEx(hHook);
                hHook = 0;
            }
            //如果去掉鉤子失敗.
            if (!retKeyboard)
            {
                throw new Exception("UnhookWindowsHookEx failed.");
            }
        }

        //這裡可以添加自己想要的信息處理
        public int KeyBoardHookProc(int nCode, int wParam, IntPtr lParam)
        {
            this.Text = "抓到ESC";
            richTextBox1.Text += "抓到ESC\n";
            return 0;
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動攔截\n";
            Hook_Start();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "停止攔截\n";
            Hook_Clear();
        }
    }
}
