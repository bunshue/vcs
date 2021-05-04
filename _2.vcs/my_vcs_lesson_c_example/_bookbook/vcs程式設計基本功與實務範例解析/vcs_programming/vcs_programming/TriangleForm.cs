using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class TriangleForm : Form
    {
        public TriangleForm()
        {
            InitializeComponent();
        }

        internal Triangle tObj;

        private void btnOK_Click(object sender, EventArgs e)
        {
            double tbase = Convert.ToDouble(txtBase.Text);
            double height = Convert.ToDouble(txtHeight.Text);

            tObj = new Triangle(tbase, height);
        }
    }
}
