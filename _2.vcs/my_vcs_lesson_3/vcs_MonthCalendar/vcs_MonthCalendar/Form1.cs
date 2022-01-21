using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MonthCalendar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            monthCalendar1.MaxSelectionCount = 1;   //設定最多可選取的天數
        }

        private void monthCalendar1_DateChanged(object sender, DateRangeEventArgs e)
        {
            richTextBox1.Text += "你選擇了 : " + monthCalendar1.SelectionStart.ToString() + "\n";
            if (radioButton2.Checked == true)
            {
                richTextBox1.Text += "選擇連續5天\n";
                richTextBox1.Text += "你選擇了 : " + monthCalendar1.SelectionStart.ToString("yyyy/MM/dd") + " 到 " + monthCalendar1.SelectionEnd.ToString("yyyy/MM/dd") + "\n";
            }
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                monthCalendar1.MinDate = DateTime.Today;
            }
            else
            {
                //不知道怎麼恢復

            }
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton2.Checked == true)
            {
                monthCalendar1.MaxSelectionCount = 5;
            }
            else
            {
                monthCalendar1.MaxSelectionCount = 1;
            }

        }



    }
}
