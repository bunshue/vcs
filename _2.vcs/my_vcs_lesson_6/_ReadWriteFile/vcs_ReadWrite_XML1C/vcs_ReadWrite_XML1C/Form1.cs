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


/*
遠端讀檔

本地存檔

開啟檔案的 也順便存一份在本地 用作基本比較
*/

/*
C#操作XML方法详解

XmlDocument xml=new XmlDocument();	//初始化一个xml实例
 
//导入指定xml文件
xml.Load(filename);

//保存XML文件
xml.Save(filename);
 
//指定一个节点
XmlNode root=xml.SelectSingleNode("/root");
 
//获取节点下所有直接子节点
XmlNodeList childlist=root.ChildNodes;
 
//判断该节点下是否有子节点
root.HasChildNodes;
 
//获取同名同级节点集合
XmlNodeList nodelist=xml.SelectNodes("/Root/News");
 
//生成一个新节点
XmlElement node=xml.CreateElement("News");
 
//将节点加到指定节点下，作为其子节点
root.AppendChild(node);
 
//将节点加到指定节点下某个子节点前
root.InsertBefore(node,root.ChildeNodes[i]);
 
//为指定节点的新建属性并赋值
node.SetAttribute("id","11111");
 
//为指定节点添加子节点
root.AppendChild(node);
 
//获取指定节点的指定属性值
string id=node.Attributes["id"].Value;
 
//获取指定节点中的文本
string content=node.InnerText;
*/


