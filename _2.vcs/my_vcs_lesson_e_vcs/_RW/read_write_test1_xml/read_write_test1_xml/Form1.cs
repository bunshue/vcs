using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;
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

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
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
                        //Console.WriteLine(readerXml.ReadElementString().Trim());
                        richTextBox1.Text += readerXml.Name + " :\t" + readerXml.ReadElementString().Trim() + "\n";
                    }
                    if (readerXml.Name == "Netmask")
                    {
                        //Console.WriteLine(readerXml.ReadElementString().Trim());
                        richTextBox1.Text += readerXml.Name + " :\t" + readerXml.ReadElementString().Trim() + "\n";
                    }
                    if (readerXml.Name == "Gateway")
                    {
                        //Console.WriteLine(readerXml.ReadElementString().Trim());
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
