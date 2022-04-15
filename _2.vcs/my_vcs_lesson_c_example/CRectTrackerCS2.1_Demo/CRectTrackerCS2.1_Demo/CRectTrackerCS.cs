/*
 * CRectTrackerCS 2.1
 * 作者：天津 赵春生
 * 制作时间：17:55 2007-06-01
 * 主页：http://timw.yeah.net or http://timw.126.com
 *	本程序代码测试环境：
 * WinXP (Professional SP2)
 * Microsoft Visual Studio 2005 (Installed Edition: C# Express)
 * Version 8.0.50727.762  (SP.050727-7600)
 * Microsoft .NET Framework
 * Version 2.0.50727
 * 
 * History:
 * 17:55 2007-06-01 2.1 Bug in the SetRubberBandStyle fixed
 * 15:51 2007-05-31 2.0 "SetRubberBandStyle LoadDefaultRubberBandStyle
 *                      HitTest HideResizePin ShowResizePin DrawResizePin
 *                      InvalidateRectangle" Added
 * 23:28 2007-05-26 1.0 Some Bugs Were Fixed(EndPoint)
 * 22:33 2007-05-24 1.0a Attribute---"RubberBandAttribute" Added
 * 15:10 2007-05-23 1.0a First Version
*/

using System;
using System.Collections.Generic;
using System.Text;
using System.Windows.Forms;//MessageBox
using System.Drawing;

namespace CustomCRectTrackerCS
{
    public class CRectTrackerCS
    {
        private static Pen SelectRectPen, ResizePinPen, SelectRectPenSolidLine/*实心*/;
        private float[] SelectRectDashPattern;
        private float SelectRectDashOffset;
        private static Rectangle SelectRect;
        private static Rectangle ResizePin1, ResizePin2, ResizePin3, ResizePin4,
            ResizePin5, ResizePin6, ResizePin7, ResizePin8;
        private static Rectangle rect;//InvalidateRectangle()
        private static int ActivationPinPosition;
        private static int SelectX0, SelectY0, SelectX1, SelectY1;
        public StyleFlags m_nStyle;

        private static int hitNothing = -1; private static int hitTopLeft = 0; private static int hitTopRight = 1;
        private static int hitBottomRight = 2; private static int hitBottomLeft = 3; private static int hitTop = 4;
        private static int hitRight = 5; private static int hitBottom = 6; private static int hitLeft = 7;
        private static int hitMiddle = 8;


        #region StyleFlags//RubberBand风格
        public enum StyleFlags
        {
            ResizePinNoHide = 1, ResizePinAutoHide = 2, ResizePinAlwaysHide = 4,
            SolidLine = 8, DottedLine = 16,
        };
        #endregion

        #region SetRubberBandStyle//设置RubberBand风格
        public void SetRubberBandStyle(StyleFlags nStyle, Color ResizePinColor, Color RubberBandColor)
        {
            m_nStyle = nStyle;
            ResizePinPen.Color = ResizePinColor;
            SelectRectPen.Color = RubberBandColor;
            SelectRectPenSolidLine.Color = RubberBandColor;
        }
        #endregion
        #region SetRubberBandStyle//设置RubberBand风格
        public void SetRubberBandStyle(StyleFlags nStyle)
        {
            if (((nStyle & (StyleFlags.DottedLine | StyleFlags.SolidLine)) != 0) &&
            ((nStyle & (StyleFlags.ResizePinAlwaysHide | StyleFlags.ResizePinAutoHide | StyleFlags.ResizePinNoHide)) != 0))
                m_nStyle = nStyle;
            else
            {
                int OldStyle0 = 0;
                int OldStyle1 = 0;
                if ((m_nStyle & StyleFlags.DottedLine) != 0)
                {
                    OldStyle0 = (int)StyleFlags.DottedLine;
                }
                else if ((m_nStyle & StyleFlags.SolidLine) != 0)
                {
                    OldStyle0 = (int)StyleFlags.SolidLine;
                }
                if ((m_nStyle & StyleFlags.ResizePinAlwaysHide) != 0)
                {
                    OldStyle1 = (int)StyleFlags.ResizePinAlwaysHide;
                }
                else if ((m_nStyle & StyleFlags.ResizePinAutoHide) != 0)
                {
                    OldStyle1 = (int)StyleFlags.ResizePinAutoHide;
                }
                else if ((m_nStyle & StyleFlags.ResizePinNoHide) != 0)
                {
                    OldStyle1 = (int)StyleFlags.ResizePinNoHide;
                }

                m_nStyle = 0;

                if ((nStyle & (StyleFlags.DottedLine | StyleFlags.SolidLine)) != 0)
                    m_nStyle = OldStyle1 + nStyle;
                else
                    m_nStyle = OldStyle0 + nStyle;
            }
        }
        #endregion
        #region SetRubberBandStyle//设置RubberBand风格
        public void SetRubberBandStyle(Color ResizePinColor, Color RubberBandColor)
        {
            ResizePinPen.Color = ResizePinColor;
            SelectRectPen.Color = RubberBandColor;
            SelectRectPenSolidLine.Color = RubberBandColor;
        }
        #endregion

