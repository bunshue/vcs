using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Tax
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 按 [確定] 鈕執行
        private void btnOK_Click(object sender, EventArgs e)
        {
            try //使用例外處理敘述來處理資料型別轉換失敗的問題
            {
                double income, tax, taxRate;
                income = Convert.ToDouble(txtIncome.Text);
                taxRate = (income < 100 ? 0.15 : (income < 300 ? 0.2 : 0.4));
                lblTaxRate.Text = Convert.ToString(taxRate * 100) + "%";
                tax = income * taxRate * 10000;
                lblTax.Text = Convert.ToString(tax) + "元";
            }
            catch
            {
                MessageBox.Show("請輸入數值...");
            }
        }
    }
}
