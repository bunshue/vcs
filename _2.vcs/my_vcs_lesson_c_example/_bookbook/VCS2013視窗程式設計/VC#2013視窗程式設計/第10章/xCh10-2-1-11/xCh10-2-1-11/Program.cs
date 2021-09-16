using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.OleDb;

namespace xCh10_2_1_11
{
    class Program
    {
        static void Main(string[] args)
        {
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"C:\Northwind.mdb";
            builder["User Id"] = "Admin";

            // 取出員工資料表中所有欄位的內容
            string queryString = "SELECT * FROM 員工";

            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            {
                OleDbCommand command = new OleDbCommand(queryString, connection);
                command.CommandTimeout = 20;

                connection.Open();
                OleDbDataReader reader = command.ExecuteReader();

                while (reader.Read())
                {
                    // 依員工資料表，reader[1]指的是第2欄的姓名欄
                    Console.WriteLine(reader[1].ToString());
                }
                reader.Close();
            }
        }
    }
}
