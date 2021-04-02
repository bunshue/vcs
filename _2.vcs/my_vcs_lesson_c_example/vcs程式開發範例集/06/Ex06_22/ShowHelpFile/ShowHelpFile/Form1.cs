using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace ShowHelpFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Help.ShowHelp(this,"help.hlp");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}