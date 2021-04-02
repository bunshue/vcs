using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace ProsessStatusBar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            while (toolStripProgressBar1.Value < toolStripProgressBar1.Maximum)
            {
                this.toolStripProgressBar1.PerformStep();
            }
        }

        private void 文件FToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }
    }
}