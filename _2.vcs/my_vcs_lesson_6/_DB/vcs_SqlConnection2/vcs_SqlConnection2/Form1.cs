using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;  // for SqlConnection, SqlCommand, SqlDataAdapter

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

namespace vcs_SqlConnection2
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
            this.Text = "vcs_SqlConnection2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void sql_read_database(string db_filename, string sqlstr, DataGridView dgv)
        {
            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

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
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        void sql_write_database(string db_filename, string sqlstr)
        {
            //依傳入的SQL陳述式對指定的資料表進行新增、修改、刪除 應該都只是操作 並不能取出資料

            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

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

        private void button0_Click(object sender, EventArgs e)
        {
            //讀取資料庫 至 DGV
            //取得數據庫中全部的預儲程序

            // 資料庫檔案
            string db_filename = string.Empty;
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = string.Empty;

            db_filename = "db_10_Data.MDF";
            // 查詢字串
            sqlstr = "SELECT * FROM sysobjects";  // 有很多欄位
            sqlstr = "SELECT name, crdate, refdate FROM sysobjects";  // 只看3個欄位
            sqlstr = "SELECT name as 預儲程序名稱,crdate as 建立時間,refdate as 最後一次修改時間 FROM sysobjects";  // 只看3個欄位+改欄名            
            sql_read_database(db_filename, sqlstr, dataGridView1);

            /*
            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢邏輯型數據
            //查詢是否為國家統招學生：
            string select_type = "是";  // "是/否"

            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM tb_08 WHERE 統招否='" + select_type + "'";

            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------\n";  // 30個
            */
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工訊息表";

            //取得資料庫的內容
            sql_read_database(db_filename, sqlstr, dataGridView1);

            return;

            // 運用查詢預儲程序
            // 查詢字串
            sqlstr = "getEmployeeOrName";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                da.SelectCommand.CommandType = CommandType.StoredProcedure;  // ????
                SqlParameter prams = new SqlParameter("@員工姓名", SqlDbType.VarChar, 50);
                prams.Value = "李丹";
                // 依次把參數傳入命令文字
                da.SelectCommand.Parameters.Add(prams);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = ds.Tables[0].DefaultView;  // DGV設置數據源
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工訊息表";

            /*
            //取得資料庫的內容
            sql_read_database(db_filename, sqlstr, dataGridView1);
            */

            //運用預儲程序刪除數據
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();
                SqlCommand cmd = new SqlCommand("procDeleteEmployee", cn);
                cmd.CommandType = CommandType.StoredProcedure;  // ????
                SqlParameter pares = new SqlParameter("@員工編號", SqlDbType.VarChar, 50);
                cmd.Parameters.Add(pares);
                cmd.Parameters["@員工編號"].Value = "12345";
                cmd.ExecuteNonQuery();
                cn.Close();
            }

            //再取得資料庫的內容
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //運用預儲程序

            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "getAllEmployee";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                da.SelectCommand.CommandType = CommandType.StoredProcedure;  // ????
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "table");  // da將查詢的結果填充至數據集ds, 指定TableName為"table"
                dataGridView1.DataSource = ds.Tables[0].DefaultView;  // DGV設置數據源
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //通配符大全

            //show
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_stu";

            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用[]通配符進行查詢

            int age_like = 3;

            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM tb_stu WHERE 年齡 LIKE '" + age_like.ToString() + "[0-9]'";

            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //show
            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM tb_stu";

            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用[^]通配符進行查詢

            //利用[^]通配符進行查詢年齡：
            string student_age = "2";

            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM tb_stu WHERE 年齡 LIKE '[^" + student_age + "][0-9]'";

            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //show
            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM tb_stu";

            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用%通配符進行查詢

            //請輸入學生編號：
            string student_id = "3";

            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM tb_stu WHERE 學生編號 LIKE '%" + student_id + "%'";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //用IN查詢表中的記錄訊息

            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM 明細工資表";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢
            string number = "4";  // 員工編號
            // 查詢字串
            sqlstr = "SELECT * FROM 明細工資表 WHERE (員工編號 IN (" + number + "))";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用外連接進行多表聯合查詢
            // 查詢字串
            sqlstr = "SELECT 員工訊息表.序號, 員工訊息表.員工編號, 員工訊息表.員工姓名, 明細工資表.薪資編號, 明細工資表.月份, 明細工資表.基本工資, 明細工資表.獎金, 員工請假表.請假天數, 員工請假表.扣除金額 FROM 員工訊息表 LEFT OUTER JOIN 明細工資表 ON 員工訊息表.員工編號 = 明細工資表.員工編號 LEFT OUTER JOIN 員工請假表 ON 員工訊息表.員工編號 = 員工請假表.員工編號 ";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用右外連接查詢數據
            //RightOuterJoin

            // 查詢字串
            sqlstr = "SELECT 明細工資表.編號, 明細工資表.薪資編號, 員工訊息表.員工編號, 明細工資表.基本工資, 明細工資表.獎金, 員工訊息表.員工姓名, 員工訊息表.身份證號 FROM 員工訊息表 RIGHT OUTER JOIN 明細工資表 ON 員工訊息表.員工編號 = 明細工資表.員工編號";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用左外連接查詢數據
            // 查詢字串
            sqlstr = "SELECT 員工訊息表.序號, 員工訊息表.員工編號, 員工訊息表.員工姓名, 明細工資表.月份, 明細工資表.基本工資, 明細工資表.獎金 FROM 員工訊息表 LEFT OUTER JOIN 明細工資表 ON 員工訊息表.員工編號 = 明細工資表.員工編號";
            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //Insert觸發器的運用

            //show
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工工資表";

            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 員工訊息註冊

            //Insert觸發器的運用
            string number = "123";
            string name = "david";
            string id = "A123456789";
            string phone = "0912345678";

            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();
                SqlCommand cmd = new SqlCommand("INSERT INTO 員工訊息表 (員工編號,員工姓名,身份證號,聯繫電話) VALUES ('" + number + "','" + name + "','" + id + "','" + phone + "')", cn);
                cmd.ExecuteNonQuery();
                cn.Close();
                MessageBox.Show("數據新增成功！");
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //運用預儲程序新增數據
            //show
            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM 員工訊息表";

            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //運用預儲程序新增數據

            //員工基本訊息註冊

            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();
                SqlCommand cmd = new SqlCommand("procInsertEmployee", cn);
                cmd.CommandType = CommandType.StoredProcedure;
                SqlParameter[] prams = {
						new SqlParameter("@員工編號",  SqlDbType.VarChar, 50),
                		new SqlParameter("@員工姓名",  SqlDbType.VarChar, 50),
                		new SqlParameter("@身份證號",  SqlDbType.VarChar, 50),
                        new SqlParameter("@聯繫電話",  SqlDbType.VarChar, 50) 
			};

                number = "123";
                name = "david";
                id = "A123456789";
                phone = "0912345678";

                prams[0].Value = number;
                prams[1].Value = name;
                prams[2].Value = id;
                prams[3].Value = phone;

                // 新增參數
                foreach (SqlParameter parameter in prams)
                {
                    cmd.Parameters.Add(parameter);
                }
                cmd.ExecuteNonQuery();
                cn.Close();
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //運用預儲程序修改數據

            //show
            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM 員工訊息表";

            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //運用預儲程序修改數據

            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                cn.Open();
                SqlCommand cmd = new SqlCommand("procUpdateEmployee", cn);
                cmd.CommandType = CommandType.StoredProcedure;
                SqlParameter[] prams = {
			        new SqlParameter("@員工編號",  SqlDbType.VarChar, 50),
                	new SqlParameter("@員工姓名",  SqlDbType.VarChar, 50),
                	new SqlParameter("@身份證號",  SqlDbType.VarChar, 50),
                    new SqlParameter("@聯繫電話",  SqlDbType.VarChar, 50)
			};

                number = "123";
                name = "david";
                id = "A123456789";
                phone = "0912345678";

                prams[0].Value = number;
                prams[1].Value = name;
                prams[2].Value = id;
                prams[3].Value = phone;
                // 依次把參數傳入命令文字
                foreach (SqlParameter parameter in prams)
                {
                    cmd.Parameters.Add(parameter);
                }
                cmd.ExecuteNonQuery();
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //show
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_stu";

            sql_read_database(db_filename, sqlstr, dataGridView1);

            /*
            //複雜的模式查詢
            string student_id = "2";  // 學生編號
            string student_name = "王";  // 學生姓名
            string student_age = "1";  // 學生年齡

            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_stu WHERE 學生編號 LIKE '"
            + student_id + "%' AND (( 學生姓名 LIKE '"
            + student_name + "_') OR (年齡 LIKE '[^"
            + student_age + "][0-9]'))";

            sql_read_database(db_filename, sqlstr, dataGridView1);            
            */
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //having語句運用在多表查詢中

            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM 部門工資統計表";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //統計
            //having語句運用在多表查詢中

            // 查詢字串
            sqlstr = "SELECT 部門工資統計表.所屬部門, MAX(部門工資統計表.基本工資) AS 部門最高工資,SUM(員工請假表.請假天數) AS 合計請假天數, AVG(員工請假表.扣除金額) AS 平均扣除金額 FROM 部門工資統計表 INNER JOIN 員工請假表 ON 部門工資統計表.員工編號 = 員工請假表.員工編號 GROUP BY 部門工資統計表.所屬部門 HAVING (SUM(員工請假表.請假天數) < 10)";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用having語句過濾分組數據
            /*
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM 部門工資統計表";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            */
            richTextBox1.Text += "------------------------------\n";  // 30個

            // 查詢字串
            sqlstr = "SELECT DISTINCT 所屬部門, COUNT(*) AS 部門人數, MAX(基本工資) AS 最高工資, AVG(基本工資) AS 平均工資 FROM 部門工資統計表 GROUP BY 所屬部門 HAVING (AVG(基本工資) > 1000)";

            //按部門計算平均工資
            //工資統計
            //利用having語句過濾分組數據

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Score";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //同時利用OR、AND進行查詢
            //查詢數學成績大於90分或者音樂成績大於90分同時還得滿足英語成績大於90分的學生訊息。
            // 查詢字串
            sqlstr = "SELECT * FROM tb_Score WHERE (Math_Score>90 OR Music_Score>90) AND English_Score>90 ";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            /*
            da.Fill(ds, "book");  // da將查詢的結果填充至數據集ds, 指定TableName為"book"
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用OR進行查詢
            //查詢數學成績或英語成績大於９５分的學生訊息
            // 查詢字串
            sqlstr = "SELECT * FROM tb_Score WHERE Math_Score>95 OR English_Score>95";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            //da.Fill(ds, "book");  // da將查詢的結果填充至數據集ds, 指定TableName為"book"

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用AND進行查詢
            //查詢英語成績或數學成績都大於90的學生訊息
            // 查詢字串
            sqlstr = "SELECT * FROM tb_Score WHERE Math_Score>90 AND English_Score>90";
            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //靜態/動態 交叉表 查詢

            //靜態 交叉表 查詢

            /*
            //show
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM 銷售表";
            
            sql_read_database(db_filename, sqlstr, dataGridView1);
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //靜態交叉表

            //銷售業績分析

            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "xxxx";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //按員工姓名分析
                // 查詢字串
                sqlstr = "SELECT 所在部門, SUM(CASE 員工姓名 WHEN '李金明' THEN 銷售業績 ELSE NULL END)AS [李金明],SUM(CASE 員工姓名 WHEN '周可人' THEN 銷售業績 ELSE NULL END)as [周可人] ,SUM(CASE 員工姓名 WHEN '韓運' THEN 銷售業績 ELSE NULL END)AS [韓運],SUM(CASE 員工姓名 WHEN '司徒南' THEN 銷售業績 ELSE NULL END)AS [司徒南],SUM(CASE 員工姓名 WHEN '史佳金' THEN 銷售業績 ELSE NULL END)AS [史佳金]  FROM 銷售表 GROUP BY 所在部門";
                //SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                //按部門分析
                // 查詢字串
                sqlstr = "SELECT 員工姓名, SUM(CASE 所在部門 WHEN '食品部' THEN 銷售業績 ELSE NULL END) AS [食品部業績],SUM(CASE 所在部門 WHEN '家電部' THEN 銷售業績 ELSE NULL END) AS [家電部業績] FROM 銷售表 GROUP BY 員工姓名";
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = ds.Tables[0].DefaultView;  // DGV設置數據源
            }

            /*
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM 銷售表";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            */
            richTextBox1.Text += "------------------------------\n";  // 30個

            // 查詢字串
            //tmp string sqlstr = "SELECT DISTINCT 所屬部門, COUNT(*) AS 部門人數, MAX(基本工資) AS 最高工資, AVG(基本工資) AS 平均工資 FROM 部門工資統計表 GROUP BY 所屬部門 HAVING (AVG(基本工資) > 1000)";

            /*
            //動態 交叉表 查詢
            // 查詢字串
            string sqlstr = "Corss";
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
            SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
            da.SelectCommand.CommandType = CommandType.StoredProcedure;  // ????
            DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            da.Fill(ds, "table");  // da將查詢的結果填充至數據集ds, 指定TableName為"table"
            dataGridView1.DataSource = ds.Tables[0].DefaultView;  // DGV設置數據源
            }
            */
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //用子查詢作表達式
            /*
            //show
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Stud";
            
            sql_read_database(db_filename, sqlstr, dataGridView1);
            */

            //用子查詢作表達式

            //查詢 計算機 課程的平均成績

            string course = "計算機";

            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT distinct (SELECT AVG(成績) FROM tb_Stud  WHERE 課程='" + course + "') as 平均成績  FROM tb_Stud ";

            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                richTextBox1.Text += "查詢 計算機 課程的平均成績 : " + ds.Tables[0].Rows[0][0].ToString() + "\n";
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //查詢庫存數量占後20%的圖書訊息

            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_kcb";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //對數據進行降序查詢
            //查詢圖書訊息並按現存數量降序排序
            // 查詢字串
            sqlstr = "SELECT distinct 書號,書名,作者,出版社,現存數量 FROM tb_kcb order by 現存數量 desc ";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢庫存數量占後20%的圖書訊息
            // 查詢字串
            sqlstr = "SELECT top 20 percent * FROM tb_kcb order by 現存數量 asc";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢前10名數據
            // 查詢字串
            sqlstr = "SELECT top 10* FROM tb_kcb order by 現存數量 desc";
            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //使用COMPUTE BY
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM 工資表";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用COMPUTE BY
            // 查詢字串
            sqlstr = "SELECT * FROM 工資表 order by 所屬部門 compute sum(工資) by 所屬部門";

            // some error
            sql_read_database(db_filename, sqlstr, dataGridView1);

            //richTextBox1.Text += "ASP部門工資統計：" + ds.Tables[1].Rows[0][0].ToString() + "\n";
            //richTextBox1.Text += "設計部門工資統計：" + ds.Tables[3].Rows[0][0].ToString() + "\n";
            //richTextBox1.Text += "檔案部門工資統計：" + ds.Tables[5].Rows[0][0].ToString() + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用COMPUTE
            //利用COMPUTE子句對工資表中全部員工的工資情況進行匯總

            // 查詢字串
            sqlstr = "SELECT * FROM 工資表 order by 所屬部門 compute sum(工資)";
            // some error
            sql_read_database(db_filename, sqlstr, dataGridView1);

            //richTextBox1.Text += ds.Tables[1].Rows[0][0].ToString();

            richTextBox1.Text += "------------------------------\n";  // 30個

            //在分組查詢中使用ROLLUP

            // 查詢字串
            sqlstr = "SELECT 所屬部門,性別, avg(工資) as 平均工資 FROM 工資表 group by 所屬部門,性別 with ROLLUP";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //在分組查詢中使用CUBE運算符
            // 查詢字串
            sqlstr = "SELECT 所屬部門,性別,avg(工資)as 平均工資 FROM 工資表 group by 所屬部門,性別 with cube";
            sql_read_database(db_filename, sqlstr, dataGridView1);


        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //聚合函數MIN/COUNT

            //聚合函數大全

            /*
            //show
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_sell";
            
            sql_read_database(db_filename, sqlstr, dataGridView1);
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用聚合函數MIN求銷售額、利潤最少的商品

            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "xxxx";

            //查詢銷售額最少的商品訊息
            // 查詢字串
            sqlstr = "SELECT * FROM tb_sell WHERE 銷價 IN(SELECT min(銷價) FROM tb_sell)";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            //查詢利潤最少的商品訊息
            // 查詢字串
            sqlstr = "SELECT * FROM tb_sell WHERE 利潤 IN(SELECT min(利潤) FROM tb_sell)";
            sql_read_database(db_filename, sqlstr, dataGridView2);


            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用聚合函數COUNT求日銷售額大於某值的商品數
            /*
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            string sqlstr = "SELECT count(distinct 日期) as 商品數 FROM tb_sell WHERE 銷價 >500";
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
            SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
            DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName

            richTextBox1.Text += "查詢日銷售額大於５００的銷售商品種數：" + ds.Tables[0].Rows[0][0].ToString() + "\n";
            }
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 資料庫檔案
            //string db_filename = "db_10_Data.MDF";
            // 查詢字串
            sqlstr = "SELECT * FROM tb_sellInfo";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用聚合函數MAX求月銷售額完成最多的員工
            //查詢銷售額最多的員工及相關訊息
            // 查詢字串
            sqlstr = "SELECT * FROM tb_sellInfo WHERE 銷售額 IN(SELECT max(銷售額) FROM tb_sellInfo)";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_stu";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            */
            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用聚合函數AVG求某班學生的平均年齡
            //統計
            // 查詢字串
            sqlstr = "SELECT avg(年齡) as 平均年齡 FROM tb_stu";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            //richTextBox1.Text += "學生平均年齡 : " + ds.Tables[0].Rows[0][0].ToString() + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用變數查詢字串數據
            string MyStr = "武梅";
            // 查詢字串
            sqlstr = "SELECT * FROM tb_stu WHERE 學生姓名='" + MyStr + "'";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用變數查詢數值型數據
            int MyInt = 23;
            // 查詢字串
            sqlstr = "SELECT * FROM tb_stu WHERE 年齡='" + MyInt + "'";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_xsb";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            */
            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用聚合函數SUM對銷售額進行匯總
            //圖書銷售統計
            // 查詢字串
            sqlstr = "SELECT sum(銷售數量) as 總數量 ,sum(金額) as 總金額 FROM tb_xsb";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            //richTextBox1.Text += "銷售總數量：" + ds.Tables[0].Rows[0][0].ToString() + "\n";
            //richTextBox1.Text += "銷售總金額：" + ds.Tables[0].Rows[0][1].ToString() + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //對統計結果進行排序
            //對圖書銷售數量前五名的書籍按降序排序
            // 查詢字串
            sqlstr = "SELECT top 5 書號,書名,作者,出版社,sum(銷售數量) as 合計銷售數量 FROM tb_xsb  group by 書號,書名,作者,出版社  order by 5 desc";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //對數據進行多條件排序
            //查詢圖書訊息，按序號升序排序並日期降序排序
            // 查詢字串
            sqlstr = "SELECT distinct 書號,書名,作者,銷售數量,日期 FROM tb_xsb order by 書號 asc,日期 desc ";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //da.Fill(ds, "book");  // da將查詢的結果填充至數據集ds, 指定TableName為"book"

            richTextBox1.Text += "------------------------------\n";  // 30個

            //列出數據中的重複記錄和記錄條數
            //查詢已銷售圖書情況
            // 查詢字串
            sqlstr = "SELECT Count(書號)as 記錄條數, 書號,書名,作者 FROM tb_xsb group by 書號,書名,作者 Having Count(書號)>1";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            //da.Fill(ds, "book");  // da將查詢的結果填充至數據集ds, 指定TableName為"book"

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢銷售量占前50%的圖書訊息
            // 查詢字串
            sqlstr = "SELECT top 50 percent 書號,書名,sum(銷售數量)as 合計銷售數量 FROM tb_xsb group by 書號,書名,作者 order by 3 desc";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //取出數據統計結果後10名數據//設定統計查詢的SQL語句
            // 查詢字串
            sqlstr = "SELECT top 10 書號,書名,sum(銷售數量)as 合計銷售數量 FROM tb_xsb group by 書號,書名,作者 order by 3 asc";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT distinct 書號,條形碼,書名,作者,出版社 FROM tb_xsb";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            */
            //da.Fill(ds, "book");  // da將查詢的結果填充至數據集ds, 指定TableName為"book"

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢時不顯示重複記錄
            //查詢已銷售圖書情況

            // 查詢字串
            sqlstr = "SELECT distinct 書號,條形碼,書名,作者,出版社 FROM tb_xsb";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            //da.Fill(ds, "book");  // da將查詢的結果填充至數據集ds, 指定TableName為"book"

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            //數據分組統計（單列）
            //庫存圖書按出版社統計圖書庫存金額，並按金額降序排序。
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT 出版社,sum(金額) as 合計金額 FROM tb_xsb group by 出版社 order by 2 desc";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            */
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


/*
            //取得數據庫中的全部使用者圖示
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT name as 圖示名稱,crdate as 建立日期,refDate as 最後修改時間 FROM sysobjects";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";

            //改顯示欄位名稱AS
            // 查詢字串
            //string sqlstr = "SELECT name as 觸發器名稱,crdate as 建立時間,refdate as 最後一次修改時間 FROM sysobjects";
            string sqlstr = "SELECT * FROM sysobjects";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            dataGridView1.Columns[0].Width = 150;//設置欄位寬度
            dataGridView1.Columns[1].Width = 150;//設置欄位寬度
            dataGridView1.Columns[2].Width = 150;//設置欄位寬度

*/