using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Class_all
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            richTextBox1.Size = new Size(400, 800);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1100, 910);
            this.Text = "vcs_Class_all";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        class Student
        {
            //第一個靜態方法-計算總分
            public static uint Total(uint a, uint b, uint c)
            {
                uint sum = a + b + c;//總分
                return sum;//回傳加總結果         
            }
            //第二個靜態方法-算平均分數
            public static float Average(string word, uint number)
            {
                float result = number / 3.0F;//平均
                return result;
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //使用類別的靜態方法
            string name = "david";
            uint math = 90;
            uint eng = 82;
            uint chin = 85;

            //直接以類別來呼叫靜態方法Total()、Average()
            uint score = Student.Total(math, eng, chin);
            float avg = Student.Average("平均分數", score);

            Console.WriteLine(name = " " + "總分 : " + score + "\t平均 : " + avg);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //class test
            Car1 Benz1 = new Car1();
            Benz1.SetSpeed(500);			// 速度值超過 200
            richTextBox1.Text += "Benz1.GetSpeed() = {0}" + Benz1.GetSpeed() + "\n";	// 顯示速度最大值200

            richTextBox1.Text += "------------------------------\n";  // 30個

            Car2 Benz2 = new Car2();
            Benz2.Speed = 199;
            richTextBox1.Text += "現在速度:{0}" + Benz2.Speed + "\n";
            richTextBox1.Text += "加速 ..." + "\n";
            Benz2.Accelerate();
            richTextBox1.Text += "現在速度:{0}" + Benz2.Speed + "\n";
            richTextBox1.Text += "加速 ..." + "\n";
            Benz2.Accelerate();
            richTextBox1.Text += "現在速度:{0}" + Benz2.Speed + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            Student1 Peter = new Student1();
            richTextBox1.Text += " Peter的資料-->使用Student()建構式\n";
            Peter.GetShow();
            Student1 David = new Student1(56);
            richTextBox1.Text += " David的資料-->使用Student(56)建構式\n";
            David.GetShow();
            Student1 Mary = new Student1(48, 150);
            richTextBox1.Text += " Mary的資料 -->使用Student(48, 150)建構式\n";
            Mary.GetShow();

            richTextBox1.Text += "------------------------------\n";  // 30個

            Student2 David2 = new Student2(56);
            richTextBox1.Text += " David2的資料-->使用Student(56)建構式\n";
            David2.GetShow();
            Student2 Mary2 = new Student2(48, 150);
            richTextBox1.Text += " Mary2的資料 -->使用Student(48, 150)建構式\n";
            Mary2.GetShow();

            richTextBox1.Text += "------------------------------\n";  // 30個

            Student3 Peter3 = new Student3();
            richTextBox1.Text += " Peter3的資料-->使用Student()建構式\n";
            Peter3.GetShow();
            Student3 David3 = new Student3(56);
            richTextBox1.Text += " David3的資料-->使用Student(56)建構式\n";
            David3.GetShow();
            Student3 Mary3 = new Student3(48, 150);
            richTextBox1.Text += " Mary3的資料 -->使用Student(48, 150)建構式\n";
            Mary3.GetShow();
        }

        class Book
        {
            public int books; //宣告books為公用變數
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //class book
            Book eng = new Book();
            eng.books = 10;
            richTextBox1.Text += "目前英文類書籍共有{0}本" + eng.books + "\n";

        }

        //------------------------------------------------------------  # 60個

        //之後 class PersonClass 在獨立成一個檔案 PersonClass.cs
        class PersonClass
        {
            //自動實作屬性
            public string Name { get; set; }
            public byte Height { get; set; }

            //定義靜態方法
            public void showInfo(PersonClass first)
            {
                //指派屬性值做物件初始化
                first = new PersonClass() { Name = "林小明", Height = 172 };
            }

            //定義靜態方法
            public void display(ref PersonClass second)
            {
                //指派屬性值做物件初始化
                second = new PersonClass { Name = "江大海", Height = 168 };
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //class

            PersonClass pern = new PersonClass() { Name = "王小風", Height = 176 };

            richTextBox1.Text += "By Value -> \n";
            //Passing By Value - 輸出王小風
            pern.showInfo(pern);

            richTextBox1.Text += pern.Name + "\t" + pern.Height + "\n";
            //Console.WriteLine($"{pern.Name}, " +               $"您的身高 {pern.Height}cm");
            richTextBox1.Text += "By Reference -> \n";
            //Passing By Reference - 輸出江大海
            pern.display(ref pern);

            richTextBox1.Text += pern.Name + "\t" + pern.Height + "\n";
            //Console.WriteLine($"{pern.Name}, " +               $"您的身高 {pern.Height}cm");
            //Console.ReadKey();
        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
            //不重複之排列

            int[] Choices;
            int num_candidates = 10;
            Choices = Extensions.RandomArrangement(num_candidates);

            foreach (int i in Choices)
            {
                richTextBox1.Text += i.ToString() + " ";

            }
            richTextBox1.Text += "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        //建立 HDateTime 類別
        public class HDateTime
        {
            public int year;
            public int month;
            public int day;
            //public string name;
            //A class被實例化時，會立即執行建構子內容，並且可以傳入參數
            public string Show
            {
                // 可以透過 get 存取子，將字串進行判斷、處理.... 再返回結果
                //get { return name; }

                // set含有特殊的keyword: value, 當有值傳入時，都會存入value中
                set
                {
                    //name = type;
                    //Console.WriteLine("I am " + value);
                }
            }

            public HDateTime Parse(string dd)
            {
                HDateTime mdt = new HDateTime();

                int index_year;
                int index_month;
                int index_day;

                index_year = dd.IndexOf("年", 0);
                index_month = dd.IndexOf("月", index_year + 1);
                index_day = dd.IndexOf("日", index_month + 1);

                int year = 0;
                int month = 0;
                int day = 0;

                if ((index_year == -1) || (index_month == -1) || (index_day == -1))
                {
                    //return new HDateTime(0, 0, 0);
                }
                else
                {
                    year = int.Parse(dd.Substring(0, index_year - 0));
                    month = int.Parse(dd.Substring(index_year + 1, index_month - index_year - 1));
                    day = int.Parse(dd.Substring(index_month + 1, index_day - index_month - 1));
                    //return new DateTime(year, month, day);
                }
                if ((month < 1) || (month > 12))
                    month = -1;
                if ((day < 1) || (day > 31))
                    day = -1;

                mdt.year = year;
                mdt.month = month;
                mdt.day = day;
                return mdt;
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //測試 MyDateTime 1
            //為年表所做的時間分析程式HDateTime.Parse


            string dd1 = "541年7月21日";
            string dd2 = "-541年17月21日";
            string dd3 = "41年7月-20日";
            string dd4 = " 541年 7月 21日";   //包含空白

            HDateTime hdt = new HDateTime();

            richTextBox1.Text += "原字串\t" + dd1 + "\n";
            hdt = hdt.Parse(dd1);
            richTextBox1.Text += "解讀後, yy = " + hdt.year.ToString() + ", mm = " + hdt.month.ToString() + ", dd = " + hdt.day.ToString() + "\n";

            richTextBox1.Text += "原字串\t" + dd2 + "\n";
            hdt = hdt.Parse(dd2);
            richTextBox1.Text += "解讀後, yy = " + hdt.year.ToString() + ", mm = " + hdt.month.ToString() + ", dd = " + hdt.day.ToString() + "\n";

            richTextBox1.Text += "原字串\t" + dd3 + "\n";
            hdt = hdt.Parse(dd3);
            richTextBox1.Text += "解讀後, yy = " + hdt.year.ToString() + ", mm = " + hdt.month.ToString() + ", dd = " + hdt.day.ToString() + "\n";

            richTextBox1.Text += "包含空白 原字串\t" + dd4 + "\n";
            hdt = hdt.Parse(dd4);
            richTextBox1.Text += "解讀後, yy = " + hdt.year.ToString() + ", mm = " + hdt.month.ToString() + ", dd = " + hdt.day.ToString() + "\n";
        }

        //------------------------------------------------------------  # 60個

        public class Person
        {
            public string Name;
            public int Age;
            public DateTime birthday;
        }

        public struct Age
        {
            public int Years;
            public int Months;
            public int Days;
        }
        public static Age CalculateAge(DateTime birthDate, DateTime endDate)
        {
            if (birthDate.Date > endDate.Date)
            {
                throw new ArgumentException("birthDate cannot be higher then endDate", "birthDate");
            }

            int years = endDate.Year - birthDate.Year;
            int months = 0;
            int days = 0;

            // Check if the last year, was a full year.
            if (endDate < birthDate.AddYears(years) && years != 0)
            {
                years--;
            }

            // Calculate the number of months.
            birthDate = birthDate.AddYears(years);

            if (birthDate.Year == endDate.Year)
            {
                months = endDate.Month - birthDate.Month;
            }
            else
            {
                months = (12 - birthDate.Month) + endDate.Month;
            }

            // Check if last month was a complete month.
            if (endDate < birthDate.AddMonths(months) && months != 0)
            {
                months--;
            }

            // Calculate the number of days.
            birthDate = birthDate.AddMonths(months);

            days = (endDate - birthDate).Days;
            Age result;
            result.Years = years;
            result.Months = months;
            result.Days = days;
            return result;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //測試 MyDateTime 2
            Person av1 = new Person();
            av1.Name = "松島かえで";
            av1.birthday = DateTime.Parse("1982年11月07日");
            av1.Age = 18;
            richTextBox1.Text += "姓名：" + av1.Name + "\n";
            //richTextBox1.Text += "年齡：" + av1.Age.ToString() + "\n";
            richTextBox1.Text += "生日：" + av1.birthday.ToShortDateString() + "\n";

            DateTime flakNow = DateTime.Now;
            Age myAge = CalculateAge(av1.birthday, flakNow);
            richTextBox1.Text += "年 : " + myAge.Years.ToString() + "\n";
            richTextBox1.Text += "月 : " + myAge.Months.ToString() + "\n";
            richTextBox1.Text += "日 : " + myAge.Days.ToString() + "\n";
            if ((myAge.Months != 0) && (myAge.Days != 0))
                av1.Age = myAge.Years + 1;
            else
                av1.Age = myAge.Years;
            richTextBox1.Text += "年齡：" + av1.Age.ToString() + "\n";

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //測試 MyDateTime 3
            string txt = "2006/3/11";

            DateTime dt = DateTime.Now;
            bool conversionSuccessful = DateTime.TryParse(txt, out dt);    //out為必須     //public static bool TryParse(string s, out DateTime result);
            if (conversionSuccessful == true)
                richTextBox1.Text += "得到DateTime資料： " + dt.ToString() + "\n";
            else
                richTextBox1.Text += "DateTime.TryParse 失敗\n";

            txt = "123年3月11";
            conversionSuccessful = DateTime.TryParse(txt, out dt);    //out為必須     //public static bool TryParse(string s, out DateTime result);
            if (conversionSuccessful == true)
                richTextBox1.Text += "得到DateTime資料： " + dt.ToString() + "\n";
            else
                richTextBox1.Text += "DateTime.TryParse 失敗\n";

        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

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

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }
    }

    //不重複之陣列
    public static class Extensions
    {
        private static Random Rand = new Random();

        // Randomize an array.
        public static void Randomize<T>(this T[] items)
        {
            // For each spot in the array, pick
            // a random item to swap into that spot.
            for (int i = 0; i < items.Length - 1; i++)
            {
                int j = Rand.Next(i, items.Length);
                T temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }

        public static int[] RandomArrangement(int num_items)
        {
            int[] items = Enumerable.Range(0, num_items).ToArray();
            items.Randomize();
            return items;
        }
    }

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
            if (vSpeed < 0) vSpeed = 0;		// 設定速度不得低於 0
            if (vSpeed > 200) vSpeed = 200;	// 設定速度不得高於 200
            _speed = vSpeed;
        }
    }

    class Car2   // 定義Car類別
    {
        // 宣告_speed私有變數用來存放車子的速度值
        private int _speed = 0;
        // 定義Speed速度屬性
        public int Speed
        {
            get
            {
                return _speed;  // 傳回目前的速度
            }
            set
            {
                if (value < 0) value = 0;       // 速度不可小於0
                if (value > 200) value = 200;   // 速度不可大於200
                _speed = value;                 // 設定速度
            }
        }
        // 定義Accelerate()方法，用來指定目前車子速度+1 
        public void Accelerate()
        {
            _speed++;					// 速度 + 1
            if (_speed > 200) _speed = 200;	// 檢查速度不可超過 200
        }
    }

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
            //richTextBox1.Text +=string.Format(" 身高是: {0} ", _Height);
            //richTextBox1.Text += string.Format(" 體重是: {0} \n", _Weight);
        }
    }

    class Student2
    {
        private int _Height, _Weight;
        //public Student()
        //{
        //    _Weight = 48;
        //    _Height = 160;
        // }
        // Student類別的建構式，須設定一個引數
        public Student2(int w)
        {
            _Weight = w;  		// 初始化_Weight欄位
            _Height = 160;	      	// 初始化_Height欄位的值為160
        }
        // Student類別的建構式，須設定兩個引數
        public Student2(int w, int h)
        {
            _Weight = w;
            _Height = h;
        }
        // Student類別的GetShow()方法，可顯示學生的身高和體重
        public void GetShow()
        {
            //richTextBox1.Text +=string.Format(" 身高是: {0} ", _Height);
            //richTextBox1.Text += string.Format(" 體重是: {0} \n", _Weight);
        }
    }

    class Student3
    {
        private int _Height, _Weight;
        public Student3()
        {
            //_Weight = 48;
            //_Height = 160;
        }
        // Student類別的建構式，須設定一個引數
        public Student3(int w)
        {
            _Weight = w;  		// 初始化_Weight欄位
            _Height = 160;	      	// 初始化_Height欄位的值為160
        }
        // Student類別的建構式，須設定兩個引數
        public Student3(int w, int h)
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
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

 */
