using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;  // for Point, Color

namespace vcs_Class2
{
    class Class1
    {
    }

    //------------------------------------------------------------  # 60個

    class ClassBall
    {
        public Point pt; // 球的位置
        public Color color; // 球的顏色
        int D = 10; // 球的半徑
        int dx, dy; // 滑鼠和球的中心位置 的 偏移值

        // 建構元
        public ClassBall(Point pt, Color color)
        {
            this.pt = pt;
            this.color = color;
        }

        // 檢查是否選到這個點
        public bool CheckSelected(int x, int y)  // 滑鼠的位置 (視窗座標)
        {
            // 滑鼠游標 和 球的 距離
            double dist = Math.Sqrt((pt.X - x) * (pt.X - x) + (pt.Y - y) * (pt.Y - y));
            if (dist <= D)
            {
                dx = x - pt.X;
                dy = y - pt.Y;
                return true;
            }
            else return false;
        }

        // 更新 球的位置
        public void Move(int x, int y)  // 參數是 滑鼠的位置
        {
            pt.X = x - dx;
            pt.Y = y - dy;
        }
    }

    //------------------------------------------------------------  # 60個

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
            return base.show() + ": 底 = " + tbase + ", 高 = " + height;
        }

        public override double area()
        {
            return 0.5 * tbase * height;
        }

        public int compareTo(Object obj)
        {
            double myArea = area();
            double sArea = ((Shape)obj).area();

            if (myArea == sArea)
            {
                return 0;
            }
            else if (myArea < sArea)
            {
                return -1;
            }
            else
            {
                return 1;
            }
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
            return base.show() + ": 寬 = " + width + ", 高 = " + height;
        }
        public override double area()
        {
            return width * height;
        }

        public int compareTo(Object obj)
        {
            double myArea = area();
            double sArea = ((Shape)obj).area();

            if (myArea == sArea)
            {
                return 0;
            }
            else if (myArea < sArea)
            {
                return -1;
            }
            else
            {
                return 1;
            }
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
            if (s != null && count < 100)
            {
                shapeArray[count++] = s;
            }
        }

        public string listing()
        {
            string res = "";

            for (int i = 0; i < count; i++)
            {   // polymorphism
                Shape s = shapeArray[i];
                res += s.show() + ", 面積 = " + s.area() + "\r\n";
            }

            return res;
        }
        /*
         * 使用interface Comparable的compareTo(Object obj)方法取得比較的結果
         */
        public string maxShape()
        {
            if (count == 0)
            {
                return "尚未有圖形";
            }

            string res = "";

            Shape max = shapeArray[0];

            for (int i = 1; i < count; i++)
            {
                Shape cObj = shapeArray[i];
                if (((Comparable)cObj).compareTo(max) > 0)
                {
                    max = cObj;
                }
            }
            res = max.show();
            return res;
        }

        public string rankShape()
        {
            string res = "[ ";

            if (count == 0)
            {
                return res + "]";
            }

            int[] rank = new int[count];

            for (int i = 0; i < count; i++)
            {
                rank[i] = 1;
                Shape iShape = shapeArray[i];

                for (int j = 0; j < count; j++)
                {
                    Shape jShape = shapeArray[j];
                    if (((Comparable)jShape).compareTo(iShape) > 0)
                    {
                        rank[i]++;
                    }
                }
            }

            for (int i = 0; i < count; i++)
            {
                res += rank[i] + " ";
            }
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
}

//------------------------------------------------------------  # 60個

