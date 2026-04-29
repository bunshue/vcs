using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Data.SqlClient;  // for SqlConnection, SqlCommand, SqlDataAdapter
using System.Data.Sql;  // for SqlDataSourceEnumerator

/*
在 sysobjects 中, xtype 表示 資料庫物件的種類，以字母代碼區分。
- U → 使用者表 (User table)
- V → 檢視 (View)
- P → 儲存過程 (Stored procedure)
- TR → 觸發器 (Trigger)
- FN → 標量函數 (Scalar function)
- TF → 表值函數 (Table function)
- PK → 主鍵約束 (Primary Key)
- F → 外鍵約束 (Foreign Key)
- X → 擴展儲存過程 (Extended stored procedure)
用法
sqlstr = "SELECT * FROM sysobjects WHERE xtype='TR'";
sqlstr = "SELECT * FROM sysobjects WHERE xtype='p'"; 
sqlstr = "SELECT * FROM sysobjects WHERE xtype='v'";
 */

namespace vcs_SqlConnection1
{
    public partial class Form1 : Form
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

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
            bt_previous.Visible = false;
            bt_next.Visible = false;
            lb_index.Visible = false;

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
            this.Text = "vcs_SqlConnection1";

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

        void sql_read_database_dr(string db_filename, string sqlstr)
        {
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            //讀取資料庫
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串, 可有可無
                cn.Open();  // 打開資料庫連線

                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
                /*
                //讀出所有欄位資訊
                DataTable schema = dr.GetSchemaTable();  // 建立DT
                foreach (DataRow schema_row in schema.Rows)
                {
                    richTextBox1.Text += "欄位名稱 : " + schema_row.Field<string>("ColumnName") + "\t";
                    richTextBox1.Text += "資料型態 : " + schema_row.Field<Type>("DataType").ToString() + "\n";
                }
                */
                richTextBox1.Text += "欄數 dr.FieldCount = " + dr.FieldCount.ToString() + "\t欄位名稱 :\n";
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    richTextBox1.Text += dr.GetName(i) + "\t";
                }
                richTextBox1.Text += "\n";

