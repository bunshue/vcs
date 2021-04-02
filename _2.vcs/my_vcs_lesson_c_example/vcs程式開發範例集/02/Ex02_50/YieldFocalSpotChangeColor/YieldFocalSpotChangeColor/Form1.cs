using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace YieldFocalSpotChangeColor
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_Enter(object sender, EventArgs e)
        {
            textBox1.BackColor = Color.Beige;
          
        }

        private void textBox1_Leave(object sender, EventArgs e)
        {
            textBox1.BackColor = Color.White;
        }

        private void textBox2_Leave(object sender, EventArgs e)
        {
            
            textBox2.BackColor = Color.White;
        }

        private void textBox2_Enter(object sender, EventArgs e)
        {
            textBox2.BackColor = Color.Beige;
          
        }

        private void textBox3_Enter(object sender, EventArgs e)
        {
            textBox3.BackColor = Color.Beige;
           

        }

        private void textBox4_Leave(object sender, EventArgs e)
        {
            
            textBox4.BackColor = Color.White;
        }

        private void textBox4_Enter(object sender, EventArgs e)
        {
            textBox4.BackColor = Color.Beige;
        

        }

        private void textBox3_Leave(object sender, EventArgs e)
        {
            textBox3.BackColor = Color.White;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

      

      
}
}
