using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;  // for Graphics, Color
using System.Windows.Forms;     //for MessageBox

namespace MyClass     //預設namespace同Form1.cs之namespace
{
    class Class1
    {
        //預設class同檔名
    }

    //------------------------------------------------------------  # 60個

    class Date
    {
        private int day;
        private int month;
        private int year;
        public Date()
        { // default constructor
            day = 1; month = 1; year = 2000;
        }
        /*
        public Date():this(1,1,2000) { // default constructor            
        }
        */

        public Date(int d, int m, int y)
        {  //constructor
            day = d; month = m; year = y;
        }

        public void setDate(int d, int m, int y)
        {
            day = d; month = m; year = y;
        }

        public string show()
        {
            return month + "-" + day + "-" + year;
        }

        public int getDay() { return day; }
        public int getMonth() { return month; }
        public int getYear() { return year; }
    }

    class Person
    {
        private string name;
        private int age;
        private char gender;
        private Date date;

        private static int ctr = 0;

        public static int counter()
        {
            return ctr;
        }
        // constructors
        public Person()
        {
            name = "unknown";
            age = 19;
            gender = 'M';
            date = new Date();
            ctr++;
        }

        public Person(string n, int a, char g)
        {
            name = n;
            age = a;
            gender = g;
            date = new Date();
            ctr++;
        }

        public Person(string n, int a, char g, Date d)
        {
            name = n;
            age = a;
            gender = g;
            date = d;
            ctr++;
        }
        // setter methods
        public void setName(string n)
        {
            name = n;
        }
        public void setAge(int a)
        {
            age = a;
        }
        public void setGender(char g)
        {
            gender = g;
        }
        public void setDate(Date d)
        {
            date = d;
        }
        // getter methods
        public string getName()
        {
            return name;
        }
        public int getAge()
        {
            return age;
        }
        public char getGender()
        {
            return gender;
        }
        public Date getDate()
        {
            return date;
        }
        public virtual string show()
        {
            string str = "名字 = " + name + "\r\n";
            str += "年齡 = " + age + "\r\n";
            str += "性別 = " + gender + "\r\n";
            str += "生日 = " + date.show();

            return str;
        }
        /*
        // operator overloading
        
        public static bool operator>=(Person p1, Person p2){
            if(p1.age >= p2.age) return true;
            else return false;
        }

        public static bool operator <=(Person p1, Person p2)
        {
            if (p1.age <= p2.age) return true;
            else return false;
        }
        */

    } // class Person


    class Student : Person
    {
        private int Chinese;  //新增私有的資料成員
        private int Math;
        // 靜態成員static members
        private static int ctr = 0;
        public static new int counter()
        {
            return ctr;
        }

        // 利用base(~)呼叫父類別Person的建構子
        public Student()
        {
            Chinese = Math = 0;  //預設值是0
            ctr++;
        }

        public Student(string n, int a, char g)
            : base(n, a, g)
        {
            Chinese = Math = 0;
            ctr++;
        }

        public Student(string n, int a, char g, Date d)
            : base(n, a, g, d)
        {
            Chinese = Math = 0;
            ctr++;
        }

        public Student(string n, int a, char g, int c, int m)
            : base(n, a, g)
        {
            Chinese = c;
            Math = m;
            ctr++;
        }

        public Student(string n, int a, char g, Date d, int c, int m)
            : base(n, a, g, d)
        {
            Chinese = c;
            Math = m;
            ctr++;
        }

        public void setChinese(int c)
        {
            Chinese = c;
        }

        public void setMath(int m)
        {
            Math = m;
        }

        public int getChinese()
        {
            return Chinese;
        }

        public int getMath()
        {
            return Math;
        }

        // 利用base.show()呼叫父類別Person的show()以取得Person的資訊
        public /*new*/ override string show()
        {
            string str = "<<< Student >>>\r\n";
            str += base.show() + "\r\n";
            str += "Chinese = " + Chinese + "\r\n";
            str += "Math = " + Math + "\r\n";

            return str;
        }
    }

    class Teacher : Person
    {
        private string Rank; //新增私有的資料成員
        // 靜態成員static members
        private static int ctr = 0;
        public static new int counter()
        {
            return ctr;
        }
        // 建構子
        public Teacher()
        {
            Rank = "Assistant Professor";
            ctr++;
        }
        public Teacher(string n, int a, char g)
            : base(n, a, g)
        {
            Rank = "Assistant Professor";
            ctr++;
        }