namespace vcs_ReadWrite_XML1C
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
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            richTextBox1.Size = new Size(800, 1000);

            x_st = 20;
            y_st = 20;
            dx = 180;
            dy = 80;
            button00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button04.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button05.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button06.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button07.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button08.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button09.Location = new Point(x_st + dx * 1, y_st + dy * 4);

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
        XmlDocument xmldoc;
        XmlNode xmlnode;
        XmlElement xmlelem;
        private void button00_Click(object sender, EventArgs e)
        {
            //建立XML檔案 1
            string filename = "vcs_ReadWrite_XML1Ca.xml";

            xmldoc = new XmlDocument();
            //加入XML的声明段落,<?xml version="1.0" encoding="gb2312"?>
            XmlDeclaration xmldecl;
            xmldecl = xmldoc.CreateXmlDeclaration("1.0", "utf-8", null);
            xmldoc.AppendChild(xmldecl);

            //加入一个根元素
            xmlelem = xmldoc.CreateElement("", "Employees", "");
            xmldoc.AppendChild(xmlelem);
            //加入另外一个元素
            for (int i = 1; i < 3; i++)
            {

                XmlNode root = xmldoc.SelectSingleNode("Employees");//查找<Employees>
                XmlElement xe1 = xmldoc.CreateElement("Node");//创建一个<Node>节点
                xe1.SetAttribute("genre", "李赞红");//设置该节点genre属性
                xe1.SetAttribute("ISBN", "2-3631-4");//设置该节点ISBN属性

                XmlElement xesub1 = xmldoc.CreateElement("title");
                xesub1.InnerText = "CS从入门到精通";//设置文本节点
                xe1.AppendChild(xesub1);//添加到<Node>节点中
                XmlElement xesub2 = xmldoc.CreateElement("author");
                xesub2.InnerText = "候捷";
                xe1.AppendChild(xesub2);
                XmlElement xesub3 = xmldoc.CreateElement("price");
                xesub3.InnerText = "58.3";
                xe1.AppendChild(xesub3);

                root.AppendChild(xe1);//添加到<Employees>节点中
            }
            //保存创建好的XML文档
            xmldoc.Save(filename);
            richTextBox1.Text += "建立XML檔案 : " + filename + "\n";
        }

        private void button01_Click(object sender, EventArgs e)
        {
            //建立XML檔案 2
            string filename = "vcs_ReadWrite_XML1Cb.xml";

            XmlTextWriter xmlWriter;

            xmlWriter = new XmlTextWriter(filename, Encoding.UTF8);//创建一个xml文档
            xmlWriter.Formatting = Formatting.Indented;
            xmlWriter.WriteStartDocument();
            xmlWriter.WriteStartElement("Employees");

            xmlWriter.WriteStartElement("Node");
            xmlWriter.WriteAttributeString("genre", "李赞红");
            xmlWriter.WriteAttributeString("ISBN", "2-3631-4");

            xmlWriter.WriteStartElement("title");
            xmlWriter.WriteString("CS从入门到精通");
            xmlWriter.WriteEndElement();

            xmlWriter.WriteStartElement("author");
            xmlWriter.WriteString("候捷");
            xmlWriter.WriteEndElement();

            xmlWriter.WriteStartElement("price");
            xmlWriter.WriteString("58.3");
            xmlWriter.WriteEndElement();

            xmlWriter.WriteEndElement();

            xmlWriter.Close();
            richTextBox1.Text += "建立XML檔案 : " + filename + "\n";
        }

        private void button02_Click(object sender, EventArgs e)
        {
            string filename1 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ca.xml";
            string filename2 = "vcs_ReadWrite_XML1Ca_add.xml";

            //添加一個節點

            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(filename1);
            XmlNode root = xmlDoc.SelectSingleNode("Employees");//查找<Employees>
            XmlElement xe1 = xmlDoc.CreateElement("Node");//创建一个<Node>节点
            xe1.SetAttribute("genre", "张三");//设置该节点genre属性
            xe1.SetAttribute("ISBN", "1-1111-1");//设置该节点ISBN属性

            XmlElement xesub1 = xmlDoc.CreateElement("title");
            xesub1.InnerText = "C#入门帮助";//设置文本节点
            xe1.AppendChild(xesub1);//添加到<Node>节点中
            XmlElement xesub2 = xmlDoc.CreateElement("author");
            xesub2.InnerText = "高手";
            xe1.AppendChild(xesub2);
            XmlElement xesub3 = xmlDoc.CreateElement("price");
            xesub3.InnerText = "158.3";
            xe1.AppendChild(xesub3);

            root.AppendChild(xe1);//添加到<Employees>节点中
            xmlDoc.Save(filename2);

            richTextBox1.Text += "原XML檔案 : " + filename1 + "\n";
            richTextBox1.Text += "添加一個節點\n";
            richTextBox1.Text += "儲存XML檔案 : " + filename2 + "\n";
        }

        private void button03_Click(object sender, EventArgs e)
        {
            //修改節點內容 1
            string filename1 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ca_add.xml";
            string filename2 = "vcs_ReadWrite_XML1Ca_add_modify1.xml";

            //3，修改结点的值（属性和子结点）：

            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(filename1);

            XmlNodeList nodeList = xmlDoc.SelectSingleNode("Employees").ChildNodes;//获取Employees节点的所有子节点

            foreach (XmlNode xn in nodeList)//遍历所有子节点
            {
                XmlElement xe = (XmlElement)xn;//将子节点类型转换为XmlElement类型
                if (xe.GetAttribute("genre") == "张三")//如果genre属性值为“张三”
                {
                    xe.SetAttribute("genre", "update张三");//则修改该属性为“update张三”

                    XmlNodeList nls = xe.ChildNodes;//继续获取xe子节点的所有子节点
                    foreach (XmlNode xn1 in nls)//遍历
                    {
                        XmlElement xe2 = (XmlElement)xn1;//转换类型
                        if (xe2.Name == "author")//如果找到
                        {
                            xe2.InnerText = "亚胜";//则修改
                        }
                    }
                }
            }
            xmlDoc.Save(filename2);
            richTextBox1.Text += "原XML檔案 : " + filename1 + "\n";
            richTextBox1.Text += "修改節點內容 1\n";
            richTextBox1.Text += "儲存XML檔案 : " + filename2 + "\n";
        }

        private void button04_Click(object sender, EventArgs e)
        {
            //修改節點內容 2
            string filename1 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ca_add_modify1.xml";
            string filename2 = "vcs_ReadWrite_XML1Ca_add_modify2.xml";


            //4，修改结点（添加结点的属性和添加结点的自结点）：
            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(filename1);

            XmlNodeList nodeList = xmlDoc.SelectSingleNode("Employees").ChildNodes;//获取Employees节点的所有子节点

            foreach (XmlNode xn in nodeList)
            {
                XmlElement xe = (XmlElement)xn;
                xe.SetAttribute("test", "111111");

                XmlElement xesub = xmlDoc.CreateElement("flag");
                xesub.InnerText = "1";
                xe.AppendChild(xesub);
            }
            xmlDoc.Save(filename2);
            richTextBox1.Text += "原XML檔案 : " + filename1 + "\n";
            richTextBox1.Text += "修改節點內容 2\n";
            richTextBox1.Text += "儲存XML檔案 : " + filename2 + "\n";
        }

        private void button05_Click(object sender, EventArgs e)
        {
            //刪除節點資料 1
            string filename1 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ca_add_modify2.xml";
            string filename2 = "vcs_ReadWrite_XML1Ca_add_modify2_delete1.xml";

            //刪除節點資料 1
            //5，删除结点中的某一个属性：
            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(filename1);
            XmlNodeList xnl = xmlDoc.SelectSingleNode("Employees").ChildNodes;
            foreach (XmlNode xn in xnl)
            {
                XmlElement xe = (XmlElement)xn;
                xe.RemoveAttribute("genre");//删除genre属性

                XmlNodeList nls = xe.ChildNodes;//继续获取xe子节点的所有子节点
                foreach (XmlNode xn1 in nls)//遍历
                {
                    XmlElement xe2 = (XmlElement)xn1;//转换类型
                    if (xe2.Name == "flag")//如果找到
                    {
                        xe.RemoveChild(xe2);//则删除
                    }
                }
            }
            xmlDoc.Save(filename2);
            richTextBox1.Text += "原XML檔案 : " + filename1 + "\n";
            richTextBox1.Text += "刪除節點資料 1\n";
            richTextBox1.Text += "儲存XML檔案 : " + filename2 + "\n";
        }

        private void button06_Click(object sender, EventArgs e)
        {
            //刪除節點資料 2
            string filename1 = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ca_add.xml";
            string filename2 = "vcs_ReadWrite_XML1Ca_add_delete.xml";
            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(filename1);
            XmlNode root = xmlDoc.SelectSingleNode("Employees");
            XmlNodeList xnl = xmlDoc.SelectSingleNode("Employees").ChildNodes;
            for (int i = 0; i < xnl.Count; i++)
            {
                XmlElement xe = (XmlElement)xnl.Item(i);
                if (xe.GetAttribute("genre") == "张三")
                {
                    root.RemoveChild(xe);
                    if (i < xnl.Count) i = i - 1;
                }
            }
            xmlDoc.Save(filename2);
            richTextBox1.Text += "原XML檔案 : " + filename1 + "\n";
            richTextBox1.Text += "刪除節點資料 2\n";
            richTextBox1.Text += "儲存XML檔案 : " + filename2 + "\n";
        }

        string read_xml_content(string filename)
        {
            //讀出全部XML
            StreamReader sr = new StreamReader(filename, Encoding.Default);

            string xml_data = sr.ReadToEnd();//myString是读出的字符串
            sr.Close();

            return xml_data;
        }

        private void button07_Click(object sender, EventArgs e)
        {
            //讀出全部XML
            string filename = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Ca.xml";

            string xml_data = read_xml_content(filename);

            richTextBox1.Text += "原XML檔案 : " + filename + "\n";
            richTextBox1.Text += "讀出全部XML\n";
            richTextBox1.Text += xml_data + "\n";
        }

        private void button08_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Cc.xml";
            string xml_data = read_xml_content(filename);

            richTextBox1.Text += "原XML檔案 : " + filename + "\n";
            richTextBox1.Text += "讀出全部XML\n";
            richTextBox1.Text += xml_data + "\n";

            XmlDocument doc = new XmlDocument();
            doc.Load(filename);

            XmlNode node = doc.SelectSingleNode("/configuration/appSettings/ConnectionString");
            if (node != null)
            {
                string k1 = node.Value;    //null
                string k2 = node.InnerText;//Data Source=yf; user id=ctm_dbo;password=123
                string k3 = node.InnerXml;//Data Source=yf; user id=ctm_dbo;password=123
                richTextBox1.Text += "k1 : " + k1 + "\n";
                richTextBox1.Text += "k2 : " + k2 + "\n";
                richTextBox1.Text += "k3 : " + k3 + "\n";
                node = null;
            }
        }

        private void button09_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML1Cd.xml";
            string xml_data = read_xml_content(filename);

            richTextBox1.Text += "原XML檔案 : " + filename + "\n";
            richTextBox1.Text += "讀出全部XML\n";
            richTextBox1.Text += xml_data + "\n";

            XmlDocument doc = new XmlDocument();
            doc.Load(filename);

            XmlNode node = doc.SelectSingleNode("/configuration/appSettings/add");
            if (node != null)
            {
                string k = node.Attributes["key"].Value;
                string v = node.Attributes["value"].Value;

                richTextBox1.Text += "k : " + k + "\n";
                richTextBox1.Text += "v : " + v + "\n";
                node = null;
            }

            XmlNode node2 = doc.SelectSingleNode("/configuration/appSettings/add");
            if (node2 != null)
            {
                XmlNodeReader nr = new XmlNodeReader(node2);
                nr.MoveToContent();
                //检查当前节点是否是内容节点。如果此节点不是内容节点，则读取器向前跳至下一个内容节点或文件结尾。
                nr.MoveToAttribute("value");
                string s = nr.Value;
                richTextBox1.Text += "s : " + s + "\n";
                node2 = null;
            }
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

        //XML操作3

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button31_Click(object sender, EventArgs e)
        {
        }

        private void button32_Click(object sender, EventArgs e)
        {
        }

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
        }

        private void button40_Click(object sender, EventArgs e)
        {
        }

        private void button41_Click(object sender, EventArgs e)
        {
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

        private void button50_Click(object sender, EventArgs e)
        {

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
