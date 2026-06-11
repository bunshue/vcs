using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Timers;
using System.Threading;

//方案總管/右鍵/加入/類別/預設Class1.cs改成MyClass.cs

//方案總管/右鍵/加入/類別/預設Class1.cs改成PersonData.cs

//方案總管/右鍵/加入/Windows Form/預設Form2.cs改成MyForm.cs
//方案總管 點選MyForm.Designer.cs 刪除之
//修改MyForm.cs

//新增/加入 類別檔案 故意讓檔名,namespace,類別不一樣
//方案總管/右鍵/現有項目 選取Class1.cs

/*
方案總管 / 右鍵 / 加入 / 新增項目 選 類別
把 Class1.cs 改成 MyClass.cs
*/

using AnimalSpace;      //animal.cs cats.cs human.cs之namespace不一樣, 要引用
using MyClass;    // MyClass.cs之namespace不一樣, 要引用

namespace vcs_Class1
{
    public partial class Form1 : Form
    {
        TimerAlarm timeAlarm = new TimerAlarm();

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

            //------------------------------------------------------------  # 60個

            test_picture_class();
        }

        void show_item_location()
        {
            int W;
            int H;

            //小的groupBox
            W = 200;
            H = 180;
            groupBox2.Size = new Size(W, H);
            groupBox3.Size = new Size(W, H);
            groupBox1.Size = new Size(W, H);
            groupBox5.Size = new Size(W, H);
            groupBox6.Size = new Size(W, H);
            groupBox8.Size = new Size(W, H);
            groupBox10.Size = new Size(W, H);
            groupBox11.Size = new Size(W, H);
            groupBox12.Size = new Size(W, H);
            groupBox13.Size = new Size(W, H);

            //大的groupBox
            W = 200;
            H = 300;
            groupBox4.Size = new Size(W, H);
            groupBox7.Size = new Size(W, H);
            groupBox9.Size = new Size(W, H);
            groupBox14.Size = new Size(W * 2 + 10, H);
            groupBox_new.Size = new Size(W, H * 2 + 90);

            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = 180 + 10;
            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox5.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox6.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            groupBox8.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox10.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox11.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            groupBox12.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            groupBox13.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            groupBox7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            groupBox9.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            groupBox14.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            groupBox_new.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            dx = 200 + 10;
            dy = 60 + 10;

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

            button31.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button32.Location = new Point(x_st + dx * 0, y_st + dy * 1);

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

            W = 305 / 3;
            H = 400 / 3;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 10);
            pictureBox1.Location = new Point(x_st + dx * 0 + 70, y_st + dy * 0 + 40 + 10);
            pictureBox2.Location = new Point(x_st + dx * 0 + 140, y_st + dy * 0 + 80 + 10);

            dy = 60 + 6;
            bt_class_new_00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_class_new_01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_class_new_02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_class_new_03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_class_new_04.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_class_new_05.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_class_new_06.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_class_new_07.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            bt_class_new_08.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            bt_class_new_09.Location = new Point(x_st + dx * 0, y_st + dy * 9);


            this.Size = new Size(1700, 750);
            this.Text = "vcs_Class1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

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

