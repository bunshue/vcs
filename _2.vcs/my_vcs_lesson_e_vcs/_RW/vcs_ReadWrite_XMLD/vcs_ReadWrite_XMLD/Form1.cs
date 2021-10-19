using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//0. 需引用System.Xml命名空間;
using System.Xml;

namespace vcs_ReadWrite_XMLD
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
            //1. 首先使用XmlDocument建構一XML object，例：
            XmlDocument xdTest = new XmlDocument();

            //2. 因XML是由許多節點所組成，因此使用XmlDocument提供的CreateElement方法來建立節點，並assign給XmlElement object，例：
            XmlElement xeDocument = xdTest.CreateElement("Document");

            //可使用<List>XmlElement xeDocument = new List<XmlElement>();
            //使用迴圈將節點加進去，例：
            xeDocument.Add(xdTest.CreateElement("Field"));
            //或
            //xeDocument[index] = xdTest.CreateElement("Field");

            //3. 設定節點的屬性，如<Field name="ID" value="12345">，Field此節點下有兩個屬性(name與value)，透過XmlElement的SetAttribute方法來設定屬性，例：
            xeField.SetAttribute("name", "ID");
            xeField.SetAttribute("value", "12345");

            //4. 最後使用XmlElement.AppendChild方法將子節點一層一層加回根節點與XmlDocument object，建立階層關係，例：
            xeMaster.AppendcChild(xeField);
            xdTest.AppendChild(xeDocument);

            //5. 接著使用XmldDocument的InnerXml屬性即可檢視產生之XML，例：
            string strXml = xdTest.InnerXml;

            //6. 若要匯出文件，可使用XmlTextWriter類別，例：
            string filename = Application.StartupPath + "\\xml_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xml";
            XmlTextWriter writer = new XmlTextWriter(filename, encoding);
            //設定是否縮排
            writer.Formatting = Formatting.Indented;
            xdTest.Save(writer);

        }
    }
}
