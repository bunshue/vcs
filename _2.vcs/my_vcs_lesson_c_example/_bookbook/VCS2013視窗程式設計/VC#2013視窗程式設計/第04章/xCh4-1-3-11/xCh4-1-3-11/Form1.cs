using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_3_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            label2.Text = "目前的寵物數量是：" + numericUpDown1.Value;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            numericUpDown1.UpButton();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            numericUpDown1.DownButton();
        }
    }
}
