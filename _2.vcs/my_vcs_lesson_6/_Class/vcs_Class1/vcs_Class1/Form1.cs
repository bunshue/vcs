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

//方案總管/右鍵/加入/Windows Form/預設Form2.cs改成MyForm.cs
//方案總管 點選MyForm.Designer.cs 刪除之
//修改MyForm.cs

//新增/加入 類別檔案 故意讓檔名,namespace,類別不一樣
//方案總管/右鍵/現有項目 選取Class1.cs

using vcs_Class6XXX;    //Class1.cs之namespace不一樣, 要引用

using CatTest;          //Cat.cs之namespace不一樣, 要引用
using AnimalSpace;      //animal.cs cats.cs human.cs之namespace不一樣, 要引用

namespace vcs_Class1
{
    public partial class Form1 : Form
    {
        class ClassExample
        {
            public ClassExample()
            {
                Console.WriteLine("建立一個ClassExample的物件");
            }

            ~ClassExample()
            {
                Console.WriteLine("銷毀一個ClassExample的物件");
            }
        }

        public class ClassPrintDataExample
        {
            private Form1 form1;
            private string _FirstName;
            public string FirstName
            {
                get { return _FirstName; }
                set { _FirstName = value; }
            }

            public string LastName { get; set; }

            public ClassPrintDataExample(string firstName, string lastName, Form1 f1)
            {
                FirstName = firstName;
                LastName = lastName;
                this.form1 = f1;
                f1.richTextBox1.Text += "ClassPrintDataExample初始化，從Class印出, FirstName = " + firstName + ", LastName = " + lastName + "\n";
            }

            public override string ToString()
            {
                return FirstName + " " + LastName;
            }
        }

        //測試Class陣列 1
        public class Person4
        {
            private string _FirstName;
            public string FirstName
            {
                get { return _FirstName; }
                set { _FirstName = value; }
            }

            public string LastName { get; set; }

            public Person4(string firstName, string lastName)
            {
                FirstName = firstName;
                LastName = lastName;
            }

            public override string ToString()
            {
                return FirstName + " " + LastName;
            }
        }

        //測試Class陣列 2
        public class Person5
        {
            public string FirstName { get; set; }
            public string LastName { get; set; }

            public override string ToString()
            {
                return FirstName + " " + LastName;
            }
        }

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
            w = 135;

            //小的groupBox
            h = 120;
            groupBox2.Size = new Size(w, h);
            groupBox3.Size = new Size(w, h);
            groupBox1.Size = new Size(w, h);
            groupBox5.Size = new Size(w, h);
            groupBox6.Size = new Size(w, h);
            groupBox8.Size = new Size(w, h);
            groupBox10.Size = new Size(w, h);
            groupBox11.Size = new Size(w, h);
            groupBox12.Size = new Size(w, h);

            //大的groupBox
            h = 250;
            groupBox4.Size = new Size(w, h);
            groupBox7.Size = new Size(w, h);
            groupBox9.Size = new Size(w, h);

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 12;
            y_st = 12;
            dx = 150;
            dy = 140;

            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox5.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox6.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            groupBox8.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox10.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox11.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            groupBox12.Location = new Point(x_st + dx * 3, y_st + dy * 1);

            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            groupBox7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            groupBox9.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            x_st = 15;
            y_st = 15;
            dx = 150;
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

