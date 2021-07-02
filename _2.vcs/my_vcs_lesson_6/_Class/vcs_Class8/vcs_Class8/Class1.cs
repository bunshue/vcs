using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Class8
{
    class Class1
    {
    }


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
