﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PicPick3
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Frm_Main_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Image img = new Bitmap(Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height);
            //richTextBox1.Text += "W = " + img.Width.ToString() + ", H = " + img.Height.ToString() + "\n";

            Graphics g = Graphics.FromImage(img);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), Screen.AllScreens[0].Bounds.Size);
            //IntPtr dc = g.GetHdc();
            //g.ReleaseHdc(dc);

            Frm_Browser frm2 = new Frm_Browser();
            frm2.ig = img;
            frm2.Show();
        }
    }
}
