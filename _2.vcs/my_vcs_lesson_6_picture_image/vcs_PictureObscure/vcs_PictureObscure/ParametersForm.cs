using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureObscure
{
    public partial class ParametersForm : Form
    {
        public ParametersForm()
        {
            InitializeComponent();
        }

        private void trkKernelSize_Scroll(object sender, EventArgs e)
        {
            lblKernelSize.Text = KernelSize.ToString();
        }

        // Get or set the kernel size.
        public int KernelSize
        {
            get { return 2 * trkKernelSize.Value + 1; }
            set { trkKernelSize.Value = (value - 1) / 2; }
        }
    }
}
