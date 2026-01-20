using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode

// 滑鼠操作畫圖相關

namespace vcs_MousePaint1
{
    public partial class Form1 : Form
    {
        Pen penRed = new Pen(Color.Red, 3);

        //pictureBox0 拖曳圓點 ST
        private const int N = 6;   //total_points
        int pt_selected = -1;  // 動態陣列 的 第幾個 被選到
        bool flag_dragging = false; // 是否拖拉中
        Pen p1 = new Pen(Color.Green, 1);
        Pen p2 = new Pen(Color.Blue, 1);
        Point[] pts = new Point[N];
        int Epsilon = 100; // 滑鼠 是否 點選到點 的距離 判斷 (避免 開根號)
        //pictureBox0 拖曳圓點 SP

        //pictureBox1 左鍵畫一橢圓, 右鍵畫一橢圓 ST
        private const float small = 0.1f;

        // Rectangles that define the ellipses.
        private bool GotEllipse1 = false;
        private bool GotEllipse2 = false;
        private Rectangle Ellipse1;
        private Rectangle Ellipse2;

        // The points of intersection.
        private List<PointF> Roots = new List<PointF>();
        private List<float> RootSign1 = new List<float>();
        private List<float> RootSign2 = new List<float>();
        private List<PointF> PointsOfIntersection = new List<PointF>();

        // Used while drawing ellipses.
        private int DrawingEllipseNum = 0;
        private int StartX;
        private int StartY;
        private int EndX;
        private int EndY;
        //pictureBox1 左鍵畫一橢圓, 右鍵畫一橢圓 SP

        //pictureBox2 累計畫矩形 ST

        // Parameters for drawing the dashed rectangle.
        private float Offset = 0;
        private float OffsetDelta = 2;
        private float[] DashPattern = { 5, 5 };

        // Previously selected rectangles.
        private List<Rectangle> Rectangles = new List<Rectangle>();

        // The rectangle we are selecting.
        private Rectangle NewRectangle;

        // Variables used to select a new rectangle.
        private int StartX2, StartY2, EndX2, EndY2;
        private bool SelectingRectangle = false;

        // The rectangles' colors.
        private Brush[] RectangleBrushes =
        {
            Brushes.Red,
            Brushes.Green,
            Brushes.Blue,
            Brushes.Lime,
            Brushes.Orange,
            Brushes.Fuchsia,
            Brushes.Yellow,
            Brushes.LightGreen,
            Brushes.LightBlue,
            Brushes.Cyan,
        };

        //pictureBox2 累計畫矩形 SP

        //pictureBox3 貝茲線與控制點 ST
        List<MovingPoint> mpList3 = new List<MovingPoint>(); // 可移動點的動態陣列
        int mp_Selected3 = -1;  // 動態陣列 的第幾個 被選到
        bool dragging3 = false; // 是否拖拉中
        //pictureBox3 貝茲線與控制點 SP

        //pictureBox4 連續貝茲線與控制點 ST
        List<MovingPoint> mpList4 = new List<MovingPoint>(); // 可移動點的動態陣列
        int mp_Selected4 = -1;  // 動態陣列 的第幾個 被選到
        bool dragging4 = false; // 是否拖拉中
        //pictureBox4 連續貝茲線與控制點 SP

        //pictureBox5 拖曳圖片框中的紅點 ST
        //Point一維陣列
        Point[] pts5 = new Point[6];    //一維陣列內有6個Point
        int find_point_index = -1;
        //pictureBox5 拖曳圖片框中的紅點 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            this.DoubleBuffered = true;

            //pictureBox0 拖曳圓點 ST
            int w = 400;
            int h = 400;

            int angle = 360 / N;
            int r = Math.Min(w, h) * 2 / 5;

            int i;
            int x = 0;
            int y = 0;

            for (i = 0; i < N; i++)
            {
                pts[i] = new Point(w / 2 + (int)(r * Math.Cos(Math.PI * angle * i / 180)), h / 2 + (int)(r * Math.Sin(Math.PI * angle * i / 180)));
            }
            //pictureBox0 拖曳圓點 SP


            //pictureBox3 貝茲線與控制點 ST
            MovingPoint mp3;
            mp3 = new MovingPoint(new Point(100, 200));
            mpList3.Add(mp3); // 第一個控制點

            mp3 = new MovingPoint(new Point(200, 100));
            mpList3.Add(mp3); // 第二個控制點

            mp3 = new MovingPoint(new Point(300, 300));
            mpList3.Add(mp3); // 第三個控制點

            mp3 = new MovingPoint(new Point(400, 200));
            mpList3.Add(mp3); // 第四個控制點
            //pictureBox3 貝茲線與控制點 SP

            //pictureBox4 連續貝茲線與控制點 ST
            MovingPoint mp4;
            mp4 = new MovingPoint(new Point(100, 200));
            mpList4.Add(mp4); // 第一個控制點

            mp4 = new MovingPoint(new Point(200, 100));
            mpList4.Add(mp4); // 第二個控制點

            mp4 = new MovingPoint(new Point(300, 300));
            mpList4.Add(mp4); // 第三個控制點

            mp4 = new MovingPoint(new Point(400, 200));
            mpList4.Add(mp4); // 第四個控制點

            mp4 = new MovingPoint(new Point(500, 100));
            mpList4.Add(mp4); // 第五個控制點

            mp4 = new MovingPoint(new Point(600, 300));
            mpList4.Add(mp4); // 第六個控制點

            mp4 = new MovingPoint(new Point(700, 200));
            mpList4.Add(mp4); // 第七個控制點
            //pictureBox4 連續貝茲線與控制點 SP

            //pictureBox5 拖曳圖片框中的紅點 ST
            int x_st = 50;
            int y_st = 80;
            int dy = 30;
            pts5[0] = new Point(x_st + 0, y_st + dy * 0);
            pts5[1] = new Point(x_st + 0, y_st + dy * 1);
            pts5[2] = new Point(x_st + 0, y_st + dy * 2);
            pts5[3] = new Point(x_st + 0, y_st + dy * 3);
            pts5[4] = new Point(x_st + 0, y_st + dy * 4);
            pts5[5] = new Point(x_st + 0, y_st + dy * 5);
            //pictureBox5 拖曳圖片框中的紅點 SP
        }

        void show_item_location()
        {
            int W = 460;
            int H = 400;
            int x_st = 10;
            int y_st = 30;
            int dx = W + 20;
            int dy = H + 50;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            int dd = 26;
            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - dd);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - dd);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - dd);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 1 - dd);
            label4.Location = new Point(x_st + dx * 1, y_st + dy * 1 - dd);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1 - dd);
            label0.Text = "拖曳正六邊形的頂點 / 拖曳圓點";
            label1.Text = "左鍵畫一橢圓, 右鍵畫一橢圓";
            label2.Text = "累計畫矩形";
            label3.Text = "貝茲線與控制點";
            label4.Text = "連續貝茲線與控制點";
            label5.Text = "";
            richTextBox1.Size = new Size(W - 200, H * 2 + 60);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1740, 940);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        // 檢查是哪一個點被 選到
        private void pictureBox0_MouseDown(object sender, MouseEventArgs e)
        {
            for (int i = 0; i < pts.Length; i++)
            {
                if (CheckSelected(pts[i], e.Location) == true)
                {
                    pt_selected = i;
                    flag_dragging = true;
                    pts[pt_selected].X = e.X;
                    pts[pt_selected].Y = e.Y;
                    richTextBox1.Text += "選中 " + i.ToString() + "\n";
                    break;
                }
                else
                {
                    //richTextBox1.Text += "沒選中\n";
                }
            }
        }

        // 更新 被選到的點 的座標
        private void pictureBox0_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_dragging == true)
            {
                pts[pt_selected].X = e.X;
                pts[pt_selected].Y = e.Y;
                this.pictureBox0.Invalidate();
            }
        }

        // 解除 被選到的點
        private void pictureBox0_MouseUp(object sender, MouseEventArgs e)
        {
            if (flag_dragging == true)
            {
                pt_selected = -1;
                flag_dragging = false;
                this.pictureBox0.Invalidate();
            }
        }

        // 檢查是否選到這個點
        bool CheckSelected(Point pt1, Point pt2)
        {
            //distance是距離的平方
            int distance = (pt1.X - pt2.X) * (pt1.X - pt2.X) + (pt1.Y - pt2.Y) * (pt1.Y - pt2.Y);
            if (distance <= Epsilon)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            int radius = 10;

            if (flag_dragging == true)
            {
                e.Graphics.DrawPolygon(p1, pts);
            }
            else
            {
                e.Graphics.DrawPolygon(p2, pts);
            }

            for (int i = 0; i < N; i++)
            {
                FillCircle(e.Graphics, pts[i], radius, Color.Red);
                e.Graphics.DrawString(i.ToString(), new Font("標楷體", 15), new SolidBrush(Color.Blue), new PointF(pts[i].X + 10, pts[i].Y));
            }
        }

        private void FillCircle(Graphics g, PointF center, int radius, Color c)
        {
            SolidBrush sb = new SolidBrush(c);

            // Fill the circle
            g.FillEllipse(sb, new RectangleF(center.X - radius, center.Y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            sb.Dispose();
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // Remove previous points of intersection.
            Roots = new List<PointF>();
            RootSign1 = new List<float>();
            RootSign2 = new List<float>();
            PointsOfIntersection = new List<PointF>();

            // If we are already drawing, stop.
            if (DrawingEllipseNum > 0)
            {
                DrawingEllipseNum = 0;
                pictureBox1.Refresh();
                return;
            }

            // See which mouse button is pressed.
            if (e.Button == MouseButtons.Left)
            {
                DrawingEllipseNum = 1;
                GotEllipse1 = false;
            }
            else if (e.Button == MouseButtons.Right)
            {
                DrawingEllipseNum = 2;
                GotEllipse2 = false;
            }

            StartX = e.X;
            StartY = e.Y;
            EndX = e.X;
            EndY = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing if we are not drawing.
            if (DrawingEllipseNum == 0)
            {
                return;
            }

            EndX = e.X;
            EndY = e.Y;

            // Redraw.
            pictureBox1.Refresh();
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            // Do nothing if we are not drawing.
            if (DrawingEllipseNum == 0)
            {
                return;
            }

            EndX = e.X;
            EndY = e.Y;

            // Make sure the ellipse has non-zero width and height.
            if ((StartX != EndX) && (StartY != EndY))
            {
                // See which ellipse we are drawing.
                if (DrawingEllipseNum == 1)
                {
                    Ellipse1 = new Rectangle(Math.Min(StartX, EndX), Math.Min(StartY, EndY), Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
                    GotEllipse1 = true;
                }
                else if (DrawingEllipseNum == 2)
                {
                    Ellipse2 = new Rectangle(Math.Min(StartX, EndX), Math.Min(StartY, EndY), Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
                    GotEllipse2 = true;
                }
            }

            // We are no longer drawing a new ellipse.
            DrawingEllipseNum = 0;

            // Redraw.
            pictureBox1.Refresh();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox1.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the first ellipse.
            if (GotEllipse1)
            {
                //richTextBox1.Text += "111\n";
                Brush brush = new SolidBrush(Color.FromArgb(128, Color.Blue));

                e.Graphics.FillEllipse(brush, Ellipse1);

                e.Graphics.DrawEllipse(Pens.Blue, Ellipse1);
            }

            // Draw the second ellipse.
            if (GotEllipse2)
            {
                //richTextBox1.Text += "222\n";
                Brush brush = new SolidBrush(Color.FromArgb(128, Color.Red));
                e.Graphics.FillEllipse(brush, Ellipse2);
                e.Graphics.DrawEllipse(Pens.Red, Ellipse2);
            }

            // Draw the new ellipse if we are drawing one.
            if (DrawingEllipseNum == 1)
            {
                //richTextBox1.Text += "aaa\n";
                e.Graphics.DrawEllipse(Pens.Blue, Math.Min(StartX, EndX), Math.Min(StartY, EndY), Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
            }
            else if (DrawingEllipseNum == 2)
            {
                //richTextBox1.Text += "bbb\n";
                e.Graphics.DrawEllipse(Pens.Red, Math.Min(StartX, EndX), Math.Min(StartY, EndY), Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
            }

            // Draw the points of intersection.
            const int radius = 4;
            foreach (PointF pt in PointsOfIntersection)
            {
                RectangleF rect = new RectangleF(pt.X - radius, pt.Y - radius, 2 * radius, 2 * radius);
                e.Graphics.DrawEllipse(Pens.Green, rect);
            }
        }

        //pictureBox2 累計畫矩形 ST
        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            // Save the current point.
            StartX2 = e.X;
            StartY2 = e.Y;
            EndX2 = e.X;
            EndY2 = e.Y;

            // Make a new selection rectangle.
            NewRectangle = new Rectangle(
                Math.Min(StartX2, EndX2),
                Math.Min(StartY2, EndY2),
                Math.Abs(StartX2 - EndX2),
                Math.Abs(StartY2 - EndY2));

            // Start marching.
            SelectingRectangle = true;
            timer2.Enabled = true;
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            if (!SelectingRectangle)
            {
                return;
            }

            // Save the current point.
            EndX2 = e.X;
            EndY2 = e.Y;

            // Make a new selection rectangle.
            NewRectangle = new Rectangle(
                Math.Min(StartX2, EndX2),
                Math.Min(StartY2, EndY2),
                Math.Abs(StartX2 - EndX2),
                Math.Abs(StartY2 - EndY2));

            // Redraw.
            Refresh();
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            if (!SelectingRectangle)
            {
                return;
            }
            SelectingRectangle = false;
            timer2.Enabled = false;
            if ((StartX2 == EndX2) || (StartY2 == EndY2))
            {
                return;
            }

            // Save the newly selected rectangle.
            Rectangles.Add(new Rectangle(
                Math.Min(StartX2, EndX2),
                Math.Min(StartY2, EndY2),
                Math.Abs(StartX2 - EndX2),
                Math.Abs(StartY2 - EndY2)));

            // Redraw.
            Refresh();
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            Offset += OffsetDelta;

            // Draw previously selected rectangles.
            for (int i = 0; i < Rectangles.Count; i++)
            {
                e.Graphics.FillRectangle(
                    RectangleBrushes[i % RectangleBrushes.Length],
                    Rectangles[i]);
                e.Graphics.DrawRectangle(Pens.Black, Rectangles[i]);
            }

            // Draw the new rectangle.
            if (SelectingRectangle)
            {
                e.Graphics.DrawRectangle(NewRectangle, Color.Yellow,
                    Color.Red, 2f, Offset, DashPattern);
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            Refresh();
        }
        //pictureBox2 累計畫矩形 SP

        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
            // 端點或控制點 是否被點選到
            for (int i = 0; i <= mpList3.Count - 1; i++)
            {
                if (mpList3[i].CheckSelected(e.X, e.Y))
                {
                    mp_Selected3 = i;
                    dragging3 = true;
                    break;
                }
            }
        }

        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging3) // 移動端點或控制點
            {
                mpList3[mp_Selected3].Move(e.X, e.Y);
                this.pictureBox3.Invalidate();
            }
        }

        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
            // 解除 端點或控制點 的點選狀況
            mp_Selected3 = -1;
            dragging3 = false;
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawBezier(penRed, mpList3[0].p, mpList3[1].p, mpList3[2].p, mpList3[3].p);

            //繪出切線
            e.Graphics.DrawLine(Pens.Black, mpList3[0].p, mpList3[1].p);
            e.Graphics.DrawLine(Pens.Black, mpList3[2].p, mpList3[3].p);

            //繪出 端點和控制點
            e.Graphics.DrawEllipse(Pens.Black, mpList3[0].p.X - 10, mpList3[0].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList3[1].p.X - 10, mpList3[1].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList3[2].p.X - 10, mpList3[2].p.Y - 10, 20, 20);
            e.Graphics.DrawEllipse(Pens.Black, mpList3[3].p.X - 10, mpList3[3].p.Y - 10, 20, 20);
        }

        private void pictureBox4_MouseDown(object sender, MouseEventArgs e)
        {
            // 端點或控制點 是否被點選到
            for (int i = 0; i <= mpList4.Count - 1; i++)
            {
                if (mpList4[i].CheckSelected(e.X, e.Y))
                {
                    mp_Selected4 = i;
                    dragging4 = true;
                    break;
                }
            }
        }

        private void pictureBox4_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging4) // 移動端點或控制點
            {
                mpList4[mp_Selected4].Move(e.X, e.Y);
                this.pictureBox4.Invalidate();
            }
        }

        private void pictureBox4_MouseUp(object sender, MouseEventArgs e)
        {
            // 解除 端點或控制點 的點選狀況
            mp_Selected4 = -1;
            dragging4 = false;
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
            Point[] mpArray = new Point[7];
            for (int i = 0; i <= mpList4.Count - 1; i++)
            {
                mpArray[i] = mpList4[i].p;
            }
            e.Graphics.DrawBeziers(penRed, mpArray);

            //繪出切線
            e.Graphics.DrawLine(Pens.Black, mpList4[0].p, mpList4[1].p);
            e.Graphics.DrawLine(Pens.Black, mpList4[2].p, mpList4[3].p);

            e.Graphics.DrawLine(Pens.Black, mpList4[3].p, mpList4[4].p);
            e.Graphics.DrawLine(Pens.Black, mpList4[5].p, mpList4[6].p);

            //繪出 端點和控制點
            e.Graphics.DrawEllipse(Pens.Black, mpList4[0].p.X - 10, mpList4[0].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList4[1].p.X - 10, mpList4[1].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList4[2].p.X - 10, mpList4[2].p.Y - 10, 20, 20);
            e.Graphics.DrawEllipse(Pens.Black, mpList4[3].p.X - 10, mpList4[3].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList4[4].p.X - 10, mpList4[4].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList4[5].p.X - 10, mpList4[5].p.Y - 10, 20, 20);
            e.Graphics.DrawEllipse(Pens.Black, mpList4[6].p.X - 10, mpList4[6].p.Y - 10, 20, 20);
        }

        bool flag_pictureBox5_mouse_down = false;
        private void pictureBox5_MouseDown(object sender, MouseEventArgs e)
        {
            Point pt = FindPointAt(e.X, e.Y);
            if (pt == new Point(9999, 9999))
            {
                richTextBox1.Text += "找不到\n";
            }
            else
            {
                flag_pictureBox5_mouse_down = true;
                richTextBox1.Text += "找到 : (" + pt.X.ToString() + ", " + pt.Y.ToString() + ")\n";
                int index = get_index(pt);
                richTextBox1.Text += index.ToString() + "\n";
                find_point_index = index;
            }
        }

        private Point FindPointAt(int X, int Y)
        {
            foreach (Point pt in pts5)
            {
                float dx = pt.X - X;
                float dy = pt.Y - Y;
                if (dx * dx + dy * dy <= 20 * 20)
                {
                    return pt;
                }
            }
            return new Point(9999, 9999);
        }

        int get_index(Point point)
        {
            int len = pts5.Length;
            int index = 0;
            for (index = 0; index < len; index++)
            {
                if (point == pts5[index])
                {
                    return index;
                }
            }
            return -1;
        }

        private void pictureBox5_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox5_mouse_down == true)
            {
                update_pts(find_point_index, e.Location);
                this.pictureBox5.Invalidate();
            }
        }

        private void pictureBox5_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pictureBox5_mouse_down = false;
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawString("拖曳圖片框中的紅點", new Font("標楷體", 16), new SolidBrush(Color.Black), 20, 20);
            //e.Graphics.DrawRectangle(Pens.Red, 100, 100, 300, 300);
            foreach (Point pt in pts5)
            {
                e.Graphics.FillEllipse(Brushes.Red, pt.X - 10, pt.Y - 10, 20, 20);
            }
        }

        void update_pts(int index, Point point)
        {
            int len = pts5.Length;
            if ((index < 0) || index >= len)
            {
                richTextBox1.Text += index.ToString();
                //richTextBox1.Text += "XXXXXXX\n";
                return;
            }
            pts5[index] = point;
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/


// Start selecting a rectangle.
// Continue selecting a rectangle.
// Finish selecting a rectangle.



/*
                Bitmap bmp = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\BMW.jfif");
                    e.Graphics.DrawImage(bmp, pt[i].X, pt[i].Y, 100, 100);
*/

