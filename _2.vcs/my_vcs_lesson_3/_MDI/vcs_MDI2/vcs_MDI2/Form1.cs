using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MDI2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.IsMdiContainer = true;
            this.Text = "父表單";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //建立Form2子表單物件ChildForm
            Form2 ChildForm = new Form2();
            //將ChildForm變成這個MDI表單的子表單，接著才顯示
            ChildForm.MdiParent = this;
            ChildForm.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form3 ChildForm = new Form3();
            ChildForm.MdiParent = this;
            ChildForm.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Form4 ChildForm = new Form4();
            ChildForm.MdiParent = this;
            ChildForm.Show();
        }
    }
}