        #region LoadDefaultRubberBandStyle//加载RubberBand的默认风格
        public void LoadDefaultRubberBandStyle()
        {
            SetRubberBandStyle(CRectTrackerCS.StyleFlags.DottedLine | CRectTrackerCS.StyleFlags.ResizePinNoHide,
                Color.SteelBlue, Color.SteelBlue);
        }
        #endregion

        #region HideResizePin//隐藏ResizePin
        private void HideResizePin()
        {
            //在鼠标按下后8PIN消失显示，在这里X和Y不用置0即可实现。
            ResizePin1.Width = 0; ResizePin1.Height = 0;
            ResizePin2.Width = 0; ResizePin2.Height = 0;
            ResizePin3.Width = 0; ResizePin3.Height = 0;
            ResizePin4.Width = 0; ResizePin4.Height = 0;
            ResizePin5.Width = 0; ResizePin5.Height = 0;
            ResizePin6.Width = 0; ResizePin6.Height = 0;
            ResizePin7.Width = 0; ResizePin7.Height = 0;
            ResizePin8.Width = 0; ResizePin8.Height = 0;
            //处理结束
        }
        #endregion

        #region ShowResizePin//显示ResizePin
        private void ShowResizePin()
        {
            //填充8个PIN的位置
            ResizePin1.X = SelectRect.X - 1;
            ResizePin1.Y = SelectRect.Y - 1;
            ResizePin2.X = SelectRect.X + SelectRect.Width / 2;
            ResizePin2.Y = SelectRect.Y - 1;
            ResizePin3.X = SelectRect.X + SelectRect.Width;
            ResizePin3.Y = SelectRect.Y - 1;
            ResizePin4.X = SelectRect.X + SelectRect.Width;
            ResizePin4.Y = SelectRect.Y + SelectRect.Height / 2;
            ResizePin5.X = SelectRect.X + SelectRect.Width;
            ResizePin5.Y = SelectRect.Y + SelectRect.Height;
            ResizePin6.X = SelectRect.X + SelectRect.Width / 2;
            ResizePin6.Y = SelectRect.Y + SelectRect.Height;
            ResizePin7.X = SelectRect.X - 1;
            ResizePin7.Y = SelectRect.Y + SelectRect.Height;
            ResizePin8.X = SelectRect.X - 1;
            ResizePin8.Y = SelectRect.Y + SelectRect.Height / 2;

            ResizePin1.Width = 1; ResizePin1.Height = 1;
            ResizePin2.Width = 1; ResizePin2.Height = 1;
            ResizePin3.Width = 1; ResizePin3.Height = 1;
            ResizePin4.Width = 1; ResizePin4.Height = 1;
            ResizePin5.Width = 1; ResizePin5.Height = 1;
            ResizePin6.Width = 1; ResizePin6.Height = 1;
            ResizePin7.Width = 1; ResizePin7.Height = 1;
            ResizePin8.Width = 1; ResizePin8.Height = 1;
            //填充完毕
        }
        #endregion

