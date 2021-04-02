using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace DrawTool
{
    public partial class text : Form
    {
        public text()
        {
            InitializeComponent();
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            //當輸入Enter時，關閉模式對話視窗
            if (e.KeyChar == (char)13)
            {
                this.DialogResult = DialogResult.OK;
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}