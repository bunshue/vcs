using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_09_Form
{
    public partial class Form2 : Form
    {
        // A variable that refers to the instance of Form2.
        // Note that it's public.
        public Form1 F1;

        public Form2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Switch to F1.
            this.Hide();
            F1.Show();
        }

        private void Form2_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Approach 1: Close the startup form.
            //F1.Close();

            // Approach 2: Hide this form instead of closing it.
            this.Hide();
            F1.Show();
            e.Cancel = true;
        }
    }
}