        #region DrawResizePin//绘制ResizePin
        private void DrawResizePin(PaintEventArgs e)
        {
            //绘制8PIN
            e.Graphics.DrawRectangle(ResizePinPen, ResizePin1);
            e.Graphics.DrawRectangle(ResizePinPen, ResizePin2);
            e.Graphics.DrawRectangle(ResizePinPen, ResizePin3);
            e.Graphics.DrawRectangle(ResizePinPen, ResizePin4);
            e.Graphics.DrawRectangle(ResizePinPen, ResizePin5);
            e.Graphics.DrawRectangle(ResizePinPen, ResizePin6);
            e.Graphics.DrawRectangle(ResizePinPen, ResizePin7);
            e.Graphics.DrawRectangle(ResizePinPen, ResizePin8);
            //绘制完毕
        }
        #endregion

        #region HitTest//测试哪个ResizePin被选中
        private int HitTest(MouseEventArgs e)
        {
            if (e.X >= SelectRect.X - 2 && e.X <= SelectRect.X + 2
                && e.Y >= SelectRect.Y - 2 && e.Y <= SelectRect.Y + 2)
                return hitTopLeft;
            else if (e.X >= SelectRect.X + (SelectRect.Width / 2) - 2 && e.X <= SelectRect.X + (SelectRect.Width / 2) + 2
                && e.Y >= SelectRect.Y - 2 && e.Y <= SelectRect.Y + 2)
                return hitTop;
            else if (e.X >= SelectRect.X + SelectRect.Width - 2 && e.X <= SelectRect.X + SelectRect.Width + 2
          && e.Y >= SelectRect.Y - 2 && e.Y <= SelectRect.Y + 2)
                return hitTopRight;
            else if (e.X >= SelectRect.X + SelectRect.Width - 2 && e.X <= SelectRect.X + SelectRect.Width + 2
     && e.Y >= SelectRect.Y + (SelectRect.Height / 2) - 2 && e.Y <= SelectRect.Y + (SelectRect.Height / 2) + 2)
                return hitRight;
            else if (e.X >= SelectRect.X + SelectRect.Width - 2 && e.X <= SelectRect.X + SelectRect.Width + 2
&& e.Y >= SelectRect.Y + SelectRect.Height - 2 && e.Y <= SelectRect.Y + SelectRect.Height + 2)
                return hitBottomRight;
            else if (e.X >= SelectRect.X + (SelectRect.Width / 2) - 2 && e.X <= SelectRect.X + (SelectRect.Width / 2) + 2
      && e.Y >= SelectRect.Y + SelectRect.Height - 2 && e.Y <= SelectRect.Y + SelectRect.Height + 2)
                return hitBottom;
            else if (e.X >= SelectRect.X - 2 && e.X <= SelectRect.X + 2
 && e.Y >= SelectRect.Y + SelectRect.Height - 2 && e.Y <= SelectRect.Y + SelectRect.Height + 2)
                return hitBottomLeft;
            else if (e.X >= SelectRect.X - 2 && e.X <= SelectRect.X + 2
&& e.Y >= SelectRect.Y + (SelectRect.Height / 2) - 2 && e.Y <= SelectRect.Y + (SelectRect.Height / 2) + 2)
                return hitLeft;
            else if (e.X >= SelectRect.X + 2 && e.X <= SelectRect.X + SelectRect.Width - 2
&& e.Y >= SelectRect.Y + 2 && e.Y <= SelectRect.Y + SelectRect.Height - 2)
                return hitMiddle;
            else
                return hitNothing;
        }
        #endregion

