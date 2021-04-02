using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace PrimeNumber
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int j;
            j=(int)Math.Ceiling( Math.Sqrt(Convert.ToDouble(textBox1.Text)));
            for (int i = 1; i < j; i++)
            {
                if (Math.IEEERemainder(Convert.ToDouble(textBox1.Text), i) == 0)
                {
                    label2.Text = "不是素數";
                }
                else
                {
                    label2.Text = "是素數";
                }
            }
        }
    }
}