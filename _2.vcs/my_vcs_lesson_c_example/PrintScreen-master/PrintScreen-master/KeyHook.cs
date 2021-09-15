using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Diagnostics;

namespace KeyHook
{
    class KeyHooker
    {
        public static Boolean IsPrintScreenPressed = false;
        public static Boolean IsF12Pressed = false;

        public class KeyboardInfo
        {
            private KeyboardInfo() { }
            [DllImport("user32")]
            private static extern short GetKeyState(int vKey);

            public static KeyStateInfo GetKeyState(Keys key)
            {
                int vkey = (int)key;
                if (key == Keys.Alt)
                {
                    vkey = 0x12;    // VK_ALT
                }

                short keyState = GetKeyState(vkey);
                int low = Low(keyState);
                int high = High(keyState);
                bool toggled = (low == 1);
                bool pressed = (high == 1);
                return new KeyStateInfo(key, pressed, toggled);
            }

            private static int High(int keyState)
            {
                if (keyState > 0)
                {
                    return keyState >> 0x10;
                }
                else
                {
                    return (keyState >> 0x10) & 0x1;
                }
            }

            private static int Low(int keyState)
            {
                return keyState & 0xffff;
            }
        }

        public struct KeyStateInfo
        {
            Keys m_Key;
            bool m_IsPressed;
            bool m_IsToggled;

            public KeyStateInfo(Keys key, bool ispressed, bool istoggled)
            {
                m_Key = key;
                m_IsPressed = ispressed;
                m_IsToggled = istoggled;
            }

            public static KeyStateInfo Default
            {
                get
                {
                    return new KeyStateInfo(Keys.None, false, false);
                }
            }

            public Keys Key
            {
                get { return m_Key; }
            }

            public bool IsPressed
            {
                get { return m_IsPressed; }
            }

            public bool IsToggled
            {
                get { return m_IsToggled; }
            }
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct KBDLLHOOKSTRUCT
        {
            public Int32 vkCode;
            public Int32 scanCode;
            public Int32 flags;
            public Int32 time;
            public IntPtr dwExtraInfo;
        }

        const int WH_KEYBOARD_LL = 13;
        public delegate int HookProc(int nCode, IntPtr wParam, IntPtr lParam);

        private static int m_HookHandle = 0;
        private HookProc m_KbdHookProc;

        [DllImport("kernel32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr GetModuleHandle(string lpModuleName);

        [DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
        //設置鉤子 
        public static extern int SetWindowsHookEx(int idHook, HookProc lpfn, IntPtr hInstance, int threadId);

        [DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
        //抽掉鉤子
        public static extern bool UnhookWindowsHookEx(int idHook);

        [DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
        //調用下一個鉤子 
        public static extern int CallNextHookEx(int idHook, int nCode, IntPtr wParam, IntPtr lParam);

        [DllImport("user32.dll", SetLastError = true)]
        public static extern int ToAscii(uint uVirtKey, uint uScanCode, byte[] lpKeyState, StringBuilder lpChar, uint flags);

        [DllImport("user32.dll", CharSet = CharSet.Auto, ExactSpelling = true, CallingConvention = CallingConvention.Winapi)]
        public static extern short GetKeyState(int keyCode);

        public void Hook()
        {
            // 安裝鍵盤鉤子 
            if (m_HookHandle == 0)
            {
                using (Process curProcess = Process.GetCurrentProcess())

                using (ProcessModule curModule = curProcess.MainModule)
                {
                    m_KbdHookProc = new HookProc(KeyHooker.KeyboardHookProc);
                    m_HookHandle = SetWindowsHookEx(WH_KEYBOARD_LL, m_KbdHookProc, GetModuleHandle(curModule.ModuleName), 0);
                }

                //如果設置鉤子失敗
                if (m_HookHandle == 0)
                {
                    MessageBox.Show("呼叫 SetWindowsHookEx 失敗!");
                    return;
                }
            }
        }

        //取消鉤子事件
        public void UnHook()
        {
            bool ret = UnhookWindowsHookEx(m_HookHandle);

            if (ret == false)   //如果去掉鉤子失敗
            {
                MessageBox.Show("呼叫 UnhookWindowsHookEx 失敗!");
                return;
            }
            m_HookHandle = 0;
        }

        //KeyboardHookProc() :
        //當按鍵按下及鬆開時都會觸發此函式。 
        //這裏可以添加自己想要的信息處理
        public static int KeyboardHookProc(int nCode, IntPtr wParam, IntPtr lParam)
        {
            const int WM_KEYDOWN = 0x100;

            if (nCode >= 0)
            {
                KBDLLHOOKSTRUCT kbd = (KBDLLHOOKSTRUCT)Marshal.PtrToStructure(lParam, typeof(KBDLLHOOKSTRUCT));

                Keys vkCode = (Keys)kbd.vkCode;

                if (wParam == (IntPtr)WM_KEYDOWN) //Key Pressed
                {
                    if (vkCode == Keys.PrintScreen)
                    {
                        IsPrintScreenPressed = true;
                    }
                    if (vkCode == Keys.F12)
                    {
                        IsF12Pressed = true;
                    }
                }

                if (kbd.vkCode == 91)  // 截獲左win(開始菜單鍵)
                {
                    return 1;
                }
                if (kbd.vkCode == 92)// 截獲右win
                {
                    return 1;
                }
                if (kbd.vkCode == (int)Keys.Escape && (int)Control.ModifierKeys == (int)Keys.Control) //截獲Ctrl+Esc
                {
                    return 1;
                }
                if (kbd.vkCode == (int)Keys.F4 && (int)Control.ModifierKeys == (int)Keys.Alt)  //截獲alt+f4
                {
                    return 1;
                }
                if (kbd.vkCode == (int)Keys.Tab && (int)Control.ModifierKeys == (int)Keys.Alt) //截獲alt+tab
                {
                    return 1;
                }
                if (kbd.vkCode == (int)Keys.Escape && (int)Control.ModifierKeys == (int)Keys.Control + (int)Keys.Shift) //截獲Ctrl+Shift+Esc
                {
                    return 1;
                }
                if (kbd.vkCode == (int)Keys.Space && (int)Control.ModifierKeys == (int)Keys.Alt)  //截獲alt+空格
                {
                    return 1;
                }
                if (kbd.vkCode == 241)                  //截獲F1
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

                //if (kbd.vkCode == (int)Keys.Space && (int)Control.ModifierKeys == (int)Keys.Control + (int)Keys.Alt)  //截獲Ctrl+Alt+空格
                //{
                //    return 1;
                //}
            }
            return CallNextHookEx(m_HookHandle, nCode, wParam, lParam);
        }
    }
}

