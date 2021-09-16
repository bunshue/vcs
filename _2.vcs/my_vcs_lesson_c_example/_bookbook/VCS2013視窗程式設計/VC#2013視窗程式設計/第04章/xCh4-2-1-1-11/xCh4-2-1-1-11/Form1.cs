using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_2_1_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            MessageBox.Show(linkLabel1.LinkArea.IsEmpty.ToString());
        }

        private void button1_Click(object sender, EventArgs e)
        {
            linkLabel1.LinkArea = new LinkArea(0, 0);
            MessageBox.Show(linkLabel1.LinkArea.IsEmpty.ToString());
        }
    }
}


