using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Clock1
{
    public partial class Form_CountDown : Form
    {
        bool flag_countdown_start = false;

        int flag_operation_mode = MODE_2;

        private const int MODE_0 = 0x00;   //測試模式
        private const int MODE_1 = 0x01;   //時鐘模式
        private const int MODE_2 = 0x02;   //倒數模式
        private const int MODE_3 = 0x03;   //馬表模式
        private const int MODE_4 = 0x04;   //

        DateTime EventDate;
        Button btn1;
        Button btn2;
        Button btn3;
        NumericUpDown nud1;
        NumericUpDown nud2;
        NumericUpDown nud3;
        Label lb_time;
        Label lb1;
        Label lb2;
        Label lb3;

        Brush bg_brush = Brushes.Black;
        Brush used_brush = Brushes.Lime;

        public Form_CountDown()
        {
            InitializeComponent();

            if (flag_operation_mode == MODE_2) //倒數模式
            {
                //一段時間以後的寫法
                EventDate = DateTime.Now + new TimeSpan(0, 0, 10, 0);    //現在時間 + 1天13時42分59秒
            }

        }

        private void Form_CountDown_Load(object sender, EventArgs e)
        {
            if (flag_operation_mode == MODE_0)  //測試模式
            {
                //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示
                //this.StartPosition = FormStartPosition.Manual;
                //this.Location = new Point(50, 100);
            }
            else if (flag_operation_mode == MODE_2)  //倒數模式
            {
                timer1.Enabled = false;
                int x_st = 0;
                int y_st = 0;
                int dx = 0;
                int W = 100;
                int H = 40;

                x_st = 120;
                y_st = 100;

                // 實例化按鈕
                lb_time = new Label();
                lb_time.AutoSize = true;
                lb_time.Font = new Font("Courier New", 20);
                lb_time.Text = "設定時間";
                lb_time.Location = new Point(x_st + dx * 0, y_st);
                this.pictureBox1.Controls.Add(lb_time); // 將此控件加入pictureBox中

                x_st = 205;
                y_st = 210;
                dx = 150;

                // 實例化按鈕
                lb1 = new Label();
                lb1.AutoSize = true;
                lb1.Font = new Font("Courier New", 18);
                lb1.Text = "時";
                lb1.Location = new Point(x_st + dx * 0, y_st);
                this.pictureBox1.Controls.Add(lb1); // 將此控件加入pictureBox中

                // 實例化按鈕
                lb2 = new Label();
                lb2.AutoSize = true;
                lb2.Font = new Font("Courier New", 18);
                lb2.Text = "分";
                lb2.Location = new Point(x_st + dx * 1, y_st);
                this.pictureBox1.Controls.Add(lb2); // 將此控件加入pictureBox中

                // 實例化按鈕
                lb3 = new Label();
                lb3.AutoSize = true;
                lb3.Font = new Font("Courier New", 18);
                lb3.Text = "秒";
                lb3.Location = new Point(x_st + dx * 2, y_st);
                this.pictureBox1.Controls.Add(lb3); // 將此控件加入pictureBox中

                x_st = 100;
                y_st = 200;
                dx = 150;
                W = 100;
                H = 40;

                // 實例化按鈕
                nud1 = new NumericUpDown();
                nud1.Name = "nud1";
                nud1.Width = W;
                nud1.Height = H;
                nud1.Font = new Font("Courier New", 30);
                nud1.TextAlign = HorizontalAlignment.Center;
                nud1.Maximum = 23;
                nud1.Minimum = 0;
                nud1.Value = 0;
                nud1.Location = new Point(x_st + dx * 0, y_st);
                // 加入按鈕事件
                //nud1.ValueChanged += new EventHandler(nud_ValueChanged);   //same
                nud1.ValueChanged += nud_ValueChanged;
                this.pictureBox1.Controls.Add(nud1);    // 將此控件加入pictureBox中

                nud2 = new NumericUpDown();
                nud2.Name = "nud2";
                nud2.Width = W;
                nud2.Height = H;
                nud2.Font = new Font("Courier New", 30);
                nud2.TextAlign = HorizontalAlignment.Center;
                nud2.Maximum = 59;
                nud2.Minimum = 0;
                nud2.Value = 10;
                nud2.Location = new Point(x_st + dx * 1, y_st);
                // 加入按鈕事件
                //nud2.ValueChanged += new EventHandler(nud_ValueChanged);   //same
                nud2.ValueChanged += nud_ValueChanged;
                this.pictureBox1.Controls.Add(nud2);    // 將此控件加入pictureBox中

                nud3 = new NumericUpDown();
                nud3.Name = "nud3";
                nud3.Width = W;
                nud3.Height = H;
                nud3.Font = new Font("Courier New", 30);
                nud3.TextAlign = HorizontalAlignment.Center;
                nud3.Maximum = 59;
                nud3.Minimum = 0;
                nud3.Value = 0;
                nud3.Location = new Point(x_st + dx * 2, y_st);
                // 加入按鈕事件
                //nud3.ValueChanged += new EventHandler(nud_ValueChanged);   //same
                nud3.ValueChanged += nud_ValueChanged;
                this.pictureBox1.Controls.Add(nud3);    // 將此控件加入pictureBox中

                x_st = 100;
                y_st = 300;
                dx = 150;
                W = 100;
                H = 60;

                // 實例化按鈕
                btn1 = new Button();
                btn1.Width = W;
                btn1.Height = H;
                btn1.Font = new Font("Courier New", 16);
                btn1.Text = "Start";
                btn1.Name = "bt_start";
                btn1.Location = new Point(x_st + dx * 0, y_st);
                // 加入按鈕事件
                //btn1.Click += new EventHandler(myClick);   //same
                btn1.Click += button_Click;
                this.pictureBox1.Controls.Add(btn1);    // 將此控件加入pictureBox中

                // 實例化按鈕
                btn2 = new Button();
                btn2.Width = W;
                btn2.Height = H;
                btn2.Font = new Font("Courier New", 16);
                btn2.Text = "Reset";
                btn2.Name = "bt_reset";
                btn2.Location = new Point(x_st + dx * 1, y_st);
                // 加入按鈕事件
                //btn2.Click += new EventHandler(button_Click);   //same
                btn2.Click += button_Click;
                this.pictureBox1.Controls.Add(btn2);    // 將此控件加入pictureBox中

                // 實例化按鈕
                btn3 = new Button();
                btn3.Width = W;
                btn3.Height = H;
                btn3.Font = new Font("Courier New", 16);
                btn3.Text = "Exit";
                btn3.Name = "bt_exit";
                btn3.Location = new Point(x_st + dx * 2, y_st);
                // 加入按鈕事件
                //btn3.Click += new EventHandler(button_Click);   //same
                btn3.Click += button_Click;
                this.pictureBox1.Controls.Add(btn3);    // 將此控件加入pictureBox中

                lb_time.Text = "設定時間 : " + nud1.Value.ToString() + "時 " + nud3.Value.ToString() + "分 " + nud3.Value.ToString() + "秒" + "\n";
            }
            else
            {
                //最大化螢幕
                this.FormBorderStyle = FormBorderStyle.None;
                this.WindowState = FormWindowState.Maximized;
                pictureBox1.Location = new Point(0, 0);
                pictureBox1.Size = new Size(1920, 1080);
            }

            if (flag_operation_mode == MODE_0)
            {
                this.Text = "測試模式";
            }
            else if (flag_operation_mode == MODE_1)
            {
                this.Text = "時鐘模式";
            }
            else if (flag_operation_mode == MODE_2)
            {
                this.Text = "倒數模式";
            }
            else if (flag_operation_mode == MODE_3)
            {
                this.Text = "馬表模式";
            }
            else
            {
                this.Text = "其他模式";
            }
        }

        private void nud_ValueChanged(object sender, EventArgs e)
        {
            if (((NumericUpDown)sender).Name == "nud1")
            {
                //richTextBox1.Text += "你按了nud1 value = " + ((NumericUpDown)sender).Value.ToString() + "\n";
            }
            else if (((NumericUpDown)sender).Name == "nud2")
            {
                //richTextBox1.Text += "你按了nud2 value = " + ((NumericUpDown)sender).Value.ToString() + "\n";
            }
            else if (((NumericUpDown)sender).Name == "nud3")
            {
                //richTextBox1.Text += "你按了nud3 value = " + ((NumericUpDown)sender).Value.ToString() + "\n";
            }

            int hh = (int)nud1.Value;
            int mm = (int)nud2.Value;
            int ss = (int)nud3.Value;

            lb_time.Text = "設定時間 : " + hh.ToString() + "時 " + mm.ToString() + "分 " + ss.ToString() + "秒" + "\n";
        }

        private void button_Click(object sender, EventArgs e)
        {
            if (((Button)sender).Name == "bt_start")
            {
                this.pictureBox1.Controls.Remove(btn1);
                this.pictureBox1.Controls.Remove(btn2);
                this.pictureBox1.Controls.Remove(btn3);
                this.pictureBox1.Controls.Remove(nud1);
                this.pictureBox1.Controls.Remove(nud2);
                this.pictureBox1.Controls.Remove(nud3);
                this.pictureBox1.Controls.Remove(lb_time);
                this.pictureBox1.Controls.Remove(lb1);
                this.pictureBox1.Controls.Remove(lb2);
                this.pictureBox1.Controls.Remove(lb3);


                int hh = (int)nud1.Value;
                int mm = (int)nud2.Value;
                int ss = (int)nud3.Value;

                richTextBox1.Text += "設定時間 : " + hh.ToString() + "時 " + mm.ToString() + "分 " + ss.ToString() + "秒" + "\n";

                //一段時間以後的寫法
                EventDate = DateTime.Now + new TimeSpan(0, hh, mm, ss);    //現在時間 + 0天hh時mm分ss秒

                //最大化螢幕
                this.FormBorderStyle = FormBorderStyle.None;
                this.WindowState = FormWindowState.Maximized;
                pictureBox1.Location = new Point(0, 0);
                pictureBox1.Size = new Size(1920, 1080);
                flag_countdown_start = true;
                richTextBox1.Visible = false;
                timer1.Enabled = true;
            }
            else if (((Button)sender).Name == "bt_reset")
            {
                nud1.Value = 0;
                nud2.Value = 10;
                nud3.Value = 0;
            }
            else if (((Button)sender).Name == "bt_exit")
            {
                Application.Exit();
            }
            else
            {
                richTextBox1.Text += "你按了按鈕 Name : " + ((Button)sender).Name + "\n";
            }
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            //TestLeds(e.Graphics);
            //TestColorful(e.Graphics);
            //TestSplat(e.Graphics);
            if (flag_countdown_start == true)
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

            Pen used_pen = Pens.Transparent;
            Brush unused_brush = new SolidBrush(Color.FromArgb(0, 40, 0));
            Pen unused_pen = Pens.Transparent;

            PointF position = new PointF(margin, margin);
            letter.DrawText(gr, bg_brush, used_brush, used_pen,
                    unused_brush, unused_pen, position,
                    1.2f, "Z");
        }

        int num = 0;
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
                    1.2f, num.ToString());

            Brush bg_brush2 = Brushes.Black;
            Brush used_brush2 = new HatchBrush(
                HatchStyle.HorizontalBrick, Color.Lime, Color.Green);
            Pen used_pen2 = new Pen(Color.LightGreen, 3);
            Brush unused_brush2 = new SolidBrush(Color.FromArgb(0, 40, 0));
            Pen unused_pen2 = Pens.Transparent;

            position.X += letter.CellWidth * 1.2f;
            letter.DrawText(gr, bg_brush2, used_brush2, used_pen2,
                    unused_brush2, unused_pen2, position,
                    1.2f, num.ToString());

            this.Size = new Size(505 + 50, 410 + 50);
            num++;
            if (num > 9)
                num = 0;
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

            if (flag_operation_mode == MODE_0)
            {
                cell_width = cell_width * 1 / 7;
                cell_height = cell_height * 1 / 7;
                led_thickness = led_thickness * 1 / 7;
            }
            else if (flag_operation_mode == MODE_1)
            {
                cell_width = cell_width * 6 / 10;
                cell_height = cell_height * 6 / 10;
                led_thickness = led_thickness * 6 / 10;
            }

            LedText letter = new LedText(
                cell_width, cell_height, led_thickness, gap);

            Pen used_pen = Pens.Transparent;
            Brush unused_brush = new SolidBrush(Color.FromArgb(0, 40, 0));
            Pen unused_pen = Pens.Transparent;

            PointF position = new PointF(margin, margin);

            if (flag_operation_mode == MODE_0)  //測試模式
            {
                cell_width = cell_width / 2;
                cell_height = cell_height / 2;
                led_thickness = led_thickness / 2;

                position.X = 50;
                position.Y = 50;

                DateTime dt = DateTime.Now;
                letter.DrawText(gr, bg_brush, used_brush, used_pen,
                        unused_brush, unused_pen, position,
                        1.2f, dt.Hour.ToString("D2") + " " + dt.Minute.ToString("D2") + " " + dt.Second.ToString("D2"));
            }
            else if (flag_operation_mode == MODE_1)  //時鐘模式
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
            else if (flag_operation_mode == MODE_2) //倒數模式
            {
                TimeSpan span;
                span = EventDate - DateTime.Now;

                position.X = 100;
                position.Y = 300;
                if (span.TotalSeconds > 0)
                {
                    if (span.TotalSeconds < 60)
                    {
                        used_brush = Brushes.Red;
                    }
                    letter.DrawText(gr, bg_brush, used_brush, used_pen,
                            unused_brush, unused_pen, position,
                            1.2f, span.Minutes.ToString("D2") + " " + span.Seconds.ToString("D2"));
                }
                else
                {
                    richTextBox1.Text += "時間到\n";

                    Bitmap bitmap1 = new Bitmap(@"C:\_git\vcs\_1.data\______test_files1\picture1.jpg");

                    int W = this.Size.Width;
                    int H = this.Size.Height;
                    int w = bitmap1.Width;
                    int h = bitmap1.Height;

                    int ww = w * 2;
                    int hh = h * 2;

                    gr.DrawImage(bitmap1, (W - ww) / 2, (H - hh) / 2, ww, hh);

                    //richTextBox1.Text += "W = " + W.ToString() + " H = " + H.ToString() + "\n";
                    //richTextBox1.Text += "w = " + w.ToString() + " h = " + h.ToString() + "\n";

                    pictureBox1.DoubleClick += pictureBox1_DoubleClick;
                    timer1.Enabled = false;
                }
            }
            else if (flag_operation_mode == MODE_3) //馬表模式
            {

            }
            else
            {
                //其他模式
            }
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
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
            richTextBox1.Text += "A";
            pictureBox1.Refresh();

        }

    }
}
