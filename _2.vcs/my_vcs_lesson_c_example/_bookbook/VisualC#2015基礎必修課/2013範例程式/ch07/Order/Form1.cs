using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Order
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            dtpDate.MinDate = DateTime.Today;
            dtpDate.MaxDate = DateTime.Today.AddDays(9);
            txtId.MaxLength = 10;  //設身份證字號最多10個字元
        }
        // 數字鈕Value攻變時執行
        private void nudTicket_ValueChanged(object sender, EventArgs e)
        {
            int[,] fee = { { 0, 700, 1490 }, { 700, 0, 790 }, { 1490, 790, 0 } };
            int num, row, col;
            num = (int)nudTicket.Value;
            row = cbxStart.SelectedIndex;
            col = cbxArrival.SelectedIndex;
            lblTotal.Text = (num * fee[row, col]).ToString();
        }
        // 按 [確定] 鈕執行 
        private void btnOK_Click(object sender, EventArgs e)
        {
            string str1, date1, date2;
            str1 = "您訂購";
            date1 = dtpDate.Value.Month.ToString() + "/" + dtpDate.Value.Day.ToString();
            str1 += date1 + " ";
            str1 += cbxTime.Text + '\n';
            str1 += cbxStart.Text + " 到 ";
            str1 += cbxArrival.Text + '\n';
            str1 += "車票" + nudTicket.Value.ToString() + "張 \n";
            date2 = DateTime.Today.AddDays(2).Month.ToString() + "/" + DateTime.Today.AddDays(2).Day.ToString();
            str1 += "請於 " + date2 + " 23:00 前取票 !";
            MessageBox.Show(str1);
        }
    }
}
