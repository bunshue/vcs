using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Data.OleDb;    //讀取Access需使用OLEDB

//"Provider=Microsoft.Jet.OleDb.4.0;"是指數據提供者,這裡使用的是Microsoft Jet引擎,也就是Access中的數據引擎,asp.net就是靠這個和Access的數據庫連接的.
//"Data Source=C:BegASPNETNorthwind.mdb"是指明數據源的位置,他的標准形式是"Data Source=MyDrive:MyPathMyFile.MDB".

/*
以将其分为两类，即：关系型数据库（SQL）和非关系型数据库（NoSQL，Not Only SQL）。
关系型数据库：
    大型：Oracle、DB2 等
    中型：SQL Server、MySQL 等
    小型：Access 等

非关系型数据库：
    Memcached、MongoDB 和 Redis 等
*/

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

            string pic_filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(pic_filename);
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

            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Size = new Size(250, 250);
            pictureBox1.Location = new Point(x_st + dx * 7 + 110 + 10, y_st + dy * 8);
            pictureBox1.Visible = false;

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

        OleDbConnectionStringBuilder get_builder(string db_filename)
        {
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";
            return builder;
        }

        //讀取資料庫至DGV
        void oledb_read_database(string db_filename, string sqlstr, DataGridView dgv)
        {
            OleDbConnectionStringBuilder builder = get_builder(db_filename);
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

        void oledb_read_database_dr(string db_filename, string sqlstr)
        {
            OleDbConnectionStringBuilder builder = get_builder(db_filename);

            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
                cmd.CommandTimeout = 20;

                cn.Open();
                OleDbDataReader dr = cmd.ExecuteReader();

                richTextBox1.Text += "欄數 dr.FieldCount = " + dr.FieldCount.ToString() + "\t欄位名稱 :\n";
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    DataColumn aColumn = new DataColumn(dr.GetName(i), dr.GetFieldType(i));
                    richTextBox1.Text += aColumn + "\t";
                }
                richTextBox1.Text += "\n";

                //印出全部資料
                //richTextBox1.Text += "內容\n";
                while (dr.Read())  // 讀取一筆資料到dr
                {
                    //richTextBox1.Text += "編號 : " + dr[0].ToString() + "\t姓名 : " + dr[1].ToString() + "\n";

                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        richTextBox1.Text += dr[i].ToString();
                        //richTextBox1.Text += dr.GetValue(i).ToString();  // same
                        if (i == (dr.FieldCount - 1))
                        {
                            richTextBox1.Text += "\n";
                        }
                        else
                        {
                            richTextBox1.Text += "\t";
                        }
                    }
                    //直接印出 richTextBox1.Text += dr[0].ToString() + "\t" + dr[1].ToString() + "\t" + dr[2].ToString() + "\n";

                }
                dr.Close();
            }
        }

        // 執行SQL命令
        void oledb_write_database(string db_filename, string sqlstr)
        {
            //依傳入的SQL陳述式對指定的資料表進行新增、修改、刪除 應該都只是操作 並不能取出資料

            //對資料庫操作 增茶改山
            try
            {
                OleDbConnectionStringBuilder builder = get_builder(db_filename);
                using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
                {
                    cn.Open();  // 打開資料庫連線
                    OleDbCommand cmd = new OleDbCommand();
                    cmd.CommandText = sqlstr;
                    cmd.Connection = cn;
                    int rowsAffected = cmd.ExecuteNonQuery();  // 執行SQL命令
                    richTextBox1.Text += "已執行 : " + rowsAffected + " 項資料\n";
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        //讀取excel資料庫至DGV
        void oledb_read_excel_database(string excel_filename, string sqlstr, DataGridView dgv)
        {
            // 連接字串
            string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + excel_filename;

            using (OleDbConnection cn = new OleDbConnection(cnstr))  // 建立資料庫連接對象cn
            {
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

        object oledb_get_database_data(string db_filename, string sqlstr)
        {
            OleDbConnectionStringBuilder builder = get_builder(db_filename);

            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                cn.Open();  // 打開資料庫連線
                OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
                object obj = cmd.ExecuteScalar();
                return obj;
            }
        }

        //6060

        private void button0_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "Northwind.mdb";
            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                try
                {
                    cn.Open();

                    richTextBox1.Text += "連接字串 : " + cn.ConnectionString + "\n";
                    richTextBox1.Text += string.Format("資料庫 : {0} 伺服器名稱或檔案名稱： {1}", cn.Database, cn.DataSource) + "\n";
                    richTextBox1.Text += string.Format("伺服器版本 : {0} 提供者名稱：{1}", cn.ServerVersion, cn.Provider) + "\n";
                    richTextBox1.Text += "目前的連線狀態 : " + cn.State + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //OleDb
            //第一種方式

            // 資料庫檔案
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
            // 資料庫檔案
            db_filename = "Northwind.mdb";
            builder = get_builder(db_filename);
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

            // 資料庫檔案
            db_filename = "Northwind.mdb";
            builder = new OleDbConnectionStringBuilder();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "Northwind.mdb";

            // 查詢字串
            string sqlstr = "SELECT * FROM 員工";
            oledb_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 員工";

            oledb_read_database_dr(db_filename, sqlstr);
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "Northwind.mdb";
            // 查詢字串
            string sqlstr = "SELECT * FROM 客戶";
            oledb_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 客戶";

            // 查詢字串
            sqlstr = "SELECT * FROM 客戶 WHERE 城市='新竹市'";
            sqlstr = "SELECT * FROM 客戶 WHERE 城市 in('新竹市', '花蓮市')";
            // 取得資料, 城市:
            // "宜蘭市","台北市","台北縣","桃園縣","新竹市","苗栗縣","台中市",
            // "南投縣市","高雄市","屏東縣","屏東市","花蓮市"

            oledb_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "客戶資料 新竹市+花蓮市";

            //3030

            //取得供應商資料
            /*
            "宜蘭","台北","桃園","新竹","苗栗",
            "台中","南投","高雄","屏東","花蓮"
            */

            // 資料庫檔案
            db_filename = "Northwind.mdb";

            // 查詢字串
            sqlstr = "SELECT * FROM 供應商";
            oledb_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "全部資料 供應商";


            // 查詢字串
            sqlstr = "SELECT * FROM 供應商 WHERE 供應商='一心' OR 行政區='新竹'";
            oledb_read_database(db_filename, sqlstr, dataGridView4);
            lb_dgv4.Text = "供應商資料 一心 或 新竹";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "Northwind2.mdb";

            // 查詢字串, 取出員工資料表中所有欄位的內容
            string sqlstr = "SELECT * FROM 員工";

            oledb_read_database(db_filename, sqlstr, dataGridView1);

            // 查詢字串 資料筆數 COUNT
            sqlstr = "SELECT COUNT(*) FROM 員工";
            object obj = oledb_get_database_data(db_filename, sqlstr);
            richTextBox1.Text += "共 " + obj.ToString() + " 筆記錄\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //取得部分資料

            // 資料庫檔案
            string db_filename = "Northwind2.mdb";  // 或者 Northwind.mdb ??

            // 查詢字串, 取出員工資料表中所有欄位的內容
            string sqlstr = "SELECT * FROM 員工";

            oledb_read_database(db_filename, sqlstr, dataGridView1);

            OleDbConnectionStringBuilder builder = get_builder(db_filename);

            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                cn.Open();

                // 查詢字串, 取出員工資料表中所有欄位的內容
                sqlstr = "SELECT * FROM 員工";

                OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
                cmd.CommandTimeout = 20;

                OleDbDataReader dr = cmd.ExecuteReader();

                int idx1 = dr.GetOrdinal("姓名");
                richTextBox1.Text += "序號 : " + idx1.ToString() + "\n";
                richTextBox1.Text += "名稱 : " + dr.GetName(idx1) + "\n";
                richTextBox1.Text += "型態 : " + dr.GetFieldType(idx1) + "\n";
                int idx2 = dr.GetOrdinal("職稱");
                richTextBox1.Text += "序號 : " + idx2.ToString() + "\n";
                richTextBox1.Text += "名稱 : " + dr.GetName(idx2) + "\n";
                richTextBox1.Text += "型態 : " + dr.GetFieldType(idx2) + "\n";
                int idx3 = dr.GetOrdinal("電話號碼");
                richTextBox1.Text += "序號 : " + idx3.ToString() + "\n";
                richTextBox1.Text += "名稱 : " + dr.GetName(idx3) + "\n";
                richTextBox1.Text += "型態 : " + dr.GetFieldType(idx3) + "\n";

                while (dr.Read())
                {
                    string str1 = dr.GetValue(idx1).ToString();
                    string str2 = dr.GetString(idx2).ToString();
                    string str3 = dr.GetValue(idx3).ToString();

                    richTextBox1.Text += str1 + "\t" + str2 + "\t" + str3 + "\n";
                }
                dr.Close();
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {
            //(1/4)讀取

            // 資料庫檔案
            string db_filename = "Northwind.mdb";
            // 查詢字串
            string sqlstr = "SELECT * FROM 客戶";
            oledb_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "原本資料";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //(2/4)新增

            string customer_id = "113";  // 最多5拜
            string company_name = "lion-mouse";  // 最多40拜
            string insert_cnstr = "INSERT INTO 客戶 (客戶編號, 公司名稱) VALUES ('{0}', '{1}')";
            // 查詢字串
            sqlstr = string.Format(insert_cnstr, customer_id, company_name);

            oledb_write_database(db_filename, sqlstr);  // 執行SQL命令

            // 資料庫檔案
            db_filename = "Northwind.mdb";
            // 查詢字串
            sqlstr = "SELECT * FROM 客戶";
            oledb_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "新增資料後";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //(3/4)修改

            // 資料庫檔案
            db_filename = "Northwind.mdb";

            customer_id = "XYZ";  // 最多5拜
            company_name = "KKKKK again ddddd";  // 最多40拜
            string contact_name = "david";
            string update_cnstr = "UPDATE 客戶 SET 公司名稱='{0}', 連絡人='{1}' WHERE 客戶編號='{2}'";
            // 查詢字串
            sqlstr = string.Format(update_cnstr, company_name, contact_name, customer_id);

            oledb_write_database(db_filename, sqlstr);  // 執行SQL命令

            // 資料庫檔案
            db_filename = "Northwind.mdb";
            // 查詢字串
            sqlstr = "SELECT * FROM 客戶";
            oledb_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "修改資料後";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //(4/4)刪除

            // 資料庫檔案
            db_filename = "Northwind.mdb";
            customer_id = "XYZ";
            sqlstr = "DELETE * FROM 客戶 " + "WHERE 客戶編號='" + customer_id + "'";

            oledb_write_database(db_filename, sqlstr);  // 執行SQL命令

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 資料庫檔案
            db_filename = "Northwind.mdb";
            // 查詢字串
            sqlstr = "SELECT * FROM 客戶";
            oledb_read_database(db_filename, sqlstr, dataGridView4);
            lb_dgv4.Text = "刪除資料後";
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得一個資料庫的所有Table名稱\n";

            // 資料庫檔案
            string db_filename = "DBMS1.mdb";
            // 連接字串
            //string cnstr = string.Format(db_cnstr, db_filename);

            //這樣會列出所有 實際的資料表（不包含檢視表）

            OleDbConnectionStringBuilder builder = get_builder(db_filename);

            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                cn.Open();
                var schema = cn.GetSchema("TABLES");
                foreach (System.Data.DataRow row in schema.Rows)
                {
                    richTextBox1.Text += row["TABLE_NAME"] + "\n";
                }
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "OleDb 15\n";

            // 資料庫檔案
            string db_filename = "book.TrasformAnalyse.mdb";
            // 查詢字串
            string sqlstr = "SELECT * FROM 圖書排行";
            oledb_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 圖書排行";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用Trasform分析數據
            // 查詢字串
            sqlstr = "transform  sum(數量) as 庫存數量 select 語言類別 from 圖書排行 where 語言類別 in( 'c','VB','java') group by (語言類別) pivot 分析時間";
            oledb_read_database(db_filename, sqlstr, dataGridView2);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "OleDb 16\n";

            // 資料庫檔案
            string db_filename = "dt.trasformDynamic.mdb";
            // 查詢字串
            string sqlstr = "SELECT * FROM 部門銷售額表";
            oledb_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 部門銷售額表";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用trasform動態分析數據

            //區間範圍 軟件部 硬件部 網絡部
            string search_dept = "軟件部','硬件部','網絡部";
            string column1 = "銷售金額";
            string column2 = "季度";
            string column3 = "部門名稱";

            // 查詢字串
            sqlstr = "transform  sum(" + column1 + ") as 數據 select " + column3 + " from 部門銷售額表 where " + column3 + "  in('" + search_dept + "')  group by (" + column3 + ")  pivot " + column2 + "";
            oledb_read_database(db_filename, sqlstr, dataGridView2);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "OleDb 17\n";

            // 資料庫檔案
            string db_filename = "db_Test.mdb";
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工生日表";
            oledb_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 員工生日表";

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 在查詢中使用日期函數
            // 使用日期函數DateDiff計算年齡
            // 自動計算年齡

            // 查詢字串
            sqlstr = "SELECT [員工生日表].[員工姓名], [員工生日表].[出生日期], DateDiff('yyyy',[員工生日表].[出生日期],DATE()) AS 年齡 FROM 員工生日表";
            oledb_read_database(db_filename, sqlstr, dataGridView2);

            //6060

            //db_Test.StringFunctionFind.mdb

            //"SELECT * FROM 員工生日表"
            //在查詢語句中使用字串函數
            //顯示出生年月

            //"SELECT [員工生日表].[員工姓名], format([員工生日表].[出生日期],'yyyy年mm月dd日') AS 出生日期, mid([員工生日表].[出生日期],1,7) AS 出生年月 FROM 員工生日表;", con);
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
            pictureBox1.Visible = true;

            //讀取圖片資料庫中的圖片

            // 資料庫檔案
            string db_filename = "books_with_images.mdb";
            // 查詢字串, 顯示 科系代碼表, 由系碼排序
            string sqlstr = "SELECT * FROM Books";
            oledb_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "科系代碼資料表, 由系碼排序";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                cn.Open();
                OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
                using (OleDbDataReader dr = cmd.ExecuteReader())
                {
                    while (dr.Read())
                    {
                        if (!dr.IsDBNull(6))
                        {
                            Bitmap bm = BytesToImage((byte[])dr.GetValue(6));
                            pictureBox1.Image = bm;
                            /* 其他資料
                            // Add the data row.
                            listView1.AddRow(
                                dr[0].ToString(),   // Image key
                                dr[0].ToString(),   // Title
                                dr[1].ToString(),   // URL
                                dr[2].ToString(),   // ISBN
                                dr[3].ToString(),   // CoverUrl
                                dr[4].ToString(),   // Pages
                                dr[5].ToString());  // Year
                            */
                        }
                    }
                }
            }
        }

        // Convert a byte array into an image.
        private Bitmap BytesToImage(byte[] bytes)
        {
            using (MemoryStream image_stream = new MemoryStream(bytes))
            {
                Bitmap bm = new Bitmap(image_stream);
                return bm;
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            // EXCEL資料庫檔案
            //string excel_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\excel_20210602_131921.xls";
            string excel_filename = @"D:\\_git\\vcs\\_1.data\\______test_files1\\__RW\\_excel\\vcs_test_excel.xls";

            // 工作表名稱
            //string sheetName = "Sheet1";

            /*步驟1：設定Excel的屬性、路徑*/
            //設定讀取的Excel屬性

            // 連接字串
            string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;" +
                //路徑(檔案讀取路徑)
            "Data Source=" + excel_filename + ";" +
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
            OleDbConnection cn = new OleDbConnection(cnstr);  // 建立資料庫連接對象cn
            //打開檔案
            cn.Open();
            /*步驟3：搜尋此Excel的所有工作表，找到特定工作表進行讀檔，並將其資料存入List*/
            //搜尋xls的工作表(工作表名稱需要加$字串)
            DataTable Table = cn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null);
            //查詢此Excel所有的工作表名稱
            foreach (DataRow row in Table.Rows)
            {
                //抓取Xls各個Sheet的名稱(+'$')-有的名稱需要加名稱''，有的不用
                string sheetName0 = (string)row["TABLE_NAME"];
                richTextBox1.Text += "取得工作表 : " + sheetName0 + "\n";
                //工作表名稱有特殊字元、空格，需加'工作表名稱$'，ex：'Sheet_A$'
                //工作表名稱沒有特殊字元、空格，需加工作表名稱$，ex：SheetA$
                //所有工作表名稱為Sheet1，讀取此工作表的內容
                //if (sheetName0 == "SheetA$")
                if (sheetName0 == "Sheet1$")   //第一頁
                {
                    // 工作表名稱
                    string sheetName = "Sheet1";
                    // 查詢字串, 選取工作表名稱
                    string sqlstr = "SELECT * FROM [" + sheetName + "$]";

                    OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
                    OleDbDataReader dr = cmd.ExecuteReader();

                    //讀取工作表SheetA資料
                    //List<string> ListSheetA = new List<string>();
                    int cnt = 0;
                    while (dr.Read())
                    {
                        //工作表SheetA的資料存入List
                        //ListSheetA.Add(dr[cnt].ToString());
                        richTextBox1.Text += "列" + cnt.ToString() + "\t" + dr[0].ToString() + "\t" + dr[1].ToString() + "\t" + dr[2].ToString() + "\n";
                        cnt++;
                    }
                    /*步驟4：關閉檔案*/
                    //結束關閉讀檔(必要，不關會有error)
                    dr.Close();
                    cn.Close();
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void button21_Click(object sender, EventArgs e)
        {
            //讀取EXCEL檔案到dataGridView

            // EXCEL資料庫檔案
            string excel_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\vcs_OleDb\vcs_OleDb\vcs_ReadWrite_EXCEL2.xls";

            // 工作表名稱
            string sheetName = "Sheet1";
            // 查詢字串, 選取工作表名稱
            string sqlstr = "SELECT * FROM [" + sheetName + "$]";

            oledb_read_excel_database(excel_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // EXCEL資料庫檔案
            excel_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\vcs_OleDb\vcs_OleDb\excel_test_data.xls";
            // 工作表名稱
            sheetName = "Sheet1";
            // 查詢字串, 選取工作表名稱
            sqlstr = "SELECT * FROM [" + sheetName + "$]";

            oledb_read_excel_database(excel_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // EXCEL資料庫檔案
            excel_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_excel\2006年圖書銷售情況.xls";
            // 工作表名稱
            sheetName = "BookSell";
            // 查詢字串, 選取工作表名稱
            sqlstr = "SELECT * FROM [" + sheetName + "$]";

            oledb_read_excel_database(excel_filename, sqlstr, dataGridView3);

        }

        //------------------------------------------------------------  # 60個

        private void button22_Click(object sender, EventArgs e)
        {
            //讀取EXCEL檔案到dataGridView

            // EXCEL資料庫檔案
            //string excel_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\vcs_OleDb\vcs_OleDb\excel_test_data.xls";
            string excel_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_excel\2006年圖書銷售情況.xls";

            // 連接字串
            string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties='Excel 8.0;HDR=Yes;IMEX=1;';Data Source=" + excel_filename;

            OleDbConnection cn = new OleDbConnection(cnstr);  // 建立資料庫連接對象cn
            cn.Open();
            DataTable dt = cn.GetSchema("Tables");
            //判斷excel的sheet頁數量，查詢第1頁
            if (dt.Rows.Count > 0)
            {
                string sqlstr = string.Format("SELECT * FROM [{0}]", dt.Rows[0]["TABLE_NAME"]);
                richTextBox1.Text += sqlstr + "\n";
                OleDbDataAdapter da = new OleDbDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                dataGridView1.DataSource = ds.Tables[0];
            }
            cn.Close();
        }

        //------------------------------------------------------------  # 60個

        private void button23_Click(object sender, EventArgs e)
        {
            //Excel多檔合一檔
            string all_files = "D:\\excel_test_data1.xls,D:\\excel_test_data2.xls,D:\\excel_test_data3.xls,";
            string output_file = "D:\\excel_all.xls";
            richTextBox1.Text += "A ";

            object missing = System.Reflection.Missing.Value;//定义object缺省值
            string[] P_str_Names = all_files.Split(',');//存储所有选择的Excel文件名

            for (int i = 0; i < P_str_Names.Length - 1; i++)//遍历所有选择的Excel文件名
            {
                richTextBox1.Text += P_str_Names[i] + "\n";
            }

            string P_str_Name = "";//存储遍历到的Excel文件名
            List<string> P_list_SheetNames = new List<string>();//实例化泛型集合对象，用来存储工作表名称

            Microsoft.Office.Interop.Excel.Application excel = new Microsoft.Office.Interop.Excel.Application();//实例化Excel对象
            //打开指定的Excel文件
            Microsoft.Office.Interop.Excel.Workbook workbook = excel.Application.Workbooks.Open(output_file, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing);
            Microsoft.Office.Interop.Excel.Worksheet newWorksheet = (Microsoft.Office.Interop.Excel.Worksheet)workbook.Worksheets.Add(missing, missing, missing, missing);//创建新工作表
            //if (DateTime.Now.Hour == nudown_Hour.Value && DateTime.Now.Minute == nudown_Min.Value)
            {
                for (int i = 0; i < P_str_Names.Length - 1; i++)//遍历所有选择的Excel文件名
                {
                    P_str_Name = P_str_Names[i];//记录遍历到的Excel文件名
                    //指定要复制的工作簿
                    Microsoft.Office.Interop.Excel.Workbook Tempworkbook = excel.Application.Workbooks.Open(P_str_Name, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing);
                    P_list_SheetNames = GetSheetName(P_str_Name);//获取Excel文件中的所有工作表名
                    for (int j = 0; j < P_list_SheetNames.Count; j++)//遍历所有工作表
                    {
                        //指定要复制的工作表
                        Microsoft.Office.Interop.Excel.Worksheet TempWorksheet = (Microsoft.Office.Interop.Excel.Worksheet)Tempworkbook.Sheets[P_list_SheetNames[j]];//创建新工作表
                        TempWorksheet.Copy(missing, newWorksheet);//将工作表内容复制到目标工作表中
                    }
                    Tempworkbook.Close(false, missing, missing);//关闭临时工作簿
                }
            }
            workbook.Save();//保存目标工作簿
            workbook.Close(false, missing, missing);//关闭目标工作簿
            MessageBox.Show("程序在" + DateTime.Now.ToShortTimeString() + "分时自动汇总了多个Excel文件！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            CloseProcess("EXCEL");//关闭所有Excel进程
        }


        private List<string> GetSheetName(string P_str_Excel)//获取所有工作表名称
        {
            List<string> P_list_SheetName = new List<string>();//实例化泛型集合对象

            // 連接字串
            //string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + P_str_Excel;

            //连接Excel数据库
            //string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + P_str_Excel;
            OleDbConnection olecon = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + P_str_Excel);
            olecon.Open();//打开数据库连接
            System.Data.DataTable DTable = olecon.GetSchema("Tables");//实例化表对象
            DataTableReader DTReader = new DataTableReader(DTable);//实例化表读取对象
            while (DTReader.Read())//循环读取
            {
                string P_str_Name = DTReader["Table_Name"].ToString().Replace('$', ' ').Trim();//记录工作表名称
                if (!P_list_SheetName.Contains(P_str_Name))//判断泛型集合中是否已经存在该工作表名称
                {
                    P_list_SheetName.Add(P_str_Name);//将工作表名添加到泛型集合中
                }
            }
            DTable = null;//清空表对象
            DTReader = null;//清空表读取对象
            olecon.Close();//关闭数据库连接
            return P_list_SheetName;//返回得到的泛型集合
        }

        private void CloseProcess(string P_str_Process)//关闭进程
        {
            System.Diagnostics.Process[] excelProcess = System.Diagnostics.Process.GetProcessesByName(P_str_Process);//实例化进程对象
            foreach (System.Diagnostics.Process p in excelProcess)
            {
                p.Kill();//关闭进程
            }
            System.Threading.Thread.Sleep(10);//使线程休眠10毫秒
        }

        //------------------------------------------------------------  # 60個

        private void button24_Click(object sender, EventArgs e)
        {
            // EXCEL資料庫檔案
            string excel_filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_excel\vcs_ReadWrite_EXCEL2.xls";

            //2.提供者名稱  Microsoft.Jet.OLEDB.4.0適用於2003以前版本，Microsoft.ACE.OLEDB.12.0 適用於2007以後的版本處理 xlsx 檔案
            //string ProviderName = "Microsoft.ACE.OLEDB.12.0;";
            string ProviderName = "Microsoft.Jet.OLEDB.4.0";

            //3.Excel版本，Excel 8.0 針對Excel2000及以上版本，Excel5.0 針對Excel97。
            string ExtendedString = "'Excel 8.0;";

            //4.第一行是否為標題(;結尾區隔)
            string HDR = "No;";

            //5.IMEX=1 通知驅動程序始終將「互混」數據列作為文本讀取(;結尾區隔,'文字結尾)
            string IMEX = "0';";

            //連線字串
            string cnstr =
                    "Data Source=" + excel_filename + ";" +
                    "Provider=" + ProviderName + ";" +
                    "Extended Properties=" + ExtendedString +
                    "HDR=" + HDR +
                    "IMEX=" + IMEX;

            richTextBox1.Text += cnstr + "\n";

            cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + excel_filename;

            richTextBox1.Text += cnstr + "\n";

            using (OleDbConnection cn = new OleDbConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();

                // 工作表名稱
                string sheetName = "Sheet1";
                // 查詢字串, 選取工作表名稱
                string sqlstr = "SELECT * FROM [" + sheetName + "$]";
                using (OleDbDataAdapter da = new OleDbDataAdapter(sqlstr, cn))
                {
                    DataTable dt = new DataTable();
                    da.Fill(dt);
                    dataGridView1.DataSource = dt;
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void button25_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "OleDb 25\n";

            //excel

            // EXCEL資料庫檔案
            //string excel_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\excel_20210602_131921.xls";
            //string excel_filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_excel\excel_20210602_131921.xls";
            //string excel_filename = "C:\\Users\\user\\documents\\visual studio 2010\\Projects\\WindowsFormsApplication1\\WindowsFormsApplication1\\Data\\Book1.xlsx";

            // EXCEL資料庫檔案
            string excel_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_excel\2006年圖書銷售情況.xls";
            // 工作表名稱
            string sheetName = "BookSell";


            /*
            //連線字串
       //2.提供者名稱  Microsoft.Jet.OLEDB.4.0適用於2003以前版本，Microsoft.ACE.OLEDB.12.0 適用於2007以後的版本處理 xlsx 檔案
        //private const string ProviderName = "Microsoft.ACE.OLEDB.12.0;";
        private const string ProviderName = "Microsoft.Jet.OLEDB.4.0;";
        //3.Excel版本，Excel 8.0 針對Excel2000及以上版本，Excel5.0 針對Excel97。
        private const string ExtendedString = "'Excel 8.0;";
        //4.第一行是否為標題
        private const string Hdr = "Yes;";
        //5.IMEX=1 通知驅動程序始終將「互混」數據列作為文本讀取
        private const string IMEX = "0';";
            string cnstr =
                    "Data Source=" + excel_filename + ";" +
                    "Provider=" + ProviderName + ";" +
                    "Extended Properties=" + ExtendedString + ";" +
                    "HDR=" + Hdr +
                    "IMEX=" + IMEX;
            */
            //string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties='Excel 8.0;HDR=Yes;IMEX=1;';Data Source=" + excel_filename;
            string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + excel_filename;

            // 工作表名稱
            //string sheetName = "Sheet1";

            using (OleDbConnection cn = new OleDbConnection(cnstr))
            {
                cn.Open();
                string sqlstr = "select * from [" + sheetName + "$]";
                using (OleDbDataAdapter dr = new OleDbDataAdapter(sqlstr, cn))
                {
                    DataTable dt = new DataTable();
                    dr.Fill(dt);
                    this.dataGridView1.DataSource = dt;
                }
            }
        }

        private void button26_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "OleDb 26\n";

            // 連接字串
            string cnstr = string.Empty;

            // 資料庫檔案
            string db_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db_09.mdb";

            FileInfo FInfo = new FileInfo(db_filename);
            string strExtention = FInfo.Extension;
            if (strExtention.ToLower() == ".mdb")
            {
                //MDB
                string db_path = "aaaaaaaa";  // 數據庫路徑
                string user_name = "david";  // 用戶名
                string password = "12345";  // 密碼

                //使用帳號密碼
                // 連接字串
                cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + db_path + ";UID=" + user_name + ";PWD=" + password + ";";

                //不使用帳號密碼
                // 連接字串
                cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + db_path + ";";
            }
            else if (strExtention.ToLower() == ".xls")
            {
                //EXCEL
                string excel_filename = "bbbbb";  // 數據庫路徑
                // 連接字串
                cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + excel_filename;
            }

            OleDbConnection cn = new OleDbConnection(cnstr);  // 建立資料庫連接對象cn

            try
            {
                cn.Open();
                richTextBox1.Clear();
                richTextBox1.Text = cnstr + "\n连接成功……";
            }
            catch
            {
                richTextBox1.Text = "连接失败";
            }
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //OleDb 27

            // 資料庫檔案
            string db_filename = "DBMS.mdb";
            // 查詢字串
            string sqlstr = "SELECT * FROM 學生資料表";

            oledb_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //string dbpath = "C:\\Inetpub\\wwwroot\\CS\\ch08\\App_Data\\DBMS.mdb";

            // 資料庫檔案
            db_filename = "DBMS.mdb";
            // 查詢字串
            sqlstr = "SELECT * FROM 學生資料表";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);

            OleDbConnection cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn

            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            OleDbDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器

            //顯示資料表欄位名稱
            for (int i = 0; i <= dr.FieldCount - 1; i++)
            {
                richTextBox1.Text += dr.GetName(i) + "\n";
            }

            //顯示資料表欄位的所有資料
            while (dr.Read())
            {
                for (int i = 0; i <= dr.FieldCount - 1; i++)
                {
                    richTextBox1.Text += dr.GetValue(i) + "\n";
                }
            }
            cn.Close();

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 資料庫檔案
            db_filename = "DBMS.mdb";
            builder = get_builder(db_filename);

            //string dbpath = "C:\\Inetpub\\wwwroot\\ASPNET\\ch14\\App_Data\\DBMS.mdb";

            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn

            cn.Open();  // 打開資料庫連線

            // 查詢字串
            sqlstr = "SELECT * FROM 學生資料表";

            OleDbDataAdapter da = new OleDbDataAdapter(sqlstr, cn);
            DataSet ds = new DataSet();
            //讀取資料表
            da.Fill(ds, "Table");
            dataGridView2.DataSource = ds.Tables["Table"];
            cn.Close();
        }

        private void button28_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "OleDb 28\n";

            // 資料庫檔案
            string db_filename = "db_database.mdb";

            // 查詢字串
            string sqlstr = "SELECT * FROM tab_booksort";
            oledb_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tab_booksort";

            oledb_read_database_dr(db_filename, sqlstr);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //第一名
            sqlstr = "select first(BookNames)as Bookname,first(author)as peo,first(sellsum)as slm from tab_booksort";
            oledb_read_database(db_filename, sqlstr, dataGridView2);

            //最後一名
            sqlstr = "select Last(BookNames) as Bookname,Last(author)as peo,Last(sellsum)as slm from tab_booksort";
            oledb_read_database(db_filename, sqlstr, dataGridView3);
        }

        private void button29_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "OleDb 29\n";

            // 資料庫檔案
            string db_filename = "db_Test.FormatFind.mdb";

            // 查詢字串
            string sqlstr = "SELECT * FROM 員工生日表";
            oledb_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 員工生日表";

            oledb_read_database_dr(db_filename, sqlstr);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //在查詢語句中使用格式化函數
            //將出生日期格式化為「年月日」的格式

            // 查詢字串
            sqlstr = "SELECT [員工生日表].[員工姓名], 出生日期 as 格式化前出生日期,format([員工生日表].[出生日期],'yyyy年mm月dd日') AS 格式化後出生日期 FROM 員工生日表;";
            oledb_read_database(db_filename, sqlstr, dataGridView2);
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



/*
OK 可以讀到資料的
            // 資料庫檔案
            string db_filename = "Northwind.mdb";

            // 查詢字串
            string sqlstr = "SELECT * FROM 供應商";
            oledb_read_database(db_filename, sqlstr, dataGridView1);

            // 查詢字串
            sqlstr = "SELECT * FROM 員工";
            oledb_read_database(db_filename, sqlstr, dataGridView2);
*/


//string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\\Northwind.mdb";
//                Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\Northwind.mdb;User ID=Admin



/*
            // 初始化ListView
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

*/


/*          
如果訪問的數據庫是SQL Server 7.0，只需要把上面源代碼中的一條語句：
private static string strConnect = "Provider = Microsoft.Jet.OLEDB.4.0 ; Data Source = " + Application.StartupPath + "\\MY.MDB" ;
改變成：
private static string strConnect = "Provider=SQLOLEDB.1 ; Persist Security Info=False ; User ID = sa ; Initial Catalog=數據庫名稱; Data Source = 服務器名稱 " ;
即可。
*/





/*
一律把上改下
                //string cnstr = @"Provider=Microsoft.ACE.OLEDB.12.0;Persist Security Info=False;Data Source=./2006年圖書銷售情況.xls;Extended Properties=Excel 8.0";
                //string cnstr = @"Provider=Microsoft.ACE.OLEDB.12.0;Persist Security Info=False;Data Source=D:\\_git\\vcs\\_2.vcs\\my_vcs_lesson_6\\_DB\\__db\\_excel\\2006年圖書銷售情況.xls;Extended Properties=Excel 8.0";
                //string cnstr = @"Provider=Microsoft.ACE.OLEDB.12.0;Persist Security Info=False;Data Source=" + excel_filename + ";Extended Properties=Excel 8.0";

string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + excel_filename;

*/


/*
            db_filename = "Northwind.mdb";

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";
*/



//                richTextBox1.Text += dr["CustomerID"].ToString().PadRight(10, ' ');
//                richTextBox1.Text += dr["CustomerID"].ToString();





/*
            // 資料庫檔案
            //string db_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\tt04.mdb";
            string db_filename = @"D:\Northwind.mdb";
            string cnstr = string.Empty;

            //Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + System.Windows.Forms.Application.StartupPath + "\\mydb.accdb;"  accdb
            //cnstr = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + db_filename+ ";Uid=Admin;Pwd=jcvadmin;";              //有帳號密碼的
            //cnstr = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + db_filename+ ";Jet OLEDB:Database Password=workbill"  //有帳號密碼的
            cnstr = @"Provider=Microsoft.Jet.OLEDB.4.0;" + "Data Source=" + db_filename;
            OleDbConnection cn = new OleDbConnection(cnstr);  // 建立資料庫連接對象cn

            // 打開數據庫連接
            cn.Open();
            richTextBox1.Text += "打開數據庫連接成功\n";

            cn.Close();  // 關閉數據庫連接
            cn.Dispose();
            richTextBox1.Text += "關閉數據庫連接成功\n";
*/


//string cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + db_filename + ";";


//NG
//string insert_cnstr = "INSERT INTO 客戶 (客戶編號, 公司名稱, 連絡人, 連絡人職稱, 地址, 城市, 行政區, 郵遞區號, 國家地區, 電話, 傳真電話) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}')";
//sqlstr = string.Format(insert_cnstr, customer_id, company_name, "aa", "aa", "aa", "aa", "aa", "aa", "aa", "aa", "aa");

