using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
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

            int dd = 26;
            dataGridView1.Size = new Size(510, 380);
            dataGridView2.Size = new Size(510, 380);
            dataGridView3.Size = new Size(420, 380);
            dataGridView4.Size = new Size(420, 380);

            lb_dgv1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd);
            lb_dgv2.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            dataGridView2.Location = new Point(x_st + dx * 3, y_st + dy * 6 + dd);
            lb_dgv3.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0);
            dataGridView3.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0 + dd);
            lb_dgv4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6);
            dataGridView4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6 + dd);
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
            lb_dgv3.Text = "";
            lb_dgv4.Text = "";

            richTextBox1.Size = new Size(300, 820);
            richTextBox1.Location = new Point(x_st + dx * 7 + 110, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1920, 890);
            this.Text = "vcs_OleDb";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            dataGridView1.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView2.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView3.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView4.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
            lb_dgv3.Text = "";
            lb_dgv4.Text = "";
        }

        void oledb_read_database(string db_filename, string sqlstr, DataGridView dgv)
        {
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";
            richTextBox1.Text += "aaaa : " + builder.ConnectionString + "\n";

            //讀取資料庫至DGV
            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                OleDbCommand cmd = new OleDbCommand(builder.ConnectionString);
                cn.Open();

                // 建構DataSet及其組成分子
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                OleDbDataAdapter da = new OleDbDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                // da.Fill(ds, "table");  // da將查詢的結果填充至數據集ds, 指定TableName為"table"
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName

                //dgv.DataSource = ds.Tables["table"];  // DGV設置數據源, same
                dgv.DataSource = ds.Tables[0];  // DGV設置數據源
            }

            if (dgv == dataGridView1)
            {
                lb_dgv1.Text = "";
                lb_dgv2.Text = "";
                lb_dgv3.Text = "";
                lb_dgv4.Text = "";
            }
            else if (dgv == dataGridView2)
                lb_dgv2.Text = "";
            else if (dgv == dataGridView3)
                lb_dgv3.Text = "";
            else if (dgv == dataGridView4)
                lb_dgv4.Text = "";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\\Northwind.mdb";
            using (OleDbConnection cn = new OleDbConnection(cnstr))  // 建立資料庫連接對象cn
            {
                richTextBox1.Text += "連線字串 : " + cnstr + "\n";
                try
                {
                    cn.Open();

                    richTextBox1.Text += "連接字串：" + cn.ConnectionString + "\n";
                    richTextBox1.Text += string.Format("資料庫： {0} 伺服器名稱或檔案名稱： {1}", cn.Database, cn.DataSource) + "\n";
                    richTextBox1.Text += string.Format("伺服器版本： {0} 提供者名稱：{1}", cn.ServerVersion, cn.Provider) + "\n";
                    richTextBox1.Text += "目前的連線狀態：" + cn.State + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                }
            }

            //6060




        }

        private void button1_Click(object sender, EventArgs e)
        {
            //OleDb
            //第一種方式

            string db_filename = "Northwind.mdb";

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";

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

            db_filename = "Northwind.mdb";

            builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin;NewValue=Bad";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "Northwind.mdb";

            // 查詢字串
            string sqlstr = "SELECT * FROM 員工";
            oledb_read_database(db_filename, sqlstr, dataGridView1);

            //3030

            db_filename = "Northwind.mdb";

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";

            // 查詢字串, 取出員工資料表中所有欄位的內容
            sqlstr = "SELECT * FROM 員工";

            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
                cmd.CommandTimeout = 20;

                cn.Open();
                OleDbDataReader dr = cmd.ExecuteReader();

                while (dr.Read())
                {
                    // 依員工資料表，dr[1]指的是第2欄的姓名欄
                    richTextBox1.Text += dr[1].ToString() + "\n";
                }
                dr.Close();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "Northwind.mdb";

            // 查詢字串
            string sqlstr = "SELECT * FROM 供應商";
            oledb_read_database(db_filename, sqlstr, dataGridView1);

            // 查詢字串
            sqlstr = "SELECT * FROM 員工";
            oledb_read_database(db_filename, sqlstr, dataGridView2);
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

            string db_filename = "Northwind.mdb";
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";

            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                cn.Open();

                // 查詢字串
                string sqlstr = "xxxxx";

                OleDbCommand cmd = new OleDbCommand("SELECT * FROM 客戶 " + "WHERE 城市 = ?", cn);
                cmd.Parameters.Add("城市", OleDbType.VarChar, 6);
                cmd.Parameters["城市"].Value = cityParam;

                OleDbDataAdapter da = new OleDbDataAdapter();  // 建立資料庫適配器對象da
                da.SelectCommand = cmd;

                // 建構DataSet及其組成分子
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "客戶Table");

                // 秀出剛動態建構出來的DataSet 
                dataGridView1.DataSource = ds.Tables["客戶Table"];
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string db_filename = "Northwind2.mdb";

            //取得資料
            string sqlstr;
            //string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\\Northwind.mdb";
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";

            // 查詢字串, 取出員工資料表中所有欄位的內容
            sqlstr = "SELECT * FROM 員工";

            string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\\Northwind2.mdb";

            //using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            using (OleDbConnection cn = new OleDbConnection(cnstr))  // 建立資料庫連接對象cn
            {
                OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
                cmd.CommandTimeout = 20;

                cn.Open();
                OleDbDataReader dr = cmd.ExecuteReader();

                richTextBox1.Text += "是否包含一個或多個資料列：" + (dr.HasRows ? "是" : "否") + "\n";
                richTextBox1.Text += "目前資料列中的資料行數目：" + dr.FieldCount.ToString() + "\n";
                richTextBox1.Text += "資料讀取器是否關閉：" + (dr.IsClosed ? "是" : "否") + "\n";

                // 建構DataSet及其組成分子
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                DataTable 員工Table = new DataTable("員工Table");
                DataColumn aColumn;

                for (int i = 0; i < dr.FieldCount; i++)
                {
                    aColumn = new DataColumn(dr.GetName(i), dr.GetFieldType(i));
                    員工Table.Columns.Add(aColumn);
                }

                // 加入記錄
                DataRow newRow = null;
                while (dr.Read())
                {
                    newRow = 員工Table.NewRow();
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        newRow[i] = dr.GetValue(i);// 相當於dr[i];
                    }
                    員工Table.Rows.Add(newRow);
                }

                ds.Tables.Add(員工Table);

                // 秀出剛動態建構出來的DataSet 
                dataGridView1.DataSource = ds.Tables["員工Table"];

                dr.Close();

                // 執行查詢，並傳回查詢所傳回的結果集中第一個資料列的第一個資料行。
                // 會忽略其他的資料行或資料列。
                cmd.CommandText = "SELECT COUNT(*) FROM 員工";
                int count = (Int32)cmd.ExecuteScalar();
                richTextBox1.Text += "共有 " + count.ToString() + " 筆記錄\n";

                dr.Close();
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //取得部分資料

            string db_filename = "Northwind2.mdb";

            string sqlstr;
            //string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\\Northwind.mdb";
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";

            // 查詢字串, 取出員工資料表中所有欄位的內容
            sqlstr = "SELECT * FROM 員工";

            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
                cmd.CommandTimeout = 20;

                cn.Open();
                OleDbDataReader dr = cmd.ExecuteReader();

                // 建構DataSet及其組成分子
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                DataTable 部份員工Table = new DataTable("部份員工Table");

                int nameNdx = dr.GetOrdinal("姓名");
                DataColumn nameColumn = new DataColumn(dr.GetName(nameNdx), dr.GetFieldType(nameNdx));
                部份員工Table.Columns.Add(nameColumn);

                int positionNdx = dr.GetOrdinal("職稱");
                DataColumn positionColumn = new DataColumn(dr.GetName(positionNdx), dr.GetFieldType(positionNdx));
                部份員工Table.Columns.Add(positionColumn);

                int telNdx = dr.GetOrdinal("電話號碼");
                DataColumn telColumn = new DataColumn(dr.GetName(telNdx), dr.GetFieldType(telNdx));
                部份員工Table.Columns.Add(telColumn);

                // 加入記錄
                DataRow newRow = null;
                while (dr.Read())
                {
                    newRow = 部份員工Table.NewRow();

                    newRow[0] = dr.GetValue(nameNdx);
                    newRow[1] = dr.GetString(positionNdx);
                    newRow[2] = dr.GetValue(telNdx);

                    部份員工Table.Rows.Add(newRow);
                }

                dr.Close();

                ds.Tables.Add(部份員工Table);

                // 秀出剛動態建構出來的DataSet 
                dataGridView2.DataSource = ds.Tables["部份員工Table"];
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

            string db_filename = "Northwind.mdb";

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";

            // 查詢字串
            string sqlstr = "SELECT * FROM 供應商 WHERE 供應商=@supplier OR 行政區=@district";

            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                cn.Open();

                OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
                OleDbParameter supplierParam = cmd.Parameters.Add("@supplier", OleDbType.Char);
                supplierParam.Value = "一心";
                // 以上二道敘述的寫法，可縮寫如下：
                // cmd.Parameters.Add("@supplier", OleDbType.Char).Value = "一心";

                // 如果有從ComboBox中挑選行政區，則將該值設定給做為篩選條件的distric
                // 否則就提示使用者，並中斷事件這個事件處理程序

                string district = "新竹";
                cmd.Parameters.AddWithValue("@district", district);

                OleDbDataReader dr = cmd.ExecuteReader();

                // 建構DataSet及其組成分子
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                DataTable 供應商Table = new DataTable("供應商Table");
                DataColumn aColumn;
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    aColumn = new DataColumn(dr.GetName(i), dr.GetFieldType(i));
                    供應商Table.Columns.Add(aColumn);
                }

                // 加入記錄
                DataRow newRow = null;
                while (dr.Read())
                {
                    newRow = 供應商Table.NewRow();
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        newRow[i] = dr.GetValue(i);// 相當於dr[i];
                    }
                    供應商Table.Rows.Add(newRow);
                }
                ds.Tables.Add(供應商Table);

                // 秀出剛動態建構出來的DataSet 
                dataGridView1.DataSource = ds.Tables["供應商Table"];
                dr.Close();
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //OleDb
            //连接加密的Access数据库

            //Access 資料庫 *.mdb
            //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db_Test.mdb";

            // 找一下 db.mdb
            string db_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\vcs精彩編程200例\05\158\ConProAccess\db.mdb";
            db_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db_Test.mdb";

            string password = "12345";
            // 連接字串
            string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + db_filename + ";JET OLEDB:Database Password=" + password + ";";
            richTextBox1.Text += "cnstr : " + cnstr + "\n";
            cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + db_filename + ";";//连接无密码的数据库
            richTextBox1.Text += "cnstr : " + cnstr + "\n";

            using (OleDbConnection cn = new OleDbConnection(cnstr))  // 建立資料庫連接對象cn
            {
                try
                {
                    cn.Open();//打开数据库连接
                    richTextBox1.Clear();//清空文本框
                    richTextBox1.Text = cnstr + "\n连接成功……";// 顯示 連接字串
                }
                catch
                {
                    richTextBox1.Text = "连接失败";
                }
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        OleDbConnection cn;
        OleDbCommand cmd;
        OleDbParameter parameter;
        OleDbDataAdapter da;
        DataSet ds;

        private void DataChanged()
        {
            ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            da.Fill(ds, "客戶Table");
            dataGridView1.DataSource = ds.Tables["客戶Table"];
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //ExecuteNonQuery範例(4)

            //(1/4)讀取

            string db_filename = "Northwind.mdb";

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";

            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();

            // 取出所有客戶資料並交由DataGridView物件顯示
            da = new OleDbDataAdapter("SELECT * FROM 客戶", cn);  // 建立資料庫適配器對象da
            ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            da.Fill(ds, "客戶Table");
            dataGridView1.DataSource = ds.Tables["客戶Table"];
        }

        private void button11_Click(object sender, EventArgs e)
        {
            string customer_id = "12345";
            string company_name = "lion-mouse";
            //新增
            // 建構Insert
            cmd = new OleDbCommand();
            cmd.CommandText = "INSERT INTO 客戶 (客戶編號, 公司名稱) VALUES (?, ?)";
            cmd.Connection = cn;

            cmd.Parameters.Add("CustomerID", OleDbType.Char, 5);
            cmd.Parameters.Add("CompanyName", OleDbType.VarChar, 40);
            cmd.Parameters["CustomerID"].Value = customer_id;//客戶編號
            cmd.Parameters["CompanyName"].Value = company_name;//公司名稱
            cmd.ExecuteNonQuery();

            ds.Tables["客戶Table"].AcceptChanges();
            DataChanged();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            string customer_id = "12345";
            string company_name_new = "cat-dog";

            //修改
            // 建構Update
            cmd = new OleDbCommand();
            cmd.CommandText =
                "UPDATE 客戶 SET " +
                    "客戶編號 = @CustomerID, " +
                    "公司名稱 = @CompanyName " +
                    "WHERE 客戶編號 = @CustomerID";
            cmd.Connection = cn;

            cmd.Parameters.Add("@CustomerID", OleDbType.Char, 5);
            cmd.Parameters.Add("@CompanyName", OleDbType.VarChar, 40);
            cmd.Parameters["@CustomerID"].Value = customer_id;//客戶編號
            cmd.Parameters["@CompanyName"].Value = company_name_new;//公司名稱

            cmd.ExecuteNonQuery();

            DataChanged();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            string customer_id = "12345";
            //刪除
            // 建構Delete
            cmd = new OleDbCommand();
            cmd.CommandText = "DELETE * FROM 客戶 " + "WHERE 客戶編號 = @CustomerID";
            cmd.Connection = cn;

            parameter = cmd.Parameters.Add("@CustomerID", OleDbType.Char, 5);
            cmd.Parameters["@CustomerID"].Value = customer_id;//客戶編號
            cmd.ExecuteNonQuery();

            ds.Tables["客戶Table"].AcceptChanges();

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
            //讀取EXCEL檔案
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\excel_20210602_131921.xls";

            //string filename = pathFile + ".xls";
            if (File.Exists(filename) == false)
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在，無法開啟。\n";
                return;
            }
            else
            {
                richTextBox1.Text += "開啟檔案: " + filename + "\n";
            }

            //string xlsPath = @"C:\tttt.xls";

            //string sheetName = "Sheet1";

            /*步驟1：設定Excel的屬性、路徑*/
            //設定讀取的Excel屬性
            string strCon = "Provider=Microsoft.Jet.OLEDB.4.0;" +
                //路徑(檔案讀取路徑)
            "Data Source=D:\\_git\\vcs\\_1.data\\______test_files1\\__RW\\_excel\\vcs_test_excel.xls;" +
                //選擇Excel版本
                //Excel 12.0 針對Excel 2010、2007版本(OLEDB.12.0)
                //Excel 8.0 針對Excel 97-2003版本(OLEDB.4.0)
                //Excel 5.0 針對Excel 97(OLEDB.4.0)
            "Extended Properties='Excel 8.0;" +
                //開頭是否為資料
                //若指定值為 Yes，代表 Excel 檔中的工作表第一列是欄位名稱，oleDB直接從第二列讀取
                //若指定值為 No，代表 Excel 檔中的工作表第一列就是資料了，沒有欄位名稱，oleDB直接從第一列讀取
            "HDR=NO;" +
                //IMEX=0 為「匯出模式」，能對檔案進行寫入的動作。
                //IMEX=1 為「匯入模式」，能對檔案進行讀取的動作。
                //IMEX=2 為「連結模式」，能對檔案進行讀取與寫入的動作。
            "IMEX=1'";
            /*步驟2：依照Excel的屬性及路徑開啟檔案*/
            //Excel路徑及相關資訊匯入
            OleDbConnection GetXLS = new OleDbConnection(strCon);
            //打開檔案
            GetXLS.Open();
            /*步驟3：搜尋此Excel的所有工作表，找到特定工作表進行讀檔，並將其資料存入List*/
            //搜尋xls的工作表(工作表名稱需要加$字串)
            DataTable Table = GetXLS.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null);
            //查詢此Excel所有的工作表名稱
            string SelectSheetName = "";
            foreach (DataRow row in Table.Rows)
            {
                //抓取Xls各個Sheet的名稱(+'$')-有的名稱需要加名稱''，有的不用
                SelectSheetName = (string)row["TABLE_NAME"];
                richTextBox1.Text += "\n" + "工作表: " + SelectSheetName + "\n";
                //工作表名稱有特殊字元、空格，需加'工作表名稱$'，ex：'Sheet_A$'
                //工作表名稱沒有特殊字元、空格，需加工作表名稱$，ex：SheetA$
                //所有工作表名稱為Sheet1，讀取此工作表的內容
                //if (SelectSheetName == "SheetA$")
                if (SelectSheetName == "Sheet1$")   //第一頁
                {
                    //select 工作表名稱
                    OleDbCommand cmSheetA = new OleDbCommand(" SELECT * FROM [Sheet1$] ", GetXLS);
                    OleDbDataReader drSheetA = cmSheetA.ExecuteReader();

                    //讀取工作表SheetA資料
                    //List<string> ListSheetA = new List<string>();
                    int cnt = 0;
                    while (drSheetA.Read())
                    {
                        //工作表SheetA的資料存入List
                        //ListSheetA.Add(drSheetA[cnt].ToString());
                        richTextBox1.Text += "列" + cnt.ToString() + "\t" + drSheetA[0].ToString() + "\t" + drSheetA[1].ToString() + "\t" + drSheetA[2].ToString() + "\n";
                        cnt++;
                    }
                    /*步驟4：關閉檔案*/
                    //結束關閉讀檔(必要，不關會有error)
                    drSheetA.Close();
                    GetXLS.Close();
                }
            }
        }

        //6060

        private void button21_Click(object sender, EventArgs e)
        {
            //讀取EXCEL檔案到dataGridView
            //sugar can not use this
            //Excel數據導入到dataGridView
            //http://weisico.com/program/2018/0531/370.html

            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\vcs_ReadWrite_EXCEL2.xls";

            try
            {
                string tableName = GetExcelFirstTableName(filename);
                richTextBox1.Text += "tableName = " + tableName + "\n";
                //設置T_Sql
                string TSql = "SELECT  * FROM [" + tableName + "]";
                richTextBox1.Text += "TSql = " + TSql + "\n";
                //讀取數據
                DataTable table = ExcelToDataSet(filename, TSql).Tables[0];
                dataGridView1.DataSource = table;

                int cols = table.Columns.Count;
                int rows = table.Rows.Count;
                richTextBox1.Text += "cols = " + cols.ToString() + "\n";
                richTextBox1.Text += "rows = " + rows.ToString() + "\n";
                int i;
                int j;
                for (i = 0; i < cols; i++)
                {
                    richTextBox1.Text += table.Columns[i] + "\t";
                }
                richTextBox1.Text += "\n";
                for (i = 0; i < rows; i++)
                {
                    for (j = 0; j < cols; j++)
                    {
                        richTextBox1.Text += table.Rows[i][j] + "\t";
                    }
                    richTextBox1.Text += "\n";
                }
                richTextBox1.Text += "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        /// <summary>
        /// 動態取Excel表名
        /// </summary>
        /// <param name="fullPath">文件路徑</param>
        /// <returns></returns>
        public string GetExcelFirstTableName(string fullPath)
        {
            string tableName = null;
            if (File.Exists(fullPath))
            {
                using (OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + fullPath))
                {
                    conn.Open();

                    richTextBox1.Text += "t0 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][0].ToString().Trim() + "\n";
                    richTextBox1.Text += "t1 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][1].ToString().Trim() + "\n";

                    richTextBox1.Text += "s1 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][2].ToString().Trim() + "\n";
                    richTextBox1.Text += "s2 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[1][2].ToString().Trim() + "\n";
                    richTextBox1.Text += "s3 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[2][2].ToString().Trim() + "\n";

                    richTextBox1.Text += "t3 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][3].ToString().Trim() + "\n";

                    richTextBox1.Text += "\n\n";

                    tableName = conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][2].ToString().Trim();
                    richTextBox1.Text += "GetExcelFirstTableName tableName = " + tableName + "\n";
                }
            }
            return tableName;
        }


        /// <summary>
        /// 返回Excel數據源
        /// </summary>
        /// <param name="filename">文件路徑</param>
        /// <param name="TSql">TSql</param>
        /// <returns>DataSet</returns>
        public static DataSet ExcelToDataSet(string filename, string TSql)
        {
            DataSet ds;
            string strCon = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;data source=" + filename;
            OleDbConnection myConn = new OleDbConnection(strCon);
            string strCom = TSql;
            myConn.Open();
            OleDbDataAdapter myCommand = new OleDbDataAdapter(strCom, myConn);
            ds = new DataSet();
            myCommand.Fill(ds);
            myConn.Close();
            return ds;
        }

        //6060
        //配置Excel的OleDb連接字符串
        public const string OledbConnString = "Provider = Microsoft.Jet.OLEDB.4.0 ; Data Source = {0};Extended Properties='Excel 8.0;HDR=Yes;IMEX=1;'"; //Excel的 OleDb 連接字符串

        private void button22_Click(object sender, EventArgs e)
        {
            //讀取EXCEL檔案到dataGridView
            //讀取EXCEL檔案到dataGridView
            //another
            //C# Excel文件導入操作

            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\excel_test_data.xls";

            richTextBox1.Text += "開啟檔案 : " + filename + "\n";

            DataTable excelTbl = this.GetExcelTable(filename);  //調用函數獲取Excel中的信息
            if (excelTbl == null)
            {
                return;
            }

            dataGridView1.DataSource = excelTbl;
        }

        /// 
        /// 獲取Excel文件中的信息，保存到一個DataTable中
        /// 

        /// 文件路徑
        /// 返回生成的DataTable
        private DataTable GetExcelTable(string path)
        {
            try
            {
                //獲取excel數據
                DataTable dt1 = new DataTable("excelTable");
                string strConn = string.Format(OledbConnString, path);
                OleDbConnection conn = new OleDbConnection(strConn);
                conn.Open();
                DataTable dt = conn.GetSchema("Tables");
                //判斷excel的sheet頁數量，查詢第1頁
                if (dt.Rows.Count > 0)
                {
                    string selSqlStr = string.Format("select * from [{0}]", dt.Rows[0]["TABLE_NAME"]);
                    OleDbDataAdapter oleDa = new OleDbDataAdapter(selSqlStr, conn);
                    oleDa.Fill(dt1);
                }
                conn.Close();
                return dt1;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Excel轉換DataTable出錯：" + ex.Message);
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                return null;
            }
        }

        //6060

        //顯示資料庫的內容 ST
        void show_dataset_content(DataSet ds)
        {
            richTextBox1.Text += "顯示資料庫的內容\n";

            richTextBox1.Text += "Tables.Count = " + ds.Tables.Count.ToString() + "\n";
            richTextBox1.Text += "Columns = " + ds.Tables[0].Columns.Count.ToString() + "\n";
            richTextBox1.Text += "Rows = " + ds.Tables[0].Rows.Count.ToString() + "\n";
            richTextBox1.Text += "TableName = " + ds.Tables[0].TableName + "\n\n";

            richTextBox1.Text += "標題\n";
            int i;
            int j;
            int C = ds.Tables[0].Columns.Count;
            int R = ds.Tables[0].Rows.Count;
            for (i = 0; i < C; i++)
            {
                richTextBox1.Text += ds.Tables[0].Columns[i] + "\t";
            }
            richTextBox1.Text += "\n\n";

            richTextBox1.Text += "內容\n";
            for (j = 0; j < R; j++)
            {
                for (i = 0; i < C; i++)
                {
                    richTextBox1.Text += ds.Tables[0].Rows[j].ItemArray[i] + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }
        //顯示資料庫的內容 SP

        private void button23_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db_09.mdb";

            //"Provider=Microsoft.Jet.OleDb.4.0;"是指數據提供者,這裡使用的是Microsoft Jet引擎,也就是Access中的數據引擎,asp.net就是靠這個和Access的數據庫連接的.
            //"Data Source=XXXXX.mdb"是指明數據源的位置

            string connection_string = "Provider=Microsoft.ACE.OLEDB.12.0;Data source=" + filename;  //sugar
            //string connection_string = "Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + filename;     //kilo

            OleDbConnection connection = new OleDbConnection(connection_string);

            connection.Open();  // 打開數據庫連接

            OleDbDataAdapter OleDat = new OleDbDataAdapter("select * from 帳目", connection);
            DataSet ds = new DataSet();
            OleDat.Fill(ds, "帳目");
            this.dataGridView1.DataSource = ds.Tables[0].DefaultView;   //將所有資料都匯出到dataGridView上

            show_dataset_content(ds);   //顯示資料庫的內容

            connection.Close(); // 關閉數據庫連接

            connection.Dispose();
        }

        //6060

        private void button24_Click(object sender, EventArgs e)
        {
            return; //TBD

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db_09.mdb";

            string connection_string = "Provider=Microsoft.ACE.OLEDB.12.0;Data source=" + filename;  //sugar
            //string connection_string = "Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + filename;     //kilo

            OleDbConnection connection = new OleDbConnection(connection_string);

            OleDbDataReader reader;

            // 獲得Person裡面的所以數據記錄

            string strCommand = "SELECT * FROM Persons";

            connection.Open();  // 打開數據連接

            OleDbCommand cmd = new OleDbCommand(strCommand, connection);

            reader = cmd.ExecuteReader();   //獲得數據集

            /*
            //（2）.對列表進行初始化，並使得列表的顯示條件符合數據記錄的條件。需要說明的是在下面源代碼中，lv是在Class中定義的一個ListView的一個實例

            // 初始化ListView

            listView1.Left = 0;

            listView1.Top = 0;

            listView1.Width = 700;

            //listView1.Height = this.ClientRectangle.Height ;

            listView1.GridLines = true;	//顯示各個記錄的分隔線

            listView1.FullRowSelect = true;	//要選擇就是一行

            listView1.View = View.Details;	//定義列表顯示的方式

            listView1.Scrollable = true;	//需要時候顯示滾動條

            listView1.MultiSelect = false; // 不可以多行選擇

            listView1.HeaderStyle = ColumnHeaderStyle.Nonclickable;

            // 針對數據庫的字段名稱，建立與之適應顯示表頭

            listView1.Columns.Add("姓名", 60, HorizontalAlignment.Right);

            listView1.Columns.Add("住宅電話", 100, HorizontalAlignment.Left);


            listView1.Columns.Add("辦公電話", 100, HorizontalAlignment.Left);

            listView1.Columns.Add("移動電話", 100, HorizontalAlignment.Left);

            listView1.Columns.Add("居住地點", 100, HorizontalAlignment.Left);

            listView1.Columns.Add("工作單位", 100, HorizontalAlignment.Left);

            listView1.Columns.Add("電子郵件", 100, HorizontalAlignment.Left);

            listView1.Visible = true;

            while (reader.Read())
            {

                ListViewItem li = new ListViewItem();

                li.SubItems.Clear();

                li.SubItems[0].Text = reader["name"].ToString();

                li.SubItems.Add(reader["HomePhone"].ToString());


                li.SubItems.Add(reader["WorkPhone"].ToString());

                li.SubItems.Add(reader["MobilePhone"].ToString());

                li.SubItems.Add(reader["City"].ToString());

                li.SubItems.Add(reader["Address"].ToString());

                li.SubItems.Add(reader["Email"].ToString());

                listView1.Items.Add(li);
            }
            */

            reader.Close();	//關閉數據集

            connection.Close();	//關閉數據連接

            /*          
          如果訪問的數據庫是SQL Server 7.0，只需要把上面源代碼中的一條語句：
          private static string strConnect = "Provider = Microsoft.Jet.OLEDB.4.0 ; Data Source = " + Application.StartupPath + "\\MY.MDB" ;
          改變成：
          private static string strConnect = "Provider=SQLOLEDB.1 ; Persist Security Info=False ; User ID = sa ; Initial Catalog=數據庫名稱; Data Source = 服務器名稱 " ;
          即可。
          */
        }

        //6060

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


/*
//也可改成用 DataTable
DataTable dt = new DataTable();//创建数据表
da.Fill(dt);//填充数据表
dgv.DataSource = dt;
*/
