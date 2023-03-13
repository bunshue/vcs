using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ControlTest
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
            //this.Controls From中的所有元件控制權
            //foreach (Control child in this.Controls)表示每次從this.Controls中取一個元件的控制權
            foreach (Control child in this.Controls)
            {
                //取元件是Label的控制權
                if (child is Label)
                {
                    //做想做的事
                    child.BackColor = Color.SkyBlue;
                    child.Text = "^^";
                    //.................
                    //.................
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int temp = 7;
            foreach (Control child in this.Controls)
            {
                if (child is Label)
                {
                    if (child.Name == "label" + temp.ToString())
                    {
                        temp -= 2;
                        child.BackColor = Color.YellowGreen;
                        child.Text = "QQ";
                    }
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int temp = 0;
            foreach (Control child in this.Controls)
            {               
                if (child is Label)
                {
                    temp++;
                    child.BackColor = SystemColors.ActiveBorder;
                    child.Text = temp.ToString();
                }
            }
        }
    }
}
