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
using System.Reflection;  // for Assembly

//方案總管/右鍵/加入/類別/預設Class1.cs改成MyClass.cs

//方案總管/右鍵/加入/Windows Form/預設Form2.cs改成MyForm.cs
//方案總管 點選MyForm.Designer.cs 刪除之
//修改MyForm.cs

//新增/加入 類別檔案 故意讓檔名,namespace,類別不一樣
//方案總管/右鍵/現有項目 選取Class1.cs

/*
方案總管 / 右鍵 / 加入 / 新增項目 選 類別
把 Class1.cs 改成 MyClass.cs
*/

using MyClass;    // MyClass.cs之namespace不一樣, 要引用, 檔名是不重要的, 加入專案就好, namespace才是重要的

//類別範例

/*
1. 建立類別物件
2. 設定類別屬性
3. 呼叫類別方法
*/

namespace vcs_Class1
{
    public partial class Form1 : Form
    {
        TimerAlarm timeAlarm = new TimerAlarm();

        class ClassExample
        {
            // 建構式
            public ClassExample()
            {
                Console.WriteLine("建立一個ClassExample的物件");
            }

            //解構式
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

            public string LastName { get; set; }  // 有get有set簡寫, 可讀可寫

            public ClassPrintDataExample(string firstName, string lastName, Form1 f1)
            {
                FirstName = firstName;
                LastName = lastName;
                this.form1 = f1;
                f1.richTextBox1.Text += "ClassPrintDataExample初始化，從Class印出, FirstName = " + firstName + ", LastName = " + lastName + "\n";
            }

            public void do_something()
            {
                this.form1.richTextBox1.Text += "從Class內印出資料到RichTextBox\n";
                this.form1.richTextBox1.Text += "資料是 : " + FirstName + " " + LastName + "\n";

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

            groupBox8.Size = new Size(W, H + 50);
            groupBox1.Size = new Size(W, H);

            //大的groupBox
            W = 200;
            H = 300;
            groupBox14.Size = new Size(W * 2 + 80, H + 150);
            groupBox0.Size = new Size(W * 2 + 10, H * 2 + 90);

            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = 180 + 10;
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            groupBox8.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox14.Location = new Point(x_st + dx * 2, y_st + dy * 1 + 50);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 4+200, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            dx = 180 + 10;
            dy = 60 + 10;

            button7.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button19.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button26.Location = new Point(x_st + dx * 0, y_st + dy * 2);

            W = 305 * 2 / 3;
            H = 400 * 2 / 3;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 10);
            pictureBox1.Location = new Point(x_st + dx * 0 + 70 + 50, y_st + dy * 0 + 70);
            pictureBox2.Location = new Point(x_st + dx * 0 + 140 + 100, y_st + dy * 0 + 140);

            dx = 190 + 10;
            dy = 60 + 6;
            bt_class00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_class01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_class02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_class03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_class04.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_class05.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_class06.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_class07.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            bt_class08.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            bt_class09.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            bt_class10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_class11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_class12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_class13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            bt_class14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            bt_class15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_class16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            bt_class17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            bt_class18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            bt_class19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            this.Size = new Size(1480, 750);
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

        //Sale範例 ST

        //類別的定義在 MyClass.cs

        //類別Sale做成的物件一維陣列 SaleList
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

        //------------------------------------------------------------  # 60個

        private void button26_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "繼承範例\n";
            richTextBox1.Text += "Human 和 Cats 都是繼承Animal\n";

            //寵物範例2
            richTextBox1.Text += "初始化 Human\n";
            Human myself = new Human("小李", "亞洲人", 64, 172);

            richTextBox1.Text += "初始化 Cats\n";
            Cats mypet = new Cats("喵仔", "暹邏貓", 7, 30, 20);

            myself.setpet(mypet);

            myself.ShowMsg444();  // 顯示訊息在Console

            richTextBox1.Text += "主人資訊 : " + myself.GetMsg444() + "\n";

            richTextBox1.Text += "類型為 : " + myself.gettype() + "\n";

            myself.getpet().ShowMsg444();  // 顯示訊息在Console

