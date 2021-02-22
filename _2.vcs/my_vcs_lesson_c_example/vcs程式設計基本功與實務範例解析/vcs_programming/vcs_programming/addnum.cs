using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class addnum : Form
    {
        public addnum()
        {
            InitializeComponent();
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            int start = Convert.ToInt32(txtStart.Text);
            int end = Convert.ToInt32(txtEnd.Text);
            int sum = 0;

            for (int i = start; i <= end; i++)
                sum += i;

            lblResult.Text = start + "¥[¨ì" + end + " = " + sum;
        }
    }
}