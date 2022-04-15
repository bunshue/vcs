/******************************************************************
 * 创 建 人：  SamWang
 * 创建时间：  2012-5-10 17:00
 * 描    述：
 *             在控件外部加上边框，用于拖拉，以改变内部控件的大小
 * 原    理：
 * 版    本：  V1.0      
 * 环    境：  VS2010
******************************************************************/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing;
using System.Drawing.Drawing2D;

namespace DragControl
{
    public class FrameControl : UserControl
    {
        #region Constructors
        /// <summary>
        /// 构造函数
        /// </summary>
        public FrameControl(Control ctrl)
        {
            baseControl = ctrl;
            AddEvents();
            CreateBounds();
        }
        #endregion

        #region Fields
        const int Band = 6; //调整大小的响应边框
        private int MinWidth = 20; //最小宽度
        private int MinHeight = 20;//最小高度
        Size square = new Size(Band, Band);//小矩形大小
        Control baseControl; //基础控件，即被包围的控件
        Rectangle[] smallRects = new Rectangle[8];//边框中的八个小圆圈
        Rectangle[] sideRects = new Rectangle[4];//四条边框，用来做响应区域
        Point[] linePoints = new Point[5];//四条边，用于画虚线
        Graphics g; //画图板
        Rectangle ControlRect; //控件包含边框的区域  
        private Point pPoint; //上个鼠标坐标
        private Point cPoint; //当前鼠标坐标
        private MousePosOnCtrl mpoc;
        #endregion

        #region Properties
        /// <summary>
        /// 鼠标在控件中位置
        /// </summary>
        enum MousePosOnCtrl
        {
            NONE = 0,
            TOP = 1,
            RIGHT = 2,
            BOTTOM = 3,
            LEFT = 4,
            TOPLEFT = 5,
            TOPRIGHT = 6,
            BOTTOMLEFT = 7,
            BOTTOMRIGHT = 8,
        }
        #endregion

        #region Methods
        /// <summary>
        /// 加载事件
        /// </summary>
        private void AddEvents()
        {
            this.Name = "FrameControl" + baseControl.Name;
            this.MouseDown += new MouseEventHandler(FrameControl_MouseDown);
            this.MouseMove += new MouseEventHandler(FrameControl_MouseMove);
            this.MouseUp += new MouseEventHandler(FrameControl_MouseUp);
        }

        #region 创建边框
        /// <summary>
        /// 建立控件可视区域
        /// </summary>
        private void CreateBounds()
        {
            //创建边界
            int X = baseControl.Bounds.X - square.Width - 1;
            int Y = baseControl.Bounds.Y - square.Height - 1;
            int Height = baseControl.Bounds.Height + (square.Height * 2) + 2;
            int Width = baseControl.Bounds.Width + (square.Width * 2) + 2;
            this.Bounds = new Rectangle(X, Y, Width, Height);
            this.BringToFront();
            SetRectangles();
            //设置可视区域
            this.Region = new Region(BuildFrame());
            g = this.CreateGraphics();
        }

        /// <summary>
        /// 设置定义8个小矩形的范围
        /// </summary>
        void SetRectangles()
        {
            //左上
            smallRects[0] = new Rectangle(new Point(0, 0), square);
            //右上
            smallRects[1] = new Rectangle(new Point(this.Width - square.Width - 1, 0), square);
            //左下
            smallRects[2] = new Rectangle(new Point(0, this.Height - square.Height - 1), square);
            //右下
            smallRects[3] = new Rectangle(new Point(this.Width - square.Width - 1, this.Height - square.Height - 1), square);
            //上中
            smallRects[4] = new Rectangle(new Point(this.Width / 2 - 1, 0), square);
            //下中
            smallRects[5] = new Rectangle(new Point(this.Width / 2 - 1, this.Height - square.Height - 1), square);
            //左中
            smallRects[6] = new Rectangle(new Point(0, this.Height / 2 - 1), square);
            //右中
            smallRects[7] = new Rectangle(new Point(square.Width + baseControl.Width + 1, this.Height / 2 - 1), square);

            //四条边线
            //左上
            linePoints[0] = new Point(square.Width / 2, square.Height / 2);
            //右上
            linePoints[1] = new Point(this.Width - square.Width / 2 - 1, square.Height / 2);
            //右下
            linePoints[2] = new Point(this.Width - square.Width / 2 - 1, this.Height - square.Height / 2);
            //左下
            linePoints[3] = new Point(square.Width / 2, this.Height - square.Height / 2 - 1);
            //左上
            linePoints[4] = new Point(square.Width / 2, square.Height / 2);

            //整个包括周围边框的范围
            ControlRect = new Rectangle(new Point(0, 0), this.Bounds.Size);
        }

