using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using vcs_Class6XXX;    //Class1.cs之namespace不一樣, 要引用
using CatTest;          //Cat.cs之namespace不一樣, 要引用
using AnimalSpace;      //animal.cs cats.cs human.cs之namespace不一樣, 要引用

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

        private void button4_Click(object sender, EventArgs e)
        {
            Cat kitty = new Cat();
            kitty.name = "凱蒂";
            Cat doraemon = new Cat("多啦A夢", "機器貓");
            doraemon.setweight(129);
            Cat garfield = new Cat("加菲", "虎斑貓");
            garfield.setweight(5);

            kitty.print();
            doraemon.print();
            garfield.print();
            Console.WriteLine();

            garfield.feed();
            doraemon.play();
            Console.WriteLine();

            kitty.print();
            doraemon.print();
            garfield.print();

            Console.Read();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            Human myself = new Human("小李", "亞洲人", 64, 172);
            Cats mypet = new Cats("喵仔", "暹邏貓", 7, 30, 20);
            myself.setpet(mypet);

            myself.print();
            Console.WriteLine("類型為:" + myself.gettype());
            Console.WriteLine();

            Console.WriteLine("他的寵物是:");
            myself.getpet().print();
            mypet.print_length();

            Console.Read();

        }
    }
}
