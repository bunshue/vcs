using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MouseControl
{
    static public class MouseLogicControl
    {
        /// <summary>
        /// 要觸發的事件
        /// </summary>
        public enum EventType : byte
        {
            /// <summary>
            /// 滑鼠左鍵點擊
            /// </summary>
            LeftClick = 1,
            /// <summary>
            /// 滑鼠右鍵點擊
            /// </summary>
            RightClick = 2,
            /// <summary>
            /// 滑鼠中鍵點擊
            /// </summary>
            MidClick = 3,
            /// <summary>
            /// 滑鼠移到某個位置
            /// </summary>
            MoveToSpecifiedLocation = 4,
            /// <summary>
            /// 滑鼠左鍵拖曳
            /// </summary>
            LeftDrag = 5,
            /// <summary>
            /// 滑鼠右鍵拖曳
            /// </summary>
            RightDrag = 6,
            /// <summary>
            /// 滑鼠左鍵雙點擊
            /// </summary>
            LeftDoubleClick = 7,
            /// <summary>
            /// 滑鼠右鍵雙點擊
            /// </summary>
            RightDoubleClick = 8,
            /// <summary>
            /// 滑鼠左鍵按下
            /// </summary>
            LeftDown = 9,
            /// <summary>
            /// 滑鼠右鍵按下
            /// </summary>
            RightDown = 10,
            /// <summary>
            /// 滑鼠左鍵放開
            /// </summary>
            LeftUp = 11,
            /// <summary>
            /// 滑鼠右鍵放開
            /// </summary>
            RightUp = 12,
            /// <summary>
            /// 滑鼠中鍵按下
            /// </summary>
            MidDown = 13,
            /// <summary>
            /// 滑鼠中鍵放開
            /// </summary>
            MidUp = 14,
        }

        public struct Config
        {
            public System.Drawing.Point Location;
        }

        /// <summary>
        /// 控制滑鼠
        /// </summary>
        /// <param name="_t">要做的動作</param>
        /// <param name="_c">傳入的參數</param>
        public static void ControlMouse(EventType _t, Config _c)
        {
            Win32Native.Structures.INPUT input = new Win32Native.Structures.INPUT();
            input.dwType = Win32Native.Structures.INPUTTYPE.Mouse;
            input.mi = new Win32Native.Structures.MOUSEINPUT();
            input.mi.dwExtraInfo = IntPtr.Zero;
            input.mi.dx = 0;
            input.mi.dy = 0;
            input.mi.time = 0;
            input.mi.mouseData = 0;

            switch (_t)
            {
                case EventType.LeftClick:
                    MouseLogicControl.Click(ClcikType.Left);
                    break;
                case EventType.LeftDoubleClick:
                    MouseLogicControl.Click(ClcikType.Left);
                    System.Threading.Thread.Sleep(50);
                    MouseLogicControl.Click(ClcikType.Left);
                    break;
                case EventType.LeftDown:
                    MouseLogicControl.Mouse(EventType.LeftDown);
                    break;
                case EventType.LeftDrag:                    
                    MouseLogicControl.Mouse(EventType.LeftDown);
                    System.Threading.Thread.Sleep(100);
                    Win32Native.Methods.SetCursorPos(_c.Location.X, _c.Location.Y);
                    System.Threading.Thread.Sleep(100);
                    MouseLogicControl.Mouse(EventType.LeftUp);
                    break;
                case EventType.LeftUp:
                    MouseLogicControl.Mouse(EventType.LeftUp);
                    break;
                case EventType.MidClick:
                    MouseLogicControl.Click(ClcikType.Mid);
                    break;
                case EventType.MoveToSpecifiedLocation:    
                    Win32Native.Methods.SetCursorPos(_c.Location.X, _c.Location.Y);
                    break;
                case EventType.RightClick:
                    MouseLogicControl.Click(ClcikType.Right);
                    break;
                case EventType.RightDoubleClick:
                    MouseLogicControl.Click(ClcikType.Right);
                    System.Threading.Thread.Sleep(50);
                    MouseLogicControl.Click(ClcikType.Right);
                    break;
                case EventType.RightDown:
                    MouseLogicControl.Mouse(EventType.RightDown);
                    break;
                case EventType.RightDrag:                   //
                    MouseLogicControl.Mouse(EventType.RightDown);
                    System.Threading.Thread.Sleep(100);
                    Win32Native.Methods.SetCursorPos(_c.Location.X, _c.Location.Y);
                    System.Threading.Thread.Sleep(100);
                    MouseLogicControl.Mouse(EventType.RightUp);
                    break;
                case EventType.RightUp:
                    MouseLogicControl.Mouse(EventType.RightUp);
                    break;
                default:
                    break;
            }
        }

        /// <summary>
        /// 要點擊的滑鼠
        /// </summary>
        public enum ClcikType : byte
        {
            /// <summary>
            /// 左邊
            /// </summary>
            Left = 0,
            /// <summary>
            /// 右邊
            /// </summary>
            Right = 1,
            /// <summary>
            /// 中間
            /// </summary>
            Mid = 2,
        }

        /// <summary>
        /// 點擊某個滑鼠按鍵
        /// </summary>
        /// <param name="CT"></param>
        public static void Click(ClcikType CT)
        {
            switch (CT)
            {
                case ClcikType.Left:        //如果要點擊左鍵
                    MouseLogicControl.Mouse(EventType.LeftDown);
                    System.Threading.Thread.Sleep(20);
                    MouseLogicControl.Mouse(EventType.LeftUp);
                    break;
                case ClcikType.Right:       //右鍵
                    MouseLogicControl.Mouse(EventType.RightDown);
                    System.Threading.Thread.Sleep(20);
                    MouseLogicControl.Mouse(EventType.RightUp);
                    break;
                case ClcikType.Mid:         //中鍵
                    MouseLogicControl.Mouse(EventType.MidDown);
                    System.Threading.Thread.Sleep(20);
                    MouseLogicControl.Mouse(EventType.MidUp);
                    break;
                default:
                    break;
            }
        }

        /// <summary>
        /// 控制滑鼠
        /// </summary>
        /// <param name="_t">觸發的事件，只接受leftup . leftdown . rightup . rightdown . midup , middown</param>
        public static void Mouse(EventType _t)
        {

            Win32Native.Structures.INPUT input = new Win32Native.Structures.INPUT();

            input.dwType = Win32Native.Structures.INPUTTYPE.Mouse;
            input.mi = new Win32Native.Structures.MOUSEINPUT();
            input.mi.dwExtraInfo = IntPtr.Zero;
            input.mi.dx = 0;
            input.mi.dy = 0;
            input.mi.time = 0;
            input.mi.mouseData = 0;
            switch (_t)
            {
                case EventType.LeftUp:
                    input.mi.dwFlags = Win32Native.Structures.MOUSEFLAG.LEFTUP;
                    break;
                case EventType.LeftDown:
                    input.mi.dwFlags = Win32Native.Structures.MOUSEFLAG.LEFTDOWN;
                    break;
                case EventType.RightUp:
                    input.mi.dwFlags = Win32Native.Structures.MOUSEFLAG.RIGHTUP;
                    break;
                case EventType.RightDown:
                    input.mi.dwFlags = Win32Native.Structures.MOUSEFLAG.RIGHTDOWN;
                    break;
                case EventType.MidDown:
                    input.mi.dwFlags = Win32Native.Structures.MOUSEFLAG.MIDDLEDOWN;
                    break;
                case EventType.MidUp:
                    input.mi.dwFlags = Win32Native.Structures.MOUSEFLAG.MIDDLEUP;
                    break;
                default:
                    break;
            }

            if (_t == EventType.MidUp || _t == EventType.MidDown || _t == EventType.LeftUp || _t == EventType.LeftDown ||
                _t == EventType.RightUp || _t == EventType.RightDown)
                Win32Native.Methods.SendInput(1, ref input, System.Runtime.InteropServices.Marshal.SizeOf(typeof(Win32Native.Structures.INPUT)));
        }



        public enum MoveDirection : byte
        {
            Up = 0 ,
            Down = 1 ,
            Left = 2 ,
            Right = 3 ,
            LeftUp = 4 ,
            LeftDown = 5 ,
            RightUp = 6 ,
            RightDown = 7 ,
        }


        public static void SetCursorLocation(MoveDirection _d, Int16 _shiftAmmount)
        {
            //先取得目前滑鼠位置
            System.Drawing.Point pt ;
            Win32Native.Methods.GetCursorPos(out pt);
            switch (_d)
            {
                case MoveDirection.Up:
                    pt.Y -= _shiftAmmount;
                    break;
                case MoveDirection.Down:
                    pt.Y += _shiftAmmount;
                    break;
                case MoveDirection.Left:
                    pt.X -= _shiftAmmount;
                    break;
                case MoveDirection.Right:
                    pt.X += _shiftAmmount;
                    break;
                case MoveDirection.LeftUp:
                    pt.X -= _shiftAmmount;
                    pt.Y -= _shiftAmmount;
                    break;
                case MoveDirection.LeftDown:
                    pt.X -= _shiftAmmount;
                    pt.Y += _shiftAmmount;
                    break;
                case MoveDirection.RightUp:
                    pt.X += _shiftAmmount;
                    pt.Y -= _shiftAmmount;
                    break;
                case MoveDirection.RightDown:
                    pt.X += _shiftAmmount;
                    pt.Y += _shiftAmmount;
                    break;
                default:
                    break;
            }

            Win32Native.Methods.SetCursorPos(pt.X, pt.Y);
        }

    }
}
