using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for Matrix

using System.Drawing.Text;      //for TextRenderingHint

//方案總管/加入/現有項目/選取Rainbow.cs, 把 namespace 改成 vcs_Draw3A
//方案總管/加入/現有項目/選取BatteryStuff.cs, 把 namespace 改成 vcs_Draw3A

namespace vcs_Draw3A
{
    public partial class Form1 : Form
    {
        Graphics g2;
        //SolidBrush sb;
        //Bitmap bitmap1;
        Bitmap bitmap2;
        Bitmap bitmap3;
        Bitmap bitmap_border1;
        Bitmap bitmap_border2;

        //for gear
        // The frame images.
        private Bitmap[] Frames;
        // The index of the current frame.
        private int FrameNum = 0;

        //for atom
        // The background Bitmap.
        private Bitmap Background;

        // The points on the curve.
        private List<PointF> Points;

        // The transformation used to draw.
        private Matrix Transform;

        // The current point number where the atom is.
        private int AtomPoint = 0;

        Graphics gc;
        Bitmap bitmap_card;
        Graphics gc2;
        Bitmap bitmap_card2;

        #region 畫random曲線
        private int Ymid;
        private int YValue;
        private const int GridStep = 40;
        #endregion


        //for pictureBox_stock ST

        // The ticker symbol.
        private const string Symbol = "ABCD Company";

        // The data.
        private List<DateTime> Times = new List<DateTime>();
        private List<PointF> Prices = new List<PointF>();

        // The values transformed for drawing.
        PointF[] TransformedValues;

        // World coordinate information.
        private float Wxmin, Wxmax, Wymin, Wymax;

        // The area where we will draw the graph.
        private int GraphXmin, GraphXmax, GraphYmin, GraphYmax;

        // The radius of a drawn point.
        private const float Radius = 4;

        //for pictureBox_stock SP

        //畫任意矩形 pictureBox1
        private Random Rand = new Random();
        private Bitmap Bm;
        private Graphics Gr;

        //畫正弦波 ST
        Bitmap bmp;
        Graphics g;
        Pen p4;
        int t;

        //int WIDTH = 720;
        int HEIGHT = 300;
        int AMPLITUDE = 150;
        //畫正弦波 SP

        //畫雷達掃瞄圖 ST
        int radar_WIDTH;
        int radar_HEIGHT;
        int radar_HAND;

        int u;  //in degree
        int cx, cy;     //center of the circle
        int x, y;       //HAND coordinate

        int tx, ty, lim = 20;

        Bitmap radar_bmp;
        Pen radar_p;
        Graphics radar_g;
        //畫雷達掃瞄圖 SP

        string filename = "C:\\______test_files1\\picture1.jpg";

