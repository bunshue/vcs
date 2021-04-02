using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace HardlyEnableFigure
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
           
        }

        private void txtSum_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar != 8 && !char.IsDigit(e.KeyChar))&&e.KeyChar!=13)
            {
                MessageBox.Show("商品數量只能輸入數字", "操作提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                e.Handled = true;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}