using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;using System.Text;using System.Threading.Tasks;using System.Windows.Forms;

namespace xCh9_4_1_11
{
    public partial class Form1 : Form
    {
        DataSet studentsDataSet;
        DataTable studentTable;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 建構DataSet及其組成分子
            studentsDataSet = new DataSet("StudentsDataSet");
            studentTable = new DataTable("StudentTable");

            DataColumn idColumn = new DataColumn("id", Type.GetType("System.Int32"));
            idColumn.AutoIncrement = true;
            DataColumn nameColumn = new DataColumn("姓名");
            DataColumn schoolColumn = new DataColumn("學歷");

            studentTable.Columns.Add(idColumn);
            studentTable.Columns.Add(nameColumn);
            studentTable.Columns.Add(schoolColumn);

            studentsDataSet.Tables.Add(studentTable);

            // 加入記錄
            DataRow newRow;

            newRow = studentTable.NewRow();
            newRow["姓名"] = "唐三藏";
            newRow["學歷"] = "博士";
            studentTable.Rows.Add(newRow);

            newRow = studentTable.NewRow();
            newRow["姓名"] = "孫悟空";
            newRow["學歷"] = "碩士";
            studentTable.Rows.Add(newRow);

            newRow = studentTable.NewRow();
            newRow["姓名"] = "豬八戒";
            newRow["學歷"] = "學士";
            studentTable.Rows.Add(newRow);

            studentsDataSet.AcceptChanges();

            // 秀出剛動態建構出來的DataSet 
            dataGridView1.DataSource = studentsDataSet.Tables["StudentTable"];
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                // 將studentsDataSet寫成XML文件
                string xmlFilename = 
                    @"C:\\XmlDocument-"+
                    DateTime.Now.Millisecond.ToString()+
                    ".xml";
                System.IO.FileStream streamWrite = new 
                    System.IO.FileStream(xmlFilename, System.IO.FileMode.Create);
                studentsDataSet.WriteXml(streamWrite);
                streamWrite.Dispose();

                MessageBox.Show("已建構完成XML文件：" + xmlFilename);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // 建構DataSet物件
            studentsDataSet = new DataSet("StudentsDataSet");

            // 讀入XML文件 
            string xmlFilename = @"C:\\XmlDocument-432.xml";
            System.IO.FileStream streamRead = 
                new System.IO.FileStream(xmlFilename, System.IO.FileMode.Open);
            studentsDataSet.ReadXml(streamRead);
            streamRead.Dispose();

            // 秀出讀入的XML文件
            dataGridView1.DataSource = studentsDataSet.Tables["StudentTable"];
        }
    }
}
