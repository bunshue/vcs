using System;
namespace Win32Native
{
    internal class Methods
    {
        /// <summary>
        /// 顯示滑鼠顯示或者隱藏
        /// </summary>
        /// <param name="bShow"></param>
        /// <returns></returns>
        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern int ShowCursor(bool bShow);


        /// <summary>
        /// 設置滑鼠位置
        /// </summary>
        /// <param name="x">畫面的x座標</param>
        /// <param name="y">畫面的y座標</param>
        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern void SetCursorPos(int x, int y);

        /// <summary>
        /// 取得目前滑鼠位置
        /// </summary>
        /// <param name="p">call by refernce會把滑鼠目前的位置傳到point物件裡面</param>
        /// <returns></returns>
        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern bool GetCursorPos(out System.Drawing.Point p);

        /// <summary>
        /// 送Input資訊給user32.dll，完成控制滑鼠點擊.鍵盤
        /// </summary>
        /// <param name="cInputs"></param>
        /// <param name="pInputs">輸入參數</param>
        /// <param name="cbSize"></param>
        /// <returns></returns>
        [System.Runtime.InteropServices.DllImport("user32.dll", SetLastError = true)]
        public static extern Int32 SendInput(Int32 cInputs, ref Win32Native.Structures.INPUT pInputs, Int32 cbSize);


        /// <summary>
        /// 取得鍵盤的狀態
        /// </summary>
        /// <param name="pbKeyState"></param>
        /// <returns></returns>
        [System.Runtime.InteropServices.DllImport("user32")]
        public static extern int GetKeyboardState(byte[] pbKeyState);

        /// <summary>
        /// 向作業系統hook一個handle
        /// </summary>
        /// <param name="idHook"></param>
        /// <param name="lpfn"></param>
        /// <param name="hInstance"></param>
        /// <param name="threadId"></param>
        /// <returns></returns>
        [System.Runtime.InteropServices.DllImport("user32.dll", CharSet = System.Runtime.InteropServices.CharSet.Auto, CallingConvention = System.Runtime.InteropServices.CallingConvention.StdCall)]
        public static extern int SetWindowsHookEx(int idHook, Win32Native.Structures.HookProc lpfn, IntPtr hInstance, int threadId);
        
        /// <summary>
        /// 向作業系統取消這個hook
        /// </summary>
        /// <param name="idHook"></param>
        /// <returns></returns>
        [System.Runtime.InteropServices.DllImport("user32.dll", CharSet = System.Runtime.InteropServices.CharSet.Auto, CallingConvention = System.Runtime.InteropServices.CallingConvention.StdCall)]
        public static extern bool UnhookWindowsHookEx(int idHook);

        /// <summary>
        /// 取得模組的handle
        /// </summary>
        /// <param name="lpModuleName"></param>
        /// <returns></returns>
        [System.Runtime.InteropServices.DllImport("kernel32.dll", CharSet = System.Runtime.InteropServices.CharSet.Auto, SetLastError = true)]
        public static extern IntPtr GetModuleHandle(string lpModuleName);

        /// <summary>
        /// 開啟下一個hook
        /// </summary>
        /// <param name="idHook"></param>
        /// <param name="nCode"></param>
        /// <param name="wParam"></param>
        /// <param name="lParam"></param>
        /// <returns></returns>
        [System.Runtime.InteropServices.DllImport("user32.dll", CharSet = System.Runtime.InteropServices.CharSet.Auto, CallingConvention = System.Runtime.InteropServices.CallingConvention.StdCall)]
        public static extern int CallNextHookEx(int idHook, int nCode, IntPtr wParam, IntPtr lParam);

        /// <summary>
        /// 取得鍵盤上的key的狀態
        /// </summary>
        /// <param name="keyCode"></param>
        /// <returns></returns>
        [System.Runtime.InteropServices.DllImport("user32.dll", CharSet = System.Runtime.InteropServices.CharSet.Auto, ExactSpelling = true, CallingConvention = System.Runtime.InteropServices.CallingConvention.Winapi)]
        public static extern short GetKeyState(int keyCode);


        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern UInt32 RegisterHotKey(IntPtr hWnd, UInt32 id, UInt32 fsModifiers, UInt32 vk);
        [System.Runtime.InteropServices.DllImport("kernel32.dll")]
        public static extern UInt32 GlobalAddAtom(String lpString);
        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern UInt32 UnregisterHotKey(IntPtr hWnd, UInt32 id);
        [System.Runtime.InteropServices.DllImport("kernel32.dll")]
        public static extern UInt32 GlobalDeleteAtom(UInt32 nAtom);


