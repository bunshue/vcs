using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;

//C# XmlTextWriter和XmlTextReader 讀寫XML文件


namespace read_write_xml
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
            //write xml
            // XmlTextWriter 寫文件
            XmlTextWriter writeXml = new XmlTextWriter("tmptmp.xml", Encoding.UTF8);
            writeXml.WriteStartDocument(false);
            writeXml.WriteStartElement("NetWork");

            writeXml.WriteComment("網絡配置信息");
            writeXml.WriteStartElement("configration");

            writeXml.WriteElementString("IpAddress", "192.168.2.168");
            writeXml.WriteElementString("Netmask", "255.255.255.0");
            writeXml.WriteElementString("Gateway", "202.103.24.68");

            writeXml.WriteEndElement();
            writeXml.WriteEndElement();

            writeXml.Flush();
            writeXml.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //read xml
            // XmlTextReader 讀文件
            XmlTextReader readerXml = new XmlTextReader("tmptmp.xml");
            while (readerXml.Read())
            {
                if (readerXml.NodeType == XmlNodeType.Element)
                {

                    if (readerXml.Name == "IpAddress")
                    {
                        richTextBox1.Text += readerXml.ReadElementString().Trim() + "\n";
                    }
                    if (readerXml.Name == "Netmask")
                    {
                        richTextBox1.Text += readerXml.ReadElementString().Trim() + "\n";
                    }
                    if (readerXml.Name == "Gateway")
                    {
                        richTextBox1.Text += readerXml.ReadElementString().Trim() + "\n";
                    }
                }
            }
        }
    }
}

