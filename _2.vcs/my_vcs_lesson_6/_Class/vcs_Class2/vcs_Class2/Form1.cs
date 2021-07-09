using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Class2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;

            Person[] people = new Person[3];
            people[0] = new Person("Jethro", "Tull", this);
            people[1] = new Person("Pink", "Floyd", this);
            people[2] = new Person("Lynyrd", "Skynyrd", this);

            for (i = 0; i < 3; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + people[i].ToString() + "\n";
            }

            Person2[] people2 = 
            {
                new Person2() { FirstName="Simon", LastName="Green" },
                new Person2() { FirstName="Terry", LastName="Pratchett" },
                new Person2() { FirstName="Eowin", LastName="Colfer" },
            };
            for (i = 0; i < 3; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + people2[i].ToString() + "\n";
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            List<Product> Products = new List<Product>();
            // Load the data.
            // Cake slices.
            string[] cakes =
            {
                "Black Forest Cake",
                "Strawberry Chocolate Mousse Cake",
                "Chocolate Mousse Cake",
                "Carrot Cake",
                "Raspberry Mousse Cake",
                "Chestnut Cream Cake",
                "Strawberry Vanilla Cake",
                "Coconut Mango Cake",
                "Chocolate Ganache Cake",
                "German Chocolate Cake",
                "Tres Leches Cake",
                "Jiggly Cheesecake",
                "Tiramisu",
                "Matcha Tiramisu",
            };
            foreach (string cake in cakes)
            {
                Products.Add(new Product(cake, 5.49m));
            }

            int len = Products.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                //使用Override的ToString
                richTextBox1.Text += i.ToString() + "\t" + Products[i].ToString() + "\n";
            }
            for (i = 0; i < len; i++)
            {
                //使用Class內的參數
                richTextBox1.Text += i.ToString() + "\t" + Products[i].Name + "\t" + Products[i].Price.ToString("c") + "\n";
            }


        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "使用Person.cs裡面的class Person3, 看輸出畫面的log\n";

            // Create a Person.
            richTextBox1.Text += "建立\n";
            Person3 person = new Person3();



            richTextBox1.Text += "銷毀\n";
            // Force garbage collection.
            GC.Collect();
        }




    }


    // A simple Person class.
    public class Person
    {
        private Form1 MainForm;
        private string _FirstName;
        public string FirstName
        {
            get { return _FirstName; }
            set { _FirstName = value; }
        }

        public string LastName { get; set; }

        public Person(string firstName, string lastName, Form1 MainForm)
        {
            FirstName = firstName;
            LastName = lastName;
            this.MainForm = MainForm;
            MainForm.richTextBox1.Text += "Person初始化，從Class印出, FirstName = " + firstName + ", LastName = " + lastName + "\n";
        }

        public override string ToString()
        {
            return FirstName + " " + LastName;
        }
    }

    // A simple Person class.
    public class Person2
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }

        public override string ToString()
        {
            return FirstName + " " + LastName;
        }
    }

    public class Product
    {
        public string Name;
        public decimal Price;
        public Product(string name, decimal price)
        {
            Name = name;
            Price = price;
        }

        public override string ToString()
        {
            return "Product : " + Name + "\tPrice : " + Price.ToString("c");
        }
    }
}
