using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Class3
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
            int y = 2006;
            int m = 3;
            int d = 11;

            Date date = new Date();
            date.setDate(d, m, y);

            //the same
            //Date date = new Date(d, m, y);

            richTextBox1.Text += date.show() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string name = "david";
            int age = 18;

            char gender = '男';

            int y = 2002;
            int m = 3;
            int d = 11;

            Date date = new Date(d, m, y);

            Person p = new Person(name, age, gender, date);

            richTextBox1.Text += p.show() + "\n";
            richTextBox1.Text += "共有" + Person.counter() + "人\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Circle物件
            Circle c1 = new Circle(2);

            richTextBox1.Text += "圓c1的半徑 = " + c1.getRadius() + "\t" + "圓c1的面積 = " + c1.getArea() + "\n";


            //Cylinder物件
            Cylinder cy1 = new Cylinder(5, 10);

            richTextBox1.Text += "圓柱體cy1的半徑 = " + cy1.getRadius() + "\t" + "圓柱體cy1的高度 = " + cy1.getLength() + "\t" + "圓柱體cy1的表面積 = " + cy1.getArea() + "\n";


        }

        private void button4_Click(object sender, EventArgs e)
        {
            string name = "david";
            int age = 18;

            char gender = '男';

            int y = 2003;
            int m = 3;
            int d = 11;

            Date date = new Date(d, m, y);

            int c = 95;
            int ma = 87;

            Student s = new Student(name, age, gender, date, c, ma);

            richTextBox1.Text += s.show() + "\n";

            String str = "共" + Person.counter() + "人, 學生: " + Student.counter() + "人\r\n";

            richTextBox1.Text += str + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string name = "john";
            int age = 30;

            char gender = '男';

            int y = 1995;
            int m = 5;
            int d = 20;

            Date date = new Date(d, m, y);

            string r = "senior";

            Teacher t = new Teacher(name, age, gender, date, r);

            String str = "共" + Person.counter() + "人, 學生: " +
                            Student.counter() + "人, 老師: " +
                            Teacher.counter() + "人\r\n";

            richTextBox1.Text += str + "\n";
            richTextBox1.Text += t.show() + "\n";
        }
    }
}
