using System;
using System.Data;
using System.Windows.Forms;

namespace MouseControl
{
        class GlobalHotKey : IMessageFilter, IDisposable
        {
            IntPtr _hWnd = IntPtr.Zero;
            UInt32 _hotKeyID;
            Keys _hotKey = Keys.None;
            Keys _comboKey = Keys.None;

            public GlobalHotKey(IntPtr formHandle, Keys hotKey, Keys comboKey)
            {
                _hWnd = formHandle; //Form Handle, 註冊系統熱鍵需要用到這個
                _hotKey = hotKey; //熱鍵
                _comboKey = comboKey; //組合鍵, 必須設定Keys.Control, Keys.Alt, Keys.Shift, Keys.None以及Keys.LWin等值才有作用

                UInt32 uint_comboKey; //由於API對於組合鍵碼的定義不一樣, 所以我們這邊做個轉換
                switch (comboKey)
                {
                    case Keys.Alt:
                        uint_comboKey = 0x1;
                        break;
                    case Keys.Control:
                        uint_comboKey = 0x2;
                        break;
                    case Keys.Shift:
                        uint_comboKey = 0x4;
                        break;
                    case Keys.LWin:
                        uint_comboKey = 0x8;
                        break;
                    default: //沒有組合鍵
                        uint_comboKey = 0x0;
                        break;
                }

                _hotKeyID = Win32Native.Methods.GlobalAddAtom(Guid.NewGuid().ToString()); //向系統取得一組id
                Win32Native.Methods.RegisterHotKey((IntPtr)_hWnd, _hotKeyID, uint_comboKey, (UInt32)hotKey); //使用Form Handle與id註冊系統熱鍵
                Application.AddMessageFilter(this); //使用HotKey類別來監視訊息
            }

            public delegate void HotkeyEventHandler(object sender, HotKeyEventArgs e); //HotKeyEventArgs是自訂事件參數
            public event HotkeyEventHandler OnHotkey; //自訂事件

            const int WM_GLOBALHOTKEYDOWN = 0x312; //當按下系統熱鍵時, 系統會發送的訊息

            public bool PreFilterMessage(ref Message m)
            {
                if (OnHotkey != null && m.Msg == WM_GLOBALHOTKEYDOWN && (UInt32)m.WParam == _hotKeyID) //如果接收到系統熱鍵訊息且id相符時
                {
                    OnHotkey(this, new HotKeyEventArgs(_hotKey, _comboKey)); //呼叫自訂事件, 傳遞自訂參數
                    return true; //並攔截這個訊息, Form將不再接收到這個訊息
                }

                return false;
            }

            private bool disposed = false;

            public void Dispose()
            {
                if (!disposed)
                {
                    Win32Native.Methods.UnregisterHotKey(_hWnd, _hotKeyID); //取消熱鍵
                    Win32Native.Methods.GlobalDeleteAtom(_hotKeyID); //刪除id
                    OnHotkey = null; //取消所有關聯的事件
                    Application.RemoveMessageFilter(this); //不再使用HotKey類別監視訊息

                    GC.SuppressFinalize(this);
                    disposed = true;
                }
            }

            ~GlobalHotKey()
            {
                Dispose();
            }
        }

        public class HotKeyEventArgs : EventArgs
        {
            private Keys _hotKey;
            public Keys HotKey
            {
                get { return _hotKey; }
                private set { }
            }

            private Keys _comboKey;
            public Keys ComboKey
            {
                get { return _comboKey; }
                private set { }
            }

            public HotKeyEventArgs(Keys hotKey, Keys comboKey)
            {
                _hotKey = hotKey;
                _comboKey = comboKey;
            }
        }

}
