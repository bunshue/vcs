using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using WMPLib;

namespace LeadWindows
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            axAnimation1.Open("Electron.avi");
            axAnimation2.Open("zybiao.avi");
            axAnimation3.Open("gd.avi");
        }

    }
}