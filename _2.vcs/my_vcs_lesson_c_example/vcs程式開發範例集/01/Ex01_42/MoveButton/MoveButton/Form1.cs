using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace MoveButton
{
    public partial class Form1 : Form
    {
        Form2 f;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Parent == this)
            {
                f.Controls.Add(this.button1);
                this.button1.Text = "返回原地";
            }
            else
            {
                this.Controls.Add(button1);
                this.button1.Text = "开始移动";
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            f = new Form2();
            f.Show();
        }
    }
}