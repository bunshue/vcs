using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh9_4_3_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DataSet studentsDataSet = new DataSet("StudentsDataSet");
            DataTable studentTable = new DataTable("StudentTable");

            DataColumn idColumn = new DataColumn("編號", Type.GetType("System.Int32"));
            DataColumn nameColumn = new DataColumn("姓名");
            DataColumn schoolColumn = new DataColumn("學歷");

            studentTable.Columns.Add(idColumn);
            studentTable.Columns.Add(nameColumn);
            studentTable.Columns.Add(schoolColumn);

            studentsDataSet.Tables.Add(studentTable);

            studentsDataSet.WriteXmlSchema(@"c:\Students.xsd");

            MessageBox.Show("成功寫入Students.xsd");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            DataSet dataSet = new DataSet();
            dataSet.ReadXmlSchema(@"c:\Students.xsd");

            dataGridView1.DataSource = dataSet.Tables["StudentTable"];
        }
    }
}
