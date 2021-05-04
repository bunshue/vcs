using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Train
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            rdbKind1.Checked = true;    //預設選取自強號
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            double unit;    //紀錄每公里費率
            //用三元運算子求費率，若選自強號就=2.27,否則若選莒光號就=1.75,否則=1.46
            unit = rdbKind1.Checked == true ? 2.27 : (rdbKind2.Checked == true ? 1.75 : 1.46);
            int km = Convert.ToInt32(txtKm.Text);   //取輸入的公里數
            double money = unit * km;   //票價等於費率*公里數
            if (chkSpecial.Checked == true) money /= 2; //若勾選優待票，票價/2
            if (chkToBack.Checked == true) money *= 1.8; //若勾選去回票，票價 *1.8
            lblTotal.Text = "票價：" + money.ToString("F0") + "元";   //顯示票價
        }
    }
}
