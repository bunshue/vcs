using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Stream

using System.Management;    //for ManagementObjectSearcher

using System.Globalization; //for 民國 農曆


namespace calendar
{
    public partial class Form1 : Form
    {


        public Form1()
        {
            InitializeComponent();
        }

        string[] SolarTerm = new string[] { 
            "小寒", "大寒", "立春", "雨水", 
            "驚蟄", "春分", "清明", "穀雨", 
            "立夏", "小滿", "芒種", "夏至", 
            "小暑", "大暑", "立秋", "處暑", 
            "白露", "秋分", "寒露", "霜降", 
            "立冬", "小雪", "大雪", "冬至" };

        string[] LunarHolDayName =
                  {
                  "小寒", "大寒", "立春", "雨水",
                  "驚蟄", "春分", "清明", "谷雨",
                  "立夏", "小滿", "芒種", "夏至",
                  "小暑", "大暑", "立秋", "處暑",
                  "白露", "秋分", "寒露", "霜降",
                  "立冬", "小雪", "大雪", "冬至"};

        private void button2_Click(object sender, EventArgs e)
        {
            foreach (string str in SolarTerm)
            {
                richTextBox1.Text += str + " ";
            }
            richTextBox1.Text += "\n";

            foreach (string str in LunarHolDayName)
            {
                richTextBox1.Text += str + " ";
            }
            richTextBox1.Text += "\n";
        }




        private void Form1_Load(object sender, EventArgs e)
        {
        }


        private void monthCalendar1_DateChanged(object sender, DateRangeEventArgs e)
        {
            /*
            //monthCalendar1.Visible = false;
            label1.Text = monthCalendar1.TodayDate.Year.ToString();
            label1.Text += "/" + monthCalendar1.TodayDate.Month.ToString();
            label1.Text += "/" + monthCalendar1.TodayDate.Day.ToString();


            label1.Text += " " + DateTime.Now.Hour;
            label1.Text += ":" + DateTime.Now.Minute;
            label1.Text += ":" + DateTime.Now.Second;
            */


        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            label1.Text = dateTimePicker1.Value.Year.ToString();
            label1.Text += "/" + dateTimePicker1.Value.Month.ToString();
            label1.Text += "/" + dateTimePicker1.Value.Day.ToString();


            label1.Text += " " + DateTime.Now.Hour;
            label1.Text += ":" + DateTime.Now.Minute;
            label1.Text += ":" + DateTime.Now.Second;

        }


    }
}
