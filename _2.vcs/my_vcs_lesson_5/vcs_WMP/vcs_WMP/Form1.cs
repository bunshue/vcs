using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_WMP
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int state = 0;

        private void button3_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                axWindowsMediaPlayer1.URL = openFileDialog1.FileName;
                axWindowsMediaPlayer1.Ctlcontrols.stop();
                state = 1;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if ((state == 1) || (state == 3))
            {
                axWindowsMediaPlayer1.Ctlcontrols.play();
                state = 2;
            }
            else if (state == 2)
            {
                axWindowsMediaPlayer1.Ctlcontrols.pause();
                state = 3;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (state > 0)
            {
                axWindowsMediaPlayer1.Ctlcontrols.stop();
                state = 1;
            }
        }
    }
}
