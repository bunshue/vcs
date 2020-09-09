using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;

namespace vcs_ReadWrite_XML5
{
    public partial class Form1 : Form
    {
        string xml_filename = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML5.xml";

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            XmlDocument xml = new XmlDocument();
            xml.Load(xml_filename);//加载xml文件
            XmlNode xn = xml.DocumentElement;
            textBox1.Text = xn["user"].InnerText;
            textBox2.Text = xn["psw"].InnerText;
            richTextBox1.Text += xn["user"].InnerText + " " + xn["psw"].InnerText + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            XmlDocument xml = new XmlDocument();
            xml.Load(xml_filename);//加载xml文件
            XmlNode xn = xml.DocumentElement;
            xn["user"].InnerText = textBox1.Text;
            xn["psw"].InnerText = textBox2.Text;
            xml.Save(xml_filename);//保存xml文件
            richTextBox1.Text += xn["user"].InnerText + " " + xn["psw"].InnerText + "\n";
        }
    }
}
