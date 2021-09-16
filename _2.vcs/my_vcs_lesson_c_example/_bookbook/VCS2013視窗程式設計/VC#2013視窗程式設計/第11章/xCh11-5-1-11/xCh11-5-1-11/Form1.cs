using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.OleDb;

namespace xCh11_5_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"C:\Northwind.mdb";
            builder["User Id"] = "Admin";

            DataSet NorthwindDataSet;
            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            {
                string queryString = "SELECT * FROM 產品資料";
                OleDbCommand command = new OleDbCommand(builder.ConnectionString);
                connection.Open();

                // 建構DataSet及其組成分子
                NorthwindDataSet = new DataSet();
                OleDbDataAdapter myAdapter = new OleDbDataAdapter(queryString, connection);
                myAdapter.Fill(NorthwindDataSet, "產品資料Table");
            }

            DataTable products = NorthwindDataSet.Tables["產品資料Table"];

            var myQuery =
                from product in products.AsEnumerable()
                where product.Field<bool>("不再銷售") == true
                select
                    new
                    {
                        產品編號 = product.Field<int>("產品編號"),
                        產品 = product.Field<string>("產品"),
                        庫存量 = product.Field<Int16>("庫存量")
                    };

            // 秀出LINQ查詢出來的資料 
            dataGridView1.DataSource = myQuery.ToList();
        }
    }
}
