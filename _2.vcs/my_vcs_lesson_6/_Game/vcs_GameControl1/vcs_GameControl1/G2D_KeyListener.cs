
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_GameControl1
{
    // 取得 鍵盤哪一個按鍵(SHIFT、CTRL 和 ALT) 處於按下的狀態
    // 鍵盤輸入 if (G2D_KeyListener.IsKeyPushedDown(Keys.Up)) ...
    static class G2D_KeyListener
    {
        [System.Runtime.InteropServices.DllImport("User32.dll")]
        private static extern short GetAsyncKeyState(System.Windows.Forms.Keys vKey); // Keys enumeration

        [System.Runtime.InteropServices.DllImport("User32.dll")]
        private static extern short GetAsyncKeyState(System.Int32 vKey);

        public static bool IsKeyPushedDown(System.Windows.Forms.Keys vKey)
        {
            return 0 != (GetAsyncKeyState((int)vKey) & 0x8000);
        }
    }
}
