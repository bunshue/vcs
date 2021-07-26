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
        private const int INITIAL_HEIGHT = 500;     //初高度
        private const int INITIAL_ENERGY = 5000;     //初能量

        int W = 0;
        int H = 0;

        int x_st = 0;
        int y_st = 0;

        int t = 0;
        int vx = 10;
        int vy = 0;

        int index = -1;
        List<int[]> pts = new List<int[]>();    //二維List for int

        float mass = 1;
        int total_energy = INITIAL_ENERGY;
        int this_energy = 0;
        int use_bird_kind = 0;
        int use_pig_kind = 0;

        bool angry_bird_move_status = false;

        int try_count = 0;

        int drop_down_time = 0;

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

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
            y_st = INITIAL_HEIGHT;
            //lb_main_mesg.Text = "";
            lb_shoot_count.Text = "發射次數 : " + try_count.ToString();
            //lb_energy_ek.Text = "";
            //lb_energy_ep.Text = "";
            //lb_energy_es.Text = "";
            //lb_energy_et.Text = "";
             
            //lb_initial_speed.Text = "";
            trackBar1_Scroll(sender, e);
            rb_bird_CheckedChanged(sender, e);

            //button2.Visible = false;
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
            x_st = 1300;
            y_st = 50;
            dx = 110;
            dy = 45;

            button1.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 30);
            button2.Location = new Point(x_st + dx * 1, y_st + dy * 0 - 30);
            button3.Location = new Point(x_st + dx * 2, y_st + dy * 0 - 30);
            button4.Location = new Point(x_st + dx * 3, y_st + dy * 0 - 30);

            groupBox_bird.Size = new Size(400, 60);
            groupBox_bird.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            pictureBox_bird.Size = new Size(200, 200);
            pictureBox_bird.Location = new Point(60, 60);

            lb_energy_ep.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_energy_ek.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            lb_velocity.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            lb_energy_es.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            lb_energy_et.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            lb_total_energy.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            lb_this_energy.Location = new Point(x_st + dx * 4, y_st + dy * 7);
            lb_initial_speed.Location = new Point(x_st + dx * 4, y_st + dy * 8 + 20);

            progressBar_total_energy.Maximum = total_energy;
            progressBar_total_energy.Minimum = 0;
            progressBar_total_energy.Value = total_energy;
            progressBar_total_energy.Size = new Size(400, 30);
            progressBar_total_energy.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            progressBar_this_energy.Maximum = 5000;
            progressBar_this_energy.Minimum = 0;
            progressBar_this_energy.Value = 0;
            progressBar_this_energy.Size = new Size(400, 30);
            progressBar_this_energy.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            trackBar1.Size = new Size(400, 30);
            trackBar1.Location = new Point(x_st + dx * 0, y_st + dy * 8 + 20);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(400, 500);

            pictureBox1.Location = new Point(50, 50);
            pictureBox1.Size = new Size(1200, 900);
            pictureBox1.BackColor = Color.FromArgb(244, 252, 254);
            pictureBox_bird.BackColor = Color.FromArgb(244, 252, 254);

            lb_shoot_count.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - 300, pictureBox1.Location.Y + 20);
            lb_main_mesg.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - 300, pictureBox1.Location.Y + 20 + 40);

            x_st = 25;
            y_st = 25;
            dx = 90;
            dy = 30;
            rb1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            rb2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            rb3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            rb4.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            rb1.Text = "紅鳥 1 Kg";
            rb2.Text = "黃鳥 0.6 Kg";
            rb3.Text = "藍鳥 0.3 Kg";
            rb4.Text = "炸彈鳥 2 Kg";

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
            int ww = 40;
            int hh = 40;

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


            /*
            Point[] curvePoints = new Point[3];    //一維陣列內有 3 個Point

            Pen p = new Pen(Color.Red, 2);
            //p.DashStyle = DashStyle.Dot;

            curvePoints[0].X = 0;
            curvePoints[0].Y = H - INITIAL_HEIGHT;
            curvePoints[1].X = 200;
            curvePoints[1].Y = H - INITIAL_HEIGHT;
            curvePoints[2].X = 200;
            curvePoints[2].Y = H;
            e.Graphics.DrawLines(p, curvePoints);   //畫直線
            */
            Rectangle destRect0 = new Rectangle(0, H - INITIAL_HEIGHT, 200, INITIAL_HEIGHT);
            e.Graphics.FillRectangle(new SolidBrush(Color.Gold), destRect0);

            e.Graphics.DrawString("高 " + INITIAL_HEIGHT.ToString() + " 公尺", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(10, H - INITIAL_HEIGHT + 10));


            GraphicsUnit units = GraphicsUnit.Pixel;

            Bitmap bmp;

            if (rb1.Checked == true)
                bmp = new Bitmap("..//..//img//AB_red.jpg");
            else if (rb2.Checked == true)
                bmp = new Bitmap("..//..//img//AB_yellow.jpg");
            else if (rb3.Checked == true)
                bmp = new Bitmap("..//..//img//AB_blue.jpg");
            else if (rb4.Checked == true)
                bmp = new Bitmap("..//..//img//AB_black.jpg");
            else
                bmp = new Bitmap("..//..//img//AB_red.jpg");

            //DrawFillCircle(e, x_st + ww / 2, H - y_st - hh / 2, 15, Color.Blue);

            //Rectangle destRect1 = new Rectangle(x_st - ww / 2, H - y_st - hh / 2, ww, hh);

            ww = hh * bmp.Width / bmp.Height;   //符合比例
            Rectangle destRect1 = new Rectangle(x_st, H - y_st - hh - 3, ww, hh);
            //e.Graphics.DrawImage(bmp, destRect1, 0, 0, bmp.Width, bmp.Height, units);

            //e.Graphics.FillRectangle(new SolidBrush(Color.Red), x_st - ww / 2, H - y_st - hh / 2, ww, hh);


            pts.Add(new int[] { index, use_bird_kind, x_st, H - y_st });

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

                        Points.Add(new PointF(pts[i][2] + ww / 2, pts[i][3] - hh / 2));


                        Color color_trajectory;

                        if (pts[i][1] == 0)
                            color_trajectory = Color.Red;
                        else if (pts[i][1] == 1)
                            color_trajectory = Color.Yellow;
                        else if (pts[i][1] == 2)
                            color_trajectory = Color.Blue;
                        else if (pts[i][1] == 3)
                            color_trajectory = Color.Black;
                        else
                            color_trajectory = Color.Red;

                        DrawFillCircle(e, pts[i][2] + ww / 2, pts[i][3] - hh / 2, 4, color_trajectory);
                        //richTextBox1.Text += pts[i][0].ToString() + "\t" + pts[i][1].ToString() + "\t" + pts[i][2].ToString() + "\n";
                    }
                    if (Points.Count > 1)
                        e.Graphics.DrawLines(thick_pen, Points.ToArray());
                }
            }

            e.Graphics.DrawImage(bmp, destRect1, 0, 0, bmp.Width, bmp.Height, units);


            if (angry_bird_move_status == true)
            {
                richTextBox1.Text += "t = " + t.ToString() + "\tx = " + x_st.ToString() + "\ty = " + y_st.ToString() + "\t";
                richTextBox1.Text += "vx = " + vx.ToString() + "\tvy = " + vy.ToString() + "\n";
                int EP = (int)(mass * g * y_st);

                //richTextBox1.Text += "height : " + y_st.ToString() + "\n";

                double v = Math.Sqrt(vx * vx + vy * vy);
                int EK = (int)(mass * (vx * vx + vy * vy) / 2);

                richTextBox1.Text += "EK = " + EK.ToString() + "\tEP = " + EP.ToString() + "\tE = " + (EK + EP).ToString() + "\n";

                if ((x_st < 1000) && (y_st >= 0))
                {
                    lb_energy_ep.Text = "位能 : " + EP.ToString() + " 焦耳";
                    lb_energy_ek.Text = "動能 : " + EK.ToString() + " 焦耳\t\t總能量" + (EK + EP).ToString() + " 焦耳";
                    lb_velocity.Text = "vx = " + vx.ToString() + " m/s\tvy = " + vy.ToString() + " m/s\tv = " + v.ToString() + " m/s";
                }
                else if (y_st <= 0)
                {
                    y_st = 0;
                    EP = (int)(mass * g * y_st);
                    lb_energy_ep.Text = "位能 : " + EP.ToString() + " 焦耳";
                    lb_energy_ek.Text = "動能 : " + EK.ToString() + " 焦耳\t\t總能量" + (EK + EP).ToString() + " 焦耳";
                    lb_velocity.Text = "vx = " + vx.ToString() + " m/s\tvy = " + vy.ToString() + " m/s\tv = " + v.ToString() + " m/s";
                }
            }

            if (x_st > 1000)
            {
                timer1.Enabled = false;
                angry_bird_move_status = false;
            }

            if (y_st <= 0)
            {
                timer1.Enabled = false;
                angry_bird_move_status = false;
            }

            if (angry_bird_move_status == true)
            {
                x_st += vx * 1;

                if (x_st > 200)
                {
                    drop_down_time++;
                    vy += g * 1;
                    //y_st -= vy * 1;
                    y_st = INITIAL_HEIGHT - g * drop_down_time * drop_down_time / 2;
                }
                t++;
            }

            ww = 100;
            hh = 100;

            string filename_AB_pig = string.Empty;

            if (use_pig_kind == 0)
            {
                bmp = new Bitmap("..//..//img//AB_pig1.jpg");
            }
            else if (use_pig_kind == 1)
            {
                bmp = new Bitmap("..//..//img//AB_pig2.jpg");
            }
            else if (use_pig_kind == 2)
            {
                bmp = new Bitmap("..//..//img//AB_pig3.jpg");
            }
            else if (use_pig_kind == 3)
            {
                bmp = new Bitmap("..//..//img//AB_pig4.jpg");
            }
            else
            {
                bmp = new Bitmap("..//..//img//AB_pig1.jpg");
            }

            Rectangle destRect2 = new Rectangle(W - 100 - ww / 2, 600 - hh / 2, ww, hh);

            e.Graphics.DrawImage(bmp, destRect2, 0, 0, bmp.Width, bmp.Height, units);

            Rectangle destRect3 = new Rectangle(W - 100 - ww / 2, 600 - hh / 2 + hh, ww, 300);
            e.Graphics.FillRectangle(new SolidBrush(Color.Lime), destRect3);
            e.Graphics.DrawString("300 M", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(W - 100 - ww / 2 + 10, 600 - hh / 2 + hh + 5));


            Pen p = new Pen(Color.Black, 5);
            e.Graphics.DrawLine(p, 200, H - 5, W - 100 - ww / 2, H - 5);
            int distance = W - 100 - ww / 2 - 200;
            //richTextBox1.Text += "line = " + distance.ToString() + "\n";
            e.Graphics.DrawString(distance.ToString() + " M", new Font("標楷體", 20), new SolidBrush(Color.Black), new PointF((W - 100 - ww / 2 + 10 + 200) / 2 - 50, H - 40));

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (total_energy < this_energy)
            {
                richTextBox1.Text += "能量不夠，無法發射\n";
                show_main_message("能量不夠，無法發射", S_FALSE, 30);
                return;
            }

            show_main_message("發射", S_OK, 30);

            drop_down_time = 0;
            try_count++;
            lb_shoot_count.Text = "發射次數 : " + try_count.ToString();

            //richTextBox1.Text += "total = " + total_energy.ToString() + "\tthis = " + this_energy.ToString() + "\n";
            total_energy -= this_energy;
            update_energy();

            angry_bird_move_status = true;
            index++;
            t = 0;
            x_st = 0;
            y_st = INITIAL_HEIGHT;
            vx = 10;
            vy = 0;
            timer1.Enabled = true;

            vx = 10 * (int)trackBar1.Value;
            richTextBox1.Text += "初速度 : " + vx.ToString() + " m/s\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // TBD
            if (angry_bird_move_status == true)
            {
                if (button2.Text == "暫停")
                {
                    button2.Text = "繼續";
                    timer1.Enabled = false;

                }
                else
                {
                    button2.Text = "暫停";
                    timer1.Enabled = true;

                }

            }
            //angry_bird_move_status = false;
            //timer1.Enabled = false;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            vx = 10 * (int)trackBar1.Value;
            //richTextBox1.Text += "初速度 : " + vx.ToString() + " m/s\n";

            update_energy();
        }

        private const int COLUMNS = 10;
        private const int ROWS = 8;

        int[,] gray = new int[COLUMNS, ROWS];

        private void button3_Click(object sender, EventArgs e)
        {
            int i;
            //int j;

            int len = pts.Count;
            richTextBox1.Text += "共有 " + len.ToString() + " 個項目, 分別是:\n";

            for (i = 0; i < pts.Count; i++)
            {
                //richTextBox1.Text += pts[i][0].ToString() + "\t" + pts[i][1].ToString() + "\t" + pts[i][2].ToString() + "\n";
                //richTextBox1.Text += i.ToString() + pts[i]
                //int tt = int.Parse(pts[i][1]);
                //richTextBox1.Text += "pts[" + i.ToString() + "][0] = " + pts[i][0].ToString() + "\tpts[" + i.ToString() + "][1] = " + pts[i][1].ToString() + "\n";
            }

            //richTextBox1.Text += pts[0][0].ToString();
            //richTextBox1.Text += pts[1][1].ToString();
            //richTextBox1.Text += pts[3][3].ToString();

            show_main_message("無相機", S_OK, 30);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            try_count = 0;
            total_energy = INITIAL_ENERGY;
            trackBar1.Value = 1;
            x_st = 0;
            y_st = INITIAL_HEIGHT;
            lb_main_mesg.Text = "";
            lb_shoot_count.Text = "發射次數 : " + try_count.ToString();
            lb_energy_ek.Text = "";
            lb_velocity.Text = "";
            trackBar1_Scroll(sender, e);
            rb2.Checked = false;
            rb3.Checked = false;
            rb4.Checked = false;
            rb1.Checked = true;
            rb_bird_CheckedChanged(sender, e);
            update_energy();
            pts.Clear();
            this.pictureBox1.Invalidate();
            richTextBox1.Clear();
        }

        private void rb_bird_CheckedChanged(object sender, EventArgs e)
        {
            if (rb1.Checked == true)
            {
                richTextBox1.Text += "改用 紅鳥 1 Kg\n";
                pictureBox_bird.Image = Image.FromFile("..//..//img//AB_red.jpg");
                mass = 1;
                use_bird_kind = 0;
            }
            else if (rb2.Checked == true)
            {
                richTextBox1.Text += "改用 黃鳥 0.6 Kg\n";
                pictureBox_bird.Image = Image.FromFile("..//..//img//AB_yellow.jpg");
                mass = 0.6f;
                use_bird_kind = 1;
            }
            else if (rb3.Checked == true)
            {
                richTextBox1.Text += "改用 藍鳥 0.3 Kg\n";
                pictureBox_bird.Image = Image.FromFile("..//..//img//AB_blue.jpg");
                mass = 0.3f;
                use_bird_kind = 2;
            }
            else if (rb4.Checked == true)
            {
                richTextBox1.Text += "改用 炸彈鳥 2 Kg\n";
                pictureBox_bird.Image = Image.FromFile("..//..//img//AB_black.jpg");
                mass = 2;
                use_bird_kind = 3;
            }
            else
            {
                richTextBox1.Text += "改用 紅鳥 1 Kg\n";
                pictureBox_bird.Image = Image.FromFile("..//..//img//AB_red.jpg");
                use_bird_kind = 0;
            }
            this.pictureBox1.Invalidate();

            update_energy();
        }

        void update_energy()
        {
            lb_initial_speed.Text = "初速度 : " + vx.ToString() + " m/s";
            this_energy = (int)(mass * vx * vx / 2);
            if (this_energy <= progressBar_this_energy.Maximum)
            {
                progressBar_this_energy.Value = this_energy;
            }
            else
            {
                progressBar_this_energy.Value = progressBar_this_energy.Maximum;
                //progressBar_this_energy 應改成紅色
            }

            lb_this_energy.Text = "預計能量 : " + this_energy.ToString() + " 焦耳";
            lb_total_energy.Text = "總能量 : " + total_energy.ToString() + " 焦耳";
            if ((total_energy >= progressBar_total_energy.Minimum) && (total_energy <= progressBar_total_energy.Maximum))
            {
                progressBar_total_energy.Value = total_energy;
                if (progressBar_total_energy.Value <= (progressBar_total_energy.Maximum * 80 / 100))
                {
                    progressBar_total_energy.ForeColor = Color.Red;
                }
            }
            else
            {
                richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";

            }

        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            use_pig_kind++;
            if (use_pig_kind > 3)
                use_pig_kind = 0;

            if (timer1.Enabled == false)
            {
                pictureBox1.Invalidate();
            }
        }

        void show_main_message(string mesg, int number, int timeout)
        {
            lb_main_mesg.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg.Text = "";
                }
            }
        }

        void playSound(int number)
        {
            //播放系統預設的音效
            switch (number)
            {
                case S_OK:
                    System.Media.SystemSounds.Hand.Play();
                    break;
                case S_FALSE:
                    System.Media.SystemSounds.Beep.Play();
                    break;
                case 2:
                    System.Media.SystemSounds.Asterisk.Play();
                    break;
                case 3:
                    System.Media.SystemSounds.Exclamation.Play();
                    break;
                case 4:
                    System.Media.SystemSounds.Question.Play();
                    break;
                default:
                    System.Media.SystemSounds.Beep.Play();
                    break;
            }
        }
    }
}
