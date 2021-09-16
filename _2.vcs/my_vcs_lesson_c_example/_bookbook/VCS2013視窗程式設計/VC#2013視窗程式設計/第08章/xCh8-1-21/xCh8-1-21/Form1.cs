using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;using System.Collections;

namespace xCh8_1_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Person[] peopleArray = new Person[3]
            {
                new Person("John", "Smith"),
                new Person("Jim", "Johnson"),
                new Person("Sue", "Rabon"),
            };

            BindingSource binding1 = new BindingSource();
            binding1.DataSource = peopleArray;

            listBox1.DataSource = binding1;
            listBox1.DisplayMember = "FirstName";
            listBox1.ValueMember = "LastName";
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex != -1)
                textBox1.Text = listBox1.SelectedValue.ToString();
        }
    }

    public class Person
    {
        private string firstName;
        private string lastName;
        public Person(string fName, string lName)
        {
            this.firstName = fName;
            this.lastName = lName;
        }

        public string FirstName
        {
            get
            {
                return firstName;
            }
        }

        public string LastName
        {
            get
            {
                return lastName;
            }
        }
    }

    public class People : IEnumerable
    {
        private Person[] _people;
        public People(Person[] pArray)
        {
            _people = new Person[pArray.Length];

            for (int i = 0; i < pArray.Length; i++)
            {
                _people[i] = pArray[i];
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return (IEnumerator)GetEnumerator();
        }

        public PeopleEnum GetEnumerator()
        {
            return new PeopleEnum(_people);
        }
    }

    public class PeopleEnum : IEnumerator
    {
        public Person[] _people;
        int position = -1;
        public PeopleEnum(Person[] list)
        {
            _people = list;
        }

        public bool MoveNext()
        {
            position++;
            return (position < _people.Length);
        }

        public void Reset()
        {
            position = -1;
        }

        object IEnumerator.Current
        {
            get
            {
                return Current;
            }
        }

        public Person Current
        {
            get
            {
                try
                {
                    return _people[position];
                }
                catch (IndexOutOfRangeException)
                {
                    throw new InvalidOperationException();
                }
            }
        }
    }
}