        private void button6_Click(object sender, EventArgs e)
        {
            // 實例化Animal類別
            // 建立物件, 修改屬性, 使用方法

            Animal dog1 = new Animal();

            dog1.number = 1;
            dog1.type = "Poodle";	//貴賓犬
            dog1.name = "Peter";
            dog1.Show = "貴賓犬";
            richTextBox1.Text += "取出名稱 : " + dog1.Show + "\n";
            richTextBox1.Text += "取出參數 : " + dog1.recorder + "\n";

            Animal dog2 = new Animal();

            dog2.number = 2;
            dog2.type = "Maltese";	//馬爾濟斯
            dog2.name = "Mary";
            dog2.Show = "馬爾濟斯";
            richTextBox1.Text += "取出名稱 : " + dog2.Show + "\n";
            richTextBox1.Text += "取出參數 : " + dog2.recorder + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        //Sale範例 ST

        //類別的定義在 MyClass.cs

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

            richTextBox1.Text += "增加一個銷售物件\t洗衣機\n";
            SaleList.Add(new Sale("洗衣機", Convert.ToDateTime("2010-3-3"), 600));

            richTextBox1.Text += "增加一個銷售物件\t洗衣機\n";
            SaleList.Add(new Sale("洗衣機", Convert.ToDateTime("2010-3-3"), 600));

            richTextBox1.Text += "增加一個銷售物件\t洗衣機\n";
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

        //------------------------------------------------------------  # 60個

        //類別的定義在 MyClass.cs

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

        private void button9_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

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

            string name = "david";
            int age = 18;
            char gender = '男';

            Person p = new Person(name, age, gender, date);

            richTextBox1.Text += p.show() + "\n";
            richTextBox1.Text += "共有" + Person.counter() + "人\n";

            //------------------------------  # 30個

            int c = 95;
            int ma = 87;

            Student s = new Student(name, age, gender, date, c, ma);
            richTextBox1.Text += s.show() + "\n";

            String str = "共" + Person.counter() + "人, 學生: " + Student.counter() + "人\n";
            richTextBox1.Text += str + "\n";

            //------------------------------  # 30個

            string r = "senior";

            Teacher t = new Teacher(name, age, gender, date, r);

            str = "共" + Person.counter() + "人, 學生: " + Student.counter() + "人, 老師: " + Teacher.counter() + "人\n";

            richTextBox1.Text += str + "\n";
            richTextBox1.Text += t.show() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }
        //PersonData範例 SP

        //------------------------------------------------------------  # 60個

        //圖形範例 ST

        //類別的定義在 MyClass.cs

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

        //------------------------------------------------------------  # 60個

        //MyTime範例 ST

        //類別的定義在 MyClass.cs

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

        //------------------------------------------------------------  # 60個

        //Student範例 ST

        public class Student0    //將預設的class Class1 改成 class Student定義Student類別  
        {
            public string Name;       //Name姓名欄位
            public int Score;         //Score成績欄位, 此時的Score無限制

            public void ShowMsg()     //ShowMsg顯示姓名與成績的方法
            {
                MessageBox.Show(Name + "同學的分數是 " + Convert.ToString(Score));
            }

