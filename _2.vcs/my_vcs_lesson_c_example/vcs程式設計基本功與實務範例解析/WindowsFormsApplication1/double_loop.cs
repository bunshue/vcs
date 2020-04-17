using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class double_loop : Form
    {
        public double_loop()
        {
            InitializeComponent();
        }

        private void btnDigitRow_Click(object sender, EventArgs e)
        {
            int n = Convert.ToInt32(txtRows.Text);
            string res = "";

            for (int i = 1; i <= n; i++) //第i列
            {
                for (int j = 1; j <= i; j++)  //數字j
                    res += j;
                res += "\r\n";  //跳行
            }

            txtOutput.Text = res;
        }

        private void btn99_Click(object sender, EventArgs e)
        {
            string res = "";

            for (int i = 1; i <= 9; i++) // 外迴圈繞9次
            {
                for (int j = 1; j <= 9; j++) // 內迴圈繞9次
                    res += (i + "*" + j + "=" + (i*j) + "\t");
                res += "\r\n"; //跳行
            }

            txtOutput.Text = res;
        }
    }
}
