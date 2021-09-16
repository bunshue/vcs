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

namespace xCh11_5_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"C:\Northwind.mdb";
            builder["User Id"] = "Admin";

            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            {
                string queryString = "SELECT * FROM 訂貨主檔";
                OleDbCommand command = new OleDbCommand(builder.ConnectionString);
                connection.Open();

                // 建構DataSet及其組成分子
                DataSet NorthwindDataSet = new DataSet();
                OleDbDataAdapter myAdapter = new OleDbDataAdapter(queryString, connection);
                myAdapter.Fill(NorthwindDataSet, "訂貨主檔Table");

                queryString = "SELECT * FROM 訂貨明細";
                myAdapter = new OleDbDataAdapter(queryString, connection);
                myAdapter.Fill(NorthwindDataSet, "訂貨明細Table");

                DataTable orders = NorthwindDataSet.Tables["訂貨主檔Table"];
                DataTable details = NorthwindDataSet.Tables["訂貨明細Table"];

                var query =
                    from order in orders.AsEnumerable()
                    join detail in details.AsEnumerable()
                    on order.Field<int>("訂單號碼") equals
                        detail.Field<int>("訂單號碼")
                    select new
                    {
                        訂單號碼 =
                            order.Field<int>("訂單號碼"),
                        客戶編號 =
                            order.Field<string>("客戶編號"),
                        訂單日期 =
                            order.Field<DateTime>("訂單日期"),
                        產品編號 =
                            detail.Field<int>("產品編號")
                    };

                dataGridView1.DataSource = query.ToList();
            }
        }
    }
}