            public string GetMsg()   //GetMsg傳回姓名與成績的方法
            {
                return Name + "同學的分數是 " + Convert.ToString(Score);
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //類別範例

            Student0 Jasper = new Student0();  // 建立類別物件
            Jasper.Name = "賈思伯";             //設定Jasper物件的學生姓名
            Jasper.Score = 98;                  //設定Jasper物件的學生成績

            //Jasper.ShowMsg();  // 呼叫類別內的方法
            richTextBox1.Text += Jasper.GetMsg() + "\n";

            Student0 Anita = new Student0();  // 建立類別物件
            Anita.Name = "愛妮達";
            Anita.Score = 85;

            //Anita.ShowMsg();  // 呼叫類別內的方法
            richTextBox1.Text += Anita.GetMsg() + "\n";
        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {
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

        //------------------------------------------------------------  # 60個

        //繼承範例 ST
        //myclass
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

        //------------------------------------------------------------  # 60個

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

        void test_picture_class()
        {
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            Color2Gray c2g; // 宣告一個物件

            c2g = new Color2Gray(new Bitmap(filename2));
            pictureBox0.Image = c2g.bitmap1;

            c2g.do_Color2Gray();
            pictureBox1.Image = c2g.bitmap2;

            c2g.Draw();
            pictureBox2.Image = c2g.bitmap3;
        }

        //------------------------------------------------------------  # 60個

        //創建一個簡單的類來表示產品，產品有ID,類別，和價格
        public sealed class Product2
        {
            public int Id { get; set; }
            public string Category { get; set; }
            public double Value { get; set; }


            public override string ToString()
            {
                return string.Format("[{0}: {1} - {2}]", Id, Category, Value);
            }
        }

        public static List<Product2> GetList()
        {
            var products = new List<Product2>
            {
            new Product2 {Id = 1, Category = "Electronics", Value = 15.0},
            new Product2 {Id = 2, Category = "Groceries", Value = 40.0},
            new Product2 {Id = 3, Category = "Garden", Value = 210.3},
            new Product2 {Id = 4, Category = "Pets", Value = 2.1},
            new Product2 {Id = 5, Category = "Electronics", Value = 19.95},
            new Product2 {Id = 6, Category = "Pets", Value = 21.25},
            new Product2 {Id = 7, Category = "Pets", Value = 5.50},
            new Product2 {Id = 8, Category = "Garden", Value = 13.0},
            new Product2 {Id = 9, Category = "Automotive", Value = 10.0},
            new Product2 {Id = 10, Category = "Electronics", Value = 250.0},
            };
            return products;
        }

        private void button31_Click(object sender, EventArgs e)
        {
            List<Product2> list = GetList();

            richTextBox1.Text += "len = " + list.Count.ToString() + "\n";
            int cnt = list.Count;
            int i;
            for (i = 0; i < cnt; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + list[i].ToString() + "\n";
            }


            richTextBox1.Text += "按類別列出一個物品清單，用GroupBy\n";
            foreach (var group in list.GroupBy(p => p.Category))
            {
                Console.WriteLine(group.Key);
                foreach (var item in group)
                {
                    richTextBox1.Text += "	" + item + "\n";
                }
            }
        }

        private void button32_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        public class Classmate  //事件訂閱者
        {
            private string name;
            public Classmate(string Name)
            {
                name = Name;
            }
            public void SendResponse()  //事件處理函數，要與自定義委托類型匹配
            {
                Console.WriteLine("來自：" + this.name + "的回復: 已經收到邀請，隨時可以開始！");
            }
        }

        private void bt_class_new_00_Click(object sender, EventArgs e)
        {
            //Class 範例 0
            //c
            Classmate classmate1 = new Classmate("Alice");
            Classmate classmate2 = new Classmate("Banana");
            Classmate classmate3 = new Classmate("Cherry");
            Classmate classmate4 = new Classmate("Daisy");

            classmate1.SendResponse();
            classmate2.SendResponse();
            classmate3.SendResponse();
            classmate4.SendResponse();
        }

        //------------------------------------------------------------  # 60個

        public class Person3
        {
            public string Name { get; set; }
            public int Age { get; set; }
            public int Weight { get; set; }
            public int Height { get; set; }
        }

        private void bt_class_new_01_Click(object sender, EventArgs e)
        {
            //Class 範例 1
            Person3 p = new Person3() { Name = "Hong", Age = 25, Weight = 65, Height = 170 };

        }

        //------------------------------------------------------------  # 60個

        public class Shoe
        {
            public string Color;
        }

        public class Dude
        {
            public string Name;
            public Shoe RightShoe;
            public Shoe LeftShoe;

            public Dude CopyDude()
            {
                Dude newPerson = new Dude();
                newPerson.Name = Name;
                newPerson.LeftShoe = LeftShoe;
                newPerson.RightShoe = RightShoe;

                return newPerson;
            }

            public override string ToString()
            {
                return (Name + " : Dude!, I have a " + RightShoe.Color + " shoe on my right foot, and a " + LeftShoe.Color + " on my left foot.");
            }
        }

        private void bt_class_new_02_Click(object sender, EventArgs e)
        {
            //Class 範例 2

            Dude Bill = new Dude();
            Bill.Name = "Bill";
            Bill.LeftShoe = new Shoe();
            Bill.RightShoe = new Shoe();
            Bill.LeftShoe.Color = "Blue";
            Bill.RightShoe.Color = "Blue";

            Dude Ted = Bill.CopyDude();
            Ted.Name = "Ted";
            Ted.LeftShoe.Color = "Red";
            Ted.RightShoe.Color = "Red";

            richTextBox1.Text += "Bill\n" + Bill.ToString() + "\n";
            richTextBox1.Text += "Ted\n" + Ted.ToString() + "\n";
        }

        //------------------------------------------------------------  # 60個

        public class People
        {
            private string Id;
            private string Name;
            private string Address;
        }

        private void bt_class_new_03_Click(object sender, EventArgs e)
        {
            //Class 範例 3

            DataTable dt = new DataTable();
            dt.Columns.Add("Id", typeof(string));
            dt.Columns.Add("Name", typeof(string));
            dt.Columns.Add("Address", typeof(string));
            dt.PrimaryKey = new DataColumn[] { dt.Columns[0] };

            dt.Rows.Add("0001", "張三", "武漢市");
            dt.Rows.Add("0002", "李四", "北京市");
            dt.AcceptChanges();
            dt.Rows.Add("0003", "王五", "深圳市");

            //List<People> allPeople = new List<People>();
            //List<People> allPeople = new List<People>();

            /*
            List<People> allPeople = new List<People>()
            {
              new People(){ Id="0001", Name="張三", Address ="武漢市"},
              new People(){ Id="0002", Name="李四", Address ="北京市"},
              new People(){ Id="0003", Name="王五", Address ="深圳市"}
            };
            */
        }

        //------------------------------------------------------------  # 60個

        class P
        {
            private string pname;
            public string Name
            {
                get
                {
                    return "name : " + pname;
                }
                set
                {
                    pname = value;
                }
            }
        }

        private void bt_class_new_04_Click(object sender, EventArgs e)
        {
            //Class 範例 4
            P obj = new P();
            obj.Name = "david wang";            //使用到set
            Console.WriteLine(obj.Name);        //使用到get
        }

        //------------------------------------------------------------  # 60個

        /*
理解多態。
首先，我們先來看下怎樣用虛方法實現多態

我們都知道，喜鵲（Magpie）、老鷹（Eagle）、企鵝（Penguin）都是屬於鳥類，
我們可以根據這三者的共有特性提取出鳥類（Bird）做為父類，
喜鵲喜歡吃蟲子，老鷹喜歡吃肉，企鵝喜歡吃魚。
*/

        //創建基類Bird如下，添加一個虛方法Eat():

        /*
        /// <summary>
        /// 鳥類：父類
        /// </summary>
        public class Bird
        {
            /// <summary>
            /// 吃：虛方法
            /// </summary>
            public virtual void Eat()
            {
                Console.WriteLine("我是一只小小鳥，我喜歡吃蟲子~");
            }
        }
        */

        /// <summary>
        /// 鳥類：基類
        /// </summary>
        public abstract class Bird
        {
            /// <summary>
            /// 吃：抽象方法
            /// </summary>
            public abstract void Eat(); //抽象類Bird內添加一個Eat()抽象方法，沒有方法體。也不能實例化。
        }

        //創建子類Magpie如下，繼承父類Bird，重寫父類Bird中的虛方法Eat()：

        /// <summary>
        /// 飛 接口
        /// </summary>
        public interface IFlyable
        {
            void Fly();
        }

        /*
        /// <summary>
        /// 喜鵲：子類
        /// </summary>
        public class Magpie : Bird
        {
            /// <summary>
            /// 重寫父類中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只喜鵲，我喜歡吃蟲子~");
            }
        }

        //創建一個子類Eagle如下，繼承父類Bird，重寫父類Bird中的虛方法Eat()：

        /// <summary>
        /// 老鷹：子類
        /// </summary>
        public class Eagle : Bird
        {
            /// <summary>
            /// 重寫父類中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只老鷹，我喜歡吃肉~");
            }
        }
        */

        //喜鵲Magpie實現IFlyable接口，代碼如下：

        /// <summary>
        /// 喜鵲：子類，實現IFlyable接口
        /// </summary>
        public class Magpie : Bird, IFlyable
        {
            /// <summary>
            /// 重寫父類Bird中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只喜鵲，我喜歡吃蟲子~");
            }
            /// <summary>
            /// 實現 IFlyable接口方法
            /// </summary>
            public void Fly()
            {
                Console.WriteLine("我是一只喜鵲，我可以飛哦~~");
            }
        }

        //老鷹Eagle實現IFlyable接口，代碼如下：

        /// <summary>
        /// 老鷹：子類實現飛接口
        /// </summary>
        public class Eagle : Bird, IFlyable
        {
            /// <summary>
            /// 重寫父類Bird中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只老鷹，我喜歡吃肉~");
            }

            /// <summary>
            /// 實現 IFlyable接口方法
            /// </summary>
            public void Fly()
            {
                Console.WriteLine("我是一只老鷹，我可以飛哦~~");
            }
        }

