using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;

namespace vcs_ReadWrite_XML3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            XmlDocument document = new XmlDocument();
            document.Load("C:\\______test_files\\_xml\\宅之力R.xml");
            richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["server"].Value + "\t";
            richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["account"].Value + "\t";
            richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["password"].Value + "\t";
            richTextBox1.Text += document.SelectSingleNode("/root/settinginfo").Attributes["delay"].Value + "\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            XmlDocument document = new XmlDocument();
            document.AppendChild(document.CreateXmlDeclaration("1.0", "UTF-8", ""));//將宣告節點加入document中
            XmlNode xmlnode_root = document.CreateNode(XmlNodeType.Element, "root", "");
            XmlNode xmlnode_settinginfo = document.CreateNode(XmlNodeType.Element, "settinginfo", "");
            XmlAttribute xmlattribute_server = document.CreateAttribute("server");
            XmlAttribute xmlattribute_account = document.CreateAttribute("account");
            XmlAttribute xmlattribute_password = document.CreateAttribute("password");
            XmlAttribute xmlattribute_delay = document.CreateAttribute("delay");
            xmlattribute_server.Value = textBox_ServerName.Text;
            xmlattribute_account.Value = textBox_Account.Text;
            xmlattribute_password.Value = textBox_Password.Text;
            xmlattribute_delay.Value = textBox_timerInterval.Text;


            xmlnode_settinginfo.Attributes.Append(xmlattribute_server);//將屬性加入xmlnode_settinginfo節點下
            xmlnode_settinginfo.Attributes.Append(xmlattribute_account);//將屬性加入xmlnode_settinginfo節點下
            xmlnode_settinginfo.Attributes.Append(xmlattribute_password);//將屬性加入xmlnode_settinginfo節點下
            xmlnode_settinginfo.Attributes.Append(xmlattribute_delay);//將屬性加入xmlnode_settinginfo節點下
            xmlnode_root.AppendChild(xmlnode_settinginfo);//將xmlnode_settinginfo節點加入xmlnode_root節點下
            document.AppendChild(xmlnode_root); //將xmlnode_root節點加入document中
            document.Save("C:\\______test_files\\_xml\\宅之力W.xml");

            richTextBox1.Text += "宅之力_xml寫入 OK\n\r";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            XmlDocument XmlDoc = new XmlDocument();
            XmlDoc.Load("C:\\______test_files\\_xml\\仙人的設計之路1.xml");
            XmlNodeList NodeLists = XmlDoc.SelectNodes("Root/MyLevel1");

            foreach (XmlNode OneNode in NodeLists)
            {
                //String StrAttrName = OneNode.Attributes.Name;
                //String StrAttrValue = OneNode.Attributes[" MyAttr1 "].Value;
                //String StrAttrValue = OneNode.InnerText;
                richTextBox1.Text += OneNode.Attributes.Count.ToString() + "\t";
                richTextBox1.Text += OneNode.Attributes[" MyAttr1 "].Value + "\t";
                richTextBox1.Text += OneNode.InnerText + "\n";
            }
            richTextBox1.Text += "\n\n仙人的設計之路1 OK\n\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            XmlDocument XmlDoc = new XmlDocument();
            XmlDoc.Load("C:\\______test_files\\_xml\\仙人的設計之路2.xml");
            XmlNodeList NodeLists = XmlDoc.SelectNodes("Root/MyLevel1");
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
    }
}
