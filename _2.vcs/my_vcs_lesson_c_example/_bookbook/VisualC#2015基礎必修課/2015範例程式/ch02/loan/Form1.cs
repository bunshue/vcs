using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace loan
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
             int loan, year;
             double rate, payRate;
             loan = 500000;
             rate = 0.04;  //年利率
             year = 20;
             //計算每月應付本息金額之平均攤還率
             payRate = ((Math.Pow((1 + rate / 12), year * 12) * rate / 12)) /
                              (Math.Pow((1 + rate / 12), year * 12) - 1);
             //顯示本金
             lblLoan.Text += loan.ToString();
             //顯示年利率
             lblRate.Text += (rate * 100).ToString() + "%";
             //顯示貸款年數
             lblYear.Text += year.ToString();
             //顯示每月應付的本息
             lblPay.Text += ((int)(loan * payRate + 0.5)).ToString();
        }
    }
}
