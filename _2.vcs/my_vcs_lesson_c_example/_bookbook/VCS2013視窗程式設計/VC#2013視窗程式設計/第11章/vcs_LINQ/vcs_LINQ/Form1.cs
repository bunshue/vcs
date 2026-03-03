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
                Console.Write("{0,1} ", x);
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
                Console.WriteLine(studentGroup.Key == true ? "高分組" : "低分組");
                foreach (var student in studentGroup)
                {
                    Console.WriteLine("   {0}: {1}", student.Name, student.Scores.Average());
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
                Console.WriteLine("以母音: {0} 開頭的群組", wordGroup.Key);
                foreach (var word in wordGroup)
                {
                    Console.WriteLine("   {0}", word);
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
                Console.WriteLine(el);
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
                Console.WriteLine("姓名->" + (string)el.Element(XName.Get("姓名")).Value);
                Console.WriteLine("郵遞區號->" + (string)el.Element(XName.Get("郵遞區號")).Value);
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

            Console.WriteLine(str);
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

            Console.WriteLine("位於 http://www.eTesting.com.tw 名稱空間的元素");
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
                Console.WriteLine(el.x + " 的內容是 " + el.y);
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
                Console.WriteLine(str);
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
                Console.WriteLine("分類號 = {0}", (string)ex.Attribute("分類號"));
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

            Console.WriteLine("書籍價目表，依價格排序：");
            foreach (decimal el in prices)
            {
                Console.WriteLine(el + " 元");
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
                Console.WriteLine(cost);
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
                Console.WriteLine(s.Name + ": " + s.Scores[0]);
            }


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
