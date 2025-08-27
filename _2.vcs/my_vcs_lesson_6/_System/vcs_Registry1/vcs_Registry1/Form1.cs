using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Registry1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Load saved values.
            RegistryTools.LoadAllSettings(Application.ProductName, this);

            label1.Text = hScrollBar1.Value.ToString();
            if (textBox1.Text == "")
            {
                textBox1.Text = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            }
            label1.Text = hScrollBar1.Value.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Load saved values.
            RegistryTools.LoadAllSettings(Application.ProductName, this);

            if (textBox1.Text == "")
            {
                textBox1.Text = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            }
            label1.Text = hScrollBar1.Value.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // Save
            RegistryTools.SaveAllSettings(Application.ProductName, this);
        }

        private void hScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            label1.Text = hScrollBar1.Value.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = openFileDialog1.FileName;
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Save
            RegistryTools.SaveAllSettings(Application.ProductName, this);
        }
    }
}
