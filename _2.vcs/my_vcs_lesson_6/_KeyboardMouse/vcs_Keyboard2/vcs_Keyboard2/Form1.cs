using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_Keyboard2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lbl_0.Click += new EventHandler(lbl_Click);
            lbl_1.Click += new EventHandler(lbl_Click);
            lbl_2.Click += new EventHandler(lbl_Click);
            lbl_3.Click += new EventHandler(lbl_Click);
            lbl_4.Click += new EventHandler(lbl_Click);
            lbl_5.Click += new EventHandler(lbl_Click);
            lbl_6.Click += new EventHandler(lbl_Click);
            lbl_7.Click += new EventHandler(lbl_Click);
            lbl_8.Click += new EventHandler(lbl_Click);
            lbl_9.Click += new EventHandler(lbl_Click);
            lbl_Q.Click += new EventHandler(lbl_Click);
            lbl_W.Click += new EventHandler(lbl_Click);
            lbl_R.Click += new EventHandler(lbl_Click);
            lbl_E.Click += new EventHandler(lbl_Click);
            lbl_T.Click += new EventHandler(lbl_Click);
            lbl_Y.Click += new EventHandler(lbl_Click);
            lbl_U.Click += new EventHandler(lbl_Click);
            lbl_I.Click += new EventHandler(lbl_Click);
            lbl_O.Click += new EventHandler(lbl_Click);
            lbl_P.Click += new EventHandler(lbl_Click);
            lbl_A.Click += new EventHandler(lbl_Click);
            lbl_S.Click += new EventHandler(lbl_Click);
            lbl_D.Click += new EventHandler(lbl_Click);
            lbl_F.Click += new EventHandler(lbl_Click);
            lbl_G.Click += new EventHandler(lbl_Click);
            lbl_H.Click += new EventHandler(lbl_Click);
            lbl_J.Click += new EventHandler(lbl_Click);
            lbl_K.Click += new EventHandler(lbl_Click);
            lbl_L.Click += new EventHandler(lbl_Click);
            lbl_Z.Click += new EventHandler(lbl_Click);
            lbl_X.Click += new EventHandler(lbl_Click);
            lbl_C.Click += new EventHandler(lbl_Click);
            lbl_V.Click += new EventHandler(lbl_Click);
            lbl_B.Click += new EventHandler(lbl_Click);
            lbl_N.Click += new EventHandler(lbl_Click);
            lbl_M.Click += new EventHandler(lbl_Click);
            label44.Click += new EventHandler(label44_Click);
        }

        void label44_Click(object sender, EventArgs e)
        {
            Label l = (Label)sender;
            textBox1.Text = textBox1.Text.Substring(0, textBox1.Text.Length - 1);
            textBox1.SelectionStart = textBox1.Text.Length;
        }

        void lbl_Click(object sender, EventArgs e)
        {
            Label l = (Label)sender;
            textBox1.Text += l.Name.Substring(4, 1);
            textBox1.SelectionStart = textBox1.Text.Length;
        }

        private void label1_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}

