using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_SendTo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int len = System.Environment.GetCommandLineArgs().Length;
            int i;
            richTextBox1.Text += "參數長度\t" + len.ToString() + "\t分別是:\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 項\t" + System.Environment.GetCommandLineArgs()[i] + "\n";
            }
        }
    }
}
