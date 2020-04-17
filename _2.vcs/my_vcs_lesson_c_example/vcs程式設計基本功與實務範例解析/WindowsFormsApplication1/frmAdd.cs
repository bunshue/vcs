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
    public partial class frmAdd : Form
    {
        public frmAdd()
        {
            InitializeComponent();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            int num1 = Convert.ToInt16(txtN1.Text);
            int num2 = Convert.ToInt16(txtN2.Text);
            int result = num1 + num2;
            lblResult.Text = num1 + " + " + num2 + " = " + result;
        }

        private void frmAdd_Load(object sender, EventArgs e)
        {

        }
    }
}
