using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace AccrueResemble
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            for (int i = 1900; i <= 2050; i++)
            {
                comboBox1.Items.Add(i);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int x = Convert.ToInt32(comboBox1.Text) % 12;
            switch(x)
            {
                case 4:
                    radioButton1.Checked = true;
                    break;
                case 5:
                    radioButton2.Checked = true;
                    break;
                case 6:
                    radioButton3.Checked = true;
                    break;
                case 7:
                    radioButton4.Checked = true;
                    break;
                case 8:
                    radioButton5.Checked = true;
                    break;
                case 9:
                    radioButton6.Checked = true;
                    break;
                case 10:
                    radioButton7.Checked = true;
                    break;
                case 11:
                    radioButton8.Checked = true;
                    break;
                case 0:
                    radioButton9.Checked = true;
                    break;
                case 1:
                    radioButton10.Checked = true;
                    break;
                case 2:
                    radioButton11.Checked = true;
                    break;
                case 3:
                    radioButton12.Checked = true;
                    break;
            }
        }
    }
}