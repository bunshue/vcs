using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace 鍵盤掛鉤屏蔽熱鍵
{
    public partial class Form1 : Form
    {
        private IntPtr pKeyboardHook = IntPtr.Zero;//鍵盤掛鉤句柄
        public delegate int HookProc(int nCode, Int32 wParam, IntPtr lParam);// 掛鉤委託宣告
        //鍵盤掛鉤委託實例不能省略變數
        private HookProc KeyboardHookProcedure;
        //底層鍵盤掛鉤
        public const int idHook = 13;
        //安裝掛鉤
        [DllImport("user32.dll", CallingConvention = CallingConvention.StdCall)]
        public static extern IntPtr SetWindowsHookEx(int idHook, HookProc lpfn, IntPtr pInstance, int threadId);
        //卸載掛鉤
        [DllImport("user32.dll", CallingConvention = CallingConvention.StdCall)]
        public static extern bool UnhookWindowsHookEx(IntPtr pHookHandle);

        //鍵盤掛鉤處理函數
        private int KeyboardHookProc(int nCode, Int32 wParam, IntPtr lParam)
        {
            KeyMSG m = (KeyMSG)Marshal.PtrToStructure(lParam, typeof(KeyMSG));
            if (pKeyboardHook != IntPtr.Zero)
            {
                richTextBox1.Text += "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n";
                switch (((Keys)m.vkCode))
                {
                    case Keys.LWin:
                    case Keys.RWin:
                    case Keys.Delete:
                    case Keys.Alt:
                    case Keys.Escape:
                    case Keys.F4:
                    case Keys.Control:
                    case Keys.Tab:
                        return 1;
                }
            }
            return 0;
        }

        //安裝掛鉤
        public bool InsertHook()
        {
            richTextBox1.Text += "安裝掛鉤\n";

            IntPtr pIn = (IntPtr)4194304;
            if (this.pKeyboardHook == IntPtr.Zero)
            {
                this.KeyboardHookProcedure = new HookProc(KeyboardHookProc);
                this.pKeyboardHook = SetWindowsHookEx(idHook, KeyboardHookProcedure, pIn, 0);
                if (this.pKeyboardHook == IntPtr.Zero)
                {
                    this.UnInsertHook();
                    return false;
                }
            }
            return true;
        }

        //卸載掛鉤
        public bool UnInsertHook()
        {
            richTextBox1.Text += "卸載掛鉤\n";

            bool result = true;
            if (this.pKeyboardHook != IntPtr.Zero)
            {
                result = (UnhookWindowsHookEx(this.pKeyboardHook) && result);
                this.pKeyboardHook = IntPtr.Zero;
            }
            return result;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct KeyMSG
        {
            public int vkCode;
            public int scanCode;
            public int flags;
            public int time;
            public int dwExtraInfo;
        }

        public Form1()
        {
            InitializeComponent();
        }


        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //安裝掛勾, 鍵盤掛鉤屏蔽系統熱鍵
            InsertHook();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //卸載掛勾, 鍵盤掛鉤屏蔽系統熱鍵
            UnInsertHook();
        }
    }
}
