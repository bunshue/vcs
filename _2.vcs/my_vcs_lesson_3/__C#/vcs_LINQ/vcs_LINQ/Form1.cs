using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml.Linq;

namespace vcs_LINQ
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
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
        }

        //語言集成查詢 (LINQ) 是 Visual Studio 2008 和 .NET Framework 3.5 版中引入的一項創新功能。
        /*
        查詢是一種從數據源檢索數據的表達式。 隨著時間的推移，人們已經為各種數據源開發了不同的語言；
        例如，用於關系數據庫的 SQL 和用於 XML 的 XQuery。 因此，開發人員不得不針對他們必須支持的每種數據源或數據格式而學習新的查詢語言。
        LINQ 通過提供一種跨數據源和數據格式使用數據的一致模型，簡化了這一情況。在 LINQ 查詢中，始終會用到對象。
        可以使用相同的編碼模式來查詢和轉換 XML 文檔、SQL 數據庫、ADO.NET 數據集、.NET 集合中的數據以及對其有 LINQ 提供程序可用的任何其他格式的數據。
        */

        private void button0_Click(object sender, EventArgs e)
        {
            //LINQ 查詢
            //1.獲取數據源
            var nums = new int[7] { 0, 1, 2, 3, 4, 5, 6 };
            richTextBox1.Text += "原資料:\n";
            foreach (var num in nums)
            {
                richTextBox1.Text += num.ToString() + " ";
            }
            richTextBox1.Text += "\n";

            //2.創建查詢
            var numQuery =
            from num in nums
            where (num % 2) == 0
            select num;

            //3.執行查詢
            richTextBox1.Text += "查詢結果:\n";
            foreach (var num in numQuery)
            {
                richTextBox1.Text += num.ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        class Student
        {
            public string Name { get; set; }
            public int Age { get; set; }
            public string City { get; set; }
            public List<int> Scores { get; set; }
        }
        class Teacher
        {
            public int Id { get; set; }
            public string Name { get; set; }
            public int Age { get; set; }
            public string City { get; set; }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //創建第一個數據源
            var students = new List<Student>()
            {
                new Student()
                {
                    Age = 23,
                    City = "廣州",
                    Name = "小C",
                    Scores = new List<int>(){85,88,83,97}
                },
                new Student()
                {
                    Age = 18,
                    City = "廣西",
                    Name = "小明",
                    Scores = new List<int>(){86,78,85,90}
                },
                new Student()
                {
                    Age = 33,
                    City = "夢裡",
                    Name = "小三",
                    Scores = new List<int>(){86,68,73,97}
                }
            };

            //創建第二個數據源
            var teachers = new List<Teacher>()
            {
                new Teacher()
                {
                    Age = 35,
                    City = "夢裡",
                    Name = "啵哆"
                },
                new Teacher()
                {
                    Age = 28,
                    City = "雲南",
                    Name = "小紅"
                },
                new Teacher()
                {
                    Age = 38,
                    City = "河南",
                    Name = "麗麗"
                }
            };

            //創建查詢
            var peopleInDreams = (from student in students
                                  where student.City == "夢裡"
                                  select student.Name)
                            .Concat(from teacher in teachers
                                    where teacher.City == "夢裡"
                                    select teacher.Name);

            //執行查詢
            foreach (var person in peopleInDreams)
            {
                richTextBox1.Text += "找到 " + person + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //將內存中的對象轉換為 XML
            //創建數據源
            var students = new List<Student>()
            {
                new Student()
                {
                    Age = 18,
                    Name = "小A",
                    Scores = new List<int>() {88,85,74,66 }
                },
                new Student()
                {
                    Age = 35,
                    Name = "小B",
                    Scores = new List<int>() {88,85,74,66 }
                },
                new Student()
                {
                    Age = 28,
                    Name = "小啥",
                    Scores = new List<int>() {88,85,74,66 }
                }
            };

            //創建查詢
            var studentsToXml = new XElement("Root",
            from student in students
            let scores = string.Join(",", student.Scores)
            select new XElement("student",
            new XElement("Name", student.Name),
            new XElement("Age", student.Age),
            new XElement("Scores", student.Scores))
            );

            //執行查詢
            //Console.WriteLine(studentsToXml);
            richTextBox1.Text += studentsToXml + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //LINQ to XML RW
            /*
            //LINQ to XML操作Xml文檔

            //.Net中的System.Xml.Linq命名空間提供了linq to xml的支持。這個命名空間中的XDocument，XElement以及XText，XAttribute提供了讀寫xml文檔的關鍵方法。
            1. 使用linq to xml寫xml：
            使用XDocument的構造函數可以構造一個Xml文檔對象；使用XElement對象可以構造一個xml節點元素，使用XAttribute構造函數可以構造元素的屬性；使用XText構造函數可以構造節點內的文本。
            */

            var xDoc = new XDocument(new XElement("root",
                new XElement("dog",
                    new XText("dog said black is a beautify color"),
                    new XAttribute("color", "black")),
                new XElement("cat"),
                new XElement("pig", "pig is great")));

            //xDoc輸出xml的encoding是系統默認編碼，對於簡體中文操作系統是gb2312
            //默認是縮進格式化的xml，而無須格式化設置
            xDoc.Save("aaaa.xml");

            //LINQ to XML read

            var query = from item in xDoc.Element("root").Elements()
                        select new
                        {
                            TypeName = item.Name,
                            Saying = item.Value,
                            Color = item.Attribute("color") == null ? (string)null : item.Attribute("color").Value
                        };

            foreach (var item in query)
            {
                Console.WriteLine("{0} 's color is {1},{0} said {2}", item.TypeName, item.Color ?? "Unknown", item.Saying ?? "nothing");
                richTextBox1.Text += item.TypeName + "\t" + item.Color + "\n";
            }
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
    }
}

