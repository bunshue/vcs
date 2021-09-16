using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_7_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            foreach (Control x in Controls)
            {
                if (x.GetType().ToString() == "System.Windows.Forms.RadioButton")
                {
                    RadioButton myRadioButton = (System.Windows.Forms.RadioButton)x;
                    if (!myRadioButton.Checked)
                        myRadioButton.FlatStyle = FlatStyle.Standard;
                }
            }
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            if (this.radioButton1.Checked)
            {
                radioButton1.FlatStyle = FlatStyle.Flat;
                textBox1.Text = this.radioButton1.Text;
            }

            if (radioButton1.CheckAlign == ContentAlignment.MiddleLeft)
            {
                radioButton1.CheckAlign = ContentAlignment.MiddleRight;
            }
            else
            {
                radioButton1.CheckAlign = ContentAlignment.MiddleLeft;
            }
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            if (this.radioButton2.Checked)
            {
                radioButton2.FlatStyle = FlatStyle.Flat;
                textBox1.Text = this.radioButton2.Text;
            }

            if (radioButton2.CheckAlign == ContentAlignment.MiddleLeft)
            {
                radioButton2.CheckAlign = ContentAlignment.MiddleRight;
            }
            else
            {
                radioButton2.CheckAlign = ContentAlignment.MiddleLeft;
            }
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            if (this.radioButton3.Checked)
            {
                radioButton3.FlatStyle = FlatStyle.Flat;
                textBox1.Text = this.radioButton3.Text;
            }

            if (radioButton3.CheckAlign == ContentAlignment.MiddleLeft)
            {
                radioButton3.CheckAlign = ContentAlignment.MiddleRight;
            }
            else
            {
                radioButton3.CheckAlign = ContentAlignment.MiddleLeft;
            }
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {
            if (this.radioButton4.Checked)
            {
                radioButton4.FlatStyle = FlatStyle.Flat;
                textBox1.Text = this.radioButton4.Text;
            }

            if (radioButton4.CheckAlign == ContentAlignment.MiddleLeft)
            {
                radioButton4.CheckAlign = ContentAlignment.MiddleRight;
            }
            else
            {
                radioButton4.CheckAlign = ContentAlignment.MiddleLeft;
            }
        }

        private void radioButton5_CheckedChanged(object sender, EventArgs e)
        {
            if (this.radioButton5.Checked)
            {
                radioButton5.FlatStyle = FlatStyle.Flat;
                textBox1.Text = this.radioButton5.Text;
            }

            if (radioButton5.CheckAlign == ContentAlignment.MiddleLeft)
            {
                radioButton5.CheckAlign = ContentAlignment.MiddleRight;
            }
            else
            {
                radioButton5.CheckAlign = ContentAlignment.MiddleLeft;
            }
        }
    }
}
