using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FILE
using System.Xml;

using System.Xml.Linq;  //for XDocument, XElement
// XElement物件預設是以序列的方式處理xml資料，可以直接根據xml資料的階層結構，透過XElement物件建立資料

namespace vcs_ReadWrite_XML1B
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
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 20;
            y_st = 20;
            dx = 240;
            dy = 460;

            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            richTextBox1.Size = new Size(800, 1000);

            x_st = 20;
            y_st = 20;
            dx = 100;
            dy = 80;
            button00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button04.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button30.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button40.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button43.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button44.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button50.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button51.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button52.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button53.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button54.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //XML操作0
        private void button00_Click(object sender, EventArgs e)
        {
            //建立XML檔案
            string filename = "aaaaa.xml";

            // XmlTextWriter 寫文件
            XmlTextWriter writeXml = new XmlTextWriter(filename, Encoding.UTF8);
            writeXml.WriteStartDocument(false);
            writeXml.WriteStartElement("NetWork");  //根結點
            writeXml.WriteComment("網絡配置信息");    //註解

            writeXml.WriteStartElement("configration");

            writeXml.WriteElementString("IpAddress", "192.168.2.168");
            writeXml.WriteElementString("Netmask", "255.255.255.0");
            writeXml.WriteElementString("Gateway", "202.103.24.68");

            writeXml.WriteEndElement();
            writeXml.WriteEndElement();

            writeXml.Flush();
            writeXml.Close();

        }

        private void button01_Click(object sender, EventArgs e)
        {
            //讀取XML檔案
            string filename = "aaaaa.xml";

            // XmlTextReader 讀文件
            XmlTextReader readerXml = new XmlTextReader(filename);
            while (readerXml.Read())
            {
                if (readerXml.NodeType == XmlNodeType.Element)
                {

                    if (readerXml.Name == "IpAddress")
                    {
                        richTextBox1.Text += readerXml.Name + " :\t" + readerXml.ReadElementString().Trim() + "\n";
                    }
                    if (readerXml.Name == "Netmask")
                    {
                        richTextBox1.Text += readerXml.Name + " :\t" + readerXml.ReadElementString().Trim() + "\n";
                    }
                    if (readerXml.Name == "Gateway")
                    {
                        richTextBox1.Text += readerXml.Name + " :\t" + readerXml.ReadElementString().Trim() + "\n";
                    }
                }
            }
        }

        private void button02_Click(object sender, EventArgs e)
        {

        }

        private void button03_Click(object sender, EventArgs e)
        {

        }

        private void button04_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //建立XML檔案
            XmlDocument doc = new XmlDocument();
            //建立根節點
            XmlElement company = doc.CreateElement("Company");
            doc.AppendChild(company);
            //建立子節點
            XmlElement department = doc.CreateElement("Department");
            department.SetAttribute("部門名稱", "技術部");//設定屬性
            department.SetAttribute("部門負責人", "余小章");//設定屬性
            //加入至company節點底下
            company.AppendChild(department);

            XmlElement members = doc.CreateElement("Members");//建立節點
            //加入至department節點底下
            department.AppendChild(members);

            XmlElement info = doc.CreateElement("Information");
            info.SetAttribute("名字", "余小章");
            info.SetAttribute("電話", "0806449");
            //加入至members節點底下
            members.AppendChild(info);
            info = doc.CreateElement("Information");
            info.SetAttribute("名字", "王大明");
            info.SetAttribute("電話", "080644978");
            //加入至members節點底下
            members.AppendChild(info);
            doc.Save("Test.xml");
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //新增XML資料
            //xml write add data

            //插入節點
            XmlDocument doc = new XmlDocument();
            doc.Load("Test.xml");
            XmlNode node = doc.SelectSingleNode("Company/Department");//選擇節點
            if (node == null)
                return;
            XmlElement main = doc.CreateElement("newPerson"); //添加person節點
            main.SetAttribute("name", "小明");
            main.SetAttribute("sex", "女");
            main.SetAttribute("age", "25");
            node.AppendChild(main);
            XmlElement sub1 = doc.CreateElement("phone");
            sub1.InnerText = "123456778";
            main.AppendChild(sub1);
            XmlElement sub2 = doc.CreateElement("address");
            sub2.InnerText = "高雄";
            main.AppendChild(sub2);
            doc.Save("Test.xml");

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //修改資料
            //取得根節點內的子節點
            XmlDocument doc = new XmlDocument();
            doc.Load("Test.xml");
            //選擇節點
            XmlNode main = doc.SelectSingleNode("Company/Department");
            if (main == null)
                return;
            //取得節點內的欄位
            XmlElement element = (XmlElement)main;
            //取得節點內的"部門名稱"內容
            string data = element.GetAttribute("部門名稱");
            //取得節點內的"部門名稱"的屬性
            XmlAttribute attribute = element.GetAttributeNode("部門名稱");
            //列舉節點內的屬性
            XmlAttributeCollection attributes = element.Attributes;
            string content = "";
            foreach (XmlAttribute item in attributes)
            {
                content += item.Name + "," + item.Value + Environment.NewLine;
                if (item.Name == "部門名稱")
                    item.Value = "胎哥部門";
                if (item.Name == "部門負責人")
                    item.Value = "胎哥郎";
            }
            doc.Save("Test.xml");
            richTextBox1.Text += content + "\n";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //remove data

            XmlDocument doc = new XmlDocument();
            doc.Load("Test.xml");
            //選擇節點
            XmlNode main = doc.SelectSingleNode("Company/Department");
            if (main == null)
                return;
            //取得節點內的欄位
            XmlElement element = (XmlElement)main;
            //刪除節點內的屬性
            element.RemoveAttribute("部門名稱");
            //刪除節點內所有的內容
            //element.RemoveAll();
            doc.Save("Test.xml");

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {
            //建立XML檔案

            XmlDocument doc = new XmlDocument();
            XmlElement name = doc.CreateElement("Name");
            name.InnerText = "Patrick Hines";
            XmlElement phone1 = doc.CreateElement("Phone");
            phone1.SetAttribute("Type", "Home");
            phone1.InnerText = "206-555-0144";
            XmlElement phone2 = doc.CreateElement("Phone");
            phone2.SetAttribute("Type", "Work");
            phone2.InnerText = "425-555-0145";
            XmlElement street1 = doc.CreateElement("Street1");
            street1.InnerText = "123 Main St";
            XmlElement city = doc.CreateElement("City");
            city.InnerText = "Mercer Island";
            XmlElement state = doc.CreateElement("State");
            state.InnerText = "WA";
            XmlElement postal = doc.CreateElement("Postal");
            postal.InnerText = "68042";
            XmlElement address = doc.CreateElement("Address");
            address.AppendChild(street1);
            address.AppendChild(city);
            address.AppendChild(state);
            address.AppendChild(postal);
            XmlElement contact = doc.CreateElement("Contact");
            contact.AppendChild(name);
            contact.AppendChild(phone1);
            contact.AppendChild(phone2);
            contact.AppendChild(address);
            XmlElement contacts = doc.CreateElement("Contacts");
            contacts.AppendChild(contact);
            doc.AppendChild(contacts);

            doc.Save("aaaaa.xml");
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //讀取XML檔案
            string filename = "aaaaa.xml";

            XmlDocument booksFromFile = new XmlDocument();
            booksFromFile.Load(filename);

        }

        private void button22_Click(object sender, EventArgs e)
        {
            //新增XML節點
            addXmlns();
        }

        public void addXmlns()
        {
            string xml = @"<?xml version=""1.0""?>
                    <kml>
                    <Document>
                    <Placemark>
                    </Placemark>
                    </Document>
                    </kml>";

            var xmldoc = new XmlDocument();

            xmldoc.LoadXml(xml);

            xmldoc.DocumentElement.SetAttribute("xmlns", "http://www.opengis.net/kml/2.2");
            xmldoc.DocumentElement.SetAttribute("xmlns:gx", "http://www.google.com/kml/ext/2.2");
            xmldoc.DocumentElement.SetAttribute("xmlns:kml", "http://www.opengis.net/kml/2.2");
            xmldoc.DocumentElement.SetAttribute("xmlns:atom", "http://www.w3.org/2005/Atom");
            xmldoc.DocumentElement.SetAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance");

            string message;
            message = xmldoc.InnerXml;

            Console.WriteLine(message); // shows the updated xml
            richTextBox1.Text += message + "\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        //XML操作3

        XmlDocument xmlDoc;

        /// <summary>
        /// 初始化xml
        /// </summary>
        public void LoadXml(string filename)
        {
            xmlDoc = new XmlDocument();
            xmlDoc.Load(filename);
        }

        /// <summary> 
        /// 向xml中新增資料 
        /// </summary> 

        public void AddElement(string FromUserName)
        {
            string filename1 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ba.xml";
            string filename2 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ba_add.xml";
            LoadXml(filename1);
            XmlNode xmldocSelect = xmlDoc.SelectSingleNode("Root");
            //查詢節點
            XmlElement el = xmlDoc.CreateElement("Person");
            //新增person節點
            el.SetAttribute("name", FromUserName);
            //新增person節點的屬性"name"
            el.SetAttribute("time", DateTime.Now.ToString());
            xmldocSelect.AppendChild(el);

            xmlDoc.Save(filename2);
        }

        //修改節點中的某個屬性
        /// <summary>
        /// 修改xml屬性
        /// </summary>
        /// <param name="FromUserName"></param>
        public void editXml(string FromUserName)
        {
            string filename1 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ba.xml";
            string filename2 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ba_edit.xml";

            LoadXml(filename1);
            XmlNodeList xnl = xmlDoc.DocumentElement.ChildNodes;
            foreach (XmlElement elementxml in xnl)
            {
                if (elementxml.Name == "Person")
                {
                    if (elementxml.Attributes["name"].Value == FromUserName)
                    {
                        elementxml.Attributes["time"].Value = DateTime.Now.ToString();
                    }
                }
            }
            xmlDoc.Save(filename2);
        }

        //刪除節點中的某個屬性
        /// <summary>
        /// 刪除xml屬性
        /// </summary>
        /// <param name="FromUserName"></param>
        public void deleteXml(string FromUserName)
        {
            string filename1 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ba.xml";
            string filename2 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ba_delete.xml";

            LoadXml(filename1);
            XmlNodeList xnl = xmlDoc.DocumentElement.ChildNodes;

            foreach (XmlElement elementxml in xnl)
            {
                if (elementxml.Name == "Person")
                {
                    if (elementxml.Attributes["name"].Value == FromUserName)
                    {
                        //elementxml.RemoveAttribute("name");//刪除單一節點資料
                        elementxml.RemoveAllAttributes();   //刪除所有節點資料
                    }
                }
            } xmlDoc.Save(filename2);
        }

        //判斷xml中是否含有這個屬性
        //判斷是否已經寫入到xml中
        public string IsExitXml(string FromUserName)
        {
            string datetime = "";
            string filename = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ba.xml";
            LoadXml(filename);
            XmlNodeList xnl = xmlDoc.DocumentElement.ChildNodes;
            foreach (XmlElement element in xnl)
            {
                if (element.Name == "Person")
                {
                    if (element.Attributes["name"].Value == FromUserName)
                    {
                        datetime = element.Attributes["time"].Value;
                    }
                }
            }
            return datetime;
        }

        private void button30_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ba.xml";
            richTextBox1.Text += "載入XML, 檔案 : " + filename + "\n";
            LoadXml(filename);
        }

        private void button31_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "向XML中新增資料 david wang\n";
            AddElement("david wang");
        }

        private void button32_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "修改XML內容 bbbbb 改時間\n";
            editXml("bbbbb");
        }

        private void button33_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "尋找節點 ccccc\n";
            string result = IsExitXml("ccccc");
            richTextBox1.Text += "找到資料 : " + result + "\n";
        }

        private void button34_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "刪除節點 ccccc\n";
            deleteXml("ccccc");
        }

        private void button40_Click(object sender, EventArgs e)
        {
            //1、建立一個XML文件
            XmlDocument doc = new XmlDocument();
            //2、建立第一行描述資訊
            XmlDeclaration dec = doc.CreateXmlDeclaration("1.0", "utf-8", null);
            //3、將建立的第一行描述資訊新增到文件中
            doc.AppendChild(dec);
            //4、給文件新增根節點
            XmlElement Books = doc.CreateElement("Books");
            doc.AppendChild(Books);
            XmlElement Book = doc.CreateElement("Book");
            Books.AppendChild(Book);
            XmlElement name = doc.CreateElement("name");
            name.InnerText = "水滸傳";
            Book.AppendChild(name);
            XmlElement author = doc.CreateElement("author");
            author.InnerText = "匿名";
            author.SetAttribute("name", "wjl");
            author.SetAttribute("count", "30");
            Book.AppendChild(author);
            doc.Save("Book.xml");
            richTextBox1.Text += "儲存成功！\n";
        }

        class Student
        {
            public int id;
            public string name;
            public int age;
            public string sex;
            public Student(int id, string name, int age, string sex)
            {
                this.id = id;
                this.name = name;
                this.age = age;
                this.sex = sex;
            }
            public Student()
            {
            }
        }


        private void button41_Click(object sender, EventArgs e)
        {
            List<Student> list = new List<Student>();
            list.Add(new Student(1, "david wang", 17, "男"));
            list.Add(new Student(2, "lion mouse", 21, "男"));
            list.Add(new Student(3, "rebecca lin", 20, "女"));
            list.Add(new Student(4, "danny chang", 24, "男"));
            XmlDocument xmldoc = new XmlDocument();
            XmlDeclaration xmldec = xmldoc.CreateXmlDeclaration("1.0", "utf-8", null);
            xmldoc.AppendChild(xmldec);
            XmlElement person = xmldoc.CreateElement("Person");
            xmldoc.AppendChild(person);
            for (int i = 0; i < list.Count; i++)
            {
                XmlElement stu = xmldoc.CreateElement("student");
                stu.SetAttribute("ID", list[i].id.ToString());
                person.AppendChild(stu);
                XmlElement name = xmldoc.CreateElement("name");
                XmlElement age = xmldoc.CreateElement("age");
                name.InnerText = list[i].name;
                age.InnerText = list[i].age.ToString();
                stu.AppendChild(name);
                stu.AppendChild(age);
            }
            xmldoc.Save("Student.xml");
        }

        private void button42_Click(object sender, EventArgs e)
        {
            //對XML檔案的新增
            XmlDocument doc = new XmlDocument();
            //首先判斷檔案是否存在，如果存在則追加否則在建立一個
            if (File.Exists("Student.xml"))
            {
                //載入
                doc.Load("Student.xml");
                //獲取根節點，給根節點新增子節點
                XmlElement person = doc.DocumentElement;
                XmlElement student = doc.CreateElement("student");
                student.SetAttribute("ID", "1");
                person.AppendChild(student);
                XmlElement name = doc.CreateElement("name");
                XmlElement age = doc.CreateElement("age");
                name.InnerText = "emily li";
                age.InnerText = "22";
                student.AppendChild(name);
                student.AppendChild(age);
            }
            else
            {
            }
            doc.Save("Student2.xml");
            richTextBox1.Text += "Student2.xml 儲存成功\n";
        }

        private void button43_Click(object sender, EventArgs e)
        {

        }

        private void button44_Click(object sender, EventArgs e)
        {

        }

        private void button50_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Bb.xml";
            richTextBox1.Text += "載入XML, 檔案 : " + filename + "\n";

            if (File.Exists(filename))
            {
                XmlDocument doc = new XmlDocument();
                doc.Load(filename);

                // 獲取根節點
                XmlElement orderElement = doc.DocumentElement;
                XmlNodeList orderChildr = orderElement.ChildNodes;
                foreach (XmlNode item in orderChildr)
                {
                    Console.WriteLine("節點名稱：" + item.Name + "節點的 InnerText ：" + item.InnerText);
                    richTextBox1.Text += "節點名稱：" + item.Name + "節點的 InnerText ：" + item.InnerText + "\n";
                }
                XmlElement orderitem = orderElement["Items"];
                XmlNodeList itemlist = orderitem.ChildNodes;
                foreach (XmlNode item in itemlist)
                {
                    Console.WriteLine(item.Attributes["Name"].Value + " " + item.Attributes["Count"].Value);
                    richTextBox1.Text += item.Attributes["Name"].Value + " " + item.Attributes["Count"].Value + "\n";
                }
            }
            else
            {
                richTextBox1.Text += "檔案不存在！\n";
            }
        }

        private void button51_Click(object sender, EventArgs e)
        {
            string filename1 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Bb.xml";
            string filename2 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Bb_modify.xml";

            //使用XPath的方式來讀取XML檔案
            // 獲取文件物件
            XmlDocument doc = new XmlDocument();
            doc.Load(filename1);
            //獲取根節點
            XmlElement order = doc.DocumentElement;
            // 獲取單個節點
            //XmlNode xn = order.SelectSingleNode(@"/Order/CustomerName");
            XmlNode xn = order.SelectSingleNode(@"/Order/Items/OrderItem[@Name='巧克力']");
            xn.Attributes["Count"].Value = "10"; // 修改
            doc.Save(filename2);

            //取得資料
            //richTextBox1.Text += "value = " + xn.Attributes["Count"].Value.ToString() + "\n";
        }

        private void button52_Click(object sender, EventArgs e)
        {
            /*其他操作
            richTextBox1.Text+="刪除元素指定的特性：\n";
            xn.Attributes.RemoveNamedItem("Count"); //刪除元素指定的特性

            richTextBox1.Text+="刪除子節點：\n";
            XmlNode xn = order.SelectSingleNode(@"/Order/Items");
            XmlNode xnchild = order.SelectSingleNode(@"/Order/Items/OrderItem[@Name = '雨衣']");
            xn.RemoveChild(xnchild); //刪除指定的子節點

            richTextBox1.Text+="刪除當前所有子節點：\n";
            xn.RemoveAll(); //刪除當前節點的所有子節點

            richTextBox1.Text+="刪除當前節點的所有特性：\n";
            xnchild.Attributes.RemoveAll();　
            */
        }

        private void button53_Click(object sender, EventArgs e)
        {

        }

        private void button54_Click(object sender, EventArgs e)
        {

        }
    }
}
