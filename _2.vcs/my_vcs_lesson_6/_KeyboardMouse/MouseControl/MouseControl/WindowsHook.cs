using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;
using System.Reflection;
using System.Runtime.InteropServices;


namespace WindwosHook
{
    /// <summary>
    /// 提供Unmanaged方法接收全域鍵盤事件。
    /// </summary>
    public static class KeyboardHook
    {
        /// <summary>
        /// 取得或設定是否獨佔所有鍵盤事件。
        /// </summary>
        public static bool Monopolize { get; set; }

        /// <summary>
        /// 不論是否擁有焦點，當鍵盤按下時引發此事件。
        /// </summary>
        public static event EventHandler<KeyEventArgs> GlobalKeyDown;
        /// <summary>
        /// 不論是否擁有焦點，當鍵盤放開時引發此事件。
        /// </summary>
        public static event EventHandler<KeyEventArgs> GlobalKeyUp;
        /// <summary>
        /// 取得或設定是否開始接收全域鍵盤事件。
        /// </summary>
        public static bool Enabled
        {
            get { return m_Enabled; }
            set
            {
                if (m_Enabled != value)
                {
                    m_Enabled = value;
                    if (value)
                        Install();
                    else
                        Uninstall();
                }
            }
        }
        private static bool m_Enabled = false;

        private static int m_HookHandle = 0;
        private static Win32Native.Structures.HookProc m_HookProc;

  
        /// <summary>
        /// 向Windows註冊Hook。
        /// </summary>
        private static void Install()
        {
            if (m_HookHandle == 0)
            {
                Process curProcess = Process.GetCurrentProcess();
                ProcessModule curModule = curProcess.MainModule;

                m_HookProc = new Win32Native.Structures.HookProc(HookProc);

                m_HookHandle = Win32Native.Methods.SetWindowsHookEx(Win32Native.NativeContansts.WH_KEYBOARD_LL, m_HookProc, Win32Native.Methods.GetModuleHandle(curModule.ModuleName), 0);
                curModule.Dispose();
                curProcess.Dispose();

                if (m_HookHandle == 0)
                    throw new Exception("Install Hook Faild.");
            }
        }
        private static void Uninstall()
        {
            if (m_HookHandle != 0)
            {
                bool ret = Win32Native.Methods.UnhookWindowsHookEx(m_HookHandle);

                if (ret)
                    m_HookHandle = 0;
                else
                    throw new Exception("Uninstall Hook Faild.");
            }
        }

        /// <summary>
        /// 註冊Windows Hook時用到的委派方法，當全域事件發生時會執行這個方法，並提供全域事件資料。
        /// </summary>
        private static int HookProc(int nCode, IntPtr wParam, IntPtr lParam)
        {
            KeyEventArgs e = null;
            int wParam_Int32 = wParam.ToInt32();
            if (nCode >= 0)
            {
                Win32Native.Structures.KEYBOARDLLHookStruct keyboardHookStruct = (Win32Native.Structures.KEYBOARDLLHookStruct)Marshal.PtrToStructure(lParam, typeof(Win32Native.Structures.KEYBOARDLLHookStruct));
                if (GlobalKeyDown != null && (wParam_Int32 == Win32Native.NativeContansts.WM_KEYDOWN || wParam_Int32 == Win32Native.NativeContansts.WM_SYSKEYDOWN))
                {
                    e = new KeyEventArgs(keyboardHookStruct.VirtualKeyCode);
                    GlobalKeyDown.Invoke(null, e);
                }
                else if (GlobalKeyUp != null && (wParam_Int32 == Win32Native.NativeContansts.WM_KEYUP || wParam_Int32 == Win32Native.NativeContansts.WM_SYSKEYUP))
                {
                    e = new KeyEventArgs(keyboardHookStruct.VirtualKeyCode);
                    GlobalKeyUp.Invoke(null, e);
                }
            }

            if (Monopolize || (e != null && e.Handled))
                return -1;
            return Win32Native.Methods.CallNextHookEx(m_HookHandle, nCode, wParam, lParam);
        }

        /// <summary>
        /// 提供 GlobalKeyDown 或 GlobalKeyUp 事件的資料。
        /// </summary>
        public class KeyEventArgs : EventArgs
        {
            /// <summary>
            /// 取得或設定值，指出是否處理事件。
            /// </summary>
            public bool Handled { get; set; }
            /// <summary>
            /// 取得值，虛擬鍵盤碼的System.Windows.Forms.Keys表示。
            /// </summary>
            public System.Windows.Forms.Keys Keys { get { return (System.Windows.Forms.Keys)VirtualKeyCode; } }
            
            /// <summary>
            /// 取得值，指出是否按下 ALT 鍵。
            /// </summary>
            public bool Alt
            {
                get
                {
                    return KeyIsDown((int)System.Windows.Forms.Keys.LMenu) || KeyIsDown((int)System.Windows.Forms.Keys.RMenu);
                }
            }
            /// <summary>
            /// 取得值，指出是否按下 CTRL 鍵。
            /// </summary>
            public bool Control
            {
                get
                {
                    return KeyIsDown((int)System.Windows.Forms.Keys.LControlKey) || KeyIsDown((int)System.Windows.Forms.Keys.RControlKey);
                }
            }
            /// <summary>
            /// 取得值，指出是否按下 SHIFT 鍵。
            /// </summary>
            public bool Shift
            {
                get
                {
                    return KeyIsDown((int)System.Windows.Forms.Keys.LShiftKey) || KeyIsDown((int)System.Windows.Forms.Keys.RShiftKey);
                }
            }
            /// <summary>
            /// 取得值，引發事件的虛擬鍵盤碼。
            /// </summary>
            public int VirtualKeyCode { get; private set; }
            internal KeyEventArgs(int virtualKey)
            {
                this.Handled = false;
                this.VirtualKeyCode = virtualKey;
            }

            private static bool KeyIsDown(int KeyCode)
            {
                if ((Win32Native.Methods.GetKeyState(KeyCode) & 0x80) == 0x80)
                    return true;
                else
                    return false;
            }
        }
    }
}
