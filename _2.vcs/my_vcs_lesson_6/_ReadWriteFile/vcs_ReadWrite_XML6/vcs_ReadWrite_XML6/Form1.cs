using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for StringWriter
using System.Xml;

namespace vcs_ReadWrite_XML6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //建立XML檔案資料
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

        // Add an Employee node to the document.
        private void MakeEmployee(XmlElement parent,
            String first_name, String last_name, int emp_id)
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
    }
}
