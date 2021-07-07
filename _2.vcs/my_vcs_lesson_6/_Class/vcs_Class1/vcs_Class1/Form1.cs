using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//方案總管/右鍵/加入/新增項目/類別/預設Class1.cs改成Person.cs

namespace vcs_Class1
{
    public partial class Form1 : Form
    {
        //建立 Animal 類別
        public class Animal
        {
            public string recorder;
            public int number;
            public string name;
            public string type;
            //A class被實例化時，會立即執行建構子內容，並且可以傳入參數
            public string Show
            {
                // 可以透過 get 存取子，將字串進行判斷、處理.... 再返回結果
                get { return name; }

                // set含有特殊的keyword: value, 當有值傳入時，都會存入value中
                set
                {
                    name = type;
                    recorder = value;
                    //Console.WriteLine("I am " + value);
                }
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "empty\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //實例化A類別
            Animal people = new Animal();

            people.type = "zzz";
            people.name = "Brown";
            people.Show = "Joe";
            richTextBox1.Text += people.Show + "\n";

            richTextBox1.Text += "ttt = " + people.recorder + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Person p1 = new Person();

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

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "empty\n";
        }
    }
}
