using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_LED_Text
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //左上
            pictureBox0.Invalidate();

            //右
            pictureBox1.Invalidate();

            //左下
            pictureBox2.Invalidate();
        }

        void show_item_location()
        {
            int W = 240;
            int H = 440;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W * 3 + 50, H * 2 + 10);
            pictureBox2.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox0.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.BackColor = Color.Pink;
            this.Size = new Size(1700, 950);
            this.Text = "vcs_LED_Text";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            //左上
            TestLeds(e.Graphics);
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            //右
            TestColorful(e.Graphics);
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            //左下
            TestSplat(e.Graphics);
        }

        //------------------------------------------------------------  # 60個

        private void TestSplat(Graphics gr)
        {
            gr.Clear(Color.Black);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            const float W = 200;
            const float H = 320;
            const float led_thickness = 28;
            const float gap = 1.5f;
            int dx = (int)W + 5;
            int dy = (int)H + 5;
            int x_st = 10;
            int y_st = 10;
            PointF position = new PointF(x_st + dx * 0, y_st + dy * 0);

            LedText letter = new LedText(W, H, led_thickness, gap);

            Brush bg_brush = Brushes.Black;
            Brush used_brush = Brushes.Lime;
            Pen used_pen = Pens.Transparent;
            Brush unused_brush = new SolidBrush(Color.FromArgb(0, 40, 0));
            Pen unused_pen = Pens.Transparent;

            position = new PointF(x_st + dx * 0, y_st + dy * 0);
            letter.DrawText(gr, bg_brush, used_brush, used_pen, unused_brush, unused_pen, position, 1.2f, "!");
        }

        //------------------------------------------------------------  # 60個

        //0123456789ABCDEFGH
        //IJKLMNOPQRSTUVWXYZ

        int index = 0;
        string text = "0";
        private void TestColorful(Graphics gr)
        {
            const float ratio = 1.3f;

            gr.Clear(Color.Black);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            const float W = 200 / ratio;
            const float H = 320 / ratio;
            const float led_thickness = 28 / ratio;
            const float gap = 5f / ratio;
            int dx = (int)W + 5;
            int dy = (int)H + 5 + 50;
            int x_st = 10;
            int y_st = 10;
            PointF position = new PointF(x_st + dx * 0, y_st + dy * 0);

            LedText letter = new LedText(W, H, led_thickness, gap);

            Brush bg_brush1 = Brushes.Black;
            Brush used_brush1 = Brushes.Yellow;
            Pen used_pen1 = new Pen(Color.DarkRed, 3);
            Brush unused_brush1 = new SolidBrush(Color.FromArgb(0, 40, 0));
            Pen unused_pen1 = used_pen1;

            position = new PointF(x_st + dx * 0, y_st + dy * 0);
            letter.DrawText(gr, bg_brush1, used_brush1, used_pen1, unused_brush1, unused_pen1, position, 1.2f, text + text + text + text);

            //------------------------------  # 30個

            Brush bg_brush2 = Brushes.Black;
            Brush used_brush2 = new HatchBrush(HatchStyle.HorizontalBrick, Color.Lime, Color.Green);
            Pen used_pen2 = new Pen(Color.LightGreen, 3);
            Brush unused_brush2 = new SolidBrush(Color.FromArgb(0, 40, 0));
            Pen unused_pen2 = Pens.Transparent;

            position = new PointF(x_st + dx * 0, y_st + dy * 1);
            letter.DrawText(gr, bg_brush2, used_brush2, used_pen2, unused_brush2, unused_pen2, position, 1.2f, text + text + text + text);

            //------------------------------  # 30個

            Brush bg_brush = Brushes.Black;
            Brush used_brush = Brushes.Lime;
            Pen used_pen = Pens.Transparent;
            Brush unused_brush = new SolidBrush(Color.FromArgb(0, 40, 0));
            Pen unused_pen = Pens.Transparent;

            position = new PointF(x_st + dx * 0, y_st + dy * 2);
            letter.DrawText(gr, bg_brush, used_brush, used_pen, unused_brush, unused_pen, position, 1.2f, text + text + text + text);


            index++;
            if (index < 10)
            {
                text = index.ToString();
            }
            else
            {
                text = ((char)(0x40 + (index - 9))).ToString();
                //richTextBox1.Text += index.ToString() + "\n";
                //richTextBox1.Text += text + " ";
                Application.DoEvents();
            }

            richTextBox1.Text += index.ToString() + "\t" + text + "\n";

            if (index >= 36)
            {
                index = 0;
                text = "0";
            }


        }

        //------------------------------------------------------------  # 60個

        private void TestLeds(Graphics g)
        {
            g.Clear(pictureBox1.BackColor);
            g.SmoothingMode = SmoothingMode.AntiAlias;

            const float W = 100;
            const float H = 160;
            const float led_thickness = 15;
            const float gap = 3;
            int dx = (int)W + 5;
            int dy = (int)H + 5;
            int x_st = 10;
            int y_st = 10;
            PointF position = new PointF(x_st + dx * 0, y_st + dy * 0);

            LedText letter = new LedText(W, H, led_thickness, gap);
            position = new PointF(x_st + dx * 0, y_st + dy * 0);

            PointF[] top = letter.MakeLed0(position);
            g.DrawPolygon(Pens.Red, top);

            PointF[] bottom = letter.MakeLed13(position);
            g.DrawPolygon(Pens.Red, bottom);

            PointF[] uleft = letter.MakeLed1(position);
            g.DrawPolygon(Pens.Red, uleft);

            PointF[] lleft = letter.MakeLed8(position);
            g.DrawPolygon(Pens.Red, lleft);

            PointF[] uright = letter.MakeLed5(position);
            g.DrawPolygon(Pens.Red, uright);

            PointF[] lright = letter.MakeLed12(position);
            g.DrawPolygon(Pens.Red, lright);

            PointF[] cl = letter.MakeLed6(position);
            g.DrawPolygon(Pens.Red, cl);

            PointF[] cr = letter.MakeLed7(position);
            g.DrawPolygon(Pens.Red, cr);

            PointF[] ct = letter.MakeLed3(position);
            g.DrawPolygon(Pens.Red, ct);

            PointF[] cb = letter.MakeLed10(position);
            g.DrawPolygon(Pens.Red, cb);

            PointF[] ul_d = letter.MakeLed2(position);
            g.DrawPolygon(Pens.Red, ul_d);

            PointF[] ur_d = letter.MakeLed4(position);
            g.DrawPolygon(Pens.Red, ur_d);

            PointF[] ll_d = letter.MakeLed9(position);
            g.DrawPolygon(Pens.Red, ll_d);

            PointF[] lr_d = letter.MakeLed11(position);
            g.DrawPolygon(Pens.Red, lr_d);

            PointF[] pts = lr_d;
            //g.DrawEllipse(Pens.Red, pts[0].X - 2, pts[0].Y - 2, 4, 4);
            //g.DrawEllipse(Pens.Green, pts[1].X - 2, pts[1].Y - 2, 4, 4);
            //g.DrawEllipse(Pens.Blue, pts[2].X - 2, pts[2].Y - 2, 4, 4);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            pictureBox1.Invalidate();
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個
