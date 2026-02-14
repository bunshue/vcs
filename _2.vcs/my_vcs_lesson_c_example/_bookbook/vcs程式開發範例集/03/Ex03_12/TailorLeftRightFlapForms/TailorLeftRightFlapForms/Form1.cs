using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace TailorLeftRightFlapForms
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //獲得當前屏幕的大小
            Rectangle rect = new Rectangle();
            rect = Screen.GetWorkingArea(this);


            if (this.Left != (rect.Width - this.Width))
            {
                this.Left++;
                this.Top += 1;

            }
            else
            {
                timer1.Enabled = false;
                timer2.Enabled = true;

            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            Rectangle rect = new Rectangle();
            rect = Screen.GetWorkingArea(this);
            if (this.Left == 0)
            {
                timer2.Enabled = false;
                timer1.Enabled = true;
            }
            else
            {
                this.Left--;
                this.Top -= 1;
            }
        }
    }
}
