using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_1_3_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (radioButton1.Checked)
                label2.Text = "答對了，您真厲害！";
            else
                label2.Text = "答案是coffee喔！！";
            panel2.Visible = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            panel2.Visible = false;
        }
    }
}
