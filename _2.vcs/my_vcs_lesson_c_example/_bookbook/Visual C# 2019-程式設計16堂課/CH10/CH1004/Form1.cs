using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1004
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnCalc_Click(object sender, EventArgs e)
        {
            string name = txtName.Text;
            //將文字方塊取得的值轉為數值型別 - 學分數
            uint number = uint.Parse(txtGrade.Text);
            uint money = 7_350;   //每學分費用
            uint total = number * money;   //學分費總額
            lblShow.Text = $"{name}, \n你的學分費共{total:c0}";
        }
    }
}