        /// <summary>
        /// 设置边框控件可视区域
        /// </summary>
        /// <returns></returns>
        private GraphicsPath BuildFrame()
        {
            GraphicsPath path = new GraphicsPath();
            //上边框
            sideRects[0] = new Rectangle(0, 0, this.Width - square.Width - 1, square.Height + 1);
            //左边框
            sideRects[1] = new Rectangle(0, square.Height + 1, square.Width + 1, this.Height - square.Height - 1);
            //下边框
            sideRects[2] = new Rectangle(square.Width + 1, this.Height - square.Height - 1, this.Width - square.Width - 1, square.Height + 1);
            //右边框
            sideRects[3] = new Rectangle(this.Width - square.Width - 1, 0, square.Width + 1, this.Height - square.Height - 1);

            path.AddRectangle(sideRects[0]);
            path.AddRectangle(sideRects[1]);
            path.AddRectangle(sideRects[2]);
            path.AddRectangle(sideRects[3]);
            return path;
        }
        #endregion

        /// <summary>
        /// 绘图
        /// </summary>
        public void Draw()
        {
            this.BringToFront();
            //g.FillRectangles(Brushes.LightGray, sideRects); //填充四条边框的内部
            Pen pen = new Pen(Color.Black);
            pen.DashStyle = DashStyle.Dot;//设置为虚线,用虚线画四边，模拟微软效果
            g.DrawLines(pen, linePoints);//绘制四条边线
            g.FillRectangles(Brushes.White, smallRects); //填充8个小矩形的内部
            foreach (Rectangle smallRect in smallRects)
            {
                g.DrawEllipse(Pens.Black, smallRect);    //绘制8个小椭圆
            }
            //g.DrawRectangles(Pens.Black, smallRects);  //绘制8个小矩形的黑色边线
        }

        /// <summary>
        /// 设置光标状态
        /// </summary>
        public bool SetCursorShape(int x, int y)
        {
            Point point = new Point(x, y);
            if (!ControlRect.Contains(point))
            {
                Cursor.Current = Cursors.Arrow;
                return false;
            }
            else if (smallRects[0].Contains(point))
            {
                Cursor.Current = Cursors.SizeNWSE;
                mpoc = MousePosOnCtrl.TOPLEFT;
            }
            else if (smallRects[1].Contains(point))
            {
                Cursor.Current = Cursors.SizeNESW;
                mpoc = MousePosOnCtrl.TOPRIGHT;
            }
            else if (smallRects[2].Contains(point))
            {
                Cursor.Current = Cursors.SizeNESW;
                mpoc = MousePosOnCtrl.BOTTOMLEFT;
            }
            else if (smallRects[3].Contains(point))
            {
                Cursor.Current = Cursors.SizeNWSE;
                mpoc = MousePosOnCtrl.BOTTOMRIGHT;
            }
            else if (sideRects[0].Contains(point))
            {
                Cursor.Current = Cursors.SizeNS;
                mpoc = MousePosOnCtrl.TOP;
            }
            else if (sideRects[1].Contains(point))
            {
                Cursor.Current = Cursors.SizeWE;
                mpoc = MousePosOnCtrl.LEFT;
            }
            else if (sideRects[2].Contains(point))
            {
                Cursor.Current = Cursors.SizeNS;
                mpoc = MousePosOnCtrl.BOTTOM;
            }
            else if (sideRects[3].Contains(point))
            {
                Cursor.Current = Cursors.SizeWE;
                mpoc = MousePosOnCtrl.RIGHT;
            }
            else
            {
                Cursor.Current = Cursors.Arrow;
            }
            return true;
        }

