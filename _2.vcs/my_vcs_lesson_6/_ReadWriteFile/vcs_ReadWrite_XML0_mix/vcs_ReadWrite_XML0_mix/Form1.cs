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

namespace vcs_ReadWrite_XML0_mix
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

            button24.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button25.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button26.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button27.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button28.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button29.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button30.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
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

        private void button16_Click(object sender, EventArgs e)
        {
            XML_RW xmlrw = new XML_RW();
            xmlrw.ShowXml();
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //XML類 各種操作
            //xml文件存儲路徑
            string myXMLFilePath = "MyComputers.xml";

            richTextBox1.Text += "生成xml文件\n";
            GenerateXMLFile(myXMLFilePath);



            richTextBox1.Text += "遍歷xml文件的信息\n";
            GetXMLInformation(myXMLFilePath);

            richTextBox1.Text += "修改xml文件的信息\n";
            ModifyXmlInformation(myXMLFilePath);


            richTextBox1.Text += "向xml文件添加節點信息\n";
            AddXmlInformation(myXMLFilePath);
            richTextBox1.Text += "刪除指定節點信息\n";
            DeleteXmlInformation(myXMLFilePath);

            richTextBox1.Text += "done\n";

        }

        private void GenerateXMLFile(string xmlFilePath)
        {
            try
            {
                //初始化一個xml實例
                XmlDocument myXmlDoc = new XmlDocument();
                //創建xml的根節點
                XmlElement rootElement = myXmlDoc.CreateElement("Computers");
                //將根節點加入到xml文件中（AppendChild）
                myXmlDoc.AppendChild(rootElement);

                //初始化第一層的第一個子節點
                XmlElement firstLevelElement1 = myXmlDoc.CreateElement("Computer");
                //填充第一層的第一個子節點的屬性值（SetAttribute）
                firstLevelElement1.SetAttribute("ID", "11111111");
                firstLevelElement1.SetAttribute("Description", "Made in China");
                //將第一層的第一個子節點加入到根節點下
                rootElement.AppendChild(firstLevelElement1);
                //初始化第二層的第一個子節點
                XmlElement secondLevelElement11 = myXmlDoc.CreateElement("name");
                //填充第二層的第一個子節點的值（InnerText）
                secondLevelElement11.InnerText = "Lenovo";
                firstLevelElement1.AppendChild(secondLevelElement11);
                XmlElement secondLevelElement12 = myXmlDoc.CreateElement("price");
                secondLevelElement12.InnerText = "5000";
                firstLevelElement1.AppendChild(secondLevelElement12);


                XmlElement firstLevelElement2 = myXmlDoc.CreateElement("Computer");
                firstLevelElement2.SetAttribute("ID", "2222222");
                firstLevelElement2.SetAttribute("Description", "Made in USA");
                rootElement.AppendChild(firstLevelElement2);
                XmlElement secondLevelElement21 = myXmlDoc.CreateElement("name");
                secondLevelElement21.InnerText = "IBM";
                firstLevelElement2.AppendChild(secondLevelElement21);
                XmlElement secondLevelElement22 = myXmlDoc.CreateElement("price");
                secondLevelElement22.InnerText = "10000";
                firstLevelElement2.AppendChild(secondLevelElement22);

                //將xml文件保存到指定的路徑下
                myXmlDoc.Save(xmlFilePath);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.ToString() + "\n";
            }
        }

        private void GetXMLInformation(string xmlFilePath)
        {
            try
            {
                //初始化一個xml實例
                XmlDocument myXmlDoc = new XmlDocument();
                //加載xml文件（參數為xml文件的路徑）
                myXmlDoc.Load(xmlFilePath);
                //獲得第一個姓名匹配的節點（SelectSingleNode）：此xml文件的根節點
                XmlNode rootNode = myXmlDoc.SelectSingleNode("Computers");
                //分別獲得該節點的InnerXml和OuterXml信息
                string innerXmlInfo = rootNode.InnerXml.ToString();
                string outerXmlInfo = rootNode.OuterXml.ToString();
                //獲得該節點的子節點（即：該節點的第一層子節點）
                XmlNodeList firstLevelNodeList = rootNode.ChildNodes;
                foreach (XmlNode node in firstLevelNodeList)
                {
                    //獲得該節點的屬性集合
                    XmlAttributeCollection attributeCol = node.Attributes;
                    foreach (XmlAttribute attri in attributeCol)
                    {
                        //獲取屬性名稱與屬性值
                        string name = attri.Name;
                        string value = attri.Value;
                        richTextBox1.Text += name + " = " + value + "\n";
                    }

                    //判斷此節點是否還有子節點
                    if (node.HasChildNodes)
                    {
                        //獲取該節點的第一個子節點
                        XmlNode secondLevelNode1 = node.FirstChild;
                        //獲取該節點的名字
                        string name = secondLevelNode1.Name;
                        //獲取該節點的值（即：InnerText）
                        string innerText = secondLevelNode1.InnerText;
                        richTextBox1.Text += name + " = " + innerText + "\n";

                        //獲取該節點的第二個子節點（用數組下標獲取）
                        XmlNode secondLevelNode2 = node.ChildNodes[1];
                        name = secondLevelNode2.Name;
                        innerText = secondLevelNode2.InnerText;
                        richTextBox1.Text += name + " = " + innerText + "\n";
                    }
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.ToString() + "\n";
            }
        }

        private void ModifyXmlInformation(string xmlFilePath)
        {
            try
            {
                XmlDocument myXmlDoc = new XmlDocument();
                myXmlDoc.Load(xmlFilePath);
                XmlNode rootNode = myXmlDoc.FirstChild;
                XmlNodeList firstLevelNodeList = rootNode.ChildNodes;
                foreach (XmlNode node in firstLevelNodeList)
                {
                    //修改此節點的屬性值
                    if (node.Attributes["Description"].Value.Equals("Made in USA"))
                    {
                        node.Attributes["Description"].Value = "Made in HongKong";
                    }
                }
                //要想使對xml文件所做的修改生效，必須執行以下Save方法
                xmlFilePath += ".modify";
                myXmlDoc.Save(xmlFilePath);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.ToString() + "\n";
            }

        }

        private void AddXmlInformation(string xmlFilePath)
        {
            try
            {
                XmlDocument myXmlDoc = new XmlDocument();
                myXmlDoc.Load(xmlFilePath);
                //添加一個帶有屬性的節點信息
                foreach (XmlNode node in myXmlDoc.FirstChild.ChildNodes)
                {
                    XmlElement newElement = myXmlDoc.CreateElement("color");
                    newElement.InnerText = "black";
                    newElement.SetAttribute("IsMixed", "Yes");
                    node.AppendChild(newElement);
                }
                //保存更改
                xmlFilePath += ".add";
                myXmlDoc.Save(xmlFilePath);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.ToString() + "\n";
            }
        }

        private void DeleteXmlInformation(string xmlFilePath)
        {
            try
            {
                XmlDocument myXmlDoc = new XmlDocument();
                myXmlDoc.Load(xmlFilePath);
                foreach (XmlNode node in myXmlDoc.FirstChild.ChildNodes)
                {
                    //記錄該節點下的最後一個子節點（簡稱：最後子節點）
                    XmlNode lastNode = node.LastChild;
                    //刪除最後子節點下的左右子節點
                    lastNode.RemoveAll();
                    //刪除最後子節點
                    node.RemoveChild(lastNode);
                }
                //保存對xml文件所做的修改
                xmlFilePath += ".delete";
                myXmlDoc.Save(xmlFilePath);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.ToString() + "\n";
            }
        }




        private void button18_Click(object sender, EventArgs e)
        {
            //TBD
            /*
            string filename = "MyComputers.xml";
            //對xml進行操作的基本方法
            //初始化一個xml實例
            XmlDocument xml = new XmlDocument();
            //導入指定xml文件
            xml.Load(filename);
            //指定一個節點
            XmlNode root = xml.SelectSingleNode("節點名稱");
            //獲取節點下所有直接子節點
            XmlNodeList childlist = root.ChildNodes;
            //判斷該節點下是否有子節點
            //root.HasChildNodes;
            //獲取同名同級節點集合
            XmlNodeList nodelist = xml.SelectNodes("節點名稱");
            //生成一個新節點
            XmlElement node = xml.CreateElement("節點名稱");
            //將節點加到指定節點下，作為其子節點
            root.AppendChild(node);
            //將節點加到指定節點下某個子節點前
            //root.InsertBefore(node,root.ChildeNodes[i]);
            //為指定節點的新建屬性並賦值
            node.SetAttribute("id", "11111");
            //為指定節點添加子節點
            root.AppendChild(node);
            //獲取指定節點的指定屬性值
            string id = node.Attributes["id"].Value;
            //獲取指定節點中的文本
            string content = node.InnerText;
            //保存XML文件
            filename = "new_file2.xml";
            xml.Save(filename);
            */
        }

        private void button19_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "XML各種操作\n";

            richTextBox1.Text += "插入一個<book>節點\n";
            string filename1a = @"../../bookstore1.xml";
            string filename1b = @"../../bookstore1_add.xml";

            //1、往<bookstore>節點中插入一個<book>節點：
            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(filename1a);
            XmlNode root = xmlDoc.SelectSingleNode("bookstore");//查找<bookstore>
            XmlElement xe1 = xmlDoc.CreateElement("book");//創建一個<book>節點
            xe1.SetAttribute("genre", "李贊紅");//設置該節點genre屬性
            xe1.SetAttribute("ISBN", "2-3631-4");//設置該節點ISBN屬性
            XmlElement xesub1 = xmlDoc.CreateElement("title");
            xesub1.InnerText = "CS從入門到精通";//設置文本節點
            xe1.AppendChild(xesub1);//添加到<book>節點中
            XmlElement xesub2 = xmlDoc.CreateElement("author");
            xesub2.InnerText = "候捷";
            xe1.AppendChild(xesub2);
            XmlElement xesub3 = xmlDoc.CreateElement("price");
            xesub3.InnerText = "58.3";
            xe1.AppendChild(xesub3);
            root.AppendChild(xe1);//添加到<bookstore>節點中
            xmlDoc.Save(filename1b);




            string filename2a = @"../../bookstore2.xml";
            string filename2b = @"../../bookstore2_modify.xml";

            richTextBox1.Text += "修改節點\n";
            //修改節點：將genre屬性值為“李贊紅“的節點的genre值改為“update李贊紅”，將該節點的子節點<author>的文本修改為“亞勝”。

            //XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(filename2a);

            XmlNodeList nodeList = xmlDoc.SelectSingleNode("bookstore").ChildNodes;//獲取bookstore節點的所有子節點
            foreach (XmlNode xn in nodeList)//遍歷所有子節點
            {
                XmlElement xe = (XmlElement)xn;//將子節點類型轉換為XmlElement類型
                if (xe.GetAttribute("genre") == "李贊紅")//如果genre屬性值為“李贊紅”
                {
                    xe.SetAttribute("genre", "update李贊紅");//則修改該屬性為“update李贊紅”
                    XmlNodeList nls = xe.ChildNodes;//繼續獲取xe子節點的所有子節點
                    foreach (XmlNode xn1 in nls)//遍歷
                    {
                        XmlElement xe2 = (XmlElement)xn1;//轉換類型
                        if (xe2.Name == "author")//如果找到
                        {
                            xe2.InnerText = "亞勝";//則修改
                            break;//找到退出來就可以了
                        }
                    }
                    break;
                }
            }
            xmlDoc.Save(filename2b);//保存。


            string filename3a = @"../../bookstore3.xml";
            string filename3b = @"../../bookstore3_delete.xml";

            //XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(filename3a);

            richTextBox1.Text += "刪除節點\n";
            //3、刪除 <book genre="fantasy" ISBN="2-3631-4">節點的genre屬性，刪除 <book genre="update李贊紅" ISBN="2-3631-4">節點。

            XmlNodeList xnl = xmlDoc.SelectSingleNode("bookstore").ChildNodes;
            foreach (XmlNode xn in xnl)
            {
                XmlElement xe = (XmlElement)xn;

                if (xe.GetAttribute("genre") == "fantasy")
                {
                    xe.RemoveAttribute("genre");//刪除genre屬性
                }
                else if (xe.GetAttribute("genre") == "update李贊紅")
                {
                    xe.RemoveAll();//刪除該節點的全部內容
                }
            }
            xmlDoc.Save(filename3b);



            string filename4 = @"../../bookstore2.xml";

            //XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(filename4);


            richTextBox1.Text += "顯示所有數據\n";

            XmlNode xnb = xmlDoc.SelectSingleNode("bookstore");
            XmlNodeList xnlb = xnb.ChildNodes;
            foreach (XmlNode xnf in xnlb)
            {
                XmlElement xe = (XmlElement)xnf;
                Console.WriteLine(xe.GetAttribute("genre"));//顯示屬性值
                richTextBox1.Text += xe.GetAttribute("genre") + "\n";//顯示屬性值
                Console.WriteLine(xe.GetAttribute("ISBN"));
                richTextBox1.Text += xe.GetAttribute("ISBN") + "\n";
                XmlNodeList xnf1 = xe.ChildNodes;
                foreach (XmlNode xn2b in xnf1)
                {
                    Console.WriteLine(xn2b.InnerText);//顯示子節點點文本
                    richTextBox1.Text += xn2b.InnerText + "\n";  //顯示子節點點文本
                }
            }

        }

        private void button20_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_xml\school.xml";

            //將XmlDocument轉化為string函數
            //讀取普通XML
            XmlDocument doc = new XmlDocument();
            //載入要讀取的XML
            doc.Load(filename);

            //獲得根節點
            XmlElement books = doc.DocumentElement;

            //獲得子節點 返回節點的集合
            XmlNodeList xnl = books.ChildNodes;

            foreach (XmlNode item in xnl)
            {
                richTextBox1.Text += item.InnerText + "\n";
            }

            //將XmlDocument轉化為string
            string result = ConvertXmlToString(doc);
            richTextBox1.Text += "result:\n" + result + "\n";
        }

        /// <summary>  
        /// 將XmlDocument轉化為string
        /// </summary>  
        /// <param name="xmlDoc"></param>  
        /// <returns></returns>  
        public string ConvertXmlToString(XmlDocument xmlDoc)
        {
            MemoryStream stream = new MemoryStream();
            XmlTextWriter writer = new XmlTextWriter(stream, null);
            writer.Formatting = Formatting.Indented;
            xmlDoc.Save(writer);
            StreamReader sr = new StreamReader(stream, System.Text.Encoding.UTF8);
            stream.Position = 0;
            string xmlString = sr.ReadToEnd();
            sr.Close();
            stream.Close();
            return xmlString;
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //XMLHelper的使用
            //class已OK

        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        //C# XML創建和解析
        private void button23_Click(object sender, EventArgs e)
        {
            XMLApply xml = new XMLApply();
            richTextBox1.Text += "建立XML\n";
            xml.CreateXML();
        }

        private void button24_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立XML\n";

            XmlDocument xdoc = new XmlDocument();
            //所有的元素使用文檔節點(XmlDocument)創建
            XmlDeclaration xdec = xdoc.CreateXmlDeclaration("1.0", "big5", null); //xml描述
            xdoc.AppendChild(xdec); //添加描述
            XmlElement xele = xdoc.CreateElement("root"); //創建節點1
            XmlElement xele2 = xdoc.CreateElement("person"); //創建節點2
            xdoc.AppendChild(xele);  //xdoc添加節點 --根節點 
            xele.AppendChild(xele2); //在節點1(xele)下添加一個節點2(xele2)
            XmlAttribute xAttr = xdoc.CreateAttribute("id"); //創建屬性
            xAttr.Value = "123";  //屬性的值
            xele.Attributes.Append(xAttr); //把屬性插入到節點
            XmlText txt = xdoc.CreateTextNode("我是文本節點");  //創建文本
            xele2.AppendChild(txt); //把文本插入到節點

            string filename = Application.StartupPath + "\\xml_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xml";
            xdoc.Save(filename);
            richTextBox1.Text += "已存檔 : " + filename + "\n";

        }

        private void button25_Click(object sender, EventArgs e)
        {
            //XML Read
            //C#讀取XML文檔的方法
            //C#讀取XML文檔的方法

            //這裡介紹一種讀取XML文檔的方法,示例中用的是 XmlTextReader 函數,每執行 Read() 一次,讀取一行.

        }


        public void ReadConfig(string XmlConfigFile)
        {
            try
            {
                // Open an XML file
                System.Xml.XmlTextReader reader;
                reader = new System.Xml.XmlTextReader(XmlConfigFile);
                while (reader.Read())
                {
                    if ((reader.NodeType == XmlNodeType.EndElement)
                    && (reader.Name == "KSBM"))
                    {
                        break;
                    }
                    if (reader.IsStartElement("ServerPath"))
                    {
                        reader.Read();
                        //_conf.ServerPath = reader.Value;
                    }
                    else if (reader.IsStartElement("SmtpServer"))
                    {
                        reader.Read();
                        //_conf.SMTPServer = reader.Value;
                    }
                    else if (reader.IsStartElement("ConnectString"))
                    {
                        reader.Read();
                        //_conf.ConnectString = reader.Value;
                    }
                }
                //return _conf;
            }
            catch
            {
                //return _conf;
            }
            finally
            {
            }
        }
    }

    //class XML_RW
    public class XMLApply
    {
        public string fileName = "Books.xml";

        private void Start()
        {
            CreateXML();
            //UpdateXml();
            //AddXml();
            //ParseXML();
        }

        /// 
        /// 創建XML文件
        /// 
        public void CreateXML()
        {
            string filename = Application.StartupPath + "//" + fileName;

            if (!File.Exists(filename))
            {
                XmlDocument BooksXML = new XmlDocument();

                XmlElement myFavoriteBooks = BooksXML.CreateElement("MyFavoriteBooks");
                XmlElement history = BooksXML.CreateElement("History");
                history.SetAttribute("year", "2013");
                XmlElement item_empireOfQing = BooksXML.CreateElement("item");
                item_empireOfQing.SetAttribute("name", "大秦帝國");
                item_empireOfQing.SetAttribute("price", "100");
                item_empireOfQing.InnerText = "Sara";

                XmlElement item_theLastMan = BooksXML.CreateElement("item");
                item_theLastMan.SetAttribute("name", "麥田的守望者");
                item_theLastMan.SetAttribute("price", "70");
                item_theLastMan.InnerText = "Lisa";

                XmlElement item_worldHistory = BooksXML.CreateElement("item");
                item_worldHistory.SetAttribute("name", "世界歷史");
                item_worldHistory.SetAttribute("price", "40");
                item_worldHistory.InnerText = "Michael";

                XmlElement software = BooksXML.CreateElement("SOftware");
                XmlElement item_php = BooksXML.CreateElement("PHP");
                item_php.SetAttribute("name", "php");
                item_php.SetAttribute("price", "35");
                item_php.InnerText = "KD";

                history.AppendChild(item_empireOfQing);
                history.AppendChild(item_theLastMan);
                history.AppendChild(item_worldHistory);
                software.AppendChild(item_php);
                myFavoriteBooks.AppendChild(history);
                myFavoriteBooks.AppendChild(software);
                BooksXML.AppendChild(myFavoriteBooks);

                BooksXML.Save(filename);
                Console.WriteLine("已存檔 : " + filename);
            }
        }

        /// 
        /// 更新xml文件內容
        /// 
        public void UpdateXml()
        {
            string filename = Application.StartupPath + "//" + fileName;

            if (File.Exists(filename))
            {
                //create a xml reference
                XmlDocument BooksXML = new XmlDocument();
                //read exists file into BooksXML
                BooksXML.Load(filename);

                XmlNodeList nodeList = BooksXML.SelectSingleNode("MyFavoriteBooks").ChildNodes;

                foreach (XmlElement node in nodeList)
                {
                    if (node.GetAttribute("year") == "2013")
                    {
                        node.SetAttribute("year", "2014");

                        XmlNodeList subNodeList = node.ChildNodes;

                        foreach (XmlElement subNode in subNodeList)
                        {
                            subNode.InnerText += "Updated...";
                        }

                        break;
                    }
                }
                BooksXML.Save(filename);
                Console.WriteLine("已存檔 : " + filename);
            }
        }

        /// 
        /// 在現有xml文件中，增加一個節點
        /// 

        public void AddXml()
        {
            string filePath = Application.StartupPath + "//" + fileName;

            if (File.Exists(filePath))
            {
                XmlDocument BooksXML = new XmlDocument();
                BooksXML.Load(filePath);

                XmlNode root = BooksXML.SelectSingleNode("MyFavoriteBooks");
                XmlElement culture = BooksXML.CreateElement("Culture");
                culture.SetAttribute("year", "2012");

                XmlElement item_China = BooksXML.CreateElement("item");
                item_China.SetAttribute("name", "中國文化");
                item_China.SetAttribute("price", "30");
                item_China.InnerText = "rechard";

                culture.AppendChild(item_China);
                root.AppendChild(culture);
                BooksXML.AppendChild(root);
                BooksXML.Save(filePath);

                //Debug.Log("Add node success...");
            }
        }


        /// 

        /// 解析xml文件
        /// 

        public void ParseXML()
        {
            string filePath = Application.StartupPath + "//" + fileName;
            StringBuilder booksInfo = new StringBuilder("");

            XmlDocument BooksXML = new XmlDocument();
            BooksXML.Load(filePath);

            XmlNode rootNode = BooksXML.FirstChild;

            if (rootNode.Name == "MyFavoriteBooks")
            {
                XmlNodeList nodeList = rootNode.ChildNodes;

                foreach (XmlElement node in nodeList)
                {
                    booksInfo.Append(node.Name + "\n");

                    foreach (XmlElement subNode in node.SelectNodes("item"))
                    {
                        booksInfo.Append("\t " + subNode.GetAttribute("name") + "   , price:" + subNode.GetAttribute("price") + "\n");
                    }

                    booksInfo.Append("\n");
                }

                //Debug.Log(booksInfo.ToString());
            }
            else
            {
                //Debug.Log("YOU LOAD WRONG FILE....");
            }

        }
    }

    class XML_RW
    {
        string xml_filename = @"C:\______test_files\__RW\_xml\bookshop.xml";


        XmlDocument xmlDoc;
        ///<summary>
        /// 插入節點
        ///</summary>
        public void InsertNode()
        {
            xmlDoc = new XmlDocument();
            xmlDoc.Load(xml_filename); //加載xml文件

            /*從指定的字符創加載xml文件 例如：
            xmlDoc.LoadXml("(<Book bookID='B001'><BookName>jeff</BookName><price>45.6</price></Book>)");
            */
            XmlNode root = xmlDoc.SelectSingleNode("bookshop");//查找﹤bookstore﹥
            XmlElement xe1 = xmlDoc.CreateElement("book");//創建一個﹤book﹥節點

            xe1.SetAttribute("genre", "Sky_Kwolf");//設置該節點genre屬性
            xe1.SetAttribute("ISBN", "2-3631-4");//設置該節點ISBN屬性

            XmlElement xesub1 = xmlDoc.CreateElement("title");
            xesub1.InnerText = "CSS禅意花園";//設置節點的文本值
            xe1.AppendChild(xesub1);//添加到﹤book﹥節點中
            XmlElement xesub2 = xmlDoc.CreateElement("author");
            xesub2.InnerText = "Jeff";
            xe1.AppendChild(xesub2);
            XmlElement xesub3 = xmlDoc.CreateElement("price");
            xesub3.InnerText = "58.3";
            xe1.AppendChild(xesub3);

            root.AppendChild(xe1);//添加到﹤bookshop﹥節點中
            xmlDoc.Save(xml_filename); //保存其更改
        }

        ///<summary>
        /// 修改節點
        ///</summary>
        public void UpdateNode()
        {
            xmlDoc = new XmlDocument();
            xmlDoc.Load(xml_filename); //加載xml文件
            //獲取bookshop節點的所有子節點
            XmlNodeList nodeList = xmlDoc.SelectSingleNode("bookshop").ChildNodes;

            //遍歷所有子節點
            foreach (XmlNode xn in nodeList)
            {
                XmlElement xe = (XmlElement)xn; //將子節點類型轉換為XmlElement類型

                if (xe.GetAttribute("genre") == "Sky_Kwolf")//如果genre屬性值為“Sky_Kwolf”
                {
                    xe.SetAttribute("genre", "update Sky_Kwolf"); //則修改該屬性為“update Sky_Kwolf”
                    XmlNodeList nls = xe.ChildNodes;//繼續獲取xe子節點的所有子節點

                    foreach (XmlNode xn1 in nls)//遍歷
                    {
                        XmlElement xe2 = (XmlElement)xn1; //轉換類型
                        if (xe2.Name == "author")//如果找到
                        {
                            xe2.InnerText = "jason";//則修改
                            break;//找到退出
                        }
                    }
                    break;
                }
            }

            xmlDoc.Save(xml_filename);//保存。
        }

        //顯示xml數據
        public void ShowXml()
        {
            xmlDoc = new XmlDocument();
            xmlDoc.Load(xml_filename); //加載xml文件
            XmlNode xn = xmlDoc.SelectSingleNode("bookshop");

            XmlNodeList xnl = xn.ChildNodes;

            foreach (XmlNode xnf in xnl)
            {
                XmlElement xe = (XmlElement)xnf;
                Console.WriteLine(xe.GetAttribute("genre"));//顯示屬性值
                Console.WriteLine(xe.GetAttribute("ISBN"));

                XmlNodeList xnf1 = xe.ChildNodes;
                foreach (XmlNode xn2 in xnf1)
                {
                    Console.WriteLine(xn2.InnerText);//顯示子節點點文本
                }
            }
        }


        ///<summary>
        /// 刪除節點
        ///</summary>
        public void DeleteNode()
        {
            xmlDoc = new XmlDocument();
            xmlDoc.Load(xml_filename); //加載xml文件
            XmlNodeList xnl = xmlDoc.SelectSingleNode("bookshop").ChildNodes;

            foreach (XmlNode xn in xnl)
            {
                XmlElement xe = (XmlElement)xn;

                if (xe.GetAttribute("genre") == "fantasy")
                {
                    xe.RemoveAttribute("genre");//刪除genre屬性
                }
                else if (xe.GetAttribute("genre") == "update Sky_Kwolf")
                {
                    xe.RemoveAll();//刪除該節點的全部內容
                }
            }
            xmlDoc.Save(xml_filename);
        }
    }

    ///<summary>
    /// XMLHelper XML文檔操作管理器
    ///</summary>
    public class XMLHelper
    {
        public XMLHelper()
        {
            //
            // TODO: 在此處添加構造函數邏輯
            //
        }


        #region XML文檔節點查詢和讀取
        ///<summary>
        /// 選擇匹配XPath表達式的第一個節點XmlNode.
        ///</summary>
        ///<param name="xmlFileName">XML文檔完全文件名(包含物理路徑)</param>
        ///<param name="xpath">要匹配的XPath表達式(例如:"//節點名//子節點名")</param>
        ///<returns>返回XmlNode</returns>
        public static XmlNode GetXmlNodeByXpath(string xmlFileName, string xpath)
        {
            XmlDocument xmlDoc = new XmlDocument();
            try
            {
                xmlDoc.Load(xmlFileName); //加載XML文檔
                XmlNode xmlNode = xmlDoc.SelectSingleNode(xpath);
                return xmlNode;
            }
            catch (Exception ex)
            {
                return null;
                //throw ex; //這裡可以定義你自己的異常處理
            }
        }

        ///<summary>
        /// 選擇匹配XPath表達式的節點列表XmlNodeList.
        ///</summary>
        ///<param name="xmlFileName">XML文檔完全文件名(包含物理路徑)</param>
        ///<param name="xpath">要匹配的XPath表達式(例如:"//節點名//子節點名")</param>
        ///<returns>返回XmlNodeList</returns>
        public static XmlNodeList GetXmlNodeListByXpath(string xmlFileName, string xpath)
        {
            XmlDocument xmlDoc = new XmlDocument();

            try
            {
                xmlDoc.Load(xmlFileName); //加載XML文檔
                XmlNodeList xmlNodeList = xmlDoc.SelectNodes(xpath);
                return xmlNodeList;
            }
            catch (Exception ex)
            {
                return null;
                //throw ex; //這裡可以定義你自己的異常處理
            }
        }

        ///<summary>
        /// 選擇匹配XPath表達式的第一個節點的匹配xmlAttributeName的屬性XmlAttribute.
        ///</summary>
        ///<param name="xmlFileName">XML文檔完全文件名(包含物理路徑)</param>
        ///<param name="xpath">要匹配的XPath表達式(例如:"//節點名//子節點名</param>

        ///<param name="xmlAttributeName">要匹配xmlAttributeName的屬性名稱</param>
        ///<returns>返回xmlAttributeName</returns>
        public static XmlAttribute GetXmlAttribute(string xmlFileName, string xpath, string xmlAttributeName)
        {
            string content = string.Empty;
            XmlDocument xmlDoc = new XmlDocument();
            XmlAttribute xmlAttribute = null;
            try
            {
                xmlDoc.Load(xmlFileName); //加載XML文檔
                XmlNode xmlNode = xmlDoc.SelectSingleNode(xpath);
                if (xmlNode != null)
                {
                    if (xmlNode.Attributes.Count > 0)
                    {
                        xmlAttribute = xmlNode.Attributes[xmlAttributeName];
                    }
                }
            }
            catch (Exception ex)
            {
                throw ex; //這裡可以定義你自己的異常處理
            }
            return xmlAttribute;
        }
        #endregion

        #region XML文檔創建和節點或屬性的添加、修改
        ///<summary>
        /// 創建一個XML文檔
        ///</summary>
        ///<param name="xmlFileName">XML文檔完全文件名(包含物理路徑)</param>
        ///<param name="rootNodeName">XML文檔根節點名稱(須指定一個根節點名稱)</param>

        ///<param name="version">XML文檔版本號(必須為:"1.0")</param>
        ///<param name="encoding">XML文檔編碼方式</param>
        ///<param name="standalone">該值必須是"yes"或"no",如果為null,Save方法不在XML聲明上寫出獨立屬性</param>
        ///<returns>成功返回true,失敗返回false</returns>
        public static bool CreateXmlDocument(string xmlFileName, string rootNodeName, string version, string encoding, string standalone)
        {
            bool isSuccess = false;
            try
            {
                XmlDocument xmlDoc = new XmlDocument();
                XmlDeclaration xmlDeclaration = xmlDoc.CreateXmlDeclaration(version, encoding, standalone);
                XmlNode root = xmlDoc.CreateElement(rootNodeName);
                xmlDoc.AppendChild(xmlDeclaration);
                xmlDoc.AppendChild(root);
                xmlDoc.Save(xmlFileName);
                isSuccess = true;
            }
            catch (Exception ex)
            {
                throw ex; //這裡可以定義你自己的異常處理
            }
            return isSuccess;
        }

        ///<summary>
        /// 依據匹配XPath表達式的第一個節點來創建它的子節點(如果此節點已存在則追加一個新的同名節點
        ///</summary>
        ///<param name="xmlFileName">XML文檔完全文件名(包含物理路徑)</param>
        ///<param name="xpath">要匹配的XPath表達式(例如:"//節點名//子節點名</param>

        ///<param name="xmlNodeName">要匹配xmlNodeName的節點名稱</param>
        ///<param name="innerText">節點文本值</param>
        ///<param name="xmlAttributeName">要匹配xmlAttributeName的屬性名稱</param>
        ///<param name="value">屬性值</param>
        ///<returns>成功返回true,失敗返回false</returns>
        public static bool CreateXmlNodeByXPath(string xmlFileName, string xpath, string xmlNodeName, string innerText, string xmlAttributeName, string value)
        {
            bool isSuccess = false;
            XmlDocument xmlDoc = new XmlDocument();
            try
            {
                xmlDoc.Load(xmlFileName); //加載XML文檔
                XmlNode xmlNode = xmlDoc.SelectSingleNode(xpath);
                if (xmlNode != null)
                {
                    //存不存在此節點都創建
                    XmlElement subElement = xmlDoc.CreateElement(xmlNodeName);
                    subElement.InnerXml = innerText;

                    //如果屬性和值參數都不為空則在此新節點上新增屬性
                    if (!string.IsNullOrEmpty(xmlAttributeName) && !string.IsNullOrEmpty(value))
                    {
                        XmlAttribute xmlAttribute = xmlDoc.CreateAttribute(xmlAttributeName);
                        xmlAttribute.Value = value;
                        subElement.Attributes.Append(xmlAttribute);
                    }

                    xmlNode.AppendChild(subElement);
                }
                xmlDoc.Save(xmlFileName); //保存到XML文檔
                isSuccess = true;
            }
            catch (Exception ex)
            {
                throw ex; //這裡可以定義你自己的異常處理
            }
            return isSuccess;
        }

        ///<summary>
        /// 依據匹配XPath表達式的第一個節點來創建或更新它的子節點(如果節點存在則更新,不存在則創建)
        ///</summary>
        ///<param name="xmlFileName">XML文檔完全文件名(包含物理路徑)</param>
        ///<param name="xpath">要匹配的XPath表達式(例如:"//節點名//子節點名</param>

        ///<param name="xmlNodeName">要匹配xmlNodeName的節點名稱</param>
        ///<param name="innerText">節點文本值</param>
        ///<returns>成功返回true,失敗返回false</returns>
        public static bool CreateOrUpdateXmlNodeByXPath(string xmlFileName, string xpath, string xmlNodeName, string innerText)
        {
            bool isSuccess = false;
            bool isExistsNode = false;//標識節點是否存在
            XmlDocument xmlDoc = new XmlDocument();
            try
            {
                xmlDoc.Load(xmlFileName); //加載XML文檔
                XmlNode xmlNode = xmlDoc.SelectSingleNode(xpath);
                if (xmlNode != null)
                {
                    //遍歷xpath節點下的所有子節點
                    foreach (XmlNode node in xmlNode.ChildNodes)
                    {
                        if (node.Name.ToLower() == xmlNodeName.ToLower())
                        {
                            //存在此節點則更新
                            node.InnerXml = innerText;
                            isExistsNode = true;
                            break;
                        }
                    }
                    if (!isExistsNode)
                    {
                        //不存在此節點則創建
                        XmlElement subElement = xmlDoc.CreateElement(xmlNodeName);
                        subElement.InnerXml = innerText;
                        xmlNode.AppendChild(subElement);
                    }
                }
                xmlDoc.Save(xmlFileName); //保存到XML文檔
                isSuccess = true;
            }
            catch (Exception ex)
            {
                throw ex; //這裡可以定義你自己的異常處理
            }
            return isSuccess;
        }

        ///<summary>
        /// 依據匹配XPath表達式的第一個節點來創建或更新它的屬性(如果屬性存在則更新,不存在則創建)
        ///</summary>
        ///<param name="xmlFileName">XML文檔完全文件名(包含物理路徑)</param>
        ///<param name="xpath">要匹配的XPath表達式(例如:"//節點名//子節點名</param>

        ///<param name="xmlAttributeName">要匹配xmlAttributeName的屬性名稱</param>
        ///<param name="value">屬性值</param>
        ///<returns>成功返回true,失敗返回false</returns>
        public static bool CreateOrUpdateXmlAttributeByXPath(string xmlFileName, string xpath, string xmlAttributeName, string value)
        {
            bool isSuccess = false;
            bool isExistsAttribute = false;//標識屬性是否存在
            XmlDocument xmlDoc = new XmlDocument();
            try
            {
                xmlDoc.Load(xmlFileName); //加載XML文檔
                XmlNode xmlNode = xmlDoc.SelectSingleNode(xpath);
                if (xmlNode != null)
                {
                    //遍歷xpath節點中的所有屬性
                    foreach (XmlAttribute attribute in xmlNode.Attributes)
                    {
                        if (attribute.Name.ToLower() == xmlAttributeName.ToLower())
                        {
                            //節點中存在此屬性則更新
                            attribute.Value = value;
                            isExistsAttribute = true;
                            break;
                        }
                    }
                    if (!isExistsAttribute)
                    {
                        //節點中不存在此屬性則創建
                        XmlAttribute xmlAttribute = xmlDoc.CreateAttribute(xmlAttributeName);
                        xmlAttribute.Value = value;
                        xmlNode.Attributes.Append(xmlAttribute);
                    }
                }
                xmlDoc.Save(xmlFileName); //保存到XML文檔
                isSuccess = true;
            }
            catch (Exception ex)
            {
                throw ex; //這裡可以定義你自己的異常處理
            }
            return isSuccess;
        }
        #endregion


        #region XML文檔節點或屬性的刪除
        ///<summary>
        /// 刪除匹配XPath表達式的第一個節點(節點中的子元素同時會被刪除)
        ///</summary>
        ///<param name="xmlFileName">XML文檔完全文件名(包含物理路徑)</param>
        ///<param name="xpath">要匹配的XPath表達式(例如:"//節點名//子節點名</param>
        ///<returns>成功返回true,失敗返回false</returns>
        public static bool DeleteXmlNodeByXPath(string xmlFileName, string xpath)
        {
            bool isSuccess = false;
            XmlDocument xmlDoc = new XmlDocument();
            try
            {
                xmlDoc.Load(xmlFileName); //加載XML文檔
                XmlNode xmlNode = xmlDoc.SelectSingleNode(xpath);
                if (xmlNode != null)
                {
                    //刪除節點
                    xmlNode.ParentNode.RemoveChild(xmlNode);
                }
                xmlDoc.Save(xmlFileName); //保存到XML文檔
                isSuccess = true;
            }
            catch (Exception ex)
            {
                throw ex; //這裡可以定義你自己的異常處理
            }
            return isSuccess;
        }

        ///<summary>
        /// 刪除匹配XPath表達式的第一個節點中的匹配參數xmlAttributeName的屬性
        ///</summary>
        ///<param name="xmlFileName">XML文檔完全文件名(包含物理路徑)</param>
        ///<param name="xpath">要匹配的XPath表達式(例如:"//節點名//子節點名</param>

        ///<param name="xmlAttributeName">要刪除的xmlAttributeName的屬性名稱</param>
        ///<returns>成功返回true,失敗返回false</returns>
        public static bool DeleteXmlAttributeByXPath(string xmlFileName, string xpath, string xmlAttributeName)
        {
            bool isSuccess = false;
            bool isExistsAttribute = false;
            XmlDocument xmlDoc = new XmlDocument();
            try
            {
                xmlDoc.Load(xmlFileName); //加載XML文檔
                XmlNode xmlNode = xmlDoc.SelectSingleNode(xpath);
                XmlAttribute xmlAttribute = null;
                if (xmlNode != null)
                {
                    //遍歷xpath節點中的所有屬性
                    foreach (XmlAttribute attribute in xmlNode.Attributes)
                    {
                        if (attribute.Name.ToLower() == xmlAttributeName.ToLower())
                        {
                            //節點中存在此屬性
                            xmlAttribute = attribute;
                            isExistsAttribute = true;
                            break;
                        }
                    }
                    if (isExistsAttribute)
                    {
                        //刪除節點中的屬性
                        xmlNode.Attributes.Remove(xmlAttribute);
                    }
                }
                xmlDoc.Save(xmlFileName); //保存到XML文檔
                isSuccess = true;
            }
            catch (Exception ex)
            {
                throw ex; //這裡可以定義你自己的異常處理
            }
            return isSuccess;
        }

        ///<summary>
        /// 刪除匹配XPath表達式的第一個節點中的所有屬性
        ///</summary>
        ///<param name="xmlFileName">XML文檔完全文件名(包含物理路徑)</param>
        ///<param name="xpath">要匹配的XPath表達式(例如:"//節點名//子節點名</param>
        ///<returns>成功返回true,失敗返回false</returns>
        public static bool DeleteAllXmlAttributeByXPath(string xmlFileName, string xpath)
        {
            bool isSuccess = false;
            XmlDocument xmlDoc = new XmlDocument();
            try
            {
                xmlDoc.Load(xmlFileName); //加載XML文檔
                XmlNode xmlNode = xmlDoc.SelectSingleNode(xpath);
                if (xmlNode != null)
                {
                    //遍歷xpath節點中的所有屬性
                    xmlNode.Attributes.RemoveAll();
                }
                xmlDoc.Save(xmlFileName); //保存到XML文檔
                isSuccess = true;
            }
            catch (Exception ex)
            {
                throw ex; //這裡可以定義你自己的異常處理
            }
            return isSuccess;
        }
        #endregion

    }
}


