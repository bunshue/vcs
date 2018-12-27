using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_20_AGauge
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int value = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            value += 13;
            if(value > 400)
                value=-100;
            aGauge1.Value = value;
        }
    }
}
