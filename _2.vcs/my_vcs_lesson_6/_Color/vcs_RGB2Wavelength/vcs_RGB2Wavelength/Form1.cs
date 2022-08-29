using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RGB2Wavelength
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            double r = 255;
            double g = 0;
            double b = 0;

            double x = 0;
            double y = 0;
            double z = 0;

            x = (0.490 * r + 0.310 * g + 0.200 * b) / (0.667 * r + 1.132 * g + 1.200 * b);

            y = (0.117 * r + 0.812 * g + 0.010 * b) / (0.667 * r + 1.132 * g + 1.200 * b);

            z = (0.000 * r + 0.010 * g + 0.990 * b) / (0.667 * r + 1.132 * g + 1.200 * b);

            richTextBox1.Text += "x = " + x.ToString() + "\n";
            richTextBox1.Text += "y = " + y.ToString() + "\n";
            richTextBox1.Text += "z = " + z.ToString() + "\n";


        }
    }
}
