using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;

namespace vcs_ReadWrite_XMLC
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
    }
}
