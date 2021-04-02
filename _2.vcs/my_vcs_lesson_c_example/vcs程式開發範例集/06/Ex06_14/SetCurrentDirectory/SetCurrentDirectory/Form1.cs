using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace SetCurrentDirectory
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            System.Environment.CurrentDirectory = textBox2.Text;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = System.Environment.CurrentDirectory;
        }
    }
}