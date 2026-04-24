using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ErrorProvider2
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

        private void textBox1_Validating(object sender, CancelEventArgs e)
        {
            try
            {
                int x = Int32.Parse(textBox1.Text);

                if (x < 60 && x > 20)
                {
                    errorProvider4.SetError(this.textBox1, "AAAA");
                }
                else
                {
                    errorProvider4.SetError(this.textBox1, "數值應在20-60之間");
                }
            }
            catch
            {
                errorProvider4.SetError(this.textBox1, "應為整數");
            }

        }
    }
}