        public Teacher(string n, int a, char g, Date d)
            : base(n, a, g, d)
        {
            Rank = "Assistant Professor";
            ctr++;
        }

        public Teacher(string n, int a, char g, string r)
            : base(n, a, g)
        {
            Rank = r;
            ctr++;
        }

        public Teacher(string n, int a, char g, Date d, string r)
            : base(n, a, g, d)
        {
            Rank = r;
            ctr++;
        }

        public void setRank(string r)
        {
            Rank = r;
        }

        public string getRank()
        {
            return Rank;
        }

        public override /*new*/ string show()
        {
            string str = "<<< Teacher >>>\r\n";
            str += base.show() + "\r\n";
            str += "Rank = " + Rank + "\r\n";
            return str;
        }
    }

    //------------------------------------------------------------  # 60個

    class Circle
    {
        //protected int radius; // 子類別可以直接存取 
        private int radius;
        public Circle() { radius = 2; }  // 預設半徑為2
        public Circle(int r) { radius = r; }
        public int getRadius()
        {
            return radius;
        }
        public double getArea()
        {
            return Math.PI * radius * radius;
        }
    }

    class Cylinder : Circle
    {
        int length; // private

        public Cylinder() { length = 3; }  // 預設高度為3
        /*
        public Cylinder(int r, int l)
        {
            radius = r; // 此radius是繼承Circle而來 
            length = l;           
        }
        */

        public Cylinder(int r, int l)
            : base(r)
        {
            length = l;
        }

        public int getLength()
        {
            return length;
        }
        /*
        public new double getArea()
        {
            double ca = base.getArea();
            double cl = 2 * Math.PI * radius;
            return 2 * ca + cl * length;
        }
        */

        public new double getArea()
        {
            double ca = base.getArea();
            double cl = 2 * Math.PI * getRadius(); // base.getRadius();亦可
            return 2 * ca + cl * length;
        }
    }

    //------------------------------------------------------------  # 60個

    class MyTime
    {
        private int Hour;
        private int Minute;
        private int Second;

        // 預設建構子
        public MyTime()
        {
        }

        // 建構子
        public MyTime(int hh, int mm)
        {
            setTime(hh, mm);
        }

        // 建構子
        public MyTime(int hh, int mm, int ss)
        {
            setTime(hh, mm, ss);
        }

        public void setTime(int hh, int mm, int ss)
        {
            // 假設超出範圍，則不處理 
            /*
            if (hh < 0 || hh > 23) return;
            if (mm < 0 || mm > 59) return;
            if (ss < 0 || ss > 59) return;
            Hour = hh; Minute = mm; Second = ss;
            */
            if (validTime(hh, mm, ss))
            {
                Hour = hh;
                Minute = mm;
                Second = ss;
            }
        }

        public void setTime(int hh, int mm)
        {
            /*
            if (hh < 0 || hh > 23) return;
            if (mm < 0 || mm > 59) return;
            Hour = hh; Minute = mm; Second = 0;
            */
            if (validTime(hh, mm, 0))
            {
                Hour = hh;
                Minute = mm;
                Second = 0;
            }
        }

        private bool validTime(int hh, int mm, int ss)
        {
            if (hh < 0 || hh > 23) return false;
            if (mm < 0 || mm > 59) return false;
            if (ss < 0 || ss > 59) return false;
            return true;  // 合法資料 
        }

        public string getTime()
        {
            return Hour + ":" + Minute + ":" + Second;
        }

        // property
        public int mHour  // 有get有set, 可讀可寫
        {
            get
            {
                return Hour;
            }
            set
            {
                if (value < 0 || value > 23)
                    return;
                Hour = value;
            }
        }

        public int mMinute  // 有get有set, 可讀可寫
        {
            get
            {
                return Minute;
            }
            set
            {
                if (value < 0 || value > 59)
                    return;
                Minute = value;
            }
        }

        public int mSecond  // 有get有set, 可讀可寫
        {
            get
            {
                return Second;
            }
            set
            {
                if (value < 0 || value > 59)
                    return;
                Second = value;
            }
        }