        #region Create//初始化参数
        public void Create()
        {
            //初始化
            ResizePinPen = new Pen(Color.SteelBlue, 2);
            SelectRectPenSolidLine = new Pen(Color.SteelBlue);//实心PEN
            SelectRectDashPattern = new float[] { 3.0f, 2.0f };
            SelectRectDashOffset = 5.0f;
            SelectRectPen = new System.Drawing.Pen(Color.SteelBlue);
            SelectRectPen.DashPattern = SelectRectDashPattern;
            SelectRect = new Rectangle();
            ResizePin1 = new Rectangle(); ResizePin2 = new Rectangle();
            ResizePin3 = new Rectangle(); ResizePin4 = new Rectangle();
            ResizePin5 = new Rectangle(); ResizePin6 = new Rectangle();
            ResizePin7 = new Rectangle(); ResizePin8 = new Rectangle();
            rect = new Rectangle();//InvalidateRectangle()

            ActivationPinPosition = hitNothing;

            LoadDefaultRubberBandStyle();
            //初始化结束

        }
        #endregion

        #region Destroy//释放资源
        public void Destroy()
        {
            SelectRectPen.Dispose();
            ResizePinPen.Dispose();
            SelectRectPenSolidLine.Dispose();
        }
        #endregion

        #region StartPoint//鼠标左键按下后
        public void StartPoint(Form frm, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                //当矩形框产生后，单击左键矩形框会立即消失，否则因定时器的间隔会产生停滞
                frm.Invalidate(null, true);

                //在鼠标按下后8PIN消失显示
                HideResizePin();

                //测试哪个PIN的被激活
                if (HitTest(e) == hitTopLeft)
                {
                    ActivationPinPosition = hitTopLeft;
                    SelectX1 = SelectRect.X + SelectRect.Width;
                    SelectY1 = SelectRect.Y + SelectRect.Height;
                }
                else if (HitTest(e) == hitTop)
                {
                    ActivationPinPosition = hitTop;
                    SelectX1 = SelectRect.Width + SelectRect.X;
                    SelectY1 = SelectRect.Height + SelectY0;
                }
                else if (HitTest(e) == hitTopRight)
                {
                    ActivationPinPosition = hitTopRight;
                    SelectY1 = SelectRect.Y + SelectRect.Height;
                }
                else if (HitTest(e) == hitRight)
                {
                    ActivationPinPosition = hitRight;
                    SelectY1 = SelectRect.Y + SelectRect.Height;
                }
                else if (HitTest(e) == hitBottomRight)
                {
                    ActivationPinPosition = hitBottomRight;
                }
                else if (HitTest(e) == hitBottom)
                {
                    ActivationPinPosition = hitBottom;
                    SelectX1 = SelectRect.X + SelectRect.Width;
                }
                else if (HitTest(e) == hitBottomLeft)
                {
                    ActivationPinPosition = hitBottomLeft;
                    SelectX1 = SelectRect.X + SelectRect.Width;
                }
                else if (HitTest(e) == hitLeft)
                {
                    ActivationPinPosition = hitLeft;
                    SelectX1 = SelectRect.X + SelectRect.Width;
                    SelectY1 = SelectRect.Y + SelectRect.Height;

                }
                else if (HitTest(e) == hitMiddle)
                {
                    ActivationPinPosition = hitMiddle;
                    SelectX0 = e.X - SelectRect.X;
                    SelectY0 = e.Y - SelectRect.Y;
                    SelectX1 = SelectRect.X + SelectRect.Width - e.X;
                    SelectY1 = SelectRect.Y + SelectRect.Height - e.Y;
                }
                else if (HitTest(e) == hitNothing)
                {
                    ActivationPinPosition = hitNothing;
                    //当鼠标不在PIN的作用范围内的时候，鼠标左键按下不弹起时矩形框则消失
                    //并且重新给X/Y赋值，准备重新创建一个矩形
                    SelectRect.Width = 0;
                    SelectRect.Height = 0;
                    SelectX0 = e.X;
                    SelectY0 = e.Y;
                }
                //测试完毕
            }
        }
        #endregion

