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

        private void button6_Click(object sender, EventArgs e)
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


        //Sale範例 ST
        class Sale
        {
            public Sale(string productName, DateTime saleDate, double salePrice)
            {
                this.ProductName = productName;
                this.SaleDate = saleDate;
                this.SalePrice = salePrice;
            }
            public string ProductName { get; set; } //貨品名稱
            public DateTime SaleDate { get; set; }  //銷售日期
            public double SalePrice { get; set; }   //銷售價格
        }

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

    }
}
