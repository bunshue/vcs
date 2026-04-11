using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MonthCalendar1
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

            //monthCalendar1.MinDate = DateTime.Now;// 日曆控制項最小可選日期為今日
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            //button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            richTextBox1.Size = new Size(500, 680);
            richTextBox1.Location = new Point(x_st + dx * 2 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1060, 750);
            this.Text = "vcs_MonthCalendar1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
            bool conversionSuccessful = DateTime.TryParse(textBox1.Text, out dt);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "得到DateTime資料： " + dt.ToString() + "\n";
                this.monthCalendar1.SetDate(dt);
            }
            else
            {
                richTextBox1.Text += "DateTime.TryParse 失敗\n";
                richTextBox1.Text += "取得DateTime失敗 3\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //set the date of today
            this.monthCalendar1.SetDate(this.monthCalendar1.TodayDate.Date);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += Environment.NewLine + "指定送貨日期為" + monthCalendar1.SelectionRange.Start.ToShortDateString() + "至" + monthCalendar1.SelectionRange.End.ToShortDateString() + " 送達貴處";
        }


        private void monthCalendar1_DateChanged(object sender, DateRangeEventArgs e)
        {
            //richTextBox1.Text += "你選擇了 : "+
        }

    }
}


/*
            //set the date of today
            //this.monthCalendar1.SetDate(this.monthCalendar1.TodayDate.Date);

                //this.monthCalendar1.SetDate(dt);


            this.monthCalendar1.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.monthCalendar1.RightToLeft = System.Windows.Forms.RightToLeft.No;

            int Aday, Amonth, Ayear;
            Aday = this.monthCalendar1.SelectionStart.Day;
            Amonth = this.monthCalendar1.SelectionStart.Month;
            Ayear = this.monthCalendar1.SelectionStart.Year;

 * Aday = this.monthCalendar1.SelectionStart.Day;
            Amonth = this.monthCalendar1.SelectionStart.Month;
            Ayear = this.monthCalendar1.SelectionStart.Year;

*/