        public Form1()
        {
            InitializeComponent();

            show_item_location();
            //pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;

            //for atom
            // Enable double buffering.
            // Reduce flicker.
            DoubleBuffered = true;

            //for gear
            // Load the frames.
            Frames = new Bitmap[18];
            for (int i = 0; i < 18; i++)
            {
                Frames[i] = new Bitmap("Frame" + i + ".png");
            }
            // Display the first frame.
            pictureBox_gear.Image = Frames[FrameNum];
            // Size the form to fit.
            ClientSize = new Size(pictureBox_gear.Right + pictureBox_gear.Left, pictureBox_gear.Bottom + pictureBox_gear.Left);

            // Make the Bitmap and associated Graphics object.
            Background = new Bitmap(300, 300);
            using (Graphics gr = Graphics.FromImage(Background))
            {
                gr.Clear(Color.White);

                // Set up a transformation to map the region
                // -2.1 <= X <= 2.1, -2.1 <= Y <= 2.1 onto the  Bitmap.
                RectangleF rect = new RectangleF(-2.1f, -2.1f, 4.2f, 4.2f);
                PointF[] pts =
                    {
                        new PointF(0, Background.Height),
                        new PointF(Background.Width, Background.Height),
                        new PointF(0, 0),
                    };
                Transform = new Matrix(rect, pts);
                gr.Transform = Transform;
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                using (Pen thin_pen = new Pen(Color.Blue, 0))
                {
                    // Draw the X and Y axes.
                    thin_pen.Color = Color.Blue;
                    gr.DrawLine(thin_pen, -2.1f, 0, 2.1f, 0);
                    const float big_tick = 0.1f;
                    const float small_tick = 0.05f;
                    for (float x = (int)-2.1f; x <= 2.1f; x += 1)
                        gr.DrawLine(thin_pen, x, -small_tick, x, small_tick);
                    for (float x = (int)-2.1f + 0.5f; x <= 2.1f; x += 1)
                        gr.DrawLine(thin_pen, x, -big_tick, x, big_tick);

                    gr.DrawLine(thin_pen, 0, -2.1f, 0, 2.1f);
                    for (float y = (int)-2.1f; y <= 2.1f; y += 1)
                        gr.DrawLine(thin_pen, -small_tick, y, small_tick, y);
                    for (float y = (int)-2.1f + 0.5f; y <= 2.1f; y += 1)
                        gr.DrawLine(thin_pen, -big_tick, y, big_tick, y);

                    // Draw the graph.
                    DrawGraph(gr);
                }
            }

            // Display the result and size the form to fit.
            pictureBox_atom.Image = Background;
            timer_atom.Enabled = true;

            #region 畫random曲線
            Ymid = pictureBox_random.ClientSize.Height / 2;
            YValue = Ymid;

            // Make the Bitmap and Graphics objects.
            int wid = pictureBox_random.ClientSize.Width;
            int hgt = pictureBox_random.ClientSize.Height;
            Bitmap bm = new Bitmap(wid, hgt);
            Graphics grnd = Graphics.FromImage(bm);

            // Draw guide lines.
            grnd.Clear(Color.Blue);
            for (int i = Ymid; i <= pictureBox_random.ClientSize.Height; i += GridStep)
            {
                grnd.DrawLine(Pens.LightBlue, 0, i, wid - 1, i);
            }
            for (int i = Ymid; i >= 0; i -= GridStep)
            {
                grnd.DrawLine(Pens.LightBlue, 0, i, wid - 1, i);
            }

            pictureBox_random.Image = bm;
            #endregion
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            FormBorderStyle = FormBorderStyle.FixedDialog;
            MinimizeBox = false;
            MaximizeBox = false;
            StartPosition = FormStartPosition.CenterScreen;

            timer_rainbow.Interval = Interval;
            SelectedColor = Color.Red;
            SelectedRainbowNumber = 0;

            //指定畫布大小
            pictureBox_card.Width = 200;
            pictureBox_card.Height = 200;
            bitmap_card = new Bitmap(pictureBox_card.Width, pictureBox_card.Height);
            gc = Graphics.FromImage(bitmap_card);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            pictureBox_card.Image = bitmap_card;

            pictureBox_card2.Width = 200;
            pictureBox_card2.Height = 200;
            bitmap_card2 = new Bitmap(pictureBox_card2.Width, pictureBox_card2.Height);
            gc2 = Graphics.FromImage(bitmap_card2);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            pictureBox_card2.Image = bitmap_card2;

            //for atom2
            this.SetStyle(ControlStyles.AllPaintingInWmPaint | ControlStyles.DoubleBuffer | ControlStyles.ResizeRedraw, true);
            this.UpdateStyles();

            //for pictureBox_stock
            SavePrice();    // Get the first price.

            //for pictureBox_move ST
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";
            //pictureBox_move.Image = Image.FromFile(filename);
            bitmap3 = new Bitmap(filename);
            richTextBox1.Text += "W = " + bitmap3.Width.ToString() + " H = " + bitmap3.Height.ToString() + "\n";
            //pictureBox_move.Size = bitmap3.Size;
            pictureBox_move.Image = bitmap3;

            timer_move.Enabled = true;
            //for pictureBox_move SP

            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";
            //pictureBox_move.Image = Image.FromFile(filename);
            bitmap_border1 = new Bitmap(filename);
            pictureBox_border1.Image = bitmap_border1;

            bitmap_border2 = new Bitmap(filename);
            pictureBox_border2.Image = bitmap_border2;

            //畫任意矩形 ST
            timer_random_rectangle.Enabled = true;
            Bm = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Gr = Graphics.FromImage(Bm);
            pictureBox1.BackColor = Color.Pink;
            pictureBox1.Image = Bm;
            //畫任意矩形 SP


            //畫正弦波 ST
            timer7.Enabled = true;
            richTextBox1.Text += "ST\n";

            //pictureBox_move.Width = 480;
            //pictureBox_move.Height = 360;
            //pictureBox_move.Location = new Point(400, 300);

            //create Bitmap
            bmp = null;
            bmp = new Bitmap(pictureBox_sine.Size.Width, pictureBox_sine.Size.Height);

            //background color
            //this.BackColor = Color.Black;

            //center
            //cx = WIDTH / 2;
            //cy = HEIGHT / 2;

            //initial degree of HAND
            //u = 0;

            //timer1.Enabled = true;
            pictureBox_sine.Image = null;
            t = 0;
            DrawXY();
            DrawYLine();
            //畫正弦波 SP


            //旋轉邊框 ST
            //新建圖檔, 初始化畫布
            bitmap2 = new Bitmap(pictureBox_rotate.Width, pictureBox_rotate.Height);
            g2 = Graphics.FromImage(bitmap2);
            g2.Clear(Color.White);
            pictureBox_rotate.Image = bitmap2;
            //旋轉邊框 SP

            //畫雷達掃瞄圖 ST
            radar_WIDTH = 270;
            radar_HEIGHT = radar_WIDTH;
            radar_HAND = radar_WIDTH / 2;

            //create Bitmap
            radar_bmp = new Bitmap(radar_WIDTH + 1, radar_HEIGHT + 1);

            //background color
            panel_radar.BackColor = Color.Black;

            //center
            cx = radar_WIDTH / 2;
            cy = radar_HEIGHT / 2;

            //initial degree of HAND
            u = 0;

            //timer
            //t.Interval = 5; //in millisecond
            //t.Tick += new EventHandler(this.t_Tick);
            //t.Start();

            //畫雷達掃瞄圖 SP
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1810;
            y_st = 80;
            dx = 120;
            dy = 50;

            richTextBox1.Location = new Point(x_st + dx * 0 - 200, y_st + dy * 12);
            richTextBox1.Size = new Size(300, 320);

            pictureBox1.Size = new Size(480, 300);
            pictureBox1.Location = new Point(910, 10);
            pictureBox1.BackColor = Color.LightGreen;

            pictureBox_sine.Size = new Size(400, 300);
            pictureBox_sine.Location = new Point(910 + 480 + 10, 10);
            pictureBox_sine.BackColor = Color.LightYellow;


            pictureBox_border1.Size = new Size(280, 350);
            pictureBox_border1.Location = new Point(1000 + 310, 10 + 300 + 10);
            pictureBox_border1.BackColor = Color.LightSkyBlue;

            pictureBox_border2.Size = new Size(280, 350);
            pictureBox_border2.Location = new Point(1000 + 310 + 300, 10 + 300 + 10);
            pictureBox_border2.BackColor = Color.LightSkyBlue;

            pictureBox_move.Size = new Size(280, 350);
            pictureBox_move.Location = new Point(1000, 10 + 300 + 10);
            pictureBox_move.BackColor = Color.LightBlue;

            pictureBox_stock.Size = new Size(680, 320);
            pictureBox_stock.Location = new Point(1000 - 700 + 15, 10 + 360 + 10);
            pictureBox_stock.BackColor = Color.LightPink;

            pictureBox_rotate.Size = new Size(220, 110);
            pictureBox_rotate.Location = new Point(680, 265);
            pictureBox_rotate.BackColor = Color.Linen;

            //pictureBox_rotate

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            int W = 300;
            int H = 300;
            x_st = 10;
            y_st = 720;
            dx = 350;

            pictureBox_random.Size = new Size(W, H);
            pictureBox_random.Location = new Point(x_st + dx * 0, y_st);

            pictureBox_atom.Size = new Size(W, H);
            pictureBox_atom.Location = new Point(x_st + dx * 1, y_st);

            pictureBox_spin.Size = new Size(100, 100);
            pictureBox_spin.Location = new Point(100, 360);
            pictureBox_spin.BackColor = Color.LightGray;

            pictureBox_hex.Size = new Size(100, 100);
            pictureBox_hex.Location = new Point(205, 360);
            pictureBox_hex.BackColor = Color.LightGray;

            pictureBox_gear.Size = new Size(W, H);
            pictureBox_gear.Location = new Point(x_st + dx * 2, y_st + 20);
            trackBar1.Location = new Point(x_st + dx * 2, y_st);
            lb_fps.Location = new Point(x_st + dx * 2 + 280, y_st + 10);
            lb_fps.Text = trackBar1.Value.ToString();

            pictureBox_circle.Size = new Size(W, H);
            pictureBox_circle.Location = new Point(x_st + dx * 3, y_st);
            pictureBox_circle.BackColor = Color.Pink;

            pictureBox_random_color.Size = new Size(W * 3 / 5, H);
            pictureBox_random_color.Location = new Point(x_st + dx * 4, y_st);
            pictureBox_random_color.BackColor = Color.Pink;

            //畫雷達掃瞄圖 ST
            panel_radar.Size = new Size(W, H);
            panel_radar.Location = new Point(10, 10);
            panel_radar.BackColor = Color.Black;
            pictureBox_radar.Size = new Size(W - 20, H - 20);
            pictureBox_radar.Location = new Point(10, 10);
            richTextBox1.Text += "pictureBox_radar W = " + pictureBox_radar.Width.ToString() + ", H = " + pictureBox_radar.Height.ToString() + "\n";
            //畫雷達掃瞄圖 SP

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void DrawXY()//画X轴Y轴
        {
            //graphics
            g = Graphics.FromImage(bmp);
            System.Drawing.Point px1 = new System.Drawing.Point(this.pictureBox_sine.Width * 10 / 100, this.pictureBox_sine.Height * 90 / 100);
            System.Drawing.Point px2 = new System.Drawing.Point(this.pictureBox_sine.Width * 90 / 100, this.pictureBox_sine.Height * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            System.Drawing.Point py1 = new System.Drawing.Point(this.pictureBox_sine.Width * 10 / 100, this.pictureBox_sine.Height * 90 / 100);
            System.Drawing.Point py2 = new System.Drawing.Point(this.pictureBox_sine.Width * 10 / 100, this.pictureBox_sine.Height * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
            g.Dispose();
        }

        private void DrawYLine()    //画X轴刻度
        {
            //graphics
            g = Graphics.FromImage(bmp);
            for (int i = 1; i < 9; i++)
            {
                System.Drawing.Point py1 = new System.Drawing.Point(100 * i, this.pictureBox_sine.Height - 5);
                System.Drawing.Point py2 = new System.Drawing.Point(100 * i, this.pictureBox_sine.Height);
                g.DrawLine(new Pen(Brushes.Red, 1), py1, py2);
            }
            g.Dispose();
        }

        //畫任意矩形
        private void timer_random_rectangle_Tick(object sender, EventArgs e)
        {
            int x = Rand.Next(pictureBox1.Width - 10);
            int y = Rand.Next(pictureBox1.Height - 10);
            int width = Rand.Next(pictureBox1.Width - x);
            int height = Rand.Next(pictureBox1.Height - y);
            Color color = Color.FromArgb(128,
                255 * Rand.Next(2),
                255 * Rand.Next(2),
                255 * Rand.Next(2));
            using (Brush brush = new SolidBrush(color))
            {
                Gr.FillRectangle(brush, x, y, width, height);
            }
            Refresh();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        int cnt = 0;
        private void timer2_Tick(object sender, EventArgs e)
        {
            cnt++;

            if ((cnt % 4) == 0)
            {
                p0.BackColor = Color.Blue;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 1)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Blue;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 2)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Blue;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 3)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Blue;
            }
        }


        int x_st = 0;
        int y_st = 0;
        int xx = 0;
        int yy = 0;
        int step = 60;
        Pen pen = new Pen(Color.Blue, 30);

        private void timer_rotate_Tick(object sender, EventArgs e)
        {
            int w = pictureBox_rotate.Width;
            int h = pictureBox_rotate.Height;
            //richTextBox1.Text += "w = " + w.ToString() + " h = " + h.ToString() + "\n";
            if ((xx < (w - 1)) && (yy == 0))
            {
                if (xx == 0)
                {
                    if (pen.Color == Color.Red)
                        pen.Color = Color.Blue;
                    else
                        pen.Color = Color.Red;
                }

                //richTextBox1.Text += "1";
                if (xx < (w - step))
                    xx += step;
                else
                    xx = w - 1;
            }
            else if ((yy < (h - 1)) && (xx == (w - 1)))
            {
                //richTextBox1.Text += "2";
                if (yy < (h - step))
                    yy += step;
                else
                    yy = h - 1;
            }
            else if ((xx > 0) && (yy == (h - 1)))
            {
                //richTextBox1.Text += "3";
                if (xx > step)
                    xx -= step;
                else
                    xx = 0;
            }
            else if ((yy > 0) && (xx == 0))
            {
                //richTextBox1.Text += "4";
                if (yy > step)
                    yy -= step;
                else
                    yy = 0;
            }
            else
            {
                richTextBox1.Text += "xxxxxx\n";
            }

            if (pen.Color == Color.Red)
                pen.Color = Color.Blue;
            else
                pen.Color = Color.Red;


            //richTextBox1.Text += "\t(" + x_st.ToString() + "," + y_st.ToString() + ")-" + "(" + xx.ToString() + "," + yy.ToString() + ")" + "\n";

            g2.DrawLine(pen, x_st, y_st, xx, yy);
            x_st = xx;
            y_st = yy;

            pictureBox_rotate.Image = bitmap2;


        }

        int x_st4 = 0;
        int y_st4 = 200;

        private void timer_move_Tick(object sender, EventArgs e)
        {
            bitmap3 = new Bitmap(filename);

            Graphics g = Graphics.FromImage(bitmap3);

            if (x_st4 < 300)
            {
                x_st4 += 5;
                //y_st4 += 10;
                //y_st4 = 200 + 200 * (int)(Math.Sin((Math.PI * x_st4 / 180)));
                y_st4 = 200 + (int)(100 * (Math.Sin((Math.PI * x_st4 / 180))));
            }
            else
            {
                x_st4 = 0;
                //y_st4 = 0;
            }
            int ww = 10;
            int hh = 10;

            //g.DrawRectangle(new Pen(Color.Red, 1), x_st4, y_st4, ww, hh);
            //g.DrawEllipse(new Pen(Color.Red, 1), x_st4, y_st4, ww, hh);
            //g.FillEllipse(new Brush(Color.Red), x_st4, y_st4, ww, hh);
            g.FillEllipse(new SolidBrush(Color.Red), x_st4, y_st4, ww, hh);

            pictureBox_move.Image = bitmap3;


            //bitmap1 = new Bitmap(filename);
            //bitmap_old = new Bitmap(filename);
            //pictureBox1.Image = bitmap1;


        }

        int step3 = 1;
        int xx3 = 0;
        int yy3 = 0;
        int ww = 0;
        int hh = 0;
        int thick5 = 10;
        int add = 10;
        int round = 0;

        private void timer_border1_Tick(object sender, EventArgs e)
        {
            //bitmap1 = new Bitmap(filename);
            ww = bitmap_border1.Width;
            hh = bitmap_border1.Height;

            Graphics g = Graphics.FromImage(bitmap_border1);

            if (step3 == 1)
            {
                if (xx3 < (ww - thick5 - add))
                {
                    xx3 += add;
                }
                else
                {
                    xx3 = ww - thick5 - 1;
                    step3 = 2;
                }
            }
            else if (step3 == 2)
            {
                if (yy3 < (hh - thick5 - add))
                {
                    yy3 += add;
                }
                else
                {
                    yy3 = hh - thick5 - 1;
                    step3 = 3;
                }
            }
            else if (step3 == 3)
            {
                if (xx3 > add)
                {
                    xx3 -= add;
                }
                else
                {
                    xx3 = 0;
                    step3 = 4;
                }
            }
            else if (step3 == 4)
            {
                if (yy3 > add)
                {
                    yy3 -= add;
                }
                else
                {
                    yy3 = 0;
                    step3 = 1;
                    round++;
                    //bitmap1 = new Bitmap(filename);
                }
            }

            if ((round % 2) == 0)
                g.FillRectangle(new SolidBrush(Color.Red), xx3, yy3, thick5, thick5);
            else
                g.FillRectangle(new SolidBrush(Color.White), xx3, yy3, thick5, thick5);

            //g.FillEllipse(new SolidBrush(Color.Red), xx3, yy3, 3, 3);

            pictureBox_border1.Image = bitmap_border1;


            //bitmap1 = new Bitmap(filename);
            //bitmap_old = new Bitmap(filename);
            //pictureBox1.Image = bitmap1;



        }

        int step8 = 1;
        int step8_old = -1;
        int round8 = 0;
        int W;
        int H;
        int w;
        int h;
        //int ratio = 7;

        int x_st8 = 0;
        int y_st8 = 0;
        int count = 0;
        int count_old = 0;

        private void timer_border2_Tick(object sender, EventArgs e)
        {
            //bitmap_border2
            W = bitmap_border2.Width;
            H = bitmap_border2.Height;

            w = 25;
            h = 25;

            //richTextBox1.Text += "W = " + W.ToString() + " H = " + H.ToString() + " w = " + w.ToString() + " h = " + h.ToString() + "\n";

            Graphics g = Graphics.FromImage(bitmap_border2);

            g.FillRectangle(new SolidBrush(Color.Red), 0, 0, w, h);

            if (step8 == 1)
            {
                //if (x_st8 < (W - w * (round8 + 2)))
                if ((x_st8 + w) < (W - w * round8 - w))
                {
                    x_st8 = x_st8 + w;
                    richTextBox1.Text += "U ";
                }
                else
                {
                    x_st8 = W - w * round8 - w;
                    step8 = 2;
                    richTextBox1.Text += "u ";
                }
                //richTextBox1.Text += x_st8.ToString() + " ";
                count++;
            }
            else if (step8 == 2)
            {
                if ((y_st8 + h) < (H - h * round8 - h))
                {
                    y_st8 = y_st8 + h;
                    richTextBox1.Text += "R ";
                }
                else
                {
                    //y_st8 = H - h * (round8 + 1) - 1;
                    y_st8 = H - h * round8 - h;
                    step8 = 3;
                    richTextBox1.Text += "r ";
                }
                //richTextBox1.Text += y_st8.ToString() + " ";
                count++;
            }
            else if (step8 == 3)
            {
                //if ((x_st8 - w * round8) > w)
                if ((x_st8 - w) > (w * round8))
                {
                    x_st8 -= w;
                    richTextBox1.Text += "D ";
                }
                else
                {
                    x_st8 = w * round8;
                    step8 = 4;
                    richTextBox1.Text += "d ";
                }
                //richTextBox1.Text += x_st8.ToString() + " ";
                count++;
            }
            else if (step8 == 4)
            {
                if ((y_st8 - h) > (h * round8))
                {
                    y_st8 -= h;
                    richTextBox1.Text += "L ";
                }
                else
                {
                    step8 = 1;
                    round8++;
                    x_st8 = w * round8;
                    y_st8 = h * round8;
                }
                //richTextBox1.Text += y_st8.ToString() + " ";
                count++;
            }

            if (step8_old != step8)
            {
                step8_old = step8;
                //richTextBox1.Text += "\nstep = " + step8.ToString() + "\t";
                //richTextBox1.Text += "count = " + count.ToString() + " ";
                if (count > 1)
                {
                    if ((count - count_old) == 1)
                    {
                        timer_border2.Enabled = false;
                        return;
                    }
                    else
                    {
                        count_old = count;
                    }
                }


                //count = 0;
            }

            if (step8 == 1)
            {
                g.FillRectangle(new SolidBrush(Color.Red), x_st8, y_st8, w, h);
            }
            else if (step8 == 2)
            {
                g.FillRectangle(new SolidBrush(Color.Green), x_st8, y_st8, w, h);
            }
            else if (step8 == 3)
            {
                g.FillRectangle(new SolidBrush(Color.Blue), x_st8, y_st8, w, h);
                //richTextBox1.Text += "(" + x_st8.ToString() + "," + y_st8.ToString() + ") ";
            }
            else if (step8 == 4)
            {
                g.FillRectangle(new SolidBrush(Color.Cyan), x_st8, y_st8, w, h);
            }

            //richTextBox1.Text += "(" + x_st8.ToString() + "," + y_st8.ToString() + ") ";

            pictureBox_border2.Image = bitmap_border2;
        }

        private void timer7_Tick(object sender, EventArgs e)
        {
            //pen
            p4 = new Pen(Color.Green, 1f);

            //graphics
            g = Graphics.FromImage(bmp);

            int xx;
            int yy;

            xx = t;
            yy = HEIGHT - (int)(AMPLITUDE * Math.Sin(Math.PI * t / 180)) - AMPLITUDE;

            g.DrawEllipse(new Pen(Color.Red, 1f), xx, yy, 1, 1);

            //load bitmap in picturebox1
            pictureBox_sine.Image = bmp;

            t += 3;
            if (t >= 450)
            {
                g.Clear(Color.LightYellow);
                t = 0;
                DrawXY();
                DrawYLine();
            }

            //dispose
            p4.Dispose();
            g.Dispose();
        }

        // The currently selected color and its number.
        private Color SelectedColor;
        private float SelectedRainbowNumber;

        // The animation parameters.
        private const float ColorDelta = 0.02f;
        private int Interval = 20;

        // Start with red selected.

        // Continue animating the rainbow colors.
        private void timer_rainbow_Tick(object sender, EventArgs e)
        {
            // Update the current color.
            SelectedRainbowNumber += ColorDelta;
            if (SelectedRainbowNumber > 1f)
                SelectedRainbowNumber = 0f;
            SelectedColor = Rainbow.RainbowNumberToColor(SelectedRainbowNumber);

            // Draw the new color.
            picRainbow.Refresh();
            picSample.Refresh();
            label1.Text = SelectedRainbowNumber.ToString();
        }

        private void picRainbow_Resize(object sender, EventArgs e)
        {
            picRainbow.Refresh();
        }

        private void picSample_Resize(object sender, EventArgs e)
        {
            picSample.Refresh();
        }

        // Draw the rainbow and the selected number.
        private void picRainbow_Paint(object sender, PaintEventArgs e)
        {
            // Draw the rainbow.
            using (Brush rainbow_brush = Rainbow.RainbowBrush(
                new Point(0, 0),
                new Point(picRainbow.ClientSize.Width, picRainbow.ClientSize.Height)))
            {
                e.Graphics.FillRectangle(rainbow_brush, picRainbow.ClientRectangle);
            }

            // Get and draw the selected location.
            int x = (int)(SelectedRainbowNumber * picRainbow.ClientSize.Width);
            Point[] pts =
            {
                new Point(x - 5, 0),
                new Point(x, 5),
                new Point(x + 5, 0)
            };
            e.Graphics.FillPolygon(Brushes.Black, pts);
        }

        // Draw the sample color.
        private void picSample_Paint(object sender, PaintEventArgs e)
        {
            picSample.BackColor = SelectedColor;
        }

        private void timer_battery_Tick(object sender, EventArgs e)
        {
            ShowBatteryStatus();

            ShowBatteryStatus2();
        }

        int percent = 0;
        void ShowBatteryStatus()
        {
            // Change the icon.
            // Draw the battery image.
            int wid = pictureBox_battery.ClientSize.Width / 2;
            int hgt = pictureBox_battery.ClientSize.Height;
            Bitmap battery_bm = BatteryStuff.DrawBattery(
                percent / 100f,
                wid, hgt,
                Color.Transparent, Color.Black,
                Color.Lime, Color.White,
                true);

            // Convert the battery image into a square icon.
            Bitmap square_bm = new Bitmap(hgt, hgt);
            using (Graphics g = Graphics.FromImage(square_bm))
            {
                g.Clear(Color.Transparent);
                Point[] dest =
                {
                    new Point((int)(0.5 * wid), 0),
                    new Point((int)(1.5 * wid), 0),
                    new Point((int)(0.5 * wid), hgt),
                };
                Rectangle source = new Rectangle(0, 0, wid, hgt);
                g.DrawImage(battery_bm, dest, source, GraphicsUnit.Pixel);
            }
            pictureBox_battery.Image = square_bm;

            //  TBD 製作 ICON 用
            // Convert the bitmap into an icon.
            Icon icon = Icon.FromHandle(square_bm.GetHicon());
            //notifyIcon1.Icon = icon;

            percent += 2;
            if (percent > 100)
                percent = 0;
        }

        float a = 0;
        private void ShowBatteryStatus2()
        {
            PowerStatus status = SystemInformation.PowerStatus;
            float percent = status.BatteryLifePercent;

            a += 0.023f;
            percent -= a;

            if (percent < 0)
            {
                percent = 1;
                a = 0;
            }

            //richTextBox1.Text += percent.ToString("P0") + "\n";

            // Draw the battery image.
            Color bg_color = Color.Transparent;
            Color outline_color = Color.Gray;
            Color charged_color = Color.LightGreen;
            Color uncharged_color = Color.White;
            if (percent < 0.15f)
            {
                outline_color = Color.Black;
                charged_color = Color.Red;
                uncharged_color = Color.Yellow;
            }
            else if (percent < 0.25f)
            {
                outline_color = Color.Black;
                charged_color = Color.Orange;
            }
            pictureBox_battery2.Image = DrawBattery(
                percent,
                pictureBox_battery2.ClientSize.Width,
                pictureBox_battery2.ClientSize.Height,
                bg_color, outline_color,
                charged_color, uncharged_color,
                true);
        }

        private Bitmap DrawBattery(
            float percent, int w, int h,
            Color bg_color, Color outline_color,
            Color charged_color, Color uncharged_color,
            bool striped)
        {
            // Bail if there's no room to draw.
            if ((w < 1) || (h < 1))
            {
                return null;
            }

            Bitmap bm = new Bitmap(w, h);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // If the battery has a horizontal orientation,
                // rotate so we can draw it vertically.
                if (w > h)
                {
                    gr.RotateTransform(90, MatrixOrder.Append);
                    gr.TranslateTransform(w, 0, MatrixOrder.Append);
                    int temp = w;
                    w = h;
                    h = temp;
                }

                // Draw the battery.
                DrawVerticalBattery(gr, percent, w, h, bg_color,
                    outline_color, charged_color, uncharged_color, striped);
            }
            return bm;
        }

