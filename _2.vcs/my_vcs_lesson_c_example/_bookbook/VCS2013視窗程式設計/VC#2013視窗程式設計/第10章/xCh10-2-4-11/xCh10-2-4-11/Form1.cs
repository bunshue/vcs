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

namespace xCh10_2_4_11
{
    public partial class Form1 : Form
    {
        OleDbConnectionStringBuilder builder;
        OleDbConnection connection;
        OleDbCommand command;
        OleDbParameter parameter;
        OleDbDataAdapter myAdapter;
        DataSet NorthwindDataSet;

        public Form1()
        {
            InitializeComponent();

            builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"C:\Northwind.mdb";
            builder["User Id"] = "Admin";

            connection = new OleDbConnection(builder.ConnectionString);
            connection.Open();

            // 取出所有客戶資料並交由DataGridView物件顯示
            myAdapter = new OleDbDataAdapter("SELECT * FROM 客戶", connection);
            NorthwindDataSet = new DataSet();
            myAdapter.Fill(NorthwindDataSet, "客戶Table");
            dataGridView1.DataSource = NorthwindDataSet.Tables["客戶Table"];         
        }

        private void DataChanged()
        {
            NorthwindDataSet = new DataSet();
            myAdapter.Fill(NorthwindDataSet, "客戶Table");
            dataGridView1.DataSource = NorthwindDataSet.Tables["客戶Table"];
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 建構Insert
            command = new OleDbCommand();
            command.CommandText = "INSERT INTO 客戶 (客戶編號, 公司名稱) VALUES (?, ?)";
            command.Connection = connection;

            command.Parameters.Add("CustomerID", OleDbType.Char, 5);
            command.Parameters.Add("CompanyName", OleDbType.VarChar, 40);
            command.Parameters["CustomerID"].Value = textBox1.Text;
            command.Parameters["CompanyName"].Value = textBox2.Text;
            command.ExecuteNonQuery();

            NorthwindDataSet.Tables["客戶Table"].AcceptChanges();
            DataChanged();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 建構Update
            command = new OleDbCommand();
            command.CommandText = 
                "UPDATE 客戶 SET " +
                    "客戶編號 = @CustomerID, "+
                    "公司名稱 = @CompanyName " +
                    "WHERE 客戶編號 = @CustomerID";
            command.Connection = connection;

            command.Parameters.Add("@CustomerID", OleDbType.Char, 5);
            command.Parameters.Add("@CompanyName", OleDbType.VarChar, 40);
            command.Parameters["@CustomerID"].Value = textBox1.Text;
            command.Parameters["@CompanyName"].Value = textBox2.Text;

            command.ExecuteNonQuery();
            DataChanged();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // 建構Delete
            command = new OleDbCommand();
            command.CommandText = "DELETE * FROM 客戶 " + 
                "WHERE 客戶編號 = @CustomerID";
            command.Connection = connection;

            parameter = command.Parameters.Add("@CustomerID", OleDbType.Char, 5);
            command.Parameters["@CustomerID"].Value = textBox1.Text;
            command.ExecuteNonQuery();

            NorthwindDataSet.Tables["客戶Table"].AcceptChanges();
            DataChanged();
        }
    }
}
