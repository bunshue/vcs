using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyToolbox
{
    public partial class Form_Stopwatch : Form
    {
        DateTime start_time = DateTime.Now;

        public Form_Stopwatch()
        {
            InitializeComponent();
        }

        private void Form_Stopwatch_Load(object sender, EventArgs e)
        {

        }

        private void btn_start_Click(object sender, EventArgs e)
        {
            start_time = DateTime.Now;
            timer1.Enabled = true;

        }

        private void btn_clear_Click(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            string diff = (DateTime.Now - start_time).TotalSeconds.ToString("0.000") + " 秒";
            this.Text = diff;
        }
    }
}

