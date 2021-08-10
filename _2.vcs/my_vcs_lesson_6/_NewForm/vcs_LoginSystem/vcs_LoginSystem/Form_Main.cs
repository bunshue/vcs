using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_LoginSystem
{
    public partial class Form_Main : Form
    {
        public Form_Main()
        {
            InitializeComponent();
        }

        private void Form_Main_FormClosed(object sender, FormClosedEventArgs e)
        {
            Application.Exit();
        }
    }
}