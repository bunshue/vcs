using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 大家來找碴網路遊戲_client
{
    public partial class Form2 : Form
    {
        int a, b = 0;
        Form1 f1 = new Form1();
        public Form2()
        {
            InitializeComponent();
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            a++;
            label5.Text = a.ToString();
            if (a == 5)
            {
                f1.LOSE = "lose";
                MessageBox.Show("超過次數，你輸了");
            }
        }

        private void pictureBox8_Click(object sender, EventArgs e)
        {
            pictureBox3.Visible = true;
            pictureBox8.Image = imageList1.Images[1];
            b = b + 1;
            label4.Text = b.ToString();
            if (b == 3)
            {
                f1.WIN = "win";
                MessageBox.Show("恭喜你過關了");
                pictureBox2.Enabled = false;
            }
        }

        private void pictureBox7_Click(object sender, EventArgs e)
        {
            pictureBox4.Visible = true;
            pictureBox7.Image = imageList1.Images[0];
            b = b + 1;
            label4.Text = b.ToString();
            if (b == 3)
            {
                f1.WIN = "win";
                MessageBox.Show("恭喜你過關了");
                pictureBox2.Enabled = false;
            }
        }

        private void pictureBox6_Click(object sender, EventArgs e)
        {
            pictureBox3.Visible = true;
            pictureBox6.Image = imageList1.Images[2];
            b = b + 1;
            label4.Text = b.ToString();
            if (b == 3)
            {
                f1.WIN = "win";
                MessageBox.Show("恭喜你過關了");
                pictureBox2.Enabled = false;
            }
        }

    }
}
