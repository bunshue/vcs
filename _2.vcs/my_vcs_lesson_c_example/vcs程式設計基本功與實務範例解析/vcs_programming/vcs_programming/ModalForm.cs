using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class ModalForm : Form
    {
        public string mInput {
            get { return txtInput.Text; }
        }

        public string getInput()
        {
            return txtInput.Text;
        }

        public ModalForm()
        {
            InitializeComponent();
        }
    }
}
