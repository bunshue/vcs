using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for DashStyle

namespace vcs_Draw_Dynamics
{
    public partial class Form1 : Form
    {
        int W = 0;
        int H = 0;

        int x_st = 0;
        int y_st = 0;

        int t = 0;
        int vx = 10;
        int vy = 0;

        int index = -1;
        List<int[]> pts = new List<int[]>();    //二維List for int

        //List<PointF[]> pts = new List<PointF[]>();

        int mass = 1;

        public Form1()
        {
            InitializeComponent();

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            W = pictureBox1.Width;
            H = pictureBox1.Height;
            x_st = 0;
            y_st = 500;
            lb_mesg.Text = "";
            trackBar1_Scroll(sender, e);
        }

        void show_item_location()
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1500;
            y_st = 10;
            dx = 110;
            dy = 45;

            button1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            lb_mesg.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            trackBar1.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            richTextBox1.Size = new Size(400,800);

            //pictureBox1.Location = new Point(10, 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

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

        private void DrawCircle(PaintEventArgs e, int center_x, int center_y, int radius, int linewidth, Color c)
        {
            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c, linewidth);

            // Draw the circle
            e.Graphics.DrawEllipse(p, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            p.Dispose();
        }

        private void DrawFillCircle(PaintEventArgs e, int center_x, int center_y, int radius, Color c)
        {
            SolidBrush newBrush = new SolidBrush(c);

            // Fill the circle
            e.Graphics.FillEllipse(newBrush, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            newBrush.Dispose();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int ww = 20;
            int hh = 20;

            List<PointF> Points = new List<PointF>();
            int g = 10;
            /*
            SolidBrush redBrush = new SolidBrush(Color.Red);
            //e.Graphics.DrawRectangle(new Pen(Color.Red, 1), x_st - sw / 2, y_st - sh / 2, sw, sh);

            x_st = 100;
            y_st = 100;

            DrawCircle(e, x_st, H - y_st, 15, 2, Color.Red);

            x_st = 200;
            y_st = 200;

            DrawFillCircle(e, x_st, H - y_st, 15, Color.Red);
            */



            Point[] curvePoints = new Point[3];    //一維陣列內有 3 個Point

            Pen p = new Pen(Color.Red, 2);
            //p.DashStyle = DashStyle.Dot;

            curvePoints[0].X = 0;
            curvePoints[0].Y = H - 500;
            curvePoints[1].X = 200;
            curvePoints[1].Y = H - 500;
            curvePoints[2].X = 200;
            curvePoints[2].Y = H;
            e.Graphics.DrawLines(p, curvePoints);   //畫直線
			

            DrawFillCircle(e, x_st, H - y_st, 15, Color.Blue);

            e.Graphics.FillRectangle(new SolidBrush(Color.Red), x_st - ww / 2, H - y_st - hh / 2, ww, hh);


            pts.Add(new int[] { index, x_st, H - y_st });

            using (Pen thick_pen = new Pen(Color.Gray, 2))
            {
                int len = pts.Count;
                int ii = -1;
                int ii_old = 0;

                if (len > 0)
                {
                    Points.Clear();

                    int i;
                    //richTextBox1.Text += "共有 " + len.ToString() + " 個項目, 分別是:\n";
                    for (i = 0; i < len; i++)
                    {
                        ii = pts[i][0];
                        if (ii < 0)
                            continue;
                        if (ii != ii_old)
                        {
                            if (Points.Count > 1)
                                e.Graphics.DrawLines(thick_pen, Points.ToArray());
                            Points.Clear();
                            ii_old = ii;
                        }

                        Points.Add(new PointF(pts[i][1], pts[i][2]));
                        DrawFillCircle(e, pts[i][1], pts[i][2], 4, Color.Red);

                        //richTextBox1.Text += pts[i][0].ToString() + "\t" + pts[i][1].ToString() + "\t" + pts[i][2].ToString() + "\n";
                    }
                    if (Points.Count > 1)
                        e.Graphics.DrawLines(thick_pen, Points.ToArray());
                }
            }

            richTextBox1.Text += "t = " + t.ToString() + "\tx = " + x_st.ToString() + "\ty = " + y_st.ToString() + "\t";
            richTextBox1.Text += "vx = " + vx.ToString() + "\tvy = " + vy.ToString() + "\n";

            x_st += vx * 1;

            if (x_st > 1000)
            {
                timer1.Enabled = false;
            }

            if (x_st > 200)
            {
                vy += g * 1;
                y_st -= vy * 1;

            }
            if (y_st <= 0)
            {
                timer1.Enabled = false;
            }
            t++;

            ww = 100;
            hh = 100;
            e.Graphics.FillRectangle(new SolidBrush(Color.Red), W - 100 - ww / 2, 200 - hh / 2, ww, hh);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            index++;
            t = 0;
            x_st = 0;
            y_st = 500;
            vx = 10;
            vy = 0;
            timer1.Enabled = true;

            vx = 10 * (int)trackBar1.Value;
            richTextBox1.Text += "初速度 : " + vx.ToString() + " m/s\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            vx = 10 * (int)trackBar1.Value;
            richTextBox1.Text += "初速度 : " + vx.ToString() + " m/s\n";

            lb_mesg.Text = "初速度 : " + vx.ToString() + " m/s       能量 : " + (mass * vx * vx / 2).ToString() + " 焦耳";
        }

        private const int COLUMNS = 10;
        private const int ROWS = 8;

        int[,] gray = new int[COLUMNS, ROWS];

        private void button3_Click(object sender, EventArgs e)
        {
            int i;
            int j;

            int len = pts.Count;
            richTextBox1.Text += "共有 " + len.ToString() + " 個項目, 分別是:\n";

            for (i = 0; i < pts.Count; i++)
            {
                richTextBox1.Text += pts[i][0].ToString() + "\t" + pts[i][1].ToString() + "\t" + pts[i][2].ToString() + "\n";
                //richTextBox1.Text += i.ToString() + pts[i]
                //int tt = int.Parse(pts[i][1]);
                //richTextBox1.Text += "pts[" + i.ToString() + "][0] = " + pts[i][0].ToString() + "\tpts[" + i.ToString() + "][1] = " + pts[i][1].ToString() + "\n";
            }

            //richTextBox1.Text += pts[0][0].ToString();
            //richTextBox1.Text += pts[1][1].ToString();
            //richTextBox1.Text += pts[3][3].ToString();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            x_st = 0;
            y_st = 500;
            pts.Clear();
            this.pictureBox1.Invalidate();
        }
    }
}
