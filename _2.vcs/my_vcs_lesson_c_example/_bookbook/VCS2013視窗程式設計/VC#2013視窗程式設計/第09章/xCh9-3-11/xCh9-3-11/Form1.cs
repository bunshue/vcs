using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh9_3_11
{
    public partial class Form1 : Form
    {
        private System.Data.DataSet dataSet;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            dataSet = new DataSet();

            MakeParentTable();
            MakeChildTable();
            MakeDataRelation();

            dataGridView1.DataSource = dataSet;
            dataGridView1.DataMember = "ParentTable";
            dataGridView2.DataSource = dataSet;
            dataGridView2.DataMember = "ParentTable.parent2Child";
        }

        private void MakeParentTable()
        {
            System.Data.DataTable table = new DataTable("ParentTable");
            DataColumn column;
            DataRow row;

            column = new DataColumn();
            column.DataType = System.Type.GetType("System.Int32");
            column.ColumnName = "客戶編號";
            column.ReadOnly = true;
            column.Unique = true;
            table.Columns.Add(column);

            column = new DataColumn();
            column.DataType = System.Type.GetType("System.String");
            column.ColumnName = "客戶名稱";
            column.AutoIncrement = false;
            column.Caption = "客戶名稱";
            column.ReadOnly = false;
            column.Unique = false;
            table.Columns.Add(column);

            // 設定客戶編號欄為primary key
            DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            PrimaryKeyColumns[0] = table.Columns["客戶編號"];
            table.PrimaryKey = PrimaryKeyColumns;

            dataSet.Tables.Add(table);

            string[] names = new string[] { "張三", "李四", "王五" };
            for (int i = 0; i <= 2; i++)
            {
                row = table.NewRow();
                row["客戶編號"] = i;
                row["客戶名稱"] = names[i];
                table.Rows.Add(row);
            }
        }

        private void MakeChildTable()
        {
            DataTable table = new DataTable("childTable");
            DataColumn column;
            DataRow row;

            column = new DataColumn();
            column.DataType = System.Type.GetType("System.Int32");
            column.ColumnName = "訂單編號";
            column.AutoIncrement = true;
            column.Caption = "訂單編號";
            column.ReadOnly = true;
            column.Unique = true;
            table.Columns.Add(column);

            column = new DataColumn();
            column.DataType = System.Type.GetType("System.String");
            column.ColumnName = "品名";
            column.AutoIncrement = false;
            column.Caption = "品名";
            column.ReadOnly = false;
            column.Unique = false;
            table.Columns.Add(column);

            column = new DataColumn();
            column.DataType = System.Type.GetType("System.Int32");
            column.ColumnName = "客戶編號";
            column.AutoIncrement = false;
            column.Caption = "客戶編號";
            column.ReadOnly = false;
            column.Unique = false;
            table.Columns.Add(column);

            dataSet.Tables.Add(table);

            string[] items = new string[] { 
                "螢幕",
                "滑鼠", 
                "鍵盤", 
                "隨身碟", 
                "MP3撥放器" 
            };
            for (int i = 0; i <= 4; i++)
            {
                row = table.NewRow();
                row["訂單編號"] = i;
                row["品名"] = items[i];
                row["客戶編號"] = 0;
                table.Rows.Add(row);
            }
            for (int i = 0; i <= 4; i++)
            {
                row = table.NewRow();
                row["訂單編號"] = i + 5;
                row["品名"] = items[i];
                row["客戶編號"] = 1;
                table.Rows.Add(row);
            }
            for (int i = 0; i <= 4; i++)
            {
                row = table.NewRow();
                row["訂單編號"] = i + 10;
                row["品名"] = items[i];
                row["客戶編號"] = 2;
                table.Rows.Add(row);
            }
        }

        private void MakeDataRelation()
        {
            DataColumn parentColumn = 
                dataSet.Tables["ParentTable"].Columns["客戶編號"];

            DataColumn childColumn = 
                dataSet.Tables["ChildTable"].Columns["客戶編號"];

            DataRelation relation = 
                new DataRelation("parent2Child", parentColumn, childColumn);

            dataSet.Tables["ChildTable"].ParentRelations.Add(relation);
        }
    }
}
