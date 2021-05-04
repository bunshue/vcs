using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Off
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            int buy = Convert.ToInt32(txtBuy.Text);//取得消費金額
            int pay = buy;   //實付金額等於消費金額
            if (buy > 1000)    //若消費金額>千元
            {
                //實付金額等於1000元加上超過千元部分打九折
                pay = 1000 + Convert.ToInt32((buy - 1000) * 0.9);
            }
            lblPay.Text = "實付金額：" + pay.ToString("C0") + "元";
        }
    }
}
