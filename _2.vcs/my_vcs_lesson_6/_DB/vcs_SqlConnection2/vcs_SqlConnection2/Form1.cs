using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;  // for SqlConnection, SqlCommand, SqlDataAdapter

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
            button30.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            dataGridView1.Size = new Size(620, 400);
            dataGridView1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            dataGridView2.Size = new Size(620, 400);
            dataGridView2.Location = new Point(x_st + dx * 4, y_st + dy * 6);

            richTextBox1.Size = new Size(380, 800);
            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1920, 910);
            this.Text = "vcs_SqlConnection2";

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
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter(cmd_name, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //取得數據庫中全部的預儲程序
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select name as 預儲程序名稱,crdate as 建立時間,refdate as 最後一次修改時間 from sysobjects where xtype ='p'", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //取得數據庫中的觸發器

            string db_filename = "db_10_Data.MDF";
            string cmd_name = "select name as 觸發器名稱,crdate as 建立時間,refdate as 最後一次修改時間 from sysobjects where xtype ='TR'";
            show_database(db_filename, cmd_name);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            /*
            //取得資料庫的內容
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM 員工訊息表", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            //運用查詢預儲程序
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("getEmployeeOrName", cn);
            dap.SelectCommand.CommandType = CommandType.StoredProcedure;  // ????
            SqlParameter prams = new SqlParameter("@員工姓名", SqlDbType.VarChar, 50);
            prams.Value = "李丹";
            // 依次把參數傳入命令文字
            dap.SelectCommand.Parameters.Add(prams);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            /*
            //取得資料庫的內容
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM 員工訊息表", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            //運用預儲程序刪除數據
            SqlConnection cn = new SqlConnection(cnstr);
            cn.Open();
            SqlCommand cmd = new SqlCommand("procDeleteEmployee", cn);
            cmd.CommandType = CommandType.StoredProcedure;  // ????
            SqlParameter pares = new SqlParameter("@員工編號", SqlDbType.VarChar, 50);
            cmd.Parameters.Add(pares);
            cmd.Parameters["@員工編號"].Value = "12345";
            cmd.ExecuteNonQuery();
            cn.Close();

            //再取得資料庫的內容
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //運用預儲程序

            string db_filename = "db_10_Data.MDF";

            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("getAllEmployee", cn);
            dap.SelectCommand.CommandType = CommandType.StoredProcedure;  // ????
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //取得數據庫中的全部使用者圖示
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "select name as 圖示名稱,crdate as 建立日期,refDate as 最後修改時間 from sysobjects where xtype='v'";
            show_database(db_filename, cmd_name);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //通配符大全

            //show
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_stu", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用[]通配符進行查詢

            int age_like = 3;
            cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            cn = new SqlConnection(cnstr);
            dap = new SqlDataAdapter("select * from tb_stu where 年齡 like '" + age_like.ToString() + "[0-9]'", cn);
            ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            //show
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_stu", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用[^]通配符進行查詢

            //利用[^]通配符進行查詢年齡：
            /*
            string student_age = "2";

            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_stu where 年齡 like '[^" + student_age + "][0-9]'", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            /*
            //show
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_stu", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用%通配符進行查詢

            /*
            //請輸入學生編號：
            string student_id = "3";

            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_stu where 學生編號 like '%" + student_id + "%'", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //用IN查詢表中的記錄訊息

            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM 明細工資表";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢
            string number = "4";  // 員工編號
            cmd_name = "SELECT * FROM 明細工資表 WHERE (員工編號 IN (" + number + "))";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用外連接進行多表聯合查詢
            cmd_name = "SELECT 員工訊息表.序號, 員工訊息表.員工編號, 員工訊息表.員工姓名, 明細工資表.薪資編號, 明細工資表.月份, 明細工資表.基本工資, 明細工資表.獎金, 員工請假表.請假天數, 員工請假表.扣除金額 FROM 員工訊息表 LEFT OUTER JOIN 明細工資表 ON 員工訊息表.員工編號 = 明細工資表.員工編號 LEFT OUTER JOIN 員工請假表 ON 員工訊息表.員工編號 = 員工請假表.員工編號 ";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用右外連接查詢數據
            //RightOuterJoin

            cmd_name = "SELECT 明細工資表.編號, 明細工資表.薪資編號, 員工訊息表.員工編號, 明細工資表.基本工資, 明細工資表.獎金, 員工訊息表.員工姓名, 員工訊息表.身份證號 FROM 員工訊息表 RIGHT OUTER JOIN 明細工資表 ON 員工訊息表.員工編號 = 明細工資表.員工編號";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用左外連接查詢數據
            cmd_name = "SELECT 員工訊息表.序號, 員工訊息表.員工編號, 員工訊息表.員工姓名, 明細工資表.月份, 明細工資表.基本工資, 明細工資表.獎金 FROM 員工訊息表 LEFT OUTER JOIN 明細工資表 ON 員工訊息表.員工編號 = 明細工資表.員工編號";
            show_database(db_filename, cmd_name);

        }

        private void button8_Click(object sender, EventArgs e)
        {
            //Insert觸發器的運用
            /*
            //show
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from 員工工資表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 員工訊息註冊

            //Insert觸發器的運用
            string number = "123";
            string name = "david";
            string id = "A123456789";
            string phone = "0912345678";

            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            SqlCommand cmd = new SqlCommand("insert into 員工訊息表 (員工編號,員工姓名,身份證號,聯繫電話) values ('" + number + "','" + name + "','" + id + "','" + phone + "')", con);
            cmd.ExecuteNonQuery();
            con.Close();
            MessageBox.Show("數據新增成功！");

            richTextBox1.Text += "------------------------------\n";  // 30個

            //運用預儲程序新增數據
            /*
            //show
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from 員工訊息表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //運用預儲程序新增數據

            //員工基本訊息註冊
            /*
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            SqlCommand cmd = new SqlCommand("procInsertEmployee", con);
            cmd.CommandType = CommandType.StoredProcedure;
            SqlParameter[] prams = {
						new SqlParameter("@員工編號",  SqlDbType.VarChar, 50),
                		new SqlParameter("@員工姓名",  SqlDbType.VarChar, 50),
                		new SqlParameter("@身份證號",  SqlDbType.VarChar, 50),
                        new SqlParameter("@聯繫電話",  SqlDbType.VarChar, 50) 
			};

            string number = "123";
            string name = "david";
            string id = "A123456789";
            string phone = "0912345678";

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
            con.Close();
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //運用預儲程序修改數據

            /*
            //show
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from 員工訊息表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            /*
            //運用預儲程序修改數據

            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            SqlCommand cmd = new SqlCommand("procUpdateEmployee", con);
            cmd.CommandType = CommandType.StoredProcedure;
            SqlParameter[] prams = {
			        new SqlParameter("@員工編號",  SqlDbType.VarChar, 50),
                	new SqlParameter("@員工姓名",  SqlDbType.VarChar, 50),
                	new SqlParameter("@身份證號",  SqlDbType.VarChar, 50),
                    new SqlParameter("@聯繫電話",  SqlDbType.VarChar, 50)
			};

            string number = "123";
            string name = "david";
            string id = "A123456789";
            string phone = "0912345678";

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
            */

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //查詢邏輯型數據
            //查詢是否為國家統招學生：
            string select_type = "是";  // "是/否"

            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM tb_08 WHERE 統招否='" + select_type + "'", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //having語句運用在多表查詢中

            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM 部門工資統計表";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //統計
            //having語句運用在多表查詢中

            cmd_name = "SELECT 部門工資統計表.所屬部門, MAX(部門工資統計表.基本工資) AS 部門最高工資,SUM(員工請假表.請假天數) AS 合計請假天數, AVG(員工請假表.扣除金額) AS 平均扣除金額 FROM 部門工資統計表 INNER JOIN 員工請假表 ON 部門工資統計表.員工編號 = 員工請假表.員工編號 GROUP BY 部門工資統計表.所屬部門 HAVING (SUM(員工請假表.請假天數) < 10)";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用having語句過濾分組數據
            /*
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM 部門工資統計表";
            show_database(db_filename, cmd_name);
            */
            richTextBox1.Text += "------------------------------\n";  // 30個

            cmd_name = "SELECT DISTINCT 所屬部門, COUNT(*) AS 部門人數, MAX(基本工資) AS 最高工資, AVG(基本工資) AS 平均工資 FROM 部門工資統計表 GROUP BY 所屬部門 HAVING (AVG(基本工資) > 1000)";

            //按部門計算平均工資
            //工資統計
            //利用having語句過濾分組數據
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter(cmd_name, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM tb_Score";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //同時利用OR、AND進行查詢
            //查詢數學成績大於90分或者音樂成績大於90分同時還得滿足英語成績大於90分的學生訊息。
            cmd_name = "SELECT * FROM tb_Score where (Math_Score>90 or Music_Score>90) and English_Score>90 ";
            show_database(db_filename, cmd_name);

            /*
            dap.Fill(ds, "book");  //test use "book"
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用OR進行查詢
            //查詢數學成績或英語成績大於９５分的學生訊息
            cmd_name = "SELECT * FROM tb_Score where Math_Score>95 or English_Score>95";
            show_database(db_filename, cmd_name);

            //dap.Fill(ds, "book");  //test use "book"

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用AND進行查詢
            //查詢英語成績或數學成績都大於90的學生訊息
            cmd_name = "SELECT * FROM tb_Score where Math_Score>90 and English_Score>90";
            show_database(db_filename, cmd_name);

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //靜態/動態 交叉表 查詢

            //靜態 交叉表 查詢

            /*
            //show
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM 銷售表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //靜態交叉表

            //銷售業績分析

            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);

            //按員工姓名分析
            //SqlDataAdapter dap = new SqlDataAdapter("SELECT 所在部門, SUM(CASE 員工姓名 WHEN '李金明' THEN 銷售業績 ELSE NULL END)AS [李金明],SUM(CASE 員工姓名 WHEN '周可人' THEN 銷售業績 ELSE NULL END)as [周可人] ,SUM(CASE 員工姓名 WHEN '韓運' THEN 銷售業績 ELSE NULL END)AS [韓運],SUM(CASE 員工姓名 WHEN '司徒南' THEN 銷售業績 ELSE NULL END)AS [司徒南],SUM(CASE 員工姓名 WHEN '史佳金' THEN 銷售業績 ELSE NULL END)AS [史佳金]  FROM 銷售表 GROUP BY 所在部門", con);

            //按部門分析
            SqlDataAdapter dap = new SqlDataAdapter("SELECT 員工姓名, SUM(CASE 所在部門 WHEN '食品部' THEN 銷售業績 ELSE NULL END) AS [食品部業績],SUM(CASE 所在部門 WHEN '家電部' THEN 銷售業績 ELSE NULL END) AS [家電部業績] FROM 銷售表 GROUP BY 員工姓名", con);

            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;

            /*
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM 銷售表";
            show_database(db_filename, cmd_name);
            */
            richTextBox1.Text += "------------------------------\n";  // 30個

            //tmp string cmd_name = "SELECT DISTINCT 所屬部門, COUNT(*) AS 部門人數, MAX(基本工資) AS 最高工資, AVG(基本工資) AS 平均工資 FROM 部門工資統計表 GROUP BY 所屬部門 HAVING (AVG(基本工資) > 1000)";

            //動態 交叉表 查詢
            /*
            //動態交叉表查詢
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("Corss", cn);
            dap.SelectCommand.CommandType = CommandType.StoredProcedure;  // ????
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //使用內連接選擇一個表與另一個表中行相關的所有行
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT 員工訊息表.員工編號, 員工訊息表.員工姓名 FROM 員工訊息表 INNER JOIN 員工工資表 ON 員工訊息表.員工編號 = 員工工資表.員工編號";
            show_database(db_filename, cmd_name);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //複雜內連接查詢
            //員工訊息表、員工工資表和加班訊息表中，使用內連接查詢出加班員工的基本訊息。
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT 員工訊息表.員工編號, 員工訊息表.員工姓名, 員工工資表.基本工資, 加班訊息表.加班天數, 加班訊息表.加班費 FROM 員工訊息表 INNER JOIN 加班訊息表 ON 員工訊息表.員工編號 = 加班訊息表.員工編號 INNER JOIN 員工工資表 ON 加班訊息表.員工編號 = 員工工資表.員工編號";
            show_database(db_filename, cmd_name);
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //對聯合查詢後的結果進行排序

            string db_filename = "db_10_Data.MDF";

            //降序排序
            //string cmd_name = "SELECT cast(成績 AS varchar(20)) AS 成績 FROM 學生成績表 UNION SELECT DISTINCT 課程編號 FROM 學生訊息表 UNION SELECT 課程名稱 FROM 課程表 WHERE 課程名稱 = '計算機英語' UNION SELECT CONVERT(varchar(20), 出勤率) FROM 學生考勤表 WHERE 出勤率 > 0.8 ORDER BY 成績 DESC";

            //升序排序
            string cmd_name = "SELECT cast(成績 AS varchar(20)) AS 成績 FROM 學生成績表 UNION SELECT DISTINCT 課程編號 FROM 學生訊息表 UNION SELECT 課程名稱 FROM 課程表 WHERE 課程名稱 = '計算機英語' UNION SELECT CONVERT(varchar(20), 出勤率) FROM 學生考勤表 WHERE 出勤率 > 0.8";

            show_database(db_filename, cmd_name);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //多表聯合查詢
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "select 姓名 From 學生訊息表 UNION select 課程名稱 From 課程表 where 課程名稱='計算機英語' UNION select convert(varchar(20),成績) from 學生成績表 where 成績 > 90 UNION Select convert(varchar(20),出勤率) From 學生考勤表 where 出勤率 > 0.8";
            show_database(db_filename, cmd_name);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //用子查詢作派生的表
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM tb_Stu";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //顯示學生編號排在前10位，而且具有相同名字的學生個數
            cmd_name = "SELECT 學生姓名, count(*) AS 相同數量 FROM (SELECT top 10 學生姓名 FROM tb_Stu order BY 學生編號 asc )as T GROUP BY 學生姓名";
            show_database(db_filename, cmd_name);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM 工資數據表, 部門表";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //複雜內嵌查詢
            //查詢學歷是本科的部門經理的2005年10月份的工資情況
            cmd_name = "SELECT * FROM 工資數據表 where 工資月份=10 and 人員姓名 in( select 負責人 from 部門表 where 負責人 in(select 人員姓名 from 人員表 where 學歷='本科')) order by 人員編號";
            show_database(db_filename, cmd_name);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //聚合函數MIN/COUNT

            //聚合函數大全

            /*
            //show
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_sell", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用聚合函數MIN求銷售額、利潤最少的商品

            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);

            //查詢銷售額最少的商品訊息
            //SqlDataAdapter dap = new SqlDataAdapter("select * from tb_sell where 銷價 in(select min(銷價) from tb_sell)", cn);

            //查詢利潤最少的商品訊息
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_sell where 利潤 in(select min(利潤) from tb_sell)", cn);

            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用聚合函數COUNT求日銷售額大於某值的商品數
            /*
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select count(distinct 日期) as 商品數 from tb_sell where 銷價 >500", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);

            richTextBox1.Text += "查詢日銷售額大於５００的銷售商品種數：" + ds.Tables[0].Rows[0][0].ToString() + "\n";
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM tb_sellInfo";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用聚合函數MAX求月銷售額完成最多的員工
            //查詢銷售額最多的員工及相關訊息
            cmd_name = "SELECT * FROM tb_sellInfo where 銷售額 in(select max(銷售額) from tb_sellInfo)";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM tb_stu";
            show_database(db_filename, cmd_name);
            */
            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用聚合函數AVG求某班學生的平均年齡
            //統計
            cmd_name = "select avg(年齡) as 平均年齡 from tb_stu";
            show_database(db_filename, cmd_name);

            //richTextBox1.Text += "學生平均年齡 : " + ds.Tables[0].Rows[0][0].ToString() + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用變數查詢字串數據
            string MyStr = "武梅";
            cmd_name = "SELECT * FROM tb_stu where 學生姓名='" + MyStr + "'";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用變數查詢數值型數據
            int MyInt = 23;
            cmd_name = "SELECT * FROM tb_stu where 年齡='" + MyInt + "'";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM tb_xsb";
            show_database(db_filename, cmd_name);
            */
            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用聚合函數SUM對銷售額進行匯總
            //圖書銷售統計
            cmd_name = "select sum(銷售數量) as 總數量 ,sum(金額) as 總金額 from tb_xsb";
            show_database(db_filename, cmd_name);

            //richTextBox1.Text += "銷售總數量：" + ds.Tables[0].Rows[0][0].ToString() + "\n";
            //richTextBox1.Text += "銷售總金額：" + ds.Tables[0].Rows[0][1].ToString() + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //對統計結果進行排序
            //對圖書銷售數量前五名的書籍按降序排序
            cmd_name = "select top 5 書號,書名,作者,出版社,sum(銷售數量) as 合計銷售數量 from tb_xsb  group by 書號,書名,作者,出版社  order by 5 desc";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //對數據進行多條件排序
            //查詢圖書訊息，按序號升序排序並日期降序排序
            cmd_name = "select distinct 書號,書名,作者,銷售數量,日期 from tb_xsb order by 書號 asc,日期 desc ";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //dap.Fill(ds, "book");  //test use "book"

            richTextBox1.Text += "------------------------------\n";  // 30個

            //列出數據中的重複記錄和記錄條數
            //查詢已銷售圖書情況
            cmd_name = "select Count(書號)as 記錄條數, 書號,書名,作者 from tb_xsb group by 書號,書名,作者 Having Count(書號)>1";
            show_database(db_filename, cmd_name);

            //dap.Fill(ds, "book");  //test use "book"

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢銷售量占前50%的圖書訊息
            cmd_name = "select top 50 percent 書號,書名,sum(銷售數量)as 合計銷售數量 from tb_xsb group by 書號,書名,作者 order by 3 desc";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //取出數據統計結果後10名數據//設定統計查詢的SQL語句
            cmd_name = "select top 10 書號,書名,sum(銷售數量)as 合計銷售數量 from tb_xsb group by 書號,書名,作者 order by 3 asc";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "select distinct 書號,條形碼,書名,作者,出版社 from tb_xsb";
            show_database(db_filename, cmd_name);
            */
            //dap.Fill(ds, "book");  //test use "book"

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢時不顯示重複記錄
            //查詢已銷售圖書情況

            cmd_name = "select distinct 書號,條形碼,書名,作者,出版社 from tb_xsb";
            show_database(db_filename, cmd_name);

            //dap.Fill(ds, "book");  //test use "book"

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            //數據分組統計（單列）
            //庫存圖書按出版社統計圖書庫存金額，並按金額降序排序。
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "select 出版社,sum(金額) as 合計金額 from tb_xsb group by 出版社 order by 2 desc";
            show_database(db_filename, cmd_name);
            */
        }

        private void button20_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM tb_stu ,tb_mark";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //簡單內嵌查詢
            //查詢總分在５８０分以上的學生訊息

            cmd_name = "select distinct 學生姓名,學生編號, 性別,出生年月,年齡,所在學院,所學專業 from tb_stu where 學生姓名 in (select  學生姓名 from  tb_mark where 總分>=580)";
            show_database(db_filename, cmd_name);
        }

        private void button21_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM 顧客表, 僱員表";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //合併多個結果集
            //利用UNION運算符完成將顧客表和僱員表中的編號、姓名、地址、郵編字段合併到一個表中。
            cmd_name = "select 顧客編號 as 編號,顧客姓名 as 姓名,所在城市,郵編 from 顧客表 union select 僱員編號,僱員名稱,家庭住址,郵編 from 僱員表";
            show_database(db_filename, cmd_name);
        }

        private void button22_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM tb_stu,tb_mark";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用表別名
            //利用表的別名查詢計算機分院學生的成績
            //string db_filename = "db_10_Data.MDF";
            cmd_name = "select distinct S.學生編號,S.學生姓名,M.高數,M.外語,M.馬經,S.所在學院 from tb_stu as S,tb_mark as M where S.學生編號=M.學生編號 and S.所在學院='計算機學院'";
            show_database(db_filename, cmd_name);
        }

        private void button23_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM tb_stu s ,tb_mark";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //利用FROM子句進行多表查詢
            //查詢高數成績大於85分的學生的詳細訊息
            //string db_filename = "db_10_Data.MDF";
            cmd_name = "select  distinct s.學生編號,s.學生姓名,s.性別,s.出生年月,s.年齡,s.所在學院,s.所學專業,m.高數 from tb_stu s ,tb_mark m where s.學生編號=m.學生編號 and m.高數 >85";
            show_database(db_filename, cmd_name);
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //用子查詢作表達式
            /*
            //show
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select  * from tb_Stud", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            //用子查詢作表達式

            //查詢 計算機 課程的平均成績

            string course = "計算機";

            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select  distinct (select  AVG(成績) from tb_Stud  where 課程='" + course + "') as 平均成績  FROM tb_Stud ", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);

            richTextBox1.Text += "查詢 計算機 課程的平均成績 : " + ds.Tables[0].Rows[0][0].ToString() + "\n";
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM 工資表";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用COMPUTE BY
            cmd_name = "SELECT * FROM 工資表 order by 所屬部門 compute sum(工資) by 所屬部門";

            // some error
            show_database(db_filename, cmd_name);

            //richTextBox1.Text += "ASP部門工資統計：" + ds.Tables[1].Rows[0][0].ToString() + "\n";
            //richTextBox1.Text += "設計部門工資統計：" + ds.Tables[3].Rows[0][0].ToString() + "\n";
            //richTextBox1.Text += "檔案部門工資統計：" + ds.Tables[5].Rows[0][0].ToString() + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //使用COMPUTE
            //利用COMPUTE子句對工資表中全部員工的工資情況進行匯總

            cmd_name = "SELECT * FROM 工資表 order by 所屬部門 compute sum(工資)";
            // some error
            show_database(db_filename, cmd_name);

            //richTextBox1.Text += ds.Tables[1].Rows[0][0].ToString();

            richTextBox1.Text += "------------------------------\n";  // 30個

            //在分組查詢中使用ROLLUP

            cmd_name = "select 所屬部門,性別, avg(工資) as 平均工資 from 工資表 group by 所屬部門,性別 with ROLLUP";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //在分組查詢中使用CUBE運算符
            cmd_name = "select 所屬部門,性別,avg(工資)as 平均工資 from 工資表 group by 所屬部門,性別 with cube";
            show_database(db_filename, cmd_name);
        }

        private void button28_Click(object sender, EventArgs e)
        {
            //查詢字串
            //請輸入查詢院系名稱：
            //計算機

            string db_filename = "db_10_Data.MDF";
            string search_college = "計算機";
            string cmd_name = "SELECT * FROM tb_05 WHERE 所在院系 LIKE '%" + search_college + "%'";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            /*
            //查詢數字
            //查詢年齡為：23

            string db_filename = "db_10_Data.MDF";
            int age = 23;
            string cmd_name = "SELECT * FROM tb_05 WHERE 學生年齡=" + age.ToString();
            show_database(db_filename, cmd_name);
            */
        }

        private void button29_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM xsb";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //多表分組統計
            //查詢圖書的銷售數量和現存數量，並按書號、書名等分組
            cmd_name = "select k.書號,k.書名,x.作者, sum(k.現存數量)as 現存數量 ,sum(x.銷售數量)as 銷售數量 from xsb x ,kcb k where x.書號=k.書號  group by k.書號,k.書名,x.作者, k.現存數量 order by 1";
            show_database(db_filename, cmd_name);
        }

        private void button30_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM tb_rkb";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //按倉庫分組統計圖書庫存（多列）
            //按倉庫名、圖書名稱進行分組，並統計其庫存數量

            cmd_name = "select 存放位置,書名,sum(庫存數量) as 合計庫存數量  from tb_rkb group by 存放位置,書名 order by 1";
            show_database(db_filename, cmd_name);
        }

        private void button31_Click(object sender, EventArgs e)
        {
            //查詢特定數據列
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT 學生編號,學生姓名 FROM tb_01";
            show_database(db_filename, cmd_name);
        }

        private void button32_Click(object sender, EventArgs e)
        {
            //在列上加入計算
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT 產品編號,產品名稱,產品單價,產品數量,(產品數量*產品單價) AS 總金額 FROM tb_03";
            show_database(db_filename, cmd_name);
        }

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM tb_kcb";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //對數據進行降序查詢
            //查詢圖書訊息並按現存數量降序排序
            cmd_name = "select distinct 書號,書名,作者,出版社,現存數量 from tb_kcb order by 現存數量 desc ";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢庫存數量占後20%的圖書訊息
            cmd_name = "select top 20 percent * from tb_kcb order by 現存數量 asc";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢前10名數據
            cmd_name = "select top 10* from tb_kcb order by 現存數量 desc";
            show_database(db_filename, cmd_name);
        }

        private void button35_Click(object sender, EventArgs e)
        {
        }

        private void button36_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cmd_name = "SELECT * FROM tb_BookSell";
            show_database(db_filename, cmd_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //在分組查詢中使用ALL關鍵字
            //在圖書銷售表中對機械出版社出版的不同圖書的銷售情況進行統計，並列出其他出版社的圖書（不作統計）
            cmd_name = "select 書名,出版社,sum(金額) as 總計金額 from tb_BookSell where 出版社='機械' group by all 書名,出版社 ";
            show_database(db_filename, cmd_name);
        }

        private void button37_Click(object sender, EventArgs e)
        {
        }

        private void button38_Click(object sender, EventArgs e)
        {
        }

        private void button39_Click(object sender, EventArgs e)
        {
            /*
            //show
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_stu", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            */

            //複雜的模式查詢
            string student_id = "2";  // 學生編號
            string student_name = "王";  // 學生姓名
            string student_age = "1";  // 學生年齡

            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            string sqlstr = "select * from tb_stu where 學生編號 like '"
            + student_id + "%' and (( 學生姓名 like '"
            + student_name + "_') or (年齡 like '[^"
            + student_age + "][0-9]'))";
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter(sqlstr, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
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
似乎
dap.Fill(ds, "table"); 和 dap.Fill(ds); 是一樣的

 */
