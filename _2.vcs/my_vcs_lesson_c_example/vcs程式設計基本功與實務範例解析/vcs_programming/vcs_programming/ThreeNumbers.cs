using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class ThreeNumbers : Form
    {
        public ThreeNumbers()
        {
            InitializeComponent();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            DialogResult result;

            result = MessageBox.Show("確定結束程式嗎?",
                "詢問", MessageBoxButtons.YesNo,
                MessageBoxIcon.Question);

            if (result == DialogResult.Yes)
            {
                Close();
            }
        }

        private void btnMax_Click(object sender, EventArgs e)
        {
            int num1 = Convert.ToInt32(txtNum1.Text);
            int num2 = Convert.ToInt32(txtNum2.Text);
            int num3 = Convert.ToInt32(txtNum3.Text);

            int max = num1;
            if (num2 > max) max = num2;
            if (num3 > max) max = num3;

            MessageBox.Show("最大值是" + max, "三數比較",
                            MessageBoxButtons.OK,
                            MessageBoxIcon.Information);
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            txtNum1.Text = "";
            txtNum2.Text = "";
            txtNum3.Text = "";
        }

        private void btnMin_Click(object sender, EventArgs e)
        {
            int num1 = Convert.ToInt32(txtNum1.Text);
            int num2 = Convert.ToInt32(txtNum2.Text);
            int num3 = Convert.ToInt32(txtNum3.Text);
           
            int min = num1;
            if (num2 < min) min = num2;
            if (num3 < min) min = num3;

            MessageBox.Show("最小值是" + min, "三數比較",
                            MessageBoxButtons.OK,
                            MessageBoxIcon.Information);
        }

                
    }
}
