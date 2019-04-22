using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Stopwatch

namespace vcs_MyClock
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Stopwatch sw = new Stopwatch();

        private const int _MODE_CLOCK = 0;  //一般
        private const int _MODE_STOPWATCH = 1;  //正數、碼表、stopwatch
        private const int _MODE_TIMER = 2;  //倒數
        private const int _MODE_ALARM = 3;  //鬧鐘

        //一般
        private const int _MODE_CLOCK_STATE_0 = 0;  //一般

        //正數
        private const int _MODE_STOPWATCH_STATE_0 = 0;  //正數準備中
        private const int _MODE_STOPWATCH_STATE_1 = 1;  //正數中、正數繼續
        private const int _MODE_STOPWATCH_STATE_2 = 2;  //正數暫停
        private const int _MODE_STOPWATCH_STATE_3 = 3;  //正數暫停歸零中

        //倒數
        private const int _MODE_TIMER_STATE_0 = 0;  //倒數準備中
        private const int _MODE_TIMER_STATE_1 = 1;  //倒數中
        private const int _MODE_TIMER_STATE_2 = 2;  //倒數暫停
        private const int _MODE_TIMER_STATE_3 = 3;  //倒數時間到

        //鬧鐘
        private const int _MODE_ALARM_STATE_0 = 0;  //鬧鐘準備中、時間到
        private const int _MODE_ALARM_STATE_1 = 1;  //鬧鐘開始
        //private const int _MODE_ALARM_STATE_2 = 2;  //鬧鐘時間到

        int flag_mode = _MODE_CLOCK;    //0:時鐘、1:正數、2:倒數、3:鬧鐘
        int flag_state = _MODE_CLOCK_STATE_0;

        int total_count_down_sec = 0;
        DateTime time_stop;
        DateTime time_pause_start;
        DateTime time_pause_stop;

        DateTime alarm_target;

        //int status = 0;
        System.DateTime time_sp;
        System.DateTime time_st;
        TimeSpan time_diff;
        TimeSpan time_diff_total;


        //for ananog clock
        //int WIDTH = 300, HEIGHT = 300, secHAND = 140, minHAND = 110, hrHAND = 80;
        int WIDTH = 150, HEIGHT = 150, secHAND = 70, minHAND = 55, hrHAND = 40;

        //center
        int cx, cy;

        Bitmap bmp;
        Graphics g;

        
        private void Form1_Load(object sender, EventArgs e)
        {
            digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
            lb_mesg.Text = "";
            lb_alarm_target.Text = "";
            //this.FormBorderStyle = FormBorderStyle.None;
            time_pause_start = DateTime.Now;
            time_pause_stop = time_pause_start;

            time_st = DateTime.Now;
            time_sp = DateTime.Now;
            time_diff = time_sp - time_st;
            time_diff_total = time_diff;
            this.Height = 161 - 38;

            //for analog clock
            //this.ClientSize = new Size(WIDTH + 20, HEIGHT + 20);
            //create bitmap
            bmp = new Bitmap(WIDTH + 1, HEIGHT + 1);
            //center
            cx = WIDTH / 2;
            cy = HEIGHT / 2;

            //backcolor
            //this.BackColor = Color.White;

            //明確指定Form表單的起始點位置
            //this.StartPosition = System.Windows.Forms.FormStartPosition.Manual;
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(1920 - this.Width, 75);
            //this.Location = new System.Drawing.Point(this.Right, this.Top);



        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime dt_now = DateTime.Now;
            toolStripStatusLabel1.Text = dt_now.ToString();
            if ((flag_mode == _MODE_CLOCK) && (flag_state == _MODE_CLOCK_STATE_0))
            {
                digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
            }
            else if ((flag_mode == _MODE_TIMER) && (flag_state == _MODE_TIMER_STATE_1))
            {
                if (time_stop <= dt_now)
                {
                    this.TopMost = true;
                    //timer1.Enabled = false;
                    flag_state = _MODE_TIMER_STATE_3;
                    //digitalDisplayControl1.BackColor = Color.Red;
                    this.BackColor = Color.Red;
                    this.WindowState = FormWindowState.Normal;
                    digitalDisplayControl1.DigitColor = Color.Purple;
                    digitalDisplayControl1.DigitText = "00.00";
                }
                else
                {
                    TimeSpan ts1 = time_stop - dt_now;
                    double remain1 = Convert.ToDouble(ts1.TotalSeconds) + Convert.ToDouble(time_diff_total.TotalSeconds);
                    double remain2;
                    int hh;
                    int mm;
                    int ss;
                    double ms;
                    hh = (int)remain1 / 3600;
                    mm = (int)(remain1 % 3600) / 60;
                    ss = (int)remain1 % 60;
                    ms = remain1 % 1;
                    remain2 = hh * 10000 + mm * 100 + ss + ms;
                    if (remain1 >= 3600)
                        digitalDisplayControl1.DigitText = remain2.ToString("00:00:00.00");
                    else if (remain1 >= 60)
                        digitalDisplayControl1.DigitText = remain2.ToString("00:00.00");
                    else
                        digitalDisplayControl1.DigitText = remain2.ToString("00.00");
                }
            }
            else if ((flag_mode == _MODE_STOPWATCH) && (flag_state == _MODE_STOPWATCH_STATE_1))
            {
                double ms = sw.ElapsedMilliseconds;

                TimeSpan ts = sw.Elapsed;

                string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
                            ts.Hours, ts.Minutes, ts.Seconds,
                            ts.Milliseconds / 10);
                digitalDisplayControl1.DigitText = elapsedTime;
            }
            else if ((flag_mode == _MODE_STOPWATCH) && (flag_state == _MODE_STOPWATCH_STATE_2))
            {
                //正數暫停中，不做事
            }
            else if ((flag_mode == _MODE_STOPWATCH) && (flag_state == _MODE_STOPWATCH_STATE_3))
            {
                //正數暫停歸零中，不做事
            }
            else if (flag_mode == _MODE_ALARM)
            {
                digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
            }
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            tabControl1.SelectedIndex = 0;
            flag_mode = _MODE_CLOCK;
            flag_state = _MODE_CLOCK_STATE_0;
            lb_mesg.Text = "時鐘模式";

            if (show_setup_panel == 1)
            {
                show_setup_panel = 0;
                update_show_setup_panel(show_setup_panel);
            }
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            tabControl1.SelectedIndex = 1;
            flag_mode = _MODE_STOPWATCH;
            flag_state = _MODE_STOPWATCH_STATE_0;
            digitalDisplayControl1.DigitText = "00:00:00.00";
            lb_mesg.Text = "正數模式";
            if (show_setup_panel == 0)
            {
                show_setup_panel = 1;
                update_show_setup_panel(show_setup_panel);
            }
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            tabControl1.SelectedIndex = 2;
            flag_mode = _MODE_TIMER;
            flag_state = _MODE_TIMER_STATE_0;
            digitalDisplayControl1.DigitText = "00.00";
            lb_mesg.Text = "倒數模式";
            if (show_setup_panel == 0)
            {
                show_setup_panel = 1;
                update_show_setup_panel(show_setup_panel);
            }
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {
            tabControl1.SelectedIndex = 3;
            flag_mode = _MODE_ALARM;
            flag_state = _MODE_ALARM_STATE_0;
            //digitalDisplayControl1.DigitText = "00.00";
            lb_mesg.Text = "鬧鐘模式";
            if (show_setup_panel == 0)
            {
                show_setup_panel = 1;
                update_show_setup_panel(show_setup_panel);
                update_alarm_time();
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button17_Click(object sender, EventArgs e)
        {
            if ((flag_mode == _MODE_STOPWATCH) && ((flag_state == _MODE_STOPWATCH_STATE_0) || (flag_state == _MODE_STOPWATCH_STATE_3)))
            {
                sw.Start();
                flag_state = _MODE_STOPWATCH_STATE_1;
                lb_mesg.Text = "正數中";
            }
            else if ((flag_mode == _MODE_STOPWATCH) && ((flag_state == _MODE_STOPWATCH_STATE_1) || (flag_state == _MODE_STOPWATCH_STATE_3)))
            {
                sw.Stop();
                flag_state = _MODE_STOPWATCH_STATE_2;
                lb_mesg.Text = "正數暫停";
            }
            else if ((flag_mode == _MODE_STOPWATCH) && (flag_state == _MODE_STOPWATCH_STATE_2))
            {
                sw.Start();
                flag_state = _MODE_STOPWATCH_STATE_1;
                lb_mesg.Text = "正數繼續";
            }
            richTextBox1.Text += "b17, flag_state = " + flag_state.ToString() + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            if ((flag_mode == _MODE_STOPWATCH) && (flag_state == _MODE_STOPWATCH_STATE_0))
            {
                //開始準備中、暫停中、停止中按停止，把數字歸零
                flag_mode = _MODE_STOPWATCH;
                flag_state = _MODE_STOPWATCH_STATE_0;
                digitalDisplayControl1.DigitText = "00:00:00.00";
                lb_mesg.Text = "歸零";
                sw.Reset();
            }
            else if ((flag_mode == _MODE_STOPWATCH) && (flag_state == _MODE_STOPWATCH_STATE_1))
            {
                //正數中按停止，數字停止
                flag_mode = _MODE_STOPWATCH;
                flag_state = _MODE_STOPWATCH_STATE_0;
                lb_mesg.Text = "正數停止";
                sw.Stop();
            }
            else if ((flag_mode == _MODE_STOPWATCH) && (flag_state == _MODE_STOPWATCH_STATE_2))
            {
                //暫停中、停止中按停止，把數字歸零
                flag_mode = _MODE_STOPWATCH;
                flag_state = _MODE_STOPWATCH_STATE_0;
                digitalDisplayControl1.DigitText = "00:00:00.00";
                lb_mesg.Text = "歸零";
                sw.Reset();
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            if ((flag_mode == _MODE_TIMER) && (flag_state == _MODE_TIMER_STATE_0))
            {
                flag_state = _MODE_TIMER_STATE_1;   //倒數中
                lb_mesg.Text = "正數";
                digitalDisplayControl1.DigitColor = Color.Red;
                this.TopMost = false;
                int hh = (int)numericUpDown1.Value;
                int mm = (int)numericUpDown2.Value;
                int ss = (int)numericUpDown3.Value;
                total_count_down_sec = hh * 60 * 60 + mm * 60 + ss;
                richTextBox1.Text += "total_count_down_sec = " + total_count_down_sec.ToString() + "\n";


                System.DateTime dt = System.DateTime.Now;
                //richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + Environment.NewLine;
                //richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + Environment.NewLine;

                //現在時間減分鐘寫法
                time_stop = dt.AddSeconds(total_count_down_sec);
                //richTextBox1.Text += "現在時間加" + total_count_down_sec.ToString() + "秒： " + time_stop.ToLongTimeString() + Environment.NewLine;
                //timer1.Enabled = true;
                richTextBox1.Text += "1111111111\n";
            }
            //else if ((flag_mode == _MODE_TIMER) && ((flag_state == _MODE_TIMER_STATE_1) || (flag_state == _MODE_TIMER_STATE_3)))
            else if ((flag_mode == _MODE_TIMER) && (flag_state == _MODE_TIMER_STATE_1))
            {
                //倒數暫停
                flag_state = _MODE_TIMER_STATE_2;   //倒數暫停
                lb_mesg.Text = "倒數暫停";
                time_pause_start = DateTime.Now;
                time_st = DateTime.Now;
                this.TopMost = false;
                //digitalDisplayControl1.BackColor = Color.Transparent;
                //this.BackColor = System.Drawing.SystemColors.Control;
                this.BackColor = default(Color);
                digitalDisplayControl1.DigitColor = Color.Purple;
                richTextBox1.Text += "2222222222\n";
            }
            else if ((flag_mode == _MODE_TIMER) && (flag_state == _MODE_TIMER_STATE_2))
            {
                flag_state = _MODE_TIMER_STATE_1;   //繼續倒數中
                lb_mesg.Text = "繼續倒數中";
                time_pause_stop = DateTime.Now;

                time_sp = DateTime.Now;
                time_diff = time_sp - time_st;
                time_diff_total += time_diff;

                digitalDisplayControl1.DigitColor = Color.Red;
                this.TopMost = false;
                /*
                int hh = (int)numericUpDown1.Value;
                int mm = (int)numericUpDown2.Value;
                int ss = (int)numericUpDown3.Value;
                total_count_down_sec = hh * 60 * 60 + mm * 60 + ss;
                //richTextBox1.Text += "total_count_down_sec = " + total_count_down_sec.ToString() + "\n";


                System.DateTime dt = System.DateTime.Now;
                //richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + Environment.NewLine;
                //richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + Environment.NewLine;

                //現在時間減分鐘寫法
                time_stop = dt.AddSeconds(total_count_down_sec);
                //richTextBox1.Text += "現在時間加" + total_count_down_sec.ToString() + "秒： " + time_stop.ToLongTimeString() + Environment.NewLine;
                //timer1.Enabled = true;
                richTextBox1.Text += "1111111111\n";
                */

            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if ((flag_mode == _MODE_TIMER) && ((flag_state == _MODE_TIMER_STATE_1) || (flag_state == _MODE_TIMER_STATE_3)))
            {
                //倒數取消
                flag_state = _MODE_TIMER_STATE_0;
                lb_mesg.Text = "倒數取消";
                this.TopMost = false;
                //digitalDisplayControl1.BackColor = Color.Transparent;
                //this.BackColor = System.Drawing.SystemColors.Control;
                this.BackColor = default(Color);
                digitalDisplayControl1.DigitColor = Color.Purple;
                richTextBox1.Text += "2222222222\n";
            }
            else if ((flag_mode == _MODE_TIMER) && (flag_state == _MODE_TIMER_STATE_2))
            {
                //倒數暫停中按STOP，清除變數
                flag_state = _MODE_TIMER_STATE_0;
                lb_mesg.Text = "數字歸位";
                this.TopMost = false;
                //digitalDisplayControl1.BackColor = Color.Transparent;
                //this.BackColor = System.Drawing.SystemColors.Control;
                this.BackColor = default(Color);
                digitalDisplayControl1.DigitColor = Color.Purple;
                if (total_count_down_sec >= 3600)
                    digitalDisplayControl1.DigitText = total_count_down_sec.ToString("00:00:00.00");
                else if (total_count_down_sec >= 60)
                    digitalDisplayControl1.DigitText = total_count_down_sec.ToString("00:00.00");
                else
                    digitalDisplayControl1.DigitText = total_count_down_sec.ToString("00.00");

                
                richTextBox1.Text += "2222222222 + total_count_down_sec = " + total_count_down_sec.ToString() + "\n";

                //total_count_down_sec

            }

        }

        private void tabControl1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (tabControl1.SelectedIndex == 0)
                radioButton1.Checked = true;
            else if (tabControl1.SelectedIndex == 1)
                radioButton2.Checked = true;
            else if (tabControl1.SelectedIndex == 2)
                radioButton3.Checked = true;
            else if (tabControl1.SelectedIndex == 3)
            {
                radioButton4.Checked = true;
                update_alarm_time();
            }
        }

        int show_setup_panel = 0;
        private void button4_Click(object sender, EventArgs e)
        {
            if (show_setup_panel == 0)
            {
                show_setup_panel = 1;
            }
            else
            {
                if (show_comport_log_panel == 1)
                {
                    show_comport_log_panel = 0;
                    update_show_comport_log_panel(show_comport_log_panel);
                }

                show_setup_panel = 0;
            }
            update_show_setup_panel(show_setup_panel);
        }

        void update_show_setup_panel(int show_setup_panel)
        {
            if (show_setup_panel == 1)
            {
                button4.BackgroundImage = vcs_MyClock.Properties.Resources.close;
                this.Height += 220;
                update_calendar();
            }
            else
            {
                button4.BackgroundImage = vcs_MyClock.Properties.Resources.open;
                this.Height -= 220;
            }
        }

        void update_calendar()
        {
            DateTime dt = DateTime.Now;
            lb_yy.Text = dt.Year.ToString();

            string[] Month_name = new string[] { "一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"};
            string month = Month_name[Convert.ToInt32(dt.Month.ToString("d"))].ToString();

            //lb_mm1.Text = dt.Month.ToString();
            lb_mm1.Text = month;
            lb_dd1.Text = dt.Day.ToString();

            string[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();
            lb_weekday.Text = week;

            System.Globalization.TaiwanLunisolarCalendar TA = new System.Globalization.TaiwanLunisolarCalendar();
            lb_mm2.Text = TA.GetMonth(dt).ToString();
            lb_dd2.Text = TA.GetDayOfMonth(dt).ToString();

            
        
        
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (sw.IsRunning == true)
            {
                sw.Restart();
                digitalDisplayControl1.DigitText = "00:00:00.00";
                lb_mesg.Text = "正數重數";
            }
            else
            {
                sw.Reset();
                digitalDisplayControl1.DigitText = "00:00:00.00";
                lb_mesg.Text = "歸零";
            }
        }


        private void timer2_Tick(object sender, EventArgs e)
        {
            //create graphics
            g = Graphics.FromImage(bmp);

            //get time
            int ss = DateTime.Now.Second;
            int mm = DateTime.Now.Minute;
            int hh = DateTime.Now.Hour;

            int[] handCoord = new int[2];

            //clear
            g.Clear(Color.White);

            //draw circle
            g.DrawEllipse(new Pen(Color.Black, 1f), 0, 0, WIDTH, HEIGHT);

            //draw figure
            g.DrawString("12", new Font("Arial", 12), Brushes.Black, new PointF(64, 1));
            g.DrawString("3", new Font("Arial", 12), Brushes.Black, new PointF(138, 68));
            g.DrawString("6", new Font("Arial", 12), Brushes.Black, new PointF(68, 133));
            g.DrawString("9", new Font("Arial", 12), Brushes.Black, new PointF(0, 68));

            //second hand
            handCoord = msCoord(ss, secHAND);
            g.DrawLine(new Pen(Color.Red, 1f), new Point(cx, cy), new Point(handCoord[0], handCoord[1]));

            //minute hand
            handCoord = msCoord(mm, minHAND);
            g.DrawLine(new Pen(Color.Black, 2f), new Point(cx, cy), new Point(handCoord[0], handCoord[1]));

            //hour hand
            handCoord = hrCoord(hh % 12, mm, hrHAND);
            g.DrawLine(new Pen(Color.Gray, 3f), new Point(cx, cy), new Point(handCoord[0], handCoord[1]));

            //load bmp in picturebox1
            pictureBox1.Image = bmp;

            //disp time
            //this.Text = "Analog Clock -  " + hh + ":" + mm + ":" + ss;
            this.Text = "ims_Clock - " + hh + ":" + mm + ":" + ss;

            //dispose
            g.Dispose();

            if ((flag_mode == _MODE_ALARM) && (flag_state == _MODE_ALARM_STATE_1))
            {
                if (alarm_target > DateTime.Now)
                {
                    if ((ss % 2) == 0)
                    {
                        lb_alarm_target.Text = alarm_target.ToString();
                    }
                    else
                    {
                        lb_alarm_target.Text = "";
                    }
                }
                else
                {
                    richTextBox1.Text += "時間到";
                    flag_state = _MODE_ALARM_STATE_0;
                    this.TopMost = true;
                }


            }


        }

        //coord for minute and second hand
        private int[] msCoord(int val, int hlen)
        {
            int[] coord = new int[2];
            val *= 6;   //each minute and second make 6 degree

            if (val >= 0 && val <= 180)
            {
                coord[0] = cx + (int)(hlen * Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            else
            {
                coord[0] = cx - (int)(hlen * -Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            return coord;
        }

        //coord for hour hand
        private int[] hrCoord(int hval, int mval, int hlen)
        {
            int[] coord = new int[2];

            //each hour makes 30 degree
            //each min makes 0.5 degree
            int val = (int)((hval * 30) + (mval * 0.5));

            if (val >= 0 && val <= 180)
            {
                coord[0] = cx + (int)(hlen * Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            else
            {
                coord[0] = cx - (int)(hlen * -Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            return coord;
        }

        int show_comport_log_panel = 0;
        private void button5_Click(object sender, EventArgs e)
        {
            if (show_comport_log_panel == 0)
            {
                show_comport_log_panel = 1;
            }
            else
            {
                show_comport_log_panel = 0;
            }
            update_show_comport_log_panel(show_comport_log_panel);

        }

        void update_show_comport_log_panel(int show_comport_log_panel)
        {
            if (show_comport_log_panel == 1)
            {
                button5.BackgroundImage = vcs_MyClock.Properties.Resources.close;
                this.Height += 143;
            }
            else
            {
                button5.BackgroundImage = vcs_MyClock.Properties.Resources.open;
                this.Height -= 143;
            }
        }

        void update_alarm_time()
        {
            DateTime dt = DateTime.Now;
            richTextBox1.Text += "時：" + dt.Hour.ToString() + "\t";
            richTextBox1.Text += "分：" + dt.Minute.ToString() + "\t";
            richTextBox1.Text += "秒：" + dt.Second.ToString() + "\n";
            numericUpDown4.Value = dt.Hour;
            numericUpDown5.Value = dt.Minute;
            numericUpDown6.Value = dt.Second;

        
        
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //richTextBox1.Text += "dt1 = " + alarm_target.ToString() + "\n";
            alarm_target = new DateTime(2019, 3, 18, (int)numericUpDown4.Value, (int)numericUpDown5.Value, (int)numericUpDown6.Value);
            //richTextBox1.Text += "dt1 = " + alarm_target.ToString() + "\n";
            flag_mode = _MODE_ALARM;
            flag_state = _MODE_ALARM_STATE_1;
            lb_alarm_target.Text = alarm_target.ToString();
            this.TopMost = false;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            flag_mode = _MODE_ALARM;
            flag_state = _MODE_ALARM_STATE_0;
            lb_alarm_target.Text = "";
            this.TopMost = false;
        }

        private void digitalDisplayControl1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();                             //關閉視窗
            //this.WindowState = FormWindowState.Minimized; //最小化視窗
        }


        //***********************
        private Point mouseOffset;//记录鼠标坐标
        private bool isMouseDown = false;//是否按下鼠标
        //***********************

        #region 移动无边框窗体
        private void digitalDisplayControl1_MouseDown(object sender, MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X;
                yOffset = -e.Y;
                mouseOffset = new Point(xOffset, yOffset);
                isMouseDown = true;
            }
        }

        private void digitalDisplayControl1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset.X, mouseOffset.Y);
                Location = mousePos;
            }
        }

        private void digitalDisplayControl1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isMouseDown = false;
            }
        }
        #endregion



    }
}
