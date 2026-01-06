using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DateTimePicker
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

        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            //groupBox5.Location = new Point(x_st + dx * 2, y_st + dy * 5 + 10);//DateTimePicker
            //groupBox8.Location = new Point(x_st + dx * 2 + 200, y_st + dy * 5 + 10);//DateTimePicker
            groupBox8.Size = new Size(250, 160);
            groupBox5.Size = new Size(180, 160);

            textBox2.Size = new Size(160, 40);
            dateTimePicker1.Size = new Size(160, 40);
            //textBox2.Location = new Point(x_st + dx * 0 - 5, y_st + dy * 0 + 10);
            //bt1.Location = new Point(x_st + 170, y_st + dy * 0 + 10);
            //dateTimePicker1.Location = new Point(x_st + dx * 0 - 5, y_st + dy * 0 + 60);
            //bt2.Location = new Point(x_st + 170, y_st + dy * 0 + 60);

            richTextBox1.Size = new Size(340, 700);
            //richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            lb_time_interval.Text = "------------";

            //this.Size = new Size(1290, 770);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        int flag_timer_counter_down_enable = 0;
        DateTime dt_timer_st = DateTime.Now;
        int wait_seconds = 0;

        private void bt1_Click(object sender, EventArgs e)
        {
            this.TopMost = false;
            if (flag_timer_counter_down_enable == 1)
            {
                flag_timer_counter_down_enable = 0;
                bt1.Text = "倒數";
            }
            else
            {
                flag_timer_counter_down_enable = 1;
                bt1.Text = "停止";

                dt_timer_st = DateTime.Now;
                wait_seconds = int.Parse(textBox2.Text) * 60;
                richTextBox1.Text += "等待時間： " + wait_seconds.ToString() + "\n";
            }

        }

        private void bt2_Click(object sender, EventArgs e)
        {
            //dateTimePicker3.Value = new DateTime(2006, 3, 11);                //特定日期
            //dateTimePicker3.Value = Convert.ToDateTime("2006/3/11 9:15:30");  //特定日期與時間
            //dateTimePicker3.Value = DateTime.Today;                      //今天日期
            this.dateTimePicker3.Value = DateTime.Now;                          //現在時刻

        }

        private void bt_dtp_set_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "設定DateTimePicker的顯示範圍\n";
            richTextBox1.Text += "顯示現在到未來12天\n";
            dateTimePicker4.MinDate = DateTime.Today;//當天時間
            dateTimePicker4.MaxDate = DateTime.Today.AddDays(12);
        }

        private void bt_dtp_get_Click(object sender, EventArgs e)
        {
            string date1 = dateTimePicker4.Value.Month.ToString() + "/" + dateTimePicker4.Value.Day.ToString();
            richTextBox1.Text += "你選取的日期是 : " + date1.ToString() + "\n";

            string date2 = DateTime.Today.AddDays(12).Month.ToString() + "/" + DateTime.Today.AddDays(12).Day.ToString();
            richTextBox1.Text += "12天後的日期是 : " + date2.ToString() + "\n";
        }

        private void dateTimePicker3_ValueChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "The selected value is " + dateTimePicker3.Value + "\n";
            richTextBox1.Text += "The selected value is " + dateTimePicker3.Text + "\n";
            richTextBox1.Text += "The day of the week is " + dateTimePicker3.Value.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "The day of the year is " + dateTimePicker3.Value.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "Millisecond is: " + dateTimePicker3.Value.Millisecond.ToString() + "\n";

            richTextBox1.Text += "\n";
            richTextBox1.Text += dateTimePicker3.Value.Year.ToString();
            richTextBox1.Text += "/" + dateTimePicker3.Value.Month.ToString();
            richTextBox1.Text += "/" + dateTimePicker3.Value.Day.ToString();

            DateTime dt = DateTime.Now;
            richTextBox1.Text += " " + dt.Hour;
            richTextBox1.Text += ":" + dt.Minute;
            richTextBox1.Text += ":" + dt.Second;
            richTextBox1.Text += "\n";

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (flag_timer_counter_down_enable == 1)
            {
                DateTime dt = DateTime.Now;
                TimeSpan interval = dt - dt_timer_st;

                //richTextBox1.Text += "與現在相距：" + ts2.ToString() + "\n";

                //TimeSpan interval = dt - dt.Date;
                //richTextBox1.Text += dt.ToString() + "\n";
                //richTextBox1.Text += dt.Date.ToString() + "\n";
                //richTextBox1.Text += "xxx " + interval.TotalSeconds.ToString();// +"\n";
                lb_time_interval.Text = "經過 : " + interval.TotalSeconds.ToString();

                if (interval.TotalSeconds > wait_seconds)
                {
                    this.TopMost = true;
                    lb_time_interval.Text += "yyyy";
                    richTextBox1.Text += "Q ";
                }
            }



        }
    }
}




//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個



