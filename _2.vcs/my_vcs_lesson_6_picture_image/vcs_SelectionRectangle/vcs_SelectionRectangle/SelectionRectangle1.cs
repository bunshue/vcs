using System.Drawing;
using System.Windows.Forms;

namespace vcs_SelectionRectangle
{
    class SelectionRec1
    {
        /// <summary>
        /// 圆的直径
        /// </summary>
        public int ResizePinSize = 6;   //預設ResizePin圓直徑大小

        //半径
        int HalfRPR
        {
            get { return ResizePinSize / 2; }
        }
        private static Pen SelectRectPen, ResizePinPen;
        private float[] SelectRectDashPattern;
        private static Rectangle SelectRect;
        private static Rectangle ResizePin1, ResizePin2, ResizePin3, ResizePin4, ResizePin5, ResizePin6, ResizePin7, ResizePin8;
        private static Rectangle rect;  
        private static int ActivationPinPosition;
        //selectrect的x,y,x1,y1
        private static int SelectX0, SelectY0, SelectX1, SelectY1;

        //8个角+点空白处+点中间
        private const int hitNothing = -1;
        private const int hitTopLeft = 0;
        private const int hitTopRight = 1;
        private const int hitBottomRight = 2;
        private const int hitBottomLeft = 3;
        private const int hitTop = 4;
        private const int hitRight = 5;
        private const int hitBottom = 6;
        private const int hitLeft = 7;
        private const int hitMiddle = 8;

        //HideResizePin//隐藏ResizePin
        private void HideResizePin()
        {
            ResizePin1.Width = 0; ResizePin1.Height = 0;
            ResizePin2.Width = 0; ResizePin2.Height = 0;
            ResizePin3.Width = 0; ResizePin3.Height = 0;
            ResizePin4.Width = 0; ResizePin4.Height = 0;
            ResizePin5.Width = 0; ResizePin5.Height = 0;
            ResizePin6.Width = 0; ResizePin6.Height = 0;
            ResizePin7.Width = 0; ResizePin7.Height = 0;
            ResizePin8.Width = 0; ResizePin8.Height = 0;
        }

        //SetResizePinVal 实时显示ResizePin
        void SetResizePinVal()
        {
            ResizePin1.X = X - HalfRPR;
            ResizePin1.Y = Y - HalfRPR;
            ResizePin2.X = X + Width / 2 - HalfRPR;
            ResizePin2.Y = Y - HalfRPR;
            ResizePin3.X = X + Width - HalfRPR;
            ResizePin3.Y = Y - HalfRPR;
            ResizePin4.X = X + Width - HalfRPR;
            ResizePin4.Y = Y + Height / 2 - HalfRPR;
            ResizePin5.X = X + Width - HalfRPR;
            ResizePin5.Y = Y + Height - HalfRPR;
            ResizePin6.X = X + Width / 2 - HalfRPR;
            ResizePin6.Y = Y + Height - HalfRPR;
            ResizePin7.X = X - HalfRPR;
            ResizePin7.Y = Y + Height - HalfRPR;
            ResizePin8.X = X - HalfRPR;
            ResizePin8.Y = Y + Height / 2 - HalfRPR;
        }

        //ShowResizePin//显示ResizePin
        private void ShowResizePin()
        {
            ResizePin1.X = SelectRect.X - HalfRPR;
            ResizePin1.Y = SelectRect.Y - HalfRPR;
            ResizePin2.X = SelectRect.X + SelectRect.Width / 2 - HalfRPR;
            ResizePin2.Y = SelectRect.Y - HalfRPR;
            ResizePin3.X = SelectRect.X + SelectRect.Width - HalfRPR;
            ResizePin3.Y = SelectRect.Y - HalfRPR;
            ResizePin4.X = SelectRect.X + SelectRect.Width - HalfRPR;
            ResizePin4.Y = SelectRect.Y + SelectRect.Height / 2 - HalfRPR;
            ResizePin5.X = SelectRect.X + SelectRect.Width - HalfRPR;
            ResizePin5.Y = SelectRect.Y + SelectRect.Height - HalfRPR;
            ResizePin6.X = SelectRect.X + SelectRect.Width / 2 - HalfRPR;
            ResizePin6.Y = SelectRect.Y + SelectRect.Height - HalfRPR;
            ResizePin7.X = SelectRect.X - HalfRPR;
            ResizePin7.Y = SelectRect.Y + SelectRect.Height - HalfRPR;
            ResizePin8.X = SelectRect.X - HalfRPR;
            ResizePin8.Y = SelectRect.Y + SelectRect.Height / 2 - HalfRPR;
            ResizePin1.Width = ResizePinSize; ResizePin1.Height = ResizePinSize;
            ResizePin2.Width = ResizePinSize; ResizePin2.Height = ResizePinSize;
            ResizePin3.Width = ResizePinSize; ResizePin3.Height = ResizePinSize;
            ResizePin4.Width = ResizePinSize; ResizePin4.Height = ResizePinSize;
            ResizePin5.Width = ResizePinSize; ResizePin5.Height = ResizePinSize;
            ResizePin6.Width = ResizePinSize; ResizePin6.Height = ResizePinSize;
            ResizePin7.Width = ResizePinSize; ResizePin7.Height = ResizePinSize;
            ResizePin8.Width = ResizePinSize; ResizePin8.Height = ResizePinSize;

        }

