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
            public int number;
            public string type;
            public string name;
            public string recorder;
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
            show_item_location();
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_item_location()
        {
            int w;
            int h;
            w = 150;
            h = 140;
            groupBox2.Size = new Size(w, h);
            groupBox3.Size = new Size(w, h);
            groupBox1.Size = new Size(w, h);
            groupBox5.Size = new Size(w, h);
            groupBox6.Size = new Size(w, h);
            groupBox8.Size = new Size(w, h);

            h = 250;
            groupBox4.Size = new Size(w, h);
            groupBox7.Size = new Size(w, h);

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 12;
            y_st = 12;
            dx = 180;
            dy = 150;

            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            groupBox5.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox8.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            groupBox7.Location = new Point(x_st + dx * 1, y_st + dy * 2);

            x_st = 20;
            y_st = 20;
            dx = 190;
            dy = 50;

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button7.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button14.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button19.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button16.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button17.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button18.Location = new Point(x_st + dx * 0, y_st + dy * 3);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //實例化Animal類別
            Animal dog1 = new Animal();

            dog1.number = 1;
            dog1.type = "Poodle";	//貴賓犬
            dog1.name = "Peter";
            dog1.Show = "ppp";
            richTextBox1.Text += dog1.Show + "\n";
            richTextBox1.Text += "recorder = " + dog1.recorder + "\n";

            Animal dog2 = new Animal();

            dog2.number = 2;
            dog2.type = "Maltese";	//馬爾濟斯
            dog2.name = "Mary";
            dog2.Show = "mmm";
            richTextBox1.Text += dog2.Show + "\n";
            richTextBox1.Text += "recorder = " + dog2.recorder + "\n";

            Animal dog3 = new Animal();

            dog3.number = 3;
            dog3.type = "Pomeranian";	//博美犬
            dog3.name = "Pluto";
            dog3.Show = "PPP";
            richTextBox1.Text += dog3.Show + "\n";
            richTextBox1.Text += "recorder = " + dog3.recorder + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        //Sale範例 ST
        List<Sale> SaleList = new List<Sale> { };    //銷售列表

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "重建一個銷售列表\n";

            SaleList = new List<Sale>
            {
                new Sale("洗衣機",Convert.ToDateTime("2010-3-3"),600),
                new Sale("電冰箱",Convert.ToDateTime("2010-12-12"),1900),
                new Sale("洗衣機",Convert.ToDateTime("2010-2-2"),550),
                new Sale("洗衣機",Convert.ToDateTime("2010-1-1"),500)
            };

            Sale refeg1 = new Sale();
            refeg1.ProductName = "電冰箱";
            refeg1.SaleDate = Convert.ToDateTime("2006-3-11");
            refeg1.SalePrice = 456;
            richTextBox1.Text += "增加一個銷售物件\t電冰箱\n";
            SaleList.Add(refeg1);

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

        private void button10_Click(object sender, EventArgs e)
        {
            Person2 p1 = new Person2();

            richTextBox1.Text += "僅宣告物件, 還沒給值, 讀FirstName, ";
            richTextBox1.Text += "firstname = " + p1.FirstName + "\n";

            p1.FirstName = "David";
            richTextBox1.Text += "寫firstname = " + p1.FirstName + "\n";

            //p1.LastName ="Wang";
            //由於LastName不可寫，因此此行會顯示readonly無法編譯
            richTextBox1.Text += "讀LastName, lastname = " + p1.LastName + "\n";
            p1.Age = 5;
            richTextBox1.Text += "讀Age, Age = " + p1.Age + "\n";
            p1.Age = 20;
            richTextBox1.Text += "讀Age, Age = " + p1.Age + "\n";

            richTextBox1.Text += "讀Sex, Sex = " + p1.Sex + "\n";

            p1.Sex = "male";
            richTextBox1.Text += "讀Sex, Sex = " + p1.Sex + "\n";
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
            richTextBox1.Text += "新增一個Circle物件, 給定參數2\n";
            Circle c1 = new Circle(2);
            richTextBox1.Text += "圓c1的半徑 = " + c1.getRadius() + "\t" + "圓c1的面積 = " + c1.getArea() + "\n";

            richTextBox1.Text += "新增一個Cylinder物件, 給定參數5, 10\n";
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


        //Student範例 ST
        private void button15_Click(object sender, EventArgs e)
        {
            //類別範例
            Student0 Jasper = new Student0();   //建立Jasper屬於Student類別的物件
            Jasper.Name = "賈思伯";             //設定Jasper物件的學生姓名
            Jasper.Score = 98;                  //設定Jasper物件的學生成績
            //Jasper.ShowMsg();                   //呼叫ShowMsg()方法顯示學生姓名和分數
            richTextBox1.Text += Jasper.GetMsg() + "\n";

            Student0 Anita = new Student0();
            Anita.Name = "愛妮達";
            Anita.Score = 85;
            //Anita.ShowMsg();
            richTextBox1.Text += Anita.GetMsg() + "\n";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //建構式範例

            //無參數的建構式
            StudentA Anita = new StudentA();
            Anita.Name = "愛妮達";
            Anita.Score = 88;
            richTextBox1.Text += Anita.GetMsg() + "\n";

            //傳一個參數的建構式
            StudentA Jasper = new StudentA("賈思伯");
            Jasper.Score = 77;
            richTextBox1.Text += Jasper.GetMsg() + "\n";

            //傳兩個參數的建構式
            StudentA Aliya = new StudentA("愛麗雅", 99);
            richTextBox1.Text += Aliya.GetMsg() + "\n";

            //呼叫StudentA類別的GetTotalStudent靜態方法取得目前有多少位學生
            richTextBox1.Text += StudentA.GetTotalStudent() + "\n";


        }

        private void button17_Click(object sender, EventArgs e)
        {
            //物件檢查參數
            //物件檢查參數
            //給錯誤參數, 讓系統自動訂正
            StudentA Jasper = new StudentA();
            Jasper.Name = "賈思伯";
            Jasper.Score = 5000;
            Jasper.ShowMsg();
            StudentA Anita = new StudentA();
            Anita.Name = "愛妮達";
            Anita.Score = -100;
            Anita.ShowMsg();

        }

        private void button18_Click(object sender, EventArgs e)
        {
            //使用靜態成員
            //使用靜態成員
            StudentA Aaita = new StudentA("愛妮達", 100);
            StudentA Jasper = new StudentA("賈思伯", 56);
            StudentA Aliya = new StudentA("愛麗雅", 99);


            richTextBox1.Text += Aaita.GetMsg() + "\n";
            richTextBox1.Text += Jasper.GetMsg() + "\n";
            richTextBox1.Text += Aliya.GetMsg() + "\n";
            richTextBox1.Text += "=====================\n";

            //呼叫StudentA類別的GetTotalStudent靜態方法取得目前有多少位學生
            richTextBox1.Text += StudentA.GetTotalStudent() + "\n";
        }
        //Student範例 SP

        //繼承範例 ST
        private void button19_Click(object sender, EventArgs e)
        {
            //繼承範例 1
            Empolyee Jasper = new Empolyee();  //Employee父類別
            Jasper.Name = "賈思伯";
            Jasper.Salary = 30000;
            richTextBox1.Text += "員工姓名：" + Jasper.Name + "\n實領薪水：" + Convert.ToString(Jasper.Salary) + "\n";
            richTextBox1.Text += "======================\n";
            Manager Aliya = new Manager();      //Manager子類別
            Aliya.Name = "愛麗雅";
            Aliya.Salary = 40000;
            Aliya.Bonus = 20000;    //Manager子類別新增的Bonus屬性
            //Manager子類別新增的GetTotal()方法
            richTextBox1.Text += Aliya.GetTotal() + "\n";


        }

        private void button20_Click(object sender, EventArgs e)
        {
            //繼承範例 2

        }

        //繼承範例 SP



    }
}