                //印出全部資料
                //richTextBox1.Text += "內容\n";
                while (dr.Read())  // 讀取一筆資料到dr
                {
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

        void sql_read_database(string db_filename, string sqlstr, DataGridView dgv)
        {
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            //richTextBox1.Text += cnstr + "\n";

            //讀取資料庫至DGV
            try
            {
                using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
                {
                    SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                    DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                    da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                    //da.Fill(ds, "table");  // da將查詢的結果填充至數據集ds, 指定TableName為"table"
                    dgv.DataSource = ds.Tables[0].DefaultView;  // DGV設置數據源
                    //dgv.DataSource = ds.Tables[0];  // DGV設置數據源, same
                    richTextBox1.Text += "取得資料 : " + ds.Tables[0].Rows.Count.ToString() + " 筆\n";

                    /*
                    //也可改成用 DataTable
                    DataTable dt = new DataTable();//创建数据表
                    da.Fill(dt);//填充数据表
                    dgv.DataSource = dt;
                    */
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
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

        // 執行SQL命令
        void sql_write_database(string db_filename, string sqlstr)
        {
            //依傳入的SQL陳述式對指定的資料表進行新增、修改、刪除 應該都只是操作 並不能取出資料

            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            //對資料庫操作 增茶改山
            try
            {
                using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
                {
                    cn.Open();  // 打開資料庫連線
                    SqlCommand cmd = new SqlCommand();
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

        object sql_get_database_data(string db_filename, string sqlstr)
        {
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();  // 打開資料庫連線
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                object obj = cmd.ExecuteScalar();
                return obj;
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //簡易測試 資料庫檔案+查詢字串+DGV

            // 資料庫檔案
            string db_filename = string.Empty;
            // 查詢字串
            string sqlstr = string.Empty;
            /*
            // 資料庫檔案
            db_filename = "db_09_Data.MDF";
            // 查詢字串
            sqlstr = "SELECT * FROM syscolumns";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "xxxxx";

            // 查詢字串
            sqlstr = "SELECT name 字段名, xusertype 类型编号, length 长度 FROM syscolumns";
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "xxxxx";

            // 查詢字串
            sqlstr = "SELECT name 类型,xusertype 类型编号 FROM systypes";
            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "xxxxx";

            // 查詢字串
            //sqlstr = "SELECT 字段名,类型,长度 FROM hy_Linshibiao t,angel_Linshibiao b WHERE t.类型编号=b.类型编号";

            // 查詢字串
            //sqlstr = "drop table hy_Linshibiao,angel_Linshibiao";

            return;

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            */
            // 分析公司男女比率
            db_filename = "db_13.mdf";
            sqlstr = "SELECT * FROM tb_sex";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            sqlstr = "SELECT sex, COUNT(sex) num FROM tb_sex GROUP BY sex";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();

            using (SqlCommand cmd = new SqlCommand("SELECT sex, COUNT(sex) num FROM tb_employee GROUP BY sex", con))
            {
                SqlDataReader dr = cmd.ExecuteReader();
                string[] str = new string[2];
                int i = 0;
                while (dr.Read())
                {
                    richTextBox1.Text += dr[0].ToString() + "\t" + dr[1].ToString() + "\n";

                    str[i] = dr[0].ToString() + "," + dr[1].ToString();
                    i++;
                }
                richTextBox1.Text += "str[0] = " + str[0] + "\n";
                richTextBox1.Text += "str[1] = " + str[1] + "\n";

                float N = Convert.ToInt16(str[0].Substring(2)) + Convert.ToInt16(str[1].Substring(2));
                richTextBox1.Text += "N = " + N.ToString() + "\n";

                float f = Convert.ToInt16(str[0].Substring(2)) / N;
                richTextBox1.Text += "f = " + f.ToString() + "\n";
            }

            con.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取資料庫 解讀, 要先知道資料庫檔案(.mdf)和表單名稱(tb_Employee)

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Employee";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tb_Employee";


            // 資料庫檔案
            db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM tb_Employee";
            sql_read_database_dr(db_filename, sqlstr);

            return;

            richTextBox1.Text += "------------------------------\n";  // 30個

            /*
            //讀取資料庫資料

            SqlDataAdapter da;//宣告一個數據讀取器
            DataSet ds;//宣告一個數據集
            SqlConnection cn;//宣告一個數據庫連接對像

            //定義一個數據庫連接字符串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            cn = new SqlConnection(cnstr);  // 建立資料庫連接對象cn
            sqlstr = "SELECT 產品名稱,產品說明 FROM tb_WidgetApply";//定義一個數據庫查詢字串
            da = new SqlDataAdapter(sqlstr, cn);//初始化數據讀取器對像
            ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            da.Fill(ds, "WidgetApply");  // da將查詢的結果填充至數據集ds, 指定TableName為"WidgetApply"

            dataGridView1.DataSource = ds.Tables["WidgetApply"];  // DGV設置數據源
            lb_dgv1.Text = "產品名稱,產品說明\n";

            richTextBox1.Text += "取得資料 : " + ds.Tables[0].Rows.Count.ToString() + " 筆\n";

            for (int i = 0; i < ds.Tables["WidgetApply"].Rows.Count; i++)//循環搜尋數據集中的每一行數據
            {
                richTextBox1.Text += ds.Tables["WidgetApply"].Rows[i][0].ToString() + "\t" + ds.Tables["WidgetApply"].Rows[i][1].ToString() + "\n";
            }
            */
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            /*
            cn = new SqlConnection(cnstr);  // 建立資料庫連接對象cn
            cn.Open();//打開數據庫連接
            sqlstr = "SELECT 產品編號,產品名稱 FROM tb_WidgetApply";//定義一個數據庫查詢字符串
            SqlCommand cmd = new SqlCommand(sqlstr, cn);//初始化執行SQL語句對像
            SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器

            while (dr.Read())  // 讀取一筆資料到dr
            {
                richTextBox1.Text += dr[1].ToString() + "\n";
            }
            dr.Close();//關閉數據讀取器
            cn.Close();//關閉數據庫連接
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 讀取資料庫資料到 DataTable
            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                // 查詢字串
                sqlstr = "SELECT * FROM 員工表";
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);

                //產生結果集
                DataTable dt = new DataTable();
                da.Fill(dt);
                richTextBox1.Text += "欄名 :\t";
                for (int i = 0; i < dt.Columns.Count; i++)//列
                {
                    richTextBox1.Text += dt.Columns[i].ColumnName.ToString() + "\t";
                }
                richTextBox1.Text += "\n";

                int R = dt.Rows.Count;
                richTextBox1.Text += "R = " + R.ToString() + "\n";

                for (int j = 0; j < R; j++)
                {
                    richTextBox1.Text += "第 " + (j + 1).ToString() + " 筆資料\t";
                    richTextBox1.Text += dt.Rows[j][0].ToString() + "\t";
                    for (int k = 1; k < dt.Columns.Count; k++)
                    {
                        richTextBox1.Text += dt.Rows[j][k].ToString() + "\t";
                    }
                    richTextBox1.Text += "\n";
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "Northwind.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串, 可有可無

                richTextBox1.Text += "連接資料庫前\t資料庫連接狀態 : " + cn.State + "\n";  // ConnectionState.Closed
                cn.Open();  // 打開資料庫連線
                if (cn.State == ConnectionState.Open)
                {
                    richTextBox1.Text += "資料庫已連接\n";
                }
                else
                {
                    richTextBox1.Text += "資料庫未連接\n";
                }

                richTextBox1.Text += "連接資料庫後\t資料庫連接狀態 : " + cn.State + "\n";  // ConnectionState.Open

                // 顯示資料來源的相關資訊
                richTextBox1.Text += "資料庫連接設定 :\n";
                richTextBox1.Text += "連接字串：" + cn.ConnectionString + "\n";
                richTextBox1.Text += "逾時秒數：" + cn.ConnectionTimeout + "\n";
                richTextBox1.Text += "　資料庫：" + cn.Database + "\n";
                richTextBox1.Text += "資料來源：" + cn.DataSource + "\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //讀取資料庫2

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //多次查詢 分別放置一個DS的多個Table中
                //不同DGV顯示不同Table的資料

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)

                //cn.ConnectionString = cnstr;  // 連接字串, 可有可無

                // 建立三個DataAdapter物件，用來取得員工, 客戶, 產品類別資料表
                // 再將三個資料表放入ds(DataSet)物件中
                // 查詢字串
                string sqlstr1 = "SELECT * FROM 員工";
                SqlDataAdapter da1 = new SqlDataAdapter(sqlstr1, cn);  // 建立資料庫適配器對象da1
                da1.Fill(ds, "員工");  // da將查詢的結果填充至數據集ds, 指定TableName為"員工"

                // 查詢字串
                string sqlstr2 = "SELECT * FROM 客戶";
                SqlDataAdapter da2 = new SqlDataAdapter(sqlstr2, cn);  // 建立資料庫適配器對象da2
                da2.Fill(ds, "客戶");  // da將查詢的結果填充至數據集ds, 指定TableName為"客戶"

                // 查詢字串
                string sqlstr3 = "SELECT * FROM 產品類別";
                SqlDataAdapter da3 = new SqlDataAdapter(sqlstr3, cn);  // 建立資料庫適配器對象da3
                da3.Fill(ds, "產品類別");  // da將查詢的結果填充至數據集ds, 指定TableName為"產品類別"

                // 將ds物件內三個DataTable
                for (int i = 0; i < ds.Tables.Count; i++)
                {
                    richTextBox1.Text += "取得 資料表 : " + ds.Tables[i].TableName + "\n";
                }

                richTextBox1.Text += "TableName1 : " + ds.Tables["員工"].TableName + "\n";
                richTextBox1.Text += "TableName2 : " + ds.Tables["客戶"].TableName + "\n";
                richTextBox1.Text += "TableName3 : " + ds.Tables["產品類別"].TableName + "\n";

                dataGridView1.DataSource = ds.Tables["員工"];  // DGV設置數據源
                lb_dgv1.Text = "員工";

                dataGridView2.DataSource = ds.Tables["客戶"];  // DGV設置數據源
                lb_dgv2.Text = "客戶";

                dataGridView3.DataSource = ds.Tables["產品類別"];  // DGV設置數據源
                lb_dgv3.Text = "產品類別";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //BETWEEN

            //查詢指定日期的數據

            //全部資料
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT 書號,書名,作者,單價,銷售數量,金額,日期 FROM tb_xsb";
            sql_read_database(db_filename, sqlstr, dataGridView1);


            //查詢指定日期的數據

            string datetime = "2005/7/22";
            // 資料庫檔案
            db_filename = "db_10_Data.MDF";

            // 查詢字串
            sqlstr = "SELECT 書號,書名,作者,單價,銷售數量,金額,日期 FROM tb_xsb WHERE 日期='" + datetime + "'";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            //查詢指定時間段的數據

            string datetime_st = "2005/5/1";
            string datetime_sp = "2005/9/30";

            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT 書號,書名,作者,單價,銷售數量,金額,日期 FROM tb_xsb WHERE 日期 BETWEEN'" + datetime_st + "'AND '" + datetime_sp + "' ORDER BY 日期";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //利用圖表分析彩票中獎情況

            //t_year 在 2005/4/1 ~ 2006/10/1 有資料
            string time_st = "2005/8/15";
            string time_sp = "2006/4/15";

            sqlstr = "SELECT * FROM tb_lottery WHERE t_year BETWEEN '" + time_st + "' AND '" + time_sp + "' ORDER BY t_year";

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            SqlCommand cmd = new SqlCommand(sqlstr, con);
            SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
            while (dr.Read())
            {
                richTextBox1.Text += dr[0].ToString() + "\t" + Convert.ToDouble(dr[1].ToString()) + "\n";
            }
            dr.Close();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 資料庫檔案
            db_filename = "db_TomeOne.mdf";
            //string time_st = "2005/8/15";
            //string time_sp = "2006/4/15";
            //sqlstr = "SELECT * FROM tb_lottery WHERE t_year BETWEEN '" + time_st + "' AND '" + time_sp + "' ORDER BY t_year";
            sqlstr = "SELECT * FROM tb_lottery WHERE t_year BETWEEN '2005/8/15' AND '2006/4/15' ORDER BY t_year";
            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv1.Text = "查詢使用指定時段 BETWEEN";

            //查询指定时间段的数据

            time_st = "2005/7/1";
            time_sp = "2005/8/31";
            // 查詢字串
            sqlstr = string.Format("SELECT * FROM tb_Book WHERE 日期 BETWEEN '{0}' AND '{1}'", time_st, time_sp);
            // 資料庫檔案
            db_filename = "db_TomeTwo.mdf";
            sql_read_database(db_filename, sqlstr, dataGridView4);
            lb_dgv2.Text = "查詢使用指定時段 BETWEEN";
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "animals1_db.mdf";
            // 查詢字串
            //string sqlstr = "SELECT * FROM animals1_table";

            string sqlstr = "select name 字段名, xusertype 類型編號, length 長度 from syscolumns";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "十二生肖全部資料";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //圖片相關

            // 資料庫檔案
            string db_filename = string.Empty;
            // 查詢字串
            string sqlstr = string.Empty;

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            pictureBox1.Visible = true;

            // 資料庫檔案
            db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM tb_Image";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料, 有圖片, 取出資料庫中的影像, DGV 加上 CellClick";
            dataGridView1.CellClick += new DataGridViewCellEventHandler(dataGridView1_CellClick_pic);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 資料庫檔案
            db_filename = "Northwind.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM 產品類別";

            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "全部資料, 有圖片, 取出資料庫中的影像, DGV 加上 CellClick";
            dataGridView2.CellClick += new DataGridViewCellEventHandler(dataGridView2_CellClick_pic);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            //加入一筆影像資料

            richTextBox1.Text += "添加用戶訊息\n";

            //選擇的頭像名稱
            string pic_filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            string user_name = "david wang aaacccddd";  // 用戶名稱

            //添加用户信息

            richTextBox1.Text += "用戶名稱 : " + user_name + "\n";
            richTextBox1.Text += "影像檔案 : " + pic_filename + "\n";

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection cn = new SqlConnection(cnstr);

            // 查詢字串
            sqlstr = "SELECT * FROM tb_Image WHERE name='" + user_name + "'";
            
            SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
            DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName

            richTextBox1.Text += "取得資料 : " + ds.Tables[0].Rows.Count.ToString() + " 筆\n";

            if (ds.Tables[0].Rows.Count <= 0)
            {
                FileStream FStream = new FileStream(pic_filename, FileMode.Open, FileAccess.Read);
                BinaryReader BReader = new BinaryReader(FStream);
                byte[] byteImage = BReader.ReadBytes((int)FStream.Length);
                SqlCommand cmd = new SqlCommand("insert into tb_Image(name,photo) values(@name,@photo)", cn);
                cmd.Parameters.Add("@name", SqlDbType.VarChar, 50).Value = user_name;
                cmd.Parameters.Add("@photo", SqlDbType.Image).Value = byteImage;
                cn.Open();
                cmd.ExecuteNonQuery();
                cn.Close();
                richTextBox1.Text += "加入用戶信息 OK\n";
            }
            else
            {
                richTextBox1.Text += "加入用戶信息 NG, 已經存在該用戶\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        private void dataGridView1_CellClick_pic(object sender, DataGridViewCellEventArgs e)
        {
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            string user_name = dataGridView1.Rows[e.RowIndex].Cells[1].Value.ToString();
            //richTextBox1.Text += "你點選的用戶名 : " + user_name + "\n";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Image WHERE name='" + user_name + "'";
            //richTextBox1.Text += sqlstr + "\n";

            if (user_name != "")
            {
                SqlConnection cn = new SqlConnection(cnstr);
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName

                // 取出圖片 在第2欄
                byte[] byteImage = (byte[])ds.Tables[0].Rows[0][2];
                //使用数据库中存储的二进制头像实例化内存数据流
                MemoryStream MStream = new MemoryStream(byteImage);
                pictureBox1.Image = Image.FromStream(MStream);
            }
        }

        void dataGridView2_CellClick_pic(object sender, DataGridViewCellEventArgs e)
        {
            // 資料庫檔案
            string db_filename = "Northwind.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            string user_name = dataGridView2.Rows[e.RowIndex].Cells[1].Value.ToString();
            //richTextBox1.Text += "你點選的類別名稱 : " + user_name + "\n";
            // 查詢字串
            string sqlstr = "SELECT * FROM 產品類別 WHERE 類別名稱='" + user_name + "'";
            richTextBox1.Text += sqlstr + "\n";

            if (user_name != "")
            {
                SqlConnection cn = new SqlConnection(cnstr);
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName

                richTextBox1.Text += ds.Tables[0].Rows[0][0] + "\n";
                richTextBox1.Text += ds.Tables[0].Rows[0][1] + "\n";
                richTextBox1.Text += ds.Tables[0].Rows[0][2] + "\n";
                /* NG
                // 取出圖片 在第3欄
                byte[] byteImage = (byte[])ds.Tables[0].Rows[0][3];
                //使用数据库中存储的二进制头像实例化内存数据流
                MemoryStream MStream = new MemoryStream(byteImage);
                pictureBox1.Image = Image.FromStream(MStream);
                */
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取出資料庫中的影像2\n";
            pictureBox1.Visible = true;

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            string str = "003";
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工訊息 WHERE 員工編號='" + str + "'";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();

                using (SqlCommand cmd = new SqlCommand(sqlstr, cn))
                {
                    SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
                    while (dr.Read())  // 讀取一筆資料到dr
                    {
                        richTextBox1.Text += "員工編號 : " + dr[0] + "\n";
                        richTextBox1.Text += "員工姓名 : " + dr[1] + "\n";
                        byte[] pic = (byte[])dr[2];
                        MemoryStream ms = new MemoryStream(pic);			//二進制流
                        this.pictureBox1.Image = Image.FromStream(ms);
                    }
                    dr.Close();
                }
            }
        }

        // CRUD 增查改刪 0 ST

        // 連接字串
        string cnstr23 = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\ch23DB.mdf;Integrated Security=True;Connect Timeout=30";

        private void button10_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "ch23DB.mdf";

            //CRUD 增查改刪 0

            // 查詢字串, 讀取全部資料庫
            string sqlstr = "SELECT * FROM 書籍";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 書籍\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增
            string 書號 = "IMS0311";  // 書號 為 PK, 不可重複
            string 書名 = "膠囊內視鏡";
            int 單價 = 12345;
            int 數量 = 20;

            // 查詢字串
            sqlstr = "INSERT INTO 書籍(書號, 書名, 單價, 數量)" + "VALUES(@BookId, @BookName, @Price, @Qty)";

            using (SqlConnection cn = new SqlConnection(cnstr23))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr23;  // 連接字串
                cn.Open();  // 打開資料庫連線

                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                cmd.Parameters.Add(new SqlParameter("@BookId", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter("@BookName", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter("@Price", SqlDbType.Int));
                cmd.Parameters.Add(new SqlParameter("@Qty", SqlDbType.Int));
                cmd.Parameters["@BookId"].Value = 書號;
                cmd.Parameters["@BookName"].Value = 書名;
                cmd.Parameters["@Price"].Value = 單價;
                cmd.Parameters["@Qty"].Value = 數量;
                cmd.ExecuteNonQuery();  // 執行SQL命令
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 查詢字串, 讀取全部資料庫
            sqlstr = "SELECT * FROM 書籍";

            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "全部資料 書籍\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //更新
            書號 = "IMS0311";//以書號為準
            書名 = "ims EGDaxx";
            單價 = 1231;
            數量 = 181;

            // 查詢字串
            sqlstr = "UPDATE 書籍 SET 書名=@BookName," + "單價=@Price, 數量=@Qty WHERE 書號=@BookId";

            using (SqlConnection cn = new SqlConnection(cnstr23))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr23;  // 連接字串
                cn.Open();  // 打開資料庫連線

                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                cmd.Parameters.Add(new SqlParameter("@BookId", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter("@BookName", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter("@Price", SqlDbType.Int));
                cmd.Parameters.Add(new SqlParameter("@Qty", SqlDbType.Int));
                cmd.Parameters["@BookId"].Value = 書號;
                cmd.Parameters["@BookName"].Value = 書名;
                cmd.Parameters["@Price"].Value = 單價;
                cmd.Parameters["@Qty"].Value = 數量;
                cmd.ExecuteNonQuery();  // 執行SQL命令
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 查詢字串, 讀取全部資料庫
            sqlstr = "SELECT * FROM 書籍";

            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "全部資料 書籍\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //刪除
            書號 = "IMS0311";//以書號為準

            // 查詢字串
            sqlstr = "DELETE FROM 書籍 WHERE 書號 = @BookId";

            using (SqlConnection cn = new SqlConnection(cnstr23))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr23;  // 連接字串
                cn.Open();  // 打開資料庫連線

                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                cmd.Parameters.Add(new SqlParameter("@BookId", SqlDbType.NVarChar));
                cmd.Parameters["@BookId"].Value = 書號;
                cmd.ExecuteNonQuery();  // 執行SQL命令
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 查詢字串, 讀取全部資料庫
            sqlstr = "SELECT * FROM 書籍";

            sql_read_database(db_filename, sqlstr, dataGridView4);
            lb_dgv4.Text = "全部資料 書籍\n";
        }

        // CRUD 增查改刪 0 SP

        private void button11_Click(object sender, EventArgs e)
        {
            //SQL 使用 合集, 新加入

            // 資料庫檔案
            string db_filename = string.Empty;
            // 連接字串
            string cnstr = string.Empty;
            // 查詢字串
            string sqlstr = string.Empty;

            // 資料庫檔案
            db_filename = "db_TomeOne.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM tb_Stat";
            // 查詢字串
            sqlstr = "SELECT * FROM tb_Stat WHERE ShowYear=" + 2006 + "";

            //sql_read_database(db_filename, sqlstr, dataGridView1);
            //lb_dgv1.Text = "全部資料 tb_Stat";

            int query_year = 2006;  // 有資料的年份 2001~2007

            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeOne.mdf;Integrated Security=True;Connect Timeout=30";

            // 查詢字串, 將符合條件的資料取資料總和
            sqlstr = "SELECT SUM(Year_M1+Year_M2+Year_M3+Year_M4+Year_M5+Year_M6+Year_M7+Year_M8+Year_M9+Year_M10+Year_M11+Year_M12) AS number FROM tb_Stat WHERE ShowYear=" + query_year + "";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "11111";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //測試登錄功能

            //先看一下資料庫內容

            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            string sqlstr = "SELECT * FROM tb_Login";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tb_Login";

            sqlstr = "SELECT Name, Pwd FROM tb_Login WHERE Name='mr' AND Pwd='mrsoft'";

            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "全部資料 tb_Login + WHERE 過濾資料";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlDataAdapter da = new SqlDataAdapter("SELECT Name, Pwd FROM tb_Login WHERE Name=@name AND Pwd=@pwd", cn);  // 建立資料庫適配器對象da

                //为SQL语句中的参数赋值
                string id_name = "david";
                string password = "123456";
                id_name = "mr";
                password = "mrsoft";
                da.SelectCommand.Parameters.Add("@name", SqlDbType.NChar, 10).Value = id_name;
                da.SelectCommand.Parameters.Add("@pwd", SqlDbType.NChar, 10).Value = password;

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName

                dataGridView3.DataSource = ds.Tables[0];  // DGV設置數據源

                richTextBox1.Text += "取得資料 : " + ds.Tables[0].Rows.Count.ToString() + " 筆\n";

                // 若能取到資料, 表示 帳號/密碼 有在資料庫內
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            // 用 SqlTransaction 一次執行一些 SQL 命令, 若有失敗者 即全部恢復

            // 資料庫檔案
            string db_filename = "animals1_db.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM animals1_table";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "十二生肖全部資料";

            //1515

            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\animals1_db.mdf;Integrated Security=True;Connect Timeout=30";
            SqlConnection m_Conn = new SqlConnection(cnstr);
            SqlCommand m_Cmd = new SqlCommand();
            m_Conn.Open();

            List<string> sqlstrs = new List<string>();//SQL语句集合
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (90, N'aaa', N'AAA', 20)";
            sqlstrs.Add(sqlstr);
            sqlstrs.Add(sqlstr);
            sqlstrs.Add(sqlstr);
            sqlstrs.Add(sqlstr);
            sqlstrs.Add(sqlstr);

            SqlTransaction sqlTran = m_Conn.BeginTransaction();//实例化事务对象
            try
            {
                m_Cmd.Connection = m_Conn;//指定SqlCommand对象的连接对象
                m_Cmd.Transaction = sqlTran;//指定SqlCommand对象的事务对象
                foreach (string item in sqlstrs)//遍历List泛型集合中的所有SQL命令
                {
                    m_Cmd.CommandType = CommandType.Text;//指定SqlCommand对象的执行命令方式
                    m_Cmd.CommandText = item;//指定SqlCommand对象要执行的SQL命令
                    m_Cmd.ExecuteNonQuery();//执行SQL命令
                }
                sqlTran.Commit();//提交数据库
                richTextBox1.Text += "OK\n";
            }
            catch
            {
                sqlTran.Rollback();//事务回滚
                richTextBox1.Text += "發生錯誤\n";
            }
            finally
            {
                m_Conn.Close();//关闭数据库连接
                sqlstrs.Clear();//清空List泛型集合
                richTextBox1.Text += "dddddddddd\n";
            }

            //1515

            // 資料庫檔案
            db_filename = "animals1_db.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM animals1_table";
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv1.Text = "十二生肖全部資料";
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //sysobjects
            //取得數據庫中全部的預儲程序, 但是取得後, 也不能利用, 因為不知道其內容

            // 資料庫檔案
            string db_filename = string.Empty;
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = string.Empty;

            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 查詢字串, 改顯示欄位名稱AS
            sqlstr = "SELECT * FROM sysobjects";  // 有很多欄位
            //sqlstr = "SELECT name, crdate, refdate FROM sysobjects";  // 只看3個欄位
            //sqlstr = "SELECT name AS 預儲程序名稱, crdate AS 建立時間, refdate AS 最後修改時間 FROM sysobjects";  // 只看3個欄位+改欄名

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //測試 getTable

            //comboBox1.DataSource = getTable(cnstr, "SELECT name FROM sysdatabases", "sysdatabases");

            /*
            //測試 getTable

            string strCon = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.MDF;DataBase=" + comboBox1.Text + ";Integrated Security=True;Connect Timeout=30";

            DataTable dt = null;
            //数据表
            dt = getTable(strCon, "SELECT name FROM sysobjects WHERE type = 'U' and name<>'dtproperties'", "sysobjects");
            //"视图"
            dt = getTable(strCon, "SELECT name FROM sysobjects WHERE xtype='v'", "sysobjects");
            //"存储过程"
            dt = getTable(strCon, "SELECT name FROM sysobjects WHERE xtype='p'", "sysobjects");
            */

        }

        private DataTable getTable(string strCon, string strSql, string strTable)
        {
            richTextBox1.Text += "strCon : " + strCon + "\n";
            richTextBox1.Text += "strSql : " + strSql + "\n";
            richTextBox1.Text += "strTable : " + strTable + "\n";

            try
            {
                SqlConnection sqlcon = new SqlConnection(strCon);
                SqlDataAdapter da = new SqlDataAdapter(strSql, sqlcon);
                DataTable dt = new DataTable(strTable);
                da.Fill(dt);
                richTextBox1.Text += "OK dt\n";

                dataGridView2.DataSource = dt;
                dataGridView2.Columns[0].Width = 350;

                return dt;
            }
            catch
            {
                richTextBox1.Text += "NG dt\n";
                return null;
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "刪除資料 與 清空表單, DELETE 和 DELETE FROM 一樣\n";

            // 資料庫檔案
            string db_filename = "animals1_db.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM animals1_table";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "十二生肖全部資料";

            // 刪除資料
            string id = "12";
            // 資料庫檔案
            db_filename = "animals1_db.mdf";
            // 查詢字串, 刪除符合條件的項目
            sqlstr = "DELETE FROM animals1_table WHERE 編號=N'" + id + "'";

            sql_write_database(db_filename, sqlstr);  // 執行SQL命令

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            // 查詢字串, 有條件刪除資料 體重 > 40 的所有資料
            sqlstr = "DELETE FROM animals1_table WHERE 體重 > 80";  // 刪除所有資料
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令

            richTextBox1.Text += "------------------------------\n";  // 30個
            */

            /*
            richTextBox1.Text += "清空一個資料庫表單 TRUNCATE TABLE\n";
            // 查詢字串, 清空整個表單
            sqlstr = "TRUNCATE TABLE animals1_table";  // 清空整個表單
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            */
        }

        private void button18_Click(object sender, EventArgs e)
        {
            // 十二生肖整理1

            // 資料庫檔案
            string db_filename = "animals1_db.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM animals1_table";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "十二生肖全部資料";

            return;

            /*
            // 查詢字串, 欄名使用AS
            sqlstr = "SELECT 英文名 AS ename, 中文名 AS cname, 體重 AS weight FROM animals1_table";
            
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "十二生肖全部資料 欄名使用AS";

            // 查詢字串, 依體重排序 DESC/降冪, ASC/升冪
            sqlstr = "SELECT * FROM animals1_table ORDER BY 體重 DESC";
            
            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "十二生肖全部資料 依體重降冪排序";

            // 查詢字串, 依體重排序 DESC/降冪, ASC/升冪, 前五名
            sqlstr = "SELECT TOP 5 * FROM animals1_table ORDER BY 體重 DESC";
            
            sql_read_database(db_filename, sqlstr, dataGridView4);
            lb_dgv4.Text = "十二生肖全部資料 依體重降冪排序 前五名";
            */

            //某一欄資料處理 COUNT SUM AVG MAX MIN, 使用 ExecuteScalar()

            // 查詢字串 資料筆數 COUNT
            sqlstr = "SELECT COUNT(*) FROM animals1_table";

            object obj = sql_get_database_data(db_filename, sqlstr);
            richTextBox1.Text += "共 " + obj.ToString() + " 筆記錄\n";

            // 查詢字串 取總和 SUM(), 計算某一欄的和
            sqlstr = "SELECT SUM(體重) FROM animals1_table";

            obj = sql_get_database_data(db_filename, sqlstr);
            richTextBox1.Text += "總和 :\t" + obj.ToString() + "\n";
            int SumNum = Convert.ToInt32(obj);
            richTextBox1.Text += "總和 :\t" + SumNum.ToString() + "\n";

            // 查詢字串 取平均 AVG()
            sqlstr = "SELECT AVG(體重) FROM animals1_table";

            obj = sql_get_database_data(db_filename, sqlstr);
            richTextBox1.Text += "平均 :\t" + obj.ToString() + "\n";

            // 查詢字串 取最大 MAX()
            sqlstr = "SELECT MAX(體重) FROM animals1_table";

            obj = sql_get_database_data(db_filename, sqlstr);
            richTextBox1.Text += "最大 :\t" + obj.ToString() + "\n";

            // 查詢字串 取最小 MIN()
            sqlstr = "SELECT MIN(體重) FROM animals1_table";

            obj = sql_get_database_data(db_filename, sqlstr);
            richTextBox1.Text += "最小 :\t" + obj.ToString() + "\n";

            //AS
            //t_Name
            //sqlstr = "SELECT t_Name, SUM(t_Num) AS Num FROM tb_product GROUP BY t_Name";

            // 更新資料 UPDATE

            // 查詢字串 更新資料
            string new_name = "巧虎";
            sqlstr = "UPDATE animals1_table SET 中文名=N'" + new_name + "' WHERE 編號=3";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令

            // 查詢字串 更新資料 多項
            string id = "11";
            string cname = "丹尼狗";
            string ename = "Danny Dog";
            int weight = 25;
            sqlstr = "UPDATE animals1_table SET 中文名=N'" + cname + "', 英文名=N'" + ename + "', 體重=" + weight + " WHERE 編號=N'" + id + "'";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令

            // 查詢字串
            sqlstr = "SELECT * FROM animals1_table";

            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "十二生肖全部資料 更新資料後";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增資料

            id = "13";
            cname = "大象";
            ename = "elephant";
            weight = 345;

            // 查詢字串
            sqlstr = "INSERT INTO animals1_table(編號, 英文名, 中文名, 體重)VALUES(N'" + id + "',N'" + ename + "',N'" + cname + "'," + weight.ToString() + ")";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令

            // 查詢字串
            sqlstr = "SELECT * FROM animals1_table";

            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "十二生肖全部資料 更新資料後";

            richTextBox1.Text += "------------------------------\n";  // 30個

            /*
            int CategoryId3 = 1;  // 類別編號
            // 查詢字串
            sqlstr = "SELECT 產品編號,品名,單價,說明 FROM 產品資料 WHERE 類別編號=" + CategoryId3;
            */

            /*
            // 查詢字串
            string sqlstr = "xxxxx";
            string new_item = "麥當勞";
            //傳入INSERT陳述式新增產品類別記錄
            sqlstr = "INSERT INTO 產品類別(類別名稱)VALUES(N'" + new_item + "')";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令


            richTextBox1.Text += "修改, 修改 類別編號4 的 產品類別\n";
            int old_id = 4;
            string new_item2 = "肯德雞";
            //傳入UPDATE陳述式修改產品類別記錄
            //取得DataGridView目前選取第一欄的資料，也就是類別編號欄位
            sqlstr = "UPDATE 產品類別 SET 類別名稱=N'" + new_item2 + "' WHERE 類別編號=" + old_id.ToString();
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            */
            /*
            // 資料庫檔案
            string db_filename = "Database1.mdf";

            //新增 修改 刪除
            richTextBox1.Text += "新增\n";
            string new_item = "必勝客";
            int price = 12345;//單價
            string mesg = "電話訂購";//說明

            string sqlstr = "INSERT INTO 產品資料(類別編號,品名,單價,說明)VALUES(1,N'" + new_item + "'," + price.ToString() + ",N'" + mesg + "')";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令

            //產品資料管理, 查詢 類別編號 = 1 的資料
            int CategoryId1 = 1;  // 類別編號
            // 查詢字串, 只看一些欄位, 加上條件
            sqlstr = "SELECT 產品編號,品名,單價,說明 FROM 產品資料 WHERE 類別編號=" + CategoryId1;
            
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "查詢 類別編號 = 1 的資料";

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "修改\n";

            new_item = "達美樂";
            price = 123;//單價
            mesg = "網路訂購";//說明

            sqlstr = "UPDATE 產品資料 SET 品名=N'" + new_item + "', 單價=" + price.ToString() + ", 說明=N'" + mesg + "' WHERE 產品編號=" + dataGridView1.CurrentRow.Cells[0].Value.ToString();
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令

            int CategoryId2 = 1;//類別編號
            richTextBox1.Text += "CategoryId2 = " + CategoryId2.ToString() + "\n";

            // 查詢字串, 只看一些欄位, 加上條件
            sqlstr = "SELECT 產品編號,品名,單價,說明 FROM 產品資料 WHERE 類別編號=" + CategoryId2;
            
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "修改 產品資料";
            */
        }

        private void button19_Click(object sender, EventArgs e)
        {
            // 十二生肖整理2

            // 資料庫檔案
            string db_filename = "animals1_db.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM animals1_table";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "十二生肖全部資料";

            // 測試基礎聚合函式(Aggregate Functions), 最大值MAX、最小值MIN、平均值AVG、總和SUM、數數COUNT
            // 查詢字串
            sqlstr = "SELECT * FROM animals1_table";
            sqlstr = "SELECT COUNT(*) AS order_cnt, SUM(體重) AS gmv, ROUND(AVG(體重), 2) AS avg_order_value, MAX(體重) AS max_order, MIN(體重) AS min_order FROM animals1_table";

            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "十二生肖全部資料";

            return;

            //查詢操作列長度

            // 查詢字串
            sqlstr = "SELECT 編號," + "英文名" + " FROM animals1_table WHERE len(" + "英文名" + ")=5";

            sql_read_database(db_filename, sqlstr, dataGridView2);


            //過濾資料 WHERE + AND + N中文
            sqlstr = "SELECT * FROM animals1_table WHERE 中文名=N'彼得兔' AND 英文名='rabbit'";

            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "WHERE + AND 過濾資料";
        }

        private void button20_Click(object sender, EventArgs e)
        {
            // 建立資料庫檔案
            // 完整測試資料庫
            // 建立資料庫、建立表單、增茶改刪

            richTextBox1.Text += "建立資料庫 (如果不存在)\n";

            // 建立資料庫 的 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();  // 打開資料庫連線
                /*
                //未指名資料庫檔案路徑, 則放在 C:\Users\bunsh\ 之下
                string createDb = @"
                    IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'animals1_db')
                    CREATE DATABASE animals1_db";
                */
                //指名資料庫檔案路徑
                string createDb = @"
                    IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'animals1_db')
                    CREATE DATABASE animals1_db
                    ON PRIMARY (
                        NAME = animals1_db,
                        FILENAME = 'D:\\animals1_db.mdf',
                        SIZE = 5MB,
                        MAXSIZE = 100MB,
                        FILEGROWTH = 10%)
                    LOG ON (
                        NAME = animals1_db_log,
                        FILENAME = 'D:\\animals1_db.ldf',
                        SIZE = 1MB,
                        MAXSIZE = 25MB,
                        FILEGROWTH = 5MB)";

                using (SqlCommand cmd = new SqlCommand(createDb, cn))
                {
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                    richTextBox1.Text += "已建立資料庫\n";
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //建立資料表, 不能重複建立
            //建立資料表 animals1_table
            //建立好資料庫後，你需要連線到 animals1_db，再執行 CREATE TABLE：

            richTextBox1.Text += "建立資料表 (如果不存在)\n";

            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\animals1_db.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();

                string createTable = @"
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='animals1_table' AND xtype='U')
                CREATE TABLE animals1_table (
                    編號 INT,
                    英文名 NVARCHAR(100),
                    中文名 NVARCHAR(100),
                    體重 INT
                )";
                //編號 INT PRIMARY KEY,  //設定主鍵

                using (SqlCommand cmd = new SqlCommand(createTable, cn))
                {
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                    richTextBox1.Text += "已建立資料庫表單\n";
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "新增5筆資料\n";

            // 資料庫檔案
            string db_filename = "animals1_db.mdf";

            // 插入資料, N是必要的(中文之前都要N)
            string sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (1, N'mouse', N'米老鼠', 3)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (2, N'ox', N'班尼牛', 48)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (3, N'tiger', N'跳跳虎', 33)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (4, N'rabbit', N'彼得兔', 8)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (5, N'dragon', N'逗逗龍', 38)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (6, N'snake', N'貪吃蛇', 16)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (7, N'horse', N'草泥馬', 31)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (8, N'goat', N'喜羊羊', 29)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (9, N'monkey', N'山道猴', 22)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (10, N'chicken', N'肯德雞', 5)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (11, N'dog', N'布丁狗', 17)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (12, N'dogpig', N'佩佩豬', 42)";
            sql_write_database(db_filename, sqlstr);  // 執行SQL命令

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "查詢資料\n";

            string selectData = "SELECT 編號, 英文名, 中文名, 體重 FROM animals1_table";
            sql_read_database(db_filename, selectData, dataGridView1);
            lb_dgv1.Text = "新增5筆資料";

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "更新資料\n";

            string updateData = "UPDATE animals1_table SET 體重 = 25 WHERE 編號 = 2";
            sql_write_database(db_filename, updateData);  // 執行SQL命令

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "再次查詢確認更新\n";
            string selectUpdated = "SELECT 編號, 英文名, 中文名, 體重 FROM animals1_table";
            sql_read_database(db_filename, selectUpdated, dataGridView2);
            lb_dgv2.Text = "更新後資料 編號=2, 體重=25";

            richTextBox1.Text += "完成\n";
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //取得一個資料庫的所有Table名稱
            richTextBox1.Text += "取得一個資料庫的所有Table名稱 3 個方法\n";

            // 資料庫檔案
            string db_filename = "db_02.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            richTextBox1.Text += "取得一個資料庫的所有Table名稱 1\n";

            //這樣會列出所有 實際的資料表（不包含檢視表）

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();

                string sqlstr = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'";

                using (SqlCommand cmd = new SqlCommand(sqlstr, cn))
                {
                    SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
                    while (dr.Read())  // 讀取一筆資料到dr
                    {
                        richTextBox1.Text += dr["TABLE_NAME"] + "\n";
                    }
                    dr.Close();
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "取得一個資料庫的所有Table名稱 2\n";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();

                string sqlstr = "SELECT NAME FROM sys.tables";  // 看NAME欄位就好
                //string sqlstr = "SELECT * FROM master..sysdatabases";  // 很多 等同上

                //這個方式直接從 SQL Server 的系統目錄取出所有表單名稱

                using (SqlCommand cmd = new SqlCommand(sqlstr, cn))
                {
                    SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
                    while (dr.Read())  // 讀取一筆資料到dr
                    {
                        for (int i = 0; i < dr.FieldCount; i++)
                        {
                            richTextBox1.Text += dr[i].ToString();
                            if (i == (dr.FieldCount - 1))
                            {
                                richTextBox1.Text += "\n";
                            }
                            else
                            {
                                richTextBox1.Text += "\t";
                            }
                        }
                    }
                    dr.Close();
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "取得一個資料庫的所有Table名稱 3\n";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();
                var schema = cn.GetSchema("TABLES");
                foreach (System.Data.DataRow row in schema.Rows)
                {
                    richTextBox1.Text += row["TABLE_NAME"] + "\n";
                }
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {


            //使用聯合查詢
            /*
            透過UNION語句，
            將高考成績表中總成績大於500的考生與高考學生訊息表中籍貫為中國北京的考生訊息，
            一起顯示在顯示出來。
            */
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            // 查詢字串
            string sqlstr = "SELECT * FROM 高考學生訊息表 SELECT * FROM 高考成績表";

            SqlConnection con = new SqlConnection(cnstr);
            SqlDataAdapter da = new SqlDataAdapter(sqlstr, con);
            DataSet ds = new DataSet();
            da.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            dataGridView2.DataSource = ds.Tables[1].DefaultView;

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            // 查詢字串
            sqlstr = "SELECT 考生編號,姓名,考生類別 FROM 高考學生訊息表 WHERE 籍貫='中國北京' UNION SELECT 考生編號,姓名,考生類別 FROM 高考成績表 WHERE 總成績 > 500 AND 考生類別='文科考生'";

            con = new SqlConnection(cnstr);
            da = new SqlDataAdapter(sqlstr, con);
            ds = new DataSet();
            da.Fill(ds);
            dataGridView3.DataSource = ds.Tables[0].DefaultView;
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //當前網路上運行的SQL伺服器

            //枚举本地网络中的SQL Server所有可用实例
            SqlDataSourceEnumerator instance = SqlDataSourceEnumerator.Instance;
            DataTable table = instance.GetDataSources();//获取所有数据源，并存储到DataTable中
            richTextBox1.Text += table + "\n";
            foreach (DataRow row in table.Rows)//遍历获取到的数据源
            {
                richTextBox1.Text += row + "\n";
                richTextBox1.Text += row["ServerName"] + "\n";
                //listBox1.Items.Add(row["ServerName"]);//向列表中添加遍历到的服务器名
            }
        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {
            // 取得資料庫的表單名稱 1

            // 資料庫檔案
            string db_filename = "db_09_Data.MDF";

            // 查詢字串
            string sqlstr = "SELECT NAME FROM sysdatabases";
            sqlstr = "SELECT NAME FROM master..sysdatabases";
            sqlstr = "SELECT NAME FROM master.dbo.sysdatabases";
            sqlstr = "SELECT NAME FROM master.dbo.sysdatabases ORDER BY Name";
            sqlstr = "SELECT NAME FROM master.dbo.sysdatabases WHERE name='new_db'";
            sqlstr = "SELECT COUNT(*) FROM master.dbo.sysdatabases WHERE name='new_db'";  // 找個數
            sqlstr = "SELECT COUNT(*) FROM master.dbo.sysdatabases";  // 找個數

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

        private void button26_Click(object sender, EventArgs e)
        {
            // 取得資料庫的表單名稱 2
            //SysDatabases

            // 資料庫檔案
            //string db_filename = "db_02.mdf";
            string db_filename = "animals1_db.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = string.Empty;

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();

                //獲取所有數據庫名稱
                //試一下  把 master 改成 dbo
                // 'dbo.tb_XML'.
                sqlstr = "SELECT NAME FROM master.dbo.sysdatabases";
                sqlstr = "SELECT NAME FROM Master.dbo.SysDatabases ORDER BY Name";
                sqlstr = "SELECT COUNT(*) FROM master.dbo.sysdatabases WHERE name='new_db'";//NG

                //獲取所有表單名稱
                sqlstr = "SELECT Name FROM SysObjects WHERE XType='U' ORDER BY Name";
                //XType='U':表示所有用户表;
                //XType='S':表示所有系统表;
                sqlstr = "SELECT name FROM sysobjects WHERE type = 'U'";

                //獲取所有的字段名
                sqlstr = "SELECT Name FROM SysColumns WHERE id=Object_Id('animals1_table')";

                //取得表單格式           欄名             格式                基本大小              總長度
                sqlstr = "SELECT syscolumns.name, systypes.name, syscolumns.isnullable, syscolumns.length FROM syscolumns, systypes WHERE syscolumns.xusertype = systypes.xusertype AND syscolumns.id = object_id('animals1_table')";

                using (SqlCommand cmd = new SqlCommand(sqlstr, cn))
                {
                    SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器

                    richTextBox1.Text += "cnt = " + dr.FieldCount.ToString() + "\n";
                    richTextBox1.Text += dr + "\n";

                    while (dr.Read())  // 讀取一筆資料到dr
                    {
                        richTextBox1.Text += "---------------\n";  // 15個

                        richTextBox1.Text += "欄數 dr.FieldCount = " + dr.FieldCount.ToString() + "\t欄位名稱 :\n";
                        for (int i = 0; i < dr.FieldCount; i++)
                        {
                            richTextBox1.Text += dr.GetName(i) + "\t";
                        }
                        richTextBox1.Text += "\n";

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
                    }
                    richTextBox1.Text += "---------------\n";  // 15個
                }
            }
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
            //檢視 SQL Server 上的資料庫清單

            // 資料庫檔案
            string db_filename = "db_09_Data.MDF";
            // 查詢字串, 檢視 SQL Server 上的資料庫清單
            string sqlstr = "SELECT name, filename FROM sysdatabases";  // 系統查詢資料庫名稱
            sql_read_database(db_filename, sqlstr, dataGridView1);

            // 查詢字串, 檢視 SQL Server 上的資料庫清單, same
            sqlstr = "SELECT name, database_id, create_date FROM sys.databases";  // same
            sql_read_database(db_filename, sqlstr, dataGridView2);

            /*
            // 資料庫檔案
            string db_filename = "db_09_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                DataTable dt = new DataTable();
                SqlDataAdapter da = new SqlDataAdapter("SELECT name FROM sysdatabases", cn);
                da.Fill(dt);
                this.comboBox1.DataSource = dt.DefaultView;
                this.comboBox1.DisplayMember = "name";
                this.comboBox1.ValueMember = "name";

                listBox1.DataSource = dt.DefaultView;
                listBox1.DisplayMember = "name";
                listBox1.ValueMember = "name";

                richTextBox1.Text += "共 : " + comboBox1.Items.Count.ToString() + " 項\n";
            }
            */
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //SQL 簡易測試
            dataGridView1.BringToFront();
            dataGridView2.BringToFront();
            dataGridView3.BringToFront();
            lb_dgv1.BringToFront();
            lb_dgv2.BringToFront();
            lb_dgv3.BringToFront();
            button0.Visible = false;
            button1.Visible = false;
            button2.Visible = false;
            button3.Visible = false;
            button4.Visible = false;
            button5.Visible = false;
            button6.Visible = false;
            button7.Visible = false;
            button8.Visible = false;
            button9.Visible = false;
            button10.Visible = false;
            button11.Visible = false;
            button12.Visible = false;
            button13.Visible = false;
            button14.Visible = false;
            button15.Visible = false;
            button16.Visible = false;
            button17.Visible = false;
            button18.Visible = false;
            button19.Visible = false;
            button20.Visible = false;
            button21.Visible = false;
            button22.Visible = false;
            button23.Visible = false;
            button24.Visible = false;
            button25.Visible = false;
            button26.Visible = false;
            button27.Visible = false;
            button28.Visible = false;
            button29.Visible = false;
            dataGridView4.Visible = false;
            lb_dgv4.Visible = false;

            int W = 930;
            int H = 410;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 64;
            int dd = 46;

            dataGridView1.Size = new Size(W, H);
            dataGridView2.Size = new Size(W, H);
            dataGridView3.Size = new Size(W, H);
            richTextBox1.Size = new Size(W, H);

            lb_dgv1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            dataGridView1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd);
            lb_dgv2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            dataGridView2.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd);
            lb_dgv3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            dataGridView3.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd);

            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 1 + 50);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            W = W - 212;
            bt_previous.Visible = true;
            bt_next.Visible = true;
            lb_index.Visible = true;
            bt_previous.Size = new Size(64, 64);
            bt_next.Size = new Size(64, 64);
            bt_previous.Location = new Point(x_st + dx * 1 + W, y_st + dy * 1 - 16); //new Point(20, 40);
            bt_next.Location = new Point(x_st + dx * 1 + 150 + W, y_st + dy * 1 - 16); //new Point(20, 40 + 100);
            lb_index.Location = new Point(x_st + dx * 1 + 90 + W, y_st + dy * 1 + 20 - 16); //new Point(20 + 20, 40 + 56);
            lb_index.Text = "";
            bt_previous.BringToFront();
            bt_next.BringToFront();
            lb_index.BringToFront();

            this.Size = new Size(1920, 890 + 100);
            this.Text = "vcs_SqlConnection1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);

            show_data_by_sqlcmd(sqlcmd_index);
        }

        void show_data_by_sqlcmd(int idx)
        {
            dataGridView1.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView2.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView3.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView4.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
            lb_dgv3.Text = "";
            lb_dgv4.Text = "";

            // 0          1            2            3           4          5           6        7
            //idx  /  資料庫檔案  /  查詢字串1  /  說明1 /  查詢字串2  /  說明2/  查詢字串3  /  說明3
            //richTextBox1.Text += "idx = " + idx.ToString() + "\n";
            string index = sqlcmd[idx, 0];
            string db_filename = sqlcmd[idx, 1];
            lb_index.Text = index;
            richTextBox1.Clear();

            if (db_filename == "")
            {
                richTextBox1.Text += "編號 :\t無資料\n";
                return;
            }
            else
            {
                richTextBox1.Text += "編號 :\t" + index + "\t資料庫檔案 :\t" + db_filename + "\n";
            }

            string sqlstr = sqlcmd[idx, 2];
            string description = sqlcmd[idx, 3];
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = description + "\n" + sqlstr;
            string mesg = "查詢字串 :\t" + sqlstr + "\n說明 :\t" + description;
            richTextBox1.Text += mesg + "\n";

            if (sqlcmd[idx, 4] != "")
            {
                sqlstr = sqlcmd[idx, 4];
                description = sqlcmd[idx, 5];
                sql_read_database(db_filename, sqlstr, dataGridView2);
                lb_dgv2.Text = description + "\n" + sqlstr;
                mesg = "查詢字串 :\t" + sqlstr + "\n說明 :\t" + description;
                richTextBox1.Text += mesg + "\n";
            }
            if (sqlcmd[idx, 6] != "")
            {
                sqlstr = sqlcmd[idx, 6];
                description = sqlcmd[idx, 7];
                sql_read_database(db_filename, sqlstr, dataGridView3);
                lb_dgv3.Text = description + "\n" + sqlstr;
                mesg = "查詢字串 :\t" + sqlstr + "\n說明 :\t" + description;
                richTextBox1.Text += mesg + "\n";
            }
        }

        int sqlcmd_index = 0;

        private void bt_previous_Click(object sender, EventArgs e)
        {
            //上一個
            int total_sqlcmd = sqlcmd.GetUpperBound(0) + 1;
            //richTextBox1.Text += "total_sqlcmd = " + total_sqlcmd.ToString() + "\n";
            if (sqlcmd_index == 0)
            {
                sqlcmd_index = total_sqlcmd - 1;
            }
            else
            {
                sqlcmd_index--;
            }
            show_data_by_sqlcmd(sqlcmd_index);
        }

        private void bt_next_Click(object sender, EventArgs e)
        {
            //下一個
            int total_sqlcmd = sqlcmd.GetUpperBound(0) + 1;
            //richTextBox1.Text += "total_sqlcmd = " + total_sqlcmd.ToString() + "\n";
            sqlcmd_index++;
            if (sqlcmd_index >= total_sqlcmd)
            {
                sqlcmd_index = 0;
            }
            show_data_by_sqlcmd(sqlcmd_index);
        }

        //二維字串串列
        string[,] sqlcmd = new string[,]
        {
            //idx  /  資料庫檔案  /  查詢字串1  /  說明1 /  查詢字串2  /  說明2/  查詢字串3  /  說明3
            /*
            { "1", "animals1_db.mdf", "SELECT * FROM animals1_table", "十二生肖全部資料", "", "", "", ""},
            { "2", "db_09_Data.mdf",
                "SELECT * FROM 員工表", "", "", "", "", ""},
            { "3", "db_TomeTwo.mdf",
                "SELECT TOP 10 * FROM (SELECT TOP 20 * FROM tb_Grade ORDER BY 总分 DESC) AS st ORDER BY 总分 ASC", "查询第10到第20名的数据", "", "", "", ""},
            { "4", "db_TomeTwo.mdf",
                "SELECT * FROM tb_Book", "", "", "", "", ""},
            { "5", "db_TomeTwo.mdf",
                "SELECT TOP 50 PERCENT 书号,书名,SUM(销售数量)AS 合计销售数量 FROM tb_Book GROUP BY 书号,书名,作者 ORDER BY 3 DESC", "查询销售量占前50%的图书信息, 查询数据库信息", "", "", "", ""},
            { "6", "db_10_Data.MDF",
                "SELECT * FROM 員工訊息表",
                "員工訊息表",
                "SELECT * FROM 員工工資表",
                "員工工資表",
                "SELECT 員工訊息表.員工姓名, 員工訊息表.員工編號, 員工訊息表.聯繫電話, 員工工資表.基本工資 FROM 員工訊息表 INNER JOIN 員工工資表 ON 員工訊息表.員工編號 = 員工工資表.員工編號",
                "簡單 內連接 查詢 INNER JOIN"},
            { "7", "db_13.mdf",
                "SELECT * FROM tb_Rectangle",
                "",
                "SELECT TOP 3 * FROM tb_Rectangle ORDER BY t_Num DESC",
                "排序, DESC降冪, ASC升冪",
                "SELECT SUM(t_Num) FROM tb_Rectangle",
                ""},
            { "8", "db_10_Data.MDF", "SELECT * FROM tb_07", "全部資料", "SELECT * FROM tb_07 WHERE 出生日期='1984/1/24'", "查詢日期數據", "", ""},
            { "9", "db_10_Data.MDF", "SELECT * FROM tb_stu", "全部資料", "SELECT * FROM tb_stu WHERE 出生年月='1983/4/2'", "查詢日期數據", "", ""},
            { "10", "db_10_Data.MDF", "SELECT * FROM tb_stu", "全部資料", "SELECT * FROM tb_stu WHERE 學生編號 like '20014103'", "利用通配符進行查詢", "", ""},
            { "11", "db_10_Data.MDF", "SELECT 書號,書名,銷售數量,日期 FROM tb_xsb", "全部資料", "SELECT 書號,書名,銷售數量,日期 FROM tb_xsb WHERE year(日期)='2005' AND month(日期)='10' AND day(日期)='1'", "按年、月或日查詢數據", "", ""},
            { "12", "Database1.mdf", "SELECT * FROM 產品資料", "全部資料, 產品資料", "SELECT 產品編號,品名,單價,說明 FROM 產品資料 WHERE 類別編號=1", "查詢 類別編號 = 1 的資料", "", ""},
            { "13", "db_10_Data.MDF", "SELECT * FROM tb_stu, tb_mark", "全部資料 tb_stu, tb_mark", "SELECT distinct 學生姓名,學生編號, 性別,出生年月,年齡,所在學院,所學專業 FROM tb_stu WHERE 學生姓名 IN (SELECT  學生姓名 FROM tb_mark WHERE 總分>=580)", "簡單內嵌查詢, 查詢總分在580分以上的學生訊息", "", ""},
            { "14", "db_10_Data.MDF", "SELECT * FROM 顧客表, 僱員表", "全部資料 顧客表, 僱員表", "SELECT 顧客編號 AS 編號,顧客姓名 AS 姓名,所在城市,郵編 FROM 顧客表 UNION SELECT 僱員編號,僱員名稱,家庭住址,郵編 FROM 僱員表", "合併多個結果集, 利用UNION運算符完成將顧客表和僱員表中的編號、姓名、地址、郵編字段合併到一個表中", "", ""},
            { "15", "db_10_Data.MDF", "SELECT * FROM tb_rkb", "全部資料 tb_rkb", "SELECT 存放位置,書名,SUM(庫存數量) AS 合計庫存數量 FROM tb_rkb GROUP BY 存放位置,書名 ORDER BY 1", "按倉庫分組統計圖書庫存（多列）, 按倉庫名、圖書名稱進行分組，並統計其庫存數量", "", ""},
            { "16", "db_10_Data.MDF", "SELECT * FROM 學生成績表", "全部資料, 有4個表, 對聯合查詢後的結果進行排序", "SELECT cast(成績 AS varchar(20)) AS 成績 FROM 學生成績表 UNION SELECT DISTINCT 課程編號 FROM 學生訊息表 UNION SELECT 課程名稱 FROM 課程表 WHERE 課程名稱 = '計算機英語' UNION SELECT CONVERT(varchar(20), 出勤率) FROM 學生考勤表 WHERE 出勤率 > 0.8 ORDER BY 成績 DESC", "降序排序", "SELECT cast(成績 AS varchar(20)) AS 成績 FROM 學生成績表 UNION SELECT DISTINCT 課程編號 FROM 學生訊息表 UNION SELECT 課程名稱 FROM 課程表 WHERE 課程名稱 = '計算機英語' UNION SELECT CONVERT(varchar(20), 出勤率) FROM 學生考勤表 WHERE 出勤率 > 0.8", "升序排序"},
            { "17", "db_10_Data.MDF", "SELECT 產品編號,產品名稱,產品單價,產品數量 FROM tb_03", "全部資料, 原本資料4欄", "SELECT 產品編號,產品名稱,產品單價,產品數量,(產品數量*產品單價) AS 總金額 FROM tb_03", "查詢特定數據列, 加上1欄資料, 在列上加入計算, 在列上加入計算, 加了 總金額 這欄, 內容是 產品數量*產品單價", "", ""},
            { "18", "db_10_Data.MDF", "SELECT * FROM xsb", "全部資料 xsb", "SELECT k.書號,k.書名,x.作者,SUM(k.現存數量)AS 現存數量,SUM(x.銷售數量)AS 銷售數量 FROM xsb x ,kcb k WHERE x.書號=k.書號 GROUP BY k.書號,k.書名,x.作者, k.現存數量 ORDER BY 1", "多表分組統計, 查詢圖書的銷售數量和現存數量，並按書號、書名等分組", "", ""},
            { "19", "db_10_Data.MDF", "SELECT * FROM 員工訊息表", "全部資料 員工訊息表", "SELECT 員工訊息表.員工編號, 員工訊息表.員工姓名 FROM 員工訊息表 INNER JOIN 員工工資表 ON 員工訊息表.員工編號 = 員工工資表.員工編號", "使用內連接選擇一個表與另一個表中行相關的所有行", "SELECT 員工訊息表.員工編號, 員工訊息表.員工姓名, 員工工資表.基本工資, 加班訊息表.加班天數, 加班訊息表.加班費 FROM 員工訊息表 INNER JOIN 加班訊息表 ON 員工訊息表.員工編號 = 加班訊息表.員工編號 INNER JOIN 員工工資表 ON 加班訊息表.員工編號 = 員工工資表.員工編號", "複雜內連接查詢, 員工訊息表、員工工資表和加班訊息表中，使用內連接查詢出加班員工的基本訊息。"},
            { "20", "db_TomeTwo.mdf", "SELECT * FROM tb_Student", "看全部欄位", "SELECT 学生姓名,年龄,性别,家庭住址 FROM tb_Student", "只看部分欄位", "SELECT 学生姓名,年龄,性别,家庭住址 FROM tb_Student WHERE 学生姓名 LIKE '李%' and 年龄 LIKE '2%' and 家庭住址 LIKE '吉林%'", "複雜的模糊查詢 姓名年齡住址"},
            { "21", "db_10_Data.MDF", "SELECT 姓名 FROM 學生訊息表 UNION SELECT 課程名稱 FROM 課程表 WHERE 課程名稱='計算機英語' UNION SELECT convert(varchar(20),成績) FROM 學生成績表 WHERE 成績 > 90 UNION SELECT convert(varchar(20),出勤率) FROM 學生考勤表 WHERE 出勤率 > 0.8", "多表聯合查詢", "", "", "", ""},
            { "22", "db_10_Data.MDF", "SELECT * FROM tb_Stu", "全部資料 tb_Stu", "SELECT 學生姓名, COUNT(*) AS 相同數量 FROM (SELECT top 10 學生姓名 FROM tb_Stu order BY 學生編號 ASC )AS T GROUP BY 學生姓名", "用子查詢作派生的表, 顯示學生編號排在前10位，而且具有相同名字的學生個數", "", ""},
            { "23", "db_10_Data.MDF", "SELECT * FROM 工資數據表", "全部資料 工資數據表", "SELECT * FROM 部門表", "全部資料 部門表", "SELECT * FROM 工資數據表 WHERE 工資月份=10 AND 人員姓名 IN( SELECT 負責人 FROM 部門表 WHERE 負責人 IN(SELECT 人員姓名 FROM 人員表 WHERE 學歷='本科')) ORDER BY 人員編號", "複雜內嵌查詢, 查詢學歷是本科的部門經理的2005年10月份的工資情況"},
            { "24", "db_10_Data.MDF", "SELECT * FROM tb_stu s ,tb_mark", "全部資料 tb_stu, tb_mark 兩表單一起顯示", "SELECT distinct S.學生編號,S.學生姓名,M.高數,M.外語,M.馬經,S.所在學院 FROM tb_stu AS S,tb_mark AS M WHERE S.學生編號=M.學生編號 AND S.所在學院='計算機學院'", "使用表別名, 利用表的別名查詢計算機分院學生的成績", "SELECT distinct s.學生編號,s.學生姓名,s.性別,s.出生年月,s.年齡,s.所在學院,s.所學專業,m.高數 FROM tb_stu s ,tb_mark m WHERE s.學生編號=m.學生編號 AND m.高數 >85", "利用FROM子句進行多表查詢, 查詢高數成績大於85分的學生的詳細訊息"},
            { "25", "db_10_Data.MDF", "SELECT * FROM tb_BookSell", "全部資料 tb_BookSell", "SELECT 書名,出版社,SUM(金額) AS 總計金額 FROM tb_BookSell WHERE 出版社='機械' GROUP BY all 書名,出版社", "在分組查詢中使用ALL關鍵字, 在圖書銷售表中對機械出版社出版的不同圖書的銷售情況進行統計，並列出其他出版社的圖書（不作統計）", "", ""},
            { "26", "db_TomeOne.mdf", "SELECT * FROM tb_manpower", "有兩欄資料 t_Point t_Num", "SELECT SUM(t_Num) FROM tb_manpower", "將 t_Num 加總", "SELECT t_Point, SUM(t_Num) FROM tb_manpower GROUP BY t_Point ORDER BY SUM(t_Num) DESC", "合併 t_Point 資料, 降冪排序, 將 t_Num 加總 有合併資料"},
            { "27", "db_TomeTwo.mdf", "SELECT * FROM tb_Student", "tb_Student 的 所有資料", "SELECT * FROM tb_Grade", "tb_Grade 的 所有資料", "SELECT 学生姓名,性别,年龄 FROM tb_Student WHERE 学生编号 IN (SELECT 学生编号 FROM tb_Grade WHERE 总分>550 AND 总分<570)", "使用IN引入子查詢限定查詢範圍, 查詢學生總分在 550 ~ 570 之間, 查 tb_Student 的 資料, 由 tb_Grade 總分在 500 ~ 600 之間"},
            { "28", "db_TomeOne.mdf", "SELECT * FROM tb_product", "全部資料 tb_product 兩欄 t_Name t_Num", "SELECT SUM(t_Num) FROM tb_product", "將 t_Num 加總", "SELECT t_Name, SUM(t_Num) AS Num FROM tb_product GROUP BY t_Name", "將 t_Name 同項合併"},
            { "29", "db_10_Data.MDF", "SELECT * FROM tb_kf WHERE 房態='空房 '", "查詢空閒客房訊息", "SELECT * FROM tb_kf WHERE 房態='入住'", "查詢使用客房訊息", "SELECT * FROM tb_kf WHERE 房態='空房 ' AND NOT(價格 between 80 and 150 )", "NOT與謂詞進行組合條件的查詢, 查詢空閒客房而且客房價格不在８０-１５０之間的客房訊息"},
            */
            { "30", "db_TomeTwo.mdf", "SELECT * FROM tb_Book", "全部資料 tb_Book", "SELECT COUNT(书号)AS 记录条数, 书号,书名,作者 FROM tb_Book GROUP BY 书号,书名,作者 HAVING COUNT(书号)>1", "查询已销售图书情况, 列出数据中的重复记录和记录条数", "", ""},
            { "31", "db_13.mdf", "SELECT * FROM tb_Rectangle", "全部資料", "SELECT SUM(t_Num) FROM tb_Rectangle", "水果出售情況統計表", "", ""},
            { "32", "", "", "", "", "", "", ""},
            { "33", "", "", "", "", "", "", ""},
            { "34", "", "", "", "", "", "", ""},
            { "35", "", "", "", "", "", "", ""},

            //{ "編號", "檔案", "查詢1", "說明1", "查詢2", "說明2", "查詢3", "說明3"},
        };
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
//richTextBox1.Text += "---------------\n";  // 15個
//---------------  # 15個


/*  可搬出

 */

//其實 Server= 和 Data Source= 在 SQL Server 的 Connection String 裡是等價的，兩者都是用來指定要連線的伺服器或資料來源。

/*
SQL不同的連線方式
1. Database=new_db;
這種寫法表示你要連線到 SQL Server 已經註冊的資料庫。
- Database=new_db; → 連線到 SQL Server 已經掛載的資料庫。

2. AttachDbFilename=D:\new_db.mdf;
這種寫法表示你要直接 附加 (Attach) 一個 MDF 檔案，讓 SQL Server 在執行時載入它。
直接附加 MDF 檔案，常用於 LocalDB 或測試。
*/

/*
// 查詢字串
            string sqlstr = "SELECT emp_id AS 用戶編號,fname AS 用戶姓名,hire_date AS 工作時間 FROM employee";//定義一個查詢字符串變量

            DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            ds.Clear();//清空數據集中原有內容
            try
            {
                using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
                {
                    da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                    da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                }
            }
            catch (Exception ex)//捕獲異常
            {
                richTextBox1.Text += ex.Message + "\n";
            }
            finally
            {
                cn.Close();//關閉數據庫連接
            }

            //顯示數據 DataTable => DGV
            dataGridView1.Rows.Clear();//清空DataGridView中原有的數據
            object[] item = new object[dt.Columns.Count];//定義一個object類型的數組
                int R = dt.Rows.Count;
                richTextBox1.Text += "R = " + R.ToString() + "\n";
            for (int i = 0; i < R; i++)//循環遍歷數據表中的每一行數據
            {
                for (int j = 0; j < dt.Columns.Count; j++)//循環遍歷數據表中每一列數據
                {
                    item[j] = dt.Rows[i][j];//保存數據表中的數據內容
                }
                dataGridView1.Rows.Add(item);//向DataGridView中添加數據
            }
*/

/*
用MSSQLLocalDB
AttachDbFilename=|DataDirectory|ch17DB.mdf  是 mdf 在 |DataDirectory|之下
AttachDbFilename=D:\ch17DB.mdf 是 指定 mdf 的位置

連接字串固定的寫法 :
Data Source=(LocalDB)\MSSQLLocalDB;
AttachDbFilename=xxxxx.mdf;
Integrated Security=True";
Connect Timeout=30
*/

//宣告cnStr連線字串置於事件處理函式外，以提供給其他事件處理函式共用
//string cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\MyDB.mdf;Integrated Security=True;Connect Timeout=30";
// 連接字串
// String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\VisualC#2015基礎必修課\2015範例程式\data\MyDB.mdf;Integrated Security=True;Connect Timeout=30";

//combobox 類別編號
//cboCategoryId.DisplayMember = "類別名稱";//指定Text屬性繫結的是類別名稱
//cboCategoryId.ValueMember = "類別編號";  //指定Value屬性繫結的是類別編號
//int CategoryId1 = int.Parse(cboCategoryId.SelectedValue.ToString());
//int CategoryId2 = int.Parse(cboCategoryId.SelectedValue.ToString());
//int CategoryId3 = int.Parse(cboCategoryId.SelectedValue.ToString());

//dataGridView1.CurrentRow.Cells[0].Value
//dataGridView1.CurrentRow.Cells[0].Value

/*
        Bitmap bitM = new Bitmap(this.pictureBox1.Width, this.pictureBox1.Height);  // 创建画布
        Graphics g = Graphics.FromImage(bitM);  // 创建Graphics对象
        Pen p = new Pen(new SolidBrush(Color.SlateGray), 1.0f);  // 创建Pen对象
        p.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;  // 设置虚线
        g.Clear(Color.White);  // 设置画布颜色

        int x, y, w, h;  // 声明变量存储坐标和大小
        g.DrawString(dr[0].ToString(), new Font("宋体", 9, FontStyle.Regular), new SolidBrush(Color.Black), 76 + 40 * j, this.pictureBox1.Height - 16);  // 绘制商品名称
        x = 78 + 40 * j;  // X坐标

        //richTextBox1.Text += "bbbb : " + Convert.ToInt32((Convert.ToDouble(Convert.ToDouble(dr[1].ToString()) * 20 / 100))) + "\n";
        y = this.pictureBox1.Height - 20 - Convert.ToInt32((Convert.ToDouble(Convert.ToDouble(dr[1].ToString()) * 20 / 100)));  // Y坐标

        w = 24;  // 宽度

        richTextBox1.Text += "cccc : " + dr[1].ToString() + "\n";
        //richTextBox1.Text += "cccc : " + Convert.ToInt32(Convert.ToDouble(dr[1].ToString()) * 20 / 100) + "\n";
        h = Convert.ToInt32(Convert.ToDouble(dr[1].ToString()) * 20 / 100);  // 高度

        g.FillRectangle(new SolidBrush(Color.SlateGray), x, y, w, h);  // 绘制柱形图
        g.DrawString((h * 100 / 20).ToString(), new Font("宋体", 8, FontStyle.Bold), new SolidBrush(Color.Tomato), new Point(x + 4, y - 10));  // 在柱形图指定的位置绘制文字
        this.pictureBox1.BackgroundImage = bitM;  // 显示绘制的图形
*/

// string sqlstr = "SELECT job_id AS 工作编号, job_desc AS 工作次序, min_lvl AS 最低水平, max_lvl AS 最高水平 FROM jobs";

/*
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT au_id AS 使用者編號,au_lname AS 姓名,phone AS 電話號碼 FROM authors";//初始化SQL查詢語句
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "authors");  // da將查詢的結果填充至數據集ds, 指定TableName為"authors"
                dataGridView1.DataSource = ds.Tables["authors"].DefaultView;//為DataGridView控制元件填充數據源
                for (int i = 0; i < dataGridView1.Columns.Count; i++)//循環搜尋DataGridView控制元件中的每一列
                {
                    //禁用DataGridView控制元件列表頭自動排序功能
                    dataGridView1.Columns[i].SortMode = DataGridViewColumnSortMode.NotSortable;//設定每一列的排序類型為不排序
                }
            }
*/

//SqlDataAdapter 資料庫適配器對象 数据库桥接器对象 數據讀取器

//richTextBox1.Text += dr["TABLE_NAME"] + "\n";

            //db_02.mdf
            //string sqlstr2 = "SELECT * FROM tb_05";

            //新增
            //string name = "david";
            //string position = "engineering";
            //string telephone = "0912345678";
            //int salary = 55555;

                    /* same
                    // 查詢字串
                    string sqlstr = "INSERT INTO 員工(姓名, 職稱, 電話, 薪資) VALUES('" + name + "','" + position + "','" + telephone + "'," + salary + ")";
                    SqlCommand cmd = new SqlCommand(sqlstr, cn);
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                    */
/*
                    // 查詢字串
                    sqlstr = "INSERT INTO 員工(姓名, 職稱, 電話, 薪資)" + "VALUES(@name, @position, @tel, @salary)";
                    SqlCommand cmd = new SqlCommand(sqlstr, cn);
                    cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@position", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@tel", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@salary", SqlDbType.Int));
                    cmd.Parameters["@name"].Value = name;
                    cmd.Parameters["@position"].Value = position;
                    cmd.Parameters["@tel"].Value = telephone;
                    cmd.Parameters["@salary"].Value = salary;
                    cmd.ExecuteNonQuery();  // 執行SQL命令
*/
            
            //修改

            //string position2 = "manager";
            //string telephone2 = "0987654321";
//int salary2 = 66666;

                    /* same
                    // 查詢字串
                    string sqlstr = "UPDATE 員工 SET 職稱 = '" + position2 + "',電話 = '" + telephone2 + "', 薪資 = " + salary2 + " WHERE 姓名 = '" + name + "'";
                    SqlCommand cmd = new SqlCommand(sqlstr, cn);
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                    */
/*
                    // 查詢字串
                    sqlstr = "UPDATE 員工 SET 職稱=@position," + "電話=@tel, 薪資=@salary WHERE 姓名=@name";
                    SqlCommand cmd = new SqlCommand(sqlstr, cn);
                    cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@position", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@tel", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@salary", SqlDbType.Int));
                    cmd.Parameters["@name"].Value = name;
                    cmd.Parameters["@position"].Value = position2;
                    cmd.Parameters["@tel"].Value = telephone2;
                    cmd.Parameters["@salary"].Value = salary2;
                    cmd.ExecuteNonQuery();  // 執行SQL命令
*/



/*
//------------------------------------------------------------  # 60個


//------------------------------------------------------------  # 60個
*/


// OK 的 SQL語法


/* same
// 查詢字串
string sqlstr = "DELETE FROM 員工 WHERE 姓名 = '" + name + "'";
SqlCommand cmd = new SqlCommand(sqlstr, cn);
cmd.ExecuteNonQuery();  // 執行SQL命令

// 查詢字串
sqlstr = "DELETE FROM 員工 WHERE 姓名 = @name";
SqlCommand cmd = new SqlCommand(sqlstr, cn);
cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
cmd.Parameters["@name"].Value = name;
cmd.ExecuteNonQuery();  // 執行SQL命令
*/

/*
// AS 的用法 "SELECT au_id AS 使用者編號,au_lname AS 使用者名,phone AS 聯繫電話 FROM authors";
// 查詢字串, 使用別名 AS
"SELECT " + comboBox1.Text + "," + comboBox1.Text + " AS " + textBox1.Text.Trim() + " FROM tb_02";
"SELECT * FROM tb_08 WHERE " + comboBox1.Text + " IS null OR " + comboBox1.Text + "=''", cn);//透過SQL語句查詢數據表中的空數據
*/



/*

            //搜尋範例
            string name = "阿龍";
            sqlstr = "SELECT * FROM 成績單 WHERE 姓名 = '" + name + "'";
            //sqlstr = "SELECT * FROM 成績單 WHERE 姓名 = '" + name.Replace("'", "''") + "'";//有些名字有'
*/


/*
            string db_filename = "ch18DB.mdf";
            string sqlstr = "SELECT * FROM 成績單";
            // 查詢字串, 依國文成績降冪排列
            sqlstr = "SELECT * FROM 成績單 ORDER BY 國文 DESC";
*/

/*
            // 資料庫檔案
            string db_filename = "ch17DB.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM 銀行帳戶";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 銀行帳戶";

            string src_ID = "A003";
            string dst_ID = "A004";
            sqlstr = "SELECT * FROM 銀行帳戶 WHERE 帳號='" + src_ID + "'";
            sqlstr = "SELECT * FROM 銀行帳戶 WHERE 帳號='" + dst_ID + "'";
            // 查詢字串
            sqlstr = "SELECT * FROM 銀行帳戶";

*/


/*
                //資料放在表格的第[0][0]格
                int sum_year = Convert.ToInt32(ds.Tables[0].Rows[0][0].ToString());
                richTextBox1.Text += "年度總和 : " + sum_year.ToString() + "\n";
*/




/*

                //加入資料庫之圖片處理 sqldb
                FileStream FStream = new FileStream(openFileDialog1.FileName, FileMode.Open, FileAccess.Read);
                BinaryReader BReader = new BinaryReader(FStream);
                byte[] byteImage = BReader.ReadBytes((int)FStream.Length);
                sqlcmd.Parameters.Add("@photo", SqlDbType.Image).Value = byteImage;


從資料庫取出圖片資料 sqldb
                MemoryStream MStream = new MemoryStream((byte[])myds.Tables[0].Rows[0][10]);
                imgPhoto = Image.FromStream(MStream);  //记录学生头像
*/                


//            sqlstr = "DELETE FROM PRProduceItem WHERE PRProduceCode = '" + strPRProduceCode + "'";
            //sqlstr = "DELETE FROM PRProduce     WHERE PRProduceCode = '" + strPRProduceCode + "'";

