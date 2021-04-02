using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace SnatchPresentSystemDate
{
    public partial class SnatchPresentSystemDate : Form
    {
        public SnatchPresentSystemDate()
        {
            InitializeComponent();
        }

        private void SnatchPresentSystemDate_Load(object sender, EventArgs e)
        {
            year.Value = Convert.ToDecimal(DateTime.Now.Year);//設置當前系統日期中的年份
            month.Value = Convert.ToDecimal(DateTime.Now.Month);//設置當前系統日期中的月份
            day.Value = Convert.ToDecimal(DateTime.Now.Day);//設置當前系統日期中的日
            year.ReadOnly = true;//設置顯示年份的區域為只讀的
            month.ReadOnly = true;//設置顯示月份的區域為只讀的
            day.ReadOnly = true;//設置顯示日的區域為只讀的     
        }
    }
}
