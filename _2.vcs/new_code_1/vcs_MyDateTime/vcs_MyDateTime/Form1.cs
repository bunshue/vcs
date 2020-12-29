using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyDateTime
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string dd1 = "541年7月21日";
            string dd2 = "20060311";
            DateTime dt;

            dt = ParseDate(dd2);

            richTextBox1.Text += "result year = " + dt.Year.ToString() + ", month = " + dt.Month.ToString() + ", day = " + dt.Day.ToString() + "\n";


        }

        private DateTime ParseDate(string date_text)
        {
            int year = int.Parse(date_text.Substring(0, 4));
            int month = int.Parse(date_text.Substring(4, 2));
            int day = int.Parse(date_text.Substring(6));
            return new DateTime(year, month, day);
        }
    }
}
