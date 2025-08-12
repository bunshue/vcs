using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Extensions
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

        private void button1_Click(object sender, EventArgs e)
        {
            listView1.Items.Clear();

            //加入項目，不使用Extensions
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listView1.Items.Clear();

            //加入項目，使用Extensions
            string ss = "";
            for (int i = 0; i < 20; i++)
            {
                ss += "s";
                listView1.AddRow(ss, ss, ss, ss, ss);
            }
            listView1.AutoSizeColumns();
        }
    }
}
