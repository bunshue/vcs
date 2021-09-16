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

namespace xCh10_3_11
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

            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            {
                string queryString = "SELECT * FROM 供應商";
                OleDbCommand command = new OleDbCommand(builder.ConnectionString);
                connection.Open();

                // 建構DataSet及其組成分子
                DataSet NorthwindDataSet = new DataSet();
                OleDbDataAdapter myAdapter = new OleDbDataAdapter(queryString, connection);
                myAdapter.Fill(NorthwindDataSet, "供應商Table");

                // 秀出剛動態建構出來的DataSet 
                dataGridView1.DataSource = NorthwindDataSet.Tables["供應商Table"];

                queryString = "SELECT * FROM 員工";
                myAdapter = new OleDbDataAdapter(queryString, connection);
                myAdapter.Fill(NorthwindDataSet, "員工Table");

                // 秀出剛動態建構出來的DataSet
                dataGridView2.DataSource = NorthwindDataSet.Tables["員工Table"];
            }
        }
    }
}