        #region EndPoint//鼠标左键松开后
        public void EndPoint(Form frm, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                //在鼠标左键松开后会立即显示PIN，否则会出现停滞
                frm.Invalidate(null, true);

                //左键松开后立即重置矩形起始点坐标
                SelectX0 = SelectRect.X;
                SelectY0 = SelectRect.Y;

                if ((m_nStyle & (StyleFlags.ResizePinNoHide | StyleFlags.ResizePinAutoHide | StyleFlags.ResizePinAlwaysHide)) != 0)
                    if ((m_nStyle & StyleFlags.ResizePinNoHide | StyleFlags.ResizePinAutoHide) != 0)
                        ShowResizePin();
            }
        }
        #endregion

        #region DrawRubberBand //绘制矩形框
        public void DrawRubberBand(Form frm, PaintEventArgs e)
        {
            if ((m_nStyle & (StyleFlags.DottedLine | StyleFlags.SolidLine)) != 0)
            {
                if ((m_nStyle & StyleFlags.DottedLine) != 0)
                {
                    SelectRectPen.DashOffset = SelectRectDashOffset;
                    e.Graphics.DrawRectangle(SelectRectPen, SelectRect);//用虚线绘制
                    if ((SelectRectDashOffset -= 1.0f) == 0)
                        SelectRectDashOffset = 5.0f;//恢复，否则会一直减下去……
                }
                else
                {
                    e.Graphics.DrawRectangle(SelectRectPenSolidLine, SelectRect);//用实心PEN绘制
                }
            }


            if ((m_nStyle & (StyleFlags.ResizePinNoHide | StyleFlags.ResizePinAutoHide | StyleFlags.ResizePinAlwaysHide)) != 0)
            {
                if ((m_nStyle & StyleFlags.ResizePinNoHide) != 0)
                    DrawResizePin(e);
                //如果RubberBand的Style是AutoHide，并且当前指针不是Cross（默认十字指针时），则显示ResizePin。
                if (((m_nStyle & StyleFlags.ResizePinAutoHide) != 0) && frm.Cursor != Cursors.Cross)
                    DrawResizePin(e);
            }

        }
        #endregion

        #region TrackRubberBand //鼠标左键拖动时动态显示矩形框
        public void TrackRubberBand(Form frm, MouseEventArgs e)
        {
            //如果RubberBand的Style是AutoHide，并且当前指针不是Cross（默认十字指针时），
            //则每次移动鼠标都刷新，为的就是实时显示鼠标的效果。
            if (((m_nStyle & StyleFlags.ResizePinAutoHide) != 0) && frm.Cursor != Cursors.Cross)
                //frm.Invalidate(null, true);
                frm.Invalidate(InvalidateRectangle(), true);

            if (HitTest(e) == hitTopLeft)
            {
                frm.Cursor = Cursors.SizeNWSE;
            }
            else if (HitTest(e) == hitTop)
            {
                frm.Cursor = Cursors.SizeNS;
            }
            else if (HitTest(e) == hitTopRight)
            {
                frm.Cursor = Cursors.SizeNESW;
            }
            else if (HitTest(e) == hitRight)
            {
                frm.Cursor = Cursors.SizeWE;
            }
            else if (HitTest(e) == hitBottomRight)
            {
                frm.Cursor = Cursors.SizeNWSE;
            }
            else if (HitTest(e) == hitBottom)
            {
                frm.Cursor = Cursors.SizeNS;
            }
            else if (HitTest(e) == hitBottomLeft)
            {
                frm.Cursor = Cursors.SizeNESW;
            }
            else if (HitTest(e) == hitLeft)
            {
                frm.Cursor = Cursors.SizeWE;
            }
            else if (HitTest(e) == hitMiddle)
            {
                frm.Cursor = Cursors.SizeAll;
            }
            else if (HitTest(e) == hitNothing)
            {
                frm.Cursor = Cursors.Cross;
                //当鼠标在外部时且非左键按下时，将ActivationPinPosition置0(v1.0)
                if (e.Button != MouseButtons.Left)
                    ActivationPinPosition = hitNothing;
            }

            if (e.Button == MouseButtons.Left)
            {
                //在鼠标按下后8PIN消失显示，在这里X和Y不用置0即可实现。
                //防止没有在用户区域点击左键后出现残留8PIN的现象，如：
                //鼠标击中statusStrip后移动到用户区域(v1.0)
                HideResizePin();
                //处理结束

                //刷新间隔如果太大的话，在拖框的时候有迟滞现象，所以
                //要加上这句，意思是：在拖框的时候不断的刷新，以取消迟滞感。
                //frm.Invalidate(null, true);
                frm.Invalidate(InvalidateRectangle(), true);

                if (ActivationPinPosition == hitTopLeft)
                {
                    GenerateRectangle(ref SelectRect, e.X, e.Y, SelectX1, SelectY1);
                }
                else if (ActivationPinPosition == hitTop)
                {
                    GenerateRectangle(ref SelectRect, SelectX0, e.Y, SelectX1, SelectY1);
                }
                else if (ActivationPinPosition == hitTopRight)
                {
                    GenerateRectangle(ref SelectRect, SelectX0, e.Y, e.X, SelectY1);
                }
                else if (ActivationPinPosition == hitRight)
                {
                    GenerateRectangle(ref SelectRect, SelectX0, SelectY0, e.X, SelectY1);
                }
                else if (ActivationPinPosition == hitBottomRight)
                {
                    GenerateRectangle(ref SelectRect, SelectX0, SelectY0, e.X, e.Y);
                }
                else if (ActivationPinPosition == hitBottom)
                {
                    GenerateRectangle(ref SelectRect, SelectX0, SelectY0, SelectX1, e.Y);
                }
                else if (ActivationPinPosition == hitBottomLeft)
                {
                    GenerateRectangle(ref SelectRect, e.X, SelectY0, SelectX1, e.Y);
                }
                else if (ActivationPinPosition == hitLeft)
                {
                    GenerateRectangle(ref SelectRect, e.X, SelectY0, SelectX1, SelectY1);
                }
                else if (ActivationPinPosition == hitMiddle)
                {
                    GenerateRectangle(ref SelectRect, e.X - SelectX0, e.Y - SelectY0, e.X + SelectX1, e.Y + SelectY1);
                }
                else if (ActivationPinPosition == hitNothing)
                {
                    GenerateRectangle(ref SelectRect, SelectX0, SelectY0, e.X, e.Y);
                }

            }

        }
        #endregion

        #region GenerateRectangle //根据指定两点坐标生成矩形框
        private void GenerateRectangle(ref Rectangle TempRectangle, int X0, int Y0, int X1, int Y1)
        {
            if (X0 < X1)
            {
                TempRectangle.X = X0;
                TempRectangle.Width = X1 - X0;
            }
            else
            {
                TempRectangle.X = X1;
                TempRectangle.Width = X0 - X1;
            }
            if (Y0 < Y1)
            {
                TempRectangle.Y = Y0;
                TempRectangle.Height = Y1 - Y0;
            }
            else
            {
                TempRectangle.Y = Y1;
                TempRectangle.Height = Y0 - Y1;
            }
        }
        #endregion

        #region RubberBandAttribute //RubberBand的属性
        public int X
        {
            get
            {
                return SelectRect.X;
            }
        }
        public int Y
        {
            get
            {
                return SelectRect.Y;
            }
        }
        public int Width
        {
            get
            {
                return SelectRect.Width;
            }
        }
        public int Height
        {
            get
            {
                return SelectRect.Height;
            }
        }
        #endregion

        #region InvalidateRectangle //获得无效区域，用来刷新时防止闪烁
        public Rectangle InvalidateRectangle()
        {
            rect.X = SelectRect.X - 8;
            rect.Y = SelectRect.Y - 8;
            rect.Width = SelectRect.Width + 16;
            rect.Height = SelectRect.Height + 16;

            return rect;
        }
        #endregion

        #region Test //测试CRectTrackerCSTest是否正常
        public void Test()
        {
            MessageBox.Show("Test CRectTracker_CS_Demo.", "OK");
        }
        #endregion

    }
}