            mypet.print_length();

            richTextBox1.Text += "他的寵物是 : " + myself.getpet().GetMsg444() + "\n";
            richTextBox1.Text += "寵物資訊 : " + mypet.show_length() + "\n";
        }

        //繼承範例 SP

        //------------------------------------------------------------  # 60個

        void test_picture_class()
        {
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = new Bitmap(filename2);

            Color2Gray c2g = new Color2Gray(bitmap1);  // 宣告一個物件, 同時設定初始值, 寫在 bitmap1裏

            pictureBox0.Image = c2g.bitmap1;  // 取出c2g物件內的資料bitmap1

            c2g.do_Color2Gray();  // 呼叫類別方法
            pictureBox1.Image = c2g.bitmap2;  // 取出c2g物件內的資料bitmap2

            c2g.do_Draw();  // 呼叫類別方法
            pictureBox2.Image = c2g.bitmap3;  // 取出c2g物件內的資料bitmap3
        }

        //------------------------------------------------------------  # 60個

        //建立 AnimalB 類別
        public class AnimalB
        {
            //4個參數都是可讀可寫
            public int number;
            public string type;
            public string name;
            public string recorder = "狗";  //  預設值

            //參數可讀可寫
            public string nickname
            {
                get
                {
                    return name;
                }

                set
                {
                    recorder = value;
                    Console.WriteLine("I am " + value);
                }
            }

            //類別內取出資料的方法 override string ToString()
            public override string ToString()
            {
                return string.Format("[{0}: {1} - {2} - {3} - {4}]", number, type, name, recorder, nickname);
            }
        }

        private void bt_class00_Click(object sender, EventArgs e)
        {
            //簡易的類別使用

            // 實例化AnimalB類別, 建立物件, 修改屬性, 使用方法, 2種寫法

            AnimalB dog1 = new AnimalB();
            dog1.number = 1;
            dog1.type = "Poodle";  // 貴賓犬
            dog1.name = "Peter";
            dog1.nickname = "貴賓犬";
            richTextBox1.Text += "取出名稱 : " + dog1.nickname + "\n";
            richTextBox1.Text += "取出參數 : " + dog1.recorder + "\n";
            richTextBox1.Text += dog1.ToString() + "\n";

            AnimalB dog2 = new AnimalB()
            {
                number = 2,
                type = "Maltese",  // 馬爾濟斯
                name = "Mary",
                nickname = "馬爾濟斯",
            };
            richTextBox1.Text += "取出名稱 : " + dog2.nickname + "\n";
            richTextBox1.Text += "取出參數 : " + dog2.recorder + "\n";
            richTextBox1.Text += dog2.ToString() + "\n";

            //------------------------------------------------------------  # 60個



        }

        //------------------------------------------------------------  # 60個

