using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
using System.Reflection;
using System.Diagnostics;
using Microsoft.Win32;


//參考    https://www.twblogs.net/a/5b823b1a2b71772b882fb103

namespace vcs_System7_Hotkey
{
    public partial class Form1 : Form
    {
        //委託
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

        public void Hook_Start()
        {
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

        //這裏可以添加自己想要的信息處理
        public static int KeyBoardHookProc(int nCode, int wParam, IntPtr lParam)
        {
            if (nCode >= 0)
            {
                KeyBoardHookStruct kbh = (KeyBoardHookStruct)Marshal.PtrToStructure(lParam, typeof(KeyBoardHookStruct));
                if (kbh.vkCode == 91)  // 截獲左win(開始菜單鍵)
                {
                    return 1;
                }
                if (kbh.vkCode == 92)// 截獲右win
                {
                    return 1;
                }
                if (kbh.vkCode == (int)Keys.Escape && (int)Control.ModifierKeys == (int)Keys.Control) //截獲Ctrl+Esc
                {
                    return 1;
                }
                if (kbh.vkCode == (int)Keys.F4 && (int)Control.ModifierKeys == (int)Keys.Alt)  //截獲alt+f4
                {
                    return 1;
                }
                if (kbh.vkCode == (int)Keys.Tab && (int)Control.ModifierKeys == (int)Keys.Alt) //截獲alt+tab
                {
                    return 1;
                }
                if (kbh.vkCode == (int)Keys.Escape && (int)Control.ModifierKeys == (int)Keys.Control + (int)Keys.Shift) //截獲Ctrl+Shift+Esc
                {
                    return 1;
                }
                if (kbh.vkCode == (int)Keys.Space && (int)Control.ModifierKeys == (int)Keys.Alt)  //截獲alt+空格
                {
                    return 1;
                }
                if (kbh.vkCode == 241)                  //截獲F1
                {
                    return 1;
                }
                if ((int)Control.ModifierKeys == (int)Keys.Control + (int)Keys.Alt + (int)Keys.Delete)      //截獲Ctrl+Alt+Delete
                {
                    return 1;
                }
                //if ((int)Control.ModifierKeys == (int)Keys.Control + (int)Keys.Shift)      //截獲Ctrl+Shift
                //{
                //    return 1;
                //}

                //if (kbh.vkCode == (int)Keys.Space && (int)Control.ModifierKeys == (int)Keys.Control + (int)Keys.Alt)  //截獲Ctrl+Alt+空格
                //{
                //    return 1;
                //}
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
            Hook_Start();

            //通過修改註冊表來屏蔽任務管理器
            //try
            //{
            //    RegistryKey r = Registry.CurrentUser.OpenSubKey("Software//Microsoft//Windows//CurrentVersion//Policies//System", true);
            //    r.SetValue("DisableTaskMgr", "1");  //屏蔽任務管理器
            //}
            //catch
            //{
            //    RegistryKey r = Registry.CurrentUser.CreateSubKey("Software//Microsoft//Windows//CurrentVersion//Policies//System");
            //    r.SetValue("DisableTaskMgr", "0");
            //}

        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Hook_Clear();

        }
    }
}
