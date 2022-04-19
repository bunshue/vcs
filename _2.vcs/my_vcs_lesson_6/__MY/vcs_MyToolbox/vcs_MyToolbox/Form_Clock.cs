using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyToolbox
{
    public partial class Form_Clock : Form
    {
        public Form_Clock()
        {
            InitializeComponent();
        }

        private void Form_Clock_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
        }
    }
}
