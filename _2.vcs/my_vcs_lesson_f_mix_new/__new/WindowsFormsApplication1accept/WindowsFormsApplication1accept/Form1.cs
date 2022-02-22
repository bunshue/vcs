using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1accept
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            label1.Text = "";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.AcceptButton = button1;
            this.CancelButton = button2;

            this.ShowInTaskbar = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = "你按了 Accept";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text = "你按了Cancel";
        }

    }
}
