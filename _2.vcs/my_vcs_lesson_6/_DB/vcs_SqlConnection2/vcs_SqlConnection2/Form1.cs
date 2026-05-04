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
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
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

            //運用預儲程序修改數據

            //show
            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);
            // 查詢字串
            sqlstr = "SELECT * FROM 員工訊息表";

            sql_read_database(db_filename, sqlstr, dataGridView1);
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

        // 以下為debug ----------------------------------------------------------------------------------------------------  # 100個

        private void button29_Click(object sender, EventArgs e)
        {
            return;
            // 以下為debug
            // 資料庫檔案
            string db_filename = "ddddddd.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM ddddddd";

            sql_read_database(db_filename, sqlstr, dataGridView1);
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

