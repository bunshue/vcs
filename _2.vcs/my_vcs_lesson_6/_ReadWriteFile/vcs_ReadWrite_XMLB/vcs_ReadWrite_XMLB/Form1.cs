using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;
using System.Xml.Linq;  //for XDocument

namespace vcs_ReadWrite_XMLB
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //使用LINQ讀取XML
            string sURL = @"C:\______test_files\__RW\_xml\weather_current.xml";

            UseLINQ(sURL);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用XML Reader讀取XML
            string sURL = @"C:\______test_files\__RW\_xml\weather_current.xml";
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
    }
}

