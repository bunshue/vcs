using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_SplitContainer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            hScrollBar1.Value = 50;
            splitContainer1.SplitterDistance = (int)(splitContainer1.ClientSize.Width * 50 / 100);
        }

        private void hScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            int value = hScrollBar1.Value;
            richTextBox1.Text += value.ToString() + " ";
            if (value < 15)
            {
                splitContainer1.Panel1Collapsed = true;
                splitContainer1.Panel2Collapsed = false;
            }
            else if (value >85)
            {
                splitContainer1.Panel1Collapsed = false;
                splitContainer1.Panel2Collapsed = true;
            }
            else
            {
                splitContainer1.Panel1Collapsed = false;
                splitContainer1.Panel2Collapsed = false;
                splitContainer1.SplitterDistance = (int)(splitContainer1.ClientSize.Width * value / 100);


            }

        }

    }
}
