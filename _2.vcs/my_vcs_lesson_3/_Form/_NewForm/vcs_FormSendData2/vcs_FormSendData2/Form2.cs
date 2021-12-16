using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData2
{
    public partial class Form2 : Form
    {
        string data_from_form1 = string.Empty;

        public Form2(string data1)
        {
            InitializeComponent();
            data_from_form1 = data1;
            textBox1.Text = data1;
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
