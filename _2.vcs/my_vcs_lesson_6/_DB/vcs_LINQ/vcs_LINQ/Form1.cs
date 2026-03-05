using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;  // for ArrayList

using System.Data.OleDb;
using System.Xml.Linq;

using System.Data.SqlClient;	//引用System.Data.SqlClient命名空間
using System.Data.Linq;    	//參考/加入參考/.Net/System.Data.Linq
using System.Data.Linq.Mapping; //含入System.Data.Linq.Mapping

namespace vcs_LINQ
{
    public partial class Form1 : Form
    {
        //string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\{0};Integrated Security=True;Connect Timeout=30";

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

            dataGridView1.Size = new Size(620, 400);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            dataGridView2.Size = new Size(620, 400);
            dataGridView2.Location = new Point(x_st + dx * 3, y_st + dy * 6);

            richTextBox1.Size = new Size(400, 800);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1720, 910);
            this.Text = "vcs_LINQ";

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
            // Step 01. 取得資料來源
            int[] numbers = new int[7] { 0, 1, 2, 3, 4, 5, 6 };

            // Step 02. 建立查詢，
            // 其中nbrQuery是「查詢變數」，具有IEnumerable<int>資料型別
            var nbrQuery =
                from nbr in numbers
                where (nbr % 2) == 0
                select nbr;

