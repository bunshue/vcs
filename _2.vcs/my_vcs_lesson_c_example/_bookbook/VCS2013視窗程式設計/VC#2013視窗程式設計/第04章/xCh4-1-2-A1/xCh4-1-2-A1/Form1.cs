using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_2_A1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (richTextBox1.SelectedText != "控制項")
            {
                if (richTextBox1.Find("控制項", RichTextBoxFinds.WholeWord) == -1)
                {
                    MessageBox.Show("The text \"控制項\" was not found!");
                    return;
                }
            }
            richTextBox1.SelectionProtected = true;
        }

        private void richTextBox1_Protected(object sender, EventArgs e)
        {
            MessageBox.Show("喔.喔.，這些字是不能改的喔！");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (richTextBox1.SelectedText != "控制項")
            {
                if (richTextBox1.Find("控制項", RichTextBoxFinds.WholeWord) == -1)
                {
                    MessageBox.Show("The text \"控制項\" was not found!");
                    return;
                }
            }
            richTextBox1.SelectionProtected = false;
        }
    }
}