        //創建一個子類Penguin如下，繼承父類Bird，重寫父類Bird中的虛方法Eat()：

        /// <summary>
        /// 企鵝：子類
        /// </summary>
        public class Penguin : Bird
        {
            /// <summary>
            /// 重寫父類中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只小企鵝，我喜歡吃魚~");
            }
        }

        /// <summary>
        /// 飛機類，實現IFlyable接口
        /// </summary>
        public class Plane : IFlyable
        {
            /// <summary>
            /// 實現接口方法
            /// </summary>
            public void Fly()
            {
                Console.WriteLine("我是一架飛機，我也能飛~~");
            }
        }

        private void bt_class_new_05_Click(object sender, EventArgs e)
        {
            //Class 範例 5

            //創建一個Bird基類數組，添加基類Bird對象，Magpie對象，Eagle對象，Penguin對象
            Bird[] birds = { 
                       //new Bird(),    用Abstract, Bird就不能創建對象了
                       new Magpie(),
                       new Eagle(),
                       new Penguin()
            };
            //遍歷一下birds數組
            foreach (Bird bird in birds)
            {
                bird.Eat();
            }

            //創建一個IFlyable接口數組，添加 Magpie對象，Eagle對象
            IFlyable[] flys = { 
                       new Magpie(),
                       new Eagle()
                              };
            //遍歷一下flys數組
            foreach (IFlyable fly in flys)
            {
                fly.Fly();
            }


            //創建一個IFlyable接口數組，添加 Magpie對象，Eagle對象，Plane對象
            IFlyable[] flys2 = { 
                           new Magpie(),
                           new Eagle(),
                           new Plane()
            };
            //遍歷一下flys數組
            foreach (IFlyable fly in flys2)
            {
                fly.Fly();
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_class_new_06_Click(object sender, EventArgs e)
        {
            //Class 範例 6 TimerAlarm

            timeAlarm = new TimerAlarm();
            timeAlarm.AlarmTime = FormatConvert.inputToSeconds("12:34:56");

            timeAlarm.Message = "AAAAAAAAA";

            if (timeAlarm.Countdown > 0)
            {
                this.timer6.Enabled = true;
            }
        }

        private void timer6_Tick(object sender, EventArgs e)
        {
            //動態顯示剩下的時間
            if (timeAlarm.Countdown >= 0)
            {
                richTextBox1.Text += FormatConvert.secondsToTime(timeAlarm.Countdown) + " ";
            }
            else
            {

                this.timer6.Enabled = false;
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_class_new_07_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("使用 類別方法 Logger\n");

            Logger.WriteLog("偵測不到PLC訊號, timeout, 清除信號, 等待使用者確認1");
            Logger.WriteLog("使用者確認, 回到原點, 開始偵測PLC訊號1");

            Logger.WriteLog("偵測不到PLC訊號, timeout, 清除信號, 等待使用者確認2");
            Logger.WriteLog("使用者確認, 回到原點, 開始偵測PLC訊號2");
        }

        //------------------------------------------------------------  # 60個

        private void bt_class_new_08_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void bt_class_new_09_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

    }

    //------------------------------------------------------------  # 60個

    public class TimerAlarm
    {
        private int clockTime = 0;
        private int alarmTime = 0;
        private string message = "时间到了";
        private System.Timers.Timer timerClock = new System.Timers.Timer();

        public int AlarmTime
        {
            set
            {
                alarmTime = value;
            }
        }

        public int ClockTime
        {
            set
            {
                clockTime = value;
            }
        }

        public string Message
        {
            set
            {
                message = value;
            }
        }

        public int Countdown
        {
            get
            {
                return alarmTime - clockTime;
            }
        }

        public TimerAlarm()
        {
            //MessageBox.Show("TimeAlarm start.");
            timerClock.Elapsed += new ElapsedEventHandler(OnTimer);
            timerClock.Interval = 1000;
            timerClock.Enabled = true;
        }

        public void OnTimer(Object source, ElapsedEventArgs e)
        {
            try
            {
                clockTime++;
                if (clockTime == alarmTime)
                {
                    MessageBox.Show(message, "时间到了", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }

            catch (Exception ex)
            {
                MessageBox.Show("OnTimer(): " + ex.Message);
            }
        }

        public void StopTimer()
        {
            timerClock.Enabled = false;
        }
    }

    //------------------------------------------------------------  # 60個

    public class FormatConvert
    {
        //inputToSeconds()将一个string型的时间字串转换成一共有多少秒。
        public static int inputToSeconds(string timerInput)
        {
            string[] timeArray = new string[3];
            int minutes = 0;
            int hours = 0;
            int seconds = 0;
            int occurence = 0;
            int length = 0;
            int totalTime = 0;

            occurence = timerInput.LastIndexOf(":");
            length = timerInput.Length;

            //Check for invalid input
            if (occurence == -1 || length != 8)
            {
                MessageBox.Show("Invalid Time Format.");
            }
            else
            {
                timeArray = timerInput.Split(':');
                seconds = Convert.ToInt32(timeArray[2]);
                minutes = Convert.ToInt32(timeArray[1]);
                hours = Convert.ToInt32(timeArray[0]);

                totalTime += seconds;
                totalTime += minutes * 60;
                totalTime += (hours * 60) * 60;
            }
            return totalTime;
        }

        //secondsToTime方法是把秒转换一个时间格式的字串返回。
        public static string secondsToTime(int seconds)
        {
            int minutes = 0;
            int hours = 0;
            while (seconds >= 60)
            {
                minutes += 1;
                seconds -= 60;
            }

            while (minutes >= 60)
            {
                hours += 1;
                minutes -= 60;
            }

            string strHours = hours.ToString();
            string strMinutes = minutes.ToString();
            string strSeconds = seconds.ToString();

            if (strHours.Length < 2)
                strHours = "0" + strHours;

            if (strMinutes.Length < 2)
                strMinutes = "0" + strMinutes;

            if (strSeconds.Length < 2)
                strSeconds = "0" + strSeconds;

            return strHours + ":" + strMinutes + ":" + strSeconds;
        }
    }

    //------------------------------------------------------------  # 60個

    public class Logger
    {
        /// <summary>
        /// 寫入日志.
        /// </summary>
        /// <param name="strList">The STR list.</param>
        /// <remarks> </remarks>
        /// <Description></Description>
        //public static void WriteLog(string ex)
        public static void WriteLog(params object[] strList)
        {
            if (strList.Count() == 0) return;
            string strDicPath = "";
            string strPath = "";
            try
            {
                //LogFileName = Application.StartupPath + "\\log_" + DateTime.Now.ToString("yyyyMMdd") + ".txt";
                strDicPath = Application.StartupPath + "//";
                strPath = strDicPath + string.Format("{0:yyyy年-MM月-dd日}", DateTime.Now) + "日誌記錄.txt";
            }
            catch (Exception e)
            {
                strDicPath = "C:/temp/log/";
                strPath = strDicPath + string.Format("{0:yyyy年-MM月-dd日}", DateTime.Now) + "日誌記錄.txt";
            }

            if (!Directory.Exists(strDicPath))
            {
                Directory.CreateDirectory(strDicPath);
            }
            if (!File.Exists(strPath))
            {
                using (FileStream fs = File.Create(strPath))
                {
                }
            }
            string str = File.ReadAllText(strPath);
            StringBuilder sb = new StringBuilder();
            foreach (var item in strList)
            {
                sb.Append(DateTime.Now.ToString() + "-----" + item + "\n");
            }

            File.WriteAllText(strPath, str + sb.ToString());
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


