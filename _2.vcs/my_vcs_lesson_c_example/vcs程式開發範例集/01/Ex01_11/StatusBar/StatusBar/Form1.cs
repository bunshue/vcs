using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace StatusBar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void toolStripContainer1_TopToolStripPanel_Click(object sender, EventArgs e)
        {
           
        }

        private void toolStripContainer1_RightToolStripPanel_Click(object sender, EventArgs e)
        {

        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            if (this.checkBox2.Checked)
            {
                statusStrip1.Items[1].Text = "日期:" + DateTime.Now.ToString();
            }
            else
            {
                statusStrip1.Items[1].Text = "";
            }
        }
    }
}