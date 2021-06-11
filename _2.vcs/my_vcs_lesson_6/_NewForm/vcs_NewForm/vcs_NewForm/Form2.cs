using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NewForm
{
    public partial class Form2 : Form
    {
        public string mInput
        {
            get { return richTextBox1.Text; }
        }

        public string getInput()
        {
            return richTextBox1.Text;
        }

        public Form2()
        {
            InitializeComponent();
        }
    }
}
