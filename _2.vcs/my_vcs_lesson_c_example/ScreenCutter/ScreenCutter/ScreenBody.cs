using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace ScreenCutter
{
    public partial class ScreenBody : Form
    {
        private Graphics MainPainter;
        private Pen pen;
        private bool isDowned;
        private Image baseImage;
        private Rectangle Rect;
        private bool RectReady;
        private Point downPoint;
        private bool change;
        Rectangle[] Rectpoints;
        int point;
        int tmpx;
        int tmpy;

        public ScreenBody()
        {
            InitializeComponent();
        }

        private void ScreenBody_Load(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Maximized;
            MainPainter = this.CreateGraphics();
            pen = new Pen(Brushes.Blue);
            isDowned = false;
            baseImage = this.BackgroundImage;
            Rect = new Rectangle();
            RectReady = false;
            change = false;
            Rectpoints = new Rectangle[8];
            for (int i = 0; i < Rectpoints.Length; i++)
            {
                Rectpoints[i].Size = new Size(4, 4);
            }
            //myRect mRect = new myRect();
            //mRect.Init(0,0,
        }

        private void ScreenBody_DoubleClick(object sender, EventArgs e)
        {
            if (((MouseEventArgs)e).Button == MouseButtons.Left && Rect.Contains(((MouseEventArgs)e).X, ((MouseEventArgs)e).Y))
            {
                Image memory = new Bitmap(Rect.Width, Rect.Height);
                Graphics g = Graphics.FromImage(memory);
                g.CopyFromScreen(Rect.X + 1, Rect.Y + 1, 0, 0, Rect.Size);
                //IntPtr dc = g.GetHdc();
                //g.ReleaseHdc(dc);
                Clipboard.SetImage(memory);
                this.Close();
            }
        }

        private void ScreenBody_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isDowned = true;

                if (RectReady == false)
                {
                    Rect.X = e.X;
                    Rect.Y = e.Y;
                    downPoint = new Point(e.X, e.Y);
                }
                if (RectReady == true)
                {
                    tmpx = e.X;
                    tmpy = e.Y;
                }
                for (int i = 0; i < Rectpoints.Length; i++)
                {
                    if (Rectpoints[i].Contains(e.X, e.Y))
                    {
                        change = true;
                        point = i + 1;
                    }
                }

            }
            if (e.Button == MouseButtons.Right)
            {
                if (RectReady != true)
                {
                    this.Close();
                    return;
                }
                this.CreateGraphics().DrawImage(baseImage, 0, 0);
                RectReady = false;
            }

        }

        private void ScreenBody_MouseMove(object sender, MouseEventArgs e)
        {

            if (RectReady == false)
            {
                if (isDowned == true)
                {
                    Image New = DrawScreen((Image)baseImage.Clone(), e.X, e.Y);
                    MainPainter.DrawImage(New, 0, 0);
                    New.Dispose();
                }
            }
            if (RectReady == true)
            {
                if (Rect.Contains(e.X, e.Y))
                {
                    //this.Cursor = Cursors.Hand;
                    if (isDowned == true && change == false)
                    {
                        //和上一次的位置比较获取偏移量
                        Rect.X = Rect.X + e.X - tmpx;
                        Rect.Y = Rect.Y + e.Y - tmpy;
                        //记录现在的位置
                        tmpx = e.X;
                        tmpy = e.Y;
                        MoveRect((Image)baseImage.Clone(), Rect);
                    }
                }
                if (change == true && isDowned == true)
                {
                    switch (point)
                    {
                        case 1:

                            break;
                        case 2:
                            break;
                        case 3:
                            break;
                        case 4:
                            break;
                        case 5:
                            break;
                        case 6:
                            ChangeRect((Image)baseImage.Clone(), e.X, e.Y, ChangeSide.RightTop);
                            break;
                        case 7:
                            ChangeRect((Image)baseImage.Clone(), e.X, e.Y, ChangeSide.Right);
                            break;
                        case 8:
                            ChangeRect((Image)baseImage.Clone(), e.X, e.Y, ChangeSide.RightBottom);
                            break;
                    }
                }
            }
        }

        private void ScreenBody_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isDowned = false;
                RectReady = true;
                change = false;
            }
        }

        private void DrawRect(Graphics Painter, int Mouse_x, int Mouse_y)
        {
            int width = 0;
            int heigth = 0;
            if (Mouse_y < Rect.Y)
            {
                Rect.Y = Mouse_y;
                heigth = downPoint.Y - Mouse_y;
            }
            else
            {
                heigth = Mouse_y - downPoint.Y;
            }
            if (Mouse_x < Rect.X)
            {
                Rect.X = Mouse_x;
                width = downPoint.X - Mouse_x;
            }
            else
            {
                width = Mouse_x - downPoint.X;
            }
            Rect.Size = new Size(width, heigth);
            DrawRects(Painter);
        }
        private void DrawRects(Graphics Painter)
        {
            Painter.DrawRectangle(pen, Rect);
            /*
            Rectpoints[0].X = Rect.X - 2;
            Rectpoints[0].Y = Rect.Y - 2;
            Rectpoints[1].X = Rect.X - 2;
            Rectpoints[1].Y = Rect.Y - 2 + Rect.Height / 2;
            Rectpoints[2].X = Rect.X - 2;
            Rectpoints[2].Y = Rect.Y - 2 + Rect.Height;
            Rectpoints[3].X = Rect.X - 2 + Rect.Width / 2;
            Rectpoints[3].Y = Rect.Y - 2;
            Rectpoints[4].X = Rect.X - 2 + Rect.Width / 2;
            Rectpoints[4].Y = Rect.Y - 2 + Rect.Height;
            Rectpoints[5].X = Rect.X - 2 + Rect.Width;
            Rectpoints[5].Y = Rect.Y - 2;
            Rectpoints[6].X = Rect.X - 2 + Rect.Width;
            Rectpoints[6].Y = Rect.Y - 2 + Rect.Height / 2;
            Rectpoints[7].X = Rect.X - 2 + Rect.Width;
            Rectpoints[7].Y = Rect.Y - 2 + Rect.Height;
            Painter.FillRectangles(Brushes.Blue, Rectpoints);
             * */
        }

        private Image DrawScreen(Image back, int Mouse_x, int Mouse_y)
        {
            Graphics Painter = Graphics.FromImage(back);
            DrawRect(Painter, Mouse_x, Mouse_y);
            return back;
        }


        private void MoveRect(Image image, Rectangle Rect)
        {
            Graphics Painter = Graphics.FromImage(image);
            Painter.DrawRectangle(pen, Rect.X, Rect.Y, Rect.Width, Rect.Height);
            DrawRects(Painter);
            MainPainter.DrawImage(image, 0, 0);
            image.Dispose();
        }

        private void ChangeRect(Image image, int Position_x, int Position_y, ChangeSide Side)
        {
            int width = 0;
            int height = 0;
            Graphics Painter = Graphics.FromImage(image);
            switch (Side)
            {
                case ChangeSide.Left:
                    break;
                case ChangeSide.LeftBottom:
                    break;
                case ChangeSide.LeftTop:
                    Rect.Y = Position_y;
                    break;
                case ChangeSide.Bottom:
                    break;
                case ChangeSide.Top:
                    break;
                case ChangeSide.Right:
                    if (Position_x < Rect.X)
                    {
                        Rect.Size = new Size(tmpx - Position_x + Rect.Width, Rect.Height);
                        Rect.X = Position_x;
                        //记录现在的位置
                        tmpx = Position_x;
                    }
                    else
                        Rect.Size = new Size(Position_x - Rect.X, Rect.Height);
                    break;
                case ChangeSide.RightBottom:
                    Rect.Size = new Size(Position_x - Rect.X, Position_y - Rect.Y);
                    break;
                case ChangeSide.RightTop:
                    //Rect.Y = Position_y;
                    Rect.Size = new Size(Position_x - Rect.X, Rect.Height + Rectpoints[5].Y - Position_y);
                    break;
            }
            //Painter.DrawRectangle(pen, Rect.X, Rect.Y, Rect.Width, Rect.Height);
            DrawRects(Painter);
            MainPainter.DrawImage(image, 0, 0);
            image.Dispose();
            /*
            MainPainter.DrawImage(New, 0, 0);
            New.Dispose();*/
        }

        private void ChangeRect(Image image, int Position, ChangeSide Side)
        {

        }

        enum ChangeSide
        {
            Left,
            LeftTop,
            LeftBottom,
            Right,
            RightTop,
            RightBottom,
            Top,
            Bottom
        }

        struct myRect
        {
            public int x;
            public int y;
            public int width;
            public int height;
            public Rectangle[] RectPoints;

            public void Init(int x, int y, int width, int height, int number)
            {
                this.x = x;
                this.y = y;
                this.width = width;
                this.height = height;
                RectPoints = new Rectangle[number];
            }
        }
    }
}

