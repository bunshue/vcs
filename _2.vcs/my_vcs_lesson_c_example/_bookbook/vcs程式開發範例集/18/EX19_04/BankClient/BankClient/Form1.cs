using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.EnterpriseServices.CompensatingResourceManager;
using System.Windows.Forms;
using BankClass;
using BankClient;

namespace BankClient
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Transfer tt = new Transfer();
            bool bl = tt.BankTransfer(txtFromBank.Text, txtFromAccount.Text, txtToBank.Text, txtToAccount.Text, Single.Parse(txtBalance.Text));
            if (bl)
                MessageBox.Show("銀行轉賬成功！", "系統提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            else
                MessageBox.Show("銀行轉賬失敗！", "系統提示", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }
}