using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_01_Richtextbox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.BackColor = Color.Pink;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.BackColor = Color.FromName("Control");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            colorDialog1.AllowFullOpen = true;
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.SelectionBackColor = colorDialog1.Color;
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowApply = true;
            fontDialog1.ShowColor = true;
            fontDialog1.ShowEffects = true;
            fontDialog1.ShowHelp = true;
            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.SelectionFont = fontDialog1.Font;
                richTextBox1.SelectionColor = fontDialog1.Color;
                //richTextBox1.SelectionBackColor
            }

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        int value1 = 12345;
        double value2 = 123.456;
        double value3 = 1234.5678;

        private void button19_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("D");
        }

        private void button31_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("D8");
        }

        private void button30_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("X");
        }

        private void button28_Click(object sender, EventArgs e)
        {
            textBox1.Text = value1.ToString("X8");
        }

        private void button27_Click(object sender, EventArgs e)
        {
            textBox1.Text = value2.ToString("F4");
        }

        private void button26_Click(object sender, EventArgs e)
        {
            textBox1.Text = value3.ToString("#0.0");         //格式化，小數點後留1位
        }

        private void button25_Click(object sender, EventArgs e)
        {
            textBox1.Text = value3.ToString("#00000.000");   //格式化，小數點前5位，小數點後留3位四捨五入
        }

        //C# richTextBox 按ctrl+a全選
        private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A)
                ((RichTextBox)sender).SelectAll();

        }


    }
}
