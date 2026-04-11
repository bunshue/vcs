using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.OleDb;

namespace vcs_OleDb
{
    public partial class Form1 : Form
    {
        //string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            dataGridView1.Size = new Size(620, 400);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            dataGridView2.Size = new Size(620, 400);
            dataGridView2.Location = new Point(x_st + dx * 3, y_st + dy * 6);

            richTextBox1.Size = new Size(400, 800);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1720, 910);
            this.Text = "vcs_OleDb";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //連線OleDb 1, 使用 連線字串

            string connectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\\Northwind.mdb";
            using (OleDbConnection connection = new OleDbConnection(connectionString))  // 連接資料庫
            {
                try
                {
                    connection.Open();

                    richTextBox1.Text += "連接字串：" + connection.ConnectionString + "\n";
                    richTextBox1.Text += string.Format("資料庫： {0} 伺服器名稱或檔案名稱： {1}", connection.Database, connection.DataSource) + "\n";
                    richTextBox1.Text += string.Format("伺服器版本： {0} 提供者名稱：{1}", connection.ServerVersion, connection.Provider) + "\n";
                    richTextBox1.Text += "目前的連線狀態：" + connection.State + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //連線OleDb 2, 使用 OleDbConnectionStringBuilder

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //OleDb
            //第一種方式

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder.ConnectionString = @"Data Source=D:\Northwind.mdb";

            // 使用Add()方法以明確地加入key/value pairs
            builder.Add("Provider", "Microsoft.Jet.Oledb.4.0");
            builder.Add("Jet OLEDB:Database Password", "p@ssw0rd");
            builder.Add("Jet OLEDB:System Database", @"C:\Workgroup.mdb");
            richTextBox1.Text += builder.ConnectionString + "\n";

            // 清除所有值，並回復到預設值
            builder.Clear();

            //第二種方式
            // 以連線字串設定給ConnectionStrin屬性 
            // 這些值可以被取得，也可以被修改
            builder.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\\Northwind.mdb;User ID=Admin";
            richTextBox1.Text += builder.ConnectionString + "\n";

            // 呼叫Remove()方法移除key/value pairs 
            builder.Remove("User ID");
            richTextBox1.Text += builder.ConnectionString + "\n";

            // 使用indexer加入新值 
            // necessary.
            builder["User ID"] = "Admin";
            builder["Password"] = "p@ssw0rd";
            richTextBox1.Text += builder.ConnectionString + "\n";

            //第三種方式
            // 使用indexer加入必要的key/value pairs
            builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\Northwind.mdb";
            builder["User Id"] = "Admin;NewValue=Bad";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"D:\Northwind.mdb";
            builder["User Id"] = "Admin";

            // 取出員工資料表中所有欄位的內容
            string queryString = "SELECT * FROM 員工";  // 設定SQL語句

            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))  // 連接資料庫
            {
                OleDbCommand command = new OleDbCommand(queryString, connection);//執行SQL語句
                command.CommandTimeout = 20;

                connection.Open();
                OleDbDataReader reader = command.ExecuteReader();

                while (reader.Read())
                {
                    // 依員工資料表，reader[1]指的是第2欄的姓名欄
                    richTextBox1.Text += reader[1].ToString() + "\n";
                }
                reader.Close();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //OleDb
            //DataAdapter的Fill方法範例

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"D:\Northwind.mdb";
            builder["User Id"] = "Admin";

            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))  // 連接資料庫
            {
                string queryString = "SELECT * FROM 供應商";  // 設定SQL語句

                OleDbCommand command = new OleDbCommand(builder.ConnectionString);//執行SQL語句
                connection.Open();

                // 建構DataSet及其組成分子
                DataSet NorthwindDataSet = new DataSet();
                OleDbDataAdapter myAdapter = new OleDbDataAdapter(queryString, connection);
                myAdapter.Fill(NorthwindDataSet, "供應商Table");

                // 秀出剛動態建構出來的DataSet 
                dataGridView1.DataSource = NorthwindDataSet.Tables["供應商Table"];

                queryString = "SELECT * FROM 員工";  // 設定SQL語句
                myAdapter = new OleDbDataAdapter(queryString, connection);
                myAdapter.Fill(NorthwindDataSet, "員工Table");

                // 秀出剛動態建構出來的DataSet
                dataGridView2.DataSource = NorthwindDataSet.Tables["員工Table"];
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //DataAdapter的SelectCommand範例

            //取得資料
            //城市:
            //"宜蘭市","台北市","台北縣","桃園縣",
            //"新竹市","苗栗縣","台中市","南投縣市",
            //"高雄市","屏東縣","屏東市","花蓮市"

            string cityParam = "新竹市";

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"D:\Northwind.mdb";
            builder["User Id"] = "Admin";

            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))  // 連接資料庫
            {
                connection.Open();

                OleDbCommand command;
                // 設定SQL語句
                command = new OleDbCommand("SELECT * FROM 客戶 " + "WHERE 城市 = ?", connection);//執行SQL語句
                command.Parameters.Add("城市", OleDbType.VarChar, 6);

                command.Parameters["城市"].Value = cityParam;

                OleDbDataAdapter myAdapter = new OleDbDataAdapter();
                myAdapter.SelectCommand = command;

                // 建構DataSet及其組成分子
                DataSet NorthwindDataSet = new DataSet();
                myAdapter.Fill(NorthwindDataSet, "客戶Table");

                // 秀出剛動態建構出來的DataSet 
                dataGridView1.DataSource = NorthwindDataSet.Tables["客戶Table"];
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //取得資料
            OleDbConnectionStringBuilder builder;
            string queryString;
            //string connectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\\Northwind.mdb";
            builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"D:\Northwind2.mdb";
            builder["User Id"] = "Admin";

            // 取出員工資料表中所有欄位的內容
            queryString = "SELECT * FROM 員工";

            string connectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\\Northwind2.mdb";

            //using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            using (OleDbConnection connection = new OleDbConnection(connectionString))
            {
                OleDbCommand command = new OleDbCommand(queryString, connection);
                command.CommandTimeout = 20;

                connection.Open();
                OleDbDataReader reader = command.ExecuteReader();

                richTextBox1.Text += "是否包含一個或多個資料列：" + (reader.HasRows ? "是" : "否") + "\n";
                richTextBox1.Text += "目前資料列中的資料行數目：" + reader.FieldCount.ToString() + "\n";
                richTextBox1.Text += "資料讀取器是否關閉：" + (reader.IsClosed ? "是" : "否") + "\n";

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
                richTextBox1.Text += "共有 " + count.ToString() + " 筆記錄\n";

                reader.Close();
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //取得部分資料
            OleDbConnectionStringBuilder builder;
            string queryString;
            //string connectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\\Northwind.mdb";
            builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"D:\Northwind2.mdb";
            builder["User Id"] = "Admin";

            // 取出員工資料表中所有欄位的內容
            queryString = "SELECT * FROM 員工";

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
                DataColumn nameColumn = new DataColumn(reader.GetName(nameNdx), reader.GetFieldType(nameNdx));
                部份員工Table.Columns.Add(nameColumn);

                int positionNdx = reader.GetOrdinal("職稱");
                DataColumn positionColumn = new DataColumn(reader.GetName(positionNdx), reader.GetFieldType(positionNdx));
                部份員工Table.Columns.Add(positionColumn);

                int telNdx = reader.GetOrdinal("電話號碼");
                DataColumn telColumn = new DataColumn(reader.GetName(telNdx), reader.GetFieldType(telNdx));
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

        private void button7_Click(object sender, EventArgs e)
        {
            //Command.Parameters範例
            //取得供應商資料
            /*
            "宜蘭","台北","桃園","新竹","苗栗",
            "台中","南投","高雄","屏東","花蓮"
            */

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"D:\Northwind.mdb";
            builder["User Id"] = "Admin";
            string queryString = "SELECT * FROM 供應商 WHERE 供應商=@supplier OR 行政區=@district";

            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            {
                connection.Open();

                OleDbCommand command = new OleDbCommand(queryString, connection);
                OleDbParameter supplierParam = command.Parameters.Add("@supplier", OleDbType.Char);
                supplierParam.Value = "一心";
                // 以上二道敘述的寫法，可縮寫如下：
                // command.Parameters.Add("@supplier", OleDbType.Char).Value = "一心";

                // 如果有從ComboBox中挑選行政區，則將該值設定給做為篩選條件的distric
                // 否則就提示使用者，並中斷事件這個事件處理程序

                string district = "新竹";
                command.Parameters.AddWithValue("@district", district);

                OleDbDataReader reader = command.ExecuteReader();

                // 建構DataSet及其組成分子
                DataSet NorthwindDataSet = new DataSet();
                DataTable 供應商Table = new DataTable("供應商Table");
                DataColumn aColumn;
                for (int i = 0; i < reader.FieldCount; i++)
                {
                    aColumn = new DataColumn(reader.GetName(i), reader.GetFieldType(i));
                    供應商Table.Columns.Add(aColumn);
                }

                // 加入記錄
                DataRow newRow = null;
                while (reader.Read())
                {
                    newRow = 供應商Table.NewRow();
                    for (int i = 0; i < reader.FieldCount; i++)
                    {
                        newRow[i] = reader.GetValue(i);// 相當於reader[i];
                    }
                    供應商Table.Rows.Add(newRow);
                }
                NorthwindDataSet.Tables.Add(供應商Table);

                // 秀出剛動態建構出來的DataSet 
                dataGridView1.DataSource = NorthwindDataSet.Tables["供應商Table"];
                reader.Close();
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        OleDbConnectionStringBuilder builder;
        OleDbConnection connection;
        OleDbCommand command;
        OleDbParameter parameter;
        OleDbDataAdapter myAdapter;
        DataSet NorthwindDataSet;

        private void DataChanged()
        {
            NorthwindDataSet = new DataSet();
            myAdapter.Fill(NorthwindDataSet, "客戶Table");
            dataGridView1.DataSource = NorthwindDataSet.Tables["客戶Table"];
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //ExecuteNonQuery範例(4)

            //(1/4)讀取

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"D:\Northwind.mdb";
            builder["User Id"] = "Admin";

            connection = new OleDbConnection(builder.ConnectionString);
            connection.Open();

            // 取出所有客戶資料並交由DataGridView物件顯示
            myAdapter = new OleDbDataAdapter("SELECT * FROM 客戶", connection);
            NorthwindDataSet = new DataSet();
            myAdapter.Fill(NorthwindDataSet, "客戶Table");
            dataGridView1.DataSource = NorthwindDataSet.Tables["客戶Table"];

        }

        private void button11_Click(object sender, EventArgs e)
        {
            string customer_id = "12345";
            string company_name = "lion-mouse";
            //新增
            // 建構Insert
            command = new OleDbCommand();
            command.CommandText = "INSERT INTO 客戶 (客戶編號, 公司名稱) VALUES (?, ?)";
            command.Connection = connection;

            command.Parameters.Add("CustomerID", OleDbType.Char, 5);
            command.Parameters.Add("CompanyName", OleDbType.VarChar, 40);
            command.Parameters["CustomerID"].Value = customer_id;//客戶編號
            command.Parameters["CompanyName"].Value = company_name;//公司名稱
            command.ExecuteNonQuery();

            NorthwindDataSet.Tables["客戶Table"].AcceptChanges();
            DataChanged();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            string customer_id = "12345";
            string company_name_new = "cat-dog";

            //修改
            // 建構Update
            command = new OleDbCommand();
            command.CommandText =
                "UPDATE 客戶 SET " +
                    "客戶編號 = @CustomerID, " +
                    "公司名稱 = @CompanyName " +
                    "WHERE 客戶編號 = @CustomerID";
            command.Connection = connection;

            command.Parameters.Add("@CustomerID", OleDbType.Char, 5);
            command.Parameters.Add("@CompanyName", OleDbType.VarChar, 40);
            command.Parameters["@CustomerID"].Value = customer_id;//客戶編號
            command.Parameters["@CompanyName"].Value = company_name_new;//公司名稱

            command.ExecuteNonQuery();
            DataChanged();

        }

        private void button13_Click(object sender, EventArgs e)
        {
            string customer_id = "12345";
            //刪除
            // 建構Delete
            command = new OleDbCommand();
            command.CommandText = "DELETE * FROM 客戶 " + "WHERE 客戶編號 = @CustomerID";
            command.Connection = connection;

            parameter = command.Parameters.Add("@CustomerID", OleDbType.Char, 5);
            command.Parameters["@CustomerID"].Value = customer_id;//客戶編號
            command.ExecuteNonQuery();

            NorthwindDataSet.Tables["客戶Table"].AcceptChanges();
            DataChanged();
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

 */
