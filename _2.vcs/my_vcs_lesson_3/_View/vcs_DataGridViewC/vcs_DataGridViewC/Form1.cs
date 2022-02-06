using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DataGridViewC
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
            dataGridView1.DataSource = MakeTable();
            dataGridView1.AutoResizeColumns();

        }

        public DataTable MakeTable()
        {
            DataTable table = new DataTable("Product");

            //建立三個DataColumn並設定相關欄位屬性
            DataColumn column1 = new DataColumn("ProductID");
            column1.DataType = System.Type.GetType("System.String");
            column1.AllowDBNull = false;
            column1.Caption = "產品編號";
            column1.DefaultValue = "Car001";

            DataColumn column2 = new DataColumn("ProductName");
            column2.DataType = System.Type.GetType("System.String");
            column2.AllowDBNull = true;
            column2.Caption = "產品名稱";
            column2.DefaultValue = "日蝕GST";

            DataColumn column3 = new DataColumn("Price");
            column3.DataType = System.Type.GetType("System.Decimal");
            column3.AllowDBNull = true;
            column3.Caption = "價格";
            column3.DefaultValue = 0;

            //將欄位加入表格中
            table.Columns.Add(column1);
            table.Columns.Add(column2);
            table.Columns.Add(column3);

            //建立二個DataRow並給定其對應欄位內容值
            DataRow row;
            row = table.NewRow();
            row["ProductID"] = "Car001";
            row["ProductName"] = "Mitsubishi Eclipse GST";
            row["Price"] = 1200000;
            table.Rows.Add(row);

            row = table.NewRow();
            row["ProductID"] = "Car002";
            row["ProductName"] = "Tigra";
            row["Price"] = 800000;
            table.Rows.Add(row);
            return table;
        }
    }
}