        //FillResizePins // 填充ResizePinRect颜色
        void FillResizePins(PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            e.Graphics.FillEllipse(Brushes.SteelBlue,ResizePin1);
            e.Graphics.FillEllipse(Brushes.SteelBlue, ResizePin2);
            e.Graphics.FillEllipse(Brushes.SteelBlue, ResizePin3);
            e.Graphics.FillEllipse(Brushes.SteelBlue, ResizePin4);
            e.Graphics.FillEllipse(Brushes.SteelBlue, ResizePin5);
            e.Graphics.FillEllipse(Brushes.SteelBlue, ResizePin6);
            e.Graphics.FillEllipse(Brushes.SteelBlue, ResizePin7);
            e.Graphics.FillEllipse(Brushes.SteelBlue, ResizePin8);
        }

        //DrawResizePin//绘制ResizePin
        void DrawResizePin(Graphics g)
        {
            g.DrawEllipse(ResizePinPen,ResizePin1);
            g.DrawEllipse(ResizePinPen,ResizePin2);
            g.DrawEllipse(ResizePinPen,ResizePin3);
            g.DrawEllipse(ResizePinPen,ResizePin4);
            g.DrawEllipse(ResizePinPen,ResizePin5);
            g.DrawEllipse(ResizePinPen,ResizePin6);
            g.DrawEllipse(ResizePinPen,ResizePin7);
            g.DrawEllipse(ResizePinPen,ResizePin8);
        }

        //InELP//是否在ResizePin圆内
        bool InELP(MouseEventArgs e,Point ElpCenter)
        {
            int elpX = ElpCenter.X;
            int elpY = ElpCenter.Y;
            return !((elpX - e.X) * (elpX - e.X) + (elpY - e.Y) * (elpY - e.Y) >= HalfRPR * HalfRPR);
        }

        //HitTest//测试哪个ResizePin被选中
        private int HitTest(MouseEventArgs e)
        {
            if(InELP(e,new Point(ResizePin1.X + HalfRPR,ResizePin1.Y + HalfRPR)))
                return hitTopLeft;
            else if (InELP(e,new Point(ResizePin2.X + HalfRPR, ResizePin2.Y + HalfRPR)))
                return hitTop;
            else if (InELP(e,new Point(ResizePin3.X + HalfRPR,ResizePin3.Y + HalfRPR)))
                return hitTopRight;
            else if (InELP(e, new Point(ResizePin4.X + HalfRPR, ResizePin4.Y + HalfRPR)))
                return hitRight;
            else if (InELP(e, new Point(ResizePin5.X + HalfRPR, ResizePin5.Y + HalfRPR)))
                return hitBottomRight;
            else if (InELP(e, new Point(ResizePin6.X + HalfRPR, ResizePin6.Y + HalfRPR)))
                return hitBottom;
            else if (InELP(e, new Point(ResizePin7.X + HalfRPR, ResizePin7.Y + HalfRPR)))
                return hitBottomLeft;
            else if (InELP(e, new Point(ResizePin8.X + HalfRPR, ResizePin8.Y + HalfRPR)))
                return hitLeft;
            else if (e.X >= SelectRect.X + ResizePinSize && e.X <= SelectRect.X + SelectRect.Width - ResizePinSize
                        && e.Y >= SelectRect.Y + ResizePinSize && e.Y <= SelectRect.Y + SelectRect.Height - ResizePinSize)
                return hitMiddle;
            else
                return hitNothing;
        }

