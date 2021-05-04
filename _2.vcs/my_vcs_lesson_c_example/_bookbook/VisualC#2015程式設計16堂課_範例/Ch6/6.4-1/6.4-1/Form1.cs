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
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int integer1 = Convert.ToInt32(integerText1.Text);
            int integer2 = Convert.ToInt32(integerText2.Text);
          
            for(int remainder = integer1 % integer2; remainder != 0;){              
                integer1 = integer2;
                integer2 = remainder;
                remainder = integer1 % integer2;
            }

            int gcd = integer2;
            gcdText.Text = gcd.ToString();
            int lcm = Convert.ToInt32(integerText1.Text) * Convert.ToInt32(integerText2.Text) / gcd;
            lcmText.Text = lcm.ToString();

        }
    }
}