        private void bt_class01_Click(object sender, EventArgs e)
        {
            //圖形範例

            richTextBox1.Text += "新增一個Circle物件, 沒給參數, 使用預設值\n";
            Circle c0 = new Circle();
            richTextBox1.Text += "圓c0的半徑 = " + c0.getRadius() + "\t" + "圓c0的面積 = " + c0.getArea() + "\n";
            //圓c0的半徑 = 2	圓c0的面積 = 12.5663706143592

            richTextBox1.Text += "新增一個Circle物件, 給定參數5\n";
            Circle c1 = new Circle(5);
            richTextBox1.Text += "圓c1的半徑 = " + c1.getRadius() + "\t" + "圓c1的面積 = " + c1.getArea() + "\n";
            //圓c1的半徑 = 2	圓c1的面積 = 12.5663706143592

            // Cylinder 繼承 Circle
            richTextBox1.Text += "新增一個Cylinder物件, 給定參數5, 10\n";
            Cylinder cy1 = new Cylinder(5, 10);
            richTextBox1.Text += "圓柱體cy1的半徑 = " + cy1.getRadius() + "\t" + "圓柱體cy1的高度 = " + cy1.getLength() + "\t" + "圓柱體cy1的表面積 = " + cy1.getArea() + "\n";
            //圓柱體cy1的半徑 = 5	圓柱體cy1的高度 = 10	圓柱體cy1的表面積 = 471.238898038469

            richTextBox1.Text += c0.ToString() + "\n";
            richTextBox1.Text += c1.ToString() + "\n";
            richTextBox1.Text += cy1.ToString() + "\n";

            // 呼叫類別內的方法
            richTextBox1.Text += "GetMsg111()\n";
            richTextBox1.Text += c0.GetMsg111() + "\n";

            richTextBox1.Text += "Class 範例 PersonData2\n";

            //呼叫Circle類別的GetTotalObject靜態方法取得目前有多少個物件
            richTextBox1.Text += Circle.GetTotalObject() + "\n";

            //------------------------------------------------------------  # 60個

            //類別Circle做成的物件一維陣列 list
            List<Circle> list = new List<Circle>
            {
                new Circle {radius = 5},
                new Circle {radius = 5},
                new Circle {radius = 5},
                new Circle {radius = 5},
                new Circle {radius = 5}
            };

            list.Add(new Circle(8));

            richTextBox1.Text += "\n建立一個Circle物件一維陣列, 長度3, 並初始化\n";
            //類別Circle做成的物件一維陣列 list2
            Circle[] list2 = new Circle[]
            {
                new Circle() { radius = 10 },
                new Circle() { radius = 11 },
                new Circle() { radius = 12 },
            };

            richTextBox1.Text += "len = " + list.Count.ToString() + "\n";
            for (int i = 0; i < list.Count; i++)
            {
                //使用Class內的參數, 使用Override的ToString
                richTextBox1.Text += "i = " + i.ToString() + "\t" + list[i].radius.ToString() + "\t" + list[i].ToString() + "\n";
            }

            //呼叫Circle類別的GetTotalObject靜態方法取得目前有多少個物件
            richTextBox1.Text += Circle.GetTotalObject() + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_class02_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建構式和解構式 class ClassExample, 看輸出畫面的log, 顯示訊息在Console\n";

            //建構式
            richTextBox1.Text += "新增一個ClassExample物件\n";
            ClassExample person = new ClassExample();

            //解構式
            richTextBox1.Text += "銷毀\n";
            GC.Collect();       // Force garbage collection.
        }

        //------------------------------------------------------------  # 60個

        private void bt_class03_Click(object sender, EventArgs e)
        {
            // 進行記憶體回收工作
            GC.Collect(2, GCCollectionMode.Forced);
        }

        //------------------------------------------------------------  # 60個

        private void bt_class04_Click(object sender, EventArgs e)
        {
            //寵物範例1
            richTextBox1.Text += "初始化 Cat 1 多型1\n";
            Cat kitty = new Cat();
            kitty.name = "凱蒂";

            richTextBox1.Text += "初始化 Cat 2 多型2\n";
            Cat doraemon = new Cat("多啦A夢", "機器貓");
            doraemon.setweight(129);  // 設定為129公斤

            richTextBox1.Text += "初始化 Cat 3\n";
            Cat garfield = new Cat("加菲", "虎斑貓");
            garfield.setweight(5);  // 設定為5公斤

            richTextBox1.Text += "訊息\n";
            kitty.ShowMsg222();  // 取得訊息, 顯示在 Console
            doraemon.ShowMsg222();  // 取得訊息, 顯示在 Console
            garfield.ShowMsg222();  // 取得訊息, 顯示在 Console
            richTextBox1.Text += kitty.GetMsg222() + "\n";  // 取得資料字串
            richTextBox1.Text += doraemon.GetMsg222() + "\n";  // 取得資料字串
            richTextBox1.Text += garfield.GetMsg222() + "\n";  // 取得資料字串

            richTextBox1.Text += "進行動作\n";
            garfield.feed();  // 餵食, 體重+1
            doraemon.play();  // 遊戲, 體重-1

            richTextBox1.Text += "訊息\n";
            kitty.ShowMsg222();  // 取得訊息, 顯示在 Console
            doraemon.ShowMsg222();  // 取得訊息, 顯示在 Console
            garfield.ShowMsg222();  // 取得訊息, 顯示在 Console
            richTextBox1.Text += kitty.GetMsg222() + "\n";  // 取得資料字串
            richTextBox1.Text += doraemon.GetMsg222() + "\n";  // 取得資料字串
            richTextBox1.Text += garfield.GetMsg222() + "\n";  // 取得資料字串
        }

