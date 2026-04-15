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
            btn_sql_test.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            btn_sql_test.BackColor = Color.Pink;
            groupBox1.Visible = false;

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
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        int select = 0;
        private void button0_Click(object sender, EventArgs e)
        {
            //讀取資料庫 至 DGV, 要先知道資料庫檔案(.mdf)和表單名稱(table_name)和查詢條件

            // 資料庫檔案
            string db_filename = string.Empty;
            // 查詢字串
            string sqlstr = string.Empty;

            if (select == 0)
            {
                richTextBox1.Text += "第 0 種\n";
            }
            else if (select == 1)
            {
                richTextBox1.Text += "第 1 種\n";
            }
            else if (select == 2)
            {
                richTextBox1.Text += "第 2 種\n";
            }
            else if (select == 3)
            {
                richTextBox1.Text += "第 3 種\n";
            }
            else if (select == 4)
            {
                richTextBox1.Text += "第 4 種\n";
            }
            else if (select == 5)
            {
                richTextBox1.Text += "第 5 種\n";
            }
            else if (select == 6)
            {
                richTextBox1.Text += "第 6 種\n";
            }
            else if (select == 7)
            {
                richTextBox1.Text += "第 7 種\n";
            }
            else
            {
                richTextBox1.Text += "xxxxxxx\n";
            }

            select++;
            if (select > 7)
                select = 0;

            sql_read_database(db_filename, sqlstr, dataGridView1);

            /* 準備加入
            
            */
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
            ds = new DataSet();//初始化數據集
            da.Fill(ds, "WidgetApply");//填充數據集

            dataGridView1.DataSource = ds.Tables["WidgetApply"];  // DGV設置數據源
            lb_dgv1.Text = "產品名稱,產品說明\n";

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
            //簡單SQL命令 6060區分

            //查詢字串 WHERE 的用法

            // 資料庫檔案
            string db_filename = "Database1.mdf";

            string sqlstr = "SELECT * FROM 產品資料";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 產品資料";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢字串 WHERE 的用法
            //產品資料管理, 查詢 類別編號 = 1 的資料
            int CategoryId1 = 1;
            // 查詢字串, 只看一些欄位, 加上條件
            sqlstr = "SELECT 產品編號,品名,單價,說明 FROM 產品資料 WHERE 類別編號=" + CategoryId1;
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "查詢 類別編號 = 1 的資料";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //簡單內嵌查詢

            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT * FROM tb_stu, tb_mark";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tb_stu, tb_mark";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //簡單內嵌查詢
            //查詢總分在５８０分以上的學生訊息

            sqlstr = "SELECT distinct 學生姓名,學生編號, 性別,出生年月,年齡,所在學院,所學專業 FROM tb_stu WHERE 學生姓名 IN (SELECT  學生姓名 FROM tb_mark WHERE 總分>=580)";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //合併多個結果集

            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT * FROM 顧客表, 僱員表";
            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "全部資料 顧客表, 僱員表";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //合併多個結果集
            //利用UNION運算符完成將顧客表和僱員表中的編號、姓名、地址、郵編字段合併到一個表中。
            sqlstr = "SELECT 顧客編號 AS 編號,顧客姓名 AS 姓名,所在城市,郵編 FROM 顧客表 union SELECT 僱員編號,僱員名稱,家庭住址,郵編 FROM 僱員表";
            sql_read_database(db_filename, sqlstr, dataGridView4);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //mmmm 2 簡單範例4個

            //按倉庫分組統計圖書庫存（多列）
            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT * FROM tb_rkb";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text += "全部資料 tb_rkb";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //按倉庫分組統計圖書庫存（多列）
            //按倉庫名、圖書名稱進行分組，並統計其庫存數量

            sqlstr = "SELECT 存放位置,書名,SUM(庫存數量) AS 合計庫存數量 FROM tb_rkb GROUP BY 存放位置,書名 ORDER BY 1";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //降序排序/升序排序

            //對聯合查詢後的結果進行排序

            db_filename = "db_10_Data.MDF";

            //降序排序
            sqlstr = "SELECT cast(成績 AS varchar(20)) AS 成績 FROM 學生成績表 UNION SELECT DISTINCT 課程編號 FROM 學生訊息表 UNION SELECT 課程名稱 FROM 課程表 WHERE 課程名稱 = '計算機英語' UNION SELECT CONVERT(varchar(20), 出勤率) FROM 學生考勤表 WHERE 出勤率 > 0.8 ORDER BY 成績 DESC";
            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text += "降序排序";

            //升序排序
            sqlstr = "SELECT cast(成績 AS varchar(20)) AS 成績 FROM 學生成績表 UNION SELECT DISTINCT 課程編號 FROM 學生訊息表 UNION SELECT 課程名稱 FROM 課程表 WHERE 課程名稱 = '計算機英語' UNION SELECT CONVERT(varchar(20), 出勤率) FROM 學生考勤表 WHERE 出勤率 > 0.8";
            sql_read_database(db_filename, sqlstr, dataGridView4);
            lb_dgv4.Text += "升序排序";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //mmmm 1 簡單範例4個

            //查詢特定數據列
            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT 產品編號,產品名稱,產品單價,產品數量 FROM tb_03";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "原本資料4欄";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //在列上加入計算, 加了 總金額 這欄, 內容是 產品數量*產品單價
            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT 產品編號,產品名稱,產品單價,產品數量,(產品數量*產品單價) AS 總金額 FROM tb_03";
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "加上1欄資料, 在列上加入計算";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //mmmm 7 簡單範例4個

            //多表分組統計

            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT * FROM xsb";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 xsb";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //多表分組統計
            //查詢圖書的銷售數量和現存數量，並按書號、書名等分組
            sqlstr = "SELECT k.書號,k.書名,x.作者,SUM(k.現存數量)AS 現存數量,SUM(x.銷售數量)AS 銷售數量 FROM xsb x ,kcb k WHERE x.書號=k.書號 GROUP BY k.書號,k.書名,x.作者, k.現存數量 ORDER BY 1";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //mmmm 5 簡單範例4個

            db_filename = "db_10_Data.MDF";
            //sqlstr = "SELECT 員工訊息表.員工編號, 員工訊息表.員工姓名 FROM 員工訊息表 INNER JOIN 員工工資表 ON 員工訊息表.員工編號 = 員工工資表.員工編號";
            sqlstr = "SELECT * FROM 員工訊息表";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 員工訊息表";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用內連接選擇一個表與另一個表中行相關的所有行
            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT 員工訊息表.員工編號, 員工訊息表.員工姓名 FROM 員工訊息表 INNER JOIN 員工工資表 ON 員工訊息表.員工編號 = 員工工資表.員工編號";
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "使用內連接";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //複雜內連接查詢
            //員工訊息表、員工工資表和加班訊息表中，使用內連接查詢出加班員工的基本訊息。
            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT 員工訊息表.員工編號, 員工訊息表.員工姓名, 員工工資表.基本工資, 加班訊息表.加班天數, 加班訊息表.加班費 FROM 員工訊息表 INNER JOIN 加班訊息表 ON 員工訊息表.員工編號 = 加班訊息表.員工編號 INNER JOIN 員工工資表 ON 加班訊息表.員工編號 = 員工工資表.員工編號";
            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "複雜內連接查詢";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // 成績單 1 ch17DB.mdf

            // 資料庫檔案
            string db_filename = "ch17DB.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 成績單";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "成績單 全部資料";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //成績單 搜尋1

            // 資料庫檔案
            db_filename = "ch17DB.mdf";
            string name = "阿龍";
            sqlstr = "SELECT * FROM 成績單 WHERE 姓名 = '" + name + "'";
            //sqlstr = "SELECT * FROM 成績單 WHERE 姓名 = '" + name.Replace("'", "''") + "'";//有些名字有'
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 成績單 2 ch18DB.mdf

            // 資料庫檔案
            db_filename = "ch18DB.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM 成績單";
            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "成績單 全部資料 原始資料";

            //成績單+搜尋條件

            // 資料庫檔案
            db_filename = "ch18DB.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM 成績單 ORDER BY 國文 DESC";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串, 可有可無

                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "成績單");  // da將查詢的結果填充至數據集ds, 指定TableName為"成績單"

                DataView dv;  // 宣告DataView物件dv

                dv = ds.Tables["成績單"].DefaultView;

                //依國文成績降冪排列
                dataGridView4.DataSource = dv;  // DGV設置數據源
                lb_dgv4.Text = "成績單 依國文成績降冪排列";

                //國文成績 > 70 的, 依英文成績降冪排列
                string filter = "國文>70";  // 篩選條件, 用WHRER語法
                string sort = "英文 DESC";  // 排序方法, 科目, ASC:遞增, DESC:遞減
                richTextBox1.Text += "篩選條件 : " + filter + "\n";
                richTextBox1.Text += "排序方法 : " + sort + "\n";

                dv.RowFilter = filter;
                dv.Sort = sort;

                dataGridView4.DataSource = dv;  // DGV設置數據源
                lb_dgv4.Text = "國文成績 > 70 的, 依英文成績降冪排列";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            // 轉帳

            // 資料庫檔案
            string db_filename = "ch17DB.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            string table_name = "銀行帳戶";
            // 查詢字串
            string sqlstr = "SELECT * FROM " + table_name;
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 " + table_name;

            richTextBox1.Text += "------------------------------\n";  // 30個

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                string src_ID = "A003";
                string dst_ID = "A004";
                int money = 500;

                //cn.ConnectionString = cnstr;  // 連接字串, 可有可無
                cn.Open();  // 打開資料庫連線

                // 建立SqlCommand物件cmd1，用來查詢使用者帳號是否存在
                // 查詢字串
                sqlstr = "SELECT * FROM 銀行帳戶 WHERE 帳號='" + src_ID + "'";
                SqlCommand cmd1 = new SqlCommand(sqlstr, cn);

                // 建立SqlCommand物件cmd1，用來查詢轉入帳號是否存在
                // 查詢字串
                sqlstr = "SELECT * FROM 銀行帳戶 WHERE 帳號='" + dst_ID + "'";
                SqlCommand cmd2 = new SqlCommand(sqlstr, cn);

                // 傳回SqlDataReader物件dr1，用來查詢使用者帳號是否存在
                SqlDataReader dr1 = cmd1.ExecuteReader();  // 建立數據讀取器
                if (!dr1.Read())  // 讀取一筆資料到dr !不存在
                {
                    richTextBox1.Text += "你的帳號" + src_ID + "錯誤\n";
                    return;
                }

                // 取得使用者的餘額並定給myMoney
                int myMoney = int.Parse(dr1["餘額"].ToString());
                dr1.Close();  // 關閉SqlDataRader物件dr1

                // 傳回SqlDataReader物件dr2，用來查詢轉入帳號是否存在
                SqlDataReader dr2 = cmd2.ExecuteReader();  // 建立數據讀取器
                if (!dr2.Read())  // 讀取一筆資料到dr !不存在
                {
                    richTextBox1.Text += "轉入帳號" + dst_ID + "錯誤\n";
                    return;
                }
                dr2.Close();  // 關閉SqlDataRader物件dr2

                try
                {
                    // 若使用者餘額小於轉入金額，則執行下列敘述
                    if (myMoney < money)
                    {
                        richTextBox1.Text += src_ID + "帳號沒這麼多存款\n";
                        return;
                    }
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += ex.Message + ", 金額請輸入數值\n";
                    return;
                }

                // 建立SqlTransaction交易物件tran
                SqlTransaction tran = cn.BeginTransaction();
                try
                {
                    // 使用者帳號扣款的SQL語法
                    // 查詢字串
                    sqlstr = "UPDATE 銀行帳戶 SET 餘額=餘額-" + money + " WHERE 帳號='" + src_ID + "'";
                    SqlCommand cmd3 = new SqlCommand(sqlstr, cn, tran);

                    // 設定轉入帳號匯款的SQL語法
                    // 查詢字串
                    sqlstr = "UPDATE 銀行帳戶 SET 餘額=餘額+" + money + " WHERE 帳號='" + dst_ID + "'";
                    SqlCommand cmd4 = new SqlCommand(sqlstr, cn, tran);

                    cmd3.ExecuteNonQuery();  // 執行SQL命令

                    cmd4.ExecuteNonQuery();  // 執行SQL命令

                    tran.Commit(); // 認可交易
                    richTextBox1.Text += "轉帳成功, 交易成功\n";
                }
                catch (Exception ex)
                {
                    tran.Rollback();// 回復交易
                    richTextBox1.Text += "轉帳失敗" + ex.Message + "交易失敗\n";
                }

                table_name = "銀行帳戶";
                // 查詢字串
                sqlstr = "SELECT * FROM " + table_name;

                sql_read_database(db_filename, sqlstr, dataGridView2);
                lb_dgv2.Text = "全部資料 " + table_name;
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //mmmm 3 簡單範例4個

            //多表聯合查詢
            string db_filename = "db_10_Data.MDF";
            string sqlstr = "SELECT 姓名 FROM 學生訊息表 UNION SELECT 課程名稱 FROM 課程表 WHERE 課程名稱='計算機英語' UNION SELECT convert(varchar(20),成績) FROM 學生成績表 WHERE 成績 > 90 UNION SELECT convert(varchar(20),出勤率) FROM 學生考勤表 WHERE 出勤率 > 0.8";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //用子查詢作派生的表
            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT * FROM tb_Stu";
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "全部資料 tb_Stu";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //顯示學生編號排在前10位，而且具有相同名字的學生個數
            sqlstr = "SELECT 學生姓名, COUNT(*) AS 相同數量 FROM (SELECT top 10 學生姓名 FROM tb_Stu order BY 學生編號 ASC )AS T GROUP BY 學生姓名";
            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "";

            richTextBox1.Text += "------------------------------\n";  // 30個

            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT * FROM 工資數據表, 部門表";
            sql_read_database(db_filename, sqlstr, dataGridView4);
            lb_dgv4.Text = "全部資料 工資數據表, 部門表";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //複雜內嵌查詢
            //查詢學歷是本科的部門經理的2005年10月份的工資情況
            sqlstr = "SELECT * FROM 工資數據表 WHERE 工資月份=10 AND 人員姓名 IN( SELECT 負責人 FROM 部門表 WHERE 負責人 IN(SELECT 人員姓名 FROM 人員表 WHERE 學歷='本科')) ORDER BY 人員編號";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //mmmm 4 簡單範例4個

            string db_filename = "db_10_Data.MDF";
            string sqlstr = "SELECT * FROM tb_stu, tb_mark";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tb_stu, tb_mark";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用表別名
            //利用表的別名查詢計算機分院學生的成績
            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT distinct S.學生編號,S.學生姓名,M.高數,M.外語,M.馬經,S.所在學院 FROM tb_stu AS S,tb_mark AS M WHERE S.學生編號=M.學生編號 AND S.所在學院='計算機學院'";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用FROM子句進行多表查詢

            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT * FROM tb_stu s ,tb_mark";
            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv1.Text = "全部資料 多表查詢";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用FROM子句進行多表查詢
            //查詢高數成績大於85分的學生的詳細訊息
            db_filename = "db_10_Data.MDF";
            sqlstr = "SELECT distinct s.學生編號,s.學生姓名,s.性別,s.出生年月,s.年齡,s.所在學院,s.所學專業,m.高數 FROM tb_stu s ,tb_mark m WHERE s.學生編號=m.學生編號 AND m.高數 >85";
            sql_read_database(db_filename, sqlstr, dataGridView4);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //mmmm 6 簡單範例4個

            //在分組查詢中使用ALL關鍵字

            string db_filename = "db_10_Data.MDF";
            string sqlstr = "SELECT * FROM tb_BookSell";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tb_BookSell";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //在分組查詢中使用ALL關鍵字
            //在圖書銷售表中對機械出版社出版的不同圖書的銷售情況進行統計，並列出其他出版社的圖書（不作統計）
            sqlstr = "SELECT 書名,出版社,SUM(金額) AS 總計金額 FROM tb_BookSell WHERE 出版社='機械' GROUP BY all 書名,出版社 ";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢字串/數字

            //查詢字串
            //請輸入查詢院系名稱：
            //計算機

            db_filename = "db_10_Data.MDF";
            string search_college = "計算機";
            sqlstr = "SELECT * FROM tb_05 WHERE 所在院系 LIKE '%" + search_college + "%'";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tb_05 + WHERE";

            richTextBox1.Text += "------------------------------\n";  // 30個

            /*
            //查詢數字
            //查詢年齡為：23

            string db_filename = "db_10_Data.MDF";
            int age = 23;
            string sqlstr = "SELECT * FROM tb_05 WHERE 學生年齡=" + age.ToString();
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tb_05 + WHERE";
            */

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
            string 書號 = "IMS0311";
            string 書名 = "膠囊內視鏡";
            int 單價 = 12345;
            int 數量 = 20;

            InsertBook(書號, 書名, 單價, 數量);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 查詢字串, 讀取全部資料庫
            sqlstr = "SELECT * FROM 書籍";
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "全部資料 書籍\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //更新
            書號 = "IMS0311";//以書號為準
            書名 = "ims EGD";
            單價 = 123;
            數量 = 18;

            UpdateBook(書號, 書名, 單價, 數量);

            // 查詢字串, 讀取全部資料庫
            sqlstr = "SELECT * FROM 書籍";
            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "全部資料 書籍\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //刪除
            書號 = "IMS0311";//以書號為準

            DeleteBook(書號);

            // 查詢字串, 讀取全部資料庫
            sqlstr = "SELECT * FROM 書籍";
            sql_read_database(db_filename, sqlstr, dataGridView4);
            lb_dgv4.Text = "全部資料 書籍\n";
        }

        public void InsertBook(string 書號, string 書名, int 單價, int 數量)
        {
            // 查詢字串
            string sqlstr = "INSERT INTO 書籍(書號, 書名, 單價, 數量)" + "VALUES(@BookId, @BookName, @Price, @Qty)";

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
        }

        public void UpdateBook(string 書號, string 書名, int 單價, int 數量)
        {
            // 查詢字串
            string sqlstr = "UPDATE 書籍 SET 書名=@BookName," + "單價=@Price, 數量=@Qty WHERE 書號=@BookId";

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
        }

        public void DeleteBook(string 書號)
        {
            // 查詢字串
            string sqlstr = "DELETE FROM 書籍 WHERE 書號 = @BookId";

            using (SqlConnection cn = new SqlConnection(cnstr23))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr23;  // 連接字串
                cn.Open();  // 打開資料庫連線

                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                cmd.Parameters.Add(new SqlParameter("@BookId", SqlDbType.NVarChar));
                cmd.Parameters["@BookId"].Value = 書號;
                cmd.ExecuteNonQuery();  // 執行SQL命令
            }
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

            int query_year = 2006;

            /*
            db_filename = "db_TomeOne.mdf";
            sqlstr = "SELECT * FROM tb_manpower";  // 有兩欄資料 t_Point t_Num
            sql_read_database(db_filename, sqlstr, dataGridView1);

            db_filename = "db_TomeOne.mdf";
            sqlstr = "SELECT SUM(t_Num) FROM tb_manpower"; // 將 t_Num 加總
            sql_read_database(db_filename, sqlstr, dataGridView2);

            db_filename = "db_TomeOne.mdf";
            //合併 t_Point 資料, 降冪排序, 將 t_Num 加總
            sqlstr = "SELECT t_Point, SUM(t_Num) FROM tb_manpower group by t_Point ORDER BY SUM(t_Num) DESC";
            sql_read_database(db_filename, sqlstr, dataGridView3);


            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeOne.mdf;Integrated Security=True;Connect Timeout=30";
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                // 查詢字串
                sqlstr = "SELECT t_Point,SUM(t_Num) FROM tb_manpower group by t_Point ORDER BY SUM(t_Num) DESC";
                using (SqlCommand cmd = new SqlCommand(sqlstr, cn))
                {
                    cmd.Connection.Open();
                    SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
                    while (dr.Read())  // 讀取一筆資料到dr
                    {
                        float f = Convert.ToSingle(dr[1]) / Sum;
                        richTextBox1.Text += dr[0] + "\t" + dr[1] + "\t占比 : " + f.ToString() + "\n";
                    }
                    dr.Close();
                    cn.Close();
                }
            }
            */
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            /*
            // 資料庫檔案
            db_filename = "db_TomeTwo.mdf";
            // tb_Student 的 所有資料
            sqlstr = string.Format("SELECT * FROM tb_Student");
            sql_read_database(db_filename, sqlstr, dataGridView1);

            // tb_Grade 的 所有資料
            sqlstr = string.Format("SELECT * FROM tb_Grade");
            sql_read_database(db_filename, sqlstr, dataGridView2);

            //使用IN引入子查询限定查询范围
            //查詢學生總分在 500 ~ 600 之間
            string Begin = "550";
            string end = "570";
            // 查 tb_Student 的 資料, 由 tb_Grade 總分在 500 ~ 600 之間
            sqlstr = string.Format(@"SELECT 学生姓名,性别,年龄 FROM tb_Student WHERE 学生编号 IN (SELECT 学生编号 FROM tb_Grade WHERE 总分>{0} AND 总分<{1})", Begin, end);
            sql_read_database(db_filename, sqlstr, dataGridView3);
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            /*
            // 查詢字串
            //SELECT ShowYear FROM tb_Stat
            sqlstr = "SELECT * FROM tb_Stat";
            // 資料庫檔案
            db_filename = "db_TomeOne.mdf";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tb_Stat\n";

            query_year = 2006;  // 有資料的年份 2001~2007
            int sum_year = SumYear(query_year);
            richTextBox1.Text += "年度總和 : " + sum_year.ToString() + "\n";

            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeOne.mdf;Integrated Security=True;Connect Timeout=30";

            // 查詢字串
            sqlstr = "SELECT * FROM tb_Stat WHERE ShowYear=" + query_year + "";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();
                SqlCommand Com = new SqlCommand(sqlstr, cn);
                SqlDataAdapter da = new SqlDataAdapter();
                da.SelectCommand = Com;
                DataSet ds = new DataSet();
                da.Fill(ds);

                for (int j = 0; j < 12; j++)
                {
                    richTextBox1.Text += ds.Tables[0].Rows[0][j + 1].ToString() + "\n";
                }
            }
            */
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            /*
            //debug
            // 資料庫檔案
            db_filename = "db_13.mdf";
            sqlstr = "SELECT * FROM tb_Stat";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tb_Stat\n";

            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";

            // 查詢字串
            sqlstr = "SELECT ShowYear FROM tb_Stat";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                DataTable dt = new DataTable();
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataAdapter da = new SqlDataAdapter();
                da.SelectCommand = cmd;
                da.Fill(dt);

                int C = dt.Columns.Count;
                int R = dt.Rows.Count;
                richTextBox1.Text += "R = " + R.ToString() + "\n";
                richTextBox1.Text += "C = " + C.ToString() + "\n";
                for (int i = 0; i < R; i++)
                {
                    richTextBox1.Text += dt.Rows[i][0].ToString() + "\n";
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //上面有查到, 有資料的年份是 2001~2007
            query_year = 2001;
            // 查詢字串
            sqlstr = "SELECT * FROM tb_Stat WHERE ShowYear=" + query_year + "";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();
                SqlCommand Com = new SqlCommand(sqlstr, cn);
                SqlDataAdapter da = new SqlDataAdapter();
                da.SelectCommand = Com;
                DataSet ds = new DataSet();
                da.Fill(ds);
                for (int j = 0; j < 12; j++)
                {
                    richTextBox1.Text += ds.Tables[0].Rows[0][j + 1].ToString() + "\n";
                }
            }
            */
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            // 資料庫檔案
            db_filename = "db_TomeOne.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM tb_product";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tb_product 兩欄 t_Name t_Num\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 資料庫檔案
            db_filename = "db_TomeOne.mdf";
            sqlstr = "SELECT SUM(t_Num) FROM tb_product";
            //將 t_Num 加總起來
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------\n";  // 30個
            
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeOne.mdf;Integrated Security=True;Connect Timeout=30";

            // 資料庫檔案
            db_filename = "db_TomeOne.mdf";
            //t_Name
            sqlstr = "SELECT t_Name, SUM(t_Num) AS Num FROM tb_product GROUP BY t_Name";
            sql_read_database(db_filename, sqlstr, dataGridView3);
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //SQL 1

            // 資料庫檔案
            db_filename = "db_TomeTwo.mdf";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM EmployeeInfo";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 EmployeeInfo\n";

            //SQL1
            //从头开始提取满足指定条件的记录

            sqlstr = "SELECT * FROM EmployeeInfo";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataAdapter da = new SqlDataAdapter(cmd);  // 建立資料庫適配器對象da
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "EmployeeInfo");  // da將查詢的結果填充至數據集ds, 指定TableName為"EmployeeInfo"

                richTextBox1.Text += "------------------------------\n";  // 30個

                //从头开始提取生日小于2009-7-1之前的员工信息
                IEnumerable<DataRow> sqlstr2 = ds.Tables["EmployeeInfo"].AsEnumerable().TakeWhile(itm => itm.Field<DateTime>("Birthday") < Convert.ToDateTime("2009-7-1"));
                dataGridView2.DataSource = sqlstr2.CopyToDataTable();  // DGV設置數據源
            }

            return;
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //SQL 2

            // 資料庫檔案
            db_filename = "ch20DB.mdf";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM 員工 ORDER BY 編號 DESC";

            //LINQ 1
            //建立DataSet物件ds，ds建立於所有事件處理函式之外以便所有事件一起共用
            DataSet ds2 = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串, 可有可無

                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                da.Fill(ds2, "員工");  // da將查詢的結果填充至數據集ds, 指定TableName為"員工"
                dataGridView1.DataSource = ds2.Tables["員工"];  // DGV設置數據源
                lb_dgv1.Text = "全部資料 員工 DESC\n";
            }

            int money = 25000;
            richTextBox1.Text += "搜尋 薪資 > " + money.ToString() + " 的資料\n";
            try
            {
                DataTable dtEmp = ds2.Tables["員工"];
                var emp = from p in dtEmp.AsEnumerable()
                          where p.Field<int>("薪資") >= money
                          orderby p.Field<int>("薪資") descending
                          select new
                          {
                              員工編號 = p.Field<int>("編號"),
                              員工姓名 = p.Field<string>("姓名"),
                              員工電話 = p.Field<string>("電話"),
                              員工職稱 = p.Field<string>("職稱"),
                              員工薪資 = p.Field<int>("薪資")
                          };
                dataGridView1.DataSource = emp.ToList();  // DGV設置數據源
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        private int SumYear(int Year)
        {
            // 連接字串
            //string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeOne.mdf;Integrated Security=True;Connect Timeout=30";
            // 連接字串 same
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";

            // 查詢字串
            string sqlstr = "SELECT SUM(Year_M1+Year_M2+Year_M3+Year_M4+Year_M5+Year_M6+Year_M7+Year_M8+Year_M9+Year_M10+Year_M11+Year_M12) AS number FROM tb_Stat WHERE ShowYear=" + Year + "";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();
                SqlDataAdapter dap = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();
                dap.Fill(ds);
                return Convert.ToInt32(ds.Tables[0].Rows[0][0].ToString());
            }
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
                //SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da old
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

                if (ds.Tables[0].Rows.Count > 0)//判断数据集中的表中是否有行
                {
                    richTextBox1.Text += "用户登录成功！\n";
                }
                else
                {
                    richTextBox1.Text += "用户登录失败，原因为：用户名或密码错误！\n";
                }
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //复杂的模糊查询

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 查詢字串
            string sqlstr = "SELECT 学生姓名,年龄,性别,家庭住址 FROM tb_Student";

            SqlDataAdapter da = new SqlDataAdapter(sqlstr, cnstr);  // 建立資料庫適配器對象da
            DataTable dt = new DataTable();//创建数据表
            da.Fill(dt);//填充数据表
            dataGridView1.DataSource = dt;//设置数据源

            richTextBox1.Text += "------------------------------\n";  // 30個

            //复杂的模糊查询

            richTextBox1.Text += "複雜的模糊查詢\n";
            string Name = "李";
            int Age = 2;
            string Address = "吉林";
            richTextBox1.Text += "Name : " + Name + "\tAge : " + Age.ToString() + "\tAddress : " + Address + "\n";

            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 查詢字串
            sqlstr = string.Format(@"SELECT 学生姓名,年龄,性别,家庭住址 FROM tb_Student WHERE 学生姓名 LIKE '{0}%' and 年龄 LIKE '{1}%' and 家庭住址 LIKE '{2}%'", Name, Age, Address);
            da = new SqlDataAdapter(sqlstr, cnstr);  // 建立資料庫適配器對象da
            dt = new DataTable();//创建数据表
            da.Fill(dt);//填充数据表

            dataGridView2.DataSource = dt;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //使用交叉表实现商品销售统计

            richTextBox1.Text += "按指定的条件使用交叉表查询数据\n";

            //表头字段
            string header_name = "订单号";

            //分组字段
            string product_name = "商品名";

            //或者交換
            //header_name = "商品名";
            //product_name = "订单号";

            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data2.mdf;Integrated Security=True;Connect Timeout=30";
            SqlConnection cn = new SqlConnection(cnstr);  // 建立資料庫連接對象cn

            // 查詢字串
            string sqlstr = "proc_across_table";
            SqlCommand cmd = new SqlCommand(sqlstr, cn);
            cmd.CommandType = CommandType.StoredProcedure;
            cmd.Parameters.Add("@TableName", SqlDbType.VarChar, 50).Value = "商品销售表";

            cmd.Parameters.Add("@NewColumn", SqlDbType.VarChar, 50).Value = header_name;  // 表頭字段
            cmd.Parameters.Add("@GroupColumn", SqlDbType.VarChar, 50).Value = product_name;  // 分組字段
            cmd.Parameters.Add("@StatColumn", SqlDbType.VarChar, 50).Value = "订货数量";
            cmd.Parameters.Add("@Operator", SqlDbType.VarChar, 10).Value = "SUM";
            SqlDataAdapter myda = new SqlDataAdapter();
            myda.SelectCommand = cmd;
            DataSet myds = new DataSet();
            myda.Fill(myds);
            dataGridView1.DataSource = myds.Tables[0];
            dataGridView1.Columns[1].Width = 120;
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
            // 有條件刪除資料

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\animals1_db.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();
                string sqlstr = "DELETE FROM animals1_table WHERE 體重 > 20";  // 刪除所有資料
                using (SqlCommand cmd = new SqlCommand(sqlstr, cn))
                {
                    int rowsAffected = cmd.ExecuteNonQuery();  // 執行SQL命令
                    richTextBox1.Text += "已刪除 : " + rowsAffected + " 筆資料\n";
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //清空一個資料庫表單 TRUNCATE TABLE

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();
                string sqlstr = "TRUNCATE TABLE animals1_table";  // 清空整個表格
                using (SqlCommand cmd = new SqlCommand(sqlstr, cn))
                {
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                    richTextBox1.Text += "已清空整個表單\n";
                }
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
            // 十二生肖整理

            // 資料庫檔案
            string db_filename = "animals1_db.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM animals1_table";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "十二生肖全部資料";
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
            /*
            //某一欄資料處理 COUNT SUM AVG MAX MIN, 使用 ExecuteScalar()
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串, 可有可無
                cn.Open();  // 打開資料庫連線

                // 查詢字串 資料筆數 COUNT
                sqlstr = "SELECT COUNT(*) FROM animals1_table";
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                richTextBox1.Text += "共 " + cmd.ExecuteScalar().ToString() + " 筆記錄\n";

                // 查詢字串 取總和 SUM()
                sqlstr = "SELECT SUM(體重) FROM animals1_table";
                cmd = new SqlCommand(sqlstr, cn);
                richTextBox1.Text += "總和 :\t" + cmd.ExecuteScalar().ToString() + "\n";
                int SumNum = Convert.ToInt32(cmd.ExecuteScalar());
                richTextBox1.Text += "總和 :\t" + SumNum.ToString() + "\n";

                // 查詢字串 取平均 AVG()
                sqlstr = "SELECT AVG(體重) FROM animals1_table";
                cmd = new SqlCommand(sqlstr, cn);
                richTextBox1.Text += "平均 :\t" + cmd.ExecuteScalar().ToString() + "\n";

                // 查詢字串 取最大 MAX()
                sqlstr = "SELECT MAX(體重) FROM animals1_table";
                cmd = new SqlCommand(sqlstr, cn);
                richTextBox1.Text += "最大 :\t" + cmd.ExecuteScalar().ToString() + "\n";

                // 查詢字串 取最小 MIN()
                sqlstr = "SELECT MIN(體重) FROM animals1_table";
                cmd = new SqlCommand(sqlstr, cn);
                richTextBox1.Text += "最小 :\t" + cmd.ExecuteScalar().ToString() + "\n";
            }
            */

            //as
            //t_Name
            //sqlstr = "SELECT t_Name, SUM(t_Num) AS Num FROM tb_product GROUP BY t_Name";

            // 更新資料 UPDATE

            // 查詢字串 更新資料
            string new_name = "巧虎";
            sqlstr = "UPDATE animals1_table SET 中文名=N'" + new_name + "' WHERE 編號=3";
            sql_write_database(db_filename, sqlstr);

            // 查詢字串 更新資料 多項
            string id = "11";
            string cname = "丹尼狗";
            string ename = "Danny Dog";
            int weight = 25;
            sqlstr = "UPDATE animals1_table SET 中文名=N'" + cname + "', 英文名=N'" + ename + "', 體重=" + weight + " WHERE 編號=N'" + id + "'";
            sql_write_database(db_filename, sqlstr);

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
            sql_write_database(db_filename, sqlstr);

            // 查詢字串
            sqlstr = "SELECT * FROM animals1_table";
            sql_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "十二生肖全部資料 更新資料後";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //刪除
            id = "13";
            // 查詢字串
            sqlstr = "DELETE FROM animals1_table WHERE 編號=N'" + id + "'";
            sql_write_database(db_filename, sqlstr);

            // 查詢字串
            sqlstr = "SELECT * FROM animals1_table";
            sql_read_database(db_filename, sqlstr, dataGridView4);
            lb_dgv4.Text = "十二生肖全部資料 更新資料後";


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
            sql_write_database(db_filename, sqlstr);


            richTextBox1.Text += "修改, 修改 類別編號4 的 產品類別\n";
            int old_id = 4;
            string new_item2 = "肯德雞";
            //傳入UPDATE陳述式修改產品類別記錄
            //取得DataGridView目前選取第一欄的資料，也就是類別編號欄位
            sqlstr = "UPDATE 產品類別 SET 類別名稱=N'" + new_item2 + "' WHERE 類別編號=" + old_id.ToString();
            sql_write_database(db_filename, sqlstr);
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
            sql_write_database(db_filename, sqlstr);

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
            sql_write_database(db_filename, sqlstr);

            int CategoryId2 = 1;//類別編號
            richTextBox1.Text += "CategoryId2 = " + CategoryId2.ToString() + "\n";

            // 查詢字串, 只看一些欄位, 加上條件
            sqlstr = "SELECT 產品編號,品名,單價,說明 FROM 產品資料 WHERE 類別編號=" + CategoryId2;
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "修改 產品資料";
            */
        }

        /*      id  ename   cname   weight
                idx	英文名	中文名	體重
        第 1筆 :  1	mouse	米老鼠	3
        第 2筆 :  2	ox	    班尼牛	48
        第 3筆 :  3	tiger	跳跳虎	33
        第 4筆 :  4	rabbit	彼得兔	8
        第 5筆 :  5	dragon	逗逗龍	38
        第 6筆 :  6	snake	貪吃蛇	16
        第 7筆 :  7	horse	草泥馬	31
        第 8筆 :  8	goat	喜羊羊	29
        第 9筆 :  9	monkey	山道猴	22
        第10筆 : 10	chicken	肯德雞	5
        第11筆 : 11	dog	    布丁狗	17
        第12筆 : 12	pig	    佩佩豬	42
        */

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
            sql_write_database(db_filename, sqlstr);
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (2, N'ox', N'班尼牛', 48)";
            sql_write_database(db_filename, sqlstr);
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (3, N'tiger', N'跳跳虎', 33)";
            sql_write_database(db_filename, sqlstr);
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (4, N'rabbit', N'彼得兔', 8)";
            sql_write_database(db_filename, sqlstr);
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (5, N'dragon', N'逗逗龍', 38)";
            sql_write_database(db_filename, sqlstr);
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (6, N'snake', N'貪吃蛇', 16)";
            sql_write_database(db_filename, sqlstr);
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (7, N'horse', N'草泥馬', 31)";
            sql_write_database(db_filename, sqlstr);
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (8, N'goat', N'喜羊羊', 29)";
            sql_write_database(db_filename, sqlstr);
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (9, N'monkey', N'山道猴', 22)";
            sql_write_database(db_filename, sqlstr);
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (10, N'chicken', N'肯德雞', 5)";
            sql_write_database(db_filename, sqlstr);
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (11, N'dog', N'布丁狗', 17)";
            sql_write_database(db_filename, sqlstr);
            sqlstr = "INSERT INTO animals1_table (編號, 英文名, 中文名, 體重) VALUES (12, N'dogpig', N'佩佩豬', 42)";
            sql_write_database(db_filename, sqlstr);

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "查詢資料\n";

            string selectData = "SELECT 編號, 英文名, 中文名, 體重 FROM animals1_table";
            sql_read_database(db_filename, selectData, dataGridView1);
            lb_dgv1.Text = "新增5筆資料";

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "更新資料\n";

            string updateData = "UPDATE animals1_table SET 體重 = 25 WHERE 編號 = 2";
            sql_write_database(db_filename, updateData);

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "再次查詢確認更新\n";
            string selectUpdated = "SELECT 編號, 英文名, 中文名, 體重 FROM animals1_table";
            sql_read_database(db_filename, selectUpdated, dataGridView2);
            lb_dgv2.Text = "更新後資料 編號=2, 體重=25";

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "刪除資料\n";
            string deleteData = "DELETE FROM animals1_table WHERE 編號 = 4";
            sql_write_database(db_filename, deleteData);

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "最後查詢確認刪除\n";

            string selectFinal = "SELECT 編號, 英文名, 中文名, 體重 FROM animals1_table";
            sql_read_database(db_filename, selectFinal, dataGridView3);
            lb_dgv3.Text = "刪除後資料, 刪除 編號=4";

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
                //string sqlstr = "SELECT NAME FROM sysdatabases";  // 很多
                //string sqlstr = "SELECT * FROM master..sysdatabases";  // 很多 等同上

                //這個方式直接從 SQL Server 的系統目錄取出所有表格名稱

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
            //LINQ
            //使用LINQ技术统计员工的工资总额

            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection cn;//声明SqlConnection对象
            SqlDataAdapter sqlda;//声明SqlDataAdapter对象
            DataSet myds;//声明DataSet数据集对象

            cn = new SqlConnection(cnstr);  // 建立資料庫連接對象cn
            sqlda = new SqlDataAdapter("SELECT * FROM tb_Salary", cn);//创建数据库桥接器对象
            myds = new DataSet();//创建数据集对象
            sqlda.Fill(myds, "tb_Salary");//填充DataSet数据集

            var query = from salary in myds.Tables["tb_Salary"].AsEnumerable()//使用LINQ从数据集中查询所有数据
                        select salary;
            DataTable dt = query.CopyToDataTable<DataRow>();//将查询结果转化为DataTable对象

            dataGridView1.DataSource = dt;//显示查询到的数据集中的信息

            richTextBox1.Text += "------------------------------\n";  // 30個

            //公司每月总薪水

            cn = new SqlConnection(cnstr);  // 建立資料庫連接對象cn
            sqlda = new SqlDataAdapter("SELECT * FROM tb_Salary", cn);//创建数据库桥接器对象
            myds = new DataSet();//创建数据集对象
            sqlda.Fill(myds, "tb_Salary");//填充DataSet数据集

            query = from salary in myds.Tables["tb_Salary"].AsEnumerable()//查询DataSet数据集中所有薪水
                    where salary.Field<int>("Salary") > 0
                    select salary;
            int intSum = query.Sum(salary => salary.Field<int>("Salary"));//汇总薪水

            dt = new DataTable();//创建DataTable对象
            dt.Columns.Add("公司每月总薪水");//在数据表中添加列
            DataRow myDRow = dt.NewRow();//创建DataRow对象
            myDRow["公司每月总薪水"] = intSum;//为DataRow中的行赋值
            dt.Rows.Add(myDRow);//将DataRow添加到DataTable的行集合中
            //dataGridView1.DataSource = dt;//显示查询到的数据集中的信息
            //dataGridView1.Columns[0].Width = 120;//设置DataGridView控件的列宽

            richTextBox1.Text += "公司每月总薪水 : " + intSum + "\n";

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
            //跳过满足指定条件的记录
            //跳过生日小于2009-7-1的员工:

            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM EmployeeInfo";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataAdapter da = new SqlDataAdapter(cmd);  // 建立資料庫適配器對象da
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "EmployeeInfo");//填充数据集
                dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv1.Text = "全部資料 EmployeeInfo";

                //跳过生日小于2009-7-1的员工信息
                IEnumerable<DataRow> sqlstr2 = ds.Tables["EmployeeInfo"].AsEnumerable().SkipWhile(itm => itm.Field<DateTime>("Birthday") < Convert.ToDateTime("2009-7-1"));
                dataGridView2.DataSource = sqlstr2.CopyToDataTable();//设置dataGridView1数据源
                lb_dgv2.Text = "過濾資料";
            }
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
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //簡易測試

            // 資料庫檔案
            string db_filename = string.Empty;
            // 查詢字串
            string sqlstr = string.Empty;

            // 資料庫檔案
            db_filename = "Northwind.mdf";
            /* ok
            // 查詢字串
            sqlstr = "SELECT * FROM 產品類別";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 產品類別 有圖片";
            */

            /* ok
            // 資料庫檔案
            db_filename = "Northwind.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM 產品資料";
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "全部資料 產品資料";
            */

            /*
            // 資料庫檔案
            db_filename = "Database1.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM 產品類別";
            sql_read_database(db_filename, sqlstr, dataGridView3);

            // 資料庫檔案
            db_filename = "Database1.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM 產品資料";
            sql_read_database(db_filename, sqlstr, dataGridView4);
            */

            /*
            // 資料庫檔案
            db_filename = "db_TomeOne.mdf";
            //string time_st = "2005/8/15";
            //string time_sp = "2006/4/15";
            //sqlstr = "SELECT * FROM tb_lottery WHERE t_year BETWEEN '" + time_st + "' AND '" + time_sp + "' ORDER BY t_year";
            sqlstr = "SELECT * FROM tb_lottery WHERE t_year BETWEEN '2005/8/15' AND '2006/4/15' ORDER BY t_year";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "查詢使用指定時段 BETWEEN";

            //查询指定时间段的数据

            string time_st = "2005/7/1";
            string time_sp = "2005/8/31";
            // 查詢字串
            sqlstr = string.Format("SELECT * FROM tb_Book WHERE 日期 BETWEEN '{0}' AND '{1}'", time_st, time_sp);
            // 資料庫檔案
            db_filename = "db_TomeTwo.mdf";
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "查詢使用指定時段 BETWEEN";
            */

            /*
            // 資料庫檔案
            db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM tb_Book";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            //查询已销售图书情况
            // 資料庫檔案
            db_filename = "db_TomeTwo.mdf";

            // 查詢字串, 列出数据中的重复记录和记录条数
            sqlstr = string.Format(@"SELECT COUNT(书号)AS 记录条数, 书号,书名,作者 FROM tb_Book GROUP BY 书号,书名,作者 HAVING COUNT(书号)>1");
            sql_read_database(db_filename, sqlstr, dataGridView2);
            */
        }

        private void btn_sql_test_Click(object sender, EventArgs e)
        {
            //SQL 簡易測試

            dataGridView1.Size = new Size(1250, 400);
            dataGridView2.Visible = false;
            dataGridView3.Visible = false;
            dataGridView4.Visible = false;
            lb_dgv2.Visible = false;
            lb_dgv3.Visible = false;
            lb_dgv4.Visible = false;

            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            richTextBox1.Size = new Size(300, 820 - 430);
            richTextBox1.Location = new Point(x_st + dx * 7 + 110, y_st + dy * 0 + 430);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bt_previous.Location = new Point(20, 40);
            bt_next.Location = new Point(20, 40 + 100);
            lb_index.Location = new Point(20 + 20, 40 + 56);
            tb_sql.Size = new Size(700 + 30 + 60 + 30, 200);
            tb_sql.Location = new Point(110, 40);
            lb_index.Text = "";

            groupBox1.Size = new Size(900 + 40, 300);
            groupBox1.Location = new Point(640, 500);
            groupBox1.Visible = true;

            show_data_by_sqlcmd(sqlcmd_index);
        }

        void show_data_by_sqlcmd(int idx)
        {
            //richTextBox1.Text += "idx = " + idx.ToString() + "\n";
            string index = sqlcmd[idx, 0];
            string db_filename = sqlcmd[idx, 1];
            string sqlstr = sqlcmd[idx, 2];
            string description = sqlcmd[idx, 3];
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = description;

            string mesg = "編號 :\t" + index + Environment.NewLine + "資料庫檔案 :\t" + db_filename + Environment.NewLine +
                "查詢字串 :\t" + sqlstr + Environment.NewLine + "說明 :\t" + description;
            tb_sql.Text = mesg;
            lb_index.Text = index;
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
            //idx  /  資料庫檔案  /  查詢字串  /  說明
            //{ "1", "", "", ""},
            { "2", "db_09_Data.mdf", "SELECT * FROM 員工表", ""},
            { "3", "db_TomeTwo.mdf", "SELECT TOP 10 * FROM (SELECT TOP 20 * FROM tb_Grade ORDER BY 总分 DESC) AS st ORDER BY 总分 ASC", "查询第10到第20名的数据"},
            { "4", "db_TomeTwo.mdf", "SELECT * FROM tb_Book", ""},
            { "5", "db_TomeTwo.mdf", "SELECT TOP 50 PERCENT 书号,书名,SUM(销售数量)AS 合计销售数量 FROM tb_Book GROUP BY 书号,书名,作者 ORDER BY 3 DESC", "查询销售量占前50%的图书信息, 查询数据库信息"},
            //{ "6", "", "", ""},
            //{ "7", "", "", ""},
            //{ "8", "", "", ""},
            //{ "9", "", "", ""},
            //{ "10", "", "", ""},
            //{ "11", "", "", ""},
            //{ "12", "", "", ""},
            //{ "13", "xxxx.MDF", "xxxx", ""},
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

//            string sqlstr = "SELECT job_id AS 工作编号,job_desc AS 工作次序,min_lvl AS 最低水平,max_lvl AS 最高水平 FROM jobs";

/*
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT au_id AS 使用者編號,au_lname AS 姓名,phone AS 電話號碼 FROM authors";//初始化SQL查詢語句
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                DataSet ds = new DataSet();//初始化一個數據集
                da.Fill(ds, "authors");//向數據集中填充內容
                dataGridView1.DataSource = ds.Tables["authors"].DefaultView;//為DataGridView控制元件填充數據源
                for (int i = 0; i < dataGridView1.Columns.Count; i++)//循環搜尋DataGridView控制元件中的每一列
                {
                    //禁用DataGridView控制元件列表頭自動排序功能
                    dataGridView1.Columns[i].SortMode = DataGridViewColumnSortMode.NotSortable;//設定每一列的排序類型為不排序
                }
            }
*/

/*
                // DataGridView控制項資料繫結
                dataGridView1.DataSource = ds;  // DGV設置數據源
                dataGridView1.DataMember = "員工";                
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

            //刪除

                /* same
                  // 查詢字串
                string sqlstr = "DELETE FROM 員工 WHERE 姓名 = '" + name + "'";
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                cmd.ExecuteNonQuery();  // 執行SQL命令
                */
/*
                // 查詢字串
                sqlstr = "DELETE FROM 員工 WHERE 姓名 = @name";
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                cmd.Parameters["@name"].Value = name;
                cmd.ExecuteNonQuery();  // 執行SQL命令
*/

