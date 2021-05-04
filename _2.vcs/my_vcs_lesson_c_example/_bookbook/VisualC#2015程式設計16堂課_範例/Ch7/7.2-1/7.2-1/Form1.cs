using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void resultButton_Click(object sender, EventArgs e)
        {
            if (checkBox2.Checked && checkBox3.Checked && !checkBox1.Checked && !checkBox4.Checked)
                MessageBox.Show("複選題正確!", "正確", MessageBoxButtons.OK, MessageBoxIcon.Information);
            else
                MessageBox.Show("複選題錯誤! 正解為56和80", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);

            if (radioButton3.Checked)
                MessageBox.Show("單選題正確!", "正確", MessageBoxButtons.OK, MessageBoxIcon.Information);
            else
                MessageBox.Show("單選題錯誤! 正解為17", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }
}
