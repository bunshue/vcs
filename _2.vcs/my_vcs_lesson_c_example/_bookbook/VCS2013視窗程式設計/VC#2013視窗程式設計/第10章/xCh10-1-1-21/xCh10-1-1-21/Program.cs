using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.OleDb;

namespace xCh10_1_1_21
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            * 第一種方式
            */
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder.ConnectionString = @"Data Source=C:\Northwind.mdb";

            // 使用Add()方法以明確地加入key/value pairs
            builder.Add("Provider", "Microsoft.Jet.Oledb.4.0");
            builder.Add("Jet OLEDB:Database Password", "p@ssw0rd");
            builder.Add("Jet OLEDB:System Database", @"C:\Workgroup.mdb");
            Console.WriteLine(builder.ConnectionString);
            Console.WriteLine();

            // 清除所有值，並回復到預設值
            builder.Clear();

            /*
             * 第二種方式
             */
            // 以連線字串設定給ConnectionStrin屬性 
            // 這些值可以被取得，也可以被修改
            builder.ConnectionString =
                "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\\Northwind.mdb;User ID=Admin";
            Console.WriteLine(builder.ConnectionString);
            Console.WriteLine();

            // 呼叫Remove()方法移除key/value pairs 
            builder.Remove("User ID");
            Console.WriteLine(builder.ConnectionString);
            Console.WriteLine();

            // 使用indexer加入新值 
            // necessary.
            builder["User ID"] = "Admin";
            builder["Password"] = "p@ssw0rd";
            Console.WriteLine(builder.ConnectionString);
            Console.WriteLine();

            /*
             * 第三種方式
             */
            // 使用indexer加入必要的key/value pairs
            OleDbConnectionStringBuilder newBuilder = new OleDbConnectionStringBuilder();
            newBuilder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            newBuilder["Data Source"] = "C:\\Northwind.mdb";
            newBuilder["User Id"] = "Admin;NewValue=Bad";
        }
    }
}
