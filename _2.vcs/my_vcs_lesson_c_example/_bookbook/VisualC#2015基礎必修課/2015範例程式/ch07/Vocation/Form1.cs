using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Vocation
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            nudYears.Maximum = 40;
            nudYears.Value = 1;
            mcaVacation.MinDate = DateTime.Today;   //最早選擇日期設為今天
        }
        // 數字鈕Value改變時執行
        private void nudYears_ValueChanged(object sender, EventArgs e)
        {

            int days = 0;  // 宣告days用來存放休假天數
            if (nudYears.Value <= 1)   // 年資大於1
            {
                days = 1;
            }
            else if (nudYears.Value >= 2 && nudYears.Value <= 5)  // 年資2-5年
            {
                days = 3;
            }
            else if (nudYears.Value >= 6 && nudYears.Value <= 10) // 年資6-10年
            {
                days = 5;
            }
            else if (nudYears.Value >= 11 && nudYears.Value <= 20) //年資11-20年
            {
                days = 14;
            }
            else if (nudYears.Value >= 21) // 年資21年以上
            {
                days = 21;
            }
            lblVacation.Text = "最多可挑選連休假期 " + days.ToString() + " 天";
            // 設定最多可選取休假的天數
            mcaVacation.MaxSelectionCount = days;
        }
        // 按 [確定] 鈕執行
        private void btnOk_Click(object sender, EventArgs e)
        {
            MessageBox.Show("你選擇 " + mcaVacation.SelectionStart.ToString("yyyy/MM/dd") + " 到 " + mcaVacation.SelectionEnd.ToString("yyyy/MM/dd") + " 為假期");
        }
    }
}
