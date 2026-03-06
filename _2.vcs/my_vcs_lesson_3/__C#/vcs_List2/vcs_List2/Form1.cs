using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;

namespace vcs_List2
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

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1070, 750);
            this.Text = "vcs_List2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //類別List
            List<Person> persons1 = new List<Person>();
            persons1.Add(new Person("张三", "男", 20, 1500));
            persons1.Add(new Person("王成", "男", 32, 3200));
            persons1.Add(new Person("李丽", "女", 19, 1700));
            persons1.Add(new Person("何英", "女", 35, 3600));
            persons1.Add(new Person("何英", "女", 18, 1600));

            //Console.WriteLine("泛型分组如下：");
            richTextBox1.Text += "泛型分组如下：\n";

            var ls = persons1.GroupBy(a => a.Sex).Select(g => (new { sex = g.Key, count = g.Count(), ageC = g.Sum(item => item.Age), moneyC = g.Sum(item => item.Money) }));
            foreach (var item in ls)
            {
                //Console.WriteLine(item.sex + "  " + item.count + "  " + item.ageC + "   " + item.moneyC);
                richTextBox1.Text += item.sex + "  " + item.count + "  " + item.ageC + "   " + item.moneyC + "\n";
            }

            //3030

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //類別List

            List<Member> m = new List<Member>();   // 泛型           

            m.Add(new Member() { Name = "David", Select = true, Score = 70 });
            m.Add(new Member() { Name = "Mary", Select = false, Score = 65 });
            m.Add(new Member() { Name = "Tom", Select = true, Score = 85 });
            m.Add(new Member() { Name = "Jack", Select = true, Score = 95 });

            Console.WriteLine(" === 泛型 LIst 操作不需強制轉換 .... \n");
            foreach (var item in m)
            {
                Console.WriteLine("姓名:{0} \t 選課:{1} \t 成績:{2} \n ", item.Name, item.Select ? "是" : "否", item.Score.ToString());
                // Console.WriteLine(item.ToString());  // 執行此行 會呼叫覆寫覆類別 ToString()方法
            }
            Console.Read();
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

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
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

        public static void PrintOut1(IEnumerable tempmySL)
        {
            Console.WriteLine("\t對應鍵(Key) \t   對應值(Value)");
            foreach (DictionaryEntry de in tempmySL)
            {
                Console.WriteLine("\t {0}  \t\t{1}", de.Key, de.Value);
            }
        }

        public static void PrintOut2(SortedList myList)
        {
            Console.WriteLine("\t對應鍵(Key) \t   對應值(Value)");
            for (int i = 0; i < myList.Count; i++)
            {
                Console.WriteLine("\t {0}  \t\t{1}", myList.GetKey(i), myList.GetByIndex(i));
                // GetKey(i):取得 SortedList 物件中指定之索引處的索引鍵。
                // GetByIndex(i):取得 SortedList 物件中指定之索引處的值。
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //SortedList 0
            SortedList mySL = new SortedList(); //建立myHT為屬於Hashtable實體

            Console.WriteLine("\n1.置入四筆Key&Value鍵值到SortedList串列內.");
            mySL["iPhone5S"] = 22000;  //添加 key&value鍵值對
            mySL["iPhone5C"] = 18000;  //添加 key&value鍵值對
            mySL["iPad2"] = 12500;     //添加 key&value鍵值對
            mySL["iPad Mini"] = 15900;  //添加 key&value鍵值對

            PrintOut1(mySL);
            Console.WriteLine(" 1.目前 SortedList串列內元素總個數 : {0}", mySL.Count);
            Console.WriteLine(" ---------------------------------------");

            // 查詢產品單價
            Console.Write(" 2.請輸入Apple產品名稱 : ");
            string item = Console.ReadLine();
            if (!mySL.ContainsKey(item))//判斷SortedList是否含特定鍵
            {
                Console.WriteLine(" 2. {0} 不存在 !!", item);
            }
            else
            {
                Console.WriteLine(" 2.{0}單價 : {1}", item, mySL[item]);
            }
            Console.WriteLine(" --------------------------------------");

            // 移除剛查詢的 Key & Value 鍵值對
            Console.WriteLine(" 3.移除剛查詢鍵值 {0}", item);
            mySL.Remove(item);
            PrintOut2(mySL);
            Console.WriteLine(" 3.目前 SortedList串列內元素總個數 : {0}", mySL.Count);
            Console.WriteLine(" ---------------------------------------");

            //移除所有元素
            Console.WriteLine(" 4.移除 SortedList串列內所有元素");
            mySL.Clear();
            Console.WriteLine(" 4.目前 SortedList串列內元素總個數 : {0}", mySL.Count);
            Console.WriteLine(" --------------------------------------");
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //SortedList 1
            SortedList m = new SortedList();  // 非泛型

            m.Add("David", new Member1() { Name = "David", Select = true, Score = 70 });
            m.Add("Mary", new Member1() { Name = "Mary", Select = false, Score = 65 });
            m.Add("Tom", new Member1() { Name = "Tom", Select = true, Score = 85 });
            m.Add("Jack", new Member1() { Name = "Jack", Select = true, Score = 95 });

            //非泛型操作
            Console.WriteLine("=== 非泛型 SortedList 操作需強制轉換 .... \n");
            foreach (DictionaryEntry item in m)
            {
                Console.WriteLine(((Member1)item.Value).ToString());
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //SortedList 2
            SortedList<string, Member2> m = new SortedList<string, Member2>();

            m.Add("David", new Member2() { Name = "David", Select = true, Score = 70 });
            m.Add("Mary", new Member2() { Name = "Mary", Select = false, Score = 65 });
            m.Add("Tom", new Member2() { Name = "Tom", Select = true, Score = 85 });
            m.Add("Jack", new Member2() { Name = "Jack", Select = true, Score = 95 });

            //泛型陣列操作
            Console.WriteLine("=== 泛型 SortedList 操作不需強制轉換 .... \n");
            foreach (KeyValuePair<string, Member2> item in m)
            {
                // Console.WriteLine (" 姓名:{0} \t 選課:{1}  \t  成績:{2}  \n" ,item.Key, item.Value.Select, item.Value.Score );
                Console.WriteLine(item.Value.ToString());
            }
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

    public class Person
    {
        public string Name { get; set; }
        public int Age { get; private set; }
        public string Sex { get; set; }
        public int Money { get; set; }

        public Person(string name, string sex, int age, int money)
        {
            Name = name;
            Age = age;
            Sex = sex;
            Money = money;
        }
    }

    class Member
    {
        public string Name { get; set; }      // 姓名屬性          
        public bool Select { get; set; }      // 選課屬性
        public int Score { get; set; }        // 成績屬性

        //public override string ToString()    // 覆寫覆類別 ToString()方法
        // {
        //   return string.Format("姓名 : {0} \t 選課 :{1} \t 成績: {2} \n ", Name, Select ? "是" : "否", Score.ToString());
        //}
    }

    class Member1
    {
        public string Name { get; set; }      // 姓名屬性          
        public bool Select { get; set; }      // 選課屬性
        public int Score { get; set; }        // 成績屬性  

        public override string ToString()    // 覆寫覆類別 ToString()方法
        {
            return string.Format("姓名 : {0} \t 選課 :{1} \t 成績: {2} \n ", Name, Select ? "是" : "否", Score.ToString());
        }
    }

    class Member2
    {
        public string Name { get; set; }      // 姓名屬性          
        public bool Select { get; set; }      // 選課屬性
        public int Score { get; set; }        // 成績屬性

        public override string ToString()    // 覆寫覆類別 ToString()方法
        {
            return string.Format("姓名 : {0} \t 選課 :{1} \t 成績: {2} \n ", Name, Select ? "是" : "否", Score.ToString());
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