        //Create    //初始化参数
        public void Create()
        {
            ResizePinPen = new Pen(Color.SteelBlue, 2);
            SelectRectDashPattern = new float[] {3,2,1};

            SelectRectPen = new Pen(Color.SteelBlue, 2.0f);
            //{
            //    DashPattern = SelectRectDashPattern,
            //};
            SelectRect = new Rectangle();
            ResizePin1 = new Rectangle();
            ResizePin2 = new Rectangle();
            ResizePin3 = new Rectangle();
            ResizePin4 = new Rectangle();
            ResizePin5 = new Rectangle();
            ResizePin6 = new Rectangle();
            ResizePin7 = new Rectangle();
            ResizePin8 = new Rectangle();
            rect = new Rectangle();
            ActivationPinPosition = hitNothing;
        }

        //待在box里面别出去
        void StayInBoxR(PictureBox R)
        {
            if (SelectRect.X < 0)
                SelectRect.X = 0;
            if (SelectRect.Y < 0)
                SelectRect.Y = 0;
            if (SelectRect.X + SelectRect.Width >  R.Width)
                SelectRect.X = R.Width - SelectRect.Width;
            if (SelectRect.Y + SelectRect.Height > R.Height)
                SelectRect.Y = R.Height - SelectRect.Height;
        }

        //Destroy  //释放资源
        public void Destroy()
        {
            SelectRectPen.Dispose();
            ResizePinPen.Dispose();
        }

        //StartPoint//鼠标左键按下后
        public void StartPoint(PictureBox p, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                p.Invalidate(null, true);
                switch (HitTest(e))
                {
                    case hitTopLeft:
                        ActivationPinPosition = hitTopLeft;
                        SelectX1 = SelectRect.X + SelectRect.Width;
                        SelectY1 = SelectRect.Y + SelectRect.Height;
                        break;
                    case hitTop:
                        ActivationPinPosition = hitTop;
                        SelectX1 = SelectRect.Width + SelectRect.X;
                        SelectY1 = SelectRect.Height + SelectY0;
                        break;
                    case hitTopRight:
                        ActivationPinPosition = hitTopRight;
                        SelectY1 = SelectRect.Y + SelectRect.Height;
                        break;
                    case hitRight:
                        ActivationPinPosition = hitRight;
                        SelectY1 = SelectRect.Y + SelectRect.Height;
                        break;
                    case hitBottomRight:
                        ActivationPinPosition = hitBottomRight;
                        break;
                    case hitBottom:
                        ActivationPinPosition = hitBottom;
                        SelectX1 = SelectRect.X + SelectRect.Width;
                        break;
                    case hitBottomLeft:
                        ActivationPinPosition = hitBottomLeft;
                        SelectX1 = SelectRect.X + SelectRect.Width;
                        break;
                    case hitLeft:
                        ActivationPinPosition = hitLeft;
                        SelectX1 = SelectRect.X + SelectRect.Width;
                        SelectY1 = SelectRect.Y + SelectRect.Height;
                        break;
                    case hitMiddle:
                        ActivationPinPosition = hitMiddle;
                        SelectX0 = e.X - SelectRect.X;
                        SelectY0 = e.Y - SelectRect.Y;
                        SelectX1 = SelectRect.X + SelectRect.Width - e.X;
                        SelectY1 = SelectRect.Y + SelectRect.Height - e.Y;
                        break;
                    case hitNothing:
                        ActivationPinPosition = hitNothing;
                        SelectRect.Width = 0;
                        SelectRect.Height = 0;
                        SelectX0 = e.X;
                        SelectY0 = e.Y;
                        HideResizePin();
                        break;
                }
            }
        }