        //------------------------------------------------------------  # 60個

        public class StudentA           //定義StudentA類別
        {
            public string Name;        //Name姓名欄位宣告為public
            private int _Score;        //_Score成績欄位宣告為private

            // 建構式1, 無參數, 不做任何事
            public StudentA()
            {
            }

            // 建構式2, 可設定姓名
            public StudentA(string _vName)
            {
                Name = _vName;
            }

            // 建構式3, 可設定姓名和分數
            public StudentA(string _vName, int _vScore)
            {
                Name = _vName;
                Score = _vScore;
            }

            public int Score  //建立Score屬性，此屬性限制在0~100  // 有get有set, 可讀可寫
            {
                get
                {
                    return _Score;
                }
                set
                {
                    if (value > 100)
                    {
                        value = 100;   //Score屬性最大值為100
                    }
                    if (value < 0)
                    {
                        value = 0;       //Score屬性最小值為0
                    }
                    _Score = value;
                }
            }

            public void ShowMsg333()      //ShowMsg顯示姓名與成績的方法
            {
                MessageBox.Show(Name + "同學的分數是 " + Convert.ToString(Score));
            }

            public string GetMsg333()   //GetMsg傳回姓名與成績的方法
            {
                return Name + "同學的分數是 " + Convert.ToString(Score);
            }
        }

