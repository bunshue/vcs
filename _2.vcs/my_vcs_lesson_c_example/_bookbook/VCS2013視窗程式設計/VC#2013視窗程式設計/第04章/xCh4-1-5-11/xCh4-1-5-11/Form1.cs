using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_5_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            label1.Text = dateTimePicker1.Value.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = dateTimePicker1.Value.ToShortDateString();
        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            MessageBox.Show("Value屬性變更 ！");
        }
    }
}


