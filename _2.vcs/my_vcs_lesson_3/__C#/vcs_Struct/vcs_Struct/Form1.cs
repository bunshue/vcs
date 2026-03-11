using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Struct
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

        void show_item_location()
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

            richTextBox1.Size = new Size(500, 690);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(760, 750);
            this.Text = "vcs_Struct";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // 定義Product產品結構資料型別
        struct Product
        {
            // Product產品結構內含No編號欄位、Name品名欄位、Price單價欄位
            public string No, Name;
            public int Price;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //struct用法
            // 宣告game結構變數為Product結構型別
            Product game;
            // 設定game.No編號欄位的值為 "G01"
            game.No = "G01";
            // 設定game.Name品名欄位的值為"XBox One"
            game.Name = "XBox One";
            // 設定game.Price單價欄位的值為10000
            game.Price = 10000;

            Product cookie;        // 宣告cookie結構變數為Product結構型別
            cookie.No = "A123";
            cookie.Name = "LION_MOUSE";
            cookie.Price = 1234;
            richTextBox1.Text += "====== 產品單價清單 ======\n";
            // 印出game及cookie結構的編號、品名及單價
            richTextBox1.Text += "產品編號： " + game.No + "\n";
            richTextBox1.Text += "產品名稱： " + game.Name + "\n";
            richTextBox1.Text += "產品單價： " + game.Price + "\n";
            richTextBox1.Text += "產品編號： " + cookie.No + "\n";
            richTextBox1.Text += "產品名稱： " + cookie.Name + "\n";
            richTextBox1.Text += "產品單價： " + cookie.Price + "\n";

        }

        struct circle
        {
            public float cRadius;
            public string cColor;
        }
        struct wheel
        {
            public circle circle1;
            public string usage;
        };

        private void button1_Click(object sender, EventArgs e)
        {
            //巢狀自訂型態
            wheel wheel1;
            wheel1.circle1.cRadius = 50;
            wheel1.circle1.cColor = "黑色";
            wheel1.usage = "汽車";
            richTextBox1.Text += "輪胎半徑：" + wheel1.circle1.cRadius + "\n";
            richTextBox1.Text += "輪胎顏色：" + wheel1.circle1.cColor + "\n";
            richTextBox1.Text += "輪胎用途：" + wheel1.usage + "\n";

        }

        //結構與結構陣列的用法 ST
        struct Ball  // 結構
        {
            public Point pt;
            public Color color;
        }
        Random rd = new Random(); // 亂數
        List<Ball> ballList = new List<Ball>(); // 動態陣列

        private void button2_Click(object sender, EventArgs e)
        {
            //結構與結構陣列的用法
            int i;
            //richTextBox1.Clear();
            richTextBox1.Text += "清除結構陣列\n";
            ballList.Clear();
            this.Invalidate();

            Ball aBall;

            richTextBox1.Text += "加入3個紅球\n";

            for (i = 0; i < 3; i++)
            {
                aBall.pt = new Point(rd.Next(20, this.ClientSize.Width - 20), rd.Next(40, this.ClientSize.Height - 20));
                aBall.color = Color.Red;
                ballList.Add(aBall);
                this.Invalidate();
            }

            richTextBox1.Text += "加入5個綠球\n";

            for (i = 0; i < 5; i++)
            {
                aBall.pt = new Point(rd.Next(20, this.ClientSize.Width - 20), rd.Next(40, this.ClientSize.Height - 20));
                aBall.color = Color.Green;
                ballList.Add(aBall);
                this.Invalidate();
            }

            richTextBox1.Text += "看結構陣列內所有資料\n";
            i = 0;
            foreach (Ball b in ballList)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 個, 位置 : " + b.pt.ToString() + ", 顏色 : " + b.color.ToString() + "\n";
                i++;

                //把圓球畫出來
                //e.Graphics.FillEllipse(new SolidBrush(b.color), b.pt.X - 10, b.pt.Y - 10, 20, 20);
                //e.Graphics.DrawEllipse(Pens.Black, b.pt.X - 10, b.pt.Y - 10, 20, 20);
            }
        }
        //結構與結構陣列的用法 SP

        private void button3_Click(object sender, EventArgs e)
        {
        }

        //6060

        struct person
        {
            public int age;
            public float salary;
            public string skin;
        };
        struct female
        {
            public person mary;
            public string hair;
        };

        private void button4_Click(object sender, EventArgs e)
        {
            //struct的用法

            female female1;
            female1.mary.age = 50;
            female1.mary.salary = 23000;
            female1.mary.skin = "黃色";
            female1.hair = "直髮";
            richTextBox1.Text += "年齡：" + female1.mary.age + "\n";
            richTextBox1.Text += "收入：" + female1.mary.salary + "\n";
            richTextBox1.Text += "膚色：" + female1.mary.skin + "\n";
            richTextBox1.Text += "髮型：" + female1.hair + "\n";
       }

        enum Animal { mouse, ox, tiger, rabbit, dragon, snake, horse, goat, monkey, chicken, dog, pig };
        private void button5_Click(object sender, EventArgs e)
        {
            //enum的用法

            richTextBox1.Text += "enum的用法\n";

            Animal my_animal = Animal.chicken;

            int animalNo = (int)my_animal;
            richTextBox1.Text += my_animal.ToString() + "的列舉值為 : " + animalNo + "\n";
        }

        //6060

        enum Products { HardDrive = 0, PenDrive = 4, Keyboard = 8 };

        enum ANIMAL
        {
            mouse = 1,
            cow = 2,
            tiger = 3,
            rabbit = 4,
            dragon = 5
        }

        //ENUM的用法
        // 定義WeekDays列舉內容7個成員
        // 用來表示一星期的星期日到星期六的列舉常數值
        enum WeekDays : int
        {
            Monday = 1,      	// 星期一
            Tuesday = 2,         // 星期二
            Wednesday = 3,       // 星期三
            Thursday = 4,        // 星期四
            Friday = 5,          // 星期五
            Saturday = 6,        // 星期六
            Sunday = 7           // 星期日
        };

        //默認從0開始：分別為0，1，2，3
        enum Level1
        {
            Employee,
            Manager,
            Boss,
            BigBoss,
        }

        //未指定的列舉名的值將依著最后一個指定值向后依次遞增（注意是最后一個指定值）
        //列舉中定義的可以自定義整數值
        enum Level2
        {
            Employee = 100,
            Manager,
            Boss,
            BigBoss,
        }
        //結果為100，101，102，103

        //列舉中定義的整數值可以部分預設
        enum Level3
        {
            Employee = 100,
            Manager,
            Boss = 102,
            BigBoss,
        }
        //Manager自動為101，BigBoss自動為103

        enum Level4
        {
            Employee = 100,
            Manager,
            Boss = 101,
            BigBoss,
        }
        //結果為100，101，101，102，有兩個101也是合法的
        //但不能有兩個Manager，即enum中的名稱不能重復，

        //位元位式用法

        enum Skill
        {
            Drive = 1,  //二進制  0001
            Cook = 2,  //二進制  0010
            Program = 4, //二進制  0100
            Teach = 8, //二進制  1000
        }

        class Person
        {
            public int ID { get; set; }
            public string Name { get; set; }
            public Level1 Level { get; set; }
            public Skill Skill { get; set; }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //ENUM的用法
            Products prod1 = Products.HardDrive;
            Products prod2 = Products.PenDrive;
            Products prod3 = Products.Keyboard;

            richTextBox1.Text += "印出各個變數\n";
            richTextBox1.Text += prod1 + "\n";
            richTextBox1.Text += prod2 + "\n";
            richTextBox1.Text += prod3 + "\n";

            int ret = prod3.CompareTo(prod2);

            if (ret > 0)
            {
                richTextBox1.Text += prod3 + " 比 " + prod2 + " 多\n";
            }
            else if (ret < 0)
            {
                richTextBox1.Text += prod3 + " 比 " + prod2 + " 少\n";
            }
            else
            {
                richTextBox1.Text += prod3 + " 比 " + prod2 + " 等同\n";
            }


            richTextBox1.Text += "打印ENUM的內容\n";
            byte c;
            for (c = 0; c <= 8; c++)
            {
                ANIMAL a = (ANIMAL)c;
                richTextBox1.Text += a.ToString() + "\n";
            }

            richTextBox1.Text += "ENUM的用法\n";
            // 取出WeekDays.Wednesday列舉常數值之後再轉成整數
            richTextBox1.Text += "星期三列舉常數值：" + (int)WeekDays.Wednesday + "\n";
            richTextBox1.Text += "星期五列舉常數值：" + (int)WeekDays.Friday + "\n";


            //ENUM的用法




            Person person1 = new Person();
            person1.Level = Level1.Employee;

            richTextBox1.Text += "result : " + ((int)Level1.Boss).ToString() + "\n";
            //結果為2

            Person person2 = new Person();
            person2.Skill = Skill.Drive | Skill.Cook | Skill.Program | Skill.Teach; //二進制  1111，十進制的15 //結果為15

            richTextBox1.Text += "Skill : " + ((int)person2.Skill).ToString() + "\n";
            richTextBox1.Text += "Skill a : " + ((person2.Skill & Skill.Cook) > 0).ToString() + "\n";
            richTextBox1.Text += "Skill b : " + ((person2.Skill & Skill.Cook) == Skill.Cook).ToString() + "\n";

            Console.WriteLine(person2.Skill);
            Console.WriteLine((person2.Skill & Skill.Cook) > 0); //結果為True，（1111 & 0010 = 0010）
            Console.WriteLine((person2.Skill & Skill.Cook) == Skill.Cook); //結果為True
        }

        //6060

        // The enumerated type.
        private enum MealType
        {
            Breakfast,
            Brunch,
            Lunch,
            Luncheon = Lunch,
            Tiffin = Lunch,
            Tea,
            Nuncheon = Tea,
            Dinner,
            Supper
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //把ENUM的字串印出來
            // Convert values to and from strings.
            foreach (string value in Enum.GetNames(typeof(MealType)))
            {
                // Get the enumeration's value.
                MealType meal = (MealType)Enum.Parse(typeof(MealType), value);

                // Display the values.
                richTextBox1.Text += ((int)meal).ToString() + "\t" + value + "\n";
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }
    }
}
