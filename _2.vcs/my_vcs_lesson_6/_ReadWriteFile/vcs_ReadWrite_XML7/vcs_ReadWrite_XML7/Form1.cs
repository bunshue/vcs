using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Xml;

using System.Xml.Linq;  //for XElement
// XElement物件預設是以序列的方式處理xml資料，可以直接根據xml資料的階層結構，透過XElement物件建立資料

namespace vcs_ReadWrite_XML7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button1_Click(object sender, EventArgs e)
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

        private void button2_Click(object sender, EventArgs e)
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

        private void button3_Click(object sender, EventArgs e)
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

        //透過XElement建立xml資料
        private void button4_Click(object sender, EventArgs e)
        {
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

        //建立XML檔案資料
        private void button5_Click(object sender, EventArgs e)
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

            // Format the XML text.
            StringWriter string_writer = new StringWriter();
            XmlTextWriter xml_text_writer = new XmlTextWriter(string_writer);
            xml_text_writer.Formatting = Formatting.Indented;
            xml_document.WriteTo(xml_text_writer);

            // Display the result.
            //txtResult.Text = string_writer.ToString();

            richTextBox1.Text += string_writer.ToString();
        }

        //開啟XML檔案到TreeView ST
        private void button6_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML6.xml";
            LoadTreeViewFromXmlFile(filename, treeView1);
        }

        // Load a TreeView control from an XML file.
        private void LoadTreeViewFromXmlFile(string filename, TreeView trv)
        {
            // Load the XML document.
            XmlDocument xml_doc = new XmlDocument();
            xml_doc.Load(filename);

            // Add the root node's children to the TreeView.
            trv.Nodes.Clear();
            AddTreeViewChildNodes(trv.Nodes, xml_doc.DocumentElement);
        }

        // Add the children of this XML node 
        // to this child nodes collection.
        private void AddTreeViewChildNodes(TreeNodeCollection parent_nodes, XmlNode xml_node)
        {
            foreach (XmlNode child_node in xml_node.ChildNodes)
            {
                // Make the new TreeView node.
                TreeNode new_node = parent_nodes.Add(child_node.Name);

                // Recursively make this node's descendants.
                AddTreeViewChildNodes(new_node.Nodes, child_node);

                // If this is a leaf node, make sure it's visible.
                if (new_node.Nodes.Count == 0) new_node.EnsureVisible();
            }
        }
        //開啟XML檔案到TreeView SP


        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //開啟XML檔案到TreeView ST
        private void button7_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_xml\NexusPoint.xml";
            //string filename = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML6.xml";

            XmlDocument NexusDocument = new XmlDataDocument();//定義一個XML文檔對像
            NexusDocument.Load(filename);//加載XML文件
            RecursionTreeControl(NexusDocument.DocumentElement, treeView1.Nodes);//將加載完成的XML文件顯示在TreeView控件中
            treeView1.ExpandAll();//展開TreeView控件中的所有項
        }

        /// <summary>
        /// RecursionTreeControl:表示將XML文件的內容顯示在TreeView控件中
        /// </summary>
        /// <param name="xmlNode">將要加載的XML文件中的節點元素</param>
        /// <param name="nodes">將要加載的XML文件中的節點集合</param>
        private void RecursionTreeControl(XmlNode xmlNode, TreeNodeCollection nodes)
        {
            foreach (XmlNode node in xmlNode.ChildNodes)//循環遍歷當前元素的子元素集合
            {
                string temp = (node.Value != null ? node.Value : (node.Attributes != null && node.Attributes.Count > 0) ? node.Attributes[0].Value : node.Name);//表示TreeNode節點的文本內容
                TreeNode new_child = new TreeNode(temp);//定義一個TreeNode節點對像
                nodes.Add(new_child);//向當前TreeNodeCollection集合中添加當前節點
                RecursionTreeControl(node, new_child.Nodes);//調用本方法進行遞歸
            }
        }




    }
}
