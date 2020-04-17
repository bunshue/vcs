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
    public partial class InstanceVar : Form
    {
        public InstanceVar()
        {
            InitializeComponent();
        }

        int y = 0;

        private void button1_Click(object sender, EventArgs e)
        {
            y = y + 1;
            lblResult.Text = "y = " + y;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            y = y + 1;
            lblResult.Text = "y = " + y;
        }
    }
}
