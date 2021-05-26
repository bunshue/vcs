using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using CallClass;
using System.Data;
using System.Data.SqlClient;

namespace CallClient
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (ComDLL com = new ComDLL())
            {
                if (com.insert(textBox1.Text, textBox2.Text, textBox3.Text, textBox4.Text))
                {
                    MessageBox.Show("执行成功");
                }
                else
                {
                    MessageBox.Show("执行失败");
                }
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
           
        }
    }
}