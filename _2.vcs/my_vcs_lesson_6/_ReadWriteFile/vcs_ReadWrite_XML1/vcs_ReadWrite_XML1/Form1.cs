using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;

namespace vcs_ReadWrite_XML1
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
            dx = 200 + 5;
            dy = 60 + 5;

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

            richTextBox1.Size = new Size(600, 640);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1260, 700);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //XML操作0
            string xml_filename2 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\_xml\vcs_ReadWrite_XML2.xml";

            //讀取資料

            XmlDocument xml = new XmlDocument();
            xml.Load(xml_filename2);//加载xml文件
            XmlNode xn = xml.DocumentElement;

            richTextBox1.Text += "取得帳號 : " + xn["user"].InnerText + "\n";
            richTextBox1.Text += "取得密碼 : " + xn["psw"].InnerText + "\n";

            //------------------------------------------------------------  # 60個

            //寫入資料

            //XmlDocument
            xml = new XmlDocument();
            xml.Load(xml_filename2);//加载xml文件
            //XmlNode
            xn = xml.DocumentElement;

            string account = "lion";
            string password = "mouse";

            xn["user"].InnerText = account;
            xn["psw"].InnerText = password;

            richTextBox1.Text += "設定帳號 : " + xn["user"].InnerText + "\n";
            richTextBox1.Text += "設定密碼 : " + xn["psw"].InnerText + "\n";

            xml.Save(xml_filename2);//保存xml文件

            richTextBox1.Text += "存檔完成\n";
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //XML操作1
            //讀取

            string filename1a = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\_xml\宅之力R.xml";

            XmlDocument document = new XmlDocument();
            richTextBox1.Text += "開啟XML文件 : " + filename1a + "\n";
            document.Load(filename1a);

            richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["server"].Value + "\t";
            richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["account"].Value + "\t";
            richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["password"].Value + "\t";
            richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["delay"].Value + "\n";

            //新增節點

            string filename1b = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\_xml\宅之力W.xml";

            //XmlDocument
            document = new XmlDocument();
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

            //存檔
            document.Save(filename1b);
            richTextBox1.Text += "已存檔 : " + filename1b + "\n";

            //------------------------------------------------------------  # 60個

            //讀取

            string filename1c = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\_xml\仙人的設計之路2.xml";
            //XmlDocument
            document = new XmlDocument();
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

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            //XML操作2

        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
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

            //存檔
            string filename = "tmp_xml_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xml";
            xmlDocument.Save(filename);
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        //------------------------------------------------------------  # 60個

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
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


