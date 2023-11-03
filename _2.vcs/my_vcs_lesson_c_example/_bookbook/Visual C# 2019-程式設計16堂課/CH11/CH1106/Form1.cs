using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1106
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        int total = 0;
        private void btnTotal_Click(object sender, EventArgs e)
        {
            //被勾選者就把金額加到total變數
            if (chkGreenTea.Checked)
                total = 35;
            if (chkBlackTea.Checked)
                total += 30;
            if (chkMilkTea.Checked)
                total += 45;
            if (chkYeast.Checked)
                total += 42;
            if (chkLemonTea.Checked)
                total += 55;
            if (chkPlumTea.Checked)
                total += 40;
            lblShow.Text = $"{total:c0}";
        }
    }
}
