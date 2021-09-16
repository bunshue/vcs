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

namespace xCh10_2_2_11
{
    public partial class Form1 : Form
    {
        OleDbConnectionStringBuilder builder;
        string queryString;

        public Form1()
        {
            InitializeComponent();

            builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"C:\Northwind.mdb";
            builder["User Id"] = "Admin";

            // 取出員工資料表中所有欄位的內容
            queryString = "SELECT * FROM 員工";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            {
                OleDbCommand command = new OleDbCommand(queryString, connection);
                command.CommandTimeout = 20;

                connection.Open();
                OleDbDataReader reader = command.ExecuteReader();

                label1.Text = "是否包含一個或多個資料列：" + (reader.HasRows ? "是" : "否");
                label2.Text = "目前資料列中的資料行數目：" + reader.FieldCount.ToString();
                label3.Text = "資料讀取器是否關閉：" + (reader.IsClosed ? "是" : "否");

                // 建構DataSet及其組成分子
                DataSet NorthwindDataSet = new DataSet();
                DataTable 員工Table = new DataTable("員工Table");
                DataColumn aColumn;

                for (int i = 0; i < reader.FieldCount; i++)
                {
                    aColumn = new DataColumn(reader.GetName(i), reader.GetFieldType(i));
                    員工Table.Columns.Add(aColumn);
                }

                // 加入記錄
                DataRow newRow = null;
                while (reader.Read())
                {
                    newRow = 員工Table.NewRow();
                    for (int i = 0; i < reader.FieldCount; i++)
                    {
                        newRow[i] = reader.GetValue(i);// 相當於reader[i];
                    }
                    員工Table.Rows.Add(newRow);
                }

                NorthwindDataSet.Tables.Add(員工Table);

                // 秀出剛動態建構出來的DataSet 
                dataGridView1.DataSource = NorthwindDataSet.Tables["員工Table"];

                reader.Close();

                // 執行查詢，並傳回查詢所傳回的結果集中第一個資料列的第一個資料行。
                // 會忽略其他的資料行或資料列。
                command.CommandText = "SELECT COUNT(*) FROM 員工";
                int count = (Int32)command.ExecuteScalar();
                label4.Text = "共有 " + count.ToString() + " 筆記錄";

                reader.Close();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            {
                OleDbCommand command = new OleDbCommand(queryString, connection);
                command.CommandTimeout = 20;

                connection.Open();
                OleDbDataReader reader = command.ExecuteReader();

                // 建構DataSet及其組成分子
                DataSet NorthwindDataSet = new DataSet();
                DataTable 部份員工Table = new DataTable("部份員工Table");

                int nameNdx = reader.GetOrdinal("姓名");
                DataColumn nameColumn = new DataColumn(
                    reader.GetName(nameNdx), 
                    reader.GetFieldType(nameNdx)
                    );
                部份員工Table.Columns.Add(nameColumn);

                int positionNdx = reader.GetOrdinal("職稱");
                DataColumn positionColumn = new DataColumn(
                    reader.GetName(positionNdx), 
                    reader.GetFieldType(positionNdx)
                    );
                部份員工Table.Columns.Add(positionColumn);

                int telNdx = reader.GetOrdinal("電話號碼");
                DataColumn telColumn = new DataColumn(
                    reader.GetName(telNdx), 
                    reader.GetFieldType(telNdx)
                    );
                部份員工Table.Columns.Add(telColumn);

                // 加入記錄
                DataRow newRow = null;
                while (reader.Read())
                {
                    newRow = 部份員工Table.NewRow();

                    newRow[0] = reader.GetValue(nameNdx);
                    newRow[1] = reader.GetString(positionNdx);
                    newRow[2] = reader.GetValue(telNdx);

                    部份員工Table.Rows.Add(newRow);
                }

                reader.Close();

                NorthwindDataSet.Tables.Add(部份員工Table);

                // 秀出剛動態建構出來的DataSet 
                dataGridView2.DataSource = NorthwindDataSet.Tables["部份員工Table"];
            }
        }
    }
}
