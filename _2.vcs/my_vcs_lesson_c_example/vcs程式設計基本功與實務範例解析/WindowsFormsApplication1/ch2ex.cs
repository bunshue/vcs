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
    public partial class ch2ex : Form
    {
        public ch2ex()
        {
            InitializeComponent();
        }

        private void btnDisplay_Click(object sender, EventArgs e)
        {
            lblOutput.Text = txtInput.Text;
        }

        private void btnYellowBackColor_Click(object sender, EventArgs e)
        {
            lblOutput.BackColor = Color.Yellow;
        }

        private void btnRedForeColor_Click(object sender, EventArgs e)
        {
            lblOutput.ForeColor = Color.Red;
        }

        private void btnRestore_Click(object sender, EventArgs e)
        {
            lblOutput.BackColor = Color.Pink;
            lblOutput.ForeColor = Color.Blue;
        }

                
    }
}
