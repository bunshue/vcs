using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Clock7_LED
{
    public partial class Form1 : Form
    {
        int flag_operation_mode = MODE_0;

        private const int MODE_0 = 0x00;   //時鐘模式
        private const int MODE_1 = 0x01;   //倒數模式
        private const int MODE_2 = 0x02;   //碼表模式
        private const int MODE_3 = 0x03;   //
        private const int MODE_4 = 0x04;   //

        //一段時間以後的寫法
        DateTime EventDate;// = DateTime.Now + new TimeSpan(0, 0, 0, 0);    //現在時間 + 1天13時42分59秒
        //richTextBox1.Text += "現在時間 + 1天13時42分59秒 = " + EventDate.ToString() + "\n";

        public Form1()
        {
            InitializeComponent();
            EventDate = DateTime.Now + new TimeSpan(0, 0, 10, 0);    //現在時間 + 1天13時42分59秒
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
//            TestLeds(e.Graphics);
//            TestColorful(e.Graphics);
//            TestSplat(e.Graphics);
            TestLetters(e.Graphics);
        }
        private void TestSplat(Graphics gr)
        {
            gr.Clear(Color.Black);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            const float margin = 10;
            const float cell_width = 200;
            const float cell_height = 320;
            const float led_thickness = 28;
            const float gap = 1.5f;

            LedText letter = new LedText(
                cell_width, cell_height, led_thickness, gap);

            Brush bg_brush = Brushes.Black;
            Brush used_brush = Brushes.Lime;
            Pen used_pen = Pens.Transparent;
            Brush unused_brush = new SolidBrush(Color.FromArgb(0, 40, 0));
            Pen unused_pen = Pens.Transparent;

            PointF position = new PointF(margin, margin);
            letter.DrawText(gr, bg_brush, used_brush, used_pen,
                    unused_brush, unused_pen, position,
                    1.2f, "!");
        }
        private void TestColorful(Graphics gr)
        {
            gr.Clear(Color.Black);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            const float margin = 10;
            const float cell_width = 200;
            const float cell_height = 320;
            const float led_thickness = 28;
            const float gap = 5f;

            LedText letter = new LedText(
                cell_width, cell_height, led_thickness, gap);

            Brush bg_brush1 = Brushes.Black;
            Brush used_brush1 = Brushes.Yellow;
            Pen used_pen1 = new Pen(Color.DarkRed, 3);
            Brush unused_brush1 = new SolidBrush(Color.FromArgb(0, 40, 0));
            Pen unused_pen1 = used_pen1;

            PointF position = new PointF(margin, margin);
            letter.DrawText(gr, bg_brush1, used_brush1, used_pen1,
                    unused_brush1, unused_pen1, position,
                    1.2f, "3");

            Brush bg_brush2 = Brushes.Black;
            Brush used_brush2 = new HatchBrush(
                HatchStyle.HorizontalBrick, Color.Lime, Color.Green);
            Pen used_pen2 = new Pen(Color.LightGreen, 3);
            Brush unused_brush2 = new SolidBrush(Color.FromArgb(0, 40, 0));
            Pen unused_pen2 = Pens.Transparent;

            position.X += letter.CellWidth * 1.2f;
            letter.DrawText(gr, bg_brush2, used_brush2, used_pen2,
                    unused_brush2, unused_pen2, position,
                    1.2f, "5");

            this.Size = new Size(505, 410);
        }

        private void TestLetters(Graphics gr)
        {
            gr.Clear(Color.Black);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            float margin = 10;
            float cell_width = 500 * 6 / 10;
            float cell_height = 800 * 6 / 10;
            float led_thickness = 70 * 6 / 10;
            float gap = 1.5f;

            if (flag_operation_mode == 0)
            {
                cell_width = cell_width * 6 / 10;
                cell_height = cell_height * 6 / 10;
                led_thickness = led_thickness * 6 / 10;
            }

            LedText letter = new LedText(
                cell_width, cell_height, led_thickness, gap);

            Brush bg_brush = Brushes.Black;
            Brush used_brush = Brushes.Lime;
            Pen used_pen = Pens.Transparent;
            Brush unused_brush = new SolidBrush(Color.FromArgb(0, 40, 0));
            Pen unused_pen = Pens.Transparent;

            PointF position = new PointF(margin, margin);


            if (flag_operation_mode == MODE_0)  //時鐘模式
            {
                cell_width = cell_width / 2;
                cell_height = cell_height / 2;
                led_thickness = led_thickness / 2;

                position.X = 100;
                position.Y = 350;

                DateTime dt = DateTime.Now;
                letter.DrawText(gr, bg_brush, used_brush, used_pen,
                        unused_brush, unused_pen, position,
                        1.2f, dt.Hour.ToString("D2") + " " + dt.Minute.ToString("D2") + " " + dt.Second.ToString("D2"));
            }
            else if (flag_operation_mode == MODE_1) //倒數模式
            {
                TimeSpan span;
                span = EventDate - DateTime.Now;

                position.X = 100;
                position.Y = 300;
                if (span.TotalSeconds > 0)
                {
                    letter.DrawText(gr, bg_brush, used_brush, used_pen,
                            unused_brush, unused_pen, position,
                            1.2f, span.Minutes.ToString("D2") + " " + span.Seconds.ToString("D2"));
                }
            }
            else if (flag_operation_mode == MODE_2) //碼表模式
            {

            }
            else
            {
                //其他模式
            }
        }

        private void TestLeds(Graphics gr)
        {
            gr.Clear(pictureBox1.BackColor);
            gr.SmoothingMode = SmoothingMode.AntiAlias;
            //gr.DrawRectangle(Pens.Green,
            //    margin, margin, cell_width, cell_height);

            const float margin = 10;
            const float cell_width = 100;
            const float cell_height = 160;
            const float led_thickness = 15;
            const float gap = 3;

            LedText letter = new LedText(
                cell_width, cell_height, led_thickness, gap);
            PointF position = new PointF(margin, margin);

            PointF[] top = letter.MakeLed0(position);
            gr.DrawPolygon(Pens.Red, top);

            PointF[] bottom = letter.MakeLed13(position);
            gr.DrawPolygon(Pens.Red, bottom);

            PointF[] uleft = letter.MakeLed1(position);
            gr.DrawPolygon(Pens.Red, uleft);

            PointF[] lleft = letter.MakeLed8(position);
            gr.DrawPolygon(Pens.Red, lleft);

            PointF[] uright = letter.MakeLed5(position);
            gr.DrawPolygon(Pens.Red, uright);

            PointF[] lright = letter.MakeLed12(position);
            gr.DrawPolygon(Pens.Red, lright);

            PointF[] cl = letter.MakeLed6(position);
            gr.DrawPolygon(Pens.Red, cl);

            PointF[] cr = letter.MakeLed7(position);
            gr.DrawPolygon(Pens.Red, cr);

            PointF[] ct = letter.MakeLed3(position);
            gr.DrawPolygon(Pens.Red, ct);

            PointF[] cb = letter.MakeLed10(position);
            gr.DrawPolygon(Pens.Red, cb);

            PointF[] ul_d = letter.MakeLed2(position);
            gr.DrawPolygon(Pens.Red, ul_d);

            PointF[] ur_d = letter.MakeLed4(position);
            gr.DrawPolygon(Pens.Red, ur_d);

            PointF[] ll_d = letter.MakeLed9(position);
            gr.DrawPolygon(Pens.Red, ll_d);

            PointF[] lr_d = letter.MakeLed11(position);
            gr.DrawPolygon(Pens.Red, lr_d);

            PointF[] pts = lr_d;
            //gr.DrawEllipse(Pens.Red, pts[0].X - 2, pts[0].Y - 2, 4, 4);
            //gr.DrawEllipse(Pens.Green, pts[1].X - 2, pts[1].Y - 2, 4, 4);
            //gr.DrawEllipse(Pens.Blue, pts[2].X - 2, pts[2].Y - 2, 4, 4);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            pictureBox1.Refresh();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(50, 100);
            
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            //this.Size = new Size(1570, 520);
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.Size = new Size(1920, 1080);

        }
    }
}