            // Step 03. 執行查詢
            foreach (int x in nbrQuery)
            {
                richTextBox1.Text += x + "\n";
            }
        }

        public static List<Student> GetStudents()
        {
            List<Student> students = new List<Student>
            {
                new Student {Name="張無忌", ID=111, Scores= new List<int> {97, 72, 81, 60}},
                new Student {Name="令孤沖", ID=112, Scores= new List<int> {75, 84, 91, 39}},
                new Student {Name="洪七公", ID=113, Scores= new List<int> {99, 89, 91, 95}},
                new Student {Name="周芷若", ID=114, Scores= new List<int> {72, 81, 65, 84}},
                new Student {Name="黃藥師", ID=115, Scores= new List<int> {97, 89, 85, 82}} 
            };
            return students;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Step 01. 資料來源
            List<Student> students = GetStudents();

            // Step 02. 查詢運算式
            var booleanGroupQuery =
                from student in students
                group student by student.Scores.Average() >= 80;

            // Step 03. 執行查詢
            foreach (var studentGroup in booleanGroupQuery)
            {
                if (studentGroup.Key == true)
                {
                    richTextBox1.Text += "高分組\n";
                }
                else
                {
                    richTextBox1.Text += "低分組\n";
                }

                foreach (var student in studentGroup)
                {
                    richTextBox1.Text += string.Format("   {0}: {1}", student.Name, student.Scores.Average()) + "\n";
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // Step 01. 資料來源
            string[] words = {
                                "blueberry", 
                                "chimpanzee", 
                                "abacus", 
                                "banana", 
                                "apple", 
                                "cheese", 
                                "elephant", 
                                "umbrella", 
                                "anteater" 
                             };

            // Step 02. 查詢運算式
            var wordGroups =
                from w in words
                group w by w[0] into grps
                where (grps.Key == 'a' ||
                            grps.Key == 'e' ||
                            grps.Key == 'i' ||
                            grps.Key == 'o' ||
                            grps.Key == 'u')
                select grps;

            //Step 03. 執行查詢
            foreach (var wordGroup in wordGroups)
            {
                richTextBox1.Text += string.Format("以母音: {0} 開頭的群組", wordGroup.Key) + "\n";
                foreach (var word in wordGroup)
                {
                    richTextBox1.Text += string.Format("   {0}", word) + "\n";
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //LINQ to DataSet範例
            //不再銷售的產品

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"D:\Northwind.mdb";
            builder["User Id"] = "Admin";

            DataSet NorthwindDataSet;
            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            {
                string queryString = "SELECT * FROM 產品資料";
                OleDbCommand command = new OleDbCommand(builder.ConnectionString);
                connection.Open();

                // 建構DataSet及其組成分子
                NorthwindDataSet = new DataSet();
                OleDbDataAdapter myAdapter = new OleDbDataAdapter(queryString, connection);
                myAdapter.Fill(NorthwindDataSet, "產品資料Table");
            }

            DataTable products = NorthwindDataSet.Tables["產品資料Table"];

            var myQuery =
                from product in products.AsEnumerable()
                where product.Field<bool>("不再銷售") == true
                select
                    new
                    {
                        產品編號 = product.Field<int>("產品編號"),
                        產品 = product.Field<string>("產品"),
                        庫存量 = product.Field<Int16>("庫存量")
                    };

            // 秀出LINQ查詢出來的資料 
            dataGridView1.DataSource = myQuery.ToList();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"D:\Northwind.mdb";
            builder["User Id"] = "Admin";

            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            {
                string queryString = "SELECT * FROM 訂貨主檔";
                OleDbCommand command = new OleDbCommand(builder.ConnectionString);
                connection.Open();

                // 建構DataSet及其組成分子
                DataSet NorthwindDataSet = new DataSet();
                OleDbDataAdapter myAdapter = new OleDbDataAdapter(queryString, connection);
                myAdapter.Fill(NorthwindDataSet, "訂貨主檔Table");

                queryString = "SELECT * FROM 訂貨明細";
                myAdapter = new OleDbDataAdapter(queryString, connection);
                myAdapter.Fill(NorthwindDataSet, "訂貨明細Table");

                DataTable orders = NorthwindDataSet.Tables["訂貨主檔Table"];
                DataTable details = NorthwindDataSet.Tables["訂貨明細Table"];

                var query =
                    from order in orders.AsEnumerable()
                    join detail in details.AsEnumerable()
                    on order.Field<int>("訂單號碼") equals
                        detail.Field<int>("訂單號碼")
                    select new
                    {
                        訂單號碼 =
                            order.Field<int>("訂單號碼"),
                        客戶編號 =
                            order.Field<string>("客戶編號"),
                        訂單日期 =
                            order.Field<DateTime>("訂單日期"),
                        產品編號 =
                            detail.Field<int>("產品編號")
                    };

                dataGridView1.DataSource = query.ToList();
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            // 如何尋找其屬性具有特定值的特定項目
            XElement root = XElement.Load(@"c:\進貨訂單.xml");
            IEnumerable<XElement> address =
                from el in root.Elements("地址")
                where (string)el.Attribute("付款方式") == "貨到付款"
                select el;

            foreach (XElement el in address)
            {
                richTextBox1.Text += el + "\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            // 利用特定的值尋找具有子項目的特定項目。
            XElement root = XElement.Load(@"c:\進貨訂單.xml");
            IEnumerable<XElement> tests =
                from el in root.Elements("地址")
                where (string)el.Element("城市") == "屏東市"
                select el;

            foreach (XElement el in tests)
            {
                richTextBox1.Text += string.Format("姓名->" + (string)el.Element(XName.Get("姓名")).Value) + "\n";
                richTextBox1.Text += string.Format("郵遞區號->" + (string)el.Element(XName.Get("郵遞區號")).Value) + "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            XElement root = XElement.Parse(@"
            <文章>
                <段落>
                    <第一章>
                      <主題>有些文字</主題>
                    </第一章>
                    <第二節>
                      <第一段>
                        <主題>被打散到</主題>
                      </第一段>
                    </第二節>
                    <第三節>
                      <第一段>
                        <主題>多個段落</主題>
                      </第一段>
                    </第三節>
                </段落>
            </文章>");
            IEnumerable<string> textSegs =
                from seg in root.Descendants("主題")
                select (string)seg;

            string str = textSegs.Aggregate(new StringBuilder(),
                (sb, i) => sb.Append(i),
                sp => sp.ToString()
            );
            richTextBox1.Text += str + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            string markup = @"
                <moto:Root xmlns:moto='http://www.eTesting.com.tw' xmlns:john='www.onlineTesting.com.tw'>
                  <john:元素1>電子商務</john:元素1>
                  <john:元素2>企業資源規劃</john:元素2>
                  <moto:元素3>Visual C# 2013視窗程式設計</moto:元素3>
                  <john:元素4>
                    <john:子元素1>電子商務網站</john:子元素1>
                    <moto:子元素2>ASP.NET程式設計</moto:子元素2>
                  </john:元素4>
                </moto:Root>";

            XElement xmlTree = XElement.Parse(markup);

            richTextBox1.Text += string.Format("位於 http://www.eTesting.com.tw 名稱空間的元素") + "\n";
            var motoElements =
                from el in xmlTree.Descendants()
                where el.Name.Namespace == "http://www.eTesting.com.tw"
                select new
                {
                    x = (string)el.Name.LocalName,
                    y = (string)el.Value
                };

            foreach (var el in motoElements)
            {
                richTextBox1.Text += el.x + " 的內容是 " + el.y + "\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            XElement root = XElement.Parse(@"
            <根元素>  
                <元素一>
                    <內容>元素一的內容</內容>
                    <類型 值=""Yes""/>
                </元素一>
                <元素二>
                    <內容>元素二的內容</內容>
                    <類型 值=""Yes""/>
                </元素二>
                <元素三>
                    <內容>元素三的內容</內容>
                    <類型 值=""No""/>
                </元素三>
                <元素四>
                    <內容>元素四的內容</內容>
                    <類型 值=""Yes""/>
                </元素四>
                <元素五>
                    <內容>元素五的內容</內容>
                </元素五>
            </根元素>");
            var cList =
                from typeElement in root.Elements().Elements("類型")
                where (string)typeElement.Attribute("值") == "Yes"
                select (string)typeElement.Parent.Element("內容");

            foreach (string str in cList)
            {
                richTextBox1.Text += str + "\n";
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            XElement root = XElement.Parse(@"
            <根元素>
                <分類 分類號=""1""/>
                <清單>程式設計</清單>
                <Microsoft系列>
                    <分類 分類號=""2""/>
                    <notul/>
                    <分類 分類號=""3""/>
                    <清單>def</清單>
                    <分類 分類號=""4""/>
                </Microsoft系列>
                <開放源始碼系列>
                    <分類 分類號=""5""/>
                    <notul/>
                    <分類 分類號=""6""/>
                    <清單>abc</清單>
                    <分類 分類號=""7""/>
                </開放源始碼系列>
            </根元素>");

            IEnumerable<XElement> items =
                from ee in root.Descendants("分類")
                let z = ee.ElementsAfterSelf().FirstOrDefault()
                where z != null && z.Name.LocalName == "清單"
                select ee;

            foreach (XElement ex in items)
            {
                richTextBox1.Text += string.Format("分類號 = {0}", (string)ex.Attribute("分類號")) + "\n";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            XElement root = XElement.Load(@"c:\價目表.xml");
            IEnumerable<decimal> prices =
                from el in root.Elements("書")
                let price = (decimal)el.Element("訂價")
                orderby price
                select price;

            richTextBox1.Text += string.Format("書籍價目表，依價格排序：") + "\n";
            foreach (decimal el in prices)
            {
                richTextBox1.Text += el + " 元\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            XElement root = XElement.Load(@"c:\價目表.xml");
            IEnumerable<decimal> costs =
                from el in root.Elements("書")
                let total = (decimal)el.Element("庫存量") * (decimal)el.Element("訂價")
                where total >= 800
                orderby total
                select total;

            foreach (decimal cost in costs)
            {
                richTextBox1.Text += cost + "\n";
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            ArrayList arrList = new ArrayList();
            arrList.Add(
                new Student2
                {
                    Name = "張無忌",
                    ID = 111,
                    Scores = new int[] { 97, 72, 81, 60 }
                }
            );
            arrList.Add(
                new Student2
                {
                    Name = "令孤沖",
                    ID = 112,
                    Scores = new int[] { 75, 84, 91, 39 }
                }
            );
            arrList.Add(
                new Student2
                {
                    Name = "洪七公",
                    ID = 113,
                    Scores = new int[] { 99, 89, 91, 95 }
                }
            );
            arrList.Add(
                new Student2
                {
                    Name = "周芷若",
                    ID = 114,
                    Scores = new int[] { 72, 81, 65, 84 }
                }
            );
            arrList.Add(
                 new Student2
                 {
                     Name = "黃藥師",
                     ID = 115,
                     Scores = new int[] { 97, 89, 85, 82 }
                 }
             );

            var query = from Student2 student in arrList
                        where student.Scores[0] > 80
                        select student;

            foreach (Student2 s in query)
            {
                richTextBox1.Text += s.Name + ": " + s.Scores[0] + "\n";
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //查詢1
            XElement root = XElement.Load(@"D:\進貨訂單.xml");
            var tests =
                from el in root.Elements("地址")
                select new
                {
                    姓名 = (string)el.Element("姓名"),
                    街道 = (string)el.Element("街道"),
                    城市 = (string)el.Element("城市"),
                    郵遞區號 = (string)el.Element("郵遞區號")
                };

            dataGridView1.DataSource = tests.ToList();
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //查詢2
            // 利用特定的值尋找具有子項目的特定項目。
            string city_name = "桃園市";
            XElement root = XElement.Load(@"D:\進貨訂單.xml");
            var tests =
                from el in root.Elements("地址")
                where (string)el.Element("城市") == city_name
                select new
                {
                    姓名 = (string)el.Element("姓名"),
                    城市 = (string)el.Element("城市"),
                    郵遞區號 = (string)el.Element("郵遞區號")
                };

            dataGridView1.DataSource = tests.ToList();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //SQL

            joinDemonstration app = new joinDemonstration();
            //app.InnerJoin();                // 內部等聯結
            //app.GroupJoin1();
            //app.GroupJoin2();
            app.GroupInnerJoin();

            //app.LeftOuterJoin1();
            //app.LeftOuterJoin2();

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
            //Employee1

            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;" +
                    @"AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch20DB.mdf;" +
                    "Integrated Security=True";
                DataContext dc = new DataContext(cn);
                Table<Employee1> emp = dc.GetTable<Employee1>();
                var result = from p in emp
                             select new { p.姓名, p.編號, p.職稱, p.電話, p.薪資 };
                dataGridView1.DataSource = result;
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //Employee2
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;" +
                    @"AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch20DB.mdf;" +
                            "Integrated Security=True";
                DataContext dc = new DataContext(cn);
                Table<Employee2> emp = dc.GetTable<Employee2>();
                var result = from p in emp
                             select new { p.員工編號, p.員工姓名, p.職位, p.聯絡電話, p.月薪 };
                dataGridView1.DataSource = result;
            }
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

    public class Student
    {
        public string Name { get; set; }
        public int ID { get; set; }
        public List<int> Scores;
    }

    public class Student2
    {
        public string Name { get; set; }
        public int ID { get; set; }
        public int[] Scores { get; set; }
    }


    [Table(Name = "員工")]   	// Employee類別對應員工資料表
    class Employee1
    {
        [Column]  		// 編號屬性對應至員工資料表的編號欄位
        public int 編號 { get; set; }
        [Column]  		// 姓名屬性對應至員工資料表的姓名欄位
        public string 姓名 { get; set; }
        [Column]  		// 職稱屬性對應至員工資料表的職稱欄位
        public string 職稱 { get; set; }
        [Column]  		// 電話屬性對應至員工資料表的電話欄位
        public string 電話 { get; set; }
        [Column]  		// 薪資屬性對應至員工資料表的薪資欄位
        public int 薪資 { get; set; }
    }


    [Table(Name = "員工")]
    class Employee2
    {
        [Column(Name = "編號")]	// 將員工編號屬性對應至員工資料表的編號欄位
        public int 員工編號 { get; set; }
        [Column(Name = "姓名")]	// 將員工姓名屬性對應至員工資料表的姓名欄位
        public string 員工姓名 { get; set; }
        [Column(Name = "職稱")]	// 將職位屬性對應至員工資料表的職稱欄位
        public string 職位 { get; set; }
        [Column(Name = "電話")]	// 將聯絡電話屬性對應至員工資料表的電話欄位
        public string 聯絡電話 { get; set; }
        [Column(Name = "薪資")]	// 將月薪屬性對應至員工資料表的薪資欄位
        public int 月薪 { get; set; }
    }

    class Product
    {
        public string Name { get; set; }
        public int CategoryID { get; set; }
    }

    class Category
    {
        public string Name { get; set; }
        public int ID { get; set; }
    }

    class joinDemonstration
    {
        // 建構第一組資料來源
        List<Category> categories = new List<Category>()
            { 
                new Category()  {Name="飲料",   ID=001},
                new Category()  {Name="佐料",   ID=002},
                new Category()  {Name="蔬菜",   ID=003},
                new Category()  {Name="穀類",   ID=004},
                new Category()  {Name="水果",   ID=005}            
            };

        // 建構第二組資料來源
        List<Product> products = new List<Product>()
            {
                new Product {Name="可樂",   CategoryID=001},
                new Product {Name="茶品",   CategoryID=001},
                new Product {Name="芥末",   CategoryID=002},
                new Product {Name="泡菜",   CategoryID=002},
                new Product {Name="蘿蔔",   CategoryID=003},
                new Product {Name="白菜",   CategoryID=003},
                new Product {Name="桃子",   CategoryID=005},
                new Product {Name="甜瓜",   CategoryID=005},
            };

        public void InnerJoin()
        {
            var innerJoinQuery =
               from category in categories
               join prod in products on category.ID equals prod.CategoryID
               select new { Category = category.ID, Product = prod.Name };

            Console.Write("*** 內部聯結：");
            Console.WriteLine("查詢運算結果->{0} 項目位於1個群組中。", innerJoinQuery.Count());
            Console.WriteLine("{0,-8}{1}", "品名", "種類");

            foreach (var item in innerJoinQuery)
            {
                Console.WriteLine("{0,-10}{1}", item.Product, item.Category);
            }
        }

        public void GroupJoin1()
        {
            var groupJoinQuery =
               from category in categories
               join prod in products on category.ID equals prod.CategoryID into prodGroup
               select prodGroup;

            int totalItems = 0;
            Console.WriteLine("*** 群組聯結：");
            Console.WriteLine("   {0,-8}{1}", "品名", "種類");

            foreach (var prodGrouping in groupJoinQuery)
            {
                Console.WriteLine("群組：");
                foreach (var item in prodGrouping)
                {
                    totalItems++;
                    Console.WriteLine("   {0,-10}{1}", item.Name, item.CategoryID);
                }
            }

            Console.WriteLine("查詢運算結果->Unshaped GroupJoin: {0} 項目位於 {1} 個未具名的群組中", totalItems, groupJoinQuery.Count());
        }

        public void GroupJoin2()
        {
            var groupJoinQuery =
                from category in categories
                join product in products on category.ID equals product.CategoryID into prodGroup
                from prod in prodGroup
                orderby prod.CategoryID
                select new { Category = prod.CategoryID, ProductName = prod.Name };

            int totalItems = 0;
            Console.WriteLine("*** 群組聯結：");
            Console.WriteLine("   {0,-8}{1}", "品名", "種類");

            foreach (var item in groupJoinQuery)
            {
                totalItems++;
                Console.WriteLine("   {0,-10}{1}", item.ProductName, item.Category);
            }
            Console.WriteLine("查詢運算結果-> {0} 項目位於1個群組中", totalItems, groupJoinQuery.Count());
        }

        public void GroupInnerJoin()
        {
            var groupJoinQuery =
                from category in categories
                orderby category.ID
                join prod in products on category.ID equals prod.CategoryID into prodGroup
                select new
                {
                    Category = category.Name,
                    Products = from prod2 in prodGroup
                               orderby prod2.Name
                               select prod2
                };

            int totalItems = 0;
            Console.WriteLine("*** 群組/內部聯結：");
            Console.WriteLine("  {0,-8}{1}", "品名", "種類");

            foreach (var productGroup in groupJoinQuery)
            {
                Console.WriteLine(productGroup.Category);
                foreach (var prodItem in productGroup.Products)
                {
                    totalItems++;
                    Console.WriteLine("  {0,-10} {1}", prodItem.Name, prodItem.CategoryID);
                }
            }

            Console.WriteLine("查詢運算結果-> {0} 項目位於 {1} 個具名的群組中", totalItems, groupJoinQuery.Count());
        }

        public void LeftOuterJoin1()
        {
            var leftOuterQuery =
               from category in categories
               join prod in products on category.ID equals prod.CategoryID into prodGroup
               select prodGroup.DefaultIfEmpty(
                    new Product() { Name = "左側來源無相符項目 !", CategoryID = category.ID });

            int totalItems = 0;
            Console.WriteLine("左外部聯結：");

            foreach (var prodGrouping in leftOuterQuery)
            {
                Console.WriteLine("群組：", prodGrouping.Count());
                Console.WriteLine("  {0,-8}{1}", "品名", "種類");

                foreach (var item in prodGrouping)
                {
                    totalItems++;
                    Console.WriteLine("  {0,-10}{1}", item.Name, item.CategoryID);
                }
            }
            Console.WriteLine("查詢運算結果-> {0} 項目位於 in {1} 個群組中", totalItems, leftOuterQuery.Count());
        }

        public void LeftOuterJoin2()
        {
            var leftOuterQuery =
               from category in categories
               join prod in products on category.ID equals prod.CategoryID into prodGroup
               from item in prodGroup.DefaultIfEmpty()
               select new
               {
                   Name = item == null ?
                   "左側來源無相符項目 !" :
                   item.Name,
                   CategoryID = category.ID
               };

            int totalItems = 0;
            Console.WriteLine("左外部聯結：");
            Console.WriteLine("{0,-23}{1}", "品名", "種類");

            foreach (var item in leftOuterQuery)
            {
                totalItems++;
                Console.WriteLine("{0,-23}{1}", item.Name, item.CategoryID);
            }
            Console.WriteLine("查詢運算結果-> {0} 項目位於1個群組中", totalItems);
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