        //解構子
        ~MyTime()
        { //不可加上public
            //MessageBox.Show("*** 物件已釋放 ***"); //測試用
        } // 必須Using System.Windows.Forms;
    }

    //------------------------------------------------------------  # 60個

    class Sale
    {
        public Sale()
        {
        }

        public Sale(string productName, DateTime saleDate, double salePrice)
        {
            this.ProductName = productName;
            this.SaleDate = saleDate;
            this.SalePrice = salePrice;
        }
        public string ProductName { get; set; } //貨品名稱  // 有get有set簡寫, 可讀可寫
        public DateTime SaleDate { get; set; }  //銷售日期  // 有get有set簡寫, 可讀可寫
        public double SalePrice { get; set; }   //銷售價格  // 有get有set簡寫, 可讀可寫
    }

    //------------------------------------------------------------  # 60個

    public class Empolyee      //定義Employee類別
    {
        public string Name;    //Name姓名欄位
        private int _Salary;   //_Salary薪水欄位
        public int Salary      //Salary薪水介於20000~40000之間  // 有get有set, 可讀可寫
        {
            get
            {
                return _Salary;
            }
            set
            {
                if (value <= 20000)
                    value = 20000;  //薪水最少20000
                if (value >= 40000)
                    value = 40000;  //薪水最多40000
                _Salary = value;
            }
        }
    }

    //Manager經理類別繼承自Empolyee員工類別
    public class Manager : Empolyee
    {
        private int _Bonus;		 //加入_Bonus獎金欄位
        public int Bonus         //_Bonus獎金介於10000~50000之間  // 有get有set, 可讀可寫
        {
            get
            {
                return _Bonus;
            }
            set
            {
                if (value <= 10000)
                    value = 10000;  //獎金最少10000
                if (value >= 50000)
                    value = 50000;  //獎金最多50000
                _Bonus = value;
            }
        }

        public string GetTotal()   	 //定義GetTotal()方法
        {
            return "經理姓名：" + Name +
                "\n實領薪水：" + Convert.ToString(Salary) +
                "\n實領獎金：" + Convert.ToString(Bonus) +
                "\n合計薪資：" + Convert.ToString(Bonus + Salary);
        }
    }

    //------------------------------------------------------------  # 60個

    class Cat
    {
        public string name;
        private string type;
        private int weight;

        public Cat()
        {
            this.name = "未知";
            this.type = "未知";
            this.weight = -1;
        }

        public Cat(string n, string t)
        {
            this.name = n;
            this.type = t;
            this.weight = -1;
        }

        public void settype(string t)
        {
            this.type = t;
        }

        public string gettype()
        {
            return this.type;
        }

        public void setweight(int w)
        {
            this.weight = w;
        }

        public int getweight()
        {
            return this.weight;
        }

        public void feed()
        {
            Console.WriteLine("餵食" + this.name);
            this.weight += 1;
        }

        public void play()
        {
            Console.WriteLine("與" + this.name + "遊戲");
            this.weight -= 1;
        }

        public void ShowMsg()
        {
            Console.WriteLine("名稱:" + this.name + " 品種:" + this.type + " 體重:" + this.weight);
        }

        public string GetMsg()
        {
            return "名稱:" + this.name + " 品種:" + this.type + " 體重:" + this.weight;
        }
    }

    //------------------------------------------------------------  # 60個

    class Color2Gray
    {
        public Bitmap bitmap1; // 原圖形
        public Bitmap bitmap2; // 新圖形
        public Bitmap bitmap3; // 新圖形

        public Color2Gray(Bitmap bmp)
        {
            this.bitmap1 = bmp;
            bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);
            bitmap3 = (Bitmap)bmp.Clone();
        }

