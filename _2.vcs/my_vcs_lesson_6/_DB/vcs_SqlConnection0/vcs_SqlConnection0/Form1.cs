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

namespace vcs_SqlConnection0
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
            this.Text = "vcs_SqlConnection0";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_database(string db_filename, string cmd_name)
        {
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                SqlDataAdapter da = new SqlDataAdapter(cmd_name, cn);
                DataSet ds = new DataSet();
                da.Fill(ds, "table");
                dataGridView1.DataSource = ds.Tables[0].DefaultView;
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //讀取資料庫0, 要先知道資料庫檔案(.mdf)和表單名稱(tb_Employee)

            // 資料庫連線參數, 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

            //创建数据库连接对象
            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                //创建适配器对象
                SqlDataAdapter da = new SqlDataAdapter("SELECT * FROM tb_Employee", cn);

                //创建数据集
                DataSet ds = new DataSet();
                da.Fill(ds);  // 將查詢的結果填充至DS數據集, 不指定TableName
                //da.Fill(ds, "員工");  // 將查詢的結果填充至DS數據集, 指定TableName為"員工"

                dataGridView2.DataSource = ds.Tables[0];//设置数据源
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            string db_filename = "db_TomeTwo.MDF";
            string cmd_name = "SELECT * FROM tb_Employee";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 讀出資料庫資料
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;  // 資料庫連線參數, 連接字串

                cn.Open();

                SqlCommand cmd = new SqlCommand("SELECT * FROM tb_Employee", cn);

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
                    //richTextBox1.Text += "第 " + cnt.ToString() + " 筆資料 :\n";
                    cnt++;
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        richTextBox1.Text += dr[i].ToString() + "\t";
                        //richTextBox1.Text += dr.GetValue(i).ToString() + "\t";    //same
                    }
                    richTextBox1.Text += "\n";
                }
            }

            // 讀出資料庫資料
            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                cn.Open();

                //搜尋 表單 tb_Employee 欄位 工资 前4筆 降冪排列
                //using (SqlCommand cmd = new SqlCommand("SELECT TOP 4 * FROM tb_Rectangle order by t_Num desc", cn))
                using (SqlCommand cmd = new SqlCommand("SELECT TOP 4 * FROM tb_Employee order by 工资 desc", cn))
                {
                    SqlDataReader dr = cmd.ExecuteReader();  // 创建SqlDataReader对象

                    for (int j = 0; j < 4; j++)
                    {
                        //richTextBox1.Text += "第 " + j.ToString() + " 筆資料 :\n";
                        if (dr.Read())
                        {
                            richTextBox1.Text += "Name : " + dr[1].ToString() + "\n";
                            richTextBox1.Text += "Age : " + dr[3].ToString() + "\n";
                            richTextBox1.Text += "工资 : " + dr[10].ToString() + "\n";
                        }
                    }
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取資料庫1
            //取得資料

            //讀取資料庫0, 要先知道資料庫檔案(.mdf)和表單名稱(tb_Rectangle)

            // 資料庫連線參數, 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeOne.mdf;Integrated Security=True;Connect Timeout=30";

            //创建数据库连接对象
            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                //创建适配器对象
                SqlDataAdapter da = new SqlDataAdapter("SELECT * FROM tb_Rectangle", cn);

                //创建数据集
                DataSet ds = new DataSet();
                da.Fill(ds);//填充数据集

                dataGridView1.DataSource = ds.Tables[0];//设置数据源
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //讀取資料庫2

            string db_filename = "Northwind.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            using (SqlConnection cn = new SqlConnection())
            {
                //多次查詢 分別放置一個DS的多個Table中
                //不同DGV顯示不同Table的資料

                DataSet ds = new DataSet();  // 建立DataSet來儲存Table

                // 連接資料庫
                cn.ConnectionString = cnstr;  // 資料庫連線參數, 連接字串

                // 建立三個DataAdapter物件，用來取得員工, 客戶, 產品類別資料表
                // 再將三個資料表放入ds(DataSet)物件中
                string sqlstr1 = "SELECT * FROM 員工";  // 宣告查詢字串
                SqlDataAdapter da1 = new SqlDataAdapter(sqlstr1, cn);
                da1.Fill(ds, "員工");  // 將DataAdapter查詢之後的結果填充至DataSet

                string sqlstr2 = "SELECT * FROM 客戶";  // 宣告查詢字串
                SqlDataAdapter da2 = new SqlDataAdapter(sqlstr2, cn);
                da2.Fill(ds, "客戶");  // 將DataAdapter查詢之後的結果填充至DataSet

                string sqlstr3 = "SELECT * FROM 產品類別";  // 宣告查詢字串
                SqlDataAdapter da3 = new SqlDataAdapter(sqlstr3, cn);
                da3.Fill(ds, "產品類別");  // 將DataAdapter查詢之後的結果填充至DataSet

                // 將ds物件內三個DataTable
                for (int i = 0; i < ds.Tables.Count; i++)
                {
                    richTextBox1.Text += "取得 資料表 : " + ds.Tables[i].TableName + "\n";
                }

                richTextBox1.Text += "TableName1 : " + ds.Tables["員工"].TableName + "\n";
                richTextBox1.Text += "TableName2 : " + ds.Tables["客戶"].TableName + "\n";
                richTextBox1.Text += "TableName3 : " + ds.Tables["產品類別"].TableName + "\n";

                dataGridView1.DataSource = ds.Tables["員工"];
                lb_dgv1.Text = "員工";

                dataGridView2.DataSource = ds.Tables["客戶"];
                lb_dgv2.Text = "客戶";

                dataGridView3.DataSource = ds.Tables["產品類別"];
                lb_dgv3.Text = "產品類別";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //讀取資料庫3

            string db_filename = "db_02.mdf";
            string cmd_name = "select * from tb_student";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                cn.Open();
                SqlCommand com = new SqlCommand("select * from tb_student", cn);
                SqlDataReader dr = com.ExecuteReader();
                while (dr.Read())
                {
                    richTextBox1.Text += dr[1].ToString() + "\n";
                }
                dr.Close();
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // 成績單
            string db_filename = "ch17DB.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;
                cn.Open();  // 打開數據庫連線

                SqlCommand cmd = new SqlCommand("SELECT * FROM 成績單", cn);

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
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

                DataSet ds = new DataSet();  // 建立DataSet來儲存Table

                // 建立SqlDataAdapter物件da並取出成績單資料表
                string sqlstr = "SELECT * FROM 成績單";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);

                // 將成績單資料表所有記錄填入ds物件
                da.Fill(ds, "成績單");  // 將DataAdapter查詢之後的結果填充至DataSet

                // 宣告DataTable物件dt，該dt內存放ds中的成績單DataTable
                DataTable dt = ds.Tables["成績單"];
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
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

                DataSet ds = new DataSet();  // 建立DataSet來儲存Table

                // 建立SqlDataAdapter物件da並取出成績單資料表
                string sqlstr = "SELECT * FROM 成績單";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);

                // 將成績單資料表所有記錄填入ds物件
                da.Fill(ds, "成績單");  // 將DataAdapter查詢之後的結果填充至DataSet

                // 宣告DataTable物件dt，該dt內存放ds中的成績單DataTable
                DataTable dt = ds.Tables["成績單"];

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
            //string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            string name = "阿龍";
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;
                cn.Open();  // 打開數據庫連線

                // 將輸入的姓名指定給searchName字串變數
                string searchName = name;
                // SELECT敘述的查詢條件為姓名等於searchName
                string selectCmd = "SELECT * FROM 成績單 WHERE 姓名 = '" + searchName + "'";
                // 建立SqlCommand物件cmd
                SqlCommand cmd = new SqlCommand(selectCmd, cn);
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
            //string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            //string name = "阿龍";
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;
                cn.Open();  // 打開數據庫連線

                // 將輸入的姓名指定給searchName字串變數
                string searchName = name;
                // SELECT敘述的查詢條件為姓名等於searchName
                string selectCmd = "SELECT * FROM 成績單 WHERE 姓名 = '" + searchName.Replace("'", "''") + "'";
                // 建立SqlCommand物件cmd
                SqlCommand cmd = new SqlCommand(selectCmd, cn);
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
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;

                string sqlstr = "SELECT * FROM 成績單 ORDER BY 國文 DESC";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);

                DataSet ds = new DataSet();

                da.Fill(ds, "成績單");

                DataView dv;  // 宣告DataView物件dv

                dv = ds.Tables["成績單"].DefaultView;

                dataGridView1.DataSource = dv;

                richTextBox1.Text += "------------------------------\n";  // 30個

                string filter = "國文>80";  // 篩選條件, 用WHRER語法
                string sort = "英文 DESC";  // 排序方法, 科目, ASC:遞增, DESC:遞減

                richTextBox1.Text += "篩選條件 : " + filter + "\n";
                richTextBox1.Text += "排序方法 : " + sort + "\n";

                dv.RowFilter = filter;
                dv.Sort = sort;

                dataGridView1.DataSource = dv;
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //讀取資料庫4
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                cn.Open();
                SqlCommand com = new SqlCommand("select * from tb_Land", cn);
                SqlDataReader dr = com.ExecuteReader();
                while (dr.Read())
                {
                    //this.listBox1.Items.Add(dr[1].ToString());
                    richTextBox1.Text += dr[1].ToString() + "\n";
                }
                dr.Close();
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //讀取資料庫5
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                cn.Open();
                SqlCommand com = new SqlCommand("select * from tb_02", cn);
                SqlDataReader dr = com.ExecuteReader();

                while (dr.Read())
                {
                    richTextBox1.Text += dr[0].ToString() + "\t" + dr[1].ToString() + "\t" + dr[2].ToString() + "\t" + "\n";
                }
                dr.Close();
            }
        }

        public void getScoure(string strName)
        {
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                cn.Open();

                SqlCommand com = new SqlCommand(strName, cn);
                SqlDataReader dr = com.ExecuteReader();


                while (dr.Read())
                {
                    richTextBox1.Text += dr[0].ToString() + "\t" + dr[1].ToString() + "\t" + dr[2].ToString() + "\n";
                }
                dr.Close();
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //讀取資料庫6
            //取得資料
            getScoure("select * from tb_05");

            /*
            //升冪排列
            getScoure("select * from tb_05  order by 銷售數量 asc");

            //降冪排列
            getScoure("select * from tb_05 order by 銷售數量 desc");
            */
        }

        private void button9_Click(object sender, EventArgs e)
        {
            // 資料庫連線參數, 連接字串
            string db_filename = "Northwind.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;  // 資料庫連線參數, 連接字串

                richTextBox1.Text += "連接資料庫前\t資料庫連接狀態 : " + cn.State + "\n";  // ConnectionState.Closed
                cn.Open();  // 連接資料庫

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
        }

        // CRUD 增查改刪 0 ST

        // 宣告cnStr資料庫連接字串，指定連接ch23DB.mdf
        string cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\ch23DB.mdf;Integrated Security=True;Connect Timeout=30";

        private void button10_Click(object sender, EventArgs e)
        {
            //CRUD 增查改刪 0

            //讀取資料庫
            DataSet ds = SelectBook();
            dataGridView1.DataSource = ds.Tables[0];//设置数据源

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
            dataGridView2.DataSource = ds.Tables[0];//设置数据源

            richTextBox1.Text += "------------------------------\n";  // 30個

            //更新
            書號 = "IMS0311";//以書號為準
            書名 = "ims EGD";
            單價 = 123;
            數量 = 18;

            UpdateBook(書號, 書名, 單價, 數量);

            //讀取資料庫
            ds = SelectBook();
            dataGridView3.DataSource = ds.Tables[0];//设置数据源

            richTextBox1.Text += "------------------------------\n";  // 30個

            //刪除
            書號 = "IMS0311";//以書號為準

            DeleteBook(書號);

            //讀取資料庫
            ds = SelectBook();
            dataGridView4.DataSource = ds.Tables[0];//设置数据源
        }

        public DataSet SelectBook()
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnStr;  // 資料庫連線參數, 連接字串
                SqlDataAdapter da = new SqlDataAdapter("SELECT * FROM 書籍", cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                return ds;
            }
        }

        public void InsertBook(string 書號, string 書名, int 單價, int 數量)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnStr;  // 資料庫連線參數, 連接字串
                cn.Open();
                string sqlStr = "INSERT INTO 書籍(書號, 書名, 單價, 數量)" + "VALUES(@BookId, @BookName, @Price, @Qty)";
                SqlCommand cmd = new SqlCommand(sqlStr, cn);
                cmd.Parameters.Add(new SqlParameter("@BookId", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter("@BookName", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter("@Price", SqlDbType.Int));
                cmd.Parameters.Add(new SqlParameter("@Qty", SqlDbType.Int));
                cmd.Parameters["@BookId"].Value = 書號;
                cmd.Parameters["@BookName"].Value = 書名;
                cmd.Parameters["@Price"].Value = 單價;
                cmd.Parameters["@Qty"].Value = 數量;
                cmd.ExecuteNonQuery();
            }
        }

        public void UpdateBook(string 書號, string 書名, int 單價, int 數量)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnStr;  // 資料庫連線參數, 連接字串
                cn.Open();
                string sqlStr = "UPDATE 書籍 SET 書名=@BookName," + "單價=@Price, 數量=@Qty WHERE 書號=@BookId";
                SqlCommand cmd = new SqlCommand(sqlStr, cn);
                cmd.Parameters.Add(new SqlParameter("@BookId", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter("@BookName", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter("@Price", SqlDbType.Int));
                cmd.Parameters.Add(new SqlParameter("@Qty", SqlDbType.Int));
                cmd.Parameters["@BookId"].Value = 書號;
                cmd.Parameters["@BookName"].Value = 書名;
                cmd.Parameters["@Price"].Value = 單價;
                cmd.Parameters["@Qty"].Value = 數量;
                cmd.ExecuteNonQuery();
            }
        }

        public void DeleteBook(string 書號)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnStr;  // 資料庫連線參數, 連接字串
                cn.Open();
                string sqlStr = "DELETE FROM 書籍 WHERE 書號 = @BookId";
                SqlCommand cmd = new SqlCommand(sqlStr, cn);
                cmd.Parameters.Add(new SqlParameter("@BookId", SqlDbType.NVarChar));
                cmd.Parameters["@BookId"].Value = 書號;
                cmd.ExecuteNonQuery();
            }
        }

        // CRUD 增查改刪 0 SP

        private void button11_Click(object sender, EventArgs e)
        {
            //讀取資料庫7

            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                cn.Open();
                SqlCommand com = new SqlCommand("select * from tb_06", cn);
                SqlDataReader dr = com.ExecuteReader();
                while (dr.Read())
                {
                    ListViewItem lv = new ListViewItem(dr[1].ToString(), 0);
                    richTextBox1.Text += dr[1].ToString() + "\n";

                }
                dr.Close();
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //讀取資料庫8

            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                cn.Open();
                SqlCommand com = new SqlCommand("select * from tb_07", cn);
                SqlDataReader dr = com.ExecuteReader();

                while (dr.Read())
                {
                    richTextBox1.Text += dr[1].ToString() + "\t" + dr[0].ToString() + "\t" + dr[3].ToString() + "\t" + dr[2].ToString() + "\n";
                }
                dr.Close();
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

        // 資料庫連線參數, 連接字串
        string connection_string =
            @"Data Source=(LocalDB)\MSSQLLocalDB;Initial Catalog=master;Integrated Security=True";
        string TestConnectionString =
            @"Data Source=(LocalDB)\MSSQLLocalDB;Initial Catalog={0};Integrated Security=True;AttachDBFilename={1}.mdf";

        string DatabaseName { get; set; }

        private void button20_Click(object sender, EventArgs e)
        {
            DatabaseName = "TestCreateDB";

            //先看看有沒有相同的DB存在，如果有的話卸離並移除
            using (SqlConnection cn = new SqlConnection(connection_string))  // 資料庫連線參數, 連接字串
            {
                cn.Open();
                var cmd = cn.CreateCommand();
                string cmd_text = string.Format("exec sp_detach_db '{0}'", DatabaseName);
                cmd.CommandText = cmd_text;
                try
                {
                    cmd.ExecuteNonQuery();
                }
                catch
                {
                    Console.WriteLine("Could not detach");
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
                Console.WriteLine("Could not delete the files (open in Visual Studio?)");
            }

            //程式建立LocalDB
            using (SqlConnection cn = new SqlConnection(connection_string))  // 資料庫連線參數, 連接字串
            {
                var commandText = new StringBuilder();
                //Create DB的語法
                string cmd_text = string.Format("CREATE DATABASE {0} ON (NAME = N'{0}', FILENAME = '{1}.mdf');", DatabaseName, fileName);
                commandText.AppendFormat(cmd_text);
                richTextBox1.Text += "cmd_text :\n" + cmd_text + "\n";

                cn.Open();

                var cmd = cn.CreateCommand();
                cmd.CommandText = commandText.ToString();
                cmd.ExecuteNonQuery();
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立資料庫, 目前只能新增表單, 需使用既有資料庫\n";

            //1 建立连接对象
            SqlConnection cn = new SqlConnection();

            //2 连接字符串(这里连接的是本地数据库，sa用户登陆，无密码)
            // 資料庫連線參數, 連接字串
            //cn.ConnectionString = "server=.;uid=sa;pwd=;";  // NG
            cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\TestCreateDB.mdf;Integrated Security=True;Connect Timeout=30";

            //3 建立命令执行对象
            SqlCommand cmd = new SqlCommand();

            //4 给命令执行对象指定连接对象
            cmd.Connection = cn;

            //5 SQL语句（指定要创建数据库的SQL句）
            //string sqlstr = "create database mydatabase2";
            string sqlstr = "create database mydatabase3aaaa";

            cmd.CommandText = sqlstr;

            cn.Open();  // 打開數據庫連線

            try  //使用try...catch...敘述來補捉異動資料可能發生的例外 
            {
                cmd.ExecuteNonQuery();  // 執行SQL命令
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + ", 新增資料發生錯誤\n";
            }
            cn.Close();  // 關閉數據庫連線

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



/* schema 應無用
                SqlDataReader dr = cmd.ExecuteReader();
                DataTable schema = dr.GetSchemaTable();
                foreach (DataRow schema_row in schema.Rows)
                {
                    richTextBox1.Text += "欄位名稱 : "+schema_row.Field<string>("ColumnName") + "\t";
                    richTextBox1.Text += "資料型態 : "+schema_row.Field<Type>("DataType").ToString() + "\n";
                }

*/


/*
            //定義數據庫連接字符串

            // 無資料庫

            //string ConnectString = "server=.;database=pubs;integrated security=sspi";
            string ConnectString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02c.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection cn;//定義數據庫連接對象
            SqlDataAdapter da;//定義填充數據集對象
            DataSet ds = new DataSet();//定義存儲數據的集合
            DataTable dt = new DataTable();//定義一個數據表

            cn = new SqlConnection(ConnectString);//初始化數據庫連接對象
            string selectString = "select emp_id as 用戶編號,fname as 用戶姓名,hire_date as 工作時間 from employee";//定義一個查詢字符串變量
            DataSet PageSet = new DataSet();// 定義一個存儲數據的集合
            PageSet.Clear();//清空數據集中原有內容

            //FillDataTable(selectString, ref PageSet);

            try
            {
                SqlConnection cn = new SqlConnection(ConnectString);//初始化數據庫連接對象
                da = new SqlDataAdapter(selectString, cn);//初始化數據讀取對象
                da.Fill(PageSet);//填充數據集
            }
            catch (Exception ex)//捕獲異常
            {
                MessageBox.Show(ex.Message);//顯示異常信息
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