        private void bt_class05_Click(object sender, EventArgs e)
        {
            //建構式範例

            //無參數的建構式
            StudentA Anita1 = new StudentA();
            Anita1.Name = "愛妮達";
            Anita1.Score = 88;
            richTextBox1.Text += Anita1.GetMsg333() + "\n";

            //傳一個參數的建構式
            StudentA Jasper1 = new StudentA("賈思伯");
            Jasper1.Score = 77;
            richTextBox1.Text += Jasper1.GetMsg333() + "\n";

            //傳兩個參數的建構式
            StudentA Aliya1 = new StudentA("愛麗雅", 99);
            richTextBox1.Text += Aliya1.GetMsg333() + "\n";

            //------------------------------  # 30個

            //物件檢查參數
            //給錯誤參數, 讓系統自動訂正
            StudentA Jasper2 = new StudentA();
            Jasper2.Name = "賈思伯";
            Jasper2.Score = 5000;
            Jasper2.ShowMsg333();
            StudentA Anita2 = new StudentA();
            Anita2.Name = "愛妮達";
            Anita2.Score = -100;
            Anita2.ShowMsg333();

            //------------------------------  # 30個

            //使用靜態成員
            StudentA Anita3 = new StudentA("愛妮達", 100);
            StudentA Jasper3 = new StudentA("賈思伯", 56);
            StudentA Aliya3 = new StudentA("愛麗雅", 99);

            richTextBox1.Text += Anita3.GetMsg333() + "\n";
            richTextBox1.Text += Jasper3.GetMsg333() + "\n";
            richTextBox1.Text += Aliya3.GetMsg333() + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_class06_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        class PersonData4
        {
            //自動實作屬性
            public string Name { get; set; }  // 有get有set簡寫, 可讀可寫
            public byte Height { get; set; }  // 有get有set簡寫, 可讀可寫

            //定義靜態方法
            public void showInfo(PersonData4 first)
            {
                //指派屬性值做物件初始化
                first = new PersonData4() { Name = "林小明", Height = 172 };
            }

            //定義靜態方法
            public void display(ref PersonData4 second)
            {
                //指派屬性值做物件初始化
                second = new PersonData4 { Name = "江大海", Height = 168 };
            }
        }

        //------------------------------------------------------------  # 60個

        public class PersonData5
        {
            private string _FirstName;
            public string FirstName
            {
                get { return _FirstName; }
                set { _FirstName = value; }
            }

            public string LastName { get; set; }  // 有get有set簡寫, 可讀可寫

            public PersonData5(string firstName, string lastName)
            {
                FirstName = firstName;
                LastName = lastName;
            }

            //類別內取出資料的方法 override string ToString()
            public override string ToString()
            {
                return FirstName + " " + LastName;
            }
        }

        //------------------------------------------------------------  # 60個

        class PersonData6
        {
            private string firstname = "DEFAULT";  // 預設值
            private string lastname = "CAN NOT CHANGE";  // 預設值
            private int age;

            public string FirstName  // 有get有set, 可讀可寫
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

            public string LastName  // 只有get沒有set, 可讀不可寫(唯讀)
            {
                get
                {
                    return lastname;
                }
            }

            public int Age  // 有get有set, 可讀可寫, set部分可加入判斷式來對傳入的值做相對應處理
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

            public string Sex  // 有get有set簡寫, 可讀可寫
            {
                get;
                set;
            }

            public string ADDR  //get set 簡寫  可讀不可寫
            {
                get;
                private set;  // 宣告為私有變數 private, 不可寫
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_class07_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Class 範例 PersonData4\n";

            PersonData4 pData4 = new PersonData4() { Name = "王小風", Height = 176 };

            richTextBox1.Text += "By Value -> \n";
            //Passing By Value - 輸出王小風
            pData4.showInfo(pData4);

            richTextBox1.Text += "姓名 : " + pData4.Name + "\t身高 : " + pData4.Height + "\n";

            richTextBox1.Text += "By Reference -> \n";
            //Passing By Reference - 輸出江大海
            pData4.display(ref pData4);

            richTextBox1.Text += pData4.Name + "\t" + pData4.Height + "\n";
            richTextBox1.Text += "姓名 : " + pData4.Name + "\t身高 : " + pData4.Height + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "Class 範例 PersonData5, 類別陣列\n";

            richTextBox1.Text += "建立一個PersonData5物件一維陣列, 長度3\n";

            //類別PersonData5做成的物件一維陣列 pData5
            PersonData5[] pData5 = new PersonData5[3];

            richTextBox1.Text += "對第0個物件初始化\n";
            pData5[0] = new PersonData5("David", "Wang");
            richTextBox1.Text += "對第1個物件初始化\n";
            pData5[1] = new PersonData5("Jerry", "Lin");
            richTextBox1.Text += "對第2個物件初始化\n";
            pData5[2] = new PersonData5("James P.", "Sullivan");

            richTextBox1.Text += "顯示每個物件的內容\n";
            for (int i = 0; i < 3; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + "個\t" + pData5[i].ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            PersonData6 pData6 = new PersonData6();

            richTextBox1.Text += "僅宣告物件, 還沒給值, 讀FirstName, ";
            richTextBox1.Text += "firstname = " + pData6.FirstName + "\n";

            pData6.FirstName = "David";
            richTextBox1.Text += "寫firstname = " + pData6.FirstName + "\n";

            //pData6.LastName ="Wang";
            //由於LastName不可寫，因此此行會顯示readonly無法編譯
            richTextBox1.Text += "讀LastName, lastname = " + pData6.LastName + "\n";
            pData6.Age = 5;
            richTextBox1.Text += "讀Age, Age = " + pData6.Age + "\n";
            pData6.Age = 20;
            richTextBox1.Text += "讀Age, Age = " + pData6.Age + "\n";

            richTextBox1.Text += "讀Sex, Sex = " + pData6.Sex + "\n";

            pData6.Sex = "male";
            richTextBox1.Text += "讀Sex, Sex = " + pData6.Sex + "\n";
            //pData6.ADDR = "123"; ADDR不可寫，因此此行會顯示readonly無法編譯

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個            
        }

        //------------------------------------------------------------  # 60個

        private void bt_class08_Click(object sender, EventArgs e)
        {
            //使用 類別方法

            richTextBox1.AppendText("使用 類別方法 Logger\n");

            Logger.WriteLog("偵測不到PLC訊號, timeout, 清除信號, 等待使用者確認1");
            Logger.WriteLog("使用者確認, 回到原點, 開始偵測PLC訊號1");

            Logger.WriteLog("偵測不到PLC訊號, timeout, 清除信號, 等待使用者確認2");
            Logger.WriteLog("使用者確認, 回到原點, 開始偵測PLC訊號2");

            //------------------------------------------------------------  # 60個

            //使用類別的靜態方法

            //使用[類別的靜態方法], 外人可以直接使用
            string name = "david";
            uint math = 90;
            uint eng = 80;
            uint chin = 70;

            //直接以類別來呼叫靜態方法Total()、Average()
            uint score = StudentScore.Total(math, eng, chin);
            float avg = StudentScore.Average("平均分數", score);

            richTextBox1.Text += "姓名 : " + name + "\t總分 : " + score + "\t平均 : " + avg + "\n";

            //------------------------------------------------------------  # 60個

            //不重複之排列

            int N = 10;
            int[] Choices = Extensions.RandomArrangement(N);

            foreach (int i in Choices)
            {
                richTextBox1.Text += i.ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_class09_Click(object sender, EventArgs e)
        {
            //從Class內印出資料到RichTextBox

            richTextBox1.Text += "從Class內印出資料到RichTextBox\n";
            ClassPrintDataExample people = new ClassPrintDataExample("David", "Wang", this);

            people.do_something();
        }

        //------------------------------------------------------------  # 60個

        private void bt_class10_Click(object sender, EventArgs e)
        {
            //Class 新進0, 直接從類別內取出/建造資料

            //類別ClassStudent做成的物件一維陣列 students
            List<ClassStudent> students = MemberData.GetStudents();

            //類別ClassTeacher做成的物件一維陣列 teachers
            List<ClassTeacher> teachers = MemberData.GetTeachers();
        }

        //------------------------------------------------------------  # 60個

        class ClassCar       // 定義ClassCar類別
        {
            // 宣告私有變數_x, _y用來表示目前車子的X, Y座標位置
            private int _x, _y;
            // 宣告_speed為私有變數，表示該變數只能在Car類別內使用
            private int _speed = 0;  // 宣告_speed為私有變數, 預設值為0
            private int _angle = 10;  // 宣告_angle為私有變數, 預設值為10

            public int Angle  // 只有get沒有set, 可讀不可寫(唯讀)
            {
                get
                {
                    return _angle;
                }
            }

            // 宣告Speed為公開屬性
            public int Speed  // 寫入有條件, 讀出無條件
            {
                get     // get存取子可傳回屬性值
                {
                    return _speed;// 傳回屬性值
                }
                set     // set存取子可設定屬性值
                {
                    if (value < 0)
                    {
                        value = 0;// 速度不得低於 0
                    }
                    if (value > 200)
                    {
                        value = 200;// 速度不得高於 200
                    }
                    _speed = value;// 設定屬性值
                }
            }

            // 第一種加速方法
            public void Accelerate()
            {
                this.Speed++;
            }

            // 第二種加速方法
            public void Accelerate(int addSpeed)
            {
                this.Speed += addSpeed;
            }

            // 第三種加速方法
            public void Accelerate(string S)
            {
                if (S == "STOP")
                {
                    this.Speed = 0;
                }
            }

            // 定義 SetPosition 方法
            public void SetPosition(int vX, int vY)
            {
                _x = vX;
                _y = vY;
            }
        }

        private void bt_class11_Click(object sender, EventArgs e)
        {
            Car1 Benz1 = new Car1();
            Benz1.SetSpeed(500);			// 速度值超過 200
            richTextBox1.Text += "Benz1.GetSpeed() = " + Benz1.GetSpeed() + "\n";	// 顯示速度最大值200

            richTextBox1.Text += "------------------------------\n";  // 30個

            Car2 Benz2 = new Car2();
            Benz2.Speed = 199;
            richTextBox1.Text += "現在速度 : " + Benz2.Speed + "\n";
            richTextBox1.Text += "加速 ...\n";
            Benz2.Accelerate();
            richTextBox1.Text += "現在速度 : " + Benz2.Speed + "\n";
            richTextBox1.Text += "加速 ...\n";
            Benz2.Accelerate();
            richTextBox1.Text += "現在速度 : " + Benz2.Speed + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            ClassCar Benz = new ClassCar();
            Benz.SetPosition(100, 200);

            richTextBox1.Text += "現在速度 : " + Benz.Speed + "\n";

            richTextBox1.Text += "加速 ...\n";
            Benz.Accelerate();		// 執行第一種加速方法
            richTextBox1.Text += "現在速度 : " + Benz.Speed + "\n";
            richTextBox1.Text += "加速 10 ...\n";
            Benz.Accelerate(10);		// 執行第二種加速方法
            richTextBox1.Text += "現在速度 : " + Benz.Speed + "\n";
            richTextBox1.Text += "停車 ...\n";
            Benz.Accelerate("STOP");	// 執行第三種加速方法
            richTextBox1.Text += "現在速度 : " + Benz.Speed + "\n";

            Benz.Speed = 500;			// 速度值超過 200
            richTextBox1.Text += "Benz.Speed = " + Benz.Speed + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_class12_Click(object sender, EventArgs e)
        {
            //Class 範例 2 TimerAlarm

            timeAlarm = new TimerAlarm();
            timeAlarm.AlarmTime = FormatConvert.inputToSeconds("12:34:56");

            timeAlarm.Message = "AAAAAAAAA";

            if (timeAlarm.Countdown > 0)
            {
                this.timer6.Enabled = true;
            }

        }

        //------------------------------------------------------------  # 60個

        private void bt_class13_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_class14_Click(object sender, EventArgs e)
        {
            //類別的定義在 MyClass.cs

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

            Person pData = new Person(name, age, gender, date);

            richTextBox1.Text += pData.show() + "\n";
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

        private void bt_class15_Click(object sender, EventArgs e)
        {
            //Class 新進5
            //Class 範例 5

            //創建一個Bird基類數組，添加基類Bird對象，Magpie對象，Eagle對象，Penguin對象

            //類別Bird做成的物件一維陣列 birds
            Bird[] birds =
            { 
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
            IFlyable[] flys =
            {
                new Magpie(),
                new Eagle()
            };

            //遍歷一下flys數組
            foreach (IFlyable fly in flys)
            {
                fly.Fly();
            }

            //創建一個IFlyable接口數組，添加 Magpie對象，Eagle對象，Plane對象
            IFlyable[] flys2 =
            { 
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

        //建立 HDateTime 類別
        public class HDateTime
        {
            public int year;
            public int month;
            public int day;
            //public string name;
            //A class被實例化時，會立即執行建構式內容，並且可以傳入參數
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

        private void bt_class16_Click(object sender, EventArgs e)
        {
            //測試 MyDateTime 0
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

        public class PersonInfo
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

        private void bt_class17_Click(object sender, EventArgs e)
        {
            //測試 MyDateTime 1
            PersonInfo av1 = new PersonInfo();
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

        //------------------------------------------------------------  # 60個

        private void bt_class18_Click(object sender, EventArgs e)
        {
            //測試 MyDateTime 2
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

        //------------------------------------------------------------  # 60個

        private void bt_class19_Click(object sender, EventArgs e)
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

            //類別MyTime做成的物件一維陣列 tArray
            MyTime[] tArray = new MyTime[3];
            tArray[0] = new MyTime();
            tArray[0].setTime(21, 40);
            tArray[1] = new MyTime(9, 30, 50);
            tArray[2] = new MyTime(10, 30, 30);

            for (int i = 0; i < 3; i++)
            {
                richTextBox1.Text += "物件" + i + " : " + tArray[i].getTime() + "\n";
            }

            //System.GC.Collect();
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
            //字串一維陣列
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
            catch (Exception ex)
            {
                strDicPath = "C:/temp/log/";
                strPath = strDicPath + string.Format("{0:yyyy年-MM月-dd日}", DateTime.Now) + "日誌記錄.txt";
                Console.WriteLine(ex.Message);
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

    //------------------------------------------------------------  # 60個

    class StudentScore
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

    //------------------------------------------------------------  # 60個

    public class ClassStudent
    {
        public long Id { get; set; }  // 有get有set簡寫, 可讀可寫
        public string Name { get; set; }  // 有get有set簡寫, 可讀可寫
        public short Age { get; set; }  // 有get有set簡寫, 可讀可寫
        public DateTime DateOfCreation { get; set; }  // 有get有set簡寫, 可讀可寫
    }

    public class ClassTeacher
    {
        public long Id { get; set; }  // 有get有set簡寫, 可讀可寫
        public string Name { get; set; }  // 有get有set簡寫, 可讀可寫
        public int DepartmentId { get; set; }  // 有get有set簡寫, 可讀可寫
    }

    public class MemberData
    {
        public static List<ClassStudent> GetStudents()
        {
            var list = new List<ClassStudent>
            {
                new ClassStudent {Id = 1, Name = "Mary", Age = 18, DateOfCreation = DateTime.Now},
                new ClassStudent {Id = 2, Name = "Hook", Age = 16, DateOfCreation = DateTime.Now.AddDays(-1)},
                new ClassStudent {Id = 3, Name = "Jhon", Age = 15, DateOfCreation = DateTime.Now.AddDays(-2)},
                new ClassStudent {Id = 4, Name = "Alan", Age = 21, DateOfCreation = DateTime.Now.AddDays(-3)}
            };
            return list;
        }

        public static List<ClassTeacher> GetTeachers()
        {
            var list = new List<ClassTeacher>
            {
                new ClassTeacher {Id = 1, Name = "Mary", DepartmentId = 11 },
                new ClassTeacher {Id = 2, Name = "Hook", DepartmentId = 22 },
                new ClassTeacher {Id = 3, Name = "Jhon", DepartmentId = 33 },
                new ClassTeacher {Id = 4, Name = "Alan", DepartmentId = 44 }
            };
            return list;
        }
    }

    public static class ExtensionUtility
    {
        /// <summary>
        /// Converts List To DataTable
        /// </summary>
        /// <typeparam name="TSource"></typeparam>
        /// <param name="data"></param>
        /// <returns></returns>
        public static DataTable ToDataTable<TSource>(this IList<TSource> data)
        {
            DataTable dataTable = new DataTable(typeof(TSource).Name);
            PropertyInfo[] props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (PropertyInfo prop in props)
            {
                dataTable.Columns.Add(prop.Name, Nullable.GetUnderlyingType(prop.PropertyType) ?? prop.PropertyType);
            }

            foreach (TSource item in data)
            {
                var values = new object[props.Length];
                for (int i = 0; i < props.Length; i++)
                {
                    values[i] = props[i].GetValue(item, null);
                }
                dataTable.Rows.Add(values);
            }
            return dataTable;
        }

        /// <summary>
        /// Converts DataTable To List
        /// </summary>
        /// <typeparam name="TSource"></typeparam>
        /// <param name="dataTable"></param>
        /// <returns></returns>
        public static List<TSource> ToList<TSource>(this DataTable dataTable) where TSource : new()
        {
            var dataList = new List<TSource>();

            const BindingFlags flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.NonPublic;
            var objFieldNames = (from PropertyInfo aProp in typeof(TSource).GetProperties(flags)
                                 select new { Name = aProp.Name, Type = Nullable.GetUnderlyingType(aProp.PropertyType) ?? aProp.PropertyType }).ToList();
            var dataTblFieldNames = (from DataColumn aHeader in dataTable.Columns
                                     select new { Name = aHeader.ColumnName, Type = aHeader.DataType }).ToList();
            var commonFields = objFieldNames.Intersect(dataTblFieldNames).ToList();

            foreach (DataRow dataRow in dataTable.AsEnumerable().ToList())
            {
                var aTSource = new TSource();
                foreach (var aField in commonFields)
                {
                    PropertyInfo propertyInfos = aTSource.GetType().GetProperty(aField.Name);
                    var value = (dataRow[aField.Name] == DBNull.Value) ? null : dataRow[aField.Name]; //if database field is nullable
                    propertyInfos.SetValue(aTSource, value, null);
                }
                dataList.Add(aTSource);
            }
            return dataList;
        }
    }

    //------------------------------------------------------------  # 60個

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
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


