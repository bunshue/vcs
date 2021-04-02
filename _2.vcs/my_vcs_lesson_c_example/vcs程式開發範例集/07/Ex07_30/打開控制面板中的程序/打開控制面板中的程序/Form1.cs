using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 打開控制面板中的程序
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("main.cpl");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("desk.cpl");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("ncpa.cpl");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("mmsys.cpl");
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}