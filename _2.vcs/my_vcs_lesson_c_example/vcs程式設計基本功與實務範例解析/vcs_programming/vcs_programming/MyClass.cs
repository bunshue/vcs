using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    class MyTime {
        private int Hour;
        private int Minute;
        private int Second;

        // constructor
        public MyTime(int h, int m, int s) {
            setTime(h, m, s);
        }

        public MyTime(int h, int m)
        {
            setTime(h, m);
        }

        // default constructor
        public MyTime() { }
        
        public void setTime(int h, int m, int s) {
            // 假設超出範圍，則不處理 
            /*
            if (h < 0 || h > 23) return;
            if (m < 0 || m > 59) return;
            if (s < 0 || s > 59) return;
            Hour = h; Minute = m; Second = s;
            */
            if ( validTime(h, m, s) ) {
                Hour = h; Minute = m; Second = s;
            }
        }

        public void setTime(int h, int m)
        {
            /*
            if (h < 0 || h > 23) return;
            if (m < 0 || m > 59) return;
            Hour = h; Minute = m; Second = 0;
            */
            if ( validTime(h, m, 0) )
            {
                Hour = h; Minute = m; Second = 0;
            }
        }

        private bool validTime(int h, int m, int s)
        {
            if (h < 0 || h > 23) return false;
            if (m < 0 || m > 59) return false;
            if (s < 0 || s > 59) return false;
            return true;  // 合法資料 
        }

        public string getTime()
        {
            return Hour + ":" + Minute + ":" + Second;
        }

        // property
        public int mHour
        {
            get { return Hour; }
            set {
                if (value < 0 || value > 23) return;
                Hour = value;
            }
        }
        public int mMinute
        {
            get { return Minute; }
            set {
                if (value < 0 || value > 59) return;
                Minute = value;
            }
        }
        public int mSecond
        {
            get { return Second; }
            set {
                if (value < 0 || value > 59) return;
                Second = value;
            }
        }

        ~MyTime() { //不可加上public
			//MessageBox.Show("*** 物件已釋放 ***"); //測試用
        } // 必須Using System.Windows.Forms;

    }

    class Date {
        private int day;
        private int month;
        private int year;
        public Date() { // default constructor
            day = 1; month = 1; year = 2000;
        }
        /*
        public Date():this(1,1,2000) { // default constructor            
        }
        */
        public Date(int d, int m, int y) {  //constructor
            day = d; month = m; year = y;
        }
        public void setDate(int d, int m, int y) {
	        day = d;  month = m;  year = y;
        }
        public string show( ) {
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

    // Protected member

    class b
    {
        protected int x = 3;
    }

    class d1
    {
        public d1()
        {
            //x = 10; //compile error
        }

        public void f1()
        {
            b bobj = new b();
            //bobj.x = 10; //can not access x
        }
    }

    class d2 : b
    {
        public d2()
        {
            x = 10;
        }

        public void f2()
        {
            b bobj = new b();
            //bobj.x = 10; // can not access x
            
            d2 dobj = new d2();
            dobj.x = 10;

            x = 100;
        }
    }

    // Inheritance: Cicle and Cylinder

    class Circle
    {
        //protected int radius; // 子類別可以直接存取 
        private int radius;
        public Circle() { radius = 2; }
        public Circle(int r) { radius = r; }
        public int getRadius() { return radius; }
        public double getArea()
        {
            return Math.PI * radius * radius;
        }
    }

    class Cylinder : Circle
    {
        int length; // private

        public Cylinder() { length = 3; }
        /*
        public Cylinder(int r, int l)
        {
            radius = r; // 此radius是繼承Circle而來 
            length = l;           
        }
        */
        
        public Cylinder(int r, int l) : base(r)
        {
            length = l;
        }
        
        public int getLength() { return length; }
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

    class Base
    {
        public void Method()
        {
            MessageBox.Show("Base.Method");
        }

        public virtual void VMethod()
        {
            MessageBox.Show("Base.VMethod");
        }
    }

    class Derived : Base
    {
        public void DMethod()  //新增方法
        {
            MessageBox.Show("Derived.DMethod");
        }

        public new void Method()  //new改寫同名方法
        {
            MessageBox.Show("Derived.Method");
        }        

        public override void VMethod()
        {
            MessageBox.Show("Derived.VMethod");
        }

    }


    abstract class Shape
    {
        private string type;
        public Shape(string type)
        {
            this.type = type;
        }
        public string getType()
        {
            return type;
        }
        public virtual string show() { return type; }
        abstract public double area();
    }

    interface Comparable
    {
        int compareTo(Object obj);
    }

    class Triangle : Shape, Comparable
    {
        private double tbase;
        private double height;
        public Triangle(double tbase, double height)
            : base("Triangle")
        {
            this.tbase = tbase;
            this.height = height;
        }
        public override string show()
        {
            return base.show() +
                   ": 底 = " + tbase +
                   ", 高 = " + height;
        }
        public override double area()
        {
            return 0.5 * tbase * height;
        }
        
        public int compareTo(Object obj)
        {
            double myArea = area();
            double sArea = ((Shape)obj).area();

            if (myArea == sArea) return 0;
            else if (myArea < sArea) return -1;
            else return 1;
        }
    }

    class Rectangle : Shape, Comparable
    {
        private double width;
        private double height;
        public Rectangle(double width, double height)
            : base("Rectangle")
        {
            this.width = width;
            this.height = height;
        }
        public override string show()
        {
            return base.show() +
                   ": 寬 = " + width +
                   ", 高 = " + height;
        }
        public override double area()
        {
            return width * height;
        }
        
        public int compareTo(Object obj)
        {
            double myArea = area();
            double sArea = ((Shape)obj).area();

            if (myArea == sArea) return 0;
            else if (myArea < sArea) return -1;
            else return 1;
        }
        
    }

    class ShapeCollection
    {
        private int count = 0;

        private Shape[] shapeArray = new Shape[100];

        public ShapeCollection() { }

        public int getCount() { return count; }

        public void add(Shape s)
        {
            if (s != null && count < 100)shapeArray[count++] = s;         
        }

        public string listing()
        {
            string res = "";

            for (int i = 0; i < count; i++)
            {   // polymorphism
                Shape s = shapeArray[i];
                res += s.show() + ", 面積 = " + s.area() +
                       "\r\n-----------------------\r\n";
            }

            return res;
        }
        /*
         * 使用interface Comparable的compareTo(Object obj)方法取得比較的結果
         */
        public string maxShape()
        {
           if (count == 0) return "尚未有圖形";

           string res = "";

           Shape max = shapeArray[0];

            for (int i = 1; i < count; i++)
            {
                Shape cObj = shapeArray[i];
                if (((Comparable)cObj).compareTo(max) > 0)               
                    max = cObj;
            }

            res = max.show();

            return res;
        }
        
        public string rankShape()
        {
            string res = "[ ";

            if (count == 0) return res + "]";

            int[] rank = new int[count];

            for (int i = 0; i < count; i++)
            {
                rank[i] = 1;
                Shape iShape = shapeArray[i];

                for (int j = 0; j < count; j++)
                {
                    Shape jShape = shapeArray[j];
                    if (((Comparable)jShape).compareTo(iShape) > 0)
                        rank[i]++;
                }
            }

            for (int i = 0; i < count; i++)
                res += rank[i] + " ";

            return res + "]";
        }

        /*
         * 直接使用area()方法來進行比較
        */
        /*
        public string maxShape()
        {
            if (count == 0) return "尚未有圖形";

            string res = "";

            Shape max = shapeArray[0];

            for (int i = 1; i < count; i++)
            {
                Shape cObj = shapeArray[i];

                if (cObj.area() > max.area())
                    max = cObj;
            }

            res = max.show();

            return res;
        }

        public string rankShape()
        {
            string res = "[ ";

            if (count == 0) return res + "]";

            int[] rank = new int[count];

            for (int i = 0; i < count; i++)
            {
                rank[i] = 1;
                Shape iShape = shapeArray[i];

                for (int j = 0; j < count; j++)
                {
                    Shape jShape = shapeArray[j];
                    if (jShape.area() > iShape.area())
                        rank[i]++;
                }
            }

            for (int i = 0; i < count; i++)
                res += rank[i] + " ";

            return res + "]";
        }
        */

    }

}
