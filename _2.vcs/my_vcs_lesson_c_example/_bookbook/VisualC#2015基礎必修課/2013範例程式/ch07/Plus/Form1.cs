using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Plus
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lblAns.Text = "0";      //預設答案為0
            nudPoint.Maximum = 2;   //設nudPoint的最大值 = 2
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            decimal n1 = nudNo1.Value;  //n1=nudNo1的Value值
            decimal n2 = nudNo2.Value;  //n2=nudNo2的Value值
            //根據nudPoint.Value來格式化顯示的數值
            lblAns.Text = (n1 + n2).ToString("F" + nudPoint.Value.ToString());
        }
        //nudPoint的Value值改變時
        private void nudPoint_ValueChanged(object sender, EventArgs e)
        {
            string p = nudPoint.Value.ToString();
            nudNo1.Value = Convert.ToDecimal((nudNo1.Value).ToString("F" + p));
            nudNo2.Value = Convert.ToDecimal((nudNo2.Value).ToString("F" + p));
            if (nudPoint.Value == 0)    //若nudPoint.Value = 0
            {   //設nudNo1和nudNo2的增減值為1
                nudNo1.Increment = 1; nudNo2.Increment = 1;
                //設nudNo1和nudNo2顯示到整數
                nudNo1.DecimalPlaces = 0; nudNo2.DecimalPlaces = 0;
            }
            else if (nudPoint.Value == 1)
            {   //設nudNo1和nudNo2的增減值為0.1
                nudNo1.Increment = 0.1M; nudNo2.Increment = 0.1M;
                //設nudNo1和nudNo2顯示到小數一位
                nudNo1.DecimalPlaces = 1; nudNo2.DecimalPlaces = 1;
            }
            else
            {   //設nudNo1和nudNo2的增減值為0.01
                nudNo1.Increment = 0.01M; nudNo2.Increment = 0.01M;
                //設nudNo1和nudNo2顯示到小數二位
                nudNo1.DecimalPlaces = 2; nudNo2.DecimalPlaces = 2;
            }
        }
    }
}
