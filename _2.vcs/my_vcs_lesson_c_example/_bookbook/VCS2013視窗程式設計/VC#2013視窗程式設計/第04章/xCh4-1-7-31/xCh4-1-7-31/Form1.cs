using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace xCh4_1_7_31
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            radioButton1.Checked = true;
            textBox1.Text = File.ReadAllText(@"C:\鹿柴.txt");
        }

        private void xCheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked)
                textBox1.Text = File.ReadAllText(@"C:\鹿柴.txt");
            else if (radioButton2.Checked)
                textBox1.Text = File.ReadAllText(@"C:\春曉.txt");
            else
                textBox1.Text = File.ReadAllText(@"C:\夜思.txt");
        }
    }
}
