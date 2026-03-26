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

namespace vcs_SqlConnection1
{
    public partial class Form1 : Form
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

        //建立MyDBClass類別物件db，來管理Database1.mdf資料庫
        MyDBClass db = new MyDBClass();

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
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

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
            dataGridView1.Size = new Size(500, 380);
            dataGridView2.Size = new Size(500, 380);
            dataGridView3.Size = new Size(300, 380);
            dataGridView4.Size = new Size(300, 380);

            lb_dgv1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd);
            lb_dgv2.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            dataGridView2.Location = new Point(x_st + dx * 3, y_st + dy * 6 + dd);
            lb_dgv3.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0);
            dataGridView3.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0 + dd);
            lb_dgv4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6);
            dataGridView4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6 + dd);
            lb_dgv1.Text = "dataGridView1";
            lb_dgv2.Text = "dataGridView2";
            lb_dgv3.Text = "dataGridView3";
            lb_dgv4.Text = "dataGridView4";

            richTextBox1.Size = new Size(400, 820);
            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1910, 890);
            this.Text = "vcs_SqlConnection1";

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
            //讀取資料庫 至 DGV, 要先知道資料庫檔案(.mdf)和表單名稱(tb_Employee)

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Employee";

            //讀取資料庫至DGV
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                //da.Fill(ds, "員工");  // da將查詢的結果填充至數據集ds, 指定TableName為"員工"
                dataGridView1.DataSource = ds.Tables[0].DefaultView;  // DGV設置數據源
                dataGridView2.DataSource = ds.Tables[0];  // DGV設置數據源, same
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

            // 查詢字串
            sqlstr = string.Format("SELECT * FROM tb_Grade");

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataTable dt = new DataTable();  // 建立DT
                da.Fill(dt);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView3.DataSource = dt;  // DGV設置數據源

                richTextBox1.Text += "------------------------------\n";  // 30個

                // 查詢字串
                sqlstr = string.Format(@"SELECT TOP 10 * FROM (SELECT TOP 20 * FROM tb_Grade ORDER BY 总分 DESC) AS st ORDER BY 总分 ASC");

                da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                dt = new DataTable();  // 建立DT
                da.Fill(dt);  // da將查詢的結果填充至數據集ds, 不指定TableName
                //查询第10到第20名的数据
                dataGridView4.DataSource = dt;  // DGV設置數據源
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //員工資料
            string db_filename = "ch18DB.mdf";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM 員工";

            //讀取資料庫至DGV
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;

                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "員工");  // da將查詢的結果填充至數據集ds, 指定TableName為"員工"

                // DataGridView控制項資料繫結
                dataGridView1.DataSource = ds;  // DGV設置數據源
                dataGridView1.DataMember = "員工";
                lb_dgv1.Text = "員工資料";

                richTextBox1.Text += "------------------------------\n";  // 30個

                // 查詢字串
                sqlstr = "SELECT * FROM 員工 ORDER BY 薪資 DESC";
                da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "員工");  // da將查詢的結果填充至數據集ds, 指定TableName為"員工"

                // DataGridView控制項資料繫結
                dataGridView2.DataSource = ds;  // DGV設置數據源
                dataGridView2.DataMember = "員工";
                lb_dgv2.Text = "員工資料 排序 薪資 降冪";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 查询销售量占前50%的图书信息
            // 查询数据库信息

            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 查詢字串
            sqlstr = string.Format("SELECT * FROM tb_Book");

            //讀取資料庫至DGV
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                DataTable dt = new DataTable();  // 建立DT
                da.Fill(dt);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = dt;//设置数据源

                richTextBox1.Text += "------------------------------\n";  // 30個

                // 查询销售量占前50%的图书信息
                // 查询数据库信息

                // 查詢字串
                sqlstr = string.Format(@"SELECT TOP 50 PERCENT 书号,书名,sum(销售数量)as 合计销售数量 FROM tb_Book group by 书号,书名,作者 order by 3 desc");

                da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                dt = new DataTable();  // 建立DT
                da.Fill(dt);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = dt;//设置数据源
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取資料庫 解讀, 要先知道資料庫檔案(.mdf)和表單名稱(tb_Employee)

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Employee";

            //讀取資料庫
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串

                cn.Open();  // 打開資料庫連線
                // 查詢字串
                sqlstr = "SELECT * FROM tb_Employee";
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataReader dr = cmd.ExecuteReader();
                richTextBox1.Text += "欄數 dr.FieldCount = " + dr.FieldCount.ToString() + "\n";
                richTextBox1.Text += "欄位名稱\n";
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    richTextBox1.Text += dr.GetName(i) + "\t";
                }
                richTextBox1.Text += "\n內容\n";
                while (dr.Read())
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
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            // 查詢字串
            sqlstr = "SELECT * FROM tb_student";
            //sqlstr = "SELECT * FROM tb_Land";
            //sqlstr = "SELECT * FROM tb_06";

            //讀取資料庫
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();  // 打開資料庫連線
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataReader dr = cmd.ExecuteReader();
                while (dr.Read())
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

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 查詢字串
            //sqlstr = "SELECT * FROM tb_02";
            sqlstr = "SELECT * FROM tb_07";

            //讀取資料庫
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();  // 打開資料庫連線
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataReader dr = cmd.ExecuteReader();
                while (dr.Read())
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

            richTextBox1.Text += "------------------------------\n";  // 30個

            //讀取資料庫6
            //取得資料
            // 查詢字串
            string sqlstr2 = "SELECT * FROM tb_05";
            getScoure(sqlstr2);
            /*
            //升冪排列 查詢字串
            string sqlstr3 = "SELECT * FROM tb_05  order by 銷售數量 asc";
            getScoure(sqlstr3);

            //降冪排列 查詢字串
            string sqlstr4 = "SELECT * FROM tb_05 order by 銷售數量 desc";
            getScoure(sqlstr4);
            */
        }

        public void getScoure(string sqlstr)
        {
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();  // 打開資料庫連線
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataReader dr = cmd.ExecuteReader();
                while (dr.Read())
                {
                    /* 印出全部資料
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
                    */
                    richTextBox1.Text += dr[0].ToString() + "\t" + dr[1].ToString() + "\t" + dr[2].ToString() + "\n";
                }
                dr.Close();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string db_filename = "Northwind.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串

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

                //cn.ConnectionString = cnstr;  // 連接字串

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
            // 成績單
            string db_filename = "ch17DB.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串

                cn.Open();  // 打開資料庫連線
                // 查詢字串
                string sqlstr = "SELECT * FROM 成績單";
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataReader dr = cmd.ExecuteReader();
                richTextBox1.Text += "欄數 dr.FieldCount = " + dr.FieldCount.ToString() + "\n";
                richTextBox1.Text += "欄位名稱\n";
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    richTextBox1.Text += dr.GetName(i) + "\t";
                }

                richTextBox1.Text += "\n內容\n";
                int cnt = 0;
                while (dr.Read())
                {
                    richTextBox1.Text += "第 " + cnt.ToString() + " 筆資料 :\n";
                    cnt++;
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        richTextBox1.Text += dr[i].ToString() + "\t";
                        //richTextBox1.Text += dr.GetValue(i).ToString() + "\t";    //same
                    }
                    richTextBox1.Text += "\n";
                    /*
                    richTextBox1.Text += dr["學號"].ToString() + "\t";
                    richTextBox1.Text += dr["姓名"].ToString() + "\t";
                    richTextBox1.Text += dr["國文"].ToString() + "\t";
                    richTextBox1.Text += dr["英文"].ToString() + "\t";
                    richTextBox1.Text += dr["數學"].ToString() + "\t";
                    richTextBox1.Text += "\n";
                    */
                    /*
                    richTextBox1.Text += dr.GetString(0) + "\t";   //讀取學號
                    richTextBox1.Text += dr.GetString(1) + "\t";   //讀取姓名
                    richTextBox1.Text += dr.GetInt32(2).ToString() + "\t";   //讀取國文
                    richTextBox1.Text += dr.GetInt32(3).ToString() + "\t";   //讀取英文
                    richTextBox1.Text += dr.GetInt32(4).ToString() + "\t";   //讀取數學
                    richTextBox1.Text += "\n";
                    */

                    /*
                    richTextBox1.Text += dr.GetSqlString(0).ToString() + "\t";//讀取學號
                    richTextBox1.Text += dr.GetSqlString(1).ToString() + "\t";//讀取姓名
                    richTextBox1.Text += dr.GetSqlInt32(2).ToString() + "\t";//讀取國文
                    richTextBox1.Text += dr.GetSqlInt32(3).ToString() + "\t";//讀取英文
                    richTextBox1.Text += dr.GetSqlInt32(4).ToString() + "\t";//讀取數學
                    richTextBox1.Text += "\n";
                    */
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //成績單
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)

                // 建立SqlDataAdapter物件da並取出成績單資料表
                // 查詢字串
                string sqlstr = "SELECT * FROM 成績單";
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                // 將成績單資料表所有記錄填入ds物件
                da.Fill(ds, "成績單");  // da將查詢的結果填充至數據集ds, 指定TableName為"成績單"

                // 宣告DataTable物件dt，該dt內存放ds中的成績單DataTable
                DataTable dt = ds.Tables["成績單"];  // 建立DT
                // 在richTextBox1內顯示成績單的所有欄位名稱
                for (int i = 0; i < dt.Columns.Count; i++)
                {
                    richTextBox1.Text += dt.Columns[i].ColumnName + "\t";
                }
                richTextBox1.Text += "\n";

                // 在richTextBox1內顯示成績單的所有記錄
                for (int i = 0; i < dt.Rows.Count; i++)
                {
                    for (int j = 0; j < dt.Columns.Count; j++)
                    {
                        richTextBox1.Text += dt.Rows[i][j].ToString() + "\t";
                    }
                    richTextBox1.Text += "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //成績單
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)

                // 建立SqlDataAdapter物件da並取出成績單資料表
                // 查詢字串
                string sqlstr = "SELECT * FROM 成績單";
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                // 將成績單資料表所有記錄填入ds物件
                da.Fill(ds, "成績單");  // da將查詢的結果填充至數據集ds, 指定TableName為"成績單"

                // 宣告DataTable物件dt，該dt內存放ds中的成績單DataTable
                DataTable dt = ds.Tables["成績單"];  // 建立DT

                // 在richTextBox1內顯示成績單的所有欄位名稱
                for (int i = 0; i < dt.Columns.Count; i++)
                {
                    richTextBox1.Text += dt.Columns[i].ColumnName + "\t";
                }
                richTextBox1.Text += "\n";

                // 在richTextBox1內顯示成績單的所有記錄
                for (int i = 0; i < dt.Rows.Count - 1; i++)
                {
                    richTextBox1.Text += dt.Rows[i]["學號"].ToString() + "\t";
                    richTextBox1.Text += dt.Rows[i]["姓名"].ToString() + "\t";
                    richTextBox1.Text += dt.Rows[i]["國文"].ToString() + "\t";
                    richTextBox1.Text += dt.Rows[i]["英文"].ToString() + "\t";
                    richTextBox1.Text += dt.Rows[i]["數學"].ToString() + "\t";
                    richTextBox1.Text += "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //成績單 搜尋1

            //string db_filename = "ch17DB.mdf";
            // 連接字串
            //string cnstr = string.Format(db_cnstr, db_filename);
            string name = "阿龍";
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串

                cn.Open();  // 打開資料庫連線

                // 將輸入的姓名指定給searchName字串變數
                string searchName = name;
                // SELECT敘述的查詢條件為姓名等於searchName
                string sqlstr = "SELECT * FROM 成績單 WHERE 姓名 = '" + searchName + "'";
                // 建立SqlCommand物件cmd
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                // 傳回查詢結果的SqlDataRadedr物件dr
                SqlDataReader dr = cmd.ExecuteReader();
                if (dr.Read())   // 若有該筆記錄則執行下面敘述
                {
                    richTextBox1.Text += "學號：" + dr["學號"].ToString() + "\n";
                    richTextBox1.Text += "姓名：" + dr["姓名"].ToString() + "\n";
                    richTextBox1.Text += "國文：" + dr["國文"].ToString() + "\n";
                    richTextBox1.Text += "英文：" + dr["英文"].ToString() + "\n";
                    richTextBox1.Text += "數學：" + dr["數學"].ToString() + "\n";
                }
                else   // 若沒有該筆記錄則執行else下面敘述
                {
                    richTextBox1.Text += "找不到這個學生的成績！\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //成績單 搜尋2

            //string db_filename = "ch17DB.mdf";
            // 連接字串
            //string cnstr = string.Format(db_cnstr, db_filename);
            //string name = "阿龍";
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串

                cn.Open();  // 打開資料庫連線

                // 將輸入的姓名指定給searchName字串變數
                string searchName = name;
                // SELECT敘述的查詢條件為姓名等於searchName
                string sqlstr = "SELECT * FROM 成績單 WHERE 姓名 = '" + searchName.Replace("'", "''") + "'";
                // 建立SqlCommand物件cmd
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                // 傳回查詢結果的SqlDataRadedr物件dr
                SqlDataReader dr = cmd.ExecuteReader();
                if (dr.Read())   // 若有該筆記錄則執行下面敘述
                {
                    richTextBox1.Text += "學號：" + dr["學號"].ToString() + "\n";
                    richTextBox1.Text += "姓名：" + dr["姓名"].ToString() + "\n";
                    richTextBox1.Text += "國文：" + dr["國文"].ToString() + "\n";
                    richTextBox1.Text += "英文：" + dr["英文"].ToString() + "\n";
                    richTextBox1.Text += "數學：" + dr["數學"].ToString() + "\n";
                }
                else   // 若沒有該筆記錄則執行else下面敘述
                {
                    richTextBox1.Text += "找不到這個學生的成績！\n";
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //成績單 2

            //成績單+搜尋條件

            string db_filename = "ch18DB.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM 成績單 ORDER BY 國文 DESC";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串

                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "成績單");  // da將查詢的結果填充至數據集ds, 指定TableName為"成績單"

                DataView dv;  // 宣告DataView物件dv

                dv = ds.Tables["成績單"].DefaultView;

                dataGridView1.DataSource = dv;  // DGV設置數據源

                richTextBox1.Text += "------------------------------\n";  // 30個

                string filter = "國文>80";  // 篩選條件, 用WHRER語法
                string sort = "英文 DESC";  // 排序方法, 科目, ASC:遞增, DESC:遞減

                richTextBox1.Text += "篩選條件 : " + filter + "\n";
                richTextBox1.Text += "排序方法 : " + sort + "\n";

                dv.RowFilter = filter;
                dv.Sort = sort;

                dataGridView1.DataSource = dv;  // DGV設置數據源
            }
        }

        // 指定查詢
        void ReadMDF(string cnstr, string table_name)
        {
            // 查詢字串
            string sqlstr = "SELECT * FROM " + table_name;

            // DB => DS => dataGridView1
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;

                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, table_name);  // da將查詢的結果填充至數據集ds, 指定TableName為 table_name
                dataGridView1.DataSource = ds.Tables[table_name];  // DGV設置數據源
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            // 轉帳

            string db_filename = "ch17DB.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            string table_name = "銀行帳戶";
            ReadMDF(cnstr, table_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                string src_ID = "A003";
                string dst_ID = "A004";
                int money = 500;

                //cn.ConnectionString = cnstr;
                cn.Open();  // 打開資料庫連線

                // 建立SqlCommand物件cmd1，用來查詢使用者帳號是否存在
                // 查詢字串
                string sqlstr = "SELECT * FROM 銀行帳戶 WHERE 帳號='" + src_ID + "'";
                SqlCommand cmd1 = new SqlCommand(sqlstr, cn);

                // 建立SqlCommand物件cmd1，用來查詢轉入帳號是否存在
                // 查詢字串
                sqlstr = "SELECT * FROM 銀行帳戶 WHERE 帳號='" + dst_ID + "'";
                SqlCommand cmd2 = new SqlCommand(sqlstr, cn);

                // 傳回SqlDataReader物件dr1，用來查詢使用者帳號是否存在
                SqlDataReader dr1 = cmd1.ExecuteReader();
                if (!dr1.Read())   // 使用者帳號不存在執行下列敘述
                {
                    richTextBox1.Text += "你的帳號" + src_ID + "錯誤\n";
                    return;
                }

                // 取得使用者的餘額並定給myMoney
                int myMoney = int.Parse(dr1["餘額"].ToString());
                dr1.Close();  // 關閉SqlDataRader物件dr1

                // 傳回SqlDataReader物件dr2，用來查詢轉入帳號是否存在
                SqlDataReader dr2 = cmd2.ExecuteReader();
                if (!dr2.Read())   // 轉入帳號不存在執行下列敘述
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

                    //throw new Exception("電腦當機");

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
                ReadMDF(cnstr, table_name);
            }
        }

        // 員工資料表1 ST

        private void ShowData1(string cnstr)
        {
            // DB => DS => dataGridView1

            // 查詢字串
            string sqlstr = "SELECT * FROM 員工 ORDER BY 編號 DESC";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;

                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "員工");  // da將查詢的結果填充至數據集ds, 指定TableName為"員工"
                dataGridView1.DataSource = ds.Tables["員工"];  // DGV設置數據源
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //員工資料表1    讀取 新增 修改 刪除

            string db_filename = "ch17DB.mdf";
            // 連接字串
            string cnstr1 = string.Format(db_cnstr, db_filename);

            ShowData1(cnstr1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增

            string name = "david";
            string position = "engineering";
            string telephone = "0912345678";
            int salary = 55555;

            try  //使用try...catch...敘述來補捉異動資料可能發生的例外 
            {
                using (SqlConnection cn = new SqlConnection(cnstr1))  // 建立資料庫連接對象cn
                {
                    //cn.ConnectionString = cnstr1;
                    cn.Open();  // 打開資料庫連線

                    /* same
                    // 查詢字串
                    string sqlstr = "INSERT INTO 員工(姓名, 職稱, 電話, 薪資) VALUES('" + name + "','" + position + "','" + telephone + "'," + salary + ")";
                    SqlCommand cmd = new SqlCommand(sqlstr, cn);
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                    */

                    // 查詢字串
                    string sqlstr = "INSERT INTO 員工(姓名, 職稱, 電話, 薪資)" + "VALUES(@name, @position, @tel, @salary)";
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
                }
                ShowData1(cnstr1);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + ", 新增資料發生錯誤\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //修改

            string position2 = "manager";
            string telephone2 = "0987654321";
            int salary2 = 66666;

            try	//使用try...catch...敘述來補捉異動資料可能發生的例外
            {
                using (SqlConnection cn = new SqlConnection(cnstr1))  // 建立資料庫連接對象cn
                {
                    //cn.ConnectionString = cnstr1;
                    cn.Open();  // 打開資料庫連線

                    /* same
                    // 查詢字串
                    string sqlstr = "UPDATE 員工 SET 職稱 = '" + position2 + "',電話 = '" + telephone2 + "', 薪資 = " + salary2 + " WHERE 姓名 = '" + name + "'";
                    SqlCommand cmd = new SqlCommand(sqlstr, cn);
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                    */
                    // 查詢字串
                    string sqlstr = "UPDATE 員工 SET 職稱=@position," + "電話=@tel, 薪資=@salary WHERE 姓名=@name";
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
                }
                ShowData1(cnstr1);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + ", 修改資料發生錯誤\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //刪除

            using (SqlConnection cn = new SqlConnection(cnstr1))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr1;
                cn.Open();  // 打開資料庫連線

                /* same
                  // 查詢字串
                string sqlstr = "DELETE FROM 員工 WHERE 姓名 = '" + name + "'";
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                cmd.ExecuteNonQuery();  // 執行SQL命令
                */
                // 查詢字串
                string sqlstr = "DELETE FROM 員工 WHERE 姓名 = @name";
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                cmd.Parameters["@name"].Value = name;
                cmd.ExecuteNonQuery();  // 執行SQL命令
            }
            ShowData1(cnstr1);
        }
        // 員工資料表1 SP

        private void button8_Click(object sender, EventArgs e)
        {
            //員工資料MyDB

            string db_filename = "MyDB0.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增

            string id = "A008";
            string name = "david";
            string sex = "男";
            int money = 12345;

            try
            {
                using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
                {
                    cn.Open();  // 打開資料庫連線
                    SqlCommand cmd = new SqlCommand();
                    // 查詢字串
                    //string sqlstr = "xxxxxxxxxxx";
                    cmd.CommandText = "INSERT INTO 員工(員工編號,姓名,性別,薪資)VALUES(N'" +
                        id + "',N'" +
                        name + "',N'" +
                        sex + "'," +
                        money.ToString() + ")";
                    cmd.Connection = cn;
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //修改

            id = "A008";
            name = "mary";
            sex = "F";
            money = 54321;

            try
            {
                using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
                {
                    cn.Open();  // 打開資料庫連線
                    SqlCommand cmd = new SqlCommand();
                    // 查詢字串
                    //string sqlstr = "xxxxxxxxxxx";
                    cmd.CommandText = "UPDATE 員工 SET 姓名=N'" +
                        name + "', 性別=N'" +
                        sex + "', 薪資=" +
                        money + " WHERE 員工編號=N'" +
                        id + "'";
                    cmd.Connection = cn;
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //刪除
            id = "A008";
            sqlstr = "DELETE FROM 員工 WHERE 員工編號=N'" + id + "'";// 查詢字串

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

        private void button9_Click(object sender, EventArgs e)
        {
        }

        // CRUD 增查改刪 0 ST

        // 連接字串
        string cnstr23 = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\ch23DB.mdf;Integrated Security=True;Connect Timeout=30";

        private void button10_Click(object sender, EventArgs e)
        {
            //CRUD 增查改刪 0

            //讀取資料庫
            DataSet ds = SelectBook();
            dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增
            string 書號 = "IMS0311";
            string 書名 = "膠囊內視鏡";
            int 單價 = 12345;
            int 數量 = 20;

            InsertBook(書號, 書名, 單價, 數量);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //讀取資料庫
            ds = SelectBook();
            dataGridView2.DataSource = ds.Tables[0];  // DGV設置數據源

            richTextBox1.Text += "------------------------------\n";  // 30個

            //更新
            書號 = "IMS0311";//以書號為準
            書名 = "ims EGD";
            單價 = 123;
            數量 = 18;

            UpdateBook(書號, 書名, 單價, 數量);

            //讀取資料庫
            ds = SelectBook();
            dataGridView3.DataSource = ds.Tables[0];  // DGV設置數據源

            richTextBox1.Text += "------------------------------\n";  // 30個

            //刪除
            書號 = "IMS0311";//以書號為準

            DeleteBook(書號);

            //讀取資料庫
            ds = SelectBook();
            dataGridView4.DataSource = ds.Tables[0];  // DGV設置數據源
        }

        public DataSet SelectBook()
        {
            using (SqlConnection cn = new SqlConnection(cnstr23))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr23;  // 連接字串

                // 查詢字串
                string sqlstr = "SELECT * FROM 書籍";
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                return ds;
            }
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
            richTextBox1.Text += "測試 ExecuteScalar()\n";

            string db_filename = "ch17DB.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;
                cn.Open();  // 打開資料庫連線
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "員工");  // da將查詢的結果填充至數據集ds, 指定TableName為"員工"
                dataGridView1.DataSource = ds.Tables["員工"];  // DGV設置數據源

                richTextBox1.Text += "------------------------------\n";  // 30個

                // 查詢字串 取員工資料筆數
                string sqlstr1 = "SELECT COUNT(*) FROM 員工";
                SqlCommand cmd1 = new SqlCommand(sqlstr1, cn);
                richTextBox1.Text += "員工資料表共 " + cmd1.ExecuteScalar().ToString() + " 筆記錄\n";
                /*
                // 查詢字串 取薪資加總
                string sqlstr2 = "SELECT SUM(薪資) FROM 員工";
                SqlCommand cmd2 = new SqlCommand(sqlstr2, cn);
                richTextBox1.Text += "員工資料表薪資加總共 " + cmd2.ExecuteScalar().ToString() + "\n";

                // 查詢字串 取薪資平均
                string sqlstr3 = "SELECT AVG(薪資) FROM 員工";
                SqlCommand cmd3 = new SqlCommand(sqlstr3, cn);
                richTextBox1.Text += "員工資料表薪資平均為 " + cmd3.ExecuteScalar().ToString() + "\n";

                // 查詢字串 取薪資最高薪
                string sqlstr4 = "SELECT Max(薪資) FROM 員工";
                SqlCommand cmd4 = new SqlCommand(sqlstr4, cn);
                richTextBox1.Text += "最高薪為 " + cmd4.ExecuteScalar().ToString() + "\n";

                // 查詢字串 取薪資最低薪
                string sqlstr5 = "SELECT Min(薪資) FROM 員工";
                SqlCommand cmd5 = new SqlCommand(sqlstr5, cn);
                richTextBox1.Text += "最低薪為 " + cmd5.ExecuteScalar().ToString() + "\n";
                */
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //SQL 1
            string db_filename = "db_TomeTwo.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM EmployeeInfo";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
            }

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
                IEnumerable<DataRow> query = ds.Tables["EmployeeInfo"].AsEnumerable().TakeWhile(itm => itm.Field<DateTime>("Birthday") < Convert.ToDateTime("2009-7-1"));
                dataGridView1.DataSource = query.CopyToDataTable();  // DGV設置數據源
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //SQL 2
            string db_filename = "ch20DB.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工 ORDER BY 編號 DESC";

            //LINQ 1
            //建立DataSet物件ds，ds建立於所有事件處理函式之外以便所有事件一起共用
            DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;

                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                da.Fill(ds, "員工");  // da將查詢的結果填充至數據集ds, 指定TableName為"員工"
                dataGridView1.DataSource = ds.Tables["員工"];  // DGV設置數據源
            }

            int money = 25000;
            richTextBox1.Text += "搜尋 薪資 > " + money.ToString() + " 的資料\n";
            try
            {
                DataTable dtEmp = ds.Tables["員工"];
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

        private void button15_Click(object sender, EventArgs e)
        {
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            richTextBox1.Text += "取得一個資料庫的所有Table名稱 1\n";

            //這樣會列出所有 實際的資料表（不包含檢視表）

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                cn.Open();

                string query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'";

                using (SqlCommand cmd = new SqlCommand(query, cn))
                using (SqlDataReader dr = cmd.ExecuteReader())
                {
                    while (dr.Read())
                    {
                        richTextBox1.Text += dr["TABLE_NAME"] + "\n";
                    }
                }
            }

            //3030
            richTextBox1.Text += "取得一個資料庫的所有Table名稱 2\n";

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                cn.Open();

                string query = "SELECT name FROM sys.tables";
                //string query = "SELECT name FROM sysdatabases";
                //string query = "SELECT NAME FROM master.dbo.sysdatabases";
                //string query = "select count(*) from master.dbo.sysdatabases where name='db_02'";
                //string query = "SELECT * FROM 員工", cn);//執行一條SQL查詢語句
                //string query = "SELECT * FROM master..sysdatabases WHERE name = N'ch17DB'", cn);//執行一條SQL查詢語句


                //這個方式直接從 SQL Server 的系統目錄取出所有表格名稱

                using (SqlCommand cmd = new SqlCommand(query, cn))
                using (SqlDataReader dr = cmd.ExecuteReader())
                {
                    while (dr.Read())
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
                }
            }

            return;

            //3030
            richTextBox1.Text += "取得一個資料庫的所有Table名稱 3\n";

            using (SqlConnection conn = new SqlConnection(cnstr))
            {
                conn.Open();
                var schema = conn.GetSchema("Tables");
                foreach (System.Data.DataRow row in schema.Rows)
                {
                    //Console.WriteLine(row["TABLE_NAME"]);
                    richTextBox1.Text += row["TABLE_NAME"] + "\n";
                }
            }
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
            //DB1
            //讀取DB的資料到dataGridView1

            string db_filename = "db_09_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Employee";

            //讀取資料庫至DGV
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                DataTable dt = new DataTable();  // 建立DT
                SqlDataAdapter da = new SqlDataAdapter("SELECT * FROM 員工表", cn);  // 建立資料庫適配器對象da
                da.Fill(dt);  // da將查詢的結果填充至數據集ds, 不指定TableName
                this.dataGridView1.DataSource = dt.DefaultView;  // DGV設置數據源
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 查詢字串
            sqlstr = "xxxxxxxxxxx";
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //在文字框中輸入有效的SQL語句修改數據

                using (SqlCommand cmd = new SqlCommand())
                {
                    try
                    {
                        cn.Open();  // 打開資料庫連線
                        cmd.Connection = cn;
                        cmd.CommandText = sqlstr;
                        cmd.ExecuteNonQuery();  // 執行SQL命令
                        cn.Close();
                        richTextBox1.Text += "刪除成功\n";
                    }
                    catch
                    {
                        richTextBox1.Text += "SQL語句有誤\n";
                    }
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //讀取DB的資料到dataGridView2
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                DataTable dt = new DataTable();  // 建立DT
                SqlDataAdapter da = new SqlDataAdapter("SELECT * FROM 員工表", cn);  // 建立資料庫適配器對象da
                da.Fill(dt);  // da將查詢的結果填充至數據集ds, 不指定TableName
                this.dataGridView2.DataSource = dt.DefaultView;  // DGV設置數據源
            }
        }

        string DatabaseName { get; set; }

        private void button20_Click(object sender, EventArgs e)
        {
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;Initial Catalog=master;Integrated Security=True";

            DatabaseName = "TestCreateDB";

            //先看看有沒有相同的DB存在，如果有的話卸離並移除
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();  // 打開資料庫連線
                var cmd = cn.CreateCommand();

                // 查詢字串
                string sqlstr = string.Format("exec sp_detach_db '{0}'", DatabaseName);

                cmd.CommandText = sqlstr;
                try
                {
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                }
                catch
                {
                    richTextBox1.Text += "Could not detach\n";
                }
            }

            //清理

            var fileName = string.Concat(@"D:\", DatabaseName);

            richTextBox1.Text += "CleanupDatabase :\n" + fileName + "\n";

            try
            {
                var mdfPath = string.Concat(fileName, ".mdf");
                var ldfPath = string.Concat(fileName, "_log.ldf");

                richTextBox1.Text += "mdfPath : " + mdfPath + "\n";
                richTextBox1.Text += "ldfPath : " + ldfPath + "\n";

                var mdfExists = File.Exists(mdfPath);
                var ldfExists = File.Exists(ldfPath);

                if (mdfExists)
                {
                    File.Delete(mdfPath);
                }
                if (ldfExists)
                {
                    File.Delete(ldfPath);
                }
            }
            catch
            {
                richTextBox1.Text += "Could not delete the files (open in Visual Studio?)\n";
            }

            //程式建立LocalDB
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                var commandText = new StringBuilder();
                //Create DB的語法
                // 查詢字串
                string sqlstr = string.Format("CREATE DATABASE {0} ON (NAME = N'{0}', FILENAME = '{1}.mdf');", DatabaseName, fileName);
                commandText.AppendFormat(sqlstr);
                richTextBox1.Text += "sqlstr :\n" + sqlstr + "\n";
                cn.Open();  // 打開資料庫連線
                var cmd = cn.CreateCommand();
                cmd.CommandText = commandText.ToString();
                cmd.ExecuteNonQuery();  // 執行SQL命令
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立資料庫, 目前只能新增表單, 需使用既有資料庫\n";

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\TestCreateDB.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串

                SqlCommand cmd = new SqlCommand();

                //4 给命令执行对象指定连接对象
                cmd.Connection = cn;

                // 查詢字串
                //string sqlstr = "create database mydatabase2";
                string sqlstr = "create database mydatabase3aaaa";
                cmd.CommandText = sqlstr;
                cn.Open();  // 打開資料庫連線
                try  //使用try...catch...敘述來補捉異動資料可能發生的例外 
                {
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += ex.Message + ", 新增資料發生錯誤\n";
                }
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //測試登錄功能

            string id_name = "david";
            string password = "123456";

            string db_filename = "db_TomeTwo.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            //SqlConnection cn = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30");//创建数据库连接对象
            SqlConnection cn = new SqlConnection(cnstr);  // 建立資料庫連接對象cn

            // 建立資料庫適配器對象da
            SqlDataAdapter sqlda = new SqlDataAdapter("SELECT Name,Pwd from tb_Login where Name=@name and Pwd=@pwd", cn);//创建数据库桥接器对象

            //为SQL语句中的参数赋值
            sqlda.SelectCommand.Parameters.Add("@name", SqlDbType.NChar, 10).Value = id_name;
            sqlda.SelectCommand.Parameters.Add("@pwd", SqlDbType.NChar, 10).Value = password;
            DataSet myds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            sqlda.Fill(myds);  // da將查詢的結果填充至數據集ds, 不指定TableName
            if (myds.Tables[0].Rows.Count > 0)//判断数据集中的表中是否有行
            {
                MessageBox.Show("用户登录成功！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("用户登录失败，原因为：用户名或密码错误！", "错误", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //跳过满足指定条件的记录
            //跳过生日小于2009-7-1的员工:

            string db_filename = "db_TomeTwo.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * from EmployeeInfo";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlCommand cmd = new SqlCommand(sqlstr, cn);

                SqlDataAdapter da = new SqlDataAdapter(cmd);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)

                da.Fill(ds, "EmployeeInfo");//填充数据集

                //跳过生日小于2009-7-1的员工信息
                IEnumerable<DataRow> query = ds.Tables["EmployeeInfo"].AsEnumerable().SkipWhile(itm => itm.Field<DateTime>("Birthday") < Convert.ToDateTime("2009-7-1"));
                dataGridView1.DataSource = query.CopyToDataTable();//设置dataGridView1数据源
            }
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        void show_product_data(DataGridView dgv, string mesg)
        {
            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

            //取得產品類別, 並顯示dataGridView1上
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                // 查詢字串
                string sqlstr = "SELECT * From 產品類別";
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dgv.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv1.Text = mesg;
            }
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //產品類別管理 產品資料管理 產品關聯查詢

            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

            //產品類別管理

            show_product_data(dataGridView1, "產品類別");

            richTextBox1.Text += "------------------------------\n";  // 30個

            //產品資料管理

            //將產品類別顯示在清單中   
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                // 查詢字串
                string sqlstr = "SELECT * From 產品類別";
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView2.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv2.Text = "產品類別";
            }

            //查詢 類別編號 = 1 的資料
            int CategoryId1 = 1;
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                // 查詢字串
                string sqlstr = "SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId1;
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView3.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv3.Text = "產品資料管理";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //產品關聯查詢

            show_product_data(dataGridView1, "產品類別");

            //查詢 類別編號 = 1 的資料
            //int CategoryId1 = 1;

            //取得目前產品類別dataGridView4所選取記錄的第一欄資料，即類別編號
            //並指定給CategoryId整數變數
            int CategoryId2 = 1;
            richTextBox1.Text += "CategoryId2 = " + CategoryId2.ToString() + "\n";
            //傳入類別編號CategoryId來取得該類別相對應的產品資料
            //接著將產品資料顯示在dataGridView4上
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                // 查詢字串
                string sqlstr = "SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId2;
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView4.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv4.Text = "產品關聯查詢";
            }
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //新增 修改 刪除

            // 連接字串
            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";
            // 查詢字串
            string sqlstr = "xxxxx";

            richTextBox1.Text += "新增類別名稱\n";

            string new_item = "麥當勞";

            //呼叫Edit()方法並傳入INSERT陳述式新增產品類別記錄
            db.Edit("INSERT INTO 產品類別(類別名稱)VALUES(N'" + new_item + "')");

            show_product_data(dataGridView1, "產品類別");

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "修改, 修改 類別編號4 的 產品類別\n";

            int old_id = 4;

            string new_item2 = "肯德雞";

            //呼叫Edit()方法並傳入UPDATE陳述式修改產品類別記錄
            //取得DataGridView目前選取第一欄的資料，也就是類別編號欄位
            db.Edit("UPDATE 產品類別 SET 類別名稱=N'" + new_item2 + "' WHERE 類別編號=" + old_id.ToString());

            show_product_data(dataGridView2, "產品類別");

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "刪除\n";

            int delete_id = 5;

            //呼叫Edit()方法並傳入DELETE陳述式刪除指定的產品類別記錄
            db.Edit("DELETE FROM 產品類別 WHERE 類別編號=" + delete_id.ToString());

            delete_id = 6;
            //刪除與產品類別相關聯的產品資料
            db.Edit("DELETE FROM 產品資料 WHERE 類別編號=" + delete_id.ToString());

            show_product_data(dataGridView3, "產品類別");
        }

        private void button28_Click(object sender, EventArgs e)
        {
            //新增 修改 刪除
            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

            richTextBox1.Text += "新增\n";

            string new_item = "必勝客";
            int price = 12345;//單價
            string mesg = "電話訂購";//說明

            db.Edit("INSERT INTO 產品資料(類別編號,品名,單價,說明)VALUES(" +
                "1" + ",N'" +
                new_item + "'," +
                price.ToString() + ",N'" +
                mesg + "')");

            int CategoryId1 = 1;//類別編號
            richTextBox1.Text += "CategoryId1 = " + CategoryId1.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                // 查詢字串
                string sqlstr = "SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId1;
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv1.Text = "新增 產品資料";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "修改\n";

            new_item = "達美樂";
            price = 123;//單價
            mesg = "網路訂購";//說明

            db.Edit("UPDATE 產品資料 SET 品名=N'" +
                new_item + "', 單價=" +
                price.ToString() + ", 說明=N'" +
                mesg + "' WHERE 產品編號=" +
                dataGridView1.CurrentRow.Cells[0].Value.ToString());

            int CategoryId2 = 1;//類別編號
            richTextBox1.Text += "CategoryId2 = " + CategoryId2.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                // 查詢字串
                string sqlstr = "SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId2;
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv1.Text = "修改 產品資料";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "刪除\n";

            db.Edit("DELETE FROM 產品資料 WHERE 產品編號=" + dataGridView1.CurrentRow.Cells[0].Value.ToString());

            int CategoryId3 = 1;//類別編號
            richTextBox1.Text += "CategoryId3 = " + CategoryId3.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                // 查詢字串
                string sqlstr = "SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId3;
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv1.Text = "刪除 產品資料";
            }
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //RelationsDemo
            string db_filename = "Northwind.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
            {
                cn.ConnectionString = cnstr;

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)

                // 查詢字串
                string sqlstr1 = "SELECT * FROM 產品類別";
                SqlDataAdapter da1 = new SqlDataAdapter(sqlstr1, cn);  // 建立資料庫適配器對象da
                da1.Fill(ds, "產品類別");

                // 查詢字串
                string sqlstr2 = "SELECT * FROM 產品資料";
                SqlDataAdapter da2 = new SqlDataAdapter(sqlstr2, cn);  // 建立資料庫適配器對象da
                da2.Fill(ds, "產品資料");

                ds.Relations.Add("FK_產品資料_產品類別", ds.Tables["產品類別"].Columns["類別編號"], ds.Tables["產品資料"].Columns["類別編號"]);

                dataGridView1.DataSource = ds;
                dataGridView1.DataMember = "產品類別";

                dataGridView2.DataSource = ds;
                dataGridView2.DataMember = "產品類別.FK_產品資料_產品類別";
            }
        }
    }

    class MyDBClass
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

        //Edit()方法可依傳入的SQL陳述式對指定的資料表進行新增、修改、刪除
        public void Edit(string SqlCmd)
        {
            try
            {
                SqlConnection cn = new SqlConnection(db_cnstr);  // 建立資料庫連接對象cn
                cn.Open();  // 打開資料庫連線
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = SqlCmd;
                cmd.Connection = cn;
                cmd.ExecuteNonQuery();
                cn.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
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



/* schema 應無用
                SqlDataReader dr = cmd.ExecuteReader();
                DataTable schema = dr.GetSchemaTable();  // 建立DT
                foreach (DataRow schema_row in schema.Rows)
                {
                    richTextBox1.Text += "欄位名稱 : "+schema_row.Field<string>("ColumnName") + "\t";
                    richTextBox1.Text += "資料型態 : "+schema_row.Field<Type>("DataType").ToString() + "\n";
                }

*/


/*

//命令字串
            string sqlstr = "select emp_id as 用戶編號,fname as 用戶姓名,hire_date as 工作時間 from employee";//定義一個查詢字符串變量

            DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            ds.Clear();//清空數據集中原有內容
            try
            {
                SqlConnection cn = new SqlConnection(ConnectString);  // 建立資料庫連接對象cn
                da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
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
            for (int i = 0; i < dt.Rows.Count; i++)//循環遍歷數據表中的每一行數據
            {
                for (int j = 0; j < dt.Columns.Count; j++)//循環遍歷數據表中每一列數據
                {
                    item[j] = dt.Rows[i][j];//保存數據表中的數據內容
                }
                dataGridView1.Rows.Add(item);//向DataGridView中添加數據
            }
*/


/*
            //可用的資料庫與表單
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeOne.mdf;Integrated Security=True;Connect Timeout=30";
              // 查詢字串
            string sqlstr = "SELECT * FROM tb_Rectangle";
            string sqlstr = "SELECT TOP 4 * FROM tb_Rectangle order by t_Num desc";

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";
  // 查詢字串
            string sqlstr = "SELECT * From 產品類別";
 *   // 查詢字串
            //string sqlstr = "SELECT * From 產品資料";

*/





// 連接字串
//string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\MyDB.mdf;Integrated Security=True;Connect Timeout=30";
//cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|\ch17DB.mdf;Integrated Security=True";
//string cnstr1 = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|ch17DB.mdf;Integrated Security=True";
//cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

/*
有v11.0的, 就不可以, 要改用MSSQLLocalDB
AttachDbFilename=|DataDirectory|ch17DB.mdf  是 mdf 在 |DataDirectory|之下
AttachDbFilename=D:\ch17DB.mdf 是 指定 mdf 的位置
固定的寫法 :
Integrated Security=True";
其他參數 :
Connect Timeout=30

cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;       AttachDbFilename=|DataDirectory|ch17DB.mdf;                                   ;
cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;       AttachDbFilename=D:\ch17DB.mdf;      ;
cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\ch17DB.mdf; ;
*/

//宣告cnStr連線字串置於事件處理函式外，以提供給其他事件處理函式共用
//string cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\MyDB.mdf;Integrated Security=True;Connect Timeout=30";
// 連接字串
//                    String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\VisualC#2015基礎必修課\2015範例程式\data\MyDB.mdf;Integrated Security=True;Connect Timeout=30";


//string cnstr =  "Data Source=MR-PC\\YL;Database=db_TomeTwo;UID=sa;Pwd=;";//取连接字符串


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


/*
可用
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 查詢字串, 搜尋 表單 tb_Employee 欄位 工资 前4筆 降冪排列
            sqlstr = "SELECT TOP 4 * FROM tb_Employee order by 工资 desc";
*/






//            string sqlstr = "select job_id as 工作编号,job_desc as 工作次序,min_lvl as 最低水平,max_lvl as 最高水平 from jobs";


/*
            SqlConnection cn = new SqlConnection(cnstr);//初始化數據庫連接對像
            string sqlstr = "select au_id as 使用者編號,au_lname as 姓名,phone as 電話號碼 from authors";//初始化SQL查詢語句
            SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);//初始化一個數據讀取器
            DataSet ds = new DataSet();//初始化一個數據集
            da.Fill(ds, "authors");//向數據集中填充內容
            dataGridView1.DataSource = ds.Tables["authors"].DefaultView;//為DataGridView控制元件填充數據源
            for (int i = 0; i < dataGridView1.Columns.Count; i++)//循環搜尋DataGridView控制元件中的每一列
            {
                //禁用DataGridView控制元件列表頭自動排序功能
                dataGridView1.Columns[i].SortMode = DataGridViewColumnSortMode.NotSortable;//設定每一列的排序類型為不排序
            }
*/
