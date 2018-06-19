using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_05
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //DateTime dt = new DateTime(2006, 3, 11);	//年月日
            DateTime dt = new DateTime(2006, 3, 11, 9, 15, 10, 20);	//年月日時分秒毫秒
            label1.Text = "完整日期： " + dt.ToString("D");
            label2.Text = "簡短日期： " + dt.ToString("d");
            label3.Text = "完整日期及時間： " + dt.ToString("F");
            label4.Text = "一般日期： " + dt.ToString("G");
            label5.Text = "月日格式： " + dt.ToString("M");
            label6.Text = "完整時間： " + dt.ToString("T");
            label7.Text = "簡短時間： " + dt.ToString("t");
            label8.Text = "年月格式： " + dt.ToString("Y");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label9.Text = "完整日期： " + DateTime.Now.ToString("D");
            label10.Text = "簡短日期： " + DateTime.Now.ToString("d");
            label11.Text = "完整日期及時間： " + DateTime.Now.ToString("F");
            label12.Text = "一般日期： " + DateTime.Now.ToString("G");
            label13.Text = "月日格式： " + DateTime.Now.ToString("M");
            label14.Text = "完整時間： " + DateTime.Now.ToString("T");
            label15.Text = "簡短時間： " + DateTime.Now.ToString("t");
            label16.Text = "年月格式： " + DateTime.Now.ToString("Y");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("時間資料範例。");
        }
    }
}
