using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.OleDb;

namespace xCh10_1_1_11
{
    class Program
    {
        static void Main(string[] args)
        {
            OpenConnection("Provider=Microsoft.Jet.OLEDB.4.0; Data Source=c:\\Northwind.mdb");
        }

        static void OpenConnection(string connectionString)
        {
            using (OleDbConnection connection = new OleDbConnection(connectionString))
            {
                try
                {
                    connection.Open();

                    Console.WriteLine("連接字串：" + connection.ConnectionString);

                    Console.WriteLine("資料庫： {0} \n伺服器名稱或檔案名稱： {1}",
                         connection.Database, connection.DataSource);

                    Console.WriteLine("伺服器版本： {0} \n提供者名稱：{1}",
                        connection.ServerVersion, connection.Provider);

                    Console.WriteLine("目前的連線狀態：" + connection.State);
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
            }
        }
    }
}
