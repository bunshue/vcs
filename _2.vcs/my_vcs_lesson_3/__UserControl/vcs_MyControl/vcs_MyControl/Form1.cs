using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyControl
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            myControl1.MinValue = 0;
            myControl1.MaxValue = 59;
            myControl1.Value = 0;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            int ss = DateTime.Now.Second;
            myControl1.Value = ss;
        }
    }
}
