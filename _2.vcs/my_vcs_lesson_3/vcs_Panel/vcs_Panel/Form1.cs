using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Panel
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SetupRandonColor();
        }

        private void panel1_Click(object sender, EventArgs e)
        {
            SetupRandonColor();
        }

        private void SetupRandonColor()
        {
            var random = new Random();
            int rr;
            int gg;
            int bb;
            rr = random.Next(0, 256);
            gg = random.Next(0, 256);
            bb = random.Next(0, 256);

            panel1.BackColor = Color.FromArgb(rr, gg, bb);
            label1.Text = (rr).ToString() + " " + (gg).ToString() + " " + (bb).ToString();
        }

    }
}
