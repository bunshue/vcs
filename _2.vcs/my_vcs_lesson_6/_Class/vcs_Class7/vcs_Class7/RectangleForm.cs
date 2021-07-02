using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Class7
{
    public partial class RectangleForm : Form
    {
        public RectangleForm()
        {
            InitializeComponent();
        }

        internal Rectangle rObj;

        private void btnOK_Click(object sender, EventArgs e)
        {
            double width = Convert.ToDouble(txtWidth.Text);
            double height = Convert.ToDouble(txtHeight.Text);

            rObj = new Rectangle(width, height);
        }

        private void RectangleForm_Load(object sender, EventArgs e)
        {

        }
    }
}
