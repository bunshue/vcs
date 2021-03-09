using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


//方案總管/右鍵/加入/新增項目/類別/預設Class1.cs改成Person.cs

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Person p1 = new Person();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Default firstname = " + p1.FirstName + "\n";
            //讀FirstName
            p1.FirstName = "FN"; //寫firstname
            richTextBox1.Text += "set new firstname = " + p1.FirstName + "\n";
            //p1.LastName ="LN";
            //由於LastName不可寫，因此此行會顯示readonly無法編譯
            richTextBox1.Text += "Default lastname = " + p1.LastName + "\n";
            p1.Age = 5;
            richTextBox1.Text += "condition change Age = " + p1.Age + "\n";
            p1.Age = 20;
            richTextBox1.Text += "condition change Age =" + p1.Age + "\n";
            richTextBox1.Text += "Default sex =" + p1.Sex + "\n";
            p1.Sex = "male";
            richTextBox1.Text += "set new sex =" + p1.Sex + "\n";
            //p1.ADDR = "123"; ADDR不可寫，因此此行會顯示readonly無法編譯



        }

        private void button2_Click(object sender, EventArgs e)
        {
            //Person p1 = new Person();
        }



        private void button4_Click(object sender, EventArgs e)
        {

        }


    }
}
