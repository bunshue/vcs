using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_System6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Load the saved settings.
        private void Form1_Load(object sender, EventArgs e)
        {
            RegistryTools.LoadAllSettings(Application.ProductName, this);
        }

        // Save settings.
        private void Form1_FormClosing(object sender,
            FormClosingEventArgs e)
        {
            RegistryTools.SaveAllSettings(Application.ProductName, this);
        }
    }
}