            button25.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button26.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button27.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button28.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button29.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button30.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button16.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button17.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button18.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            button21.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 3);
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
            //繼承表單
            MyForm f = new MyForm();    //建立f 為MyForm類別
            f.ShowDialog();			//呼叫f.ShowDialog()方法使視窗顯示
        }
        //繼承範例 SP

        //Stack範例 ST
        MyStack stack;
        private void button21_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "初始化20個stack\n";
            stack = new MyStack(20);
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //push
            stack.Push(1);
            stack.Push(3);
            stack.Push(5);
            stack.Push(7);
            stack.Push(9);
            stack.Push(11);
            richTextBox1.Text += "Push 6 個stack : 1 3 5 7 9 11\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //pop
            int pop = stack.Pop();
            richTextBox1.Text += "Pop 1 個stack : " + pop.ToString() + "\n";
        }

        private void button24_Click(object sender, EventArgs e)
        {

        }
        //Stack範例 SP

        //寵物範例 ST
        private void button25_Click(object sender, EventArgs e)
        {
            //寵物範例1
            richTextBox1.Text += "初始化 Cat 1\n";
            Cat kitty = new Cat();
            kitty.name = "凱蒂";

            richTextBox1.Text += "初始化 Cat 2\n";
            Cat doraemon = new Cat("多啦A夢", "機器貓");
            doraemon.setweight(129);

            richTextBox1.Text += "初始化 Cat 3\n";
            Cat garfield = new Cat("加菲", "虎斑貓");
            garfield.setweight(5);

            richTextBox1.Text += "訊息\n";
            kitty.ShowMsg();
            doraemon.ShowMsg();
            garfield.ShowMsg();
            richTextBox1.Text += kitty.GetMsg() + "\n";
            richTextBox1.Text += doraemon.GetMsg() + "\n";
            richTextBox1.Text += garfield.GetMsg() + "\n";

            richTextBox1.Text += "進行動作\n";
            garfield.feed();
            doraemon.play();

            richTextBox1.Text += "訊息\n";
            kitty.ShowMsg();
            doraemon.ShowMsg();
            garfield.ShowMsg();
            richTextBox1.Text += kitty.GetMsg() + "\n";
            richTextBox1.Text += doraemon.GetMsg() + "\n";
            richTextBox1.Text += garfield.GetMsg() + "\n";
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //寵物範例2
            richTextBox1.Text += "初始化 Human\n";
            Human myself = new Human("小李", "亞洲人", 64, 172);

            richTextBox1.Text += "初始化 Cats\n";
            Cats mypet = new Cats("喵仔", "暹邏貓", 7, 30, 20);

            myself.setpet(mypet);

            myself.ShowMsg();
            richTextBox1.Text += "主人資訊:\t" + myself.GetMsg() + "\n";

            Console.WriteLine("類型為:" + myself.gettype());
            richTextBox1.Text += "類型為:\t" + myself.gettype() + "\n";

            Console.WriteLine("他的寵物是:");
            myself.getpet().ShowMsg();
            mypet.print_length();

            richTextBox1.Text += "他的寵物是:\t" + myself.getpet().GetMsg() + "\n";
            richTextBox1.Text += "寵物資訊:\t" + mypet.show_length() + "\n";
        }

        //寵物範例 SP

        private void button27_Click(object sender, EventArgs e)
        {
            //Class List 使用
            List<Product> Products = new List<Product>();

            // Load the data.
            // Cake slices.
            string[] cakes =
            {
                "Black Forest Cake",
                "Strawberry Chocolate Mousse Cake",
                "Chocolate Mousse Cake",
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
        private void button28_Click(object sender, EventArgs e)
        {
            //Class 陣列使用

            int i;

            richTextBox1.Text += "建立一個Person4物件一維陣列, 長度3\n";
            Person4[] people = new Person4[3];

            richTextBox1.Text += "對第0個物件初始化\n";
            people[0] = new Person4("David", "Wang");
            richTextBox1.Text += "對第1個物件初始化\n";
            people[1] = new Person4("Jerry", "Lin");
            richTextBox1.Text += "對第2個物件初始化\n";
            people[2] = new Person4("James P.", "Sullivan");

            richTextBox1.Text += "顯示每個物件的內容\n";
            for (i = 0; i < 3; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + "個\t" + people[i].ToString() + "\n";
            }

            richTextBox1.Text += "\n建立一個Person物件一維陣列, 長度3, 並初始化\n";
            Person5[] people2 = 
            {
                new Person5() { FirstName="David", LastName="Wang" },
                new Person5() { FirstName="Jerry", LastName="Lin" },
                new Person5() { FirstName="James P.", LastName="Sullivan" },
            };

            richTextBox1.Text += "顯示每個物件的內容\n";
            for (i = 0; i < 3; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + "個\t" + people2[i].ToString() + "\n";
            }
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //從Class內印出資料
            //從Class內使用Form1的控件，richTextBox改為Public ?? 不用??

            richTextBox1.Text += "從Class內印出資料, 建立一個 ClassPrintDataExample 物件\n";
            ClassPrintDataExample people;

            richTextBox1.Text += "初始化\n";
            people = new ClassPrintDataExample("David", "Wang", this);

            richTextBox1.Text += "顯示物件的內容\n";

            richTextBox1.Text += people.ToString() + "\n";
        }

        private void button30_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建構子和解構子 class ClassExample, 看輸出畫面的log\n";

            //建構子
            richTextBox1.Text += "新增一個ClassExample物件\n";
            ClassExample person = new ClassExample();

            //解構子
            richTextBox1.Text += "銷毀\n";
            GC.Collect();       // Force garbage collection.

        }
    }
}
