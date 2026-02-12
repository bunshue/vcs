using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace SQLServerDistill
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        public Form2(string strname)
        {
            InitializeComponent();
            this.Text = strname + "±í½á¹¹";
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }
    }
}