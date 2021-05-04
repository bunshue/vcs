using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Reflection;
using System.IO;

namespace ScreenImage
{
    class HOOK
    {
        #region 私有變數

        /// <summary>
        /// 鍵盤掛鉤句柄
        /// </summary>
        private IntPtr m_pKeyboardHook = IntPtr.Zero;

        /// <summary>
        /// 掛鉤委託宣告
        /// </summary>
        /// <param name="nCode"></param>
        /// <param name="wParam"></param>
        /// <param name="lParam"></param>
        /// <returns></returns>
        public delegate int HookProc(int nCode, Int32 wParam, IntPtr lParam);

        /// <summary>
        /// 鍵盤掛鉤委託實例
        /// </summary>
        private HookProc m_KeyboardHookProcedure;

        /// <summary>
        /// 底層的掛鉤變數
        /// </summary>
        public const int idHook = 13;

        /// <summary>
        /// 安裝掛鉤
        /// </summary>
        /// <param name="idHook"></param>
        /// <param name="lpfn"></param>
        /// <param name="hInstance"></param>
        /// <param name="threadId"></param>
        /// <returns></returns>
        [DllImport("user32.dll", CallingConvention = CallingConvention.StdCall)]
        public static extern IntPtr SetWindowsHookEx(int idHook, HookProc lpfn, IntPtr pInstance, int threadId);

        /// <summary>
        /// 卸載掛鉤
        /// </summary>
        /// <param name="idHook"></param>
        /// <returns></returns>
        [DllImport("user32.dll", CallingConvention = CallingConvention.StdCall)]
        public static extern bool UnhookWindowsHookEx(IntPtr pHookHandle);

        /// <summary>
        /// 傳遞掛鉤
        /// </summary>
        /// <param name="pHookHandle">是您自己的掛鉤函數的句柄。用該句柄可以搜尋掛鉤鏈</param>
        /// <param name="nCode">把傳入的參數簡單傳給CallNextHookEx即可</param>
        /// <param name="wParam">把傳入的參數簡單傳給CallNextHookEx即可</param>
        /// <param name="lParam"></param>
        /// <returns></returns>
        [DllImport("user32.dll", CallingConvention = CallingConvention.StdCall)]
        public static extern int CallNextHookEx(IntPtr pHookHandle, int nCode, Int32 wParam, IntPtr lParam);

        [StructLayout(LayoutKind.Sequential)]
        public struct KeyMSG
        {
            public int vkCode;
            public int scanCode;
            public int flags;
            public int time;
            public int dwExtraInfo;
        }

        protected const int WM_KEYUP = 0x101;
        protected const int WM_SYSKEYUP = 0x105;

        public static int pp = 0;//熱鍵的傳回值
        public static bool isInstall = false;//是否安裝掛鉤，true為安裝
        #endregion

        #region 事件的宣告
        public event KeyEventHandler KeyUp;//鍵盤鬆開事件
        #endregion

        #region 方法
        /// <summary>
        /// 掛鉤擷取訊息後，對訊息進行處理
        /// </summary>
        /// <param nCode="int">標識，鍵盤是否操作</param> 
        /// <param wParam="int">鍵盤的操作值</param>
        /// <param lParam="IntPtr">指針</param>
        private int KeyboardHookProc(int nCode, int wParam, IntPtr lParam)
        {
            if (nCode > -1 && KeyUp != null)
            {

                KeyMSG keyboardHookStruct = (KeyMSG)Marshal.PtrToStructure(lParam, typeof(KeyMSG));//取得掛鉤的相關訊息
                KeyEventArgs e = new KeyEventArgs((Keys)(keyboardHookStruct.vkCode));//取得KeyEventArgs事件的相磁訊息
                switch (wParam)
                {
                    case WM_KEYUP://鍵盤鬆開操作
                    case WM_SYSKEYUP:
                        if (KeyUp != null)//如果加載了目前事件
                        {
                            KeyUp(this, e);//呼叫該事件
                        }
                        break;
                }
            }
            return pp;//是否屏蔽目前熱鍵，1為屏蔽，2為執行
        }
        #endregion

        #region 安裝、卸載掛鉤

        /// <summary>
        /// 安裝掛鉤
        /// </summary>
        /// <returns>是否安裝成功</returns>
        public bool Start()
        {
            IntPtr pInstance = (IntPtr)4194304;//掛鉤所在實例的句柄
            if (this.m_pKeyboardHook == IntPtr.Zero)//如果鍵盤的句柄為空
            {
                this.m_KeyboardHookProcedure = new HookProc(KeyboardHookProc);//宣告一個托管掛鉤
                this.m_pKeyboardHook = SetWindowsHookEx(idHook, m_KeyboardHookProcedure, pInstance, 0);//安裝掛鉤
                if (this.m_pKeyboardHook == IntPtr.Zero)//如果安裝失敗
                {
                    this.Stop();//卸載掛鉤
                    return false;
                }
            }
            isInstall = true;//安裝了掛鉤
            return true;
        }

        /// <summary>
        /// 卸載掛鉤
        /// </summary>
        /// <returns>是否卸載成功</returns>
        public bool Stop()
        {
            if (isInstall == false)//如果沒有安裝掛鉤
            {
                return true;
            }
            bool result = true;
            if (this.m_pKeyboardHook != IntPtr.Zero)//如果安裝了掛鉤
            {
                result = (UnhookWindowsHookEx(this.m_pKeyboardHook) && result);//卸載掛鉤
                this.m_pKeyboardHook = IntPtr.Zero;//清空鍵盤的掛鉤句柄
            }
            return result;
        }
        #endregion 公共方法
    }
}
//