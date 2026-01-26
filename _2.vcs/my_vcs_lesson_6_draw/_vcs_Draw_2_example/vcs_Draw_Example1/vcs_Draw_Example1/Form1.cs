using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat   //提供畫GDI+圖形的高級功能
using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode //提供畫高級二維，矢量圖形功能
using System.Drawing.Text;      //for TextRenderingHint //提供畫GDI+圖形的高級功能

using System.IO;
using System.Collections;   //for ArrayList
using System.Runtime.InteropServices;   //for Marshal
using System.Diagnostics;       //for Debug
using System.Reflection;    //PropertyInfo
using System.Threading;

namespace vcs_Draw_Example1
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        private List<Point> Points = new List<Point>();


        public Form1()
        {
            InitializeComponent();
        }

        //重寫表單的OnPaint範例 直接寫在此即可
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            //繪製螞蟻線
            draw_ant_line();
        }

        void show_item_location()
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st = 10;
            int y_st = 10;
            int dx = 140;
            int dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            button30.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            button40.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button43.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            button44.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            button45.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            button46.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            button47.Location = new Point(x_st + dx * 4, y_st + dy * 7);
            button48.Location = new Point(x_st + dx * 4, y_st + dy * 8);
            button49.Location = new Point(x_st + dx * 4, y_st + dy * 9);

            groupBox3.Size = new Size(580, 80);
            groupBox3.Location = new Point(x_st + dx * 0, y_st + dy * 10+10);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 14 + 20);

            cb_manual.Location = new Point(x_st + dx * 1, y_st + dy * 14 + 30);
            cb_snake.Location = new Point(x_st + dx * 2, y_st + dy * 14 + 30);
            cb_magnifying.Location = new Point(x_st + dx * 2, y_st + dy * 14 + dy / 2 + 30);

            pictureBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            pictureBox1.Size = new Size(1060, 600);
            pictureBox1.BackColor = Color.White;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            checkBox1.Location = new Point(pictureBox1.Location.X, pictureBox1.Location.Y + pictureBox1.Size.Height - checkBox1.Size.Height);
            bt_save.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_save.Size.Width * 2, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_save.Size.Height);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_reset.Size.Height);

            pictureBox2.Size = new Size(360, 250);
            pictureBox2.BackColor = Color.Pink;
            pictureBox2.Location = new Point(x_st + dx * 5 + 40, y_st + dy * 13);
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox2.Visible = false;

            richTextBox1.Size = new Size(480, 250);
            richTextBox1.Location = new Point(x_st + dx * 9, y_st + dy * 13);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            y_st += 10;
            bt_2d_array0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_2d_array1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_2d_array2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_2d_array3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_long0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_long1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_long2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_long3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_long4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_long5.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_long6.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_long7.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_long8.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_long9.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            bt_long10.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            bt_long11.Location = new Point(x_st + dx * 5, y_st + dy * 1);


            this.Size = new Size(1800, 960);
            this.Text = "vcs_Draw_Example1";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            int x_st = 10;
            int y_st = 10;
            int dx = 140;
            int dy = 50;
            pictureBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            pictureBox1.Size = new Size(1060, 600);
            pictureBox1.BackColor = Color.White;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                string filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        //沒用到????
        void open_new_file()
        {
            richTextBox1.Text += "開啟一個 640 X 480 的空畫布\n";
            //指定畫布大小
            pictureBox1.Width = 640;
            pictureBox1.Height = 480;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
            return;
        }

        bool isDrawing = false;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            isDrawing = true;

            pictureBox1_MouseMove(sender, e);
        }

        bool isDoingMagnifying = false;
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            int region = 30;
            if (isMagnifying == true)
            {
                //pictureBox1擷取一小部分貼到pictureBox2上, 達到放大功能
                if (isDoingMagnifying == false)
                {
                    isDoingMagnifying = true;

                    if (((e.X - region * 2) < 0) || ((e.X + region * 2) > pictureBox1.Width))
                    {
                        isDoingMagnifying = false;
                        return;
                    }

                    if (((e.Y - region * 2) < 0) || ((e.Y + region * 2) > pictureBox1.Height))
                    {
                        isDoingMagnifying = false;
                        return;
                    }

                    RectangleF rect = new RectangleF(e.X, e.Y, 50, 50);

                    try
                    {
                        // 擷取部份影像，顯示於pictureBox2，區域為(起點x座標, 起點y座標, 寬度, 高度)
                        // 將處理之後的圖片貼出來
                        pictureBox2.Image = bitmap1.Clone(rect, PixelFormat.Format32bppArgb);
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "xxx錯誤訊息p : " + ex.Message + "\t";
                        //richTextBox1.Text += "e.X = " + e.X.ToString() + ", e.Y = " + e.Y.ToString() + "\n";
                        //richTextBox1.Text += "t1 = " + (e.X - region).ToString() + ", t2 = " + (e.X + region).ToString() + "\n";
                        //richTextBox1.Text += "t3 = " + (e.Y - region).ToString() + ", t4 = " + (e.Y + region).ToString() + "\n";
                        //richTextBox1.Text += "W = " + pictureBox1.Width.ToString() + ", H = " + pictureBox1.Height.ToString() + "\n";
                    }
                    GC.Collect();       //回收資源
                    isDoingMagnifying = false;
                }
                return;
            }

            if (isDrawing == false)
            {
                return;
            }

            if (cb_snake.Checked == false)
            {
                return;
            }

            this.Text = e.X.ToString() + ", " + e.Y.ToString();
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            int i;
            int j;
            int r;
            //g.Clear(Color.White);
            for (j = 0; j < H; j++)
            {
                if ((j > (e.Y - region)) && (j < (e.Y + region)))
                {
                    for (i = 0; i < W; i++)
                    {
                        if ((i > (e.X - region)) && (i < (e.X + region)))
                        {
                            r = (int)Math.Sqrt((e.X - i) * (e.X - i) + (e.Y - j) * (e.Y - j));
                            if (r < region)
                            {
                                bitmap1.SetPixel(i, j, Color.FromArgb(255 - r * (256 / region), 0xff, 0x0, 0x0));
                            }
                        }
                    }
                }
            }
            pictureBox1.Image = bitmap1;
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            isDrawing = false;
        }

        private void cb_snake_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            //指定畫布大小
            pictureBox1.Width = 600;
            pictureBox1.Height = 600;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            p = new Pen(Color.Red, 3);     // 設定畫筆為紅色、粗細為 3 點。

            if (cb_snake.Checked == true)
            {
                g.Clear(Color.Lime);
            }
            else
            {
                g.Clear(Color.Pink);
            }
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
        }

        bool isMagnifying = false;
        private void cb_magnifying_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_magnifying.Checked == true)
                isMagnifying = true;
            else
                isMagnifying = false;
        }

        //繪製螞蟻線 ST
        delegate void LINEDDAPROC(int X, int Y, IntPtr lpData);
        [DllImport("gdi32.dll")]
        static extern int LineDDA(int nXStart, int nYStart, int nXEnd, int nYEnd, LINEDDAPROC lpLineFunc, IntPtr lpData);

        private const byte PT_CLOSEFIGURE = 1;
        private const byte PT_LINETO = 2;
        private const byte PT_BEZIERTO = 4;
        private const byte PT_MOVETO = 6;

        [DllImport("gdi32.dll")]
        static extern int SetPixel(IntPtr hdc, int X, int Y, int crColor);

        GraphicsPath graphicsPath = new GraphicsPath();
        private int counter = 0;
        private IntPtr graphicsHandle = IntPtr.Zero;

        void draw_ant_line()
        {
            //繪製螞蟻線, 目前只能畫在表單上, 只能畫一個矩形
            graphicsPath.ClearMarkers();
            graphicsPath.AddRectangle(new Rectangle(8, 8, 280, 298));
            timer_dot_line.Interval = 100;
            timer_dot_line.Enabled = true;
        }

        private void MovingDots(int X, int Y, IntPtr lpData)
        {
            counter = (counter + 1) % 15;
            Color vColor;
            if (counter < 5)
            {
                vColor = Color.White;
            }
            else if (counter < 12)
            {
                vColor = Color.Red;
            }
            else
            {
                vColor = Color.Blue;
            }
            SetPixel(graphicsHandle, X, Y, vColor.R | vColor.G << 8 | vColor.B << 16);
        }

        private void timer_dot_line_Tick(object sender, EventArgs e)
        {
            graphicsHandle = Graphics.FromHwnd(Handle).GetHdc();
            for (int i = 0; i < graphicsPath.PathPoints.Length; i++)
            {
                if (graphicsPath.PathTypes[i] == (byte)(PT_CLOSEFIGURE | PT_LINETO))
                {
                    for (int j = i; j >= 0; j--)
                    {
                        if (graphicsPath.PathTypes[j] == PT_MOVETO)
                        {
                            LineDDA(
                                (int)graphicsPath.PathPoints[i].X,
                                (int)graphicsPath.PathPoints[i].Y,
                                (int)graphicsPath.PathPoints[j].X,
                                (int)graphicsPath.PathPoints[j].Y,
                                MovingDots, IntPtr.Zero);
                            break;
                        }
                    }
                    continue;
                }
                if (i == graphicsPath.PathPoints.Length - 1)
                    LineDDA(
                        (int)graphicsPath.PathPoints[i].X,
                        (int)graphicsPath.PathPoints[i].Y,
                        (int)graphicsPath.PathPoints[0].X,
                        (int)graphicsPath.PathPoints[0].Y,
                        MovingDots, IntPtr.Zero);
                else
                    LineDDA(
                        (int)graphicsPath.PathPoints[i].X,
                        (int)graphicsPath.PathPoints[i].Y,
                        (int)graphicsPath.PathPoints[i + 1].X,
                        (int)graphicsPath.PathPoints[i + 1].Y,
                        MovingDots, IntPtr.Zero);

            }
        }
        //繪製螞蟻線 SP

        private void button0_Click(object sender, EventArgs e)
        {
            //Pacman
            int center_x = 250;
            int center_y = 200;
            int radius = 180;
            //DrawPacman(center_x, center_y, radius);

            Brush brush = new SolidBrush(Color.Blue);

            g.FillPie(brush, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2), 320, -280);

            pictureBox1.Image = bitmap1;

            //6060

            //兩種星型

            g.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw diamonds on the form.
            Rectangle rect1 = new Rectangle(4, 4,
                this.pictureBox1.ClientSize.Width / 2 - 6,
                this.pictureBox1.ClientSize.Height - 8);
            Rectangle rect2 = new Rectangle(
                rect1.Right + 4, 4,
                this.pictureBox1.ClientSize.Width / 2 - 6,
                this.pictureBox1.ClientSize.Height - 8);

            DrawStar(g, 9, 4, rect1, null, Brushes.Orange);
            DrawStar(g, null, null, rect2, Pens.Red, null);


            //6060

            //畫多角星形

            g.SmoothingMode = SmoothingMode.AntiAlias;

            Rectangle rect = new Rectangle(0, 0, pictureBox1.Width, pictureBox1.Height);

            PointF[] pts = NonIntersectingStarPoints(7, rect);
            g.DrawPolygon(Pens.Blue, pts);

            pictureBox1.Image = bitmap1;


        }

        private void DrawStar(Graphics g, int? point_count,
    int? skip_count, Rectangle bounds, Pen pen, Brush brush)
        {
            int num_points = (point_count.HasValue) ? point_count.Value : 5;
            int num_skip = (skip_count.HasValue) ? skip_count.Value : 2;

            // Get the star's points.
            PointF[] points = MakeStarPoints(
                -Math.PI / 2, num_points, num_skip, bounds);

            // Fill the star.
            if (brush != null) g.FillPolygon(brush, points);

            // Draw the star.
            if (pen != null) g.DrawPolygon(pen, points);
        }

        // Generate the points for a star.
        private PointF[] MakeStarPoints(double start_theta, int num_points, int skip, Rectangle rect)
        {
            double theta, dtheta;
            PointF[] result;
            float rx = rect.Width / 2f;
            float ry = rect.Height / 2f;
            float cx = rect.X + rx;
            float cy = rect.Y + ry;

            // If this is a polygon, don't bother with concave points.
            if (skip == 1)
            {
                result = new PointF[num_points];
                theta = start_theta;
                dtheta = 2 * Math.PI / num_points;
                for (int i = 0; i < num_points; i++)
                {
                    result[i] = new PointF(
                        (float)(cx + rx * Math.Cos(theta)),
                        (float)(cy + ry * Math.Sin(theta)));
                    theta += dtheta;
                }
                return result;
            }

            // Find the radius for the concave vertices.
            double concave_radius = CalculateConcaveRadius(num_points, skip);

            // Make the points.
            result = new PointF[2 * num_points];
            theta = start_theta;
            dtheta = Math.PI / num_points;
            for (int i = 0; i < num_points; i++)
            {
                result[2 * i] = new PointF(
                    (float)(cx + rx * Math.Cos(theta)),
                    (float)(cy + ry * Math.Sin(theta)));
                theta += dtheta;
                result[2 * i + 1] = new PointF(
                    (float)(cx + rx * Math.Cos(theta) * concave_radius),
                    (float)(cy + ry * Math.Sin(theta) * concave_radius));
                theta += dtheta;
            }
            return result;
        }

        // Calculate the inner star radius.
        private double CalculateConcaveRadius(int num_points, int skip)
        {
            // For really small numbers of points.
            if (num_points < 5) return 0.33f;

            // Calculate angles to key points.
            double dtheta = 2 * Math.PI / num_points;
            double theta00 = -Math.PI / 2;
            double theta01 = theta00 + dtheta * skip;
            double theta10 = theta00 + dtheta;
            double theta11 = theta10 - dtheta * skip;

            // Find the key points.
            PointF pt00 = new PointF(
                (float)Math.Cos(theta00),
                (float)Math.Sin(theta00));
            PointF pt01 = new PointF(
                (float)Math.Cos(theta01),
                (float)Math.Sin(theta01));
            PointF pt10 = new PointF(
                (float)Math.Cos(theta10),
                (float)Math.Sin(theta10));
            PointF pt11 = new PointF(
                (float)Math.Cos(theta11),
                (float)Math.Sin(theta11));

            // See where the segments connecting the points intersect.
            bool lines_intersect, segments_intersect;
            PointF intersection, close_p1, close_p2;
            FindIntersection(pt00, pt01, pt10, pt11,
                out lines_intersect, out segments_intersect,
                out intersection, out close_p1, out close_p2);

            // Calculate the distance between the
            // point of intersection and the center.
            return Math.Sqrt(
                intersection.X * intersection.X +
                intersection.Y * intersection.Y);
        }

        // Find the point of intersection between
        // the lines p1 --> p2 and p3 --> p4.
        private void FindIntersection(
            PointF p1, PointF p2, PointF p3, PointF p4,
            out bool lines_intersect, out bool segments_intersect,
            out PointF intersection,
            out PointF close_p1, out PointF close_p2)
        {
            // Get the segments' parameters.
            float dx12 = p2.X - p1.X;
            float dy12 = p2.Y - p1.Y;
            float dx34 = p4.X - p3.X;
            float dy34 = p4.Y - p3.Y;

            // Solve for t1 and t2
            float denominator = (dy12 * dx34 - dx12 * dy34);

            float t1 =
                ((p1.X - p3.X) * dy34 + (p3.Y - p1.Y) * dx34)
                    / denominator;
            if (float.IsInfinity(t1))
            {
                // The lines are parallel (or close enough to it).
                lines_intersect = false;
                segments_intersect = false;
                intersection = new PointF(float.NaN, float.NaN);
                close_p1 = new PointF(float.NaN, float.NaN);
                close_p2 = new PointF(float.NaN, float.NaN);
                return;
            }
            lines_intersect = true;

            float t2 =
                ((p3.X - p1.X) * dy12 + (p1.Y - p3.Y) * dx12)
                    / -denominator;

            // Find the point of intersection.
            intersection = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);

            // The segments intersect if t1 and t2 are between 0 and 1.
            segments_intersect =
                ((t1 >= 0) && (t1 <= 1) &&
                 (t2 >= 0) && (t2 <= 1));

            // Find the closest points on the segments.
            if (t1 < 0)
            {
                t1 = 0;
            }
            else if (t1 > 1)
            {
                t1 = 1;
            }

            if (t2 < 0)
            {
                t2 = 0;
            }
            else if (t2 > 1)
            {
                t2 = 1;
            }
            close_p1 = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);
            close_p2 = new PointF(p3.X + dx34 * t2, p3.Y + dy34 * t2);
        }

        // Return PointFs to define a non-intersecting star.
        private PointF[] NonIntersectingStarPoints(int num_points, Rectangle bounds)
        {
            // Make room for the points.
            PointF[] pts = new PointF[2 * num_points];

            double rx1 = bounds.Width / 2;
            double ry1 = bounds.Height / 2;
            double rx2 = rx1 * 0.5;
            double ry2 = ry1 * 0.5;
            double cx = bounds.X + rx1;
            double cy = bounds.Y + ry1;

            // Start at the top.
            double theta = -Math.PI / 2;
            double dtheta = Math.PI / num_points;
            for (int i = 0; i < 2 * num_points; i += 2)
            {
                pts[i] = new PointF(
                    (float)(cx + rx1 * Math.Cos(theta)),
                    (float)(cy + ry1 * Math.Sin(theta)));
                theta += dtheta;

                pts[i + 1] = new PointF(
                    (float)(cx + rx2 * Math.Cos(theta)),
                    (float)(cy + ry2 * Math.Sin(theta)));
                theta += dtheta;
            }

            return pts;
        }
        // 畫多角星形

        private void button1_Click(object sender, EventArgs e)
        {
            int i;

            make_pattern_recursive_data();

            richTextBox1.Text += "len = " + pattern_recursive.Count.ToString() + "\n";
            for (i = 0; i < pattern_recursive.Count; i++)
            {
                //richTextBox1.Text += "(" + pattern_recursive[i].X.ToString() + ", " + pattern_recursive[i].Y.ToString() + "),\n";
            }

            Pen bluePen = new Pen(Color.Blue, 8);
            Pen redPen = new Pen(Color.Red, 8);
            int step = 20;
            int offset_x = 450;
            int offset_y = 300;

            Point corner = new Point(0, 0); //平移的座標
            List<Point> points_draw1 = new List<Point>();
            int x1 = 0;
            int y1 = 0;
            int x2 = 0;
            int y2 = 0;

            for (i = 0; i < pattern_recursive.Count; i++)
            {
                x1 = corner.X + pattern_recursive[i].X;
                y1 = corner.Y + pattern_recursive[i].Y;

                x2 = offset_x + x1 * step;
                y2 = offset_y + y1 * step;

                points_draw1.Add(new Point(x2, y2));
            }
            if (points_draw1.Count > 1)
            {
                g.DrawLines(bluePen, points_draw1.ToArray());  //畫直線
            }
            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "測試Pattern\n";

            int x_ratio = 6;
            int y_ratio = 8;
            int W = 256 * x_ratio;
            int H = 800;

            int pic_width = W + 200;
            int pic_height = H + 200;

            bitmap1 = new Bitmap(pic_width, pic_height);
            g = Graphics.FromImage(bitmap1);

            int i;
            int j;
            for (j = 0; j < pic_height; j++)
            {
                for (i = 0; i < pic_width; i++)
                {
                    bitmap1.SetPixel(i, j, Color.FromArgb(255, 0x80, 0x80, 0x80));
                }
            }

            int x_st = 100;
            int y_st = 100;
            int k = 0;
            int cc = 0;
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < 264; i++)
                {
                    for (k = 0; k < 6; k++)
                    {
                        int dd = (int)(j / (H / y_ratio));
                        cc = (i / 8) * 8 + dd;
                        if (cc >= 256)
                        {
                            cc = 255;
                        }
                        if (j == 5)
                        {
                            //richTextBox1.Text += cc.ToString() + " ";
                        }
                        bitmap1.SetPixel(x_st + i * x_ratio + k, y_st + j, Color.FromArgb(255, cc, cc, cc));
                    }
                }
            }

            for (i = 0; i <= 32; i++)
            {
                cc = i * 8;
                if (cc == 256)
                {
                    cc = 255;
                }
                g.DrawString(cc.ToString(), new Font("細明體", 18), new SolidBrush(Color.Red), new PointF(x_st + i * 8 * x_ratio + 5, y_st - 25));
            }
            for (i = 0; i < 8; i++)
            {
                g.DrawString(i.ToString(), new Font("細明體", 18), new SolidBrush(Color.Red), new PointF(x_st - 20, y_st + i * (H / y_ratio) + 30));
            }

            //畫垂直線
            for (i = 0; i <= W; i += (256 * 6 / 32))
            {
                g.DrawLine(new Pen(Brushes.Green, 3), x_st + i, y_st, x_st + i, y_st + H);
            }
            //畫水平線
            for (i = 0; i <= H; i += (H / y_ratio))
            {
                g.DrawLine(new Pen(Brushes.Green, 3), x_st, y_st + i, x_st + W, y_st + i);
            }

            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            int cx = W / 2;
            int cy = H / 2;

            //int radius = 200;
            int r = Math.Min(W, H) / 2 - 50;
            int linewidth = 5;
            int angle = 0;

            g.Clear(Color.White);

            // Create a new pen.
            Pen p = new Pen(Color.Red);

            // Set the pen's width.
            p.Width = linewidth;

            // Draw

            g.DrawEllipse(p, new Rectangle(cx - r, cy - r, r * 2, r * 2));

            for (angle = 0; angle < 360; angle += 10)
            {
                int xx = 0;
                int yy = 0;
                xx = (int)(r * Math.Cos(angle * Math.PI / 180));
                yy = (int)(r * Math.Sin(angle * Math.PI / 180));

                // Create a new pen.
                //Pen PenStyle = new Pen(Brushes.DeepSkyBlue);

                // Set the pen's width.
                p.Width = 8.0F;

                g.DrawLine(new Pen(Brushes.Red, 5), cx, cy, cx + xx, cy - yy);


            }
            //Dispose of the pen.
            p.Dispose();
            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            g.Clear(Color.White);

            Pen p = new Pen(Color.Black, 8);
            p.EndCap = LineCap.ArrowAnchor;  //EndCap設定 這支筆的結尾會是個箭頭

            g.DrawLine(p, 50, 400, 50, 100);  //畫出X軸及y軸
            g.DrawLine(p, 50, 400, 350, 400);

            p = new Pen(Color.Blue, 6);   //重新設定pp的線條樣式
            //pp.DashStyle = DashStyle.Dot; //DashStyle設定線條 點
            //pp.StartCap = LineCap.RoundAnchor; //設定為圓頭

            p.EndCap = LineCap.ArrowAnchor;

            //gg.DrawLine(pp, 50, 50, 250, 250);//只畫一條
            g.DrawLines(p, new Point[]
            {//一次畫好多條
            new Point(70,350),
            new Point(100,280),
            new Point(120,300),
            new Point(200,220),
            new Point(250,260),
            new Point(340,150)
            }
            );
            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);
            Bitmap bitmap1 = new Bitmap(image);
            image.Dispose();
            Graphics g = Graphics.FromImage(bitmap1);
            g.InterpolationMode = InterpolationMode.HighQualityBilinear;
            SolidBrush brush = new SolidBrush(Color.Red);
            PointF P = new PointF(120, 20);
            Font font = new Font(this.Font.Name, 40);
            g.DrawString("牡丹亭", font, brush, P);
            font.Dispose();
            pictureBox1.Image = bitmap1;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //畫邊框

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);

            int x_st = 500;
            int y_st = 50;
            int step = 20;
            int dx = -120;
            int dy = 70;
            draw_frame_style(pattern0, x_st + dx * 0, y_st + dy * 0, step);
            draw_frame_style(pattern1, x_st + dx * 1, y_st + dy * 1, step);
            draw_frame_style(pattern2, x_st + dx * 2, y_st + dy * 2, step);
            draw_frame_style(pattern3, x_st + dx * 3, y_st + dy * 3, step);
            draw_frame_style(pattern4, -250, 50, step);

            pictureBox1.Image = bitmap1;

        }

        private void button8_Click(object sender, EventArgs e)
        {
            //動畫邊框

            List<Point> pattern = pattern0;


            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);

            int x_st = 500;
            int y_st = 50;
            int step = 20;
            int dx = -120;
            int dy = 70;

            richTextBox1.Text += "len = " + pattern.Count.ToString() + "\n";

            int index = 0;

            for (index = 0; index < pattern.Count; index++)
            {
                richTextBox1.Text += "index = " + index.ToString() + " ";
                draw_frame_style_index(pattern, x_st + dx * 0, y_st + dy * 0, step, index);
                pictureBox1.Image = bitmap1;
                Application.DoEvents();
                delay(200);
            }
        }

        int audit_picture_index = 1;
        private void button9_Click(object sender, EventArgs e)
        {
            //稽核圖片 6個

            draw_audit_picture(audit_picture_index);

            audit_picture_index++;
            if (audit_picture_index > 6)
            {
                audit_picture_index = 1;
            }
        }

        void draw_audit_picture(int draw_case)
        {
            int title_size1 = 50;
            int title_size2 = 40;
            int title_size3 = 40;
            int H = 100;
            int h = 10;
            int width = 440;
            int height = h + title_size1 + title_size2 + h + H + h + title_size3 + h + H + h;

            Pen ArrowPen;
            Pen redPen = new Pen(Color.Red, 3);
            Pen greenPen = new Pen(Color.Green, 3);
            Pen blackPen = new Pen(Color.Black, 3);

            //pictureBox1.Width = width;
            //pictureBox1.Height = height;

            if (bitmap1 == null)
                bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.White);

            /*
            //debug
            Pen debug = new Pen(Color.Green, 1);
            g.DrawRectangle(debug, 0, 0, width - 1, h - 1); //h
            g.DrawRectangle(debug, 0, h, width - 1, title_size1 - 1);   //title_size1
            g.DrawRectangle(debug, 0, h + title_size1, width - 1, title_size2 - 1);   //title_size2
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2, width - 1, h - 1);   //h
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h, width - 1, H - 1);   //H
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H, width - 1, h - 1);   //h
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h, width - 1, title_size3 - 1); //title_size3
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h + title_size3, width - 1, h - 1);   //h
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h + title_size3 + h, width - 1, H - 1);   //H
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h + title_size3 + h + H, width - 1, h - 1);   //h
            */

            g.DrawRectangle(p, 0, 0, width - 1, height - 1);

            int x_st = 0;
            int y_st = 0;
            int x_sp = 0;
            int y_sp = 0;
            int offset = 10;

            int h_st = height;

            int[] x_data = new int[21];
            int[] y_data = new int[21];
            Point point0;
            Point point1;
            Point point2;
            Point point3;
            Point point4;
            Point point5;
            Point point6;
            Point point7;
            Point point8;
            Point point9;
            Point point10;
            Point point11;
            Point point12;
            Point point13;
            Point point14;
            Point point15;
            Point point16;
            Point point17;
            Point point18;
            Point point19;
            Point point20;

            int dx = 22;
            y_st = h + H + h + title_size3 + h;

            if ((draw_case == 1) || (draw_case == 2))
            {
                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;
                x_data[5] = dx * 5; y_data[5] = y_st;
                x_data[6] = dx * 6; y_data[6] = y_st;
                x_data[7] = dx * 7; y_data[7] = y_st;
                x_data[8] = dx * 8; y_data[8] = y_st;
                x_data[9] = dx * 9; y_data[9] = y_st;

                x_data[10] = dx * 10; y_data[10] = y_st;
                y_st += H;
                x_data[11] = dx * 10; y_data[11] = y_st;

                x_data[12] = dx * 11; y_data[12] = y_st;
                y_st -= H;
                x_data[13] = dx * 11; y_data[13] = y_st;

                x_data[14] = dx * 12; y_data[14] = y_st;
                y_st += H;
                x_data[15] = dx * 12; y_data[15] = y_st;

                x_data[16] = dx * 13; y_data[16] = y_st;
                y_st -= H;
                x_data[17] = dx * 13; y_data[17] = y_st;

                x_data[18] = dx * 14; y_data[18] = y_st;
                y_st += H;
                x_data[19] = dx * 14; y_data[19] = y_st;

                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線

                y_st = h;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;
                x_data[5] = dx * 5; y_data[5] = y_st;
                x_data[6] = dx * 6; y_data[6] = y_st;
                x_data[7] = dx * 7; y_data[7] = y_st;
                x_data[8] = dx * 8; y_data[8] = y_st;
                x_data[9] = dx * 9; y_data[9] = y_st;

                x_data[10] = dx * 10; y_data[10] = y_st;
                y_st += H;
                x_data[11] = dx * 10; y_data[11] = y_st;

                x_data[12] = dx * 11; y_data[12] = y_st;
                y_st -= H;
                x_data[13] = dx * 11; y_data[13] = y_st;

                x_data[14] = dx * 12; y_data[14] = y_st;
                y_st += H;
                x_data[15] = dx * 12; y_data[15] = y_st;

                x_data[16] = dx * 13; y_data[16] = y_st;
                y_st -= H;
                x_data[17] = dx * 13; y_data[17] = y_st;

                x_data[18] = dx * 14; y_data[18] = y_st;
                y_st += H;
                x_data[19] = dx * 14; y_data[19] = y_st;

                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints2 = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(redPen, curvePoints2);   //畫直線
            }
            else if ((draw_case == 3) || (draw_case == 4))
            {
                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 8; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 8; y_data[8] = y_st;

                x_data[9] = dx * 8; y_data[9] = y_st;
                x_data[10] = dx * 10; y_data[10] = y_st;
                x_data[11] = dx * 11; y_data[11] = y_st;
                x_data[12] = dx * 12; y_data[12] = y_st;
                x_data[13] = dx * 13; y_data[13] = y_st;
                x_data[14] = dx * 14; y_data[14] = y_st;

                x_data[15] = dx * 15; y_data[15] = y_st;
                y_st += H;
                x_data[16] = dx * 15; y_data[16] = y_st;

                x_data[17] = dx * 18; y_data[17] = y_st;
                y_st -= H;
                x_data[18] = dx * 18; y_data[18] = y_st;

                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線




                y_st = h + offset;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 20; y_data[1] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);

                Point[] curvePoints3 = { point0, point1 };

                // Draw lines between original points to screen.
                g.DrawLines(blackPen, curvePoints3);   //畫直線
            }
            else if (draw_case == 5)
            {
                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 7; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 7; y_data[8] = y_st;

                x_data[9] = dx * 7; y_data[9] = y_st;
                x_data[10] = dx * 10; y_data[10] = y_st;
                x_data[11] = dx * 11; y_data[11] = y_st;
                x_data[12] = dx * 12; y_data[12] = y_st;
                x_data[13] = dx * 13; y_data[13] = y_st;
                x_data[14] = dx * 14; y_data[14] = y_st;

                x_data[15] = dx * 15; y_data[15] = y_st;
                y_st += H;
                x_data[16] = dx * 15; y_data[16] = y_st;

                x_data[17] = dx * 17; y_data[17] = y_st;
                y_st -= H;
                x_data[18] = dx * 17; y_data[18] = y_st;

                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線


                y_st = h;


                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 8; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 8; y_data[8] = y_st;

                x_data[9] = dx * 8; y_data[9] = y_st;
                x_data[10] = dx * 10; y_data[10] = y_st;
                x_data[11] = dx * 11; y_data[11] = y_st;
                x_data[12] = dx * 12; y_data[12] = y_st;
                x_data[13] = dx * 13; y_data[13] = y_st;
                x_data[14] = dx * 14; y_data[14] = y_st;

                x_data[15] = dx * 15; y_data[15] = y_st;
                y_st += H;
                x_data[16] = dx * 15; y_data[16] = y_st;

                x_data[17] = dx * 18; y_data[17] = y_st;
                y_st -= H;
                x_data[18] = dx * 18; y_data[18] = y_st;

                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints2 = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(redPen, curvePoints2);   //畫直線






                /*
                y_st = h + offset;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 20; y_data[1] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);

                Point[] curvePoints3 = { point0, point1 };

                // Draw lines between original points to screen.
                g.DrawLines(blackPen, curvePoints3);   //畫直線
                */


            }
            else if (draw_case == 6)
            {

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 6; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 6; y_data[8] = y_st;

                x_data[9] = dx * 7; y_data[9] = y_st;
                y_st += H;
                x_data[10] = dx * 7; y_data[10] = y_st;

                x_data[11] = dx * 8; y_data[11] = y_st;
                y_st -= H;
                x_data[12] = dx * 8; y_data[12] = y_st;

                x_data[13] = dx * 9; y_data[13] = y_st;
                y_st += H;
                x_data[14] = dx * 9; y_data[14] = y_st;

                x_data[15] = dx * 10; y_data[15] = y_st;
                y_st -= H;
                x_data[16] = dx * 10; y_data[16] = y_st;

                x_data[17] = dx * 18; y_data[17] = y_st;
                x_data[18] = dx * 18; y_data[18] = y_st;
                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線




                y_st = h + offset;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 20; y_data[1] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);

                Point[] curvePoints3 = { point0, point1 };

                // Draw lines between original points to screen.
                g.DrawLines(blackPen, curvePoints3);   //畫直線



            }


            ArrowPen = new Pen(Color.Red, 6);   //重新設定pp的線條樣式
            ArrowPen.EndCap = LineCap.ArrowAnchor;

            if ((draw_case == 1) || (draw_case == 2))
            {
                x_st = dx * 10;
                y_st = h_st - (h + H + h + title_size3 + h + offset);

                x_sp = dx * 10;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
            }
            else if (draw_case == 3)
            {

            }
            else if (draw_case == 4)
            {
                x_st = dx * 8 + 3;
                y_st = h_st - (h + H + h + title_size3 + h + offset);
                x_sp = dx * 8 + 3;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                g.DrawString("Initialize OK", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st, y_st - H / 2));

                x_st = dx * 18 + 3;
                y_st = h_st - (h + H + h + title_size3 + h + offset);
                x_sp = dx * 18 + 3;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

            }
            else if (draw_case == 5)
            {

            }
            else if (draw_case == 6)
            {
                x_st = dx * 5;
                y_st = h_st - (h + H + h + title_size3 + h + offset);

                x_sp = dx * 5;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

            }

            ArrowPen = new Pen(Color.Blue, 6);   //重新設定pp的線條樣式
            ArrowPen.EndCap = LineCap.ArrowAnchor;

            if (draw_case == 1)
            {
                x_st = dx * 10;
                y_st = h_st - (h + offset);

                x_sp = dx * 10;
                y_sp = h_st - (h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 11;
                x_sp = dx * 11;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 12;
                x_sp = dx * 12;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 13;
                x_sp = dx * 13;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 14;
                x_sp = dx * 14;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
            }
            else if (draw_case == 2)
            {

                y_st = h_st - (h + offset);
                y_sp = h_st - (h + offset + (H - offset * 2));

                for (int i = 1; i < 13; i++)
                {
                    x_st = dx * i * 3 / 2 + 5;
                    x_sp = dx * i * 3 / 2 + 5;
                    if (i == 12)
                    {
                        ArrowPen = new Pen(Color.Red, 10);   //重新設定pp的線條樣式
                        ArrowPen.EndCap = LineCap.ArrowAnchor;
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
                    }
                    else
                    {
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
                    }
                }
            }
            else if (draw_case == 3)
            {
                y_st = h_st - (h + offset);
                y_sp = h_st - (h + offset + (H - offset * 2));

                int x_st2 = 0;
                int y_st2 = h_st - (h + 60);
                int x_sp2 = 0;
                int y_sp2 = h_st - (h + 60);

                for (int i = 1; i < 4; i++)
                {
                    x_st = dx * i * 13 / 2 - 70;
                    x_sp = dx * i * 13 / 2 - 70;
                    richTextBox1.Text += "x = " + x_st.ToString() + "\n";
                    if (i == 3)
                    {
                        ArrowPen = new Pen(Color.Red, 10);   //重新設定pp的線條樣式
                        ArrowPen.EndCap = LineCap.ArrowAnchor;
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                        //int height = h + title_size1 + title_size2 + h + H + h + title_size3 + h + H + h;
                        Pen p2 = new Pen(Color.Black, 2);
                        p2.DashStyle = DashStyle.Dash;
                        g.DrawLine(p2, x_st, h + title_size1 + 30, x_sp, height);
                    }
                    else
                    {
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
                    }
                    if (i == 1)
                        x_st2 = x_st;
                    if (i == 2)
                        x_sp2 = x_st;
                }

                ArrowPen = new Pen(Color.Red, 5);   //重新設定pp的線條樣式
                ArrowPen.StartCap = LineCap.ArrowAnchor;
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                richTextBox1.Text += "x_st2 = " + x_st2.ToString() + "x_sp2 = " + x_sp2.ToString() + "\n";

                g.DrawString("1 sec", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2 + 40, y_st2 + 5));
                g.DrawString("Conflict!", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(315, y_st2 - 55));

            }
            else if (draw_case == 4)
            {
                int x_st2 = 0;
                int y_st2 = h_st - (h + offset);
                int x_sp2 = 0;
                int y_sp2 = h_st - (h + offset + (H - offset * 2));

                x_st2 = dx * 8 + 6;
                x_sp2 = dx * 8 + 6;
                ArrowPen = new Pen(Color.Red, 8);   //重新設定pp的線條樣式
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                //richTextBox1.Text += "(" + x_st2.ToString() + ", " + y_st2.ToString() + ") - (" + x_sp2.ToString() + ", " + y_sp2.ToString() + ")\n";

                g.DrawString("Detect OK Signal", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2, y_st2 - H / 2));

                x_st2 = dx * 18 + 6;
                x_sp2 = dx * 18 + 6;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                //richTextBox1.Text += "(" + x_st2.ToString() + ", " + y_st2.ToString() + ") - (" + x_sp2.ToString() + ", " + y_sp2.ToString() + ")\n";
            }
            else if (draw_case == 5)
            {



            }
            else if (draw_case == 6)
            {
                int x_st2 = 0;
                int y_st2 = h_st - (h + offset);
                int x_sp2 = 0;
                int y_sp2 = h_st - (h + offset + (H - offset * 2));

                x_st2 = dx * 5;
                x_sp2 = dx * 5;
                ArrowPen = new Pen(Color.Red, 8);   //重新設定pp的線條樣式
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                //richTextBox1.Text += "(" + x_st2.ToString() + ", " + y_st2.ToString() + ") - (" + x_sp2.ToString() + ", " + y_sp2.ToString() + ")\n";

                g.DrawString("Detect OK Signal", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2 + 10, y_st2 - H / 2 - 30));



                ArrowPen = new Pen(Color.Black, 5);   //重新設定pp的線條樣式
                ArrowPen.StartCap = LineCap.ArrowAnchor;
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2 - H / 2 + 20, x_st2 + 300, y_st2 - H / 2 + 20);
                richTextBox1.Text += "x_st2 = " + x_st2.ToString() + "x_sp2 = " + x_sp2.ToString() + "\n";

                g.DrawString("0.2 sec", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2 + 120, y_st2 - H / 2 + 25));



            }

            int offset2 = 15;
            SolidBrush sb;
            Font f;
            f = new Font("Times New Roman", 17);
            sb = new SolidBrush(Color.Purple);
            if ((draw_case == 1) || (draw_case == 2))
            {
                g.DrawString("IE Insert Bouncing", f, sb, new PointF(0, h + offset2));
                //g.DrawString("Push Button Bouncing", f, sb, new PointF(0, h + offset2));
            }
            else if ((draw_case == 3) || (draw_case == 4))
            {
                g.DrawString("IE initialization fails", f, sb, new PointF(0, h + offset2));
            }
            else if (draw_case == 5)
            {
                g.DrawString("Send Command to IE Error", f, sb, new PointF(0, h + offset2));
            }
            else if (draw_case == 6)
            {
                g.DrawString("Pedal Bouncing", f, sb, new PointF(0, h + offset2));
            }

            if ((draw_case == 1) || (draw_case == 2))
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("IE Insert", f, sb, new PointF(0, h + title_size1 + offset2));
                //g.DrawString("User Push Button", f, sb, new PointF(0, h + title_size1 + offset2));
                if (draw_case == 1)
                {
                    sb = new SolidBrush(Color.Green);
                    f = new Font("Times New Roman", 11);
                    g.DrawString("Hardware Response", f, sb, new PointF(310, h + title_size1 + title_size2 + h + 10));
                }
            }
            else if ((draw_case == 3) || (draw_case == 4))
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("IE Plug-in & initialize", f, sb, new PointF(0, h + title_size1 + offset2));
            }
            else if (draw_case == 5)
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("Send Data without Check-Sum", f, sb, new PointF(0, h + title_size1 + offset2));
            }
            else if (draw_case == 6)
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("Real Pedal Bouncing", f, sb, new PointF(0, h + title_size1 + offset2));
            }


            f = new Font("Times New Roman", 17);
            sb = new SolidBrush(Color.Blue);
            if (draw_case == 1)
                g.DrawString("Software Response", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 2)
                g.DrawString("Software Detect Stable IE Signal", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 3)
                g.DrawString("Software Detect IE", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 4)
                g.DrawString("Software Detect IE OK Signal", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 5)
                g.DrawString("Send Data with Check-Sum", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 6)
                g.DrawString("Software Catthes First One", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));

            pictureBox1.Image = bitmap1;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            g.Clear(Color.White);
            //畫各種編碼的區間
            int xx;
            int yy;
            int dd = 20;
            int allow = 0;

            //richTextBox1.Text += "W = " + this.pictureBox1.Width.ToString() + " H = " + this.pictureBox1.Height.ToString() + "\n";

            //Graphics g = pictureBox1.CreateGraphics();
            //g.Clear(Color.White);
            //DrawXY();

            Point[] pt1 = new Point[656];    //一維陣列內有360個Point
            yy = 200;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt1[xx / 100].X = xx / 100;
                if ((((xx / 256) >= 0xA1) && ((xx / 256) <= 0xE7)) && (((xx % 256) >= 0xA1) && ((xx % 256) <= 0xFE)))
                {
                    pt1[xx / 100].Y = yy - 100 + dd;
                    allow++;
                }
                else
                {
                    //pt1[xx / 100].Y = 300 - 100;
                    pt1[xx / 100].Y = yy - dd;
                }
            }
            g.DrawLines(new Pen(Brushes.Red, 3), pt1);
            g.DrawString("GB2313", new Font("標楷體", 30), new SolidBrush(Color.Red), new PointF(20, yy - 80));
            richTextBox1.Text += "e1 allow = " + allow.ToString() + "\n";

            Point[] pt2 = new Point[656];    //一維陣列內有360個Point
            yy = 300;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt2[xx / 100].X = xx / 100;
                if ((((xx / 256) >= 0x81) && ((xx / 256) <= 0xFE)) && ((((xx % 256) >= 0x40) && ((xx % 256) <= 0x7E)) || (((xx % 256) >= 0x80) && ((xx % 256) <= 0xFE))))
                {
                    pt2[xx / 100].Y = yy - 100 + dd;
                    allow++;
                    //pt1[xx / 100].Y = 300 - 100;
                }
                else
                {
                    //pt1[xx / 100].Y = 300 - 100;
                    pt2[xx / 100].Y = yy - dd;
                }
            }
            g.DrawLines(new Pen(Brushes.Green, 3), pt2);
            g.DrawString("GBK", new Font("標楷體", 30), new SolidBrush(Color.Green), new PointF(20, yy - 80));
            richTextBox1.Text += "e2 allow = " + allow.ToString() + "\n";

            Point[] pt3 = new Point[656];    //一維陣列內有360個Point
            yy = 400;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt3[xx / 100].X = xx / 100;
                if ((((xx / 256) >= 0x81) && ((xx / 256) <= 0xFE)) && ((((xx % 256) >= 0x40) && ((xx % 256) <= 0x7E)) || (((xx % 256) >= 0xA1) && ((xx % 256) <= 0xFE))))
                {
                    pt3[xx / 100].Y = yy - 100 + dd;
                    allow++;
                    //pt1[xx / 100].Y = 300 - 100;
                }
                else
                {
                    //pt1[xx / 100].Y = 300 - 100;
                    pt3[xx / 100].Y = yy - dd;
                }
            }
            g.DrawLines(new Pen(Brushes.Blue, 3), pt3);
            g.DrawString("GB2313", new Font("Big5", 30), new SolidBrush(Color.Blue), new PointF(20, yy - 80));
            richTextBox1.Text += "e3 allow = " + allow.ToString() + "\n";

            Point[] pt4 = new Point[656];    //一維陣列內有360個Point
            yy = 500;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt4[xx / 100].X = xx / 100;
                if ((xx > 0x4e00) && (xx < 0x9fbf))
                {
                    pt4[xx / 100].Y = yy - 100 + dd;
                    allow++;
                }
                else
                {
                    pt4[xx / 100].Y = yy - dd;
                }
            }
            g.DrawLines(new Pen(Brushes.Yellow, 3), pt4);
            g.DrawString("Unicode", new Font("標楷體", 30), new SolidBrush(Color.Yellow), new PointF(20, yy - 80));
            richTextBox1.Text += "e4 allow = " + allow.ToString() + "\n";
            pictureBox1.Image = bitmap1;
        }

        //畫OV亮度
        private void button11_Click(object sender, EventArgs e)
        {
            g.Clear(Color.White);

            int i;
            double gamma;

            int[] data_in = new int[256];
            int[] data_out = new int[256];
            Point[] curvePoints = new Point[256];    //一維陣列內有 N 個Point

            Pen gammaPen = new Pen(Color.Red, 2);
            gamma = 2.2;
            //畫出真正的 Gamma 2.2曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(gammaPen, curvePoints);   //畫直線

            pictureBox1.Image = bitmap1;
        }

        void DrawCircle(Graphics g, Pen p, int cx, int cy, int r)
        {
            g.DrawEllipse(p, cx - r, cy - r, r * 2, r * 2);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            int W = 340;
            int H = 543;
            int x_st;
            int y_st;
            int w;
            int h;

            Graphics g;

            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            sb = new SolidBrush(Color.Red);
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(0, 0, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(W - w, 0, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(0, H - h, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(W - w, H - h, w, h));

            //door
            x_st = 0; y_st = 6 + 205; w = 10; h = 88; g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h));

            //window
            x_st = W - 10; y_st = 6 + 66; w = 10; h = 205; g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h));

            Font f;
            f = new Font("Times New Roman", 14);
            sb = new SolidBrush(Color.Black);
            g.DrawString("205", f, sb, new PointF(0, 205 / 2));
            g.DrawString("268", f, sb, new PointF(0, 573 - 6 - 268 + 268 / 2));
            g.DrawString("66", f, sb, new PointF(W - 30, 66 / 2));
            g.DrawString("290", f, sb, new PointF(W - 40, 573 - 6 - 290 + 290 / 2));

            Pen p = new Pen(Color.Black, 5);
            p.StartCap = LineCap.ArrowAnchor;
            p.EndCap = LineCap.ArrowAnchor;  //EndCap設定 這支筆的結尾會是個箭頭

            g.DrawLine(p, 0, H + 10, W, H + 10);
            g.DrawLine(p, W + 10, 0, W + 10, H);
            g.DrawString("340", f, sb, new PointF(W / 2, H + 15));
            g.DrawString("573", f, sb, new PointF(W + 15, H / 2));

            int dw;
            int dh;

            //draw desk
            dw = 152;
            dh = 78;

            x_st = (W - dw) / 2;
            //y_st = (H - dh) / 2;
            y_st = 205 + 6 - dh;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));
            //g.DrawEllipse(new Pen(Color.Red, 3), cx - r, cy - r, r * 2, r * 2);
            int cx = W / 2;
            int cy = 90;
            int r = 30;
            DrawCircle(g, new Pen(Color.Black), cx, cy, r);

            /*
            x_st = W - dh - 12;
            y_st = 6 + 66 + 205;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dh, dw));
            g.DrawString("138", f, sb, new PointF(W + 15, H - 152 / 2));
            */

            //draw sofa
            dw = 180;
            dh = 86;
            x_st = 0;
            y_st = H - dh;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));
            g.DrawString("180", f, sb, new PointF(180 / 2 - 10, H - 86));
            g.DrawString("86", f, sb, new PointF(180, H - 86 / 2 - 10));

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, W, H));
            //p = new Pen(Color.Black, 1);
            //g.DrawLine(p, 0, 0, W, H);
            //g.DrawLine(p, W, 0, 0, H);

            pictureBox1.Image = bitmap1;
        }

        void draw_bookshelf(Graphics g, int x_st, int y_st, int M, int N)
        {
            //M     //橫向
            //N     //高
            int i;
            int j;
            int d = 7;
            int D = 28;
            //int x_sp;
            //int y_sp;
            int w = 0;
            int h = 0;

            p = new Pen(Color.Black, 1);

            w = M * D + (M + 1) * d;
            h = N * D + (N + 1) * d;

            //x_sp = x_st + M * D + (M + 1) * d;
            //y_sp = y_st + N * D + (N + 1) * d;

            for (i = 0; i <= M; i++)
            {
                g.DrawLine(p, x_st + i * (d + D), y_st, x_st + i * (d + D), y_st + h);
                g.DrawLine(p, x_st + i * (d + D) + d, y_st, x_st + i * (d + D) + d, y_st + h);
            }

            for (j = 0; j <= N; j++)
            {
                g.DrawLine(p, x_st, y_st + j * (d + D), x_st + w, y_st + j * (d + D));
                g.DrawLine(p, x_st, y_st + j * (d + D) + d, x_st + w, y_st + j * (d + D) + d);
            }

        }

        private void button13_Click(object sender, EventArgs e)
        {
            int W = 532;
            int H = 543;
            int x_st;
            int y_st;
            int w;
            int h;

            Graphics g;

            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            sb = new SolidBrush(Color.Red);
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(0, 0, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(W - w, 0, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(0, H - h, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(W - w, H - h, w, h));

            //door1
            x_st = W - 10; y_st = 6 + 205; w = 10; h = 90; g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h));

            //door2
            x_st = W - 10; y_st = 6 + 205 + 90 + 12; w = 10; h = 75; g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h));

            //window1
            x_st = 0; y_st = 6 + 65; w = 10; h = 90; g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h));

            //window2
            x_st = 0; y_st = 6 + 65 + 90 + 126; w = 10; h = 200; g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h));

            Font f;
            f = new Font("Times New Roman", 14);
            sb = new SolidBrush(Color.Black);
            //g.DrawString("205", f, sb, new PointF(0, 205 / 2));
            //g.DrawString("268", f, sb, new PointF(0, 573 - 6 - 268 + 268 / 2));
            //g.DrawString("66", f, sb, new PointF(W - 30, 66 / 2));
            //g.DrawString("290", f, sb, new PointF(W - 40, 573 - 6 - 290 + 290 / 2));

            Pen p = new Pen(Color.Black, 5);
            p.StartCap = LineCap.ArrowAnchor;
            p.EndCap = LineCap.ArrowAnchor;  //EndCap設定 這支筆的結尾會是個箭頭

            g.DrawLine(p, 0, H + 10, W, H + 10);
            g.DrawLine(p, W + 10, 0, W + 10, H);
            g.DrawString("532", f, sb, new PointF(W / 2, H + 15));
            g.DrawString("573", f, sb, new PointF(W + 15, H / 2 + 100));

            int dw;
            int dh;

            //draw desk
            dw = 140;
            dh = 78;

            //x_st = (W - dw) / 2;
            x_st = 30;
            //y_st = (H - dh) / 2;
            y_st = 6;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));
            g.DrawString(dw.ToString(), f, sb, new PointF(x_st + dw / 3, y_st));
            g.DrawString(dh.ToString(), f, sb, new PointF(x_st, dh / 2));


            int cx = 30 + dw / 2;
            int cy = dh + 50;
            int r = 30;
            DrawCircle(g, new Pen(Color.Black), cx, cy, r);

            /*
            x_st = W - dh - 12;
            y_st = 6 + 66 + 205;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dh, dw));
            g.DrawString("138", f, sb, new PointF(W + 15, H - 152 / 2));
            */

            //draw sofa
            dw = 190;
            dh = 86;
            x_st = W - dh;
            //y_st = 6 + 205 - dw;
            y_st = 6;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dh, dw));
            //g.DrawString("180", f, sb, new PointF(180 / 2 - 10, H - 86));
            //g.DrawString("86", f, sb, new PointF(180, H - 86 / 2 - 10));

            //draw bed
            dw = 204;
            dh = 225;
            x_st = (W - dw) / 2;
            //y_st = (6 + 205 + 90 + 12 + 75 + 183 + 6) - 225;
            y_st = H - dh;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));

            Bitmap bmp = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\BMW.jfif");

            Rectangle destRect1 = new Rectangle(x_st + 12, y_st + 10, 180, 180);

            float x = 0;
            float y = 0;
            float width = bmp.Width;
            float height = bmp.Height;

            GraphicsUnit units = GraphicsUnit.Pixel;
            g.DrawImage(bmp, destRect1, x, y, width, height, units);

            //draw pillow
            dw = 204 - 50;
            dh = 25;
            x_st = (W - dw) / 2;
            //y_st = (6 + 205 + 90 + 12 + 75 + 183 + 6) - 225;
            y_st = H - dh;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));

            //床頭櫃 dw=45,dh=45
            dw = 60;
            dh = 60;
            x_st = (W - 204) / 2 - dw;
            //y_st = (6 + 205 + 90 + 12 + 75 + 183 + 6) - 225;
            y_st = H - dh;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));

            x_st = (W + 204) / 2;
            //y_st = (6 + 205 + 90 + 12 + 75 + 183 + 6) - 225;
            y_st = H - dh;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));

            //draw cabinet1  dw=147,dh=39
            dw = 147;
            dh = 39;
            x_st = W - dw - 100;
            y_st = 0;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));

            //draw cabinet1  dw=112,dh=39
            dw = 112;
            dh = 39;
            x_st = W - dw - 100 - 147;
            y_st = 0;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));

            //draw division  dw=200,dh=40
            dw = 30 + 140;
            dh = 40;
            x_st = 0;
            y_st = 220;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));


            draw_bookshelf(g, 560, 50, 3, 3);
            draw_bookshelf(g, 560, 50 + 112, 3, 3);
            draw_bookshelf(g, 560 + 112, 50, 4, 3);
            draw_bookshelf(g, 560 + 112, 50 + 112, 4, 3);

            //draw_bookshelf(600, 200, 5, 2);

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, W, H));
            //p = new Pen(Color.Black, 1);
            //g.DrawLine(p, 0, 0, W, H);
            //g.DrawLine(p, W, 0, 0, H);

            pictureBox1.Image = bitmap1;
        }

        void open_test_file()
        {
            //開檔
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims03.bmp";
            Image image1 = new Bitmap(filename, true);
            pictureBox1.Image = image1;
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.ClientSize = new Size(image1.Size.Width, image1.Size.Height);    //設定pictureBox的大小

            richTextBox1.Text += "W = " + image1.Size.Width.ToString() + "  H = " + image1.Size.Height.ToString() + "\n";
        }

        void find_brightness()
        {
            //找過亮
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims03.bmp";
            bitmap1 = new Bitmap(filename);
            Graphics g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;

            int i;
            int j;
            int A;
            int R;
            int G;
            int B;
            int search_size = 256;   //256X256
            int awb_block = 32;     //AWB block size width, height
            int ww = awb_block;
            int hh = awb_block;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int center_x = W / 2;
            int center_y = H / 2;
            int x_st = center_x - search_size / 2;
            int y_st = center_y - search_size / 2;

            for (i = 0; i <= (search_size / awb_block); i++)
            {
                g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + search_size - 1, y_st + awb_block * i);
                g.DrawLine(new Pen(Color.Red, 1), x_st + awb_block * i, y_st, x_st + awb_block * i, y_st + search_size - 1);
            }

            int[] saturation_array = new int[(search_size / awb_block) * (search_size / awb_block)];

            int upper_bound = 240;
            for (j = y_st; j < (y_st + search_size); j++)
            {
                for (i = x_st; i < (x_st + search_size); i++)
                {
                    Color pp = bitmap1.GetPixel(i, j);

                    A = pp.A;
                    R = pp.R;
                    G = pp.G;
                    B = pp.B;

                    if ((R >= upper_bound) && (G >= upper_bound) && (B >= upper_bound))
                    {
                        saturation_array[((i - x_st) / awb_block) + (((j - y_st) / awb_block)) * (search_size / awb_block)]++;

                    }
                }
            }

            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(60, 0, 255, 0));
            //richTextBox1.Text += "\nresult:\n";
            for (i = 0; i < saturation_array.Length; i++)
            {
                //richTextBox1.Text += "saturation_array[" + i.ToString() + "] = " + saturation_array[i].ToString() + "\n";
                if (saturation_array[i] == 0)
                {
                    g.FillRectangle(semiTransBrush, new Rectangle(x_st + awb_block * (i % (search_size / awb_block)), y_st + awb_block * (i / (search_size / awb_block)), awb_block, awb_block));
                }
            }
        }

        void do_statistics()
        {
            //統計
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims03.bmp";
            bitmap1 = new Bitmap(filename);
            Graphics g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;

            Graphics g2 = pictureBox2.CreateGraphics();
            //pictureBox1.Image = bitmap1;

            int i;
            int j;
            int A;
            int R;
            int G;
            int B;
            int search_size = 256;   //256X256
            int awb_block = 32;     //AWB block size width, height
            int ww = awb_block;
            int hh = awb_block;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int center_x = W / 2;
            int center_y = H / 2;
            int x_st = center_x - search_size / 2;
            int y_st = center_y - search_size / 2;

            int[,] rgb_array = new int[3, 16];

            for (i = 0; i <= (search_size / awb_block); i++)
            {
                g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + search_size - 1, y_st + awb_block * i);
                g.DrawLine(new Pen(Color.Red, 1), x_st + awb_block * i, y_st, x_st + awb_block * i, y_st + search_size - 1);
            }

            int[] saturation_array = new int[(search_size / awb_block) * (search_size / awb_block)];

            int upper_bound = 240;
            for (j = y_st; j < (y_st + search_size); j++)
            {
                for (i = x_st; i < (x_st + search_size); i++)
                {
                    Color pp = bitmap1.GetPixel(i, j);

                    A = pp.A;
                    R = pp.R;
                    G = pp.G;
                    B = pp.B;

                    if ((R >= upper_bound) && (G >= upper_bound) && (B >= upper_bound))
                    {
                        saturation_array[((i - x_st) / awb_block) + (((j - y_st) / awb_block)) * (search_size / awb_block)]++;

                    }
                    rgb_array[0, (R / 16)] += R;
                    rgb_array[1, (G / 16)] += G;
                    rgb_array[2, (B / 16)] += B;
                }

            }

            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(60, 0, 255, 0));
            //richTextBox1.Text += "\nresult:\n";
            for (i = 0; i < saturation_array.Length; i++)
            {
                //richTextBox1.Text += "saturation_array[" + i.ToString() + "] = " + saturation_array[i].ToString() + "\n";
                if (saturation_array[i] == 0)
                {
                    g.FillRectangle(semiTransBrush, new Rectangle(x_st + awb_block * (i % (search_size / awb_block)), y_st + awb_block * (i / (search_size / awb_block)), awb_block, awb_block));
                }
            }

            int rgb_max = 0;

            richTextBox1.Text += "R = " + "\n";
            for (i = 0; i < 16; i++)
            {
                richTextBox1.Text += rgb_array[0, i].ToString() + " ";
                if (rgb_max < rgb_array[0, i])
                    rgb_max = rgb_array[0, i];
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "G = " + "\n";
            for (i = 0; i < 16; i++)
            {
                richTextBox1.Text += rgb_array[1, i].ToString() + " ";
                if (rgb_max < rgb_array[1, i])
                    rgb_max = rgb_array[1, i];
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "B = " + "\n";
            for (i = 0; i < 16; i++)
            {
                richTextBox1.Text += rgb_array[2, i].ToString() + " ";
                if (rgb_max < rgb_array[2, i])
                    rgb_max = rgb_array[2, i];
            }
            richTextBox1.Text += "\n";
            richTextBox1.Text += "rgb_max = " + rgb_max.ToString() + "\n";

            //g2.DrawRectangle(new Pen(Color.Red, 1), new Rectangle(50, 50, 200, 100));

            //g2.FillRectangle(new SolidBrush(Color.FromArgb(255, 0, 255, 0)), new Rectangle(50, 50, 200, 100));


            //SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(255, 0, 255, 0));

            int height = 300;
            int h = 0;
            richTextBox1.Text += "normalize\n";

            richTextBox1.Text += "R = " + "\n";
            for (i = 0; i < 16; i++)
            {
                h = (int)((double)rgb_array[0, i] * height / rgb_max);
                richTextBox1.Text += ((int)((double)rgb_array[0, i] * height / rgb_max)).ToString() + " ";

                if (h < 1)
                {
                    h = 1;
                }
                g2.FillRectangle(new SolidBrush(Color.FromArgb(255, 255, 0, 0)), new Rectangle(20 + i * 20, pictureBox2.Height - 50 - h, 4, h));

                //g2.FillRectangle(new SolidBrush(Color.FromArgb(255, 128, 128, 0)), new Rectangle(20 + i * 20, 50, 4, h));
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "G = " + "\n";
            for (i = 0; i < 16; i++)
            {
                h = (int)((double)rgb_array[1, i] * height / rgb_max);
                richTextBox1.Text += ((int)((double)rgb_array[1, i] * height / rgb_max)).ToString() + " ";
                if (h < 1)
                {
                    h = 1;
                }
                g2.FillRectangle(new SolidBrush(Color.FromArgb(255, 0, 255, 0)), new Rectangle(20 + i * 20 + 5, pictureBox2.Height - 50 - h, 4, h));
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "B = " + "\n";
            for (i = 0; i < 16; i++)
            {
                h = (int)((double)rgb_array[2, i] * height / rgb_max);
                richTextBox1.Text += ((int)((double)rgb_array[2, i] * height / rgb_max)).ToString() + " ";
                if (h < 1)
                {
                    h = 1;
                }
                g2.FillRectangle(new SolidBrush(Color.FromArgb(255, 0, 0, 255)), new Rectangle(20 + i * 20 + 10, pictureBox2.Height - 50 - h, 4, h));
            }
            richTextBox1.Text += "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            open_test_file();
            find_brightness();
            do_statistics();
        }

        //畫Gamma曲線
        private void button15_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(256 * 3 + 500, 256 * 2);   //改變圖框大小

            Graphics g;

            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            int i;
            double gamma;

            int[] data_in = new int[256];
            int[] data_out = new int[256];
            Point[] curvePoints = new Point[256];    //一維陣列內有 N 個Point

            Pen redPen = new Pen(Color.Red, 2);
            Pen greenPen = new Pen(Color.Green, 2);
            Pen bluePen = new Pen(Color.Blue, 2);
            Pen grayPen = new Pen(Color.Gray, 6);
            Pen blackPen = new Pen(Color.Black, 6);

            gamma = 2.2;
            //畫出真正的Gamma 2.2曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            //g.DrawLines(redPen, curvePoints);   //畫直線 gamma 2.2

            gamma = 2.3;
            //畫出真正的Gamma 2.3曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            //g.DrawLines(greenPen, curvePoints);   //畫直線 gamma 2.3

            gamma = 2.4;
            //畫出真正的Gamma 2.4曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(grayPen, curvePoints);   //畫直線 gamma 2.4


            int[] yst = new int[17];

            /*
            int YST0 = 0x00;    //必為0, 設為yst[0]
            int YST1 = 0x14;
            int YST2 = 0x22;
            int YST3 = 0x37;
            int YST4 = 0x4B;
            int YST5 = 0x5E;
            int YST6 = 0x6B;
            int YST7 = 0x76;
            int YST8 = 0x82;
            int YST9 = 0x8C;
            int YST10 = 0x9F;
            int YST11 = 0xAB;
            int YST12 = 0xB5;
            int YST13 = 0xCF;
            int YST14 = 0xDE;
            int YST15 = 0xED;
            int YSLP15 = 0x1B;  //設為yst[16]
            */

            yst[0] = 0x00;
            yst[1] = 0x14;
            yst[2] = 0x22;
            yst[3] = 0x37;
            yst[4] = 0x4B;
            yst[5] = 0x5E;
            yst[6] = 0x6B;
            yst[7] = 0x76;
            yst[8] = 0x82;
            yst[9] = 0x8C;
            yst[10] = 0x9F;
            yst[11] = 0xAB;
            yst[12] = 0xB5;
            yst[13] = 0xCF;
            yst[14] = 0xDE;
            yst[15] = 0xED;
            yst[16] = 0x1B;
            draw_gamma_curve(g, yst, Color.Red);    //OV spec上的數字, IC的預設值


            yst = new int[] { 0, 0x2C, 0x33, 0x41, 0x55, 0x67, 0x74, 0x7E, 0x87, 0x8F, 0x96, 0x9F, 0xAA, 0xB8, 0xC9, 0xDA, 0x1E };
            draw_gamma_curve(g, yst, Color.Green);  //gamma 2.4

            yst = new int[] { 0, 0x14, 0x22, 0x37, 0x4B, 0x5E, 0x68, 0x6F, 0x78, 0x7E, 0x86, 0x90, 0x99, 0xA7, 0xB1, 0xBA, 0x0E };
            draw_gamma_curve(g, yst, Color.Blue);   //HLG 2

            yst = new int[] { 0, 18, 34, 56, 86, 96, 107, 116, 125, 134, 141, 156, 168, 182, 192, 201, 14 };
            draw_gamma_curve(g, yst, Color.Yellow);

            int dy = 50;
            g.DrawString("灰色: 標準的gamma2.4".ToString(), new Font("細明體", 25), new SolidBrush(Color.Gray), new PointF(800, 50 + dy * 0));
            g.DrawString("紅色: IC的預設值".ToString(), new Font("細明體", 25), new SolidBrush(Color.Red), new PointF(800, 50 + dy * 1));
            g.DrawString("綠色: Gamma2.4 @ 2020/3/6".ToString(), new Font("細明體", 25), new SolidBrush(Color.Green), new PointF(800, 50 + dy * 2));
            g.DrawString("藍色: HLG2".ToString(), new Font("細明體", 25), new SolidBrush(Color.Blue), new PointF(800, 50 + dy * 3));
            g.DrawString("黃色: SLG".ToString(), new Font("細明體", 25), new SolidBrush(Color.Yellow), new PointF(800, 50 + dy * 4));

            g.DrawRectangle(new Pen(Color.Red, 5), new Rectangle(0, 0, pictureBox1.Width - 5, pictureBox1.Height - 5));  //畫外框
            pictureBox1.Image = bitmap1;
        }

        void draw_gamma_curve(Graphics g, int[] yst, Color color)
        {
            int i;
            int[] data_in = new int[256];
            int[] data_out = new int[256];
            Point[] curvePoints = new Point[256];    //一維陣列內有 N 個Point

            Pen p = new Pen(color, 2);

            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;

                if (data_in[i] <= 4)
                    data_out[i] = yst[0] + (yst[1] - yst[0]) * (data_in[i] - 0) / 4;
                else if (data_in[i] <= 8)
                    data_out[i] = yst[1] + (yst[2] - yst[1]) * (data_in[i] - 4) / 4;
                else if (data_in[i] <= 16)
                    data_out[i] = yst[2] + (yst[3] - yst[2]) * (data_in[i] - 8) / 8;
                else if (data_in[i] <= 32)
                    data_out[i] = yst[4] + (yst[4] - yst[3]) * (data_in[i] - 16) / 16;
                else if (data_in[i] <= 40)
                    data_out[i] = yst[5] + (yst[5] - yst[4]) * (data_in[i] - 32) / 8;
                else if (data_in[i] <= 48)
                    data_out[i] = yst[6] + (yst[6] - yst[5]) * (data_in[i] - 40) / 8;
                else if (data_in[i] <= 56)
                    data_out[i] = yst[7] + (yst[7] - yst[6]) * (data_in[i] - 48) / 8;
                else if (data_in[i] <= 64)
                    data_out[i] = yst[8] + (yst[8] - yst[7]) * (data_in[i] - 56) / 8;
                else if (data_in[i] <= 72)
                    data_out[i] = yst[9] + (yst[9] - yst[8]) * (data_in[i] - 64) / 8;
                else if (data_in[i] <= 80)
                    data_out[i] = yst[10] + (yst[10] - yst[9]) * (data_in[i] - 72) / 8;
                else if (data_in[i] <= 96)
                    data_out[i] = yst[11] + (yst[11] - yst[10]) * (data_in[i] - 80) / 16;
                else if (data_in[i] <= 112)
                    data_out[i] = yst[12] + (yst[12] - yst[11]) * (data_in[i] - 96) / 16;
                else if (data_in[i] <= 144)
                    data_out[i] = yst[13] + (yst[13] - yst[12]) * (data_in[i] - 112) / 32;
                else if (data_in[i] <= 176)
                    data_out[i] = yst[14] + (yst[14] - yst[13]) * (data_in[i] - 144) / 32;
                else if (data_in[i] <= 208)
                    data_out[i] = yst[15] + (yst[15] - yst[14]) * (data_in[i] - 176) / 32;
                else
                {
                    if (cb_manual.Checked == false)
                    {
                        data_out[i] = yst[15] + yst[16] * (data_in[i] - 208) / 64;
                    }
                    else
                    {
                        data_out[i] = yst[15] + yst[16] * (data_in[i] - 208) / 64;
                    }
                }
            }

            //int YSLP15 = 0x1B;
            //Yst15 + Yslp15 × (data - 208) / 64

            /*
            richTextBox1.Text += "In:\n";
            for (i = 0; i < 256; i++)
                richTextBox1.Text += data_in[i].ToString() + " ";
            richTextBox1.Text += "\n";
            */

            richTextBox1.Text += "Out:\n";
            for (i = 0; i < 256; i++)
                richTextBox1.Text += data_out[i].ToString() + " ";
            richTextBox1.Text += "\n";

            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = data_in[i] * 3;
                //curvePoints[i].Y = H - (int)y1_data[i] - 100;
                //curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + (draw_max - draw_min) / 2000) * 2;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;

                //curvePoints[i].X = i;
                //curvePoints[i].Y = H - (int)y1_data[i] - 100;
                //curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + (draw_max - draw_min) / 2000) * 2;
                //curvePoints[i].Y = 100;
            }
            g.DrawLines(p, curvePoints);   //畫直線
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //文本轉成圖片
            richTextBox1.Clear();

            //讀取純文字檔到richTextBox裏
            try
            {
                richTextBox1.LoadFile(@"D:\_git\vcs\_1.data\______test_files1\article.txt", RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            catch (FileNotFoundException)
            {
                richTextBox1.Text += "找不到檔案\n";
                return;
            }

            //獲取文本
            string text = richTextBox1.Text;

            //得到Bitmap(傳入Rectangle.Empty自動計算寬高)
            Bitmap bitmap1 = TextToBitmap(text, this.richTextBox1.Font, Rectangle.Empty, this.richTextBox1.ForeColor, this.richTextBox1.BackColor);

            //用PictureBox顯示
            this.pictureBox1.Image = bitmap1;
        }

        //通過系統Graphics繪圖把文字繪製到位圖上，然後顯示或保存起來，這裡用定義該函數
        /// <summary>
        /// 把文字轉換才Bitmap
        /// </summary>
        /// <param name="text"></param>
        /// <param name="font"></param>
        /// <param name="rect">用於輸出的矩形，文字在這個矩形內顯示，為空時自動計算</param>
        /// <param name="fontcolor">字體顏色</param>
        /// <param name="backColor">背景顏色</param>
        /// <returns></returns>
        private Bitmap TextToBitmap(string text, Font font, Rectangle rect, Color fontcolor, Color backColor)
        {
            Graphics g;
            Bitmap bitmap1;
            StringFormat format = new StringFormat(StringFormatFlags.NoClip);
            if (rect == Rectangle.Empty)
            {
                bitmap1 = new Bitmap(1, 1);
                g = Graphics.FromImage(bitmap1);
                //計算繪製文字所需的區域大小（根據寬度計算長度），重新創建矩形區域繪圖
                SizeF sizef = g.MeasureString(text, font, PointF.Empty, format);

                int width = (int)(sizef.Width + 1);
                int height = (int)(sizef.Height + 1);
                rect = new Rectangle(0, 0, width, height);
                bitmap1.Dispose();

                bitmap1 = new Bitmap(width, height);
            }
            else
            {
                bitmap1 = new Bitmap(rect.Width, rect.Height);
            }

            g = Graphics.FromImage(bitmap1);

            //使用ClearType字體功能
            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.ClearTypeGridFit;
            g.FillRectangle(new SolidBrush(backColor), rect);
            g.DrawString(text, font, Brushes.Black, rect, format);
            return bitmap1;
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        //Pie Chart 1 ST
        private void button20_Click(object sender, EventArgs e)
        {
            // Pie Chart 1, 10片
            // Brushes used to fill pie slices.
            Brush[] SliceBrushes =
            {
                Brushes.Red,
                Brushes.LightGreen,
                Brushes.Blue,
                Brushes.LightBlue,
                Brushes.Green,
                Brushes.Lime,
                Brushes.Orange,
                Brushes.Fuchsia,
                Brushes.Yellow,
                Brushes.Cyan,
            };
            // Pens used to outline pie slices.
            Pen[] SlicePens = { Pens.Black };

            // The data values to chart.
            float[] Values = new float[10];

            // Make some random data.
            Random rand = new Random();
            for (int i = 0; i < Values.Length; i++)
            {
                // Pick a random value between 5 and 40.
                Values[i] = (float)(5 + 35 * rand.NextDouble());
            }

            // Draw the pie chart.

            //Graphics g = pictureBox1.CreateGraphics();
            g.Clear(BackColor);

            g.SmoothingMode = SmoothingMode.AntiAlias;

            int x_st = 10;
            int y_st = 10;
            int W = 400;
            int H = 400;
            Rectangle rect = new Rectangle(10, 10, W - 20, W - 20);

            DrawLabeledPieChart(g, rect, -90, SliceBrushes, SlicePens, Values, "0.0", Font, Brushes.Black);
            pictureBox1.Image = bitmap1;
        }

        // Draw a pie chart.
        private static void DrawLabeledPieChart(Graphics g, Rectangle rect, float initial_angle, Brush[] brushes, Pen[] pens, float[] values, string label_format, Font label_font, Brush label_brush)
        {
            // Get the total of all angles.
            float total = values.Sum();

            g.DrawRectangle(new Pen(Color.Red, 3), rect);

            // Draw the slices.
            float start_angle = initial_angle;
            for (int i = 0; i < values.Length; i++)
            {
                float sweep_angle = values[i] * 360f / total;

                // Fill and outline the pie slice.
                g.FillPie(brushes[i % brushes.Length], rect, start_angle, sweep_angle);
                g.DrawPie(pens[i % pens.Length], rect, start_angle, sweep_angle);

                start_angle += sweep_angle;
            }

            // Label the slices.
            // We label the slices after drawing them all so one
            // slice doesn't cover the label on another very thin slice.
            using (StringFormat string_format = new StringFormat())
            {
                // Center text.
                string_format.Alignment = StringAlignment.Center;
                string_format.LineAlignment = StringAlignment.Center;

                // Find the center of the rectangle.
                float cx = (rect.Left + rect.Right) / 2f;
                float cy = (rect.Top + rect.Bottom) / 2f;

                // Place the label about 2/3 of the way out to the edge.
                float radius = (rect.Width + rect.Height) / 2f * 0.33f;

                start_angle = initial_angle;
                for (int i = 0; i < values.Length; i++)
                {
                    float sweep_angle = values[i] * 360f / total;

                    // Label the slice.
                    double label_angle = Math.PI * (start_angle + sweep_angle / 2f) / 180f;
                    float x = cx + (float)(radius * Math.Cos(label_angle));
                    float y = cy + (float)(radius * Math.Sin(label_angle));
                    g.DrawString(values[i].ToString(label_format), label_font, label_brush, x, y, string_format);

                    start_angle += sweep_angle;
                }
            }
        }
        //Pie Chart 1 SP

        //Pie Chart 2 ST
        private void button21_Click(object sender, EventArgs e)
        {
            //Pie Chart 2

            // Brushes used to fill pie slices.
            Brush[] SliceBrushes =
            {
                Brushes.Red,
                Brushes.LightGreen,
                Brushes.Blue,
                Brushes.LightBlue,
                Brushes.Green,
                Brushes.Lime,
                Brushes.Orange,
                Brushes.Fuchsia,
                Brushes.Yellow,
                Brushes.Cyan,
            };

            // Pens used to outline pie slices.
            Pen[] SlicePens = { Pens.Black };

            // Top 10 languages on September 13, 2012 according to:
            //      http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html
            // The data values to chart.
            float[] Values = 
            {
                19.295f,
                16.267f,
                9.770f,
                9.147f,
                6.596f,
                5.614f,
                5.528f,
                3.861f,
                2.267f,
                1.724f,
            };

            // The values' annotations.
            string[] Annotations = new string[]
            {
                "C",
                "Java",
                "Objective-C",
                "C++",
                "C#",
                "PHP",
                "(Visual) Basic",
                "Python",
                "Perl",
                "Ruby",
            };

            // Draw the pie chart.

            Graphics g = pictureBox1.CreateGraphics();

            const int top_margin = 30;
            const int left_margin = 15;
            g.Clear(BackColor);

            if ((pictureBox1.Size.Width < 2 * top_margin) || (pictureBox1.Size.Height < 2 * top_margin))
            {
                return;
            }
            g.SmoothingMode = SmoothingMode.AntiAlias;

            int circle_width = pictureBox1.Size.Height - 2 * top_margin;
            int annotation_width = (pictureBox1.Size.Width - circle_width) / 2 - 2 * left_margin;
            int annotation_height = pictureBox1.Size.Height - 2 * left_margin;
            Rectangle left_rect = new Rectangle(left_margin, left_margin, annotation_width, annotation_height);
            Rectangle ellipse_rect = new Rectangle(left_rect.Right + left_margin, top_margin, circle_width, circle_width);
            Rectangle right_rect = new Rectangle(ellipse_rect.Right + left_margin, left_rect.Top, left_rect.Width, left_rect.Height);
            using (Font annotation_font = new Font("Times New Roman", 12))
            {
                DrawAnnotatedPieChart(g,
                    ellipse_rect, left_rect, right_rect, 1.1f, 0,
                    SliceBrushes, SlicePens,
                    Values, Annotations, "0.0", Font, Brushes.Black,
                    annotation_font, Pens.Blue, Brushes.Green,
                    Brushes.LightBlue, null);
            }
        }

        // Draw a pie chart.
        private static void DrawAnnotatedPieChart(Graphics g, Rectangle ellipse_rect, Rectangle left_rect, Rectangle right_rect, float annotation_radius_scale, float initial_angle, Brush[] brushes, Pen[] pens, float[] values, string[] annotations, string label_format, Font label_font, Brush label_brush, Font annotation_font, Pen annotation_pen, Brush annotation_brush, Brush rectangle_brush, Pen rectangle_pen)
        {
            // Get the total of all angles.
            float total = values.Sum();

            // Draw the slices.
            float start_angle = initial_angle;
            for (int i = 0; i < values.Length; i++)
            {
                float sweep_angle = values[i] * 360f / total;

                // Fill and outline the pie slice.
                g.FillPie(brushes[i % brushes.Length], ellipse_rect, start_angle, sweep_angle);
                g.DrawPie(pens[i % pens.Length], ellipse_rect, start_angle, sweep_angle);

                start_angle += sweep_angle;
            }

            // Draw the rectangles if desired.
            if (rectangle_brush != null)
            {
                g.FillRectangle(rectangle_brush, left_rect);
                g.FillRectangle(rectangle_brush, right_rect);
            }
            if (rectangle_pen != null)
            {
                g.DrawRectangle(rectangle_pen, left_rect);
                g.DrawRectangle(rectangle_pen, right_rect);
            }

            // Label and annotate the slices.
            // We label the slices after drawing them all so one
            // slice doesn't cover the label on another very thin slice.
            using (StringFormat string_format = new StringFormat())
            {
                // Find the center of the rectangle.
                float cx = (ellipse_rect.Left + ellipse_rect.Right) / 2;
                float cy = (ellipse_rect.Top + ellipse_rect.Bottom) / 2;

                // Place the label about 2/3 of the way out to the edge.
                float radius = (ellipse_rect.Width + ellipse_rect.Height) / 2f * 0.33f;

                // Distances for annotation lines.
                float annotation_rx1 = ellipse_rect.Width / 2;
                float annotation_ry1 = ellipse_rect.Height / 2;
                float annotation_rx2 = annotation_rx1 * annotation_radius_scale;
                float annotation_ry2 = annotation_ry1 * annotation_radius_scale;

                start_angle = start_angle = initial_angle;
                for (int i = 0; i < values.Length; i++)
                {
                    float sweep_angle = values[i] * 360f / total;

                    // Label the slice.
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    double label_angle = Math.PI * (start_angle + sweep_angle / 2) / 180;
                    float x = cx + (float)(radius * Math.Cos(label_angle));
                    float y = cy + (float)(radius * Math.Sin(label_angle));
                    g.DrawString(values[i].ToString(label_format), label_font, label_brush, x, y, string_format);

                    // Draw a radial line to connect to the annotation.
                    float x1 = cx + (float)(annotation_rx1 * Math.Cos(label_angle));
                    float y1 = cy + (float)(annotation_rx1 * Math.Sin(label_angle));
                    float x2 = cx + (float)(annotation_rx2 * Math.Cos(label_angle));
                    float y2 = cy + (float)(annotation_rx2 * Math.Sin(label_angle));
                    g.DrawLine(annotation_pen, x1, y1, x2, y2);

                    // Draw a horizontal line to the annotation.
                    if (x2 < x1)
                    {
                        // Draw to the left.
                        g.DrawLine(annotation_pen, x2, y2, left_rect.Right, y2);

                        // Draw the annotation right justified.
                        string_format.Alignment = StringAlignment.Far;
                        g.DrawString(annotations[i], annotation_font, annotation_brush, left_rect.Right, y2, string_format);
                    }
                    else
                    {
                        // Draw to the right.
                        g.DrawLine(annotation_pen, x2, y2, right_rect.Left, y2);

                        // Draw the annotation left justified.
                        string_format.Alignment = StringAlignment.Near;
                        g.DrawString(annotations[i], annotation_font, annotation_brush, right_rect.Left, y2, string_format);
                    }
                    start_angle += sweep_angle;
                }
            }
        }
        //Pie Chart 2 SP

        //Pie Chart 3 ST
        private void button22_Click(object sender, EventArgs e)
        {
            //Pie Chart 3
            int W = 230;
            int H = 230;

            //pictureBox1.Size = new Size(W * 2, H * 2);

            // Brushes used to fill pie slices.
            Brush[] SliceBrushes =
            {
                Brushes.Red,
                Brushes.LightGreen,
                Brushes.Blue,
                Brushes.LightBlue,
                Brushes.Green,
                Brushes.Lime,
                Brushes.Orange,
                Brushes.Fuchsia,
                Brushes.Yellow,
                Brushes.Cyan,
            };

            // Pens used to outline pie slices.
            Pen[] SlicePens = { Pens.Black };

            // The data values to chart.
            float[] Values = new float[10];

            // Make some random data.
            Random rand = new Random();
            for (int i = 0; i < Values.Length; i++)
            {
                Values[i] = rand.Next(10, 40);
            }

            // Draw the pie chart.
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(BackColor);
            if ((pictureBox1.Size.Width < 20) || (pictureBox1.Size.Height < 20))
            {
                return;
            }

            g.SmoothingMode = SmoothingMode.AntiAlias;
            Rectangle rect = new Rectangle(10, 10, pictureBox1.Size.Width - 20, pictureBox1.Size.Height - 20);
            DrawPieChart(g, rect, SliceBrushes, SlicePens, Values);
        }

        // Draw a pie chart.
        private static void DrawPieChart(Graphics g, Rectangle rect, Brush[] brushes, Pen[] pens, float[] values)
        {
            // Get the total of all angles.
            float total = values.Sum();

            // Draw the slices.
            float start_angle = 0;
            for (int i = 0; i < values.Length; i++)
            {
                float sweep_angle = values[i] * 360f / total;
                g.FillPie(brushes[i % brushes.Length], rect, start_angle, sweep_angle);
                g.DrawPie(pens[i % pens.Length], rect, start_angle, sweep_angle);
                start_angle += sweep_angle;
            }
        }
        //Pie Chart 3 SP

        //Pie Chart 4 ST
        private void button23_Click(object sender, EventArgs e)
        {
            //Pie Chart 4

            // Draw pie slices.

            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(BackColor);

            g.SmoothingMode = SmoothingMode.AntiAlias;

            const int margin = 10;
            const int width = 100;
            Pen outline_pen = Pens.Red;
            Brush fill_brush = Brushes.LightGreen;

            using (Pen ellipse_pen = new Pen(Color.Blue))
            {
                ellipse_pen.DashPattern = new float[] { 5, 5 };

                // Northeast wedge.
                Rectangle rect = new Rectangle(margin + 30, 10, width, width);
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 300, 30);
                g.DrawPie(outline_pen, rect, 300, 30);

                // Everything else.
                rect.X += width + margin;
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 300, -330);
                g.DrawPie(outline_pen, rect, 300, -330);

                // East wedge.
                rect.Y += width + margin;
                rect.X = margin + 30;
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 315, 90);
                g.DrawPie(outline_pen, rect, 315, 90);

                // Everything else.
                rect.X += width + margin;
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 315, -270);
                g.DrawPie(outline_pen, rect, 315, -270);

                // Northwest quadrant.
                rect.Y += width + margin;
                rect.X = margin + 30;
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 180, 90);
                g.DrawPie(outline_pen, rect, 180, 90);

                // Everything else.
                rect.X += width + margin;
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 180, -270);
                g.DrawPie(outline_pen, rect, 180, -270);
            }
        }
        //Pie Chart 4 SP

        //Pie Chart 5 ST
        private void button24_Click(object sender, EventArgs e)
        {
            //Pie Chart 5
            Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            draw_hall_map();
        }

        private void draw_hall_map()
        {
            Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(100, 100, 300, 300));
            g.FillEllipse(new SolidBrush(Color.Lime), new Rectangle(90, 90, 320, 320));
            g.FillPie(new SolidBrush(Color.Red), new Rectangle(100, 100, 300, 300), 0, 60);
            g.FillPie(new SolidBrush(Color.Green), new Rectangle(100, 100, 300, 300), 60, 60);
            g.FillPie(new SolidBrush(Color.Blue), new Rectangle(100, 100, 300, 300), 120, 60);
            g.FillPie(new SolidBrush(Color.Yellow), new Rectangle(100, 100, 300, 300), 180, 60);
            g.FillPie(new SolidBrush(Color.Lime), new Rectangle(100, 100, 300, 300), 240, 60);
            g.FillPie(new SolidBrush(Color.Navy), new Rectangle(100, 100, 300, 300), 300, 60);
            pictureBox1.Refresh();
        }
        //Pie Chart 5 SP

        private void button25_Click(object sender, EventArgs e)
        {
            //餅圖

            int x_st = 10;
            int y_st = 10;
            int W = 300;
            int H = 180;

            Rectangle outline = new Rectangle(x_st, y_st, W, H);

            // 外框
            g.DrawEllipse(new Pen(Color.Black, 8.0f), outline);
            // 第1片
            g.FillPie(new SolidBrush(Color.Red), outline, -20f, 120f);
            // 第2片
            g.FillPie(new SolidBrush(Color.Green), outline, 100f, 120f);
            // 第3片
            g.FillPie(new SolidBrush(Color.Blue), outline, 220f, 100f);
            // 第4片
            g.FillPie(new SolidBrush(Color.Yellow), outline, 320f, 40f);

            pictureBox1.Image = bitmap1;
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //畫餅圖
            string[] sitem = { "很好", "好", "一般", "差" };
            int[] num = { 1000, 69, 90, 20 };
            int cnt = 0;
            int i = 0;
            int len = num.Length;
            float s = 0;
            float[] nflt;
            string header = "";

            //nflt.Length = len;
            nflt = new float[len];
            for (i = 0; i < len; i++)
            {
                cnt += num[i];
            }
            //flt = cnt /len;
            for (i = 0; i < len; i++)
            {
                nflt[i] = 360 * num[i] / cnt;
            }

            header = "調查統計結果一覽圖";
            g.DrawString(header, new Font("宋體", 12, FontStyle.Bold), Brushes.Black, new Point(75, 10));
            g.DrawString("單位：次", new Font("宋體", 9), Brushes.Black, new Point(300, 25));

            Point myRec = new Point(300, 40);
            Point myDec = new Point(320, 40);

            for (i = 0; i < len; i++)
            {
                if (i == len - 1)
                {
                    //s = 360-s;
                    nflt[i] = 360 - s;
                }

                g.DrawRectangle(Pens.Black, myRec.X, myRec.Y, 20, 10);
                //繪製小方塊
                g.FillRectangle(new SolidBrush(Return_Color(i)), myRec.X, myRec.Y, 20, 10);
                //填充小方塊
                g.DrawString(" " + sitem[i] + " " + num[i], new Font("宋體", 9), Brushes.Black, myDec);
                //繪製小方塊右邊的文字
                myRec.Y += 15;
                myDec.Y += 15;

                g.FillPie(new SolidBrush(Return_Color(i)), 50, 50, 200, 200, s, nflt[i]);
                g.DrawPie(Pens.Black, 50, 50, 200, 200, s, nflt[i]);
                s = s + nflt[i];
            }
            Pen p = new Pen(Color.Black, 1);
            g.DrawRectangle(p, 1, 1, 398, 298);
            pictureBox1.Image = bitmap1;
        }

        public Color Return_Color(int i)
        {
            switch (i)
            {
                case 0:
                    return Color.Red;
                //break;
                case 1:
                    return Color.Blue;
                //break;
                case 2:
                    return Color.Yellow;
                case 3:
                    return Color.Green;
                //break;
                case 4:
                    return Color.Pink;
                //break;
                case 5:
                    return Color.Plum;
                //break;
                case 6:
                    return Color.Gray;
                //break;
                case 7:
                    return Color.Salmon;
                //break;
                case 8:
                    return Color.RosyBrown;
                //break;
                case 9:
                    return Color.Teal;
                //break;
                case 10:
                    return Color.Orange;
                //break;
                case 11:
                    return Color.Thistle;
                //break;
                case 12:
                    return Color.Maroon;
                //break;
                default:
                    return Color.WhiteSmoke;
                //break;
            }
        }

        //在餅型圖的外圍顯示說明文字 ST

        public static string[] XText = new string[7] { "商品1", "商品2", "商品3", "商品4", "商品5", "商品6", "商品7" };//儲存數據的名稱數組
        public static float[] SzData = new float[7] { 5F, 17F, 7F, 2F, 10F, 5F, 4F };//取得每列的和
        public static Color[] WearColor = new Color[] { Color.Red,Color.Gold,Color.Chartreuse,Color.Teal,Color.RoyalBlue,Color.Fuchsia,Color.Firebrick,
            Color.Goldenrod,Color.ForestGreen,Color.Aqua,Color.Blue,Color.PaleVioletRed,Color.Salmon,Color.Yellow,Color.LimeGreen,Color.LightBlue,Color.LightSteelBlue,Color.MediumPurple};
        public static string[] AreaText;//臨時儲存數據的名稱數組
        Pen mypen;
        float AreaAngle = 0F;
        public static float XSize = 50;//X軸的大小
        public static float YSize = 50;//Y軸的大小
        public static float ASum = 50;//記錄餅形的總和
        public static float TemXSize = 0;//X軸的臨時大小
        public static float XLeft = 0;//X軸的左端點
        public static float XRight = 0;//X軸的右端點
        public static float YUp = 0;//Y軸的上端點
        public static float YDown = 50;//Y軸的下端點
        public static SolidBrush mybrush = new SolidBrush(Color.Red);
        public static float Aline = 20;//標識文字的前端線長
        public static float Asash = 3;//標識文字名邊框的寬度
        public static float temXLeft = 0;//X軸的左端點初始化

        #region 繪製餅形圖(Area)
        public static float AreaXMaxWidth = 0;//取得字串的寬度
        public static float AreaXMaxHeight = 0;//取得字串的高度
        //取得餅形圖的標識文字
        public void AreaValue()
        {
            string temTextSize = "";//儲存最長的名稱
            Font LSfont = new System.Drawing.Font("細明體", 8);//設定說明文字的字體
            AreaText = new string[XText.Length];//實例化一個臨時數組
            for (int i = 0; i < AreaText.Length; i++)//取得名稱
            {
                AreaText[i] = XText[i];
            }
            float AresF = 0;//記錄百分比
            for (int i = 0; i < AreaText.Length; i++)//透過名稱及百分比,組合說明文字
            {
                AresF = (SzData[i] / ASum) * 100;//取得目前記錄的百分比
                AresF = (float)Math.Round(AresF, 3);//對百分比進行四捨五入
                AreaText[i] = AreaText[i] + " " + AresF.ToString() + "%";//組合說明文字
                if (AreaText[i].Length > temTextSize.Length)//取得最長的說明文件
                    temTextSize = AreaText[i];
            }
            Graphics TitG = this.CreateGraphics();//建立Graphics類對像
            SizeF XMaxSize = TitG.MeasureString(temTextSize + Asash * 2, LSfont);//將繪製的字串進行格式化
            AreaXMaxWidth = XMaxSize.Width;//取得字串的寬度
            AreaXMaxHeight = XMaxSize.Height;//取得字串的高度
        }

        //繪製餅形圖表
        public void ProtractArea(Graphics g, PictureBox pbx)
        {
            AreaValue();//計算最長說明文字的大小
            //初始化變數
            mypen = new Pen(Color.Black, 1);//設定畫筆的顏色及大小
            float f = 0;//記錄百分比
            float TimeNum = 0;//扇形的繪製度數
            float AXLeft = 0;//設定餅形圖的X座標
            float AYUp = 0;//設定餅形圖的Y座標
            float AXSize = 0;//設定餅形圖的寬度
            float AYSize = 0;//設定餅形圖的高度
            float Atop = 0;//記錄餅形的高度為長和寬的最小值
            float Aleft = 0;//記錄餅形的高度為長和寬的最小值
            TimeNum = AreaAngle;//設定餅形圖的起始度數
            //計算餅形圖的初始位置
            XLeft = pbx.Width - (pbx.Width - 5);//去了邊框後餅形圖的X位置
            XSize = pbx.Width - 10;//設定餅形圖的寬度
            temXLeft = AXLeft;//記錄餅形圖的X座標
            AXLeft = XLeft;//記錄餅形圖的X座標
            AXSize = XSize;//記錄餅形圖的寬度

            //透過說明文字的大小計算餅形圖的位置
            AXLeft = AXLeft + AreaXMaxWidth + Aline;//設定去除說明文字後的餅形圖X座標
            AYUp = AYUp + AreaXMaxHeight;//設定去除說明文字後的餅形圖Y座標
            AXSize = XSize - AreaXMaxWidth * 2 - Aline * 2;//設定去除說明文字後的餅形圖寬度
            AYSize = YSize - AreaXMaxHeight * 2;//設定去除說明文字後的餅形圖高度
            if (AXSize >= AYSize)//如果餅形圖的寬度大於等於高度
            {
                Aleft = AXSize - AYSize;//記錄餅形圖的X座標
                AXSize = AYSize;//將高度設為寬度
            }
            else
            {
                Atop = AYSize - AXSize;//記錄餅形圖的Y座標
                AYSize = AXSize;//將寬度設為高度
            }
            if (Aleft != 0)//如果寬大於高
            {
                AXLeft = AXLeft + Aleft / 2;//設定餅形圖橫向局中
            }
            if (Atop != 0)//如果高大於寬
            {
                AYUp = AYUp + Atop / 2;//設定餅形圖縱向局中
            }
            temXLeft = XLeft;
            //繪製餅形圖
            if (AXSize > 0 && AYSize > 0)//如果餅形圖的寬和高大於0
            {
                for (int i = 0; i < SzData.Length; i++)//搜尋數據
                {
                    f = SzData[i] / ASum;//取得目前數據的百分比
                    //設定目前扇形圖的填充顏色
                    if (i >= WearColor.Length)//如果沒有超出顏色數組
                        mybrush = new SolidBrush(WearColor[i - WearColor.Length]);
                    else
                        mybrush = new SolidBrush(WearColor[i]);
                    g.FillPie(mybrush, AXLeft, AYUp, AXSize, AYSize, TimeNum, f * 360);//繪製扇形圖
                    TimeNum += f * 360;//設定下一個扇形圖的度數
                }
                ProAreaSign(g, pbx);//繪製餅形圖的說明文字
            }
            else
                return;
        }
        #endregion

        #region 繪製餅形圖標識(Area)
        public void ProAreaSign(Graphics g, PictureBox pbx)
        {
            AreaValue();//儲存最長的名稱
            mypen = new Pen(Color.Black, 1);//設定畫筆的顏色及大小
            Font LSfont = new System.Drawing.Font("細明體", 8);//設定說明文字的字體樣式
            SolidBrush Zbrush = new SolidBrush(Color.Black);//設定存放說明文字邊框的畫刷
            SolidBrush ATbrush = new SolidBrush(Color.Khaki);//設定存放說明文字方塊的背景畫刷
            //初始化變數
            float f = 0;//記錄百分比
            float TimeNum = 0;//扇形的繪製度數
            float AXLeft = 0;//設定餅形圖的X座標
            float AYUp = 0;//設定餅形圖的Y座標
            float AXSize = 0;//設定餅形圖的寬度
            float AYSize = 0;//設定餅形圖的高度
            float Atop = 0;//記錄餅形的高度為長和寬的最小值
            float Aleft = 0;//記錄餅形的高度為長和寬的最小值
            Graphics TitG = pbx.CreateGraphics();//建立Graphics類對像
            SizeF XMaxSize = TitG.MeasureString("", LSfont);//將繪製的字串進行格式化
            float SWidth = 0;//取得字串的寬度
            float SHeight = 0;//取得字串的高度
            //計算餅形圖的初始位置
            XLeft = pbx.Width - (pbx.Width - 5);//去了邊框後餅形圖的X位置
            XSize = pbx.Width - 10;//設定餅形圖的寬度
            temXLeft = AXLeft;//記錄餅形圖的X座標
            AXLeft = XLeft;//記錄餅形圖的X座標
            AXSize = XSize;//記錄餅形圖的寬度
            //透過說明文字的大小計算餅形圖的位置
            AXLeft = AXLeft + AreaXMaxWidth + Aline;//設定去除說明文字後的餅形圖X座標
            AYUp = AYUp + AreaXMaxHeight;//設定去除說明文字後的餅形圖Y座標
            AXSize = XSize - AreaXMaxWidth * 2 - Aline * 2;//設定去除說明文字後的餅形圖寬度
            AYSize = YSize - AreaXMaxHeight * 2;//設定去除說明文字後的餅形圖高度
            if (AXSize >= AYSize)//如果餅形圖的寬度大於等於高度
            {
                Aleft = AXSize - AYSize;//記錄餅形圖的X座標
                AXSize = AYSize;//將高度設為寬度
            }
            else
            {
                Atop = AYSize - AXSize;//記錄餅形圖的Y座標
                AYSize = AXSize;//將寬度設為高度
            }
            if (Aleft != 0)//如果寬大於高
            {
                AXLeft = AXLeft + Aleft / 2;//設定餅形圖橫向局中
            }
            if (Atop != 0)//如果高大於寬
            {
                AYUp = AYUp + Atop / 2;//設定餅形圖縱向局中
            }
            temXLeft = XLeft;
            //初始化說明文字前橫線的變數
            float X1 = 0;
            float Y1 = 0;
            float X2 = 0;
            float Y2 = 0;
            //初始化說明文字位置的變數
            float TX1 = 0;
            float TY1 = 0;
            float TX2 = 0;
            float TY2 = 0;
            float temf = 0;//記錄百分比
            double radians = 0;//記錄扇形的角度
            temf = (this.AreaAngle * (ASum / 360) / ASum);//記錄起始位置的度數
            TimeNum = this.AreaAngle;//記錄扇形的起始角度
            //繪製說明文字
            if (AXSize > 0 && AYSize > 0)
            {
                for (int i = 0; i < SzData.Length; i++)//搜尋所有說明文字
                {
                    f = SzData[i] / ASum;//取得目前記錄的百分比
                    if (f == 0)//如果目前值為0
                        continue;//執行下一次循環
                    radians = ((double)((temf + f / 2) * 360) * Math.PI) / (double)180;
                    X1 = Convert.ToSingle(AXLeft + (AXSize / 2.0 + (int)((float)(AXSize / 2.0) * Math.Cos(radians))));
                    Y1 = Convert.ToSingle(AYUp + (AYSize / 2.0 + (int)((float)(AYSize / 2.0) * Math.Sin(radians))));

                    XMaxSize = TitG.MeasureString(AreaText[i].Trim(), LSfont);//將繪製的字串進行格式化
                    SWidth = XMaxSize.Width;//取得字串的寬度
                    SHeight = XMaxSize.Height;//取得字串的高度
                    if ((temf + f / 2) * 360 > 90 && (temf + f / 2) * 360 <= 270)
                    {
                        X2 = X1 - Aline;

                        TX1 = X2 - 1 - SWidth;
                        TY1 = Y1 - SHeight / 2 - Asash;
                        TX2 = SWidth;
                        TY2 = SHeight + Asash * 2;
                        g.FillRectangle(ATbrush, TX1, TY1, TX2, TY2);//繪製內矩形
                        g.DrawRectangle(new Pen(Color.Black, 1), TX1, TY1, TX2, TY2);//繪製矩形
                        g.DrawString(AreaText[i].Trim(), LSfont, Zbrush, new PointF(X2 - SWidth + Asash - 1, Y1 - SHeight / 2));
                    }
                    else
                    {
                        X2 = X1 + Aline;

                        TX1 = X2 + 1;
                        TY1 = Y1 - SHeight / 2 - Asash;
                        TX2 = SWidth;
                        TY2 = SHeight + Asash * 2;
                        g.FillRectangle(ATbrush, TX1, TY1, TX2, TY2);//繪製內矩形
                        g.DrawRectangle(new Pen(Color.Black, 1), TX1, TY1, TX2, TY2);//繪製矩形
                        g.DrawString(AreaText[i].Trim(), LSfont, Zbrush, new PointF(X2 + Asash + 1, Y1 - SHeight / 2));
                    }
                    Y2 = Y1;
                    g.DrawLine(new Pen(new SolidBrush(Color.Black), 1), X1, Y1, X2, Y2);
                    TimeNum += f * 360;
                    temf = temf + f;
                }
            }
            else
                return;
        }
        #endregion

        private void button27_Click(object sender, EventArgs e)
        {
            //在餅型圖的外圍顯示說明文字
            XSize = pictureBox1.Width;//X軸的大小
            YSize = pictureBox1.Height;//Y軸的大小
            YDown = pictureBox1.Height;//Y軸的下端點
            ProtractArea(pictureBox1.CreateGraphics(), pictureBox1);
        }
        //在餅型圖的外圍顯示說明文字SP

        private void button28_Click(object sender, EventArgs e)
        {
            //畫柱狀圖
            g.Clear(Color.White);

            Font f = new Font("宋體", 24, FontStyle.Regular);
            Pen p = new Pen(Color.Blue);
            g.DrawString("報名及考試統計柱狀圖", f, p.Brush, 200, 20);

            //畫表格
            for (int i = 0; i <= 9; i++)
            {
                g.DrawLine(p, 30, 90 + 31 * i, 620, 90 + 31 * i);
            }
            for (int i = 1; i <= 14; i++)
            {
                g.DrawLine(p, 30 + 42 * i, 60, 30 + 42 * i, 370);
            }

            Pen MyPen = new Pen(Color.Blue, 2);
            Point p1 = new Point(30, 60);
            Point p2 = new Point(30, 370);
            Point p3 = new Point(30, 370);
            Point p4 = new Point(620, 370);
            g.DrawLine(MyPen, p1, p2);
            g.DrawLine(MyPen, p3, p4);

            //紅色圖形部分
            Pen drawPen = new Pen(Color.Red, 1);
            SolidBrush mybrush = new SolidBrush(Color.Red);

            g.DrawRectangle(drawPen, 30 + 21, 370 - 41, 21, 41);
            g.FillRectangle(mybrush, 30 + 21, 370 - 41, 21, 41);

            g.DrawRectangle(drawPen, 30 + 42 * 2 + 21, 370 - 31 * 4 - 10, 21, 31 * 4 + 10);
            g.FillRectangle(mybrush, 30 + 42 * 2 + 21, 370 - 31 * 4 - 10, 21, 31 * 4 + 10);

            g.DrawRectangle(drawPen, 30 + 42 * 4 + 21, 370 - 31 * 2 - 20, 21, 31 * 2 + 20);
            g.FillRectangle(mybrush, 30 + 42 * 4 + 21, 370 - 31 * 2 - 20, 21, 31 * 2 + 20);

            g.DrawRectangle(drawPen, 30 + 42 * 6 + 21, 370 - 31 * 1 - 20, 21, 31 * 1 + 20);
            g.FillRectangle(mybrush, 30 + 42 * 6 + 21, 370 - 31 * 1 - 20, 21, 31 * 1 + 20);

            g.DrawRectangle(drawPen, 30 + 42 * 8 + 21, 370 - 31 * 5 - 25, 21, 31 * 5 + 25);
            g.FillRectangle(mybrush, 30 + 42 * 8 + 21, 370 - 31 * 5 - 25, 21, 31 * 5 + 25);

            g.DrawRectangle(drawPen, 30 + 42 * 10 + 21, 370 - 31 * 4 - 7, 21, 31 * 4 + 7);
            g.FillRectangle(mybrush, 30 + 42 * 10 + 21, 370 - 31 * 4 - 7, 21, 31 * 4 + 7);

            g.DrawRectangle(drawPen, 30 + 42 * 12 + 21, 60, 21, 370 - 60);
            g.FillRectangle(mybrush, 30 + 42 * 12 + 21, 60, 21, 370 - 60);

            //綠色圖形部分
            Pen drawPen2 = new Pen(Color.Green, 1);
            SolidBrush brush = new SolidBrush(Color.Green);
            g.DrawRectangle(drawPen2, 30 + 42, 370 - 31, 21, 31);
            g.FillRectangle(brush, 30 + 42, 370 - 31, 21, 31);

            g.DrawRectangle(drawPen2, 30 + 42 * 3, 370 - 31 * 2 - 15, 21, 31 * 2 + 15);
            g.FillRectangle(brush, 30 + 42 * 3, 370 - 31 * 2 - 15, 21, 31 * 2 + 15);

            g.DrawRectangle(drawPen2, 30 + 42 * 5, 370 - 31 - 10, 21, 41);
            g.FillRectangle(brush, 30 + 42 * 5, 370 - 31 - 10, 21, 41);

            g.DrawRectangle(drawPen2, 30 + 42 * 7, 370 - 16, 21, 16);
            g.FillRectangle(brush, 30 + 42 * 7, 370 - 16, 21, 16);

            g.DrawRectangle(drawPen2, 30 + 42 * 9, 370 - 31 * 3 - 20, 21, 31 * 3 + 20);
            g.FillRectangle(brush, 30 + 42 * 9, 370 - 31 * 3 - 20, 21, 31 * 3 + 20);

            g.DrawRectangle(drawPen2, 30 + 42 * 11, 370 - 31 * 1 - 28, 21, 31 * 1 + 28);
            g.FillRectangle(brush, 30 + 42 * 11, 370 - 31 * 1 - 28, 21, 31 * 1 + 28);

            g.DrawRectangle(drawPen2, 30 + 42 * 13, 370 - 31 * 5 - 15, 21, 31 * 5 + 15);
            g.FillRectangle(brush, 30 + 42 * 13, 370 - 31 * 5 - 15, 21, 31 * 5 + 15);

            //圖上的文字部分
            Font font2 = new Font("宋體", 10, FontStyle.Regular);
            g.DrawString("第一期", font2, p.Brush, 30 + 21, 375);
            g.DrawString("第二期", font2, p.Brush, 30 + 42 * 2 + 21, 375);
            g.DrawString("第三期", font2, p.Brush, 30 + 42 * 4 + 21, 375);
            g.DrawString("第四期", font2, p.Brush, 30 + 42 * 6 + 21, 375);
            g.DrawString("上半年", font2, p.Brush, 30 + 42 * 8 + 21, 375);
            g.DrawString("下半年", font2, p.Brush, 30 + 42 * 10 + 21, 375);
            g.DrawString("全年統計", font2, p.Brush, 30 + 42 * 12 + 21, 375);

            //圖上數位部分
            g.DrawString("25", font2, p.Brush, 10, 370 - 35);
            g.DrawString("50", font2, p.Brush, 10, 370 - 35 * 2);
            g.DrawString("75", font2, p.Brush, 10, 370 - 34 * 3);
            g.DrawString("100", font2, p.Brush, 5, 370 - 33 * 4);
            g.DrawString("125", font2, p.Brush, 5, 370 - 33 * 5);
            g.DrawString("150", font2, p.Brush, 5, 370 - 32 * 6);
            g.DrawString("175", font2, p.Brush, 5, 370 - 32 * 7);
            g.DrawString("200", font2, p.Brush, 5, 370 - 32 * 8);
            g.DrawString("225", font2, p.Brush, 5, 370 - 32 * 9);
            g.DrawString("250", font2, p.Brush, 5, 370 - 32 * 10);

            //紅色數
            Pen pen2 = new Pen(Color.Red);
            g.DrawString("39", font2, pen2.Brush, 30 + 21, 370 - 41 - 15);
            g.DrawString("111", font2, pen2.Brush, 30 + 42 * 2 + 21, 370 - 31 * 4 - 10 - 15);
            g.DrawString("71", font2, pen2.Brush, 30 + 42 * 4 + 21, 370 - 31 * 2 - 20 - 15);
            g.DrawString("40", font2, pen2.Brush, 30 + 42 * 6 + 21, 370 - 31 * 1 - 20 - 15);
            g.DrawString("150", font2, pen2.Brush, 30 + 42 * 8 + 21, 370 - 31 * 5 - 25 - 15);
            g.DrawString("111", font2, pen2.Brush, 30 + 42 * 10 + 21, 370 - 31 * 4 - 7 - 15);
            g.DrawString("261", font2, pen2.Brush, 30 + 42 * 12 + 21, 60 - 15);

            //綠色數
            Pen pen3 = new Pen(Color.Green);
            g.DrawString("39", font2, pen2.Brush, 30 + 21, 370 - 41 - 15);
            g.DrawString("111", font2, pen2.Brush, 30 + 42 * 2 + 21, 370 - 31 * 4 - 10 - 15);
            g.DrawString("71", font2, pen2.Brush, 30 + 42 * 4 + 21, 370 - 31 * 2 - 20 - 15);
            g.DrawString("40", font2, pen2.Brush, 30 + 42 * 6 + 21, 370 - 31 * 1 - 20 - 15);
            g.DrawString("150", font2, pen2.Brush, 30 + 42 * 8 + 21, 370 - 31 * 5 - 25 - 15);
            g.DrawString("111", font2, pen2.Brush, 30 + 42 * 10 + 21, 370 - 31 * 4 - 7 - 15);
            g.DrawString("261", font2, pen2.Brush, 30 + 42 * 12 + 21, 60 - 15);

            //最下面的矩形框
            g.DrawRectangle(p, 30 + 42 * 2 + 30, 400, 42 * 7, 31 * 2);

            g.DrawRectangle(drawPen, 30 + 42 * 5, 410, 21, 10);
            g.FillRectangle(mybrush, 30 + 42 * 5, 410, 21, 10);
            g.DrawString("報名人數", font2, pen2.Brush, 30 + 42 * 6, 410);

            g.DrawRectangle(drawPen2, 30 + 42 * 5, 440, 21, 10);
            g.FillRectangle(brush, 30 + 42 * 5, 440, 21, 10);
            g.DrawString("通過人數", font2, pen3.Brush, 30 + 42 * 6, 440);

            pictureBox1.Image = bitmap1;
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //畫棒圖

            g.Clear(Color.Snow);
            string[] sitem = { "很好", "好", "一般", "差" };
            int[] num = { 1000, 69, 90, 2000 };
            int cnt = 0;
            int i = 0;
            int iBarWidth = 40;
            float scale = 1;
            float[] nflt;
            int len = num.Length;
            //nflt.Length = len;
            nflt = new float[len];
            for (i = 0; i < len; i++)
            {
                cnt += num[i];
            }
            //flt = cnt /len;
            for (i = 0; i < len; i++)
            {
                nflt[i] = 200 * num[i] / cnt;
                //nflt[i] = scale * num[i]/cnt;
            }

            string header = "調查統計結果一覽圖";
            g.DrawString(header, new Font("宋體", 12, FontStyle.Bold), Brushes.Black, new Point(75, 10));
            Point myRec = new Point(300, 40);
            Point myDec = new Point(320, 40);

            for (i = 0; i < len; i++)
            {
                g.DrawRectangle(Pens.Black, myRec.X, myRec.Y, 20, 10);
                //繪製小方塊
                g.FillRectangle(new SolidBrush(Return_Color(i)), myRec.X, myRec.Y, 20, 10);
                //填充小方塊
                g.DrawString(" " + sitem[i], new Font("宋體", 9), Brushes.Black, myDec);
                //繪製小方塊右邊的文字
                myRec.Y += 15;
                myDec.Y += 15;

                g.DrawRectangle(Pens.Black, (i * iBarWidth) + 15, 290 - (nflt[i] * scale), 20, (nflt[i] * scale) + 5);
                //繪製Bar圖
                g.FillRectangle(new SolidBrush(Return_Color(i)), (i * iBarWidth) + 15, 290 - (nflt[i] * scale), 20, (nflt[i] * scale) + 5);
                //以指定的色彩填充Bar圖
                g.DrawString(num[i].ToString(), new Font("宋體", 9), Brushes.Black, (i * iBarWidth) + 20, 275 - (nflt[i] * scale));
                //顯示Bar圖代表的數據

                //s = s + nflt[i];   
            }
            g.DrawRectangle(Pens.Black, 1, 1, 398, 298);

            pictureBox1.Image = bitmap1;
        }

        private void button30_Click(object sender, EventArgs e)
        {
            //折線圖
            //坐標系畫圖

            //數據初始化   
            string[] month = new string[12] { "一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月" };
            float[] d = new float[12] { 20.5F, 60, 10.8F, 15.6F, 30, 70.9F, 50.3F, 30.7F, 70, 50.4F, 30.8F, 20 };

            PointF cPt = new PointF(40, 420);//中心點
            PointF[] xPt = new PointF[3]
            {
                new PointF(cPt.Y + 15, cPt.Y),
                new PointF(cPt.Y, cPt.Y - 8),
                new PointF(cPt.Y, cPt.Y + 8)
            };//X軸三角形
            PointF[] yPt = new PointF[3]
            {
                new PointF(cPt.X, cPt.X - 15),
                new PointF(cPt.X - 8, cPt.X),
                new PointF(cPt.X + 8, cPt.X)
            };//Y軸三角形
            g.DrawString("某工廠某產品月生產量圖表", new Font("宋體", 14), Brushes.Black, new PointF(cPt.X + 60, cPt.X));//圖表標題
            //畫X軸
            g.DrawLine(Pens.Black, cPt.X, cPt.Y, cPt.Y, cPt.Y);
            g.DrawPolygon(Pens.Black, xPt);
            g.FillPolygon(new SolidBrush(Color.Black), xPt);
            g.DrawString("月份", new Font("宋體", 12), Brushes.Black, new PointF(cPt.Y + 10, cPt.Y + 10));
            //畫Y軸
            g.DrawLine(Pens.Black, cPt.X, cPt.Y, cPt.X, cPt.X);
            g.DrawPolygon(Pens.Black, yPt);
            g.FillPolygon(new SolidBrush(Color.Black), yPt);
            g.DrawString("單位(萬)", new Font("宋體", 12), Brushes.Black, new PointF(0, 7));
            for (int i = 1; i <= 12; i++)
            {
                //畫Y軸刻度
                if (i < 11)
                {
                    g.DrawString((i * 10).ToString(), new Font("宋體", 11), Brushes.Black, new PointF(cPt.X - 30, cPt.Y - i * 30 - 6));
                    g.DrawLine(Pens.Black, cPt.X - 3, cPt.Y - i * 30, cPt.X, cPt.Y - i * 30);
                }
                //畫X軸項目
                g.DrawString(month[i - 1].Substring(0, 1), new Font("宋體", 11), Brushes.Black, new PointF(cPt.X + i * 30 - 5, cPt.Y + 5));
                g.DrawString(month[i - 1].Substring(1, 1), new Font("宋體", 11), Brushes.Black, new PointF(cPt.X + i * 30 - 5, cPt.Y + 20));
                if (month[i - 1].Length > 2)
                {
                    g.DrawString(month[i - 1].Substring(2, 1), new Font("宋體", 11), Brushes.Black, new PointF(cPt.X + i * 30 - 5, cPt.Y + 35));
                }
                //畫點
                g.DrawEllipse(Pens.Black, cPt.X + i * 30 - 1.5F, cPt.Y - d[i - 1] * 3 - 1.5F, 3, 3);
                g.FillEllipse(new SolidBrush(Color.Black), cPt.X + i * 30 - 1.5F, cPt.Y - d[i - 1] * 3 - 1.5F, 3, 3);
                //畫數值
                g.DrawString(d[i - 1].ToString(), new Font("宋體", 11), Brushes.Black, new PointF(cPt.X + i * 30, cPt.Y - d[i - 1] * 3));
                //畫折線
                if (i > 1)
                {
                    g.DrawLine(Pens.Red, cPt.X + (i - 1) * 30, cPt.Y - d[i - 2] * 3, cPt.X + i * 30, cPt.Y - d[i - 1] * 3);
                }
            }
            pictureBox1.Image = bitmap1;
        }

        private void button31_Click(object sender, EventArgs e)
        {
            //畫折線圖
            g.Clear(Color.White);

            Font f = new Font("宋體", 24, FontStyle.Regular);
            Pen p = new Pen(Color.Blue);
            g.DrawString("報名及考試統計折線圖", f, p.Brush, 200, 20);

            //畫表格
            for (int i = 0; i <= 9; i++)
            {
                g.DrawLine(p, 30, 90 + 31 * i, 620, 90 + 31 * i);
            }
            for (int i = 1; i <= 7; i++)
            {
                g.DrawLine(p, 30 + 84 * i, 60, 30 + 84 * i, 370);
            }
            Pen MyPen = new Pen(Color.Blue, 2);
            Point p1 = new Point(30, 60);
            Point p2 = new Point(30, 370);
            Point p3 = new Point(30, 370);
            Point p4 = new Point(620, 370);
            g.DrawLine(MyPen, p1, p2);
            g.DrawLine(MyPen, p3, p4);

            //繪製折線
            Pen pen1 = new Pen(Color.Red, 2);
            Pen pen2 = new Pen(Color.Green, 2);

            //紅色折線
            Point a1, a2, a3, a4, a5, a6, a7;
            a1 = new Point(30, 370 - 31 - 20);
            a2 = new Point(30 + 84 * 1, 370 - (31 * 4 + 9));
            a3 = new Point(30 + 84 * 2, 370 - (31 * 2 + 28));
            a4 = new Point(30 + 84 * 3, 370 - (31 * 1 + 20));
            a5 = new Point(30 + 84 * 4, 370 - (31 * 5 + 21));
            a6 = new Point(30 + 84 * 5, 370 - (31 * 4 + 10));
            a7 = new Point(30 + 84 * 6, 60);
            Point[] points = { a1, a2, a3, a4, a5, a6, a7 };
            g.DrawLines(pen1, points);

            //綠色折線
            Point b1, b2, b3, b4, b5, b6, b7;
            b1 = new Point(30, 370 - (31 * 1 + 1));
            b2 = new Point(30 + 84 * 1, 370 - (31 * 2 + 15));
            b3 = new Point(30 + 84 * 2, 370 - (31 * 1 + 10));
            b4 = new Point(30 + 84 * 3, 370 - (31 * 0 + 15));
            b5 = new Point(30 + 84 * 4, 370 - (31 * 3 + 15));
            b6 = new Point(30 + 84 * 5, 370 - (31 * 1 + 29));
            b7 = new Point(30 + 84 * 6, 370 - (31 * 5 + 14));
            Point[] points2 = { b1, b2, b3, b4, b5, b6, b7 };
            g.DrawLines(pen2, points2);

            //圖上數位部分
            Font font2 = new Font("宋體", 10, FontStyle.Regular);
            g.DrawString("25", font2, pen1.Brush, 10, 370 - 35);
            g.DrawString("50", font2, pen1.Brush, 10, 370 - 35 * 2);
            g.DrawString("75", font2, pen1.Brush, 10, 370 - 34 * 3);
            g.DrawString("100", font2, pen1.Brush, 5, 370 - 33 * 4);
            g.DrawString("125", font2, pen1.Brush, 5, 370 - 33 * 5);
            g.DrawString("150", font2, pen1.Brush, 5, 370 - 32 * 6);
            g.DrawString("175", font2, pen1.Brush, 5, 370 - 32 * 7);
            g.DrawString("200", font2, pen1.Brush, 5, 370 - 32 * 8);
            g.DrawString("225", font2, pen1.Brush, 5, 370 - 32 * 9);
            g.DrawString("250", font2, pen1.Brush, 5, 370 - 32 * 10);

            //文字
            g.DrawString("第一期", font2, pen1.Brush, 15, 375);
            g.DrawString("第二期", font2, pen1.Brush, 15 + 84 * 1, 375);
            g.DrawString("第三期", font2, pen1.Brush, 15 + 84 * 2, 375);
            g.DrawString("第四期", font2, pen1.Brush, 15 + 84 * 3, 375);
            g.DrawString("上半年", font2, pen1.Brush, 15 + 84 * 4, 375);
            g.DrawString("下半年", font2, pen1.Brush, 15 + 84 * 5, 375);
            g.DrawString("全年統計", font2, pen1.Brush, 15 + 84 * 6, 375);

            //折線圖上的數位
            g.DrawString("39", font2, pen1.Brush, 30, 370 - 31 - 20 - 15);
            g.DrawString("111", font2, pen1.Brush, 30 + 84 * 1, 370 - (31 * 4 + 9) - 15);
            g.DrawString("71", font2, pen1.Brush, 30 + 84 * 2, 370 - (31 * 2 + 28) - 15);
            g.DrawString("40", font2, pen1.Brush, 30 + 84 * 3, 370 - (31 * 1 + 20) - 15);
            g.DrawString("150", font2, pen1.Brush, 30 + 84 * 4, 370 - (31 * 5 + 21) - 15);
            g.DrawString("111", font2, pen1.Brush, 30 + 84 * 5, 370 - (31 * 4 + 10) - 15);
            g.DrawString("261", font2, pen1.Brush, 30 + 84 * 6, 60 - 15);

            g.DrawString("26", font2, pen2.Brush, 30, 370 - (31 * 1 + 1) - 15);
            g.DrawString("68", font2, pen2.Brush, 30 + 84 * 1, 370 - (31 * 2 + 15) - 15);
            g.DrawString("35", font2, pen2.Brush, 30 + 84 * 2, 370 - (31 * 1 + 10) - 15);
            g.DrawString("14", font2, pen2.Brush, 30 + 84 * 3, 370 - (31 * 0 + 15) - 15);
            g.DrawString("94", font2, pen2.Brush, 30 + 84 * 4, 370 - (31 * 3 + 15) - 15);
            g.DrawString("49", font2, pen2.Brush, 30 + 84 * 5, 370 - (31 * 1 + 29) - 15);
            g.DrawString("143", font2, pen2.Brush, 30 + 84 * 6, 370 - (31 * 5 + 14) - 15);

            //最下面的矩形框

            SolidBrush mybrush = new SolidBrush(Color.Red);
            SolidBrush brush = new SolidBrush(Color.Green);

            g.DrawRectangle(pen1, 30 + 42 * 2 + 30, 400, 42 * 7, 31 * 2);

            g.DrawRectangle(pen1, 30 + 42 * 5, 410, 21, 10);
            g.FillRectangle(mybrush, 30 + 42 * 5, 410, 21, 10);
            g.DrawString("報名人數", font2, pen1.Brush, 30 + 42 * 6, 410);

            g.DrawRectangle(pen2, 30 + 42 * 5, 440, 21, 10);
            g.FillRectangle(brush, 30 + 42 * 5, 440, 21, 10);
            g.DrawString("通過人數", font2, pen2.Brush, 30 + 42 * 6, 440);

            pictureBox1.Image = bitmap1;
        }

        private void button32_Click(object sender, EventArgs e)
        {
            //折線圖
            //測試數據
            DataTable table = new DataTable("Data");
            DataRow Dr;
            DataColumn Dc = new DataColumn("ID", Type.GetType("System.Int32"));
            DataColumn Dc2 = new DataColumn("Num", Type.GetType("System.Int32"));
            DataColumn Dc3 = new DataColumn("name", Type.GetType("System.String"));
            table.Columns.Add(Dc);
            table.Columns.Add(Dc2);
            table.Columns.Add(Dc3);
            Random rnd = new Random();
            for (int n = 0; n < 61; n++)
            {
                Dr = table.NewRow();
                Dr[0] = n;
                Dr[1] = rnd.Next(10, 140);
                Dr[2] = n.ToString();
                table.Rows.Add(Dr);
            }
            //畫圖參數
            int BG_Width = 450;
            int BG_Height = 180;
            //int Pic_Width = 450;
            //int Pic_Height = 180;
            int pic_X = 6;
            int pic_H = 1;
            int pic_tr = 5;
            int pic_td = 12;
            Rectangle rec = new Rectangle(50, 15, 360, 150);
            Pen Pic_Bolder = new Pen(Color.Black, 1);
            Pen Pic_line = new Pen(Color.Gray, 1);
            Pen Pic_Data = new Pen(Color.Red, 2);
            SolidBrush brusth = new SolidBrush(Color.Blue);
            Point[] DataPt = new Point[table.Rows.Count];
            int x;
            int y;
            for (int n = 0; n < table.Rows.Count; n++)
            {
                Dr = table.Rows[n];
                x = (int)Dr[0] * pic_X + rec.X;
                y = (int)Dr[1] * pic_H + rec.Y;
                DataPt[n] = new Point(x, y);
            }
            Bitmap Bg = new Bitmap(BG_Width, BG_Height, PixelFormat.Format24bppRgb);
            Graphics Ph = Graphics.FromImage(Bg);
            Ph.Clear(Color.White);
            Ph.DrawRectangle(Pic_Bolder, rec);
            //畫折線
            Ph.DrawCurve(Pic_Data, DataPt);
            //rec.
            Point SPoint = new Point();
            Point Epoint = new Point();
            //畫橫線
            for (int n = 1; n < pic_tr; n++)
            {
                //cell[0] = new Point(rec.X);
                SPoint.X = 0 + rec.X;
                SPoint.Y = n * 30 + rec.Y;
                Epoint.X = rec.Width + rec.X;
                Epoint.Y = n * 30 + rec.Y;
                Ph.DrawLine(Pic_line, SPoint, Epoint);
            }
            //畫豎線
            for (int n = 1; n < pic_td; n++)
            {
                SPoint.X = n * 30 + rec.X;
                SPoint.Y = rec.Y;
                Epoint.X = n * 30 + rec.X;
                Epoint.Y = rec.Height + rec.Y;
                Ph.DrawLine(Pic_line, SPoint, Epoint);
            }
            //畫標題
            string Title = "畫折線測試";
            SolidBrush brush = new SolidBrush(Color.RoyalBlue);
            Ph.DrawString(Title, new Font("Franklin Gothic Demi", 12, FontStyle.Italic), brush, new Point(200, 0));
            Ph.Save();
            pictureBox1.Image = Bg;
        }

        private void button33_Click(object sender, EventArgs e)
        {
            //畫曲線圖

            Curve2D cuv2D = new Curve2D();

            cuv2D.Fit();
            Bitmap bitmap1 = cuv2D.CreateImage();
            pictureBox1.Image = bitmap1;
        }

        private void button34_Click(object sender, EventArgs e)
        {
            // 在此處放置用戶代碼以初始化頁面
            Graphics g;//建立畫板對象
            Bitmap objBitMap = new Bitmap(600, 300);//建立位圖對象
            g = Graphics.FromImage(objBitMap);//根據位圖對象建立畫板對象
            g.Clear(Color.Gray);//設置畫板對象的背景色
            int[] arrValues = { 0, 0, 0, 0, 0, 0 };//數據數組
            arrValues[0] = 100;
            arrValues[1] = 60;
            arrValues[2] = 50;
            arrValues[3] = 40;
            arrValues[4] = 50;
            arrValues[5] = 220;
            string[] arrValueNames = { "0", "0", "0", "0", "0", "0" };//月份
            arrValueNames[0] = "一月";
            arrValueNames[1] = "二月";
            arrValueNames[2] = "三月";
            arrValueNames[3] = "四月";
            arrValueNames[4] = "五月";
            arrValueNames[5] = "六月";

            g.DrawString("上半年銷售情況統計", new Font("宋體", 16), Brushes.Black, new PointF(0, 0));

            //創建圖例文字
            PointF symbolLeg = new PointF(335, 20);
            PointF descLeg = new PointF(360, 18);

            //畫出圖例。利用g圖形對象的3個方法畫出圖例：
            //FillRectangle()方法畫出填充矩形，DrawRectangle()方法畫出矩形的邊框
            //DrawString()方法畫出說明文字。這3個圖像對象的方法在.NET框架類庫中均已重載
            //可以很方便根據不同的參數來畫出圖形
            //畫出各個月的標示圖形
            for (int i = 0; i < arrValueNames.Length; i++)
            {
                g.FillRectangle(new SolidBrush(GetColor(i)), symbolLeg.X, symbolLeg.Y, 20, 10);

                g.DrawRectangle(Pens.Black, symbolLeg.X, symbolLeg.Y, 20, 10);

                g.DrawString(arrValueNames[i].ToString(), new Font("宋體", 10), Brushes.Black, descLeg);

                symbolLeg.Y += 15;
                descLeg.Y += 15;
            }
            //畫矩形圖
            for (int j = 0; j < arrValues.Length; j++)
            {
                g.FillRectangle(new SolidBrush(GetColor(j)), (j * 35) + 15, 200 - arrValues[j], 20, arrValues[j]);
                g.DrawRectangle(Pens.Black, (j * 35) + 15, 200 - arrValues[j], 20, arrValues[j]);
            }

            float sglCurrentAngle;
            float sglTotalAngle = 0;

            for (int a = 0; a < arrValues.Length - 1; a++)
            {
                //取得數據總量
                sglTotalAngle += arrValues[a];
            }

            for (int b = 0; b < arrValues.Length; b++)
            {
                //求出該數據所占總數據的百分比
                sglCurrentAngle = arrValues[b] / sglTotalAngle * 360;
                //畫出橢圓
                g.FillPie(new SolidBrush(GetColor(b)), 220, 95, 100, 100, sglTotalAngle, sglCurrentAngle);
                sglTotalAngle += sglCurrentAngle;
            }
            pictureBox1.Image = objBitMap;
        }

        private Color GetColor(int itemIndex)
        {
            Color objColor = new Color();
            switch (itemIndex)
            {
                case 0:
                    objColor = Color.Blue;
                    break;
                case 1:
                    objColor = Color.Yellow;
                    break;
                case 2:
                    objColor = Color.Red;
                    break;
                case 3:
                    objColor = Color.Orange;
                    break;
                case 4:
                    objColor = Color.Purple;
                    break;
                case 5:
                    objColor = Color.Brown;
                    break;
                case 6:
                default:
                    objColor = Color.Blue;
                    break;
            }
            return objColor;
        }

        private void button35_Click(object sender, EventArgs e)
        {
            //繪製面形圖

            Graphics g;//建立Graphics對像
            Bitmap bt = new Bitmap(pictureBox1.Width, pictureBox1.Height);//實例化一個Bitmap對像
            int flag = (pictureBox1.Width - 4) / 6;//X軸的增值
            g = Graphics.FromImage(bt);//實例化Graphics對像
            Pen p = new Pen(Color.Black, 1);//設定Pen對像
            g.DrawLine(p, new Point(0, 0), new Point(0, pictureBox1.Height - 20));//繪製Y軸
            g.DrawLine(p, new Point(0, pictureBox1.Height - 20), new Point(pictureBox1.Width - 4, pictureBox1.Height - 20));//繪製X軸
            //宣告一個用於繪製顏色的數組
            Color[] cl = new Color[] { Color.Red, Color.Blue, Color.YellowGreen, Color.Yellow, Color.RoyalBlue, Color.Violet, Color.Tomato };
            int[] points = { 20, 70, 80, 60, 40, 100, 10 };//宣告一個計算走勢峰值的數組
            Point pt1 = new Point(0, pictureBox1.Height - 20 - points[0]);//記錄繪製四邊形的第一個點
            Point pt2 = new Point(0, pictureBox1.Height - 20);//記錄繪製四邊形的第二個點
            for (int i = 0; i <= 6; i++)//透過for循環繪製月份和面形圖
            {
                PointF p1 = new PointF(flag * i, pictureBox1.Height - 20);//計算每個月份數字的座標
                //繪製顯示月份的數字
                g.DrawString(i.ToString(), new Font("細明體", 9), new SolidBrush(Color.Black), new PointF(p1.X - 2, p1.Y));
                //記錄繪製四邊形的第三個點
                Point pt3 = new Point(flag * i, pictureBox1.Height - 20);
                //記錄繪製四邊形的第四個點
                Point pt4 = new Point(flag * i, pictureBox1.Height - 20 - points[i]);
                Point[] pt = { pt1, pt2, pt3, pt4 };//宣告一個Point數組
                g.FillPolygon(new SolidBrush(cl[i]), pt);//填充四邊形的顏色
                //當繼續繪製下一個四邊形時，前一個四邊形的最後兩個點作為下一個四邊形的起始點
                pt1 = pt4;
                pt2 = pt3;
            }
            pictureBox1.Image = bt;
        }

        private void button36_Click(object sender, EventArgs e)
        {
            //繪製正弦曲線
            g.Clear(Color.White);

            g.SmoothingMode = SmoothingMode.AntiAlias;
            Rectangle r1 = new Rectangle(0, 0, 360, 20);
            Rectangle r2 = new Rectangle(0, 20, 360, 40);
            Rectangle r3 = new Rectangle(0, 60, 360, 40);
            Rectangle r4 = new Rectangle(0, 100, 360, 20);

            Brush brush1 = new SolidBrush(Color.OrangeRed);
            Brush brush2 = new SolidBrush(Color.SkyBlue);
            Brush brush3 = new SolidBrush(Color.Pink);
            Brush brush4 = new SolidBrush(Color.YellowGreen);

            g.FillRectangle(brush1, r1);
            g.FillRectangle(brush2, r2);
            g.FillRectangle(brush2, r3);
            g.FillRectangle(brush1, r4);

            g.DrawString("0", new Font("宋體", 8), brush1, new PointF(3, 65));
            g.DrawString("90", new Font("宋體", 8), brush1, new PointF(85, 65));
            g.DrawString("180", new Font("宋體", 8), brush1, new PointF(170, 65));
            g.DrawString("360", new Font("宋體", 8), brush1, new PointF(336, 65));

            Point myPoint = new Point(0, 60);

            float sinValue = 0.0F;

            for (int i = 0; i < 360; i++)
            {
                sinValue = Convert.ToSingle(Math.Sin(Convert.ToSingle((i * Math.PI) / 180))) * 40;
                //事實上，這裡根本無需注意 sinValue 的正負
                //當其為負時，  60-sinValue 則會變大
                Point thisPoint = new Point(i, Convert.ToInt32(60 - sinValue));
                g.DrawLine(new Pen(brush3), thisPoint, myPoint);
                myPoint = thisPoint;
            }
            pictureBox1.Image = bitmap1;
        }

        private void button37_Click(object sender, EventArgs e)
        {
        }

        private void button38_Click(object sender, EventArgs e)
        {
            //從DataTable畫曲線圖 1

            //建立DataTable

            DataTable dt = new DataTable();

            Random r = new Random();

            //2.建立表結構
            dt.Columns.Add("月份");
            dt.Columns.Add("數量");

            //3.創建新行
            DataRow dr1 = dt.NewRow();
            DataRow dr2 = dt.NewRow();
            DataRow dr3 = dt.NewRow();
            DataRow dr4 = dt.NewRow();
            DataRow dr5 = dt.NewRow();
            DataRow dr6 = dt.NewRow();
            DataRow dr7 = dt.NewRow();
            DataRow dr8 = dt.NewRow();
            DataRow dr9 = dt.NewRow();
            DataRow dr10 = dt.NewRow();
            DataRow dr11 = dt.NewRow();
            DataRow dr12 = dt.NewRow();

            //4.為新行賦值 並 添加到DataTable
            dr1[0] = "1";
            dr1[1] = r.Next(30).ToString();
            dr2[0] = "2";
            dr2[1] = r.Next(30).ToString();
            dr3[0] = "3";
            dr3[1] = r.Next(30).ToString();
            dr4[0] = "4";
            dr4[1] = r.Next(30).ToString();
            dr5[0] = "5";
            dr5[1] = r.Next(30).ToString();
            dr6[0] = "6";
            dr6[1] = r.Next(30).ToString();
            dr7[0] = "7";
            dr7[1] = r.Next(30).ToString();
            dr8[0] = "8";
            dr8[1] = r.Next(30).ToString();
            dr9[0] = "9";
            dr9[1] = r.Next(30).ToString();
            dr10[0] = "10";
            dr10[1] = r.Next(30).ToString();
            dr11[0] = "11";
            dr11[1] = r.Next(30).ToString();
            dr12[0] = "12";
            dr12[1] = r.Next(30).ToString();

            dt.Rows.Add(dr1);
            dt.Rows.Add(dr2);
            dt.Rows.Add(dr3);
            dt.Rows.Add(dr4);
            dt.Rows.Add(dr5);
            dt.Rows.Add(dr6);
            dt.Rows.Add(dr7);
            dt.Rows.Add(dr8);
            dt.Rows.Add(dr9);
            dt.Rows.Add(dr10);
            dt.Rows.Add(dr11);
            dt.Rows.Add(dr12);

            //建立DrawingCurve, 並把剛剛建立的DataTable給他用
            DrawingCurve MyDc = new DrawingCurve();

            MyDc.tbData = dt;

            Bitmap bitmap1 = new Bitmap(100, 100);

            bitmap1 = MyDc.DrawingImg();

            Graphics g = Graphics.FromImage(MyDc.DrawingImg());
            //显示图形
            pictureBox1.Image = bitmap1;
        }

        private void button39_Click(object sender, EventArgs e)
        {
            //從DataTable畫曲線圖 2
            DrawingCurve MyDc = new DrawingCurve();

            MyDc.tbData = create_datatable_data();

            Bitmap img = new Bitmap(100, 100);

            img = MyDc.DrawingImg();

            pictureBox1.Image = img;

            //Graphics g = Graphics.FromImage(MyDc.DrawingImg());

            //显示图形

            //pictureBox1.Image = bitmap1;

            //Response.Write("<br>" + MyDc.intData.ToString());
        }

        public DataTable create_datatable_data()
        {
            DataTable dt = new DataTable();
            //2.建立表結構
            dt.Columns.Add("月份");
            dt.Columns.Add("數量");

            //3.創建新行
            DataRow dr1 = dt.NewRow();
            DataRow dr2 = dt.NewRow();
            DataRow dr3 = dt.NewRow();
            DataRow dr4 = dt.NewRow();
            DataRow dr5 = dt.NewRow();
            DataRow dr6 = dt.NewRow();
            DataRow dr7 = dt.NewRow();
            DataRow dr8 = dt.NewRow();
            DataRow dr9 = dt.NewRow();
            DataRow dr10 = dt.NewRow();
            DataRow dr11 = dt.NewRow();
            DataRow dr12 = dt.NewRow();

            //4.為新行賦值 並 添加到DataTable
            dr1[0] = "1";
            dr1[1] = "20";
            dt.Rows.Add(dr1);

            dr2[0] = "2";
            dr2[1] = "15";
            dt.Rows.Add(dr2);

            dr3[0] = "3";
            dr3[1] = "18";
            dt.Rows.Add(dr3);

            dr4[0] = "4";
            dr4[1] = "18";
            dt.Rows.Add(dr4);

            dr5[0] = "5";
            dr5[1] = "18";
            dt.Rows.Add(dr5);

            dr6[0] = "6";
            dr6[1] = "18";
            dt.Rows.Add(dr6);

            dr7[0] = "7";
            dr7[1] = "18";
            dt.Rows.Add(dr7);

            dr8[0] = "8";
            dr8[1] = "18";
            dt.Rows.Add(dr8);

            dr9[0] = "9";
            dr9[1] = "18";
            dt.Rows.Add(dr9);

            dr10[0] = "10";
            dr10[1] = "18";
            dt.Rows.Add(dr10);

            dr11[0] = "11";
            dr11[1] = "20";
            dt.Rows.Add(dr11);

            dr12[0] = "12";
            dr12[1] = "15";
            dt.Rows.Add(dr12);

            return dt;
        }

        private void button40_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "RGB三原色\n";

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";

            W = 512;
            H = 512;

            int R = W / 5;
            int cx = W / 2;
            int cy = H / 2;
            int angle = -90;
            int px1 = cx + (int)(R * Math.Cos(Math.PI * (angle) / 180));
            int py1 = cy + (int)(R * Math.Sin(Math.PI * (angle) / 180));
            richTextBox1.Text += "px1 = " + px1.ToString() + "\n";
            richTextBox1.Text += "py1 = " + py1.ToString() + "\n";
            angle -= 120;
            int px2 = cx + (int)(R * Math.Cos(Math.PI * (angle) / 180));
            int py2 = cy + (int)(R * Math.Sin(Math.PI * (angle) / 180));
            richTextBox1.Text += "px2 = " + px2.ToString() + "\n";
            richTextBox1.Text += "py2 = " + py2.ToString() + "\n";
            angle -= 120;
            int px3 = cx + (int)(R * Math.Cos(Math.PI * (angle) / 180));
            int py3 = cy + (int)(R * Math.Sin(Math.PI * (angle) / 180));
            richTextBox1.Text += "px3 = " + px2.ToString() + "\n";
            richTextBox1.Text += "py3 = " + py2.ToString() + "\n";

            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);

            int i;
            int j;
            int r = 120;
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    int d1 = (int)(Math.Sqrt((px1 - i) * (px1 - i) + (py1 - j) * (py1 - j)));
                    int d2 = (int)(Math.Sqrt((px2 - i) * (px2 - i) + (py2 - j) * (py2 - j)));
                    int d3 = (int)(Math.Sqrt((px3 - i) * (px3 - i) + (py3 - j) * (py3 - j)));
                    if ((d1 < r) && (d2 < r) && (d3 < r))
                    {
                        bitmap1.SetPixel(i, j, Color.FromArgb(255, 0xff, 0xff, 0xff));
                    }
                    else if ((d1 < r) && (d2 < r))
                    {
                        bitmap1.SetPixel(i, j, Color.FromArgb(255, 0xff, 0xff, 0x00));
                    }
                    else if ((d2 < r) && (d3 < r))
                    {
                        bitmap1.SetPixel(i, j, Color.FromArgb(255, 0x00, 0xff, 0xff));
                    }
                    else if ((d1 < r) && (d3 < r))
                    {
                        bitmap1.SetPixel(i, j, Color.FromArgb(255, 0xff, 0x00, 0xff));
                    }
                    else if (d1 < r)
                    {
                        bitmap1.SetPixel(i, j, Color.FromArgb(255, 0xff, 0x00, 0x00));
                    }
                    else if (d2 < r)
                    {
                        bitmap1.SetPixel(i, j, Color.FromArgb(255, 0x00, 0xff, 0x00));
                    }
                    else if (d3 < r)
                    {
                        bitmap1.SetPixel(i, j, Color.FromArgb(255, 0x00, 0x00, 0xff));
                    }
                    else
                    {
                        bitmap1.SetPixel(i, j, Color.FromArgb(255, 0x00, 0x00, 0x00));
                    }
                }
            }

            int x_st = 128 * 3;
            int y_st = 0;
            int w = 128;
            int h = 150;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    //bitmap1.SetPixel(xx, yy, background_color);
                    if (j < 50)
                        bitmap1.SetPixel(x_st + i, y_st + j, Color.FromArgb(255, ((i * 2) % 256), 0x00, 0x00));
                    else if (j < 100)
                        bitmap1.SetPixel(x_st + i, y_st + j, Color.FromArgb(255, 0x00, ((i * 2) % 256), 0x00));
                    else
                        bitmap1.SetPixel(x_st + i, y_st + j, Color.FromArgb(255, 0x00, 0x00, ((i * 2) % 256)));
                }
            }

            /* debug
            g.FillEllipse(Brushes.Red, px1 - 5, py1 - 5, 10, 10);
            g.FillEllipse(Brushes.Green, px2 - 5, py2 - 5, 10, 10);
            g.FillEllipse(Brushes.Blue, px3 - 5, py3 - 5, 10, 10);
            g.DrawLine(new Pen(new SolidBrush(Color.Black), 3), px1, py1, px2, py2);
            g.DrawLine(new Pen(new SolidBrush(Color.Black), 3), px1, py1, px3, py3);
            g.DrawLine(new Pen(new SolidBrush(Color.Black), 3), px2, py2, px3, py3);
            */

            x_st = 50;
            y_st = 450;
            int dx = 45;

            g.FillRectangle(Brushes.White, x_st - 20, y_st + 25, 450, 25);

            g.DrawString("R", new Font("標楷體", 36), new SolidBrush(Color.FromArgb(255, 0xff, 0x00, 0x00)), new PointF(x_st, y_st));
            x_st += dx;
            g.DrawString("G", new Font("標楷體", 36), new SolidBrush(Color.FromArgb(255, 0x00, 0xff, 0x00)), new PointF(x_st, y_st));
            x_st += dx;
            g.DrawString("B", new Font("標楷體", 36), new SolidBrush(Color.FromArgb(255, 0x00, 0x00, 0xff)), new PointF(x_st, y_st));
            x_st += dx;
            g.DrawString("紅", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0xff, 0x00, 0x00)), new PointF(x_st, y_st));
            x_st += dx;
            g.DrawString("綠", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0x00, 0xff, 0x00)), new PointF(x_st, y_st));
            x_st += dx;
            g.DrawString("藍", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0x00, 0x00, 0xff)), new PointF(x_st, y_st));
            x_st += dx;
            g.DrawString("三", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0xff, 0x00, 0x00)), new PointF(x_st, y_st));
            x_st += dx;
            g.DrawString("原", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0x00, 0xff, 0x00)), new PointF(x_st, y_st));
            x_st += dx;
            g.DrawString("色", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0x00, 0x00, 0xff)), new PointF(x_st, y_st));

            x_st = 20;
            y_st = 20;
            int dy = 50;
            g.DrawString("紅", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0xff, 0x00, 0x00)), new PointF(x_st, y_st));
            y_st += dy;
            g.DrawString("綠", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0x00, 0xff, 0x00)), new PointF(x_st, y_st));
            y_st += dy;
            g.DrawString("藍", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0x00, 0x00, 0xff)), new PointF(x_st, y_st));

            x_st = 20 + 50;
            y_st = 20;
            g.DrawString("紅", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0xff, 0xff, 0xff)), new PointF(x_st, y_st));
            y_st += dy;
            g.DrawString("綠", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0xff, 0xff, 0xff)), new PointF(x_st, y_st));
            y_st += dy;
            g.DrawString("藍", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0xff, 0xff, 0xff)), new PointF(x_st, y_st));

            /*
            g.DrawString("紅", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0x00, 0xff, 0xff)), new PointF(px1, py1));
            g.DrawString("綠", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0xff, 0x00, 0xff)), new PointF(px2, py2));
            g.DrawString("藍", new Font("標楷體", 32), new SolidBrush(Color.FromArgb(255, 0xff, 0xff, 0x00)), new PointF(px3, py3));
            */

            pictureBox1.Image = bitmap1;
        }

        private void button41_Click(object sender, EventArgs e)
        {
            //奧運五環
            Pen penBlack = new Pen(Color.Black, 6); // 黑色的畫筆 筆寬為 6
            Pen penBlue = new Pen(Color.Blue, 6); // 藍色的畫筆
            Pen penRed = new Pen(Color.Red, 6);  // 紅色的畫筆
            Pen penYellow = new Pen(Color.Yellow, 6); // 黃色的畫筆
            Pen penGreen = new Pen(Color.Green, 6); // 綠色的畫筆

            Graphics g = this.pictureBox1.CreateGraphics();

            int D = 50;  // 圓的半徑
            int Gap = 20;// 圓和圓的 間距
            int Cx = this.pictureBox1.ClientSize.Width / 2; // 抓一個中心點
            int Cy = this.pictureBox1.ClientSize.Height / 2 - D / 2;

            g.SmoothingMode = SmoothingMode.AntiAlias;

            g.DrawEllipse(penBlack, Cx - D, Cy - D, 2 * D, 2 * D);
            g.DrawEllipse(penBlue, Cx - 2 * D - Gap - D, Cy - D, 2 * D, 2 * D);
            g.DrawEllipse(penRed, Cx + 2 * D + Gap - D, Cy - D, 2 * D, 2 * D);
            g.DrawEllipse(penYellow, Cx - D - Gap / 2 - D, Cy + D - D, 2 * D, 2 * D);
            g.DrawEllipse(penGreen, Cx + D + Gap / 2 - D, Cy + D - D, 2 * D, 2 * D);

            // 黑色的弧在上面
            g.DrawArc(penBlack, Cx - D, Cy - D, 2 * D, 2 * D, -10, 20);
            g.DrawArc(penBlack, Cx - D, Cy - D, 2 * D, 2 * D, 90, 20);

            // 藍色的弧在上面
            g.DrawArc(penBlue, Cx - 2 * D - Gap - D, Cy - D, 2 * D, 2 * D, -10, 20);

            // 紅色的弧在上面
            g.DrawArc(penRed, Cx + 2 * D + Gap - D, Cy - D, 2 * D, 2 * D, 90, 20);
        }

        //圓圈拼圖 ST
        private void button42_Click(object sender, EventArgs e)
        {
            //圓圈拼圖
            Graphics g = this.pictureBox1.CreateGraphics();// 取得 表單畫布
            g.SmoothingMode = SmoothingMode.AntiAlias;

            int D = this.pictureBox1.ClientSize.Height / 6; // 第一個圓的半徑
            Point p = new Point(this.pictureBox1.ClientSize.Width / 2, this.pictureBox1.ClientSize.Height / 2);

            g.TranslateTransform(p.X, p.Y); // 從這個點開始長出
            g.FillEllipse(Brushes.Red, -D, -D, 2 * D, 2 * D); // 繪出第一個圓

            int n = 6; // 遞迴深入 6 層
            Matrix m = g.Transform;  // 暫存目前的 矩陣
            Draw1(g, p, n, D, 0); //呼叫 遞迴函數 開始圓圈的增長 右

            g.Transform = m;
            Draw1(g, p, n, D, 90); //呼叫 遞迴函數 開始圓圈的增長 下

            g.Transform = m;
            Draw1(g, p, n, D, 180); //呼叫 遞迴函數 開始圓圈的增長 左

            g.Transform = m;
            Draw1(g, p, n, D, 270); //呼叫 遞迴函數 開始圓圈的增長 上
        }

        // 遞迴函數
        void Draw1(Graphics g, Point p, int n, int D, float Angle)
        {
            if (n > 0) // 共有 n 層
            {
                n = n - 1;
                int D2 = (int)(D * 0.5f); // 這一層的 圓的半徑

                Point p1 = new Point(D2, 0);
                g.RotateTransform(Angle);      // 從上一層 圓圈 長出去的角度
                g.TranslateTransform(D + D2, 0); // 從這個點開始長出
                if (n % 2 == 0) // 偶數著紅色
                {
                    g.FillEllipse(Brushes.Red, -D2, -D2, 2 * D2, 2 * D2);
                }
                else  // 奇數著藍色
                {
                    g.FillEllipse(Brushes.Blue, -D2, -D2, 2 * D2, 2 * D2);
                }
                Matrix m = g.Transform; // 暫存目前的 矩陣 
                Draw1(g, p1, n, D2, 0); // 同方向 繼續長出去

                g.Transform = m; // 取回先前暫存的 矩陣 
                Draw1(g, p1, n, D2, 90); // 同方向 轉 90 度繼續長出去

                g.Transform = m; // 取回先前暫存的 矩陣
                Draw1(g, p1, n, D2, -90); // 同方向 轉 -90 度繼續長出去
            }
        }
        //圓圈拼圖 SP

        private void button43_Click(object sender, EventArgs e)
        {
            g = pictureBox1.CreateGraphics();
            //三個齒輪
            // Draw smoothly.
            g.SmoothingMode = SmoothingMode.AntiAlias;

            const float radius = 50;
            const float tooth_length = 10;
            float x = pictureBox1.ClientSize.Width / 2 - radius - tooth_length - 1;
            float y = pictureBox1.ClientSize.Height / 3;
            DrawGear(g, Brushes.Black, Brushes.LightBlue, Pens.Blue, new PointF(x, y),
                radius, tooth_length, 10, 5, true);

            x += 2 * radius + tooth_length + 2;
            DrawGear(g, Brushes.Black, Brushes.LightGreen, Pens.Green, new PointF(x, y),
                radius, tooth_length, 10, 5, false);

            y += 2 * radius + tooth_length + 2;
            DrawGear(g, Brushes.Black, Brushes.Pink, Pens.Red, new PointF(x, y),
                radius, tooth_length, 10, 5, true);
        }

        // Draw a gear.
        private void DrawGear(Graphics g, Brush axle_brush, Brush gear_brush, Pen gear_pen, PointF center, float radius, float tooth_length, int num_teeth, float axle_radius, bool start_with_tooth)
        {
            float dtheta = (float)(Math.PI / num_teeth);
            float dtheta_degrees = (float)(dtheta * 180 / Math.PI);     // dtheta in degrees.

            const float chamfer = 2;
            float tooth_width = radius * dtheta - chamfer;
            float alpha = tooth_width / (radius + tooth_length);
            float alpha_degrees = (float)(alpha * 180 / Math.PI);
            float phi = (dtheta - alpha) / 2;

            // Set theta for the beginning of the first tooth.
            float theta;
            if (start_with_tooth) theta = dtheta / 2;
            else theta = -dtheta / 2;

            // Make rectangles to represent the gear's inner and outer arcs.
            RectangleF inner_rect = new RectangleF(
                center.X - radius, center.Y - radius,
                2 * radius, 2 * radius);
            RectangleF outer_rect = new RectangleF(
                center.X - radius - tooth_length, center.Y - radius - tooth_length,
                2 * (radius + tooth_length), 2 * (radius + tooth_length));

            // Make a path representing the gear.
            GraphicsPath path = new GraphicsPath();
            for (int i = 0; i < num_teeth; i++)
            {
                // Move across the gap between teeth.
                float degrees = (float)(theta * 180 / Math.PI);
                path.AddArc(inner_rect, degrees, dtheta_degrees);
                theta += dtheta;

                // Move across the tooth's outer edge.
                degrees = (float)((theta + phi) * 180 / Math.PI);
                path.AddArc(outer_rect, degrees, alpha_degrees);
                theta += dtheta;
            }

            path.CloseFigure();

            // Draw the gear.
            g.FillPath(gear_brush, path);
            g.DrawPath(gear_pen, path);
            g.FillEllipse(axle_brush,
                center.X - axle_radius, center.Y - axle_radius,
                2 * axle_radius, 2 * axle_radius);
        }

        //樹木的增長 ST
        private void button44_Click(object sender, EventArgs e)
        {
            //樹木的增長
            Graphics g = this.pictureBox1.CreateGraphics();// 取得 表單畫布

            g.SmoothingMode = SmoothingMode.AntiAlias;

            int len = this.pictureBox1.ClientSize.Height / 7; // 第一根樹枝的高度
            Point p1 = new Point(this.pictureBox1.ClientSize.Width / 2, this.pictureBox1.ClientSize.Height);
            Point p2 = new Point(this.pictureBox1.ClientSize.Width / 2, this.pictureBox1.ClientSize.Height - len);
            g.DrawLine(Pens.Black, p1, p2); // 繪出第一根樹枝

            Draw2(g, p2, 10, len); //呼叫 遞迴函數 開始樹木的增長
        }

        void Draw2(Graphics g, Point p, int n, int len)
        {
            if (n > 0) // 共有 n 層
            {
                n = n - 1;
                int len2 = (int)(len * 0.9f); // 這一層的 樹枝的高度
                Point p1 = new Point(0, 0);
                Point p2 = new Point(0, -len2);

                g.TranslateTransform(p.X, p.Y); // 從這個點開始長出
                Matrix m = g.Transform; // 暫存目前的 矩陣 (左枝 還要用)

                // 右枝
                g.RotateTransform(15);
                g.DrawLine(Pens.Black, p1, p2);  // 長出
                Draw2(g, p2, n, len2);  // 呼叫 下一層

                // 左枝
                g.Transform = m;
                g.RotateTransform(-15);
                g.DrawLine(Pens.Black, p1, p2); // 長出
                Draw2(g, p2, n, len2); // 呼叫 下一層
            }
        }
        //樹木的增長 SP

        private void button45_Click(object sender, EventArgs e)
        {
            //太極圖
            //太極圖
            int imgWidth = 400; //圖象尺寸
            int eyeRadius = imgWidth / 20; //魚眼半徑
            int headDiameter = imgWidth / 2; //魚頭直徑

            Bitmap image = new Bitmap(imgWidth, imgWidth);
            image.SetResolution(300, 300);

            Graphics g = Graphics.FromImage(image);

            //設置圖像質量
            g.CompositingQuality = CompositingQuality.HighQuality;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;


            //底色填充為白色
            Brush white = new SolidBrush(Color.White);
            g.FillRectangle(white, new Rectangle(0, 0, imgWidth, imgWidth));

            Brush blue = new SolidBrush(Color.Blue);//定義藍色筆刷
            Brush red = new SolidBrush(Color.Red);//定義紅色筆刷

            //整個圓形填充藍色
            g.FillPie(blue, 0, 0, imgWidth, imgWidth, 0, 360);

            //定義右邊的路徑（紅色部分）
            GraphicsPath redPath = new GraphicsPath();//初始化路徑
            redPath.AddArc(0, 0, imgWidth, imgWidth, 0, -180);
            redPath.AddArc(0, headDiameter / 2, headDiameter, headDiameter, 0, -180);
            redPath.AddArc(headDiameter, headDiameter / 2, headDiameter, headDiameter, 0, 180);
            //填充右邊部分
            g.FillPath(red, redPath);
            //填充紅色眼睛
            g.FillPie(red, new Rectangle(headDiameter / 2 - eyeRadius, headDiameter - eyeRadius, eyeRadius * 2, eyeRadius * 2), 0, 360);
            //填充藍色眼睛
            g.FillPie(blue, new Rectangle(headDiameter + headDiameter / 2 - eyeRadius, headDiameter - eyeRadius, eyeRadius * 2, eyeRadius * 2), 0, 360);

            pictureBox1.Image = image;
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        private void button46_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(268, 186);
            Font Var_Font = new Font("Arial", 12, FontStyle.Bold);//定義字符串的字體樣式
            Rectangle rect = new Rectangle(10, 10, 160, 160);//實例化Rectangle類

            int tem_Line = 0;//記錄圓的直徑
            int circularity_W = 4;//設置圓畫筆的粗細
            if (pictureBox1.Width >= pictureBox1.Height)//如果pictureBox1控件的寬度大於等於高度
            {
                tem_Line = pictureBox1.Height;//設置高度為圓的直徑
            }
            else
            {
                tem_Line = pictureBox1.Width;//設置寬度為圓的直徑
            }
            rect = new Rectangle(circularity_W, circularity_W, tem_Line - circularity_W * 2, tem_Line - circularity_W * 2);//設置圓的繪製區域
            Font star_Font = new Font("Arial", 30, FontStyle.Regular);//設置星號的字體樣式
            string star_Str = "★";
            Graphics g = this.pictureBox1.CreateGraphics();//實例化Graphics類
            g.SmoothingMode = SmoothingMode.AntiAlias;//消除繪製圖形的鋸齒
            g.Clear(Color.White);//以白色清空pictureBox1控件的背景
            Pen myPen = new Pen(Color.Red, circularity_W);//設置畫筆的顏色
            g.DrawEllipse(myPen, rect); //繪製圓 
            SizeF Var_Size = new SizeF(rect.Width, rect.Width);//實例化SizeF類
            Var_Size = g.MeasureString(star_Str, star_Font);//對指定字符串進行測量
            //要指定的位置繪製星號
            g.DrawString(star_Str, star_Font, myPen.Brush, new PointF((rect.Width / 2F) + circularity_W - Var_Size.Width / 2F, rect.Height / 2F - Var_Size.Width / 2F));
            Var_Size = g.MeasureString("專用章", Var_Font);//對指定字符串進行測量
            //繪製文字
            g.DrawString("專用章", Var_Font, myPen.Brush, new PointF((rect.Width / 2F) + circularity_W - Var_Size.Width / 2F, rect.Height / 2F + Var_Size.Height * 2));
            string tempStr = "吉林省明日科技有限公司";
            int len = tempStr.Length;//獲取字符串的長度
            float angle = 180 + (180 - len * 20) / 2;//設置文字的旋轉角度
            for (int i = 0; i < len; i++)//將文字以指定的弧度進行繪製
            {
                //將指定的平移添加到g的變換矩陣前         
                g.TranslateTransform((tem_Line + circularity_W / 2) / 2, (tem_Line + circularity_W / 2) / 2);
                g.RotateTransform(angle);//將指定的旋轉用於g的變換矩陣   
                Brush myBrush = Brushes.Red;//定義畫刷
                g.DrawString(tempStr.Substring(i, 1), Var_Font, myBrush, 60, 0);//顯示旋轉文字
                g.ResetTransform();//將g的全局變換矩陣重置為單位矩陣
                angle += 20;//設置下一個文字的角度
            }
        }

        private void button47_Click(object sender, EventArgs e)
        {
            //利用GDI畫樹狀圖
            //第一步，定義一下各個結點的內容以及結點數量等初始信息
            string parentTree = "中國";
            ArrayList midTree = new ArrayList();
            midTree.Add("江蘇省");
            midTree.Add("山東省");
            int midTreeCount = midTree.Count;
            ArrayList subTree = new ArrayList();
            subTree.Add("南京市");
            subTree.Add("揚州市");
            subTree.Add("蘇州市");
            subTree.Add("青島市");
            subTree.Add("日照市");
            int subTreeCount = subTree.Count;
            ArrayList eachSubTreeCount = new ArrayList();
            eachSubTreeCount.Add(3);
            eachSubTreeCount.Add(2);

            //定義一些畫圖需要的初始變量

            int midCountFlag = 0;   //畫中間結點時用到的偏移量 
            int subCountFlag = 0;   //畫頂層結點時用到的偏移量 
            int x = 0;              //結點矩形圖左上角X坐標 
            int y = 0;              //結點矩形圖左上角Y坐標 
            int picX = pictureBox1.Width;   //繪圖區域水平長度 
            int picY = pictureBox1.Height;  //繪圖區域豎直長度 
            StringFormat sf = new StringFormat();
            sf.Alignment = StringAlignment.Center;
            Rectangle rect;         //結點矩形圖 
            Point loc;              //結點矩形圖左上角坐標 
            Point startP;           //連接線起始坐標 
            Point endP;             //連接線終止坐標 
            Point tempP = new Point();   //坐標緩存量 
            SizeF sizeF;            //結點內容尺寸大小 
            Size s;
            Font font = new Font("宋體", 18);     //結點內容的字體 
            Pen redPen = new Pen(Color.Red, 2);   //連線需要的畫筆 
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);         //每次重繪先把繪圖區域清空 

            //OK，這時我們就可以開始畫了，先把根部畫出來。

            #region  畫樹根
            sizeF = g.MeasureString(parentTree, font);
            sizeF.Width += 10;
            s = sizeF.ToSize();

            x = Convert.ToInt32((picX - sizeF.Width) / 2);
            y = 30;
            startP = new Point(picX / 2, y + s.Height);
            loc = new Point(x, y);

            rect = new Rectangle(loc, s);
            g.DrawRectangle(Pens.Black, rect);
            g.DrawString(parentTree, font, Brushes.Black, rect, sf);
            #endregion

            //再把樹根的子樹畫出來。

            #region  畫子樹
            foreach (object o in midTree)
            {
                int picXMid = picX / midTreeCount;

                string strMidTree = o.ToString();
                sizeF = g.MeasureString(strMidTree, font);
                sizeF.Width += 10;
                s = sizeF.ToSize();

                x = Convert.ToInt32((picXMid - sizeF.Width) / 2 + picXMid * midCountFlag);
                y = 230;
                endP = new Point(picXMid / 2 + picXMid * midCountFlag, y);
                loc = new Point(x, y);

                rect = new Rectangle(loc, s);
                g.DrawRectangle(Pens.Black, rect);
                g.DrawString(strMidTree, font, Brushes.Black, rect, sf);
                g.DrawLine(redPen, startP, endP);

                midCountFlag++;
                if (midCountFlag == 1)
                    tempP = new Point(endP.X, endP.Y + s.Height);
            }
            #endregion

            //畫出子樹的樹枝。

            #region  畫子樹的樹枝

            startP = tempP;

            for (int i = 0; i != midTree.Count; ++i)
            {
                int picXMid = picX / midTreeCount;
                startP.X += picXMid * i;
                if (i >= 1)
                    subCountFlag += (int)eachSubTreeCount[i - 1];
                for (int j = 0; j != (int)eachSubTreeCount[i]; ++j)
                {

                    int picXSub = picX / (midTreeCount * (int)eachSubTreeCount[i]);

                    string strSubTree = subTree[j + subCountFlag].ToString();
                    sizeF = g.MeasureString(strSubTree, font);
                    sizeF.Width += 10;
                    s = sizeF.ToSize();

                    x = Convert.ToInt32(((picXSub - sizeF.Width) / 2 + picXSub * j) + picXMid * i);
                    y = 430;
                    endP = new Point(picXSub / 2 + picXSub * j + picXMid * i, y);
                    loc = new Point(x, y);

                    rect = new Rectangle(loc, s);
                    g.DrawRectangle(Pens.Black, rect);
                    g.DrawString(strSubTree, font, Brushes.Black, rect, sf);
                    g.DrawLine(redPen, startP, endP);
                }
            }
            #endregion
        }

        private void button48_Click(object sender, EventArgs e)
        {
            PieChart pc = new PieChart();
            //pc.Render(title, subTitle, width, height, ds, Response.OutputStream);

            BarChart bc = new BarChart();
            //bc.Render(title, subTitle, width, height, ds, Response.OutputStream);
        }

        private void button49_Click(object sender, EventArgs e)
        {
            //座標圖
            //使用GDI畫坐標圖(支持負值)

            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height, PixelFormat.Format24bppRgb);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            Font font = new Font(Font.Name, 11);
            SolidBrush brush = new SolidBrush(Color.Black);
            Pen pen = new Pen(Color.Black);
            pen.EndCap = LineCap.ArrowAnchor;
            pen.DashStyle = DashStyle.Solid;
            //坐标轴
            Point pCenter = new Point(300, 260);
            g.DrawLine(pen, new Point(pCenter.X - 200, pCenter.Y), new Point(pCenter.X + 200, pCenter.Y));//x
            g.DrawLine(pen, new Point(pCenter.X, pCenter.Y + 200), new Point(pCenter.X, pCenter.Y - 200));//y            
            //轴标格
            int iX = 30;
            for (int i = 0; i < 5; i++)
            {
                //零點向左
                g.DrawLine(Pens.Black, new Point(pCenter.X - iX * i, pCenter.Y), new Point(pCenter.X - iX * i, pCenter.Y - 4));//x
                g.DrawString((-i).ToString(), font, brush, new PointF(pCenter.X - iX * i, pCenter.Y));

                //零點向右
                g.DrawLine(Pens.Black, new Point(pCenter.X + iX * i, pCenter.Y), new Point(pCenter.X + iX * i, pCenter.Y - 4));//x
                g.DrawString(i.ToString(), font, brush, new PointF(pCenter.X + iX * i, pCenter.Y));

                //零點向上
                g.DrawLine(Pens.Black, new Point(pCenter.X, pCenter.Y - iX * i), new Point(pCenter.X + 4, pCenter.Y - iX * i));//y
                g.DrawString(i.ToString(), font, brush, new PointF(pCenter.X, pCenter.Y - iX * i));

                //零點向下
                g.DrawLine(Pens.Black, new Point(pCenter.X, pCenter.Y + iX * i), new Point(pCenter.X + 4, pCenter.Y + iX * i));//y
                g.DrawString((-i).ToString(), font, brush, new PointF(pCenter.X, pCenter.Y + iX * i));
            }

            StringFormat sf = new StringFormat();
            sf.Alignment = StringAlignment.Far;
            g.DrawString("x", font, brush, new PointF(pCenter.X + 200, pCenter.Y));
            g.DrawString("y", font, brush, new PointF(pCenter.X, pCenter.Y - 200));
            g.DrawString("0", font, brush, new PointF(pCenter.X, pCenter.Y));
            //定义比例尺
            int BX = 4;
            int BY = 4;
            Point new1 = getNewPoint(new Point(200, 300), pCenter, BX, BY);
            Point new2 = getNewPoint(new Point(-300, 400), pCenter, BX, BY);
            Point new3 = getNewPoint(new Point(-400, -500), pCenter, BX, BY);
            Point new4 = getNewPoint(new Point(500, -300), pCenter, BX, BY);
            //g.DrawLine(Pens.Black, pCenter, new1);
            g.DrawArc(Pens.Black, new1.X, new1.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p1", font, brush, new PointF(new1.X, new1.Y));
            g.DrawArc(Pens.Black, new2.X, new2.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p2", font, brush, new PointF(new2.X, new2.Y));
            g.DrawArc(Pens.Black, new3.X, new3.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p3", font, brush, new PointF(new3.X, new3.Y));
            g.DrawArc(Pens.Black, new4.X, new4.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p4", font, brush, new PointF(new4.X, new4.Y));
            g.DrawLine(Pens.Black, new1, new2);
            g.DrawLine(Pens.Black, new2, new3);
            g.DrawLine(Pens.Black, new3, new4);
            g.DrawLine(Pens.Black, new4, new1);

            pictureBox1.Image = bitmap1;
        }

        Point getNewPoint(Point p, Point pZero, int bx, int by)
        {
            Point myp = new Point();
            myp.X = pZero.X + p.X / bx;
            if (p.Y > 0)
            {
                myp.Y = pZero.Y - Math.Abs(p.Y / by);
            }
            else
            {
                myp.Y = pZero.Y + Math.Abs(p.Y / by);
            }
            return myp;
        }

        List<Point> pattern0 = new List<Point>
            {
            new Point(-15, 0),
            new Point(-8, 0),
            new Point(-8, 1),
            new Point(-7, 1),
            new Point(-6, 1),
            new Point(-6, 0),
            new Point(-7, 0),
            new Point(-7, 1),
            new Point(-7, 2),
            new Point(-6, 2),
            new Point(-5, 2),
            new Point(-5, 1),
            new Point(-5, 0),
            new Point(-4, 0),
            new Point(-3, 0),
            new Point(-3, 1),
            new Point(-3, 2),
            new Point(-3, 3),
            new Point(-2, 3),
            new Point(-1, 3),
            new Point(0, 3),
            new Point(0, 4),
            new Point(0, 5),
            new Point(-1, 5),
            new Point(-2, 5),
            new Point(-2, 6),
            new Point(-2, 7),
            new Point(-1, 7),
            new Point(0, 7),
            new Point(0, 6),
            new Point(-1, 6),
            new Point(-1, 7),
            new Point(-1, 8),
            new Point(0, 8),
            new Point(0, 15),
            new Point(9999, 9999),  //以9999為分段界限
            new Point(0, 0),
            new Point(-1, 0),
            new Point(-2, 0),
            new Point(-2, 1),
            new Point(-2, 2),
            new Point(-2, 3),
            new Point(-2, 4),
            new Point(-1, 4),
            new Point(-1, 3),
            new Point(-1, 2),
            new Point(-1, 1),
            new Point(-2, 1),
            new Point(-3, 1),
            new Point(-4, 1),
            new Point(-4, 2),
            new Point(-3, 2),
            new Point(-2, 2),
            new Point(-1, 2),
            new Point(-0, 2),
            new Point(-0, 1),
            new Point(-0, 0),
            new Point(-1, 0)
            };

        List<Point> pattern1 = new List<Point>
            {
            new Point(-15, 0),
            new Point(-3, 0),
            new Point(-2, 0),
            new Point(-2, 1),
            new Point(-2, 2),
            new Point(-2, 3),
            new Point(-1, 3),
            new Point(-1, 2),
            new Point(-1, 1),
            new Point(-1, 0),
            new Point(-0, 0),
            new Point(-0, 1),
            new Point(-1, 1),
            new Point(-2, 1),
            new Point(-3, 1),
            new Point(-3, 2),
            new Point(-2, 2),
            new Point(-1, 2),
            new Point(-0, 2),
            new Point(-0, 3),
            new Point(-0, 15)
            };

        List<Point> pattern2 = new List<Point>
            {
            new Point(-15, 0),
            new Point(-6, 0),
            new Point(-5, 0),
            new Point(-4, 0),
            new Point(-3, 0),
            new Point(-3, 1),
            new Point(-3, 2),
            new Point(-2, 2),
            new Point(-1, 2),
            new Point(0, 2),
            new Point(0, 1),
            new Point(0, 0),
            new Point(-1, 0),
            new Point(-2, 0),
            new Point(-2, 1),
            new Point(-2, 2),
            new Point(-2, 3),
            new Point(-1, 3),
            new Point(0, 3),
            new Point(0, 4),
            new Point(0, 5),
            new Point(0, 6),
            new Point(0, 15),
            new Point(9999, 9999),
            new Point(-15, 1),
            new Point(-6, 1),
            new Point(-5, 1),
            new Point(-4, 1),
            new Point(-3, 1),
            new Point(-2, 1),
            new Point(-1, 1),
            new Point(-1, 2),
            new Point(-1, 3),
            new Point(-1, 4),
            new Point(-1, 5),
            new Point(-1, 6),
            new Point(-1, 15)
            };

        List<Point> pattern3 = new List<Point>
            {
            new Point(-15, 0),
            new Point(-10, 0),
            new Point(-6, 0),
            new Point(-6, 4),
            new Point(-10, 4),
            new Point(9999, 9999),
            new Point(0, 0),
            new Point(0, 4),
            new Point(-4, 4),
            new Point(-4, 0),
            new Point(0, 0),
            new Point(0, 4),
            new Point(9999, 9999),
            new Point(-4, 10),
            new Point(-4, 6),
            new Point(0, 6),
            new Point(0, 10),
            new Point(0, 15)
            };

        List<Point> pattern4 = new List<Point>
            {
            new Point(0, 0),
            new Point(1, 0),
            new Point(1, 1),
            new Point(1, 2),
            new Point(1, 3),
            new Point(1, 4),
            new Point(2, 4),
            new Point(2, 3),
            new Point(2, 2),
            new Point(2, 1),
            new Point(2, 0),
            new Point(3, 0),
            new Point(3, 1),
            new Point(3, 2),
            new Point(3, 3),
            new Point(3, 4),
            new Point(4, 4),
            new Point(4, 3),
            new Point(3, 3),
            new Point(2, 3),
            new Point(1, 3),
            new Point(0, 3),
            new Point(0, 2),
            new Point(1, 2),
            new Point(2, 2),
            new Point(3, 2),
            new Point(4, 2),
            new Point(4, 1),
            new Point(3, 1),
            new Point(2, 1),
            new Point(1, 1),
            new Point(0, 1),
            new Point(0, 0),
            new Point(1, 0)
            };

        void draw_frame_style(List<Point> pattern, int offset_x, int offset_y, int step)
        {
            //畫邊框
            Pen bluePen = new Pen(Color.Blue, 8);
            Pen redPen = new Pen(Color.Red, 8);
            Point corner = new Point(15, 0); //最右上角的點
            List<Point> points_draw = new List<Point>();
            int x1 = 0;
            int y1 = 0;
            int x2 = 0;
            int y2 = 0;
            int i;

            for (i = 0; i < pattern.Count; i++)
            {
                if ((pattern[i].X == 9999) && (pattern[i].Y == 9999))
                {
                    if (points_draw.Count > 1)
                    {
                        g.DrawLines(bluePen, points_draw.ToArray());  //畫直線
                    }
                    points_draw.Clear();
                }
                else
                {
                    x1 = corner.X + pattern[i].X;
                    y1 = corner.Y + pattern[i].Y;

                    x2 = offset_x + x1 * step;
                    y2 = offset_y + y1 * step;

                    points_draw.Add(new Point(x2, y2));
                }
            }
            if (points_draw.Count > 1)
            {
                g.DrawLines(bluePen, points_draw.ToArray());  //畫直線
            }
        }

        void draw_frame_style_index(List<Point> pattern, int offset_x, int offset_y, int step, int index)
        {
            //畫邊框
            Pen bluePen = new Pen(Color.Blue, 8);
            Pen redPen = new Pen(Color.Red, 8);
            Point corner = new Point(15, 0); //最右上角的點
            List<Point> points_draw = new List<Point>();
            int x1 = 0;
            int y1 = 0;
            int x2 = 0;
            int y2 = 0;
            int i;

            for (i = 0; i < index; i++)
            {
                if ((pattern[i].X == 9999) && (pattern[i].Y == 9999))
                {
                    if (points_draw.Count > 1)
                    {
                        g.DrawLines(bluePen, points_draw.ToArray());  //畫直線
                    }
                    points_draw.Clear();
                }
                else
                {
                    x1 = corner.X + pattern[i].X;
                    y1 = corner.Y + pattern[i].Y;

                    x2 = offset_x + x1 * step;
                    y2 = offset_y + y1 * step;

                    points_draw.Add(new Point(x2, y2));
                }
            }
            if (points_draw.Count > 1)
            {
                g.DrawLines(bluePen, points_draw.ToArray());  //畫直線
            }
        }

        List<Point> pattern_recursive = new List<Point> { };

        void make_pattern_recursive_data()
        {

            int x_st = 0;
            int y_st = 0;
            int N = 50;
            int i;
            int j;
            int direction = 0;  //0: 向右 1: 向上 2: 向左 3: 向下
            int go_steps = 1;   // 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8
            int go_count = 0;   // 0 or 1

            pattern_recursive.Clear();
            pattern_recursive.Add(new Point(x_st, y_st));

            for (i = 0; i < N; i++)
            {
                for (j = 0; j < go_steps; j++)
                {
                    if (direction == 0)
                    {
                        x_st++;
                    }
                    else if (direction == 1)
                    {
                        y_st--;
                    }
                    else if (direction == 2)
                    {
                        x_st--;
                    }
                    else if (direction == 3)
                    {
                        y_st++;
                    }
                    else
                    {
                        richTextBox1.Text += "XXXXX\n";
                    }
                    //richTextBox1.Text += "dir = " + direction.ToString() + "\tgo_steps = " + go_steps.ToString() + "\tgo_count = " + go_count.ToString() + "\n";
                    pattern_recursive.Add(new Point(x_st, y_st));
                }
                go_count++;
                if (go_count > 1)
                {
                    go_count = 0;
                    go_steps++;
                }

                direction++;
                if (direction > 3)
                {
                    direction = 0;
                }
            }
        }

        private void bt_long0_Click(object sender, EventArgs e)
        {
        }

        private void bt_long1_Click(object sender, EventArgs e)
        {
        }

        private void bt_long2_Click(object sender, EventArgs e)
        {
            //以四周擴散形式顯示圖片
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            DiffuseEffect(filename.Trim(), pictureBox1);//呼叫自定義方法完成圖片向四周的擴充
        }

        public void DiffuseEffect(string Str, PictureBox pictureBox1)
        {
            Bitmap tem_Bitmap = new Bitmap(Str);//根據字串實例化Bitmap類
            Bitmap Var_Bitmap = new Bitmap(tem_Bitmap, pictureBox1.Width, pictureBox1.Height);//根據大小實例化Bitmap類
            int Var_W = Var_Bitmap.Width; //圖片寬度 
            int Var_H = Var_Bitmap.Height; //圖片高度 
            Graphics g = pictureBox1.CreateGraphics();//取得Graphics對像 
            g.Clear(pictureBox1.BackColor); //初始為全灰色 
            for (int i = 0; i <= Var_W / 2; i++)
            {
                //取得高和寬的比例
                int j = Convert.ToInt32(i * (Convert.ToSingle(Var_H) / Convert.ToSingle(Var_W)));
                //設定縮小後圖片的大小
                Rectangle Var_D_Rect = new Rectangle(Var_W / 2 - i, Var_H / 2 - j, 2 * i, 2 * j);
                //取得原圖片大小
                Rectangle Var_S_Rect = new Rectangle(0, 0, Var_Bitmap.Width, Var_Bitmap.Height);
                g.DrawImage(Var_Bitmap, Var_D_Rect, Var_S_Rect, GraphicsUnit.Pixel);//按照指定的大小繪製原圖片
                Thread.Sleep(10);//線程序掛掉
            }
        }

        private void bt_long3_Click(object sender, EventArgs e)
        {
            //圖片的上下對接顯示
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            UpDownConnect(filename.Trim(), pictureBox1);//呼叫自定義方法
        }

        public void UpDownConnect(string Str, PictureBox pictureBox1)
        {
            Bitmap tem_Bitmap = new Bitmap(Str);
            Bitmap Var_Bitmap = new Bitmap(tem_Bitmap, pictureBox1.Width, pictureBox1.Height);

            int Var_W = Var_Bitmap.Width; //圖片寬度 
            int Var_H = Var_Bitmap.Height; //圖片高度 
            Graphics g = pictureBox1.CreateGraphics();//實例化Graphics類
            g.Clear(Color.Gray);//清空panel控制元件
            Bitmap Tem_bmp = new Bitmap(Var_W, Var_H);//透過圖片大小實例化Bitmap類
            int n = 0;
            //搜尋圖片中的各象素
            while (n <= Var_H / 2)
            {
                for (int i = 0; i <= Var_W - 1; i++)//取得上半張圖片的象素
                {
                    Tem_bmp.SetPixel(i, n, Var_Bitmap.GetPixel(i, n));//根據象素取得目前象的顏色，並記錄在Bitmap類中
                }
                for (int i = 0; i <= Var_W - 1; i++)//取得下半張圖片的象素
                {
                    //根據象素取得目前象的顏色，並記錄在Bitmap類中
                    Tem_bmp.SetPixel(i, Var_H - n - 1, Var_Bitmap.GetPixel(i, Var_H - n - 1));
                }
                n++;
                pictureBox1.Refresh();//設定工作區無效
                g.DrawImage(Tem_bmp, 0, 0);//繪製圖片
                Thread.Sleep(5);//掛掉線程
            }
        }

        //謝爾平斯基的三角形 ST
        //Sierpinski triangle 謝爾平斯基的三角形
        private void bt_long4_Click(object sender, EventArgs e)
        {
            PointF[] pt = new PointF[3];  // 3個點座標陣列
            // 中心點　在視窗客戶區的　正中心
            PointF center = new PointF(this.pictureBox1.ClientSize.Width / 2, this.pictureBox1.ClientSize.Height / 2);
            // 半徑　取短的
            float D = Math.Min(this.pictureBox1.ClientSize.Width / 2, this.pictureBox1.ClientSize.Height / 2) - 10;

            // 　　　　p0
            //      p2     p1 
            for (int i = 0; i < 3; i++) // 定義一個正三角形 的三個角的座標
            {
                pt[i].X = (float)(center.X + D * Math.Cos(-Math.PI / 2 + i * 2 * Math.PI / 3));
                pt[i].Y = (float)(center.Y + D * Math.Sin(-Math.PI / 2 + i * 2 * Math.PI / 3));
            }

            DrawTriangle(pt[0], pt[1], pt[2]); // 畫出第一個 正三角形
            Sierp(pt[0], pt[1], pt[2], 0);
        }

        private void DrawTriangle(PointF p0, PointF p1, PointF p2)
        {
            Graphics g = this.pictureBox1.CreateGraphics();// 取得 表單畫布
            g.DrawLine(Pens.Black, p0, p1); // 畫出三角形
            g.DrawLine(Pens.Black, p1, p2);
            g.DrawLine(Pens.Black, p2, p0);
        }

        void Sierp(PointF p0, PointF p1, PointF p2, int n)
        {
            PointF m0 = new PointF(); // 新的三個點座標
            PointF m1 = new PointF();
            PointF m2 = new PointF();

            if (n < 10)
            {
                // 　　　　p0
                //       /     \
                //     m1        m2
                //    /            \
                // p2 ---- m0 ----  p1
                //
                m2.X = (p0.X + p1.X) / 2; // 新的三個點座標
                m2.Y = (p0.Y + p1.Y) / 2;

                m1.X = (p0.X + p2.X) / 2;
                m1.Y = (p0.Y + p2.Y) / 2;

                m0.X = (p2.X + p1.X) / 2;
                m0.Y = (p2.Y + p1.Y) / 2;

                DrawTriangle(m0, m1, m2); // 畫出 新的三角形

                // 以三個新的三角形 往下呼叫
                Sierp(p0, m2, m1, n + 1);
                Sierp(m1, m0, p2, n + 1);
                Sierp(m2, p1, m0, n + 1);
            }
        }
        //謝爾平斯基的三角形 SP


        private void bt_long5_Click(object sender, EventArgs e)
        {
            //動態旋轉文字

            Bitmap bitmap1 = new Bitmap(300, 200);
            Graphics g = Graphics.FromImage(bitmap1);
            Font f = new Font("arial", 11f);
            Brush b = Brushes.Blue;

            string txt = "Rotate text animation!";
            SizeF sz = g.MeasureString(txt, f);
            g.Clear(Color.WhiteSmoke);
            g.DrawString(txt, f, b, 50 - sz.Width / 2, 50 - sz.Height / 2);
            g.Flush();

            for (int i = 1; i < 36; ++i)
            {
                g.Clear(Color.WhiteSmoke);
                g.TranslateTransform(50, 50);
                g.RotateTransform(10f * i);
                g.DrawString(txt, f, b, sz.Width / -2, sz.Height / -2);
                g.ResetTransform();
                g.DrawString("Hello", f, Brushes.Red, -50 + i * 4, 20);
                g.DrawString("Yeah", f, Brushes.Orange, 60, -20 + i * 4);

                g.Flush();

                pictureBox1.Image = bitmap1;
                Application.DoEvents();
                delay(300);
            }

            f.Dispose();
            bitmap1.Dispose();
        }

        private void bt_long6_Click(object sender, EventArgs e)
        {
            //以任意角度旋轉圖像
            //實現任意角度旋轉圖像主要使用Graphics類提供的RotateTransform()方法

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            //pictureBox1.Image = bitmap1;

            //以任意角度旋轉顯示圖像
            Graphics g = this.pictureBox1.CreateGraphics();
            float MyAngle = 0;//旋轉的角度
            while (MyAngle < 360)
            {
                TextureBrush MyBrush = new TextureBrush(bitmap1);
                this.pictureBox1.Refresh();
                MyBrush.RotateTransform(MyAngle);
                g.FillRectangle(MyBrush, 0, 0, this.ClientRectangle.Width, this.ClientRectangle.Height);
                MyAngle += 0.5f;
                Thread.Sleep(50);
            }

        }

        private void bt_long7_Click(object sender, EventArgs e)
        {
            //實現任意角度旋轉圖片
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);

            //以任意角度旋轉顯示圖像
            Graphics g = this.pictureBox1.CreateGraphics();
            float angle = 0;//旋轉的角度
            while (angle < 360)
            {
                TextureBrush tb = new TextureBrush(image);
                this.pictureBox1.Refresh();
                tb.RotateTransform(angle);
                g.FillRectangle(tb, 0, 0, this.ClientRectangle.Width, this.ClientRectangle.Height);
                angle += 0.5f;
                Thread.Sleep(50);
            }
        }

        private void bt_long8_Click(object sender, EventArgs e)
        {
            //任意角度旋轉圖片
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            CircumgyrateEffect(filename.Trim(), pictureBox1);//呼叫自定義方法
        }

        public void CircumgyrateEffect(string Str, PictureBox pictureBox1)
        {
            Bitmap tem_Bitmap = new Bitmap(Str);//透過字串實例化Bitmap類
            Bitmap Var_Bitmap = new Bitmap(tem_Bitmap, pictureBox1.Width, pictureBox1.Height);//透過panel按件的大小實例化Bitmap類

            Graphics g = pictureBox1.CreateGraphics();//實例化panel控制元件的Graphics類
            float Var_Angle = 0;//設定圖片的旋轉角度
            while (Var_Angle <= 360)//使圖片旋轉360度
            {
                TextureBrush Var_Brush = new TextureBrush(Var_Bitmap);//實例化TextureBrush類
                pictureBox1.Refresh();//使工作區無效
                Var_Brush.RotateTransform(Var_Angle);//以指定角度旋轉圖片
                //繪製旋轉後的圖片
                g.FillRectangle(Var_Brush, 0, 0, this.ClientRectangle.Width, this.ClientRectangle.Height);
                Var_Angle += 2f;//增加旋轉的角度
                Thread.Sleep(30);//掛掉目前線程
            }
        }

        private void bt_long9_Click(object sender, EventArgs e)
        {
            int NNN = 1000;
            Random r = new Random();
            Graphics g = this.pictureBox1.CreateGraphics();


            /*         while(true)
                      {
                          int x1 = r.Next(0, 1366);
                          int y1 = r.Next(0, 200);
                          int x2 = x1;
                          int y2 = y1 + r.Next(0, 400);
                          for(int i=y1;i<=y2;i++)
                          {
                              Pen greenPen = new Pen(Color.Green, r.Next(1, 15));
                              g.DrawLine(greenPen, x1, y1, x2, y2);
                          }
                      }
           */

            int W = 150;
            int H = 300;
            int dx = 50;
            int dy = 50;
            int x_st = dx;
            int y_st = dy;

            for (int i = 0; i < NNN; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), 8);
                int x1 = r.Next(x_st, x_st + W);
                int y1 = r.Next(y_st, y_st + H);
                int x2 = r.Next(x_st, x_st + W);
                int y2 = r.Next(y_st, y_st + H);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);

            }

            x_st = dx + W + dx;
            int cx = x_st + W / 2;
            int cy = y_st + H / 2;

            for (int i = 0; i < NNN; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), 9);
                int x1 = cx;
                int y1 = cy;
                int x2 = r.Next(x_st, x_st + W);
                int y2 = r.Next(y_st, y_st + H);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);

            }

            x_st = dx + W + dx + W + dx;
            cx = x_st + W;
            cy = y_st;
            for (int i = 0; i < NNN; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), 10);
                int x1 = cx;
                int y1 = cy;
                int x2 = r.Next(x_st, x_st + W);
                int y2 = r.Next(y_st, y_st + H);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);

            }

            x_st = dx + W + dx + W + dx + W + dx;
            cx = x_st;
            cy = y_st + H;
            for (int i = 0; i < NNN; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), 11);
                int x1 = cx;
                int y1 = cy;
                int x2 = r.Next(x_st, x_st + W);
                int y2 = r.Next(y_st, y_st + H);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);

            }

            x_st = dx;
            y_st = dy + H + dy;
            //cx = x_st;
            //cy = y_st + H;
            W = dx * 3 + W * 4; ;
            H = 100;

            for (int i = 0; i < NNN; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), 12);
                int x1 = r.Next(x_st, x_st + W);
                int y1 = r.Next(y_st, y_st + H);
                int x2 = r.Next(x_st, x_st + W);
                int y2 = r.Next(y_st, y_st + H);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);

            }
            for (int i = 0; i < NNN; i++)
            {
                Pen whitePen = new Pen(Color.FromArgb(r.Next(0, 255), r.Next(0, 255), r.Next(0, 255)), r.Next(1, 15));
                int x1 = r.Next(x_st, x_st + W); ; //650-900
                int y1 = r.Next(y_st, y_st + H); ; //100-500
                int x2 = r.Next(x_st, x_st + W);
                int y2 = r.Next(y_st, y_st + H);
                // int x1 = 500;
                // int y1 = 500;
                // int x2 = i;
                // int y2 = 1000 * 1000 - i * i;
                g.DrawLine(whitePen, x1, y1, x2, y2);
            }
        }

        private void bt_long10_Click(object sender, EventArgs e)
        {

        }

        private void bt_long11_Click(object sender, EventArgs e)
        {

        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            //g.Clear(Color.White);
            if (checkBox1.Checked == true)
            {
                draw_grid();
            }
            pictureBox1.Image = bitmap1;
        }

        public void draw_grid()
        {
            int i;
            int rows = pictureBox1.ClientSize.Height / 100;
            int cols = pictureBox1.ClientSize.Width / 100;
            p = new Pen(Color.Navy, 1);
            for (i = 0; i <= rows; i++)
            {
                g.DrawLine(p, 0, i * 100, pictureBox1.ClientSize.Width - 1, i * 100);
            }
            for (i = 0; i <= cols; i++)
            {
                g.DrawLine(p, new Point(i * 100, 0), new Point(i * 100, pictureBox1.ClientSize.Height - 1));
            }
        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        int COLUMN = 360 + 1 + 360;
        int ROW = 360 + 1 + 360;

        private double F1(int x, int y)
        {
            return cosd(x) + cosd(y);   //z=cox(x) + cos(y)
        }

        void draw_contour(int cx, int cy)
        {
            int i, j;
            //                                  R   C
            double[,] brightness = new double[ROW, COLUMN];    //Row = 19, Column = 8
            int[,] brightness2 = new int[ROW, COLUMN];    //Row = 19, Column = 8

            //richTextBox1.Text += "assign value\n";

            double stepx = 360.0 / ((COLUMN - 1) / 2);
            double stepy = 360.0 / ((ROW - 1) / 2);

            double max = 0;
            double min = 100;
            double vv = 0;

            //richTextBox1.Text += "stepx = " + stepx.ToString() + "\tstepy = " + stepy.ToString() + "\n";

            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COLUMN; i++)
                {
                    vv = F1(i - cx, j - cy);

                    brightness[j, i] = vv;
                    if (vv > max)
                        max = vv;
                    else if (vv < min)
                        min = vv;

                    //對應到0~255
                    brightness2[j, i] = (int)((vv + 2.0) * 64);
                    if (brightness2[j, i] == 256)
                    {
                        brightness2[j, i] = 255;
                    }
                    brightness2[j, i] = (brightness2[j, i] / 5) * 5;
                }
            }
            //richTextBox1.Text += "max = " + max.ToString() + "\tmin = " + min.ToString() + "\n";

            /*
            richTextBox1.Text += "print value\n";
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    richTextBox1.Text += gray[j, i].ToString("D2") + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            /*
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    //richTextBox1.Text += brightness[j, i].ToString("D2") + "\t";
                    //richTextBox1.Text += brightness[j, i].ToString() + "\t";
                    richTextBox1.Text += ((int)(brightness[j, i] * 100)).ToString("D2") + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            //逐點製作圖檔

            Bitmap bitmap1 = new Bitmap(COLUMN, ROW);

            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COLUMN; i++)
                {
                    if (((i % 100) == 0) && ((j % 50) == 0))
                    {
                        //bitmap1.SetPixel(i, j, Color.Red);
                        brightness2[j, i] = 255;
                    }
                    bitmap1.SetPixel(i, j, Color.FromArgb(255, (byte)(brightness2[j, i]), (byte)(brightness2[j, i]), (byte)(brightness2[j, i])));
                }
            }

            /*
            Graphics g = Graphics.FromImage(bitmap1);
            Pen p = new Pen(Color.Red, 5);
            Point point1a = new Point(0, 360);
            Point point2a = new Point(720, 360);
            g.DrawLine(p, point1a, point2a);

            point1a = new Point(360, 0);
            point2a = new Point(360, 720);
            g.DrawLine(p, point1a, point2a);
            */

            pictureBox1.Image = bitmap1;
            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
        }

        private void bt_2d_array0_Click(object sender, EventArgs e)
        {
            //z=cos(x)+cos(y)
            draw_contour(cx, cy);
            timer2.Enabled = true;
        }

        void fillup_data1(int[,] gray)
        {
            /*
            int i;
            int j;

            int ROW = gray.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = gray.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int length = gray.Length;//獲取整個二維陣列的長度，即所有元 的個數
            richTextBox1.Text += "ROW = " + ROW.ToString() + "\n";
            richTextBox1.Text += "COL = " + COL.ToString() + "\n";
            richTextBox1.Text += "length = " + length.ToString() + "\n";

            richTextBox1.Text += "assign value\n";

            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    gray[j, i] = i * 10 + j;
                }
            }

            return;
            */

            gray[0, 0] = 8;
            gray[1, 0] = 7;
            gray[2, 0] = 8;
            gray[3, 0] = 10;
            gray[4, 0] = 27;
            gray[5, 0] = 85;
            gray[6, 0] = 126;
            gray[7, 0] = 134;
            gray[8, 0] = 138;
            gray[9, 0] = 140;
            gray[10, 0] = 142;
            gray[11, 0] = 143;
            gray[12, 0] = 144;
            gray[13, 0] = 144;
            gray[14, 0] = 146;
            gray[15, 0] = 146;
            gray[16, 0] = 146;
            gray[17, 0] = 146;
            gray[18, 0] = 145;
            gray[19, 0] = 144;
            gray[20, 0] = 141;
            gray[21, 0] = 140;
            gray[22, 0] = 138;
            gray[23, 0] = 135;
            gray[24, 0] = 130;
            gray[25, 0] = 98;
            gray[26, 0] = 28;
            gray[27, 0] = 9;
            gray[28, 0] = 7;
            gray[29, 0] = 8;
            gray[30, 0] = 9;
            gray[0, 1] = 7;
            gray[1, 1] = 8;
            gray[2, 1] = 11;
            gray[3, 1] = 36;
            gray[4, 1] = 105;
            gray[5, 1] = 130;
            gray[6, 1] = 135;
            gray[7, 1] = 139;
            gray[8, 1] = 142;
            gray[9, 1] = 144;
            gray[10, 1] = 146;
            gray[11, 1] = 147;
            gray[12, 1] = 149;
            gray[13, 1] = 150;
            gray[14, 1] = 151;
            gray[15, 1] = 151;
            gray[16, 1] = 151;
            gray[17, 1] = 150;
            gray[18, 1] = 149;
            gray[19, 1] = 148;
            gray[20, 1] = 146;
            gray[21, 1] = 144;
            gray[22, 1] = 142;
            gray[23, 1] = 139;
            gray[24, 1] = 136;
            gray[25, 1] = 131;
            gray[26, 1] = 96;
            gray[27, 1] = 25;
            gray[28, 1] = 9;
            gray[29, 1] = 7;
            gray[30, 1] = 8;
            gray[0, 2] = 7;
            gray[1, 2] = 9;
            gray[2, 2] = 31;
            gray[3, 2] = 107;
            gray[4, 2] = 130;
            gray[5, 2] = 135;
            gray[6, 2] = 139;
            gray[7, 2] = 143;
            gray[8, 2] = 145;
            gray[9, 2] = 148;
            gray[10, 2] = 150;
            gray[11, 2] = 151;
            gray[12, 2] = 153;
            gray[13, 2] = 154;
            gray[14, 2] = 155;
            gray[15, 2] = 155;
            gray[16, 2] = 155;
            gray[17, 2] = 154;
            gray[18, 2] = 154;
            gray[19, 2] = 152;
            gray[20, 2] = 150;
            gray[21, 2] = 149;
            gray[22, 2] = 147;
            gray[23, 2] = 144;
            gray[24, 2] = 140;
            gray[25, 2] = 136;
            gray[26, 2] = 130;
            gray[27, 2] = 92;
            gray[28, 2] = 26;
            gray[29, 2] = 9;
            gray[30, 2] = 7;
            gray[0, 3] = 8;
            gray[1, 3] = 18;
            gray[2, 3] = 91;
            gray[3, 3] = 127;
            gray[4, 3] = 134;
            gray[5, 3] = 139;
            gray[6, 3] = 142;
            gray[7, 3] = 145;
            gray[8, 3] = 148;
            gray[9, 3] = 151;
            gray[10, 3] = 153;
            gray[11, 3] = 154;
            gray[12, 3] = 156;
            gray[13, 3] = 157;
            gray[14, 3] = 158;
            gray[15, 3] = 157;
            gray[16, 3] = 158;
            gray[17, 3] = 157;
            gray[18, 3] = 157;
            gray[19, 3] = 156;
            gray[20, 3] = 154;
            gray[21, 3] = 152;
            gray[22, 3] = 150;
            gray[23, 3] = 147;
            gray[24, 3] = 143;
            gray[25, 3] = 139;
            gray[26, 3] = 134;
            gray[27, 3] = 128;
            gray[28, 3] = 97;
            gray[29, 3] = 22;
            gray[30, 3] = 7;
            gray[0, 4] = 11;
            gray[1, 4] = 59;
            gray[2, 4] = 122;
            gray[3, 4] = 131;
            gray[4, 4] = 136;
            gray[5, 4] = 141;
            gray[6, 4] = 145;
            gray[7, 4] = 148;
            gray[8, 4] = 151;
            gray[9, 4] = 153;
            gray[10, 4] = 155;
            gray[11, 4] = 156;
            gray[12, 4] = 158;
            gray[13, 4] = 159;
            gray[14, 4] = 159;
            gray[15, 4] = 159;
            gray[16, 4] = 159;
            gray[17, 4] = 159;
            gray[18, 4] = 159;
            gray[19, 4] = 158;
            gray[20, 4] = 157;
            gray[21, 4] = 155;
            gray[22, 4] = 152;
            gray[23, 4] = 149;
            gray[24, 4] = 146;
            gray[25, 4] = 142;
            gray[26, 4] = 138;
            gray[27, 4] = 132;
            gray[28, 4] = 125;
            gray[29, 4] = 66;
            gray[30, 4] = 10;
            gray[0, 5] = 26;
            gray[1, 5] = 105;
            gray[2, 5] = 126;
            gray[3, 5] = 133;
            gray[4, 5] = 138;
            gray[5, 5] = 143;
            gray[6, 5] = 146;
            gray[7, 5] = 150;
            gray[8, 5] = 152;
            gray[9, 5] = 155;
            gray[10, 5] = 156;
            gray[11, 5] = 158;
            gray[12, 5] = 159;
            gray[13, 5] = 160;
            gray[14, 5] = 161;
            gray[15, 5] = 161;
            gray[16, 5] = 161;
            gray[17, 5] = 161;
            gray[18, 5] = 160;
            gray[19, 5] = 160;
            gray[20, 5] = 158;
            gray[21, 5] = 156;
            gray[22, 5] = 154;
            gray[23, 5] = 152;
            gray[24, 5] = 148;
            gray[25, 5] = 143;
            gray[26, 5] = 139;
            gray[27, 5] = 133;
            gray[28, 5] = 127;
            gray[29, 5] = 107;
            gray[30, 5] = 22;
            gray[0, 6] = 62;
            gray[1, 6] = 119;
            gray[2, 6] = 127;
            gray[3, 6] = 134;
            gray[4, 6] = 139;
            gray[5, 6] = 144;
            gray[6, 6] = 147;
            gray[7, 6] = 151;
            gray[8, 6] = 154;
            gray[9, 6] = 156;
            gray[10, 6] = 157;
            gray[11, 6] = 159;
            gray[12, 6] = 160;
            gray[13, 6] = 161;
            gray[14, 6] = 162;
            gray[15, 6] = 162;
            gray[16, 6] = 162;
            gray[17, 6] = 162;
            gray[18, 6] = 162;
            gray[19, 6] = 161;
            gray[20, 6] = 159;
            gray[21, 6] = 157;
            gray[22, 6] = 156;
            gray[23, 6] = 153;
            gray[24, 6] = 149;
            gray[25, 6] = 145;
            gray[26, 6] = 141;
            gray[27, 6] = 135;
            gray[28, 6] = 129;
            gray[29, 6] = 122;
            gray[30, 6] = 51;
            gray[0, 7] = 94;
            gray[1, 7] = 120;
            gray[2, 7] = 128;
            gray[3, 7] = 135;
            gray[4, 7] = 140;
            gray[5, 7] = 145;
            gray[6, 7] = 148;
            gray[7, 7] = 152;
            gray[8, 7] = 154;
            gray[9, 7] = 156;
            gray[10, 7] = 158;
            gray[11, 7] = 159;
            gray[12, 7] = 161;
            gray[13, 7] = 162;
            gray[14, 7] = 164;
            gray[15, 7] = 166;
            gray[16, 7] = 166;
            gray[17, 7] = 165;
            gray[18, 7] = 164;
            gray[19, 7] = 162;
            gray[20, 7] = 161;
            gray[21, 7] = 159;
            gray[22, 7] = 155;
            gray[23, 7] = 153;
            gray[24, 7] = 149;
            gray[25, 7] = 147;
            gray[26, 7] = 141;
            gray[27, 7] = 135;
            gray[28, 7] = 130;
            gray[29, 7] = 123;
            gray[30, 7] = 80;
            gray[0, 8] = 108;
            gray[1, 8] = 121;
            gray[2, 8] = 129;
            gray[3, 8] = 136;
            gray[4, 8] = 141;
            gray[5, 8] = 146;
            gray[6, 8] = 149;
            gray[7, 8] = 153;
            gray[8, 8] = 155;
            gray[9, 8] = 156;
            gray[10, 8] = 158;
            gray[11, 8] = 160;
            gray[12, 8] = 162;
            gray[13, 8] = 165;
            gray[14, 8] = 168;
            gray[15, 8] = 169;
            gray[16, 8] = 168;
            gray[17, 8] = 168;
            gray[18, 8] = 167;
            gray[19, 8] = 164;
            gray[20, 8] = 161;
            gray[21, 8] = 160;
            gray[22, 8] = 157;
            gray[23, 8] = 153;
            gray[24, 8] = 149;
            gray[25, 8] = 145;
            gray[26, 8] = 140;
            gray[27, 8] = 135;
            gray[28, 8] = 129;
            gray[29, 8] = 124;
            gray[30, 8] = 100;
            gray[0, 9] = 111;
            gray[1, 9] = 121;
            gray[2, 9] = 130;
            gray[3, 9] = 136;
            gray[4, 9] = 142;
            gray[5, 9] = 146;
            gray[6, 9] = 150;
            gray[7, 9] = 153;
            gray[8, 9] = 155;
            gray[9, 9] = 157;
            gray[10, 9] = 158;
            gray[11, 9] = 160;
            gray[12, 9] = 163;
            gray[13, 9] = 168;
            gray[14, 9] = 169;
            gray[15, 9] = 171;
            gray[16, 9] = 170;
            gray[17, 9] = 169;
            gray[18, 9] = 168;
            gray[19, 9] = 166;
            gray[20, 9] = 162;
            gray[21, 9] = 160;
            gray[22, 9] = 158;
            gray[23, 9] = 154;
            gray[24, 9] = 150;
            gray[25, 9] = 147;
            gray[26, 9] = 143;
            gray[27, 9] = 137;
            gray[28, 9] = 132;
            gray[29, 9] = 126;
            gray[30, 9] = 114;
            gray[0, 10] = 112;
            gray[1, 10] = 121;
            gray[2, 10] = 129;
            gray[3, 10] = 136;
            gray[4, 10] = 142;
            gray[5, 10] = 146;
            gray[6, 10] = 150;
            gray[7, 10] = 152;
            gray[8, 10] = 155;
            gray[9, 10] = 157;
            gray[10, 10] = 158;
            gray[11, 10] = 160;
            gray[12, 10] = 164;
            gray[13, 10] = 168;
            gray[14, 10] = 171;
            gray[15, 10] = 172;
            gray[16, 10] = 172;
            gray[17, 10] = 169;
            gray[18, 10] = 167;
            gray[19, 10] = 166;
            gray[20, 10] = 163;
            gray[21, 10] = 160;
            gray[22, 10] = 158;
            gray[23, 10] = 154;
            gray[24, 10] = 152;
            gray[25, 10] = 148;
            gray[26, 10] = 143;
            gray[27, 10] = 139;
            gray[28, 10] = 133;
            gray[29, 10] = 126;
            gray[30, 10] = 118;
            gray[0, 11] = 111;
            gray[1, 11] = 121;
            gray[2, 11] = 129;
            gray[3, 11] = 135;
            gray[4, 11] = 141;
            gray[5, 11] = 145;
            gray[6, 11] = 149;
            gray[7, 11] = 151;
            gray[8, 11] = 154;
            gray[9, 11] = 156;
            gray[10, 11] = 158;
            gray[11, 11] = 159;
            gray[12, 11] = 164;
            gray[13, 11] = 168;
            gray[14, 11] = 170;
            gray[15, 11] = 172;
            gray[16, 11] = 171;
            gray[17, 11] = 169;
            gray[18, 11] = 167;
            gray[19, 11] = 166;
            gray[20, 11] = 162;
            gray[21, 11] = 160;
            gray[22, 11] = 158;
            gray[23, 11] = 155;
            gray[24, 11] = 152;
            gray[25, 11] = 148;
            gray[26, 11] = 144;
            gray[27, 11] = 138;
            gray[28, 11] = 132;
            gray[29, 11] = 126;
            gray[30, 11] = 118;
            gray[0, 12] = 111;
            gray[1, 12] = 120;
            gray[2, 12] = 128;
            gray[3, 12] = 135;
            gray[4, 12] = 140;
            gray[5, 12] = 145;
            gray[6, 12] = 148;
            gray[7, 12] = 150;
            gray[8, 12] = 153;
            gray[9, 12] = 155;
            gray[10, 12] = 157;
            gray[11, 12] = 158;
            gray[12, 12] = 162;
            gray[13, 12] = 166;
            gray[14, 12] = 168;
            gray[15, 12] = 170;
            gray[16, 12] = 170;
            gray[17, 12] = 167;
            gray[18, 12] = 166;
            gray[19, 12] = 165;
            gray[20, 12] = 161;
            gray[21, 12] = 159;
            gray[22, 12] = 157;
            gray[23, 12] = 155;
            gray[24, 12] = 151;
            gray[25, 12] = 148;
            gray[26, 12] = 144;
            gray[27, 12] = 138;
            gray[28, 12] = 131;
            gray[29, 12] = 124;
            gray[30, 12] = 117;
            gray[0, 13] = 110;
            gray[1, 13] = 120;
            gray[2, 13] = 127;
            gray[3, 13] = 134;
            gray[4, 13] = 139;
            gray[5, 13] = 144;
            gray[6, 13] = 147;
            gray[7, 13] = 150;
            gray[8, 13] = 152;
            gray[9, 13] = 155;
            gray[10, 13] = 156;
            gray[11, 13] = 157;
            gray[12, 13] = 158;
            gray[13, 13] = 163;
            gray[14, 13] = 165;
            gray[15, 13] = 166;
            gray[16, 13] = 166;
            gray[17, 13] = 166;
            gray[18, 13] = 165;
            gray[19, 13] = 162;
            gray[20, 13] = 159;
            gray[21, 13] = 158;
            gray[22, 13] = 156;
            gray[23, 13] = 151;
            gray[24, 13] = 148;
            gray[25, 13] = 145;
            gray[26, 13] = 142;
            gray[27, 13] = 138;
            gray[28, 13] = 131;
            gray[29, 13] = 124;
            gray[30, 13] = 116;
            gray[0, 14] = 110;
            gray[1, 14] = 119;
            gray[2, 14] = 127;
            gray[3, 14] = 133;
            gray[4, 14] = 139;
            gray[5, 14] = 143;
            gray[6, 14] = 147;
            gray[7, 14] = 149;
            gray[8, 14] = 151;
            gray[9, 14] = 153;
            gray[10, 14] = 154;
            gray[11, 14] = 155;
            gray[12, 14] = 156;
            gray[13, 14] = 159;
            gray[14, 14] = 162;
            gray[15, 14] = 163;
            gray[16, 14] = 164;
            gray[17, 14] = 163;
            gray[18, 14] = 161;
            gray[19, 14] = 159;
            gray[20, 14] = 157;
            gray[21, 14] = 156;
            gray[22, 14] = 153;
            gray[23, 14] = 150;
            gray[24, 14] = 147;
            gray[25, 14] = 144;
            gray[26, 14] = 141;
            gray[27, 14] = 136;
            gray[28, 14] = 130;
            gray[29, 14] = 123;
            gray[30, 14] = 115;
            gray[0, 15] = 109;
            gray[1, 15] = 118;
            gray[2, 15] = 125;
            gray[3, 15] = 132;
            gray[4, 15] = 138;
            gray[5, 15] = 142;
            gray[6, 15] = 145;
            gray[7, 15] = 148;
            gray[8, 15] = 150;
            gray[9, 15] = 152;
            gray[10, 15] = 153;
            gray[11, 15] = 154;
            gray[12, 15] = 155;
            gray[13, 15] = 156;
            gray[14, 15] = 157;
            gray[15, 15] = 158;
            gray[16, 15] = 158;
            gray[17, 15] = 158;
            gray[18, 15] = 158;
            gray[19, 15] = 157;
            gray[20, 15] = 156;
            gray[21, 15] = 153;
            gray[22, 15] = 151;
            gray[23, 15] = 149;
            gray[24, 15] = 146;
            gray[25, 15] = 143;
            gray[26, 15] = 139;
            gray[27, 15] = 134;
            gray[28, 15] = 129;
            gray[29, 15] = 122;
            gray[30, 15] = 113;
            gray[0, 16] = 107;
            gray[1, 16] = 116;
            gray[2, 16] = 124;
            gray[3, 16] = 131;
            gray[4, 16] = 136;
            gray[5, 16] = 140;
            gray[6, 16] = 144;
            gray[7, 16] = 146;
            gray[8, 16] = 148;
            gray[9, 16] = 150;
            gray[10, 16] = 152;
            gray[11, 16] = 153;
            gray[12, 16] = 154;
            gray[13, 16] = 154;
            gray[14, 16] = 154;
            gray[15, 16] = 155;
            gray[16, 16] = 156;
            gray[17, 16] = 156;
            gray[18, 16] = 156;
            gray[19, 16] = 155;
            gray[20, 16] = 154;
            gray[21, 16] = 152;
            gray[22, 16] = 149;
            gray[23, 16] = 148;
            gray[24, 16] = 145;
            gray[25, 16] = 141;
            gray[26, 16] = 138;
            gray[27, 16] = 133;
            gray[28, 16] = 127;
            gray[29, 16] = 119;
            gray[30, 16] = 106;
            gray[0, 17] = 104;
            gray[1, 17] = 114;
            gray[2, 17] = 122;
            gray[3, 17] = 128;
            gray[4, 17] = 134;
            gray[5, 17] = 138;
            gray[6, 17] = 142;
            gray[7, 17] = 144;
            gray[8, 17] = 147;
            gray[9, 17] = 148;
            gray[10, 17] = 150;
            gray[11, 17] = 151;
            gray[12, 17] = 152;
            gray[13, 17] = 153;
            gray[14, 17] = 153;
            gray[15, 17] = 153;
            gray[16, 17] = 153;
            gray[17, 17] = 153;
            gray[18, 17] = 153;
            gray[19, 17] = 152;
            gray[20, 17] = 151;
            gray[21, 17] = 150;
            gray[22, 17] = 148;
            gray[23, 17] = 146;
            gray[24, 17] = 143;
            gray[25, 17] = 140;
            gray[26, 17] = 136;
            gray[27, 17] = 131;
            gray[28, 17] = 124;
            gray[29, 17] = 116;
            gray[30, 17] = 95;
            gray[0, 18] = 97;
            gray[1, 18] = 111;
            gray[2, 18] = 119;
            gray[3, 18] = 126;
            gray[4, 18] = 131;
            gray[5, 18] = 136;
            gray[6, 18] = 139;
            gray[7, 18] = 142;
            gray[8, 18] = 144;
            gray[9, 18] = 146;
            gray[10, 18] = 148;
            gray[11, 18] = 148;
            gray[12, 18] = 150;
            gray[13, 18] = 150;
            gray[14, 18] = 151;
            gray[15, 18] = 151;
            gray[16, 18] = 151;
            gray[17, 18] = 151;
            gray[18, 18] = 151;
            gray[19, 18] = 150;
            gray[20, 18] = 149;
            gray[21, 18] = 147;
            gray[22, 18] = 146;
            gray[23, 18] = 143;
            gray[24, 18] = 140;
            gray[25, 18] = 136;
            gray[26, 18] = 133;
            gray[27, 18] = 129;
            gray[28, 18] = 122;
            gray[29, 18] = 114;
            gray[30, 18] = 77;
            gray[0, 19] = 74;
            gray[1, 19] = 107;
            gray[2, 19] = 115;
            gray[3, 19] = 122;
            gray[4, 19] = 128;
            gray[5, 19] = 132;
            gray[6, 19] = 136;
            gray[7, 19] = 140;
            gray[8, 19] = 141;
            gray[9, 19] = 143;
            gray[10, 19] = 144;
            gray[11, 19] = 145;
            gray[12, 19] = 147;
            gray[13, 19] = 148;
            gray[14, 19] = 148;
            gray[15, 19] = 148;
            gray[16, 19] = 149;
            gray[17, 19] = 148;
            gray[18, 19] = 148;
            gray[19, 19] = 147;
            gray[20, 19] = 146;
            gray[21, 19] = 145;
            gray[22, 19] = 143;
            gray[23, 19] = 141;
            gray[24, 19] = 137;
            gray[25, 19] = 134;
            gray[26, 19] = 130;
            gray[27, 19] = 125;
            gray[28, 19] = 119;
            gray[29, 19] = 110;
            gray[30, 19] = 43;
            gray[0, 20] = 34;
            gray[1, 20] = 99;
            gray[2, 20] = 111;
            gray[3, 20] = 118;
            gray[4, 20] = 123;
            gray[5, 20] = 129;
            gray[6, 20] = 133;
            gray[7, 20] = 136;
            gray[8, 20] = 139;
            gray[9, 20] = 139;
            gray[10, 20] = 140;
            gray[11, 20] = 141;
            gray[12, 20] = 143;
            gray[13, 20] = 145;
            gray[14, 20] = 145;
            gray[15, 20] = 146;
            gray[16, 20] = 145;
            gray[17, 20] = 145;
            gray[18, 20] = 145;
            gray[19, 20] = 144;
            gray[20, 20] = 143;
            gray[21, 20] = 141;
            gray[22, 20] = 140;
            gray[23, 20] = 137;
            gray[24, 20] = 134;
            gray[25, 20] = 131;
            gray[26, 20] = 127;
            gray[27, 20] = 121;
            gray[28, 20] = 115;
            gray[29, 20] = 89;
            gray[30, 20] = 15;
            gray[0, 21] = 11;
            gray[1, 21] = 69;
            gray[2, 21] = 104;
            gray[3, 21] = 112;
            gray[4, 21] = 119;
            gray[5, 21] = 124;
            gray[6, 21] = 129;
            gray[7, 21] = 132;
            gray[8, 21] = 134;
            gray[9, 21] = 135;
            gray[10, 21] = 136;
            gray[11, 21] = 137;
            gray[12, 21] = 139;
            gray[13, 21] = 140;
            gray[14, 21] = 141;
            gray[15, 21] = 142;
            gray[16, 21] = 142;
            gray[17, 21] = 142;
            gray[18, 21] = 142;
            gray[19, 21] = 140;
            gray[20, 21] = 139;
            gray[21, 21] = 138;
            gray[22, 21] = 136;
            gray[23, 21] = 134;
            gray[24, 21] = 131;
            gray[25, 21] = 127;
            gray[26, 21] = 122;
            gray[27, 21] = 116;
            gray[28, 21] = 109;
            gray[29, 21] = 42;
            gray[30, 21] = 8;
            gray[0, 22] = 6;
            gray[1, 22] = 22;
            gray[2, 22] = 87;
            gray[3, 22] = 106;
            gray[4, 22] = 113;
            gray[5, 22] = 118;
            gray[6, 22] = 123;
            gray[7, 22] = 127;
            gray[8, 22] = 130;
            gray[9, 22] = 130;
            gray[10, 22] = 132;
            gray[11, 22] = 133;
            gray[12, 22] = 135;
            gray[13, 22] = 136;
            gray[14, 22] = 137;
            gray[15, 22] = 137;
            gray[16, 22] = 137;
            gray[17, 22] = 138;
            gray[18, 22] = 137;
            gray[19, 22] = 137;
            gray[20, 22] = 135;
            gray[21, 22] = 134;
            gray[22, 22] = 131;
            gray[23, 22] = 129;
            gray[24, 22] = 126;
            gray[25, 22] = 122;
            gray[26, 22] = 117;
            gray[27, 22] = 111;
            gray[28, 22] = 74;
            gray[29, 22] = 12;
            gray[30, 22] = 5;
        }


        private void bt_2d_array1_Click(object sender, EventArgs e)
        {
            //畫二維矩陣 + 輪廓
            g.Clear(Color.White);

            Pen p = new Pen(Color.Red, 10);  // 設定畫筆為紅色、粗細為 10 點。
            SolidBrush sb = new SolidBrush(Color.Blue);

            int[,] gray = new int[31, 23];

            fillup_data1(gray);

            int dd = 20;
            int xx;
            int yy;
            int width = dd * 31;
            int height = dd * 23;

            byte aa = 255;
            byte rr = 0;
            byte gg = 0;
            byte bb = 0;

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //Color p = Color.FromName("SlateBlue");
                    /*
                    Color p ;
                    p.A = (byte)(xx % 255);
                    p.R = (byte)(xx % 127 + 127);
                    p.G = (byte)(xx % 127);
                    p.B = (byte)(xx % 63);
                    */

                    //獲取像素的ＲＧＢ顏色值
                    //srcColor = srcBitmap.GetPixel(x, y);
                    //byte temp = (byte)(srcColor.R * .299 + srcColor.G * .587 + srcColor.B * .114);

                    //byte temp = (byte)((byte)(xx % 255) + (byte)(xx % 127 + 127) + (byte)(xx % 63));

                    //設置像素的ＲＧＢ顏色值
                    rr = (byte)gray[xx / dd, yy / dd];
                    gg = (byte)gray[xx / dd, yy / dd];
                    bb = (byte)gray[xx / dd, yy / dd];
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                }
            }

            //以上為 畫二維矩陣
            //以下為 畫輪廓

            //二值化 把邊框畫出來 ST

            int row = gray.Rank;//獲取行數
            int col1 = gray.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int col2 = gray.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int num1 = gray.Length;//獲取整個二維陣列的長度，即所有元 的個數

            richTextBox1.Text += "row = " + row.ToString() + "\n";
            richTextBox1.Text += "col1 = " + col1.ToString() + "\n";
            richTextBox1.Text += "col2 = " + col2.ToString() + "\n";
            richTextBox1.Text += "num1 = " + num1.ToString() + "\n";

            int total_rows = gray.GetUpperBound(0) + 1;
            richTextBox1.Text += "total_rows = " + total_rows.ToString() + "\n";

            int w = gray.GetUpperBound(0) + 1;
            int h = gray.GetLength(1);
            int i;
            int j;

            //二值化
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    //richTextBox1.Text += gray[i, j] + "\t";


                    if (gray[i, j] > 150)
                        gray[i, j] = 220;
                    else
                        gray[i, j] = 30;
                }
                //richTextBox1.Text += "\n";
            }
            //richTextBox1.Text += "\n";

            //中間挖空
            int[,] gray_new2 = new int[w, h];
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    gray_new2[i, j] = gray[i, j];

                    //不在邊界的點
                    if ((i > 0) && (i < (w - 1)) && (j > 0) && (j < (h - 1)))
                    {
                        if (gray[i, j] < 200)
                            continue;

                        //四鄰皆有者
                        if ((gray[i + 1, j] >= 200) && (gray[i - 1, j] >= 200) && (gray[i, j + 1] >= 200) && (gray[i, j - 1] >= 200))
                        {
                            gray_new2[i, j] = 0;
                        }
                    }
                }
            }

            find_connected_points(gray_new2);

            richTextBox1.Text += "point array:\n";
            richTextBox1.Text += "len = " + Points.Count.ToString() + "\n";

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);

            int len = Points.Count;
            int ratio = 20;
            for (i = 0; i < len - 1; i++)
            {
                g.DrawLine(new Pen(Color.Red, 5), Points[i].X * ratio, Points[i].Y * ratio, Points[i + 1].X * ratio, Points[i + 1].Y * ratio);

                //richTextBox1.Text += (Points[i].X * ratio).ToString() + " " + (Points[i].Y * ratio).ToString() + " " + (Points[i + 1].X * ratio).ToString() + " " + (Points[i + 1].Y * ratio).ToString() + "\n";

            }
            //二值化 把邊框畫出來 SP

            pictureBox1.Image = bitmap1;
        }

        void find_connected_points(int[,] array)
        {
            Points.Clear();

            int row = array.Rank;//獲取行數
            int col1 = array.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int col2 = array.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int num1 = array.Length;//獲取整個二維陣列的長度，即所有元 的個數

            richTextBox1.Text += "row = " + row.ToString() + "\n";
            richTextBox1.Text += "col1 = " + col1.ToString() + "\n";
            richTextBox1.Text += "col2 = " + col2.ToString() + "\n";
            richTextBox1.Text += "num1 = " + num1.ToString() + "\n";

            int total_rows = array.GetUpperBound(0) + 1;
            richTextBox1.Text += "total_rows = " + total_rows.ToString() + "\n";

            int w = array.GetUpperBound(0) + 1;
            int h = array.GetLength(1);
            int i;
            int j;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    richTextBox1.Text += array[i, j] + "\t";

                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";

            int i_st = 0;
            int j_st = 0;
            int total_points = 0;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {

                    if (array[i, j] >= 200)
                    {
                        total_points++;
                    }
                }
            }
            richTextBox1.Text += "共找到 : " + total_points.ToString() + " 點\n";


            bool flag_got_break = false;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {

                    if (array[i, j] >= 200)
                    {
                        richTextBox1.Text += "找到 i = " + i.ToString() + ", j = " + j.ToString() + "\n";
                        i_st = i;
                        j_st = j;
                        flag_got_break = true;
                        break;
                    }


                }
                if (flag_got_break == true)
                    break;
            }
            richTextBox1.Text += "找到起始點 i_st = " + i_st.ToString() + ", j_st = " + j_st.ToString() + "\n";

            int i_next = i_st;
            int j_next = j_st;
            Points.Add(new Point(i_next, j_next));

            for (i = 0; i < total_points; i++)
            {
                i_st = i_next;
                j_st = j_next;
                FindNeighborPoint(array, i_st, j_st, out i_next, out j_next);
                Points.Add(new Point(i_next, j_next));
                richTextBox1.Text += "i_next = " + i_next.ToString() + "\t" + "j_next = " + j_next.ToString() + "\n";
                array[i_next, j_next] = 0;
            }
        }

        void FindNeighborPoint(int[,] array, int i_st, int j_st, out int i_next, out int j_next)
        {
            //int i;
            int len = array.Length;
            i_next = int.MaxValue;
            j_next = int.MinValue;

            int i = 0;
            int j = 0;

            //richTextBox1.Text += "1111 i_st = " + i_st.ToString() + ", j_st = " + j_st.ToString() + "\n";
            //richTextBox1.Text += "2222 i = " + i.ToString() + ", j = " + j.ToString() + "\n";

            int w = array.GetUpperBound(0) + 1;
            int h = array.GetLength(1);


            //richTextBox1.Text += "上";
            i = i_st;
            j = j_st - 1;

            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到";
                i_next = i;
                j_next = j;
                return;
            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "右上";
            i = i_st + 1;
            j = j_st - 1;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "右";
            i = i_st + 1;
            j = j_st;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "右下";
            i = i_st + 1;
            j = j_st + 1;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "下";
            i = i_st;
            j = j_st + 1;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "左下";
            i = i_st - 1;
            j = j_st + 1;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "左";
            i = i_st - 1;
            j = j_st;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "左上";
            i = i_st - 1;
            j = j_st - 1;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

        }

        private void bt_2d_array2_Click(object sender, EventArgs e)
        {

        }

        private void bt_2d_array3_Click(object sender, EventArgs e)
        {

        }

        int dd = 20;
        int cx = 360;
        int cy = 360;
        private void timer2_Tick(object sender, EventArgs e)
        {
            cx += dd;
            cy += dd;
            if (cx > 721)
                cx = dd;
            if (cy > 721)
                cy = dd;
            draw_contour(cx, cy);
        }


    }

    /// <summary>
    /// DrawingCurve 的摘要說明
    /// </summary>
    public class DrawingCurve
    {
        public int intXLong = 800;   //圖片大小 長
        public int intYLong = 600;   //圖片大小 高
        public int intXMultiple = 1;    //零刻度的值 X
        public int intYMultiple = 0;    //零刻度的值 Y
        public int intXMax = 12;    //最大刻度(點數) X
        public int intYMax = 30;    //最大刻度(點數) Y

        public int intLeft = 50;   //左邊距
        public int intRight = 120; //右邊距
        public int intTop = 30;    //上邊距
        public int intEnd = 50;    //下邊距

        public string strXText = "時間(單位:月)";    //單位 X
        public string strYText = "數量(單位:個)";    //單位 Y
        public string strTitle = "趨勢線圖";    //標題
        public DataTable tbData;    //要統計的數據


        private int intXScale = 30;    //一刻度長度 X
        private int intYScale = 30;    //一刻度高度 Y
        //private int intX = 0;   //0點 X坐標
        //private int intY = 0;   //0點 Y坐標
        public int intData = 0;    //記錄數

        public DrawingCurve()
        {

            intXScale = (intXLong - intLeft - intRight) / (intXMax + 1);//一刻度長度 X
            intYScale = (intYLong - intTop - intEnd) / (intYMax + 1);//一刻度高度 Y

            //intX = intXLong - intLeft;   //0點 X坐標
            //intY = intYLong - intEnd;   //0點 Y坐標
        }

        public Bitmap DrawingImg()
        {

            Bitmap img = new Bitmap(intXLong, intYLong); //圖片大小
            Graphics g = Graphics.FromImage(img);
            g.Clear(Color.Snow);
            g.DrawString(strTitle, new Font("宋體", 14), Brushes.Black, new Point(5, 5));
            g.DrawLine(new Pen(Color.Black, 2), intLeft, intYLong - intEnd, intXLong - intRight, intYLong - intEnd); //繪製橫向
            g.DrawLine(new Pen(Color.Black, 2), intLeft, intTop, intLeft, intYLong - intEnd);   //繪製縱向

            //繪製縱坐標
            g.DrawString(strYText, new Font("宋體", 12), Brushes.Black, new Point(intLeft, intTop));//Y 單位
            Point p1 = new Point(intLeft - 10, intYLong - intEnd);
            for (int j = 0; j <= intYMax; j++)
            {
                p1.Y = intYLong - intEnd - j * intYScale;
                Point pt = new Point(p1.X + 10, p1.Y);
                //繪製縱坐標的刻度和直線
                g.DrawLine(Pens.Black, pt, new Point(p1.X + 15, p1.Y));
                //繪製縱坐標的文字說明
                g.DrawString(Convert.ToString(j + intYMultiple), new Font("宋體", 12), Brushes.Black, new Point(p1.X - 25, p1.Y - 8));
            }

            //繪製橫坐標
            g.DrawString(strXText, new Font("宋體", 12), Brushes.Black, new Point(intXLong - intRight, intYLong - intEnd));//X 單位
            Point p = new Point(intLeft, intYLong - intEnd);
            for (int i = 0; i < intXMax; i++)
            {
                p.X = intLeft + i * intXScale;
                //繪製橫坐標刻度和直線
                g.DrawLine(Pens.Black, p, new Point(p.X, p.Y - 5));
                //繪製橫坐標的文字說明
                g.DrawString(Convert.ToString(i + intXMultiple), new Font("宋體", 12), Brushes.Black, p);
            }

            intData = tbData.Rows.Count;
            if (intData > 0)
            {
                //趨勢線圖
                for (int i = 0; i < intData - 1; i++)
                {
                    DataRow Row1 = tbData.Rows[i];
                    DataRow Row2 = tbData.Rows[i + 1];
                    //定義起點
                    Point rec = new Point(Convert.ToInt32(intLeft + ((TurnNumber(Row1[0].ToString()) - intXMultiple) * intXScale)), Convert.ToInt32(intYLong - intEnd - (TurnNumber(Row1[1].ToString()) - intYMultiple) * intYScale));
                    //定義終點
                    Point dec = new Point(Convert.ToInt32(intLeft + ((TurnNumber(Row2[0].ToString()) - intXMultiple) * intXScale)), Convert.ToInt32(intYLong - intEnd - (TurnNumber(Row2[1].ToString()) - intYMultiple) * intYScale));
                    //繪製趨勢折線
                    g.DrawLine(new Pen(Color.Red), rec, dec);
                }
            }
            return img;
        }

        //转换数字

        private double TurnNumber(string str)
        {

            double dubReturn;

            try
            {

                dubReturn = Convert.ToDouble(str);

            }

            catch
            {

                dubReturn = 0;

            }

            return dubReturn;
        }
    }



    public class PieChart
    {
        public PieChart()
        {
        }
        public void Render(string title, string subTitle, int width, int height, DataSet chartData, string target)
        {
            const int SIDE_LENGTH = 400;
            const int PIE_DIAMETER = 200;
            DataTable dt = chartData.Tables[0];

            //通過輸入參數，取得餅圖中的總基數
            float sumData = 0;
            foreach (DataRow dr in dt.Rows)
            {
                sumData += Convert.ToSingle(dr[1]);
            }
            //產生一個image對象，並由此產生一個Graphics對象
            Bitmap bm = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(bm);
            //設置對象g的屬性
            g.ScaleTransform((Convert.ToSingle(width)) / SIDE_LENGTH, (Convert.ToSingle(height)) / SIDE_LENGTH);
            g.SmoothingMode = SmoothingMode.Default;
            g.TextRenderingHint = TextRenderingHint.AntiAlias;

            //畫布和邊的設定
            g.Clear(Color.White);
            g.DrawRectangle(Pens.Black, 0, 0, SIDE_LENGTH - 1, SIDE_LENGTH - 1);
            //畫餅圖標題
            g.DrawString(title, new Font("Tahoma", 24), Brushes.Black, new PointF(5, 5));
            //畫餅圖的圖例
            g.DrawString(subTitle, new Font("Tahoma", 14), Brushes.Black, new PointF(7, 35));
            //畫餅圖
            float curAngle = 0;
            float totalAngle = 0;
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                curAngle = Convert.ToSingle(dt.Rows[i][1]) / sumData * 360;

                g.FillPie(new SolidBrush(ChartUtil.GetChartItemColor(i)), 100, 65, PIE_DIAMETER, PIE_DIAMETER, totalAngle, curAngle);
                g.DrawPie(Pens.Black, 100, 65, PIE_DIAMETER, PIE_DIAMETER, totalAngle, curAngle);
                totalAngle += curAngle;
            }
            //畫圖例框及其文字
            g.DrawRectangle(Pens.Black, 200, 300, 199, 99);
            g.DrawString("Legend", new Font("Tahoma", 12, FontStyle.Bold), Brushes.Black, new PointF(200, 300));

            //畫圖例各項
            PointF boxOrigin = new PointF(210, 330);
            PointF textOrigin = new PointF(235, 326);
            float percent = 0;
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                g.FillRectangle(new SolidBrush(ChartUtil.GetChartItemColor(i)), boxOrigin.X, boxOrigin.Y, 20, 10);
                g.DrawRectangle(Pens.Black, boxOrigin.X, boxOrigin.Y, 20, 10);
                percent = Convert.ToSingle(dt.Rows[i][1]) / sumData * 100;
                g.DrawString(dt.Rows[i][0].ToString() + " - " + dt.Rows[i][1].ToString() + " (" + percent.ToString("0") + "%)", new Font("Tahoma", 10), Brushes.Black, textOrigin);
                boxOrigin.Y += 15;
                textOrigin.Y += 15;
            }
            //通過Response.OutputStream，將圖形的內容發送到瀏覽器
            bm.Save(target, ImageFormat.Gif);
            //回收資源
            bm.Dispose();
        }
    }

    //畫條形圖
    public class BarChart
    {
        public BarChart()
        {
        }

        /// <summary>
        /// 画条形图方法
        /// </summary>
        /// <param name="title">大标题</param>
        /// <param name="subTitle">小标题</param>
        /// <param name="width">宽度</param>
        /// <param name="height">高度</param>
        /// <param name="chartData">DataSet数据源</param>
        /// <param name="target">系统二进制</param>
        public void Render(string title, string subTitle, int width, int height, DataSet chartData, string target)
        {
            const int SIDE_LENGTH = 400;
            const int CHART_TOP = 75;
            const int CHART_HEIGHT = 200;
            const int CHART_LEFT = 50;
            const int CHART_WIDTH = 300;
            DataTable dt = chartData.Tables[0];

            //計算最高的點
            float highPoint = 0;
            foreach (DataRow dr in dt.Rows)
            {
                if (highPoint < Convert.ToSingle(dr[1]))
                {
                    highPoint = Convert.ToSingle(dr[1]);
                }
            }
            //建立一個Graphics對象實例
            Bitmap bm = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(bm);
            //設置條圖圖形和文字屬性
            g.ScaleTransform((Convert.ToSingle(width)) / SIDE_LENGTH, (Convert.ToSingle(height)) / SIDE_LENGTH);
            g.SmoothingMode = SmoothingMode.Default;
            g.TextRenderingHint = TextRenderingHint.AntiAlias;

            //設定畫布和邊
            g.Clear(Color.White);
            g.DrawRectangle(Pens.Black, 0, 0, SIDE_LENGTH - 1, SIDE_LENGTH - 1);
            //畫大標題
            g.DrawString(title, new Font("Tahoma", 24), Brushes.Black, new PointF(5, 5));
            //畫小標題
            g.DrawString(subTitle, new Font("Tahoma", 14), Brushes.Black, new PointF(7, 35));
            //畫條形圖
            float barWidth = CHART_WIDTH / (dt.Rows.Count * 2);
            PointF barOrigin = new PointF(CHART_LEFT + (barWidth / 2), 0);
            float barHeight = dt.Rows.Count;
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                barHeight = Convert.ToSingle(dt.Rows[i][1]) * 200 / highPoint;
                barOrigin.Y = CHART_TOP + CHART_HEIGHT - barHeight;
                g.FillRectangle(new SolidBrush(ChartUtil.GetChartItemColor(i)), barOrigin.X, barOrigin.Y, barWidth, barHeight);
                barOrigin.X = barOrigin.X + (barWidth * 2);
            }
            //設置邊
            g.DrawLine(new Pen(Color.Black, 2), new Point(CHART_LEFT, CHART_TOP), new Point(CHART_LEFT, CHART_TOP + CHART_HEIGHT));
            g.DrawLine(new Pen(Color.Black, 2), new Point(CHART_LEFT, CHART_TOP + CHART_HEIGHT), new Point(CHART_LEFT + CHART_WIDTH, CHART_TOP + CHART_HEIGHT));
            //畫圖例框和文字
            g.DrawRectangle(new Pen(Color.Black, 1), 200, 300, 199, 99);
            g.DrawString("Legend", new Font("Tahoma", 12, FontStyle.Bold), Brushes.Black, new PointF(200, 300));

            //畫圖例
            PointF boxOrigin = new PointF(210, 330);
            PointF textOrigin = new PointF(235, 326);
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                g.FillRectangle(new SolidBrush(ChartUtil.GetChartItemColor(i)), boxOrigin.X, boxOrigin.Y, 20, 10);
                g.DrawRectangle(Pens.Black, boxOrigin.X, boxOrigin.Y, 20, 10);
                g.DrawString(dt.Rows[i][0].ToString() + " - " + dt.Rows[i][1].ToString(), new Font("Tahoma", 10), Brushes.Black, textOrigin);
                boxOrigin.Y += 15;
                textOrigin.Y += 15;
            }
            //輸出圖形
            bm.Save(target, ImageFormat.Gif);

            //資源回收
            bm.Dispose();
        }
    }
    public class ChartUtil
    {
        public ChartUtil()
        {
        }
        public static Color GetChartItemColor(int itemIndex)
        {
            Color selectedColor;
            switch (itemIndex)
            {
                case 0:
                    selectedColor = Color.Blue;
                    break;
                case 1:
                    selectedColor = Color.Red;
                    break;
                case 2:
                    selectedColor = Color.Yellow;
                    break;
                case 3:
                    selectedColor = Color.Purple;
                    break;
                case 4:
                    selectedColor = Color.Green;
                    break;
                case 5:
                    selectedColor = Color.CadetBlue;
                    break;
                case 6:
                    selectedColor = Color.Black;
                    break;
                case 7:
                    selectedColor = Color.BlanchedAlmond;
                    break;
                case 8:
                    selectedColor = Color.BlueViolet;
                    break;
                case 9:
                    selectedColor = Color.Brown;
                    break;
                case 10:
                    selectedColor = Color.BurlyWood;
                    break;
                case 11:
                    selectedColor = Color.Coral;
                    break;
                case 12:
                    selectedColor = Color.Chartreuse;
                    break;
                default:
                    selectedColor = Color.Green;
                    break;
            }
            return selectedColor;
        }
    }

    public class Curve2D
    {
        private Graphics g; //Graphics 類提供將對象繪製到顯示設備的方法
        private Bitmap objBitmap; //位圖對象
        private float fltWidth = 480; //圖像寬度
        private float fltHeight = 248; //圖像高度
        private float fltXSlice = 50; //X軸刻度寬度
        private float fltYSlice = 50; //Y軸刻度寬度
        private float fltYSliceValue = 20; //Y軸刻度的數值寬度
        private float fltYSliceBegin = 0; //Y軸刻度開始值
        private float fltTension = 0.5f;
        private string strTitle = "曲線圖"; //標題
        private string strXAxisText = "月份"; //X軸說明文字
        private string strYAxisText = "萬元"; //Y軸說明文字
        private string[] strsKeys = new string[] { "一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月" }; //鍵
        private float[] fltsValues = new float[] { 20.0f, 30.0f, 50.0f, 55.4f, 21.6f, 12.8f, 99.5f, 36.4f, 78.2f, 56.4f, 45.8f, 66.5f, 99.5f, 36.4f, 78.2f, 56.4f, 45.8f, 66.5f, 20.0f, 30.0f, 50.0f, 55.4f, 21.6f, 12.8f }; //值
        private Color clrBgColor = Color.Snow; //背景色
        private Color clrTextColor = Color.Black; //文字顏色
        private Color clrBorderColor = Color.Black; //整體邊框顏色
        private Color clrAxisColor = Color.Black; //軸線顏色
        private Color clrAxisTextColor = Color.Black; //軸說明文字顏色
        private Color clrSliceTextColor = Color.Black; //刻度文字顏色
        private Color clrSliceColor = Color.Black; //刻度顏色
        private Color[] clrsCurveColors = new Color[] { Color.Red, Color.Blue }; //曲線顏色
        private float fltXSpace = 100f; //圖像左右距離邊緣距離
        private float fltYSpace = 100f; //圖像上下距離邊緣距離
        private int intFontSize = 9; //字體大小號數
        private float fltXRotateAngle = 30f; //X軸文字旋轉角度
        private float fltYRotateAngle = 0f; //Y軸文字旋轉角度
        private int intCurveSize = 2; //曲線線條大小
        private int intFontSpace = 0; //intFontSpace 是字體大小和距離調整出來的一個比較適合的數字
        #region 公共屬性
        /// <summary>

        /// 圖像的寬度
        /// </summary>
        public float Width
        {
            set
            {
                if (value < 100)
                {
                    fltWidth = 100;
                }
                else
                {
                    fltWidth = value;
                }
            }
            get
            {
                if (fltWidth <= 100)
                {
                    return 100;
                }
                else
                {
                    return fltWidth;
                }
            }
        }
        /// <summary>
        /// 圖像的高度
        /// </summary>
        public float Height
        {
            set
            {
                if (value < 100)
                {
                    fltHeight = 100;
                }
                else
                {
                    fltHeight = value;
                }
            }
            get
            {
                if (fltHeight <= 100)
                {
                    return 100;
                }
                else
                {
                    return fltHeight;
                }
            }
        }

        /// <summary>
        /// X軸刻度寬度
        /// </summary>
        public float XSlice
        {
            set { fltXSlice = value; }
            get { return fltXSlice; }
        }
        /// <summary>
        /// Y軸刻度寬度
        /// </summary>
        public float YSlice
        {
            set { fltYSlice = value; }
            get { return fltYSlice; }
        }

        /// <summary>
        /// Y軸刻度的數值寬度
        /// </summary>


        public float YSliceValue
        {
            set { fltYSliceValue = value; }
            get { return fltYSliceValue; }
        }
        /// <summary>
        /// Y軸刻度開始值
        /// </summary>
        public float YSliceBegin
        {
            set { fltYSliceBegin = value; }
            get { return fltYSliceBegin; }
        }
        /// <summary>
        /// 張力系數
        /// </summary>
        public float Tension
        {
            set
            {
                if (value < 0.0f && value > 1.0f)
                {
                    fltTension = 0.5f;
                }
                else
                {
                    fltTension = value;
                }
            }
            get
            {
                return fltTension;
            }
        }
        /// <summary>
        /// 標題
        /// </summary>
        public string Title
        {
            set { strTitle = value; }
            get { return strTitle; }
        }
        /// <summary>
        /// 鍵，X軸數據
        /// </summary>
        public string[] Keys
        {
            set
            {
                strsKeys = value;
            }
            get { return strsKeys; }
        }
        /// <summary>
        /// 值，Y軸數據
        /// </summary>
        public float[] Values
        {
            set { fltsValues = value; }
            get
            {
                return fltsValues;
            }
        }
        /// <summary>
        /// 背景色
        /// </summary>
        public Color BgColor
        {
            set
            {
                clrBgColor = value;
            }
            get { return clrBgColor; }
        }
        /// <summary>
        /// 文字顏色
        /// </summary>
        public Color TextColor
        {
            set { clrTextColor = value; }
            get { return clrTextColor; }
        }
        /// <summary>
        /// 整體邊框顏色
        /// </summary>
        public Color BorderColor
        {
            set { clrBorderColor = value; }
            get { return clrBorderColor; }
        }
        /// <summary>
        /// 軸線顏色
        /// </summary>
        public Color AxisColor
        {
            set
            {
                clrAxisColor = value;
            }
            get { return clrAxisColor; }
        }

        /// <summary>
        /// X軸說明文字
        /// </summary>
        public string XAxisText
        {
            set { strXAxisText = value; }
            get { return strXAxisText; }
        }
        /// <summary>
        /// Y軸說明文字
        /// </summary>
        public string YAxisText
        {
            set { strYAxisText = value; }
            get { return strYAxisText; }
        }
        /// <summary>
        /// 軸說明文字顏色
        /// </summary>
        public Color AxisTextColor
        {
            set
            {
                clrAxisTextColor = value;
            }
            get { return clrAxisTextColor; }
        }
        /// <summary>
        /// 刻度文字顏色
        /// </summary>
        public Color SliceTextColor
        {
            set
            {
                clrSliceTextColor = value;
            }
            get { return clrSliceTextColor; }
        }
        /// <summary>
        /// 刻度顏色
        /// </summary>
        public Color SliceColor
        {
            set { clrSliceColor = value; }
            get { return clrSliceColor; }
        }
        /// <summary>
        /// 曲線顏色
        /// </summary>
        public Color[] CurveColors
        {
            set { clrsCurveColors = value; }
            get
            {
                return clrsCurveColors;
            }
        }
        /// <summary>
        /// X軸文字旋轉角度
        /// </summary>
        public float XRotateAngle
        {
            get { return fltXRotateAngle; }
            set { fltXRotateAngle = value; }
        }
        /// <summary>
        /// Y軸文字旋轉角度
        /// </summary>
        public float YRotateAngle
        {
            get
            {
                return fltYRotateAngle;
            }
            set { fltYRotateAngle = value; }
        }

        /// <summary>
        /// 圖像左右距離邊緣距離
        /// </summary>
        public float XSpace
        {
            get
            {
                return fltXSpace;
            }
            set { fltXSpace = value; }
        }

        /// <summary>
        /// 圖像上下距離邊緣距離
        /// </summary>
        public float YSpace
        {
            get { return fltYSpace; }
            set { fltYSpace = value; }
        }
        /// <summary>
        /// 字體大小號數
        /// </summary>
        public int FontSize
        {
            get { return intFontSize; }
            set { intFontSize = value; }
        }

        /// <summary>
        /// 曲線線條大小
        /// </summary>
        public int CurveSize
        {
            get
            {
                return intCurveSize;
            }
            set { intCurveSize = value; }
        }

        #endregion
        /// <summary>
        /// 自動根據參數調整圖像大小
        /// 根據數據自動計算邊距和字體等
        /// </summary>
        public void Fit()
        {
            //計算字體距離
            intFontSpace = FontSize + 5;
            //計算圖像邊距

            float fltSpace = Math.Min(Width / 6, Height / 6);
            XSpace = fltSpace;
            YSpace = fltSpace;
            //計算X軸刻度寬度
            XSlice = (Width - 2 * XSpace) / (Keys.Length - 1);
            //計算Y軸刻度寬度和Y軸刻度開始值
            float fltMinValue = 0;
            float fltMaxValue = 0;
            for (int i = 0; i < Values.Length; i++)
            {
                if (Values[i] < fltMinValue)
                {
                    fltMinValue = Values[i];
                }
                else if (Values[i] > fltMaxValue)
                {
                    fltMaxValue = Values[i];
                }
            }

            if (YSliceBegin > fltMinValue)
            {
                YSliceBegin = fltMinValue;
            }
            int intYSliceCount = (int)(fltMaxValue / YSliceValue);
            if (fltMaxValue % YSliceValue != 0)
            {
                intYSliceCount++;
            }
            YSlice = (Height - 2 * YSpace) / intYSliceCount;
        }

        /// <summary>
        /// 生成圖像並返回bmp圖像對象
        /// </summary>
        /// <returns></returns>
        public Bitmap CreateImage()
        {
            InitializeGraph();

            int intKeysCount = Keys.Length;
            int intValuesCount = Values.Length;

            if (intValuesCount % intKeysCount == 0)
            {
                int intCurvesCount = intValuesCount / intKeysCount;
                for (int i = 0; i < intCurvesCount; i++)
                {
                    float[] fltCurrentValues = new float[intKeysCount];
                    for (int j = 0; j < intKeysCount; j++)
                    {
                        fltCurrentValues[j] = Values[i * intKeysCount + j];
                    }
                    DrawContent(ref g, fltCurrentValues, clrsCurveColors[i]);
                }
            }
            else
            {
                g.DrawString("發生錯誤，Values的長度必須是Keys的整數倍!", new Font("宋體", FontSize + 5), new SolidBrush(TextColor), new Point((int)XSpace, (int)(Height / 2)));
            }
            return objBitmap;
        }

        /// <summary>
        /// 初始化和填充圖像區域，畫出邊框，初始標題
        /// </summary>
        private void InitializeGraph()
        {
            //根據給定的高度和寬度創建一個位圖圖像
            objBitmap = new Bitmap((int)Width, (int)Height);
            //從指定的 objBitmap 對象創建 g 對象 (即在objBitmap對象中畫圖)
            g = Graphics.FromImage(objBitmap);
            //根據給定顏色(LightGray)填充圖像的矩形區域 (背景)
            g.DrawRectangle(new Pen(BorderColor, 1), 0, 0, Width - 1, Height - 1); //畫邊框
            g.FillRectangle(new SolidBrush(BgColor), 1, 1, Width - 2, Height - 2); //填充邊框
            //畫X軸,注意圖像的原始X軸和Y軸計算是以左上角為原點，向右和向下計算的
            float fltX1 = XSpace;
            float fltY1 = Height - YSpace;
            float fltX2 = Width - XSpace + XSlice / 2;
            float fltY2 = fltY1;
            g.DrawLine(new Pen(new SolidBrush(AxisColor), 1), fltX1, fltY1, fltX2, fltY2);
            //畫Y軸
            fltX1 = XSpace;
            fltY1 = Height - YSpace;
            fltX2 = XSpace;

            fltY2 = YSpace - YSlice / 2;
            g.DrawLine(new Pen(new SolidBrush(AxisColor), 1), fltX1, fltY1, fltX2, fltY2);
            //初始化軸線說明文字

            SetAxisText(ref g);
            //初始化X軸上的刻度和文字

            SetXAxis(ref g);
            //初始化Y軸上的刻度和文字
            SetYAxis(ref g);
            //初始化標題
            CreateTitle(ref g);
        }

        /// <summary>
        /// 初始化軸線說明文字
        /// </summary>
        /// <param name="g"></param>
        private void SetAxisText(ref Graphics g)
        {
            float fltX = Width - XSpace + XSlice / 2 - (XAxisText.Length - 1) * intFontSpace;
            float fltY = Height - YSpace - intFontSpace;
            g.DrawString(XAxisText, new Font("宋體", FontSize), new SolidBrush(AxisTextColor), fltX, fltY);
            fltX = XSpace + 5;
            fltY = YSpace - YSlice / 2 - intFontSpace;
            for (int i = 0; i < YAxisText.Length; i++)
            {
                g.DrawString(YAxisText[i].ToString(), new Font("宋體", FontSize), new SolidBrush(AxisTextColor), fltX, fltY);
                fltY += intFontSpace; //字體上下距離
            }
        }

        /// <summary>
        /// 初始化X軸上的刻度和文字
        /// </summary>
        /// <param name="g"></param>

        private void SetXAxis(ref Graphics g)
        {
            float fltX1 = XSpace;
            float fltY1 = Height - YSpace;
            float fltX2 = XSpace;
            float fltY2 = Height - YSpace;
            int iCount = 0;
            int iSliceCount = 1;
            float Scale = 0;
            float iWidth = ((Width - 2 * XSpace) / XSlice) * 50; //將要畫刻度的長度分段，並乘以50，以10為單位畫刻度線。
            float fltSliceHeight = XSlice / 10; //刻度線的高度
            g.TranslateTransform(fltX1, fltY1); //平移圖像(原點)
            g.RotateTransform(XRotateAngle, MatrixOrder.Prepend); //旋轉圖像
            g.DrawString(Keys[0].ToString(), new Font("宋體", FontSize), new
            SolidBrush(SliceTextColor), 0, 0);
            g.ResetTransform(); //重置圖像

            for (int i = 0; i <= iWidth; i += 10) //以10為單位
            {
                Scale = i * XSlice / 50;//即(i / 10) * (XSlice / 5)，將每個刻度分五部分畫，但因為i以10為單位，得除以10
                if (iCount == 5)
                {
                    g.DrawLine(new Pen(new SolidBrush(AxisColor)), fltX1 + Scale, fltY1 + fltSliceHeight * 1.5f, fltX2 + Scale, fltY2 - fltSliceHeight * 1.5f);

                    //畫網格虛線
                    Pen penDashed = new Pen(new SolidBrush(AxisColor));

                    penDashed.DashStyle = DashStyle.Dash;


                    g.DrawLine(penDashed, fltX1 + Scale, fltY1, fltX2 + Scale, YSpace - YSlice / 2);
                    //這裡顯示X軸刻度
                    if (iSliceCount <= Keys.Length - 1)
                    {
                        g.TranslateTransform(fltX1 + Scale, fltY1);
                        g.RotateTransform(XRotateAngle, MatrixOrder.Prepend);
                        g.DrawString(Keys[iSliceCount].ToString(), new Font("宋體", FontSize), new SolidBrush(SliceTextColor), 0, 0);
                        g.ResetTransform();
                    }
                    else
                    {
                        //超過范圍，不畫任何刻度文字
                    }
                    iCount = 0;
                    iSliceCount++;

                    if (fltX1 + Scale > Width - XSpace)
                    {
                        break;
                    }
                }
                else
                {
                    g.DrawLine(new Pen(new SolidBrush(SliceColor)), fltX1 + Scale, fltY1 + fltSliceHeight, fltX2 + Scale, fltY2 - fltSliceHeight);
                }
                iCount++;
            }
        }
        /// <summary>
        /// 初始化Y軸上的刻度和文字
        /// </summary>
        /// <param name="g"></param>
        private void SetYAxis(ref Graphics g)
        {
            float fltX1 = XSpace;
            float fltY1 = Height - YSpace;
            float fltX2 = XSpace;
            float fltY2 = Height - YSpace;
            int iCount = 0;
            float Scale = 0;
            int iSliceCount = 1;
            float iHeight = ((Height - 2 * YSpace) / YSlice) * 50; //將要畫刻度的長度分段，並乘以50，以10為單位畫刻度線。
            float fltSliceWidth = YSlice / 10; //刻度線的寬度
            string strSliceText = string.Empty;
            g.TranslateTransform(XSpace - intFontSpace * YSliceBegin.ToString().Length, Height - YSpace); //平移圖像(原點)
            g.RotateTransform(YRotateAngle, MatrixOrder.Prepend); //旋轉圖像
            g.DrawString(YSliceBegin.ToString(), new Font("宋體", FontSize), new SolidBrush(SliceTextColor), 0, 0);
            g.ResetTransform(); //重置圖像

            for (int i = 0; i < iHeight; i += 10)
            {
                Scale = i * YSlice / 50; //即(i / 10) * (YSlice / 5)，將每個刻度分五部分畫，但因為i以10為單位，得除以10
                if (iCount == 5)
                {
                    g.DrawLine(new Pen(new SolidBrush(AxisColor)), fltX1 - fltSliceWidth * 1.5f, fltY1 - Scale, fltX2 + fltSliceWidth * 1.5f, fltY2 - Scale);
                    //畫網格虛線

                    Pen penDashed = new Pen(new SolidBrush(AxisColor));

                    penDashed.DashStyle = DashStyle.Dash;
                    g.DrawLine(penDashed, XSpace, fltY1 - Scale, Width - XSpace + XSlice / 2, fltY2 - Scale);

                    //這裡顯示Y軸刻度
                    strSliceText = Convert.ToString(YSliceValue * iSliceCount + YSliceBegin);

                    g.TranslateTransform(XSpace - intFontSize * strSliceText.Length, fltY1 - Scale);

                    //平移圖像(原點)
                    g.RotateTransform(YRotateAngle, MatrixOrder.Prepend); //旋轉圖像
                    g.DrawString(strSliceText, new Font("宋體", FontSize), new SolidBrush(SliceTextColor), 0, 0);

                    g.ResetTransform(); //重置圖像
                    iCount = 0;
                    iSliceCount++;
                }
                else
                {
                    g.DrawLine(new Pen(new SolidBrush(SliceColor)), fltX1 - fltSliceWidth, fltY1 - Scale, fltX2 + fltSliceWidth, fltY2 - Scale);
                }
                iCount++;
            }
        }

        /// <summary>
        /// 畫曲線
        /// </summary>
        /// <param name="g"></param>
        private void DrawContent(ref Graphics g, float[] fltCurrentValues, Color clrCurrentColor)
        {
            Pen CurvePen = new Pen(clrCurrentColor, CurveSize);
            PointF[] CurvePointF = new PointF[Keys.Length];
            float keys = 0;
            float values = 0;
            for (int i = 0; i < Keys.Length; i++)
            {
                keys = XSlice * i + XSpace;
                values = (Height - YSpace) + YSliceBegin - YSlice * (fltCurrentValues[i] / YSliceValue);
                CurvePointF[i] = new PointF(keys, values);
            }
            g.DrawCurve(CurvePen, CurvePointF, Tension);
        }
        /// <summary>
        /// 初始化標題
        /// </summary>
        /// <param name="g"></param>
        private void CreateTitle(ref Graphics g)
        {
            g.DrawString(Title, new Font("宋體", FontSize), new SolidBrush(TextColor), new Point((int)(Width - XSpace) - intFontSize * Title.Length, (int)(YSpace - YSlice / 2 - intFontSpace)));
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



//arc
//g.DrawArc(Pens.Red, 100, 100, 20, 10, -190, -160);


/*

            //直書橫書
            Font font = new Font("隸書", 17);
            StringFormat format = new StringFormat();
            format.FormatFlags = StringFormatFlags.DirectionVertical;

            g.DrawString("三杯祝福歌", font, brBlack, 250, 30, format);
            g.DrawString("一曲迎春調", font, brBlack, 20, 30, format);
            g.DrawString("迎春祝福", font, brBlack, 100, 0);
*/





/*
            //擷取部分圖形
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);
            pictureBox1.Image = image;

            int x_st = 0;
            int y_st = 0;
            int W = 150;
            int H = 150;

            Graphics g = this.CreateGraphics();
            Bitmap bitmap = new Bitmap(filename);
            Rectangle rectangle = new Rectangle(x_st, y_st, W, H);
            Bitmap cloneBitmap = bitmap.Clone(rectangle, PixelFormat.DontCare);
            pictureBox2.Image = cloneBitmap;
            pictureBox2.Visible = true;

            richTextBox1.Text += "從(" + x_st.ToString() + ", " + y_st.ToString() + ") 擷取 W = " + W.ToString() + ", H = " + H.ToString() + " 區域\n";
*/


/*
//影像的寬高可以是負的, 做倒影鏡射
string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

Bitmap bitmap1 = new Bitmap(filename);

int Cx = this.pictureBox1.ClientSize.Width / 2; // 視窗客戶區 正中心
int Cy = this.pictureBox1.ClientSize.Height / 2;

int W = bitmap1.Width;
int H = bitmap1.Height;

Graphics g = this.pictureBox1.CreateGraphics();

g.DrawImage(bitmap1, Cx, Cy, W / 2, H / 2);
g.DrawImage(bitmap1, Cx, Cy, -W / 2, H / 2);
g.DrawImage(bitmap1, Cx, Cy, W / 2, -H / 2);
g.DrawImage(bitmap1, Cx, Cy, -W / 2, -H / 2);
*/


/*

ddddd

            //畫圖初始化   
            //Bitmap bitmap1 = new Bitmap(500, 500);
            //Graphics g = Graphics.FromImage(bitmap1);
            //g.Clear(Color.White);

//創建一個長度為400，寬帶為400的Bitmap實例
//Bitmap bmp = new Bitmap(400, 300);
//Graphics g;
//g = Graphics.FromImage(bmp);

 * 
 * 
 * 
            g.Dispose();  // dispose後, 就不能再使用了

*/
