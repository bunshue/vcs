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

//方案總管/加入/現有項目/選取Rainbow.cs, 把 namespace 改成 vcs_Draw3
//方案總管/加入/現有項目/選取BatteryStuff.cs, 把 namespace 改成 vcs_Draw3

namespace vcs_Draw3
{
    public partial class Form1 : Form
    {
        Graphics g1;
        Graphics g2;
        Pen p;
        //SolidBrush sb;
        //Bitmap bitmap1;
        Bitmap bitmap2;
        Bitmap bitmap3;

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

        int label_size_w_old = 0;
        int label_size_h_old = 0;

        // The PictureBox's current size.
        private float StartWidth;
        private int StartHeight;
        private float EndWidth = 260;
        private float Dx, CurrentWidth;
        private int TicksToGo, TotalTicks;

        // Information about the string to draw.
        private const string LabelText = "群曜醫電股份有限公司";
        //private const string LabelText = "C# Programming";
        private Font TextFont;
        private float[] CharacterWidths;
        private float TotalCharacterWidth;

        Graphics gc;
        Bitmap bitmap_card;
        Graphics gc2;
        Bitmap bitmap_card2;

        public Form1()
        {
            InitializeComponent();

            show_item_location();
            //pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            this.DoubleBuffered = true;

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

            //for atom
            // Enable double buffering.
            this.DoubleBuffered = true;

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


        }


        private void Form1_Load(object sender, EventArgs e)
        {
            g1 = panel1.CreateGraphics();
            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。

            g1.Clear(Color.Red);             //useless??
            panel1.BackColor = Color.Pink;

            FormBorderStyle = FormBorderStyle.FixedDialog;
            MinimizeBox = false;
            MaximizeBox = false;
            DoubleBuffered = true;
            StartPosition = FormStartPosition.CenterScreen;


            timer_rainbow.Interval = Interval;
            SelectedColor = Color.Red;
            SelectedRainbowNumber = 0;


            label_size_w_old = label_size.Size.Width;
            label_size_h_old = label_size.Size.Height;


            // Set the initial size.
            StartWidth = pictureBox_stretching.Size.Width;
            StartHeight = pictureBox_stretching.Size.Height;
            CurrentWidth = StartWidth;

            // Stretch for 2 seconds.
            TotalTicks = 2 * 1000 / timer1.Interval;
            Dx = (EndWidth - StartWidth) / TotalTicks;

            // Make the font and measure the characters.
            CharacterWidths = new float[LabelText.Length];
            TextFont = new Font("Times New Roman", 16);
            using (Graphics gr = this.CreateGraphics())
            {
                for (int i = 0; i < LabelText.Length; i++)
                {
                    SizeF ch_size = gr.MeasureString(LabelText.Substring(i, 1), TextFont);
                    CharacterWidths[i] = ch_size.Width;
                }
            }
            TotalCharacterWidth = CharacterWidths.Sum();

            CurrentWidth = StartWidth;
            pictureBox_stretching.Size = new Size((int)StartWidth, pictureBox_stretching.Size.Height);
            pictureBox_stretching.Refresh();
            TicksToGo = TotalTicks;

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


        }


        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 900;
            y_st = 10;
            dx = 120;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            button3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            button9.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            button18.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 6);

