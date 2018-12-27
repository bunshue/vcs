using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyClock
{
    public partial class Form1 : Form
    {
        int flash = 0;
        public Form1()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //this.digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
            if (flash == 0)
            {
                digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm");
                flash = 1;
            }
            else
            {
                digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH") + " " + DateTime.Now.ToString("mm");
                flash = 0;
            }
            digitalDisplayControl2.DigitText = DateTime.Now.ToString("yyyy");
            digitalDisplayControl3.DigitText = DateTime.Now.ToString("MM") + "/" + DateTime.Now.ToString("dd");
        }
    }
}
