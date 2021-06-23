using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MultiForm3
{
    public partial class frmCal : Form
    {
        public frmCal()
        {
            InitializeComponent();
        }

        //Cal 方法可計算配息方式
        public int Cal(int vMoney, int vYear, double vRate)
        {
            if (radYear.Checked)
            {
                richTextBox1.Text += "每年計息一次\n";
                //每年計息一次
                return (int)(vMoney * Math.Pow(1 + vRate, vYear));
            }
            else
            {
                richTextBox1.Text += "每月計息一次\n";
                //每月計息一次
                return (int)(vMoney * Math.Pow(1 + (vRate) / 12, vYear * 12));
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Dispose();
        }
    }
}
