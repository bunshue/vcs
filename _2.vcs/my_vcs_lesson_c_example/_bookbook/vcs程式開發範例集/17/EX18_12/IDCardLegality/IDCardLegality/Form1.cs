using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace IDCardLegality
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length != 15 || textBox1.Text.Length != 18)
                label3.Text = "不合法";
            if (textBox1.Text.Length == 15)
            {
                if ((textBox1.Text.Substring(14, 1) == "1" && comboBox1.SelectedItem.ToString() == "男") || (textBox1.Text.Substring(14, 1) == "2" && comboBox1.SelectedItem.ToString() == "女"))
                {
                    label3.Text = "合法";
                }
                else
                {
                    label3.Text = "不合法";
                }
            }
            if (textBox1.Text.Length == 18)
            {
                if ((textBox1.Text.Substring(16, 1) == "1" && comboBox1.SelectedItem.ToString() == "男") || (textBox1.Text.Substring(16, 1) == "2" && comboBox1.SelectedItem.ToString() == "女") || (textBox1.Text.Substring(16, 1) == "4" && comboBox1.SelectedItem.ToString() == "女"))
                {
                    label3.Text = "合法";
                }
                else
                {
                    label3.Text = "不合法";
                }
            }
        }
    }
}