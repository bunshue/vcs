using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.IO;

namespace CreateFolder
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (DialogResult.Yes == MessageBox.Show("是否要建立文件夾"+textBox1.Text.ToString(), "提示", MessageBoxButtons.YesNo))
            {

                Directory.CreateDirectory(textBox1.Text);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (DialogResult.Yes == MessageBox.Show("是否要刪除文件夾" + textBox1.Text.ToString(), "提示", MessageBoxButtons.YesNo))
            {
                Directory.Delete(textBox1.Text);
            }
        }
    }
}