            button21.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 8);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            pictureBox_gear.Size = new Size(280, 280);
            pictureBox_gear.Location = new Point(richTextBox1.Location.X - 300, richTextBox1.Location.Y);
            trackBar1.Location = new Point(richTextBox1.Location.X - 300 - 20, richTextBox1.Location.Y - 50);
            lb_fps.Location = new Point(richTextBox1.Location.X - 40, richTextBox1.Location.Y - 45);

            pictureBox_atom.Size = new Size(300, 300);
            pictureBox_atom.Location = new Point(pictureBox_gear.Location.X - 340, pictureBox_gear.Location.Y - 50);
        }

        bool isRunning1 = false;
        bool isRunning2 = false;
        bool isRunning3 = false;
        bool isRunning4 = false;

        string filename = "C:\\______test_files\\picture1.jpg";
        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            //pictureBox2.Image = Image.FromFile(filename);

            bitmap3 = new Bitmap(filename);
            richTextBox1.Text += "W = " + bitmap3.Width.ToString() + " H = " + bitmap3.Height.ToString() + "\n";
            pictureBox2.Size = bitmap3.Size;
            pictureBox2.Image = bitmap3;
            pictureBox2.Location = new Point(570, 10);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (bitmap3 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

            if (isRunning1 == false)
            {
                isRunning1 = true;
                timer4.Enabled = true;
                richTextBox1.Text += "ST\n";
            }
            else
            {
                isRunning1 = false;
                timer4.Enabled = false;
                richTextBox1.Text += "SP\n";
            }

        }

        int tt = 0;
        int xx2 = 0;
        int yy2 = 0;
        double gg = 9.8;
        private void button2_Click(object sender, EventArgs e)
        {
            if (bitmap3 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

            if (isRunning3 == false)
            {
                isRunning3 = true;
                timer6.Enabled = true;
                richTextBox1.Text += "ST\n";
                tt = 0;
                xx2 = 0;
                yy2 = 0;
            }
            else
            {
                isRunning3 = false;
                timer6.Enabled = false;
                richTextBox1.Text += "SP\n";
            }


        }

        private void button3_Click(object sender, EventArgs e)
        {
            Bitmap bitmap_old;
            bitmap_old = new Bitmap(filename);
            pictureBox2.Image = bitmap_old;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (bitmap3 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

            if (isRunning2 == false)
            {
                isRunning2 = true;
                timer5.Enabled = true;
                richTextBox1.Text += "ST\n";
            }
            else
            {
                isRunning2 = false;
                timer5.Enabled = false;
                richTextBox1.Text += "SP\n";
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (bitmap3 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

            if (isRunning2 == false)
            {
                isRunning2 = true;
                timer8.Enabled = true;
                richTextBox1.Text += "ST\n";
                round8 = 0;
            }
            else
            {
                isRunning2 = false;
                timer8.Enabled = false;
                richTextBox1.Text += "SP\n";
            }

        }

        Bitmap bmp;
        Graphics g;
        Pen p4;
        int t;

        //int WIDTH = 720;
        int HEIGHT = 300;
        int AMPLITUDE = 150;

        private void button6_Click(object sender, EventArgs e)
        {
            /*
            if (bitmap3 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }
             */

            if (isRunning4 == false)
            {
                isRunning4 = true;
                timer7.Enabled = true;
                richTextBox1.Text += "ST\n";

                pictureBox2.Width = 640;
                pictureBox2.Height = 480;
                pictureBox2.Location = new Point(400, 300);

                //create Bitmap
                bmp = null;
                bmp = new Bitmap(pictureBox2.Size.Width, pictureBox2.Size.Height);

                //background color
                //this.BackColor = Color.Black;

                //center
                //cx = WIDTH / 2;
                //cy = HEIGHT / 2;

                //initial degree of HAND
                //u = 0;

                //timer1.Enabled = true;
                pictureBox2.Image = null;
                t = 0;
                DrawXY();
                DrawYLine();

                //timer1.Enabled = true;
            }
            else
            {
                isRunning4 = false;
                timer7.Enabled = false;
                richTextBox1.Text += "SP\n";
            }
        }

        private void DrawXY()//画X轴Y轴
        {
            //graphics
            g = Graphics.FromImage(bmp);
            System.Drawing.Point px1 = new System.Drawing.Point(this.pictureBox1.Width * 10 / 100, this.pictureBox1.Height * 90 / 100);
            System.Drawing.Point px2 = new System.Drawing.Point(this.pictureBox1.Width * 90 / 100, this.pictureBox1.Height * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            System.Drawing.Point py1 = new System.Drawing.Point(this.pictureBox1.Width * 10 / 100, this.pictureBox1.Height * 90 / 100);
            System.Drawing.Point py2 = new System.Drawing.Point(this.pictureBox1.Width * 10 / 100, this.pictureBox1.Height * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
            g.Dispose();
        }

        private void DrawYLine()    //画X轴刻度
        {
            //graphics
            g = Graphics.FromImage(bmp);
            for (int i = 1; i < 9; i++)
            {
                System.Drawing.Point py1 = new System.Drawing.Point(100 * i, this.pictureBox1.Height - 5);
                System.Drawing.Point py2 = new System.Drawing.Point(100 * i, this.pictureBox1.Height);
                g.DrawLine(new Pen(Brushes.Red, 1), py1, py2);
            }
            g.Dispose();
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private Random Rand = new Random();
        private Bitmap Bm;
        private Graphics Gr;
        private void button9_Click(object sender, EventArgs e)
        {
            if (button9.Text == "畫任意矩形 ST")
            {
                timer_random_rectangle.Enabled = true;
                button9.Text = "畫任意矩形 SP";

                Bm = new Bitmap(pictureBox1.Width, pictureBox1.Height);
                Gr = Graphics.FromImage(Bm);
                pictureBox1.BackColor = Color.Pink;
                pictureBox1.Image = Bm;
            }
            else
            {
                timer_random_rectangle.Enabled = false;
                button9.Text = "畫任意矩形 ST";
            }
        }

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

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

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

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }


        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


        int dw = 0;
        int dh = 0;
        double degree = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            int r = 150;
            int x;
            int y;
            degree += 0.1;
            x = r + (int)(r * Math.Cos(degree * Math.PI / 180));
            y = r + (int)(r * Math.Sin(degree * Math.PI / 180));

            g1.Clear(Color.Pink);

            Point point1a = new Point(r, r);
            Point point2a = new Point(x, y);
            g1.DrawLine(p, point1a, point2a);     // Draw line to screen.

            /*
             * 可以變大變小的Label
             * 屬性
             * BackColor
             * BorderStype 改 FixedSingle
             * AutoSize 改 False
             * 改 Size
            */
            dw++;
            dh++;
            if (dw > 50)
                dw = 0;
            if (dh > 50)
                dh = 0;
            label_size.Size = new Size(label_size_w_old + dw, label_size_h_old + dh);

            CurrentWidth += Dx;
            pictureBox_stretching.Size = new Size((int)CurrentWidth, StartHeight);
            pictureBox_stretching.Refresh();

            // If we're done moving, disable the Timer.
            if (--TicksToGo <= 0)
            {
                timer1.Enabled = false;
                //TicksToGo = TotalTicks;
            }

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

        private void timer3_Tick(object sender, EventArgs e)
        {
            int w = pictureBox1.Width;
            int h = pictureBox1.Height;
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

            pictureBox1.Image = bitmap2;


        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                //新建圖檔, 初始化畫布
                bitmap2 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
                g2 = Graphics.FromImage(bitmap2);
                g2.Clear(Color.White);
                pictureBox1.Image = bitmap2;

                timer3.Enabled = true;
                pictureBox1.Location = new Point(10, 350);
                pictureBox1.Size = new Size(300, 200);
            }
            else
            {
                timer3.Enabled = false;

            }

        }

        int x_st4 = 0;
        int y_st4 = 200;

        private void timer4_Tick(object sender, EventArgs e)
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

            pictureBox2.Image = bitmap3;


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

        private void timer5_Tick(object sender, EventArgs e)
        {
            //bitmap1 = new Bitmap(filename);

            ww = bitmap3.Width;
            hh = bitmap3.Height;

            Graphics g = Graphics.FromImage(bitmap3);

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

            pictureBox2.Image = bitmap3;


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

        private void timer8_Tick(object sender, EventArgs e)
        {
            W = bitmap3.Width;
            H = bitmap3.Height;

            w = 25;
            h = 25;

            //richTextBox1.Text += "W = " + W.ToString() + " H = " + H.ToString() + " w = " + w.ToString() + " h = " + h.ToString() + "\n";
            
            Graphics g = Graphics.FromImage(bitmap3);

            g.FillRectangle(new SolidBrush(Color.Red), 0, 0, w, h);

            if (step8 == 1)
            {
                //if (x_st8 < (W - w * (round8 + 2)))
                if ((x_st8 + w) < (W -w * round8-w))
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
                if ((y_st8 + h) < (H - h * round8-h))
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
                if ((x_st8 - w)> (w* round8))
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
                richTextBox1.Text += "\nstep = " + step8.ToString() + "\t";

                richTextBox1.Text += "count = " + count.ToString() + " ";
                if (count > 1)
                {
                    if ((count - count_old) == 1)
                    {
                        timer8.Enabled = false;
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


            richTextBox1.Text += "(" + x_st8.ToString() + "," + y_st8.ToString() + ") ";

            pictureBox2.Image = bitmap3;

        }

        private void timer6_Tick(object sender, EventArgs e)
        {
            bitmap3 = new Bitmap(filename);
            Graphics g = Graphics.FromImage(bitmap3);
            pictureBox2.Image = bitmap3;

            /*
            xx += 2;
            yy += 2;
            //g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + search_size - 1, y_st + awb_block * i);

            //g.DrawEllipse(new Pen(Color.Red, 3), xx, yy, 20, 20);
            g.FillEllipse(new SolidBrush(Color.Red), new Rectangle(xx, yy, 20, 20));

            if (xx >= 300)
                yy -= 4;

            if (xx >= 600)
                timer1.Enabled = false;
            */

            tt++;
            xx2 = tt * 30;
            yy2 = (int)(gg * tt * tt / 2);
            //g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + search_size - 1, y_st + awb_block * i);

            //g.DrawEllipse(new Pen(Color.Red, 3), xx, yy, 20, 20);
            g.FillEllipse(new SolidBrush(Color.Red), new Rectangle(xx2, yy2, 20, 20));

            if (xx2 >= 200)
                yy2 -= 4;

            if (xx2 >= 800)
            {
                tt = 0;
                xx2 = 0;
                yy2 = 0;

            }

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
            pictureBox2.Image = bmp;


            //dispose
            p4.Dispose();
            g.Dispose();

            t += 3;
            if (t >= 720)
                timer1.Enabled = false;


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

        // Draw the text on the control.
        private void pictureBox_stretching_Paint(object sender, PaintEventArgs e)
        {
            // Use AntiAlias for the best result.
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAlias;
            e.Graphics.Clear(pictureBox_stretching.BackColor);

            SpaceTextToFit(e.Graphics, pictureBox_stretching.ClientRectangle,
                TextFont, Brushes.Red, LabelText);

        }

        // Draw text inserting space between characters
        // to make it fill the indicated width.
        private void SpaceTextToFit(Graphics gr, Rectangle rect, Font font, Brush brush, string text)
        {
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Near;
                string_format.LineAlignment = StringAlignment.Near;

                // Calculate the spacing.
                float space = (rect.Width - TotalCharacterWidth) / (text.Length - 1);

                // Draw the characters.
                PointF point = new PointF(rect.X, rect.Y);
                for (int i = 0; i < text.Length; i++)
                {
                    gr.DrawString(text[i].ToString(), font, brush, point);
                    point.X += CharacterWidths[i] + space;
                }
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
            Image img = Image.FromFile("c:\\______test_files\\_material\\cards1.png");
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
            Image img = Image.FromFile("c:\\______test_files\\_material\\cards2.png");
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

        private float GradientStart = 0;
        private float Delta = 5f;

        // Make the PictureBox redraw.
        private void timer_moving_Tick(object sender, EventArgs e)
        {
            pictureBox_gradient.Refresh();
            pictureBox_text.Refresh();
        }

        // Draw the background with text on top.
        private void pictureBox_gradient_Paint(object sender, PaintEventArgs e)
        {
            // Shade the background.
            int wid = pictureBox_gradient.ClientSize.Width;
            ShadeRect(e.Graphics, GradientStart, GradientStart + wid);

            // Increase the start position.
            GradientStart += Delta;
            if (GradientStart >= wid) GradientStart = 0;

            // Draw some text.
            using (Font font = new Font("Times New Roman", 18, FontStyle.Bold))
            {
                using (StringFormat string_format = new StringFormat())
                {
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    e.Graphics.DrawString("群曜醫電 Insight Medical Solutions Inc.",
                        font, Brushes.Black,
                        pictureBox_gradient.ClientSize.Width / 2,
                        pictureBox_gradient.ClientSize.Height / 2,
                        string_format);
                }
            }
        }

        // Fill the rectangle with a gradient that
        // shades from red to white to red.
        private void ShadeRect(Graphics gr, float xmin, float xmax)
        {
            using (LinearGradientBrush br = new LinearGradientBrush(
                new PointF(xmin, 0), new PointF(xmax, 0),
                Color.Red, Color.Red))
            {
                br.WrapMode = WrapMode.Tile;
                ColorBlend color_blend = new ColorBlend();
                color_blend.Colors = new Color[] { Color.Red, Color.White, Color.Red };
                color_blend.Positions = new float[] { 0, 0.5f, 1 };

                br.InterpolationColors = color_blend;
                gr.FillRectangle(br, pictureBox_gradient.ClientRectangle);
            }
        }

        // Draw the background with text on top.
        private void pictureBox_text_Paint(object sender, PaintEventArgs e)
        {
            // Clear the background.
            int wid = pictureBox_text.ClientSize.Width;
            e.Graphics.Clear(Color.White);

            // Make the gradient brush.
            using (LinearGradientBrush brush = new LinearGradientBrush(
                new PointF(GradientStart, 0),
                new PointF(GradientStart + wid, 0),
                Color.Red, Color.Red))
            {
                brush.WrapMode = WrapMode.Tile;
                ColorBlend color_blend = new ColorBlend();
                color_blend.Colors = new Color[]
                {
                    Color.Blue, Color.Blue,
                    Color.White, Color.Blue, Color.Blue
                };
                color_blend.Positions =
                    new float[] { 0, 0.4f, 0.5f, 0.6f, 1 };
                brush.InterpolationColors = color_blend;

                // Use the brush to draw some text.
                using (Font font = new Font("Times New Roman", 18, FontStyle.Bold))
                {
                    using (StringFormat string_format = new StringFormat())
                    {
                        string_format.Alignment = StringAlignment.Center;
                        string_format.LineAlignment = StringAlignment.Center;
                        e.Graphics.DrawString("群曜醫電 Insight Medical Solutions Inc.",
                            font, brush,
                            pictureBox_text.ClientSize.Width / 2,
                            pictureBox_text.ClientSize.Height / 2,
                            string_format);
                    }
                }
            }

            // Increase the start position.
            GradientStart += Delta;
            if (GradientStart >= wid) GradientStart = 0;


        }


    }
}
