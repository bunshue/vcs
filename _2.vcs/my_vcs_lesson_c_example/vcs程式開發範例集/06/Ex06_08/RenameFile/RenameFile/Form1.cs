using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.IO;

namespace RenameFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != textBox2.Text)
            {
                File.Move(textBox1.Text, textBox2.Text);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.ShowDialog();
            textBox1.Text = openFileDialog1.FileName;
            textBox2.Text = openFileDialog1.FileName;
        }
    }
}