        // Draw a vertically oriented battery with
        // the indicated percentage filled in.
        private void DrawVerticalBattery(Graphics gr,
            float percent, int w, int h,
            Color bg_color, Color outline_color,
            Color charged_color, Color uncharged_color,
            bool striped)
        {
            gr.Clear(bg_color);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            // Make a rectangle for the main body.
            float thickness = h / 20f;
            RectangleF body_rect = new RectangleF(
                thickness * 0.5f, thickness * 1.5f,
                w - thickness, h - thickness * 2f);

            using (Pen pen = new Pen(outline_color, thickness))
            {
                // Fill the body with the uncharged color.
                using (Brush brush = new SolidBrush(uncharged_color))
                {
                    gr.FillRectangle(brush, body_rect);
                }

                // Fill the charged area.
                float charged_hgt = body_rect.Height * percent;
                RectangleF charged_rect = new RectangleF(
                    body_rect.Left, body_rect.Bottom - charged_hgt,
                    body_rect.Width, charged_hgt);
                using (Brush brush = new SolidBrush(charged_color))
                {
                    gr.FillRectangle(brush, charged_rect);
                }

                // Optionally stripe multiples of 25%
                if (striped)
                    for (int i = 1; i <= 3; i++)
                    {
                        float y = body_rect.Bottom - i * 0.25f * body_rect.Height;
                        gr.DrawLine(pen, body_rect.Left, y, body_rect.Right, y);
                    }

                // Draw the main body.
                gr.DrawPath(pen, MakeRoundedRect(body_rect, thickness, thickness, true, true, true, true));

                // Draw the positive terminal.
                RectangleF terminal_rect = new RectangleF(w / 2f - thickness, 0, 2 * thickness, thickness);
                gr.DrawPath(pen, MakeRoundedRect(terminal_rect, thickness / 2f, thickness / 2f, true, true, false, false));
            }
        }

