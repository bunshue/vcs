using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormMoveButton
{
    public partial class Form1 : Form
    {
        Form2 f2;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            f2 = new Form2();
            f2.Show();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Parent == this)
            {
                f2.Controls.Add(this.button1);
                this.button1.Text = "按鈕跳回上一個表單";
            }
            else
            {
                this.Controls.Add(button1);
                this.button1.Text = "按鈕移至下一個表單";
            }
        }
    }
}
