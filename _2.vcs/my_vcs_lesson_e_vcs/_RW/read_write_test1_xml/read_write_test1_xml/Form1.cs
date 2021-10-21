using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;
using System.Xml.Linq;  //for XNamespace, XElement
using System.IO;

namespace read_write_test1_xml
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
            x_st = 15;
            y_st = 15;
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

            button16.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button19.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
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

        private void button1_Click(object sender, EventArgs e)
        {
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

        private void button2_Click(object sender, EventArgs e)
        {
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

        private void button3_Click(object sender, EventArgs e)
        {
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

        private void button4_Click(object sender, EventArgs e)
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

        private void button5_Click(object sender, EventArgs e)
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

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {
            //XElement物件預設是以序列的方式處理xml資料，可以直接根據xml資料的階層結構，透過XElement物件建立資料

            //XML Test
            XElement xmlTree1a = new XElement("Root",
                new XElement("Child1", 1),
                new XElement("Child2", 2),
                new XElement("Child3", 3),
                new XElement("Child4", 4),
                new XElement("Child5", 5),
                new XElement("Child6", 6)
                );

            richTextBox1.Text += "XML 內容\n";
            richTextBox1.Text += xmlTree1a + "\n";

            XElement xmlTree2a = new XElement("Root",
                from el in xmlTree1a.Elements()
                where ((int)el >= 3 && (int)el <= 5)
                select el
            );

            richTextBox1.Text += "XML 內容\n";
            richTextBox1.Text += xmlTree2a + "\n";

            XNamespace aw = "http://www.adventure-works.com";
            XElement xmlTree1b = new XElement(aw + "Root",
                new XElement(aw + "Child1", 1),
                new XElement(aw + "Child2", 2),
                new XElement(aw + "Child3", 3),
                new XElement(aw + "Child4", 4),
                new XElement(aw + "Child5", 5),
                new XElement(aw + "Child6", 6)
                );

            richTextBox1.Text += "XML 內容\n";
            richTextBox1.Text += xmlTree1b + "\n";

            XElement xmlTree2b = new XElement(aw + "Root",
                from el in xmlTree1b.Elements()
                where ((int)el >= 3 && (int)el <= 5)
                select el
            );

            richTextBox1.Text += "XML 內容\n";
            richTextBox1.Text += xmlTree2b + "\n";

            XElement company =
                new XElement("Company",
                new XElement("Employee",
                new XElement("ID", "001"),
                new XElement("Name", "胖虎")),
                new XElement("Employee",
                new XElement("ID", "002"),
                new XElement("Name", "小夫")
                )
                );
            richTextBox1.Text += "XML 內容\n";
            richTextBox1.Text += company.ToString() + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //建立普通XML

            //通過代碼來創建XML文檔
            //1、引用命名空間
            //2、創建XML文檔對象
            XmlDocument doc = new XmlDocument();
            //3、創建第一個行描述信息，並且添加到doc文檔中
            XmlDeclaration dec = doc.CreateXmlDeclaration("1.0", "utf-8", null);
            doc.AppendChild(dec);
            //4、創建根節點
            XmlElement books = doc.CreateElement("Books");
            //將根節點添加到文檔中
            doc.AppendChild(books);

            //5、給根節點Books創建子節點
            XmlElement book1 = doc.CreateElement("Book");
            //將book添加到根節點
            books.AppendChild(book1);
            //6、給Book1添加子節點
            XmlElement name1 = doc.CreateElement("Name");
            name1.InnerText = "三國演義";
            book1.AppendChild(name1);

            XmlElement price1 = doc.CreateElement("Price");
            price1.InnerText = "70";
            book1.AppendChild(price1);

            XmlElement des1 = doc.CreateElement("Des");
            des1.InnerText = "好看";
            book1.AppendChild(des1);

            XmlElement book2 = doc.CreateElement("Book");
            books.AppendChild(book2);


            XmlElement name2 = doc.CreateElement("Name");
            name2.InnerText = "西游記";
            book2.AppendChild(name2);

            XmlElement price2 = doc.CreateElement("Price");
            price2.InnerText = "80";
            book2.AppendChild(price2);

            XmlElement des2 = doc.CreateElement("Des");
            des2.InnerText = "還不錯";
            book2.AppendChild(des2);

            doc.Save("Books.xml");
            richTextBox1.Text += "存檔完成\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //建立帶屬性的XML

            XmlDocument doc = new XmlDocument();
            XmlDeclaration dec = doc.CreateXmlDeclaration("1.0", "utf-8", "yes");
            doc.AppendChild(dec);

            XmlElement order = doc.CreateElement("Order");
            doc.AppendChild(order);

            XmlElement customerName = doc.CreateElement("CustomerName");
            customerName.InnerText = "張三";
            order.AppendChild(customerName);

            XmlElement customerNumber = doc.CreateElement("CustomerNumber");
            customerNumber.InnerText = "1010101";
            order.AppendChild(customerNumber);


            XmlElement items = doc.CreateElement("Items");
            order.AppendChild(items);

            XmlElement orderItem1 = doc.CreateElement("OrderItem");
            //給節點添加屬性
            orderItem1.SetAttribute("Name", "單反");
            orderItem1.SetAttribute("Count", "1120");
            items.AppendChild(orderItem1);

            XmlElement orderItem2 = doc.CreateElement("OrderItem");
            //給節點添加屬性
            orderItem2.SetAttribute("Name", "書");
            orderItem2.SetAttribute("Count", "30");
            items.AppendChild(orderItem2);

            XmlElement orderItem3 = doc.CreateElement("OrderItem");
            //給節點添加屬性
            orderItem3.SetAttribute("Name", "手機");
            orderItem3.SetAttribute("Count", "2000");
            items.AppendChild(orderItem3);

            doc.Save("Order.xml");
            richTextBox1.Text += "存檔完成\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //追加XML

            //追加XML文檔
            XmlDocument doc = new XmlDocument();
            XmlElement books;
            if (File.Exists("Books.xml"))
            {
                //如果文件存在 載入XML
                doc.Load("Books.xml");
                //獲得文件的根節點
                books = doc.DocumentElement;
            }
            else
            {
                //如果文件不存在
                //創建第一行
                XmlDeclaration dec = doc.CreateXmlDeclaration("1.0", "utf-8", null);
                doc.AppendChild(dec);
                //創建跟節點
                books = doc.CreateElement("Books");
                doc.AppendChild(books);
            }
            //5、給根節點Books創建子節點
            XmlElement book1 = doc.CreateElement("Book");
            //將book添加到根節點
            books.AppendChild(book1);

            //6、給Book1添加子節點
            XmlElement name1 = doc.CreateElement("Name");
            name1.InnerText = "c#開發大全";
            book1.AppendChild(name1);

            XmlElement price1 = doc.CreateElement("Price");
            price1.InnerText = "110";
            book1.AppendChild(price1);

            XmlElement des1 = doc.CreateElement("Des");
            des1.InnerText = "看不懂";
            book1.AppendChild(des1);

            doc.Save("Books2.xml");
            richTextBox1.Text += "存檔完成\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //讀取普通XML
            XmlDocument doc = new XmlDocument();
            //載入要讀取的XML
            doc.Load("Books.xml");

            //獲得根節點
            XmlElement books = doc.DocumentElement;

            //獲得子節點 返回節點的集合
            XmlNodeList xnl = books.ChildNodes;

            foreach (XmlNode item in xnl)
            {
                richTextBox1.Text += item.InnerText + "\n";
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //讀取帶屬性的XML

            XmlDocument doc = new XmlDocument();
            doc.Load("Order.xml");
            XmlNodeList xnl = doc.SelectNodes("/Order/Items/OrderItem");
            foreach (XmlNode node in xnl)
            {
                richTextBox1.Text += node.Attributes["Name"].Value + "\n";
                richTextBox1.Text += node.Attributes["Count"].Value + "\n";
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //修改屬性的值
            XmlDocument doc = new XmlDocument();
            doc.Load("Order.xml");
            XmlNode xn = doc.SelectSingleNode("/Order/Items/OrderItem[@Name='單反']");
            xn.Attributes["Count"].Value = "2000";
            xn.Attributes["Name"].Value = "電腦";
            doc.Save("Order2.xml");
            richTextBox1.Text += "存檔完成\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //刪除XML節點
            XmlDocument doc = new XmlDocument();
            doc.Load("Order.xml");
            XmlNode xn = doc.SelectSingleNode("/Order/Items");
            xn.RemoveAll();
            doc.Save("Order3.xml");
            richTextBox1.Text += "存檔完成\n";
        }
    }
}
