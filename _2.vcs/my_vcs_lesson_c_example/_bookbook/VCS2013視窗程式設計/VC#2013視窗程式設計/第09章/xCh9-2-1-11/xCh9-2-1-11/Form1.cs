using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh9_2_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 建構DataSet及其組成的資料表
            DataSet studentsDataSet = new DataSet("StudentsDataSet");
            DataTable studentTable = new DataTable("StudentTable");

            // 建構資料欄
            DataColumn idColumn = new DataColumn("編號" );
            DataColumn nameColumn = new DataColumn("姓名");
            DataColumn schoolColumn = new DataColumn("學歷");

            // 設定「編號」資料欄為自動增加數值
            idColumn.DataType=Type.GetType("System.Int32");
            idColumn.AutoIncrement = true;

            // 加入資料欄
            studentTable.Columns.Add(idColumn);
            studentTable.Columns.Add(nameColumn);
            studentTable.Columns.Add(schoolColumn);

            // 將資料表加入DataSet
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

            // 秀出剛動態建構出來的DataSet 
            dataGridView1.DataSource = 
                studentsDataSet.Tables["StudentTable"];
        }
    }
}
