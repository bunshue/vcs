using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MyClass     //預設namespace同Form1.cs之namespace
{
    class Class1
    {
        //預設class同檔名
    }

    //------------------------------------------------------------  # 60個

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

        public Cylinder(int r, int l)
            : base(r)
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

    //------------------------------------------------------------  # 60個

    class Person2
    {
        private string firstname = "DEFAULT";
        private string lastname = "CAN NOT CHANGE";
        private int age;

        public string FirstName  //可讀可寫, 有get有set
        {
            get
            {
                return firstname;
            }
            set
            {
                firstname = value;
            }
        }

        public string LastName  //可讀不可寫, 只有get
        {
            get
            {
                return lastname;
            }
        }

        public int Age  //可讀可寫, 有get有set
        //可讀可寫  set部分可加入判斷式來對傳入的值做相對應處理
        {
            get
            {
                return age;
            }
            set
            {
                age = (value < 10) ? 0 : 100; //if簡寫
                //原表示
                /*if(value<10)
                {
                        age =0;
                }
                else
                {
                        age =100;
                }*/
            }
        }

        public string Sex  //get set 簡寫  可讀可寫
        {
            get;
            set;
        }

        public string ADDR  //get set 簡寫  可讀不可寫
        {
            get;
            private set;
        }
    }

    //------------------------------------------------------------  # 60個

    class MyTime
    {
        private int Hour;
        private int Minute;
        private int Second;

        // constructor
        public MyTime(int h, int m, int s)
        {
            setTime(h, m, s);
        }

        public MyTime(int h, int m)
        {
            setTime(h, m);
        }

        // default constructor
        public MyTime() { }

        public void setTime(int h, int m, int s)
        {
            // 假設超出範圍，則不處理 
            /*
            if (h < 0 || h > 23) return;
            if (m < 0 || m > 59) return;
            if (s < 0 || s > 59) return;
            Hour = h; Minute = m; Second = s;
            */
            if (validTime(h, m, s))
            {
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
            if (validTime(h, m, 0))
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
            set
            {
                if (value < 0 || value > 23) return;
                Hour = value;
            }
        }
        public int mMinute
        {
            get { return Minute; }
            set
            {
                if (value < 0 || value > 59) return;
                Minute = value;
            }
        }
        public int mSecond
        {
            get { return Second; }
            set
            {
                if (value < 0 || value > 59) return;
                Second = value;
            }
        }

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
        public string ProductName { get; set; } //貨品名稱
        public DateTime SaleDate { get; set; }  //銷售日期
        public double SalePrice { get; set; }   //銷售價格
    }

    //------------------------------------------------------------  # 60個

    public class Empolyee      //定義Employee類別
    {
        public string Name;    //Name姓名欄位
        private int _Salary;   //_Salary薪水欄位
        public int Salary      //Salary薪水介於20000~40000之間
        {
            get
            {
                return _Salary;
            }
            set
            {
                if (value <= 20000) value = 20000;  //薪水最少20000
                if (value >= 40000) value = 40000;  //薪水最多40000
                _Salary = value;
            }
        }
    }
    //Manager經理類別繼承自Empolyee員工類別
    public class Manager : Empolyee
    {
        private int _Bonus;		 //加入_Bonus獎金欄位
        public int Bonus         //_Bonus獎金介於10000~50000之間
        {
            get
            {
                return _Bonus;
            }
            set
            {
                if (value <= 10000) value = 10000;  //獎金最少10000
                if (value >= 50000) value = 50000;  //獎金最多50000
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

}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

