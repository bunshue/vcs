using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_21_ListBox3
{
    public partial class Form1 : Form
    {
        string[] animal_array = { "ape", "bear", "cat", "dolphin", "eagle", "fox", "giraffe" };
        List<string> animal_list;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            animal_list = new List<string>(animal_array);


        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.DataSource = animal_array;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            listBox1.DataSource = animal_list;

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }
    }
}