        // Draw a rectangle in the indicated Rectangle
        // rounding the indicated corners.
        private GraphicsPath MakeRoundedRect(
            RectangleF rect, float xradius, float yradius,
            bool round_ul, bool round_ur, bool round_lr, bool round_ll)
        {
            // Make a GraphicsPath to draw the rectangle.
            PointF point1, point2;
            GraphicsPath path = new GraphicsPath();

            // Upper left corner.
            if (round_ul)
            {
                RectangleF corner = new RectangleF(rect.X, rect.Y, 2 * xradius, 2 * yradius);
                path.AddArc(corner, 180, 90);
                point1 = new PointF(rect.X + xradius, rect.Y);
            }
            else point1 = new PointF(rect.X, rect.Y);

            // Top side.
            if (round_ur)
            {
                point2 = new PointF(rect.Right - xradius, rect.Y);
            }
            else
            {
                point2 = new PointF(rect.Right, rect.Y);
            }
            path.AddLine(point1, point2);

            // Upper right corner.
            if (round_ur)
            {
                RectangleF corner = new RectangleF(rect.Right - 2 * xradius, rect.Y, 2 * xradius, 2 * yradius);
                path.AddArc(corner, 270, 90);
                point1 = new PointF(rect.Right, rect.Y + yradius);
            }
            else point1 = new PointF(rect.Right, rect.Y);

            // Right side.
            if (round_lr)
            {
                point2 = new PointF(rect.Right, rect.Bottom - yradius);
            }
            else
            {
                point2 = new PointF(rect.Right, rect.Bottom);
            }
            path.AddLine(point1, point2);

            // Lower right corner.
            if (round_lr)
            {
                RectangleF corner = new RectangleF(rect.Right - 2 * xradius, rect.Bottom - 2 * yradius, 2 * xradius, 2 * yradius);
                path.AddArc(corner, 0, 90);
                point1 = new PointF(rect.Right - xradius, rect.Bottom);
            }
            else point1 = new PointF(rect.Right, rect.Bottom);

            // Bottom side.
            if (round_ll)
            {
                point2 = new PointF(rect.X + xradius, rect.Bottom);
            }
            else
            {
                point2 = new PointF(rect.X, rect.Bottom);
            }
            path.AddLine(point1, point2);

            // Lower left corner.
            if (round_ll)
            {
                RectangleF corner = new RectangleF(rect.X, rect.Bottom - 2 * yradius, 2 * xradius, 2 * yradius);
                path.AddArc(corner, 90, 90);
                point1 = new PointF(rect.X, rect.Bottom - yradius);
            }
            else
            {
                point1 = new PointF(rect.X, rect.Bottom);
            }

            // Left side.
            if (round_ul)
            {
                point2 = new PointF(rect.X, rect.Y + yradius);
            }
            else
            {
                point2 = new PointF(rect.X, rect.Y);
            }
            path.AddLine(point1, point2);

            // Join with the start point.
            path.CloseFigure();

            return path;
        }

        // Display the next image.
        private void timer_gear_Tick(object sender, EventArgs e)
        {
            FrameNum = ++FrameNum % Frames.Length;
            pictureBox_gear.Image = Frames[FrameNum];
        }

        // Set the delay per frame.
        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            richTextBox1.Text += trackBar1.Value.ToString() + " ";
            timer_gear.Interval = 1000 / trackBar1.Value;
            lb_fps.Text = trackBar1.Value.ToString();
        }

        // Draw the atom.
        private void timer_atom_Tick(object sender, EventArgs e)
        {
            // Refresh the image with the background.
            Bitmap bm = (Bitmap)Background.Clone();

            // Draw the atom.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Transform = Transform;
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.FillEllipse(Brushes.Green,
                    Points[AtomPoint].X - 0.075f,
                    Points[AtomPoint].Y - 0.075f,
                    0.15f, 0.15f);
            }

            // Display the result.
            pictureBox_atom.Image = bm;

            // Move the atom.
            AtomPoint = (AtomPoint + 1) % Points.Count;
        }

        // Draw the graph on a Bitmap.
        private void DrawGraph(Graphics gr)
        {
            // Generate the points.
            double t = 0;
            const double dt = Math.PI / 100.0;
            const double two_pi = Math.PI;
            Points = new List<PointF>();
            while (t <= two_pi)
            {
                double r = 2 * Math.Sin(5 * t);
                float x = (float)(r * Math.Cos(t));
                float y = (float)(r * Math.Sin(t));
                Points.Add(new PointF(x, y));
                t += dt;
            }

            // Draw the curve.
            using (Pen thin_pen = new Pen(Color.Red, 0))
            {
                gr.DrawPolygon(thin_pen, Points.ToArray());
            }
        }

        int card_no = 0;
        int card_no2 = 0;
        private void timer_card_Tick(object sender, EventArgs e)
        {
            show_card(card_no);
            card_no++;
            if (card_no > (13 * 4 + 7))
                card_no = 0;

            show_card2(card_no2);
            card_no2++;
            if (card_no2 >= 13 * 4)
                card_no2 = 0;
        }

        void show_card(int card_no)
        {
            Image img = Image.FromFile(@"C:\______test_files1\__pic\_poker_card\cards1.png");
            int W = img.Width;
            int H = img.Height;
            int w = W / 13;
            int h = H / 5;

            int index_x = card_no % 13;
            int index_y = card_no / 13;

            GraphicsUnit units = GraphicsUnit.Pixel;
            //來源矩形的大小會決定要將未縮放原始影像的哪個部分繪製到螢幕上。

            int sx;
            int sy;
            int sw;
            int sh;
            int dx;
            int dy;
            int dw;
            int dh;

            //使用兩個Rectangle結構
            //source
            sx = w * index_x;
            sy = h * index_y;
            sw = w;
            sh = h;
            //destination
            dx = 0;
            dy = 0;
            dw = w;
            dh = h;

            // Create rectangle for displaying image.
            Rectangle destRect = new Rectangle(dx, dy, dw, dh);

            // Create rectangle for source image.
            Rectangle srcRect3 = new Rectangle(sx, sy, sw, sh);

            // Draw image to screen.
            gc.DrawImage(img, destRect, srcRect3, units);

            pictureBox_card.Image = bitmap_card;
            pictureBox_card.Size = new Size(w, h);
        }

        //int card_no2 = 0;
        private void timer_card2_Tick(object sender, EventArgs e)
        {
            show_card2(card_no2);
            card_no2++;
            if (card_no2 > 13 * 4)
                card_no2 = 0;
        }

        void show_card2(int card_no)
        {
            Image img = Image.FromFile(@"C:\______test_files1\__pic\_poker_card\cards2.png");
            int W = img.Width;
            int H = img.Height;
            int w = W / 13;
            int h = H / 4;

            int index_x = card_no % 13;
            int index_y = card_no / 13;

            GraphicsUnit units = GraphicsUnit.Pixel;
            //來源矩形的大小會決定要將未縮放原始影像的哪個部分繪製到螢幕上。

            int sx;
            int sy;
            int sw;
            int sh;
            int dx;
            int dy;
            int dw;
            int dh;

            //使用兩個Rectangle結構
            //source
            sx = w * index_x;
            sy = h * index_y;
            sw = w;
            sh = h;
            //destination
            dx = 0;
            dy = 0;
            dw = w;
            dh = h;

            // Create rectangle for displaying image.
            Rectangle destRect = new Rectangle(dx, dy, dw, dh);

            // Create rectangle for source image.
            Rectangle srcRect3 = new Rectangle(sx, sy, sw, sh);

            // Draw image to screen.
            gc2.DrawImage(img, destRect, srcRect3, units);

            pictureBox_card2.Image = bitmap_card;
            pictureBox_card2.Size = new Size(w, h);
        }

        private double Theta = 0;
        private const double Dtheta = Math.PI / 5;

        // Draw the atom.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(this.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            Theta += Dtheta;

            const int radius = 3;
            int cx = 50, cy = 400, rx = 45, ry = 15;
            Rectangle rect = new Rectangle(-rx, -ry, 2 * rx, 2 * ry);
            double x, y;
            e.Graphics.RotateTransform(60, MatrixOrder.Append);
            e.Graphics.TranslateTransform(cx, cy, MatrixOrder.Append);
            e.Graphics.DrawEllipse(Pens.Red, rect);
            x = rx * Math.Cos(Theta);
            y = ry * Math.Sin(Theta);
            e.Graphics.FillEllipse(Brushes.Red,
                (int)(x - radius), (int)(y - radius),
                2 * radius, 2 * radius);

            e.Graphics.ResetTransform();
            e.Graphics.RotateTransform(-60, MatrixOrder.Append);
            e.Graphics.TranslateTransform(cx, cy, MatrixOrder.Append);
            e.Graphics.DrawEllipse(Pens.Red, rect);
            x = rx * Math.Cos(-Theta * 0.9);
            y = ry * Math.Sin(-Theta * 0.9);
            e.Graphics.FillEllipse(Brushes.Green,
                (int)(x - radius), (int)(y - radius),
                2 * radius, 2 * radius);

            e.Graphics.ResetTransform();
            e.Graphics.TranslateTransform(cx, cy, MatrixOrder.Append);
            e.Graphics.DrawEllipse(Pens.Red, rect);
            x = rx * Math.Cos(Theta * 0.8);
            y = ry * Math.Sin(Theta * 0.8);
            e.Graphics.FillEllipse(Brushes.Blue,
                (int)(x - radius), (int)(y - radius),
                2 * radius, 2 * radius);

            e.Graphics.ResetTransform();
            e.Graphics.FillEllipse(Brushes.Black,
                cx - radius, cy - radius,
                2 * radius, 2 * radius);
        }

        private void timer_atom2_Tick(object sender, EventArgs e)
        {
            //for atom2
            Refresh();
        }

        #region 畫random曲線
        private void timer_random_Tick(object sender, EventArgs e)
        {
            DrawGraph();
        }

        private void DrawGraph()
        {
            try
            {
                int y = YValue;
                // Generate the next value.
                NewValue();

                // Plot the new value.
                PlotValue(y, YValue);
                y = YValue;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error : " + ex.Message + "\n";
            }
        }

        // Generate the next value.
        private Random Rnd = new Random();
        private void NewValue()
        {
            // Delay a bit before calculating the value.
            DateTime stop_time = DateTime.Now.AddMilliseconds(1);
            while (DateTime.Now < stop_time) { };

            // Calculate the next value.
            YValue += Rnd.Next(-4, 5);
            if (YValue < 0) YValue = 0;
            if (YValue >= pictureBox_random.ClientSize.Height - 1)
                YValue = pictureBox_random.ClientSize.Height - 1;
        }

        // Plot a new value.
        private void PlotValue(int old_y, int new_y)
        {
            // Invoke not required. Go ahead and plot.
            // Make the Bitmap and Graphics objects.
            int wid = pictureBox_random.ClientSize.Width;
            int hgt = pictureBox_random.ClientSize.Height;
            Bitmap bm = new Bitmap(wid, hgt);
            Graphics grnd = Graphics.FromImage(bm);

            // Move the old data one pixel to the left.
            grnd.DrawImage(pictureBox_random.Image, -1, 0);

            // Erase the right edge and draw guide lines.
            grnd.DrawLine(Pens.Blue, wid - 1, 0, wid - 1, hgt - 1);
            for (int i = Ymid; i <= pictureBox_random.ClientSize.Height; i += GridStep)
            {
                grnd.DrawLine(Pens.LightBlue, wid - 2, i, wid - 1, i);
            }
            for (int i = Ymid; i >= 0; i -= GridStep)
            {
                grnd.DrawLine(Pens.LightBlue, wid - 2, i, wid - 1, i);
            }

            // Plot a new pixel.
            grnd.DrawLine(Pens.White, wid - 2, old_y, wid - 1, new_y);

            // Display the result.
            pictureBox_random.Image = bm;
            pictureBox_random.Refresh();

            grnd.Dispose();
        }
        #endregion

        private void timer_spin_Tick(object sender, EventArgs e)
        {
            this.pictureBox_spin.Refresh();
        }

        float spin = 0;
        private void pictureBox_spin_Paint(object sender, PaintEventArgs e)
        {
            int w = pictureBox_spin.Width;
            int h = pictureBox_spin.Height;
            int cx = w / 2;
            int cy = h / 2;
            int r = Math.Min((w / 2) * 4 / 5, (h / 2) * 4 / 5);
            int px = cx + (int)(r * Math.Cos(spin));
            int py = cy + (int)(r * Math.Sin(spin));
            spin += 0.30f;

            using (Pen pen = new Pen(Color.Black, 0))
            {
                e.Graphics.DrawLine(pen, cx, cy, px, py);
            }

            using (Pen pen = new Pen(Color.Black, 0))
            {
                const float radius = 10;
                //e.Graphics.DrawLine(pen, cx, cy, px, py);
                e.Graphics.DrawEllipse(Pens.Blue, px - radius, py - radius, 2 * radius, 2 * radius);
                e.Graphics.FillEllipse(new SolidBrush(Color.Blue), px - radius, py - radius, 2 * radius, 2 * radius);
            }
        }

        double angle = 12;
        private void timer_circle_Tick(object sender, EventArgs e)
        {
            draw_circles();
            angle++;
        }

        void draw_circles()
        {
            int w = pictureBox_circle.Width;
            int h = pictureBox_circle.Height;

            Bitmap bitmap1 = new Bitmap(w, h);

            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(Pens.Blue, 100, 100, 100, 100);

            int cx = w / 2;
            int cy = h / 2;
            //int r = Math.Min((w / 2) * 4 / 5, (h / 2) * 4 / 5) / 2;
            int r = 15;
            int px;
            int py;

            int radius = 10;
            Point pt = new Point();

            double i;
            int r2 = r;
            //richTextBox1.Text += "angle = " + angle.ToString() + " ";
            for (i = 12; i < angle; i++)
            {
                if (i == 0)
                {
                    pt = new Point(cx, cy);
                }
                else
                {
                    //r2 = r + (((int)i - 1) / 12) * 15;
                    r2 = r + (int)i * 3 / 2;
                    px = cx + (int)(r2 * cosd(i * 30));
                    py = cy + (int)(r2 * sind(i * 30));
                    pt = new Point(px, py);
                }
                //richTextBox1.Text += i.ToString() + "  x = " + pt.X.ToString() + " y = " + pt.Y.ToString() + "  ";
                FillCircle(g, pt, radius, Color.Red);
            }
            pictureBox_circle.Image = bitmap1;
            if (angle == 100)
            {
                angle = 12;
            }
            //richTextBox1.Text += "\n";
            /*
            using (Pen pen = new Pen(Color.Black, 0))
            {
                e.Graphics.DrawLine(pen, cx, cy, px, py);
            }

            using (Pen pen = new Pen(Color.Black, 0))
            {
                const float radius = 10;
                //e.Graphics.DrawLine(pen, cx, cy, px, py);
                e.Graphics.DrawEllipse(Pens.Blue, px - radius, py - radius, 2 * radius, 2 * radius);
                e.Graphics.FillEllipse(new SolidBrush(Color.Blue), px - radius, py - radius, 2 * radius, 2 * radius);
            }
            */
        }

        private void FillCircle(Graphics g, PointF center, int radius, Color c)
        {
            SolidBrush sb = new SolidBrush(c);

            // Fill the circle
            g.FillEllipse(sb, new RectangleF(center.X - radius, center.Y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            sb.Dispose();
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

        //for pictureBox_stock ST

        // Get a new stock price.
        private int PointNum = 0;
        private void SavePrice()
        {
            Prices.Add(new PointF(PointNum++, GetPrice()));
            Times.Add(DateTime.Now);

            // Redraw.
            pictureBox_stock.Refresh();
        }

        // Get the stock price.
        private float GetPrice()
        {
            Random r = new Random();
            return r.Next(10);
        }

        // Draw the graph.
        private void pictureBox_stock_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox_stock.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            if (Times.Count == 0)
                return;

            // Define the graph area.
            GraphXmin = 80;
            GraphXmax = pictureBox_stock.ClientSize.Width - 10;
            GraphYmin = 40;
            GraphYmax = pictureBox_stock.ClientSize.Height - 80;
            Rectangle graph_area = new Rectangle(GraphXmin, GraphYmin, GraphXmax - GraphXmin, GraphYmax - GraphYmin);

            // Get bounds.
            GetBounds();

            // Draw with the identity transformation.
            DrawWithoutTransformation(e.Graphics);

            // Fill the graph area.
            e.Graphics.FillRectangle(Brushes.White, graph_area);

            // Draw things in the graph's world coordinate space.
            DrawInGraphCoordinates(e.Graphics, GraphXmin, GraphXmax, GraphYmin, GraphYmax);

            // Save the graph's coordinate transformation.
            Matrix graph_transformation = e.Graphics.Transform;

            // Draw things that are positioned using the graph's
            // transformation but that are drawn in pixels.
            DrawWithGraphTransformation(e.Graphics, graph_transformation);
        }

        // Get the world coordinate bounds.
        private void GetBounds()
        {
            float ymin = Prices.Min(pt => pt.Y);
            float ymax = Prices.Max(pt => pt.Y);
            float ydiff = 1.2f * (ymax - ymin);
            if (ydiff < 20)
                ydiff = 20;
            float ymid = (ymin + ymax) / 2f;
            Wymin = ymid - ydiff / 2f;
            Wymax = Wymin + ydiff;

            // Make sure we don't have too many values.
            const float pix_per_x = 20;
            while ((Times.Count - 1) * pix_per_x > (GraphXmax - GraphXmin))
            {
                Times.RemoveAt(0);
                Prices.RemoveAt(0);
            }

            Wxmin = Prices.Min(pt => pt.X);
            Wxmax = Wxmin + (GraphXmax - GraphXmin) / pix_per_x;
        }

        // Draw things that use the identity transformation.
        private void DrawWithoutTransformation(Graphics gr)
        {
            // Draw the main title centered on the top.
            using (Font title_font = new Font("Times New Roman", 20))
            {
                using (StringFormat string_format = new StringFormat())
                {
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    Point title_center = new Point(pictureBox_stock.ClientSize.Width / 2, 20);
                    gr.DrawString(Symbol, title_font, Brushes.Blue, title_center, string_format);
                }
            }
        }

        // Draw things in the graph's world coordinate.
        private void DrawInGraphCoordinates(Graphics gr, int xmin, int xmax, int ymin, int ymax)
        {
            // Define the world coordinate rectangle.
            RectangleF world_rect = new RectangleF(Wxmin, Wymin, Wxmax - Wxmin, Wymax - Wymin);

            // Define the points to which the rectangle's upper left,
            // upper right, and lower right corners should map.
            // Note the vertical flip so large Y values are at the top.
            PointF[] window_points =
            {
                new PointF(xmin, ymax),
                new PointF(xmax, ymax),
                new PointF(xmin, ymin),
            };

            // Define the transformation.
            Matrix graph_transformation = new Matrix(world_rect, window_points);

            // Apply the transformation.
            gr.Transform = graph_transformation;

            // Plot the data lines.
            using (Pen green_pen = new Pen(Color.Green, 0))
            {
                for (int i = 1; i < Prices.Count; i++)
                {
                    gr.DrawLine(green_pen, Prices[i - 1], Prices[i]);
                }
            }
        }

        // Draw things that are positioned using the graph's
        // transformation but that are drawn in pixels.
        private void DrawWithGraphTransformation(Graphics gr, Matrix graph_matrix)
        {
            // Reset to the identity transformation.
            gr.ResetTransform();

            // Draw the axes.
            using (Font label_font = new Font("Times New Roman", 8))
            {
                // Draw the Y axis.
                using (StringFormat label_format = new StringFormat())
                {
                    label_format.Alignment = StringAlignment.Far;
                    label_format.LineAlignment = StringAlignment.Center;

                    // Draw the tick marks and labels.
                    int ystart = 10 * (int)(Wymin / 10);
                    if (ystart < Wymin) ystart += 10;
                    for (int y = ystart; y <= Wymax; y += 10)
                    {
                        // Axis mark.
                        PointF[] tick_points = 
                        {
                            new PointF(Wxmin, y),
                            new PointF(Wxmax, y),
                        };
                        graph_matrix.TransformPoints(tick_points);
                        // Horizontal line.
                        gr.DrawLine(Pens.LightBlue,
                            tick_points[0].X, tick_points[0].Y,
                            tick_points[1].X, tick_points[1].Y);
                        //// Tic mark.
                        //gr.DrawLine(Pens.Black,
                        //    tick_points[0].X, tick_points[0].Y,
                        //    tick_points[0].X + 10, tick_points[0].Y);

                        // Label.
                        PointF[] label_point = { new PointF(0, y) };
                        graph_matrix.TransformPoints(label_point);
                        gr.DrawString(y.ToString("C3"), label_font, Brushes.Black, GraphXmin - 10, label_point[0].Y, label_format);
                    }
                }

                // Draw the X axis.
                // Draw the tick marks and labels.
                for (int x = 0; x < Times.Count; x++)
                {
                    // Axis mark.
                    PointF[] tick_points =
                    {
                        new PointF(Wxmin + x, Wymin),
                        new PointF(Wxmin + x, Wymax)
                    };
                    graph_matrix.TransformPoints(tick_points);
                    // Vertical line.
                    gr.DrawLine(Pens.LightBlue,
                        tick_points[0].X, tick_points[0].Y,
                        tick_points[1].X, tick_points[1].Y);
                    // Tick mark.
                    gr.DrawLine(Pens.Black,
                        tick_points[0].X, tick_points[0].Y,
                        tick_points[0].X, tick_points[0].Y - 10);

                    // Label.
                    DrawXLabel(gr,
                        Times[x].ToShortTimeString(),
                        label_font, Brushes.Black,
                        tick_points[0].X, GraphYmax + 10);
                }

                // Draw the X axis.
                PointF[] x_points = 
                {
                    new PointF(Wxmin, Wymin),
                    new PointF(Wxmax, Wymin),
                };
                graph_matrix.TransformPoints(x_points);
                gr.DrawLine(Pens.Black, x_points[0], x_points[1]);

                // Draw the Y axis.
                PointF[] y_points = 
                    {
                        new PointF(Wxmin, Wymin),
                        new PointF(Wxmin, Wymax),
                    };
                graph_matrix.TransformPoints(y_points);
                gr.DrawLine(Pens.Black, y_points[0], y_points[1]);


                // Plot the data points.
                // Copy the points so we don't mess up the original values.
                TransformedValues = (PointF[])Prices.ToArray().Clone();

                // Transform the points to see where they are on the PictureBox.
                graph_matrix.TransformPoints(TransformedValues);

                // Draw the points.
                foreach (PointF pt in TransformedValues)
                {
                    gr.FillEllipse(Brushes.Lime,
                        pt.X - Radius, pt.Y - Radius, 2 * Radius, 2 * Radius);
                    gr.DrawEllipse(Pens.Black,
                        pt.X - Radius, pt.Y - Radius, 2 * Radius, 2 * Radius);
                }
            }

            // Label the axes.
            using (Font axis_font = new Font("Times New Roman", 14))
            {
                // Label the Y axis.
                using (StringFormat ylabel_format = new StringFormat())
                {
                    ylabel_format.Alignment = StringAlignment.Center;
                    ylabel_format.LineAlignment = StringAlignment.Near;
                    gr.ResetTransform();
                    gr.RotateTransform(-90);
                    float cx = 0;
                    float cy = (GraphYmin + GraphYmax) / 2;
                    gr.TranslateTransform(cx, cy, MatrixOrder.Append);
                    gr.DrawString("Price", axis_font,
                        Brushes.Green, 0, 0, ylabel_format);
                    gr.ResetTransform();
                }

                // Label the X axis.
                using (StringFormat xlabel_format = new StringFormat())
                {
                    xlabel_format.Alignment = StringAlignment.Center;
                    xlabel_format.LineAlignment = StringAlignment.Far;
                    RectangleF xlabel_rect = new RectangleF(
                        GraphXmin, GraphYmax,
                        GraphXmax - GraphXmin,
                        pictureBox_stock.ClientSize.Height - GraphYmax);
                    gr.DrawString("Time", axis_font,
                        Brushes.Green, xlabel_rect, xlabel_format);
                }
            }
        }

        // Draw a string rotated 90 degrees at the given position.
        private void DrawXLabel(Graphics gr, string txt, Font label_font,
            Brush label_brush, float x, float y)
        {
            // Transform to center the label's right edge
            // at the origin when we draw at the origin.
            gr.ResetTransform();

            // Rotate the translated text.
            gr.RotateTransform(90, MatrixOrder.Append);

            // Translate to the final destination.
            gr.TranslateTransform(x, y, MatrixOrder.Append);

            // Draw the label.
            using (StringFormat label_format = new StringFormat())
            {
                // Draw so the text is centered vertically and
                // left aligned at the origin.
                label_format.Alignment = StringAlignment.Near;
                label_format.LineAlignment = StringAlignment.Center;

                // Draw the text at the origin.
                gr.DrawString(txt, label_font, label_brush, 0, 0, label_format);
            }

            gr.ResetTransform();
        }

        // If the mouse is hovering over a data point,
        // set the PictureBox's tooltip.
        private void pictureBox_stock_MouseMove(object sender, MouseEventArgs e)
        {
            if (TransformedValues == null) return;

            // See what tool tip to display.
            string tip = "";
            for (int i = 0; i < TransformedValues.Length; i++)
            {
                if ((Math.Abs(e.X - TransformedValues[i].X) < Radius) &&
                    (Math.Abs(e.Y - TransformedValues[i].Y) < Radius))
                {
                    tip = Prices[i].Y.ToString("C3");
                    break;
                }
            }

            // Set the new tool tip.
            if (tipData.GetToolTip(pictureBox_stock) != tip)
            {
                tipData.SetToolTip(pictureBox_stock, tip);
            }
        }

        private void timer_stock_Tick(object sender, EventArgs e)
        {
            // Get the next price.
            SavePrice();
        }

        //for pictureBox_stock SP


        //畫雷達掃瞄圖 ST
        private void timer_radar_Tick(object sender, EventArgs e)
        {
            //pen
            radar_p = new Pen(Color.Green, 1f);

            //graphics
            radar_g = Graphics.FromImage(radar_bmp);

            //calculate x, y coordinate of HAND
            int tu = (u - lim) % 360;

            if (u >= 0 && u <= 180)
            {
                //right half
                //u in degree is converted into radian.

                x = cx + (int)(radar_HAND * Math.Sin(Math.PI * u / 180));
                y = cy - (int)(radar_HAND * Math.Cos(Math.PI * u / 180));
            }
            else
            {
                x = cx - (int)(radar_HAND * -Math.Sin(Math.PI * u / 180));
                y = cy - (int)(radar_HAND * Math.Cos(Math.PI * u / 180));
            }

            if (tu >= 0 && tu <= 180)
            {
                //right half
                //tu in degree is converted into radian.

                tx = cx + (int)(radar_HAND * Math.Sin(Math.PI * tu / 180));
                ty = cy - (int)(radar_HAND * Math.Cos(Math.PI * tu / 180));
            }
            else
            {
                tx = cx - (int)(radar_HAND * -Math.Sin(Math.PI * tu / 180));
                ty = cy - (int)(radar_HAND * Math.Cos(Math.PI * tu / 180));
            }

            //draw circle
            radar_g.DrawEllipse(radar_p, 0, 0, radar_WIDTH, radar_HEIGHT);  //bigger circle
            //radar_g.DrawEllipse(radar_p, 80, 80, radar_WIDTH - 160, radar_HEIGHT - 160);    //smaller circle
            radar_g.DrawEllipse(radar_p, 70, 70, radar_WIDTH - 140, radar_HEIGHT - 140);    //smaller circle

            //draw perpendicular line
            radar_g.DrawLine(radar_p, new Point(cx, 0), new Point(cx, radar_HEIGHT)); // UP-DOWN
            radar_g.DrawLine(radar_p, new Point(0, cy), new Point(radar_WIDTH, cy)); //LEFT-RIGHT

            //draw HAND
            radar_g.DrawLine(new Pen(Color.Black, 1f), new Point(cx, cy), new Point(tx, ty));
            radar_g.DrawLine(radar_p, new Point(cx, cy), new Point(x, y));

            //load bitmap in pictureBox_radar
            pictureBox_radar.Image = radar_bmp;

            //dispose
            radar_p.Dispose();
            radar_g.Dispose();

            //update
            u += 2;
            if (u == 360)
            {
                u = 0;
            }

        }

        //畫雷達掃瞄圖 SP

        int offset = 0;
        void draw_hex()
        {
            int W = pictureBox_hex.Width;
            int H = pictureBox_hex.Height;
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Pink);
            g.SmoothingMode = SmoothingMode.AntiAlias;

            int cx = W / 2;
            int cy = H / 2;
            int r1 = Math.Min(W, H) * 4 / 10;
            int r2 = Math.Min(W, H) * 3 / 10;

            int x_st = cx;
            int y_st = cy;

            Point[] points1 = new Point[6];
            Point[] points2 = new Point[6];

            for (int i = 0; i < 6; i++)
            {
                points1[i] = new Point(cx + (int)(r1 * cosd(60 * i + offset * 10)), cy + (int)(r1 * sind(60 * i + offset * 10)));
                points2[i] = new Point(cx + (int)(r2 * cosd(60 * i - offset * 10)), cy + (int)(r2 * sind(60 * i - offset * 10)));
            }

            g.DrawPolygon(new Pen(Color.Red, 3), points1);
            g.DrawPolygon(new Pen(Color.Red, 3), points2);

            pictureBox_hex.Image = bitmap1;
            offset++;
            if (offset > 5)
                offset = 0;
        }

        private void timer_hex_Tick(object sender, EventArgs e)
        {
            draw_hex();
        }

        private void timer_random_color_Tick(object sender, EventArgs e)
        {
            this.pictureBox_random_color.Invalidate();
        }

        private void pictureBox_random_color_Paint(object sender, PaintEventArgs e)
        {
            int w = this.pictureBox_random_color.Width;
            int h = this.pictureBox_random_color.Height;
            int i;
            Random r = new Random();
            for (i = 0; i < h; i++)
            {
                //製作任意顏色
                e.Graphics.DrawLine(new Pen(Color.FromArgb(r.Next(0, 256), r.Next(0, 256), r.Next(0, 256))), 0, i, w, i);   //r.Next(0, 256) 產出0~255之間的整數
            }
        }
    }
}
