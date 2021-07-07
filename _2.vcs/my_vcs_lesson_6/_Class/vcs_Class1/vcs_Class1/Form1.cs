using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//方案總管/右鍵/加入/類別/預設Class1.cs改成Person.cs
//方案總管/右鍵/加入/類別/預設Class1.cs改成PersonData.cs
//方案總管/右鍵/加入/類別/預設Class1.cs改成Sale.cs
//方案總管/右鍵/加入/類別/預設Class1.cs改成Shape.cs

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


        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //Sale範例 ST
        List<Sale> SaleList = new List<Sale> { };    //銷售列表

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "重建一個銷售列表\n";

            SaleList = new List<Sale>
            {
                new Sale("洗衣機",Convert.ToDateTime("2010-3-3"),600),
                new Sale("冰箱",Convert.ToDateTime("2010-12-12"),1900),
                new Sale("洗衣機",Convert.ToDateTime("2010-2-2"),550),
                new Sale("洗衣機",Convert.ToDateTime("2010-1-1"),500)
            };

            richTextBox1.Text += "增加一個銷售物件\n";
            SaleList.Add(new Sale("洗衣機", Convert.ToDateTime("2010-3-3"), 600));


            richTextBox1.Text += "增加一個銷售物件\n";
            SaleList.Add(new Sale("洗衣機", Convert.ToDateTime("2010-3-3"), 600));

            richTextBox1.Text += "增加一個銷售物件\n";
            SaleList.Add(new Sale("洗衣機", Convert.ToDateTime("2010-3-3"), 523));

            int cnt = SaleList.Count;
            richTextBox1.Text += "目前共有銷售個數 : " + cnt.ToString() + " 個\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            int cnt = SaleList.Count;
            richTextBox1.Text += "目前共有銷售個數 : " + cnt.ToString() + " 個\n";
            if (cnt > 0)
            {
                richTextBox1.Text += "銷售列表\n";
                for (int i = 0; i < cnt; i++)
                {
                    richTextBox1.Text += SaleList[i].ProductName + "\t" + SaleList[i].SaleDate.ToString() + "\t" + SaleList[i].SalePrice.ToString() + "\n";
                }

                richTextBox1.Text += "查詢最後一次洗衣機的銷售價格\n";
                Sale sa = SaleList.Where(itm => itm.ProductName == "洗衣機").OrderBy(itm => itm.SaleDate).Last();
                richTextBox1.Text += "查詢結果：" + sa.SalePrice.ToString() + "\n";
            }
        }
        //Sale範例 SP

        private void button6_Click(object sender, EventArgs e)
        {
            //實例化Animal類別
            Animal people = new Animal();

            people.type = "zzz";
            people.name = "Brown";
            people.Show = "Joe";
            richTextBox1.Text += people.Show + "\n";

            richTextBox1.Text += "recorder = " + people.recorder + "\n";

        }

        private void button10_Click(object sender, EventArgs e)
        {
            Person2 p1 = new Person2();

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

        //PersonData範例 ST
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

        private void button4_Click(object sender, EventArgs e)
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
        //PersonData範例 SP

        //圖形範例 ST
        private void button12_Click(object sender, EventArgs e)
        {
            //Circle物件
            Circle c1 = new Circle(2);
            richTextBox1.Text += "圓c1的半徑 = " + c1.getRadius() + "\t" + "圓c1的面積 = " + c1.getArea() + "\n";


            //Cylinder物件
            Cylinder cy1 = new Cylinder(5, 10);
            richTextBox1.Text += "圓柱體cy1的半徑 = " + cy1.getRadius() + "\t" + "圓柱體cy1的高度 = " + cy1.getLength() + "\t" + "圓柱體cy1的表面積 = " + cy1.getArea() + "\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        //圖形範例 SP

        //MyTime範例 ST
        private void button14_Click(object sender, EventArgs e)
        {
            MyTime now = new MyTime();
            //now.Hour = 30;
            //now.Minute = 30;
            //now.Second = 30;

            // encapsulation
            now.setTime(12, 34, 56);

            richTextBox1.Text += now.getTime() + "\n";

            // property: get and set
            now.mHour = 7;
            now.mMinute = 8;
            now.mSecond = 9;

            richTextBox1.Text += "Hour = " + now.mHour + ", " + "Minute = " + now.mMinute + ", " + "Second = " + now.mSecond + "\n";

            // method overloading
            MyTime obj2 = new MyTime();
            obj2.setTime(21, 40);

            richTextBox1.Text += obj2.getTime() + "\n";

            // constructors
            MyTime t1 = new MyTime(9, 30, 50);
            MyTime t2 = new MyTime(21, 40);

            richTextBox1.Text += t1.getTime() + "\n";
            richTextBox1.Text += t2.getTime() + "\n";

            // 物件陣列

            MyTime[] tArray = new MyTime[3];
            tArray[0] = new MyTime();
            tArray[0].setTime(21, 40);
            tArray[1] = new MyTime(9, 30, 50);
            tArray[2] = new MyTime(10, 30, 30);

            for (int i = 0; i < 3; i++)
            {
                richTextBox1.Text += "物件" + i + " :\t" + tArray[i].getTime() + "\n";
            }

            //System.GC.Collect();


        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        //MyTime範例 SP



    }
}
