using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace KeyPress2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = "Visual C#";
            textBox4.Text = "Visual C#";
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            byte asc = Convert.ToByte(e.KeyChar);
            if (asc == 18) textBox1.ForeColor = Color.Red;
        }

        private void textBox2_KeyPress(object sender, KeyPressEventArgs e)
        {
            byte asc = Convert.ToByte(e.KeyChar);
            if (asc < 48 || asc > 57) e.Handled = true;  //不接受字元
        }

        private void textBox3_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar < 'a' || e.KeyChar > 'z') e.Handled = true;  //不接受字元
        }

        private void textBox4_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (char)Keys.Enter)
            {
                e.Handled = true; textBox4.Clear();  //清除文字方塊中的文字
            }
        }
    }
}
