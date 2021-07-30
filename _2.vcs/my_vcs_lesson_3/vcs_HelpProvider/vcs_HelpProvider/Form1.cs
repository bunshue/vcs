using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
this.HelpButton = true;
this.MaximizeBox = false;
this.MinimizeBox = false;
*/

namespace vcs_HelpProvider
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string strpath = Application.StartupPath.Substring(0, Application.StartupPath.Substring(0, Application.StartupPath.LastIndexOf("\\")).LastIndexOf("\\"));
            strpath += @"\AMCap.chm";
            helpProvider1.HelpNamespace = strpath;

            richTextBox1.Text += "filename = " + strpath + "\n";

        }
    }
}
