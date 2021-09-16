using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_PicPick3
{
    public partial class Frm_Browser : Form
    {
        public Image ig;
        private Graphics MainPainter;
        private Pen pen;
        private bool isDowned;
        private Image baseImage;
        private Rectangle rect;
        private bool flag_rect_ready;
        private Point downPoint;
        private bool change;
        Rectangle[] Rectpoints;
        int point;
        int tmpx;
        int tmpy;

        public Frm_Browser()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            this.BackgroundImage = ig;
            this.WindowState = FormWindowState.Maximized;
            MainPainter = this.CreateGraphics();
            pen = new Pen(Brushes.Red);
            isDowned = false;
            baseImage = this.BackgroundImage;
            rect = new Rectangle();
            flag_rect_ready = false;
            change = false;
            Rectpoints = new Rectangle[8];
            for (int i = 0; i < Rectpoints.Length; i++)
            {
                Rectpoints[i].Size = new Size(4, 4);
            }
        }

        private void DrawRect(Graphics Painter, int Mouse_x, int Mouse_y)
        {
            int width = 0;
            int heigth = 0;
            if (Mouse_y < rect.Y)
            {
                rect.Y = Mouse_y;
                heigth = downPoint.Y - Mouse_y;
            }
            else
            {
                heigth = Mouse_y - downPoint.Y;
            }
            if (Mouse_x < rect.X)
            {
                rect.X = Mouse_x;
                width = downPoint.X - Mouse_x;
            }
            else
            {
                width = Mouse_x - downPoint.X;
            }
            rect.Size = new Size(width, heigth);
            DrawRects(Painter);
        }

        private void DrawRects(Graphics Painter)
        {
            Painter.DrawRectangle(pen, rect);
        }

        private Image DrawScreen(Image back, int Mouse_x, int Mouse_y)
        {
            Graphics Painter = Graphics.FromImage(back);
            DrawRect(Painter, Mouse_x, Mouse_y);
            return back;
        }

        private void Form2_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)
            {
                this.Close();
            }
        }

        private void Form2_DoubleClick(object sender, EventArgs e)
        {
            if ((rect.Size.Width <= 0) || (rect.Size.Height <= 0))
            {
                return;
            }

            if (((MouseEventArgs)e).Button == MouseButtons.Left && rect.Contains(((MouseEventArgs)e).X, ((MouseEventArgs)e).Y))
            {
                //部分螢幕截圖
                int W = rect.Width - 1;
                int H = rect.Height - 1;

                using (Bitmap bitmap1 = new Bitmap(W, H))
                {
                    using (Graphics g = Graphics.FromImage(bitmap1))
                    {
                        //             擷取螢幕位置起點  自建bmp的位置起點     擷取大小
                        g.CopyFromScreen(rect.X + 1, rect.Y + 1, 0, 0, rect.Size);
                        //richTextBox1.Text += "W = " + W.ToString() + "\n";
                        //richTextBox1.Text += "H = " + H.ToString() + "\n";
                    }
                    //存成bmp檔
                    String filename = "C:\\dddddddddd\\part_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                    bitmap1.Save(filename, ImageFormat.Bmp);
                    //richTextBox1.Text += "全螢幕截圖，存檔檔名：\n" + filename + "\n";

                    Clipboard.SetImage(bitmap1);    //同時把截圖存到剪貼簿裏
                }
                this.Close();
            }
        }

        private void Form2_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isDowned = true;
                if (flag_rect_ready == true)
                {
                    tmpx = e.X;
                    tmpy = e.Y;
                }
                else
                {
                    rect.X = e.X;
                    rect.Y = e.Y;
                    downPoint = new Point(e.X, e.Y);
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
                if (flag_rect_ready != true)
                {
                    this.Close();
                    return;
                }
                this.CreateGraphics().DrawImage(baseImage, 0, 0);
                flag_rect_ready = false;
            }
        }

        private void Form2_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isDowned = false;
                flag_rect_ready = true;
                change = false;
            }
        }

        private void Form2_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_rect_ready == true)
            {
                if (rect.Contains(e.X, e.Y))
                {
                    if (isDowned == true && change == false)
                    {
                        //和上一次的位置比较获取偏移量
                        rect.X = rect.X + e.X - tmpx;
                        rect.Y = rect.Y + e.Y - tmpy;
                        //记录现在的位置
                        tmpx = e.X;
                        tmpy = e.Y;
                        MoveRect((Image)baseImage.Clone(), rect);
                    }
                }
                //if (change == true && isDowned == true)
                //{
                //    if (point == 6)
                //    {
                //        ChangeRect((Image)baseImage.Clone(), e.X, e.Y, ChangeSide.RightTop);
                //    }
                //    if (point == 7)
                //    {
                //        ChangeRect((Image)baseImage.Clone(), e.X, e.Y, ChangeSide.Right);
                //    }
                //    if (point == 8)
                //    {
                //        ChangeRect((Image)baseImage.Clone(), e.X, e.Y, ChangeSide.RightBottom);
                //    }
                //}
            }
            else
            {
                if (isDowned == true)
                {
                    Image New = DrawScreen((Image)baseImage.Clone(), e.X, e.Y);
                    MainPainter.DrawImage(New, 0, 0);
                    New.Dispose();
                }
            }
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
            Graphics Painter = Graphics.FromImage(image);
            switch (Side)
            {
                case ChangeSide.Left:
                    break;
                case ChangeSide.LeftBottom:
                    break;
                case ChangeSide.LeftTop:
                    rect.Y = Position_y;
                    break;
                case ChangeSide.Bottom:
                    break;
                case ChangeSide.Top:
                    break;
                case ChangeSide.Right:
                    if (Position_x < rect.X)
                    {
                        rect.Size = new Size(tmpx - Position_x + rect.Width, rect.Height);
                        rect.X = Position_x;
                        //记录现在的位置
                        tmpx = Position_x;
                    }
                    else
                        rect.Size = new Size(Position_x - rect.X, rect.Height);
                    break;
                case ChangeSide.RightBottom:
                    rect.Size = new Size(Position_x - rect.X, Position_y - rect.Y);
                    break;
                case ChangeSide.RightTop:
                    rect.Size = new Size(Position_x - rect.X, rect.Height + Rectpoints[5].Y - Position_y);
                    break;
            }
            DrawRects(Painter);
            MainPainter.DrawImage(image, 0, 0);
            image.Dispose();
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