        /// <summary>
        /// 控件移动
        /// </summary>
        private void ControlMove()
        {
            cPoint = Cursor.Position;
            int x = cPoint.X - pPoint.X;
            int y = cPoint.Y - pPoint.Y;
            switch (this.mpoc)
            {
                case MousePosOnCtrl.TOP:
                    if (baseControl.Height - y > MinHeight)
                    {
                        baseControl.Top += y;
                        baseControl.Height -= y;                        
                    }
                    else
                    {
                        baseControl.Top -= MinHeight - baseControl.Height;
                        baseControl.Height = MinHeight;
                    }
                    break;
                case MousePosOnCtrl.BOTTOM:
                    if (baseControl.Height + y > MinHeight)
                    {
                        baseControl.Height += y;
                    }
                    else
                    {
                        baseControl.Height = MinHeight;
                    }
                    break;
                case MousePosOnCtrl.LEFT:
                    if (baseControl.Width - x > MinWidth)
                    {
                        baseControl.Left += x;
                        baseControl.Width -= x;                        
                    }
                    else
                    {
                        baseControl.Left -= MinWidth - baseControl.Width;
                        baseControl.Width = MinWidth;
                    }
                    
                    break;
                case MousePosOnCtrl.RIGHT:
                    if (baseControl.Width + x > MinWidth)
                    {
                        baseControl.Width += x;
                    }
                    else
                    {
                        baseControl.Width = MinWidth;
                    }
                    break;
                case MousePosOnCtrl.TOPLEFT:
                    if (baseControl.Height - y > MinHeight)
                    {
                        baseControl.Top += y;
                        baseControl.Height -= y;
                    }
                    else
                    {
                        baseControl.Top -= MinHeight - baseControl.Height;
                        baseControl.Height = MinHeight;
                    }
                    if (baseControl.Width - x > MinWidth)
                    {
                        baseControl.Left += x;
                        baseControl.Width -= x;
                    }
                    else
                    {
                        baseControl.Left -= MinWidth - baseControl.Width;
                        baseControl.Width = MinWidth;
                    }
                    break;
                case MousePosOnCtrl.TOPRIGHT:
                    if (baseControl.Height - y > MinHeight)
                    {
                        baseControl.Top += y;
                        baseControl.Height -= y;
                    }
                    else
                    {
                        baseControl.Top -= MinHeight - baseControl.Height;
                        baseControl.Height = MinHeight;
                    }
                    if (baseControl.Width + x > MinWidth)
                    {
                        baseControl.Width += x;
                    }
                    else
                    {
                        baseControl.Width = MinWidth;
                    }
                    break;               
                case MousePosOnCtrl.BOTTOMLEFT:
                    if (baseControl.Height + y > MinHeight)
                    {
                        baseControl.Height += y;
                    }
                    else
                    {
                        baseControl.Height = MinHeight;
                    }
                    if (baseControl.Width - x > MinWidth)
                    {
                        baseControl.Left += x;
                        baseControl.Width -= x;
                    }
                    else
                    {
                        baseControl.Left -= MinWidth - baseControl.Width;
                        baseControl.Width = MinWidth;
                    }
                    break;
                case MousePosOnCtrl.BOTTOMRIGHT:
                    if (baseControl.Height + y > MinHeight)
                    {
                        baseControl.Height += y;
                    }
                    else
                    {
                        baseControl.Height = MinHeight;
                    }
                    if (baseControl.Width + x > MinWidth)
                    {
                        baseControl.Width += x;
                    }
                    else
                    {
                        baseControl.Width = MinWidth;
                    }
                    break;
                
            }
            pPoint = Cursor.Position;
        }        

        #endregion

        #region Events
        /// <summary>
        /// 鼠标按下事件：记录当前鼠标相对窗体的坐标
        /// </summary>
        void FrameControl_MouseDown(object sender, MouseEventArgs e)
        {
            pPoint = Cursor.Position;
        }

        /// <summary>
        /// 鼠标移动事件：让控件跟着鼠标移动
        /// </summary>
        void FrameControl_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                this.Visible = false;
                MoveControl.DrawDragBound(baseControl);
                ControlMove();
            }
            else
            {
                this.Visible = true;
                SetCursorShape(e.X, e.Y); //更新鼠标指针样式
            }
        }

        /// <summary>
        /// 鼠标弹起事件：让自定义的边框出现
        /// </summary>
        void FrameControl_MouseUp(object sender, MouseEventArgs e)
        {
            this.baseControl.Refresh(); //刷掉黑色边框
            this.Visible = true;
            CreateBounds();
            Draw();
        }
        #endregion
    }
}