        public void do_Color2Gray()
        {
            int xx;
            int yy;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    byte rrr = bitmap1.GetPixel(xx, yy).R;
                    byte ggg = bitmap1.GetPixel(xx, yy).G;
                    byte bbb = bitmap1.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap2.SetPixel(xx, yy, zz);
                }
            }
        }

        public void Draw()
        {
            Graphics g = Graphics.FromImage(bitmap3);
            g.DrawRectangle(Pens.Red, 10, 10, 100, 100);
            g.DrawRectangle(Pens.Red, 0, 0, bitmap3.Width, bitmap3.Height);
        }
    }

    //------------------------------------------------------------  # 60個

    class Animal
    {
        private string name;
        private string type;
        private int weight;

        protected void setname(string n)
        {
            this.name = n;
        }

        public string getname()
        {
            return this.name;
        }

        protected void settype(string t)
        {
            this.type = t;
        }

        public string gettype()
        {
            return this.type;
        }

        protected void setweight(int w)
        {
            this.weight = w;
        }

        public int getweight()
        {
            return this.weight;
        }

        public virtual void ShowMsg()
        {
            Console.WriteLine("名字:" + this.name + " 類型:" + this.type + " 重量:" + this.weight);
        }

        public virtual string GetMsg()
        {
            return "名字:" + this.name + " 類型:" + this.type + " 重量:" + this.weight;
        }
    }

    //------------------------------  # 30個

    class Human : Animal
    {
        private int height;
        private Animal pet;

        public Human(string n, string t, int w, int h)
        {
            this.setname(n);
            this.settype(t);
            this.setweight(w);
            this.height = h;
        }

        public void setpet(Animal a)
        {
            this.pet = a;
        }

        public Animal getpet()
        {
            return this.pet;
        }

        public override void ShowMsg()
        {
            Console.WriteLine("名字:" + this.getname() + " 重量:" + this.getweight() + " 身高:" + this.height);
        }

        public override string GetMsg()
        {
            return "名字:" + this.getname() + " 重量:" + this.getweight() + " 身高:" + this.height;
        }
    }

    //------------------------------  # 30個

    class Cats : Animal
    {
        private int body_length;
        private int tail_length;

        public Cats(string n, string t, int w, int b_length, int t_length)
        {
            this.setname(n);
            this.settype(t);
            this.setweight(w);
            this.body_length = b_length;
            this.tail_length = t_length;
        }

        public void print_length()
        {
            Console.WriteLine("體長:" + this.body_length + " 尾長:" + this.tail_length);
        }

        public string show_length()
        {
            return "體長:" + this.body_length + " 尾長:" + this.tail_length;
        }
    }

    //------------------------------------------------------------  # 60個

    class Car1
    {
        // 宣告_speed為私有變數，表示該變數只能在Car類別內使用
        private int _speed;

        // 定義GetSpeed()方法用來傳回_speed
        public int GetSpeed()
        {
            return _speed;
        }

        // 定義SetSpeed()方法用來設定_speed
        public void SetSpeed(int vSpeed)
        {
            if (vSpeed < 0)
            {
                vSpeed = 0;		// 設定速度不得低於 0
            }
            if (vSpeed > 200)
            {
                vSpeed = 200;	// 設定速度不得高於 200
            }
            _speed = vSpeed;
        }
    }

    class Car2   // 定義Car類別
    {
        // 宣告_speed私有變數用來存放車子的速度值
        private int _speed = 0;

        // 定義Speed速度屬性
        public int Speed  // 寫入有條件, 讀出無條件
        {
            get
            {
                return _speed;  // 傳回目前的速度
            }
            set
            {
                if (value < 0)
                {
                    value = 0;       // 速度不可小於0
                }
                if (value > 200)
                {
                    value = 200;   // 速度不可大於200
                }
                _speed = value;                 // 設定速度
            }
        }

        // 定義Accelerate()方法，用來指定目前車子速度+1 
        public void Accelerate()
        {
            _speed++;					// 速度 + 1
            if (_speed > 200)
            {
                _speed = 200;	// 檢查速度不可超過 200
            }
        }
    }

    //------------------------------------------------------------  # 60個

    class Student1
    {
        private int _Height, _Weight;

        public Student1()
        {
            _Weight = 48;
            _Height = 160;
        }

        // Student類別的建構式，須設定一個引數
        public Student1(int w)
        {
            _Weight = w;  		// 初始化_Weight欄位
            _Height = 160;	      	// 初始化_Height欄位的值為160
        }

        // Student類別的建構式，須設定兩個引數
        public Student1(int w, int h)
        {
            _Weight = w;
            _Height = h;
        }

        // Student類別的GetShow()方法，可顯示學生的身高和體重
        public void GetShow()
        {
            //richTextBox1.Text +=" 身高是: {0} "+ _Height+ "\n";
            //richTextBox1.Text +=" 體重是: {0} \n"+ _Weight+ "\n";
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
