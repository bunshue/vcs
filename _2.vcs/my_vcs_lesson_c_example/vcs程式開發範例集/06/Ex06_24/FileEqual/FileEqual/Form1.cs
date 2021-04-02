using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.IO;

namespace FileEqual
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.ShowDialog();
            textBox1.Text = openFileDialog1.FileName;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.ShowDialog();
            textBox2.Text = openFileDialog1.FileName;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            StreamReader sr1 = new StreamReader(textBox1.Text);
            StreamReader sr2 = new StreamReader(textBox2.Text);
            if (object.Equals(sr1.ReadToEnd(),sr2.ReadToEnd()))
            {
                MessageBox.Show("兩個文件相等");
            }
            else
            {
                MessageBox.Show("兩個文件不相等");
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}