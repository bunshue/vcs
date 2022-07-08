using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
//using System.Reflection;
using System.Diagnostics;

namespace vcs_Hook1
{
    public partial class Form1 : Form
    {
        //委托
        public delegate int HookProc(int nCode, int wParam, IntPtr lParam);
        static int hHook = 0;
        public const int WH_KEYBOARD_LL = 13;
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
        #region DllImport
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

        #endregion
        #region 自定義事件
        public void Hook_Start()
        {
            richTextBox1.Text += "安裝鍵盤鉤子\n";
            // 安裝鍵盤鉤子
            if (hHook == 0)
            {
                KeyBoardHookProcedure = new HookProc(KeyBoardHookProc);

                //hHook = SetWindowsHookEx(2, KeyBoardHookProcedure, GetModuleHandle(Process.GetCurrentProcess().MainModule.ModuleName), GetCurrentThreadId());

                hHook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyBoardHookProcedure, GetModuleHandle(Process.GetCurrentProcess().MainModule.ModuleName), 0);

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
            if (nCode >= 0)
            {
                KeyBoardHookStruct kbh = (KeyBoardHookStruct)Marshal.PtrToStructure(lParam, typeof(KeyBoardHookStruct));
                if (kbh.vkCode == (int)Keys.S && (int)Control.ModifierKeys == (int)Keys.Control)  // 截獲F8
                {
                    richTextBox1.Text += "快捷鍵已攔截! F8\n";
                    return 1;

                }
                if (kbh.vkCode == (int)Keys.Y&& (int)Control.ModifierKeys == (int)Keys.Control + (int)Keys.Alt)  //截獲Ctrl+Alt+Y
                {
                    richTextBox1.Text += "快捷鍵已攔截! Ctrl + Alt + Y\n";
                    return 1;
                }
                if (kbh.vkCode == (int)Keys.X)
                {
                    richTextBox1.Text += "快捷鍵已攔截! X\n";
                    return 1;
                }
                if (kbh.vkCode == (int)Keys.LWin)
                {
                    richTextBox1.Text += "快捷鍵已攔截! 系統開始菜單\n";
                    return 1;
                }
            }
            return CallNextHookEx(hHook, nCode, wParam, lParam);
        }
        #endregion

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "攔截目標 : F8 TBD\n";
            richTextBox1.Text += "攔截目標 : Ctrl + Alt + Y\n";
            richTextBox1.Text += "攔截目標 : X\n";
            richTextBox1.Text += "攔截目標 : 系統開始菜單\n";

            richTextBox1.Text += "未啟動攔截\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動攔截\n";
            Hook_Start();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "未啟動攔截\n";
            Hook_Clear();
        }
    }
}