        [System.Runtime.InteropServices.DllImport("User32.dll")]  
        public static extern bool ShowWindowAsync(IntPtr hWnd, int cmdShow);

        [System.Runtime.InteropServices.DllImport("User32.dll")]  
        public static extern bool SetForegroundWindow(IntPtr hWnd); 

    }

    internal struct Structures
    {
        [System.Runtime.InteropServices.StructLayout(System.Runtime.InteropServices.LayoutKind.Explicit, Pack = 1, Size = 28)]
        public struct INPUT
        {
            [System.Runtime.InteropServices.FieldOffset(0)]
            public INPUTTYPE dwType;
            [System.Runtime.InteropServices.FieldOffset(4)]
            public MOUSEINPUT mi;
            [System.Runtime.InteropServices.FieldOffset(4)]
            public KEYBOARDINPUT ki;
            [System.Runtime.InteropServices.FieldOffset(4)]
            public HARDWAREINPUT hi;
        }

        [System.Runtime.InteropServices.StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential, Pack = 1)]
        public struct MOUSEINPUT
        {
            public Int32 dx;
            public Int32 dy;
            public Int32 mouseData;
            public MOUSEFLAG dwFlags;
            public Int32 time;
            public IntPtr dwExtraInfo;
        }

        [System.Runtime.InteropServices.StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential, Pack = 1)]
        public struct KEYBOARDINPUT
        {
            public Int16 wVk;
            public Int16 wScan;
            public KEYBOARDFLAG dwFlags;
            public Int32 time;
            public IntPtr dwExtraInfo;
        }

        [System.Runtime.InteropServices.StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential, Pack = 1)]
        public struct HARDWAREINPUT
        {
            public Int32 uMsg;
            public Int16 wParamL;
            public Int16 wParamH;
        }

        public enum INPUTTYPE : int
        {
            Mouse = 0,
            Keyboard = 1,
            Hardware = 2
        }

        [Flags()]
        public enum MOUSEFLAG : int
        {
            MOVE = 0x1,
            LEFTDOWN = 0x2,
            LEFTUP = 0x4,
            RIGHTDOWN = 0x8,
            RIGHTUP = 0x10,
            MIDDLEDOWN = 0x20,
            MIDDLEUP = 0x40,
            XDOWN = 0x80,
            XUP = 0x100,
            VIRTUALDESK = 0x400,
            WHEEL = 0x800,
            ABSOLUTE = 0x8000
        }

        [Flags()]
        public enum KEYBOARDFLAG : int
        {
            EXTENDEDKEY = 1,
            KEYUP = 2,
            UNICODE = 4,
            SCANCODE = 8
        }

        [System.Runtime.InteropServices.StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential)]
        public struct KEYBOARDLLHookStruct
        {
            public int VirtualKeyCode;
            public int ScanCode;
            public int Flags;
            public int Time;
            public int ExtraInfo;
        }

        public delegate int HookProc(int nCode, IntPtr wParam, IntPtr lParam);



    }

    internal class NativeContansts
    {
        public const int WH_MOUSE_LL = 14;
        public const int WH_KEYBOARD_LL = 13;
        public const int WH_MOUSE = 7;
        public const int WH_KEYBOARD = 2;

        public const int WM_MOUSEMOVE = 0x200;
        public const int WM_LBUTTONDOWN = 0x201;
        public const int WM_RBUTTONDOWN = 0x204;
        public const int WM_MBUTTONDOWN = 0x207;
        public const int WM_LBUTTONUP = 0x202;
        public const int WM_RBUTTONUP = 0x205;
        public const int WM_MBUTTONUP = 0x208;
        public const int WM_LBUTTONDBLCLK = 0x203;
        public const int WM_RBUTTONDBLCLK = 0x206;
        public const int WM_MBUTTONDBLCLK = 0x209;
        public const int WM_MOUSEWHEEL = 0x020A;
        public const int WM_KEYDOWN = 0x100;
        public const int WM_KEYUP = 0x101;
        public const int WM_SYSKEYDOWN = 0x104;
        public const int WM_SYSKEYUP = 0x105;

        public const int MEF_LEFTDOWN = 0x00000002;
        public const int MEF_LEFTUP = 0x00000004;
        public const int MEF_MIDDLEDOWN = 0x00000020;
        public const int MEF_MIDDLEUP = 0x00000040;
        public const int MEF_RIGHTDOWN = 0x00000008;
        public const int MEF_RIGHTUP = 0x00000010;

        public const int KEF_EXTENDEDKEY = 0x1;
        public const int KEF_KEYUP = 0x2;

        public const byte VK_SHIFT = 0x10;
        public const byte VK_CAPITAL = 0x14;
        public const byte VK_NUMLOCK = 0x90;
    }
}
