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

namespace vcs_ReadWrite_XML7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
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

    }
}