        //TrackRubberBand //鼠标左键拖动时动态显示矩形框
        public void TrackRubberBand(PictureBox p, MouseEventArgs e, bool Iskeep = false)
        {
            switch (HitTest(e))
            {
                case hitTopLeft:
                    p.Cursor = Cursors.SizeNWSE;
                    break;
                case hitTop:
                    p.Cursor = Cursors.SizeNS;
                    break;
                case hitTopRight:
                    p.Cursor = Cursors.SizeNESW;
                    break;
                case hitRight:
                    p.Cursor = Cursors.SizeWE;
                    break;
                case hitBottomRight:
                    p.Cursor = Cursors.SizeNWSE;
                    break;
                case hitBottom:
                    p.Cursor = Cursors.SizeNS;
                    break;
                case hitBottomLeft:
                    p.Cursor = Cursors.SizeNESW;
                    break;
                case hitLeft:
                    p.Cursor = Cursors.SizeWE;
                    break;
                case hitMiddle:
                    p.Cursor = Cursors.SizeAll;
                    break;
                case hitNothing:
                    p.Cursor = Cursors.Default;
                    break;
            }
            if (e.Button == MouseButtons.Left)
            {
                int TLX = e.X;
                int TLY = e.Y;

                if (e.X < 0)
                    TLX = 0;
                else if (e.X > p.Width)
                    TLX = p.Width;

                if (e.Y < 0)
                    TLY = 0;
                else if (e.Y > p.Height)
                    TLY = p.Height;
                if (!Iskeep)
                {
                    p.Invalidate(InvalidateRectangle(), false);
                }

                switch (ActivationPinPosition)
                {
                    case hitTopLeft:
                        GenerateRectangle(ref SelectRect, TLX, TLY, SelectX1, SelectY1);
                        StayInBoxR(p);
                        SetResizePinVal();
                        break;
                    case hitTop:
                        GenerateRectangle(ref SelectRect, SelectX0, TLY, SelectX1, SelectY1);
                        StayInBoxR(p);
                        SetResizePinVal();
                        break;
                    case hitTopRight:
                        GenerateRectangle(ref SelectRect, SelectX0, TLY, TLX, SelectY1);
                        StayInBoxR(p);
                        SetResizePinVal();
                        break;
                    case hitRight:
                        GenerateRectangle(ref SelectRect, SelectX0, SelectY0, TLX, SelectY1);
                        StayInBoxR(p);
                        SetResizePinVal();
                        break;
                    case hitBottomRight:
                        GenerateRectangle(ref SelectRect, SelectX0, SelectY0, TLX, TLY);
                        StayInBoxR(p);
                        SetResizePinVal();
                        break;
                    case hitBottom:
                        GenerateRectangle(ref SelectRect, SelectX0, SelectY0, SelectX1, TLY);
                        StayInBoxR(p);
                        SetResizePinVal();
                        break;
                    case hitBottomLeft:
                        GenerateRectangle(ref SelectRect, TLX, SelectY0, SelectX1, TLY);
                        StayInBoxR(p);
                        SetResizePinVal();
                        break;
                    case hitLeft:
                        GenerateRectangle(ref SelectRect, TLX, SelectY0, SelectX1, SelectY1);
                        StayInBoxR(p);
                        SetResizePinVal();
                        break;
                    case hitMiddle:
                        GenerateRectangle(ref SelectRect, e.X - SelectX0, e.Y - SelectY0, e.X + SelectX1, e.Y + SelectY1);
                        StayInBoxR(p);
                        SetResizePinVal();
                        break;
                    case hitNothing:
                        GenerateRectangle(ref SelectRect, SelectX0, SelectY0, TLX, TLY);
                        StayInBoxR(p);
                        SetResizePinVal();
                        break;
                }
            }
        }

        //EndPoint//鼠标左键放開後
        public void EndPoint(PictureBox frm, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                frm.Invalidate(null, true);
                SelectX0 = SelectRect.X;
                SelectY0 = SelectRect.Y;
                if(HitTest(e) != hitNothing && X > ResizePinSize && Y > ResizePinSize)
                    ShowResizePin();
            }
        }

        //DrawRubberBand //绘制矩形框
        public void DrawRubberBand(PictureBox frm, PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(SelectRectPen, SelectRect);
            FillResizePins(e);
            DrawResizePin(e.Graphics);
        }

        //GenerateRectangle //根据指定两点坐标生成矩形框
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

        //RubberBandAttribute //RubberBand的属性
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

        //public Pen RectView;

        //InvalidateRectangle //获得无效区域，用来刷新时防止闪烁
        public Rectangle InvalidateRectangle()
        {
            rect.X = SelectRect.X - 8;
            rect.Y = SelectRect.Y - 8;
            rect.Width = SelectRect.Width + 16;
            rect.Height = SelectRect.Height + 16;

            return rect;
        }

        /// <summary>
        /// set ccs框的位置以及尺寸
        /// </summary>
        /// <param name="ex">x坐标</param>
        /// <param name="ey">y坐标</param>
        /// <param name="ew">宽</param>
        /// <param name="eh">高</param>
        public void SetRect(int ex, int ey, int ew, int eh)
        {
            GenerateRectangle(ref SelectRect, ex, ey, ex + ew, ey + eh);
        }

        //隐藏起来
        public void HideCCS()
        {
            HideResizePin();
            SetRect(0, 0, 0, 0);
        }
    }
}
