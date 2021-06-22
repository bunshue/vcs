using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using vcs_Class6XXX;    //Class1之namespace不一樣, 要引用

namespace vcs_Class6
{
    public partial class Form1 : Form
    {
        my_stack stack;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "init 20 stacks\n";
            stack = new my_stack(20);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //push
            stack.Push(1);
            stack.Push(3);
            stack.Push(5);
            stack.Push(7);
            stack.Push(9);
            stack.Push(11);
            richTextBox1.Text += "push 1 3 5 7 9 11\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //pop
            int pop = stack.Pop();
            richTextBox1.Text += "pop " + pop.ToString() + "\n";
        }
    }
}
