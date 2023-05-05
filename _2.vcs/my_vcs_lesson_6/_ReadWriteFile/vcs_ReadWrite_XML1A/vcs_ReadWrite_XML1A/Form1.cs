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

namespace vcs_ReadWrite_XML1A
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
        string filename0 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\vcs_ReadWrite_XML1.xml";
        string filename0_add = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\vcs_ReadWrite_XML1_add.xml";
        string filename0_delete = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\vcs_ReadWrite_XML1_delete.xml";

        private void button00_Click(object sender, EventArgs e)
        {
            if (File.Exists(filename0))
            {
                ParseXML(filename0);
            }
            else
            {
                richTextBox1.Text += "XML文件 : " + filename0 + " 不存在\n";
            }
        }

        // 標準版XML讀取解析程式 ST
        private void ParseXML(string filename0)
        {
            //加載XML文件
            XmlDocument xdDocument = new XmlDocument();
            richTextBox1.Text += "開啟XML文件 : " + filename0 + "\n";
            xdDocument.Load(filename0);

            //得到主節點
            XmlElement xeRoot = xdDocument.DocumentElement;
            if (xeRoot != null)
            {
                XmlNode xnNodeRoot = (XmlNode)xeRoot;
                RecurseXmlDocument(xnNodeRoot, 0);
                richTextBox1.Text += "\n讀取XML文件 : " + filename0 + " 完成\n";
            }
        }

        /// <summary>
        /// 讀取ＸＭＬ
        /// </summary>
        /// <param name="aXnNode">節點</param>
        /// <param name="aIndent">縮進大小</param>
        private void RecurseXmlDocument(XmlNode aXnNode, int aIndent)
        {
            //判斷結點中是否有內容
            if (aXnNode == null)
            {
                return;
            }

            //節點是元素時
            if (aXnNode is XmlElement)
            {
                //顯示根元素的名稱
                richTextBox1.Text += "\n\t根元素 : " + "\"" + aXnNode.Name.PadLeft(aXnNode.Name.Length + aIndent) + "\"" + "\t";
                //listBox1.Items.Add(aXnNode.Name.PadLeft(aXnNode.Name.Length + aIndent));
                if (aXnNode.Attributes != null)
                {
                    //得到屬性
                    foreach (XmlAttribute xaAttribute in aXnNode.Attributes)
                    {
                        string sText = "";
                        sText = xaAttribute.Name;
                        richTextBox1.Text += "\n\t\t屬性名 sText1 = " + "\"" + sText + "\"";
                        //listBox1.Items.Add(sText.PadLeft(sText.Length + aIndent + 2));
                        sText = xaAttribute.Value;
                        //listBox1.Items.Add(sText.PadLeft(sText.Length + aIndent + 4));
                        richTextBox1.Text += "\t屬性值 sText2 = " + "\"" + sText + "\"";
                    }
                }
                //根元素中是否有子元素
                if (aXnNode.HasChildNodes)
                {
                    //有子節點，遍歷子節點
                    RecurseXmlDocument(aXnNode.FirstChild, aIndent + 2);
                }
                //判斷下個節點是為空
                if (aXnNode.NextSibling != null)
                {
                    RecurseXmlDocument(aXnNode.NextSibling, aIndent);
                }
            }
            else if (aXnNode is XmlText)
            {
                //顯示節點中的內容
                string sText = ((XmlText)aXnNode).Value;
                //listBox1.Items.Add(sText.PadLeft(sText.Length + aIndent));
                richTextBox1.Text += "\t文本 sText3 = " + "\"" + sText + "\"";
            }
            else if (aXnNode is XmlComment)
            {
                string sText = aXnNode.Value;
                //listBox1.Items.Add(sText.PadLeft(sText.Length + aIndent));
                richTextBox1.Text += "\n註釋 sText4 = " + "\"" + sText + "\"";
                //如果不加下邊的遍歷，資料只會得出備註中的內容，不會得出子節點內容
                if (aXnNode.HasChildNodes)
                {
                    //有子節點，遍歷子節點
                    RecurseXmlDocument(aXnNode.FirstChild, aIndent + 2);
                }
                if (aXnNode.NextSibling != null)
                {
                    RecurseXmlDocument(aXnNode.NextSibling, aIndent);
                }
            }
        }
        // 標準版XML讀取解析程式 SP

        private void button01_Click(object sender, EventArgs e)
        {
            if (File.Exists(filename0))
            {
                //加載XML文件
                XmlDocument xdDocument = new XmlDocument();
                richTextBox1.Text += "開啟XML文件 : " + filename0 + "\n";
                xdDocument.Load(filename0);

                //得到主節點
                XmlElement xeRoot = xdDocument.DocumentElement;

                //創建節點
                XmlElement newBook = xdDocument.CreateElement("book");
                XmlElement newTitle = xdDocument.CreateElement("title");
                XmlElement newAuthor = xdDocument.CreateElement("author");
                XmlElement newCode = xdDocument.CreateElement("code");

                //創建屬性
                XmlAttribute xaNewAttribute = xdDocument.CreateAttribute("Pages");
                xaNewAttribute.Value = "1000";
                XmlText title = xdDocument.CreateTextNode("Beginning Visual C# 3rd Edition");
                XmlText author = xdDocument.CreateTextNode("Karli Watson et al");
                XmlText code = xdDocument.CreateTextNode("123456789");
                //創建備註
                XmlComment comment = xdDocument.CreateComment("This book is the book you are reading");

                //元素插入ＸＭＬ樹中
                newBook.AppendChild(comment);
                newBook.Attributes.Append(xaNewAttribute);
                newBook.AppendChild(newTitle);
                newBook.AppendChild(newAuthor);
                newBook.AppendChild(newCode);
                newTitle.AppendChild(title);
                newAuthor.AppendChild(author);
                newCode.AppendChild(code);

                //插入某節點後邊
                xeRoot.InsertAfter(newBook, xeRoot.FirstChild);

                //插入某節點前邊
                //xeRoot.InsertBefore(newBook, xeRoot.FirstChild);

                //保存結果
                xdDocument.Save(filename0_add);
                richTextBox1.Text += "寫入XML文件 : " + filename0_add + "\n";
            }
            else
                richTextBox1.Text += "XML文件 : " + filename0 + " 不存在\n";
        }

        private void button02_Click(object sender, EventArgs e)
        {
            if (File.Exists(filename0))
            {
                //加載XML文件
                XmlDocument xdDocument = new XmlDocument();
                richTextBox1.Text += "開啟XML文件 : " + filename0 + "\n";
                xdDocument.Load(filename0);

                //得到主節點
                XmlElement xeRoot = xdDocument.DocumentElement;

                if (xeRoot.HasChildNodes)
                {
                    //得到最後一個節點
                    XmlNode xnBook = xeRoot.LastChild;
                    //刪除最後一個結點
                    xeRoot.RemoveChild(xnBook);
                    //保存結果
                    xdDocument.Save(filename0_delete);
                    richTextBox1.Text += "寫入XML文件 : " + filename0_delete + "\n";
                }
            }
            else
                richTextBox1.Text += "XML文件 : " + filename0 + " 不存在\n";
        }

        private void button03_Click(object sender, EventArgs e)
        {

        }

        private void button04_Click(object sender, EventArgs e)
        {

        }

        //XML操作1
        private void button10_Click(object sender, EventArgs e)
        {
            string filename1a = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\宅之力R.xml";
            if (File.Exists(filename1a))
            {
                XmlDocument document = new XmlDocument();
                richTextBox1.Text += "開啟XML文件 : " + filename1a + "\n";
                document.Load(filename1a);

                richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["server"].Value + "\t";
                richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["account"].Value + "\t";
                richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["password"].Value + "\t";
                richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["delay"].Value + "\n";
            }
            else
            {
                richTextBox1.Text += "XML文件 : " + filename1a + " 不存在\n";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            string filename1b = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\宅之力W.xml";

            XmlDocument document = new XmlDocument();
            document.AppendChild(document.CreateXmlDeclaration("1.0", "UTF-8", ""));//將宣告節點加入document中
            XmlNode xmlnode_root = document.CreateNode(XmlNodeType.Element, "root", "");
            XmlNode xmlnode_settinginfo = document.CreateNode(XmlNodeType.Element, "settinginfo", "");
            XmlAttribute xmlattribute_server = document.CreateAttribute("server");
            XmlAttribute xmlattribute_account = document.CreateAttribute("account");
            XmlAttribute xmlattribute_password = document.CreateAttribute("password");
            XmlAttribute xmlattribute_delay = document.CreateAttribute("delay");

            xmlattribute_server.Value = "Server Name A";
            xmlattribute_account.Value = "Account Lion";
            xmlattribute_password.Value = "Password mouse";
            xmlattribute_delay.Value = "Interval 12345";

            xmlnode_settinginfo.Attributes.Append(xmlattribute_server);//將屬性加入xmlnode_settinginfo節點下
            xmlnode_settinginfo.Attributes.Append(xmlattribute_account);//將屬性加入xmlnode_settinginfo節點下
            xmlnode_settinginfo.Attributes.Append(xmlattribute_password);//將屬性加入xmlnode_settinginfo節點下
            xmlnode_settinginfo.Attributes.Append(xmlattribute_delay);//將屬性加入xmlnode_settinginfo節點下
            xmlnode_root.AppendChild(xmlnode_settinginfo);//將xmlnode_settinginfo節點加入xmlnode_root節點下
            document.AppendChild(xmlnode_root); //將xmlnode_root節點加入document中

            //保存結果
            document.Save(filename1b);
            richTextBox1.Text += "寫入XML文件 : " + filename1b + "\n";

        }

        private void button12_Click(object sender, EventArgs e)
        {
            string filename1c = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\仙人的設計之路2.xml";
            if (File.Exists(filename1c))
            {
                XmlDocument document = new XmlDocument();
                richTextBox1.Text += "開啟XML文件 : " + filename1c + "\n";
                document.Load(filename1c);

                XmlNodeList NodeLists = document.SelectNodes("Root/MyLevel1");
                //XmlNodeList NodeLists = XmlDoc.SelectNodes("Root/MyLevel1/MyLevel2");

                richTextBox1.Text += "Attribute" + "\t|\t" + "參數" + "\t\t|\t" + "內容" + "\n\n";

                foreach (XmlNode OneNode in NodeLists)
                {
                    String StrNodeName = OneNode.Name.ToString();
                    foreach (XmlAttribute Attr in OneNode.Attributes)
                    {
                        String StrAttr = Attr.Name.ToString();
                        String StrValue = OneNode.Attributes[Attr.Name.ToString()].Value;
                        String StrInnerText = OneNode.InnerText;
                        richTextBox1.Text += "[" + StrAttr + "\t|\t" + StrValue + "\t|\t" + StrInnerText + "]\n";
                    }
                }
                richTextBox1.Text += "\n\n仙人的設計之路2 OK\n\n";
            }
            else
                richTextBox1.Text += "XML文件 : " + filename1c + " 不存在\n";

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        //XML操作2

        string xml_filename2 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\vcs_ReadWrite_XML2.xml";
        private void button20_Click(object sender, EventArgs e)
        {
            XmlDocument xml = new XmlDocument();
            xml.Load(xml_filename2);//加载xml文件
            XmlNode xn = xml.DocumentElement;

            richTextBox1.Text += "取得帳號 : " + xn["user"].InnerText + "\n";
            richTextBox1.Text += "取得密碼 : " + xn["psw"].InnerText + "\n";
        }

        private void button21_Click(object sender, EventArgs e)
        {
            XmlDocument xml = new XmlDocument();
            xml.Load(xml_filename2);//加载xml文件
            XmlNode xn = xml.DocumentElement;

            string account = "lion";
            string password = "mouse";

            xn["user"].InnerText = account;
            xn["psw"].InnerText = password;

            richTextBox1.Text += "設定帳號 : " + xn["user"].InnerText + "\n";
            richTextBox1.Text += "設定密碼 : " + xn["psw"].InnerText + "\n";

            xml.Save(xml_filename2);//保存xml文件

            richTextBox1.Text += "存檔完成\n";
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

        //XML操作3
        private void button30_Click(object sender, EventArgs e)
        {
            // Make the XML document.
            XmlDocument xml_document = new XmlDocument();

            // Make the root element.
            XmlElement employees_element = xml_document.CreateElement("Employees");
            xml_document.AppendChild(employees_element);

            // Make some Employee elements.
            MakeEmployee(employees_element, "Albert", "Anders", 11111);
            MakeEmployee(employees_element, "Betty", "Beach", 22222);
            MakeEmployee(employees_element, "Chuck", "Cinder", 33333);

            richTextBox1.Text += xml_document.OuterXml + "\n";
        }

        // Add an Employee node to the document.
        private void MakeEmployee(XmlElement parent, String first_name, String last_name, int emp_id)
        {
            // Make the Employee element.
            XmlNode employee_element = parent.OwnerDocument.CreateElement("Employee");
            parent.AppendChild(employee_element);

            // Add the FirstName, LastName, and EmployeeId elements.
            XmlNode first_name_element = parent.OwnerDocument.CreateElement("FirstName");
            first_name_element.InnerText = first_name;
            employee_element.AppendChild(first_name_element);

            XmlNode last_name_element = parent.OwnerDocument.CreateElement("LastName");
            last_name_element.InnerText = last_name;
            employee_element.AppendChild(last_name_element);

            XmlNode employee_id_element = parent.OwnerDocument.CreateElement("EmployeeId");
            employee_id_element.InnerText = emp_id.ToString();
            employee_element.AppendChild(employee_id_element);
        }

        private void button31_Click(object sender, EventArgs e)
        {
            MemoryStream memory_stream = new MemoryStream();
            XmlTextWriter xml_text_writer = new XmlTextWriter(memory_stream, System.Text.Encoding.UTF8);

            // Use indentation to make the result look nice.
            xml_text_writer.Formatting = Formatting.Indented;
            xml_text_writer.Indentation = 4;

            // Write the XML declaration.
            xml_text_writer.WriteStartDocument(true);

            // Start the Employees node.
            xml_text_writer.WriteStartElement("Employees");

            // Write some Employee elements.
            MakeEmployee(xml_text_writer, "Albert", "Anders", 11111);
            MakeEmployee(xml_text_writer, "Betty", "Beach", 22222);
            MakeEmployee(xml_text_writer, "Chuck", "Cinder", 33333);

            // End the Employees node.
            xml_text_writer.WriteEndElement();

            // End the document.
            xml_text_writer.WriteEndDocument();
            xml_text_writer.Flush();

            // Use a StreamReader to display the result.
            StreamReader stream_reader = new StreamReader(memory_stream);

            memory_stream.Seek(0, SeekOrigin.Begin);

            richTextBox1.Text += stream_reader.ReadToEnd() + "\n";

            // Close the XmlTextWriter.
            xml_text_writer.Close();
        }

        // Add an Employee node to the document.
        private void MakeEmployee(XmlTextWriter xml_text_writer, String first_name, String last_name, int emp_id)
        {
            // Start the Employee element.
            xml_text_writer.WriteStartElement("Employee");

            // Write the FirstName.
            xml_text_writer.WriteStartElement("FirstName");
            xml_text_writer.WriteString(first_name);
            xml_text_writer.WriteEndElement();

            // Write the LastName.
            xml_text_writer.WriteStartElement("LastName");
            xml_text_writer.WriteString(last_name);
            xml_text_writer.WriteEndElement();

            // Write the EmployeeId.
            xml_text_writer.WriteStartElement("EmployeeId");
            xml_text_writer.WriteString(emp_id.ToString());
            xml_text_writer.WriteEndElement();

            // Close the Employee element.
            xml_text_writer.WriteEndElement();
        }

        private void button32_Click(object sender, EventArgs e)
        {
            // Read the XElement.
            XElement xelement = XElement.Parse(
                @"<employees>
                    <employee firstname=""Terry"" lastname=""Pratchett""/>
                    <employee firstname='Glen' lastname='Cook'/>
                    <employee firstname='Tom' lastname='Holt'/>
                    <employee>
                      <firstname>Rod</firstname>
                      <lastname>Stephens</lastname>
                    </employee>
                  </employees>
                ");

            // Display the nodes.
            foreach (XNode node in xelement.Nodes())
            {
                richTextBox1.Text += node.ToString() + "\n";
            }
        }

        private void button33_Click(object sender, EventArgs e)
        {
            //透過XElement建立xml資料
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
            richTextBox1.Text += company.ToString();
        }

        private void button34_Click(object sender, EventArgs e)
        {
            //建立XML檔案資料

            // Make the XML document.
            XmlDocument xml_document = new XmlDocument();

            // Make the root element.
            XmlElement employees_element = xml_document.CreateElement("Employees");
            xml_document.AppendChild(employees_element);

            // Make some Employee elements.
            MakeEmployee(employees_element, "Albert", "Anders", 11111);
            MakeEmployee(employees_element, "Betty", "Beach", 22222);
            MakeEmployee(employees_element, "Chuck", "Cinder", 33333);

            // Format the XML text.
            StringWriter string_writer = new StringWriter();
            XmlTextWriter xml_text_writer = new XmlTextWriter(string_writer);
            xml_text_writer.Formatting = Formatting.Indented;
            xml_document.WriteTo(xml_text_writer);

            // Display the result.
            //txtResult.Text = string_writer.ToString();

            richTextBox1.Text += string_writer.ToString();
        }

        //XML操作4
        private void button40_Click(object sender, EventArgs e)
        {
            //使用LINQ讀取XML
            //使用LINQ讀取XML
            string sURL = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\weather_current.xml";

            UseLINQ(sURL);

        }

        private void button41_Click(object sender, EventArgs e)
        {
            //使用XML Reader讀取XML
            //使用XML Reader讀取XML
            string sURL = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\weather_current.xml";
            UseXmlReader(sURL);
        }


                //一、使用LINQ讀取

        ///　<summary>
        ///　使用LINQ讀取web上的xml
        ///　</summary>
        public void UseLINQ(string sURL)
        {
            //string sURL = "http://localhost:9058/GameServerInfo/XMLFile.xml";
            XDocument oXDoc = XDocument.Load(sURL);
            var qurey = from e in oXDoc.Descendants()
                        where e.NodeType == XmlNodeType.Element
                        select new
                        {
                            ElementName = e.Name.ToString(),
                            ElementValue = e.Value
                        };
            foreach (var elementInfo in qurey)
            {
                //HttpContext.Current.Response.Write(string.Format("ElementName->{0}　ElementValue->{1}<br　/>", elementInfo.ElementName, elementInfo.ElementValue));
                richTextBox1.Text += "ElementName:\t" + elementInfo.ElementName + "\tElementValue:\t" + elementInfo.ElementValue + "\n";
            }
        }

        //二、使用XmlReader構造函數
        ///　<summary>
        ///　使用XmlReader構造函數
        ///　</summary>
        public void UseXmlReader(string sURL)
        {
            using (XmlReader read = XmlReader.Create(sURL))
            {
                while (read.Read())
                {
                    switch (read.NodeType)
                    {
                        case XmlNodeType.Element:
                            richTextBox1.Text += "1ElementName:\t" + read.Name + "\n";
                            break;
                        case XmlNodeType.Text:
                            //HttpContext.Current.Response.Write(string.Format("ElementValue->{0}<br　/>", read.Value));
                            richTextBox1.Text += "2ElementValue:\t" + read.Value + "\n";
                            break;
                        case XmlNodeType.CDATA:
                            //HttpContext.Current.Response.Write(string.Format("ElementValue->{0}<br　/>", read.Value));
                            richTextBox1.Text += "3ElementValue:\t" + read.Value + "\n";

                            break;
                        //other
                    }
                }
            }
        }

        private void button42_Click(object sender, EventArgs e)
        {

        }

        private void button43_Click(object sender, EventArgs e)
        {

        }

        private void button44_Click(object sender, EventArgs e)
        {

        }

        //XML操作5
        private void button50_Click(object sender, EventArgs e)
        {
            //建立XML檔案
            XmlDocument xmlDocument = new XmlDocument(); //create xml document
            XmlNode xmlNode = xmlDocument.CreateNode(XmlNodeType.XmlDeclaration, "", ""); //xml document header declaration
            xmlDocument.AppendChild(xmlNode); // add xml document header declarations
            XmlElement xmlElement = xmlDocument.CreateElement("", "TestDataModels", ""); //create xml root node
            XmlElement element2 = xmlDocument.CreateElement("", "TestDataModels", ""); //create TestDataModels' child node
            for (int i = 1; i < 4; i++)
            {
                XmlElement element = xmlDocument.CreateElement("", "TestDataModels", ""); //create TestDataModels' child node
                //add child node for the TestDataModels's node
                XmlElement elementCode = xmlDocument.CreateElement("Test", "Code", "");
                XmlText xmlTextCode = xmlDocument.CreateTextNode("TCode " + i.ToString());
                elementCode.AppendChild(xmlTextCode);
                element.AppendChild(elementCode);

                XmlElement elementName = xmlDocument.CreateElement("Test", "Name", "");
                XmlText xmlTextName = xmlDocument.CreateTextNode("TName " + i.ToString());
                elementName.AppendChild(xmlTextName);
                element.AppendChild(elementName);

                //testType start
                XmlElement elementType = xmlDocument.CreateElement("Test", "Type", "");
                XmlElement elementTypeCode = xmlDocument.CreateElement("Type", "TCode", "");
                XmlText xmlTextTypeCode = xmlDocument.CreateTextNode("tt.TtCode-" + i.ToString());
                elementTypeCode.AppendChild(xmlTextTypeCode);
                elementType.AppendChild(elementTypeCode);

                XmlElement elementTypeName = xmlDocument.CreateElement("Type", "TName", "");
                XmlText xmlTextTypeName = xmlDocument.CreateTextNode("tt.TtName-" + i.ToString());
                elementTypeName.AppendChild(xmlTextTypeName);
                elementType.AppendChild(elementTypeName);
                element.AppendChild(elementType);

                //testType end
                xmlElement.AppendChild(element); //For xmlElement add child element
            }
            xmlDocument.AppendChild(xmlElement); //For xmlDocument add child node

            string filename = Application.StartupPath + "\\xml_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xml";

            xmlDocument.Save(filename); //save the xmlDocument

            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        private void button51_Click(object sender, EventArgs e)
        {

        }

        private void button52_Click(object sender, EventArgs e)
        {

        }

        private void button53_Click(object sender, EventArgs e)
        {

        }

        private void button54_Click(object sender, EventArgs e)
        {

        }
    }
}
