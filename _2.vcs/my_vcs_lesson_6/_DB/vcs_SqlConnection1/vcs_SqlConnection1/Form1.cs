using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;  // for SqlConnection, SqlCommand, SqlDataAdapter

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

            this.Size = new Size(1910, 910);
            this.Text = "vcs_SqlConnection1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // 固定查詢
        private void ShowData3(string cnstr)
        {
            // DB => DS => dataGridView1
            using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

                string sqlstr = "SELECT * FROM 銀行帳戶";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "銀行帳戶");  // 將DataAdapter查詢之後的結果填充至DataSet

                dataGridView1.DataSource = ds.Tables["銀行帳戶"];
            }
        }

        // 指定查詢
        void ReadMDF(string cnstr, string table_name)
        {
            // DB => DS => dataGridView1
            using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

                string sqlstr = "SELECT * FROM " + table_name;  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, table_name);  // 將DataAdapter查詢之後的結果填充至DataSet

                dataGridView1.DataSource = ds.Tables[table_name];
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            string db_filename = "MyDB0.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 連接字串
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT * From 員工";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName

                dataGridView1.DataSource = ds.Tables[0];
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
                    cn.Open();  // 打開數據庫連線
                    SqlCommand cmd = new SqlCommand();
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
                MessageBox.Show(ex.Message);
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
                    cn.Open();  // 打開數據庫連線
                    SqlCommand cmd = new SqlCommand();
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
                MessageBox.Show(ex.Message);
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //刪除
            id = "A008";

            try
            {
                using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
                {
                    cn.Open();  // 打開數據庫連線
                    SqlCommand cmd = new SqlCommand();
                    cmd.CommandText = "DELETE FROM 員工 WHERE 員工編號=N'" + id + "'";
                    cmd.Connection = cn;
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string db_filename = "ch17DB.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 連接字串

            using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;
                cn.Open();  // 打開數據庫連線

                string sqlstr = "SELECT * FROM 員工";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "員工");  // 將DataAdapter查詢之後的結果填充至DataSet

                dataGridView1.DataSource = ds.Tables["員工"];

                richTextBox1.Text += "------------------------------\n";  // 30個

                SqlCommand cmdCount, cmdSum, cmdAvg, cmdMax, cmdMin;

                //取員工資料筆數
                cmdCount = new SqlCommand("SELECT COUNT(*) FROM 員工", cn);
                richTextBox1.Text += "員工資料表共 " + cmdCount.ExecuteScalar().ToString() + " 筆記錄\n";

                //取薪資加總
                cmdSum = new SqlCommand("SELECT SUM(薪資) FROM 員工", cn);
                richTextBox1.Text += "員工資料表薪資加總共 " + cmdSum.ExecuteScalar().ToString() + "\n";

                //取薪資平均
                cmdAvg = new SqlCommand("SELECT AVG(薪資) FROM 員工", cn);
                richTextBox1.Text += "員工資料表薪資平均為 " + cmdAvg.ExecuteScalar().ToString() + "\n";

                //取薪資最高薪
                cmdMax = new SqlCommand("SELECT Max(薪資) FROM 員工", cn);
                richTextBox1.Text += "最高薪為 " + cmdMax.ExecuteScalar().ToString() + "\n";

                //取薪資最低薪
                cmdMin = new SqlCommand("SELECT Min(薪資) FROM 員工", cn);
                richTextBox1.Text += "最低薪為 " + cmdMin.ExecuteScalar().ToString() + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //測試登錄功能

            string id_name = "david";
            string password = "123456";

            string db_filename = "db_TomeTwo.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 連接字串

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

        private void button3_Click(object sender, EventArgs e)
        {
            // 查询销售量占前50%的图书信息
            // 查询数据库信息

            //创建数据库连接字符串
            //string P_Str_ConnectionStr = string.Format(@"server=MR-PC\YL;database=db_TomeTwo;uid=sa;pwd=");
            //String P_Str_ConnectionStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            String P_Str_ConnectionStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

            //创建SQL查询字符串
            string sqlstr = string.Format("SELECT * FROM tb_Book");

            //创建数据适配器
            SqlDataAdapter da = new SqlDataAdapter(sqlstr, P_Str_ConnectionStr);  // 建立資料庫適配器對象da
            //SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);//compare    // 建立資料庫適配器對象da

            //创建数据表
            DataTable dt = new DataTable();

            da.Fill(dt);  // da將查詢的結果填充至數據集ds, 不指定TableName

            dataGridView1.DataSource = dt;//设置数据源

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 查询销售量占前50%的图书信息
            // 查询数据库信息

            //创建数据库连接字符串
            //string P_Str_ConnectionStr = string.Format(@"server=USER-20170504OU;database=db_TomeTwo;uid=sa;pwd=");
            //String P_Str_ConnectionStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            P_Str_ConnectionStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

            //创建SQL查询字符串
            sqlstr = string.Format(@"SELECT TOP 50 PERCENT 书号,书名,sum(销售数量)as 合计销售数量 FROM tb_Book group by 书号,书名,作者 order by 3 desc");

            //创建数据适配器
            da = new SqlDataAdapter(sqlstr, P_Str_ConnectionStr);  // 建立資料庫適配器對象da
            //SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);//compare    // 建立資料庫適配器對象da

            //创建数据表
            dt = new DataTable();

            da.Fill(dt);  // da將查詢的結果填充至數據集ds, 不指定TableName

            dataGridView1.DataSource = dt;//设置数据源
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //跳过满足指定条件的记录
            //跳过生日小于2009-7-1的员工:

            //string cnstr = "Data Source=USER-20170504OU;Database=db_TomeTwo;UID=sa;Pwd=;";//取连接字符串
            string db_filename = "db_TomeTwo.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 連接字串
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                string sql = "SELECT * from EmployeeInfo";//构造sql语句
                SqlCommand cmd = new SqlCommand(sql, cn);//创建Command对象

                SqlDataAdapter da = new SqlDataAdapter(cmd);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)

                da.Fill(ds, "EmployeeInfo");//填充数据集

                //跳过生日小于2009-7-1的员工信息
                IEnumerable<DataRow> query = ds.Tables["EmployeeInfo"].AsEnumerable().SkipWhile(itm => itm.Field<DateTime>("Birthday") < Convert.ToDateTime("2009-7-1"));
                dataGridView1.DataSource = query.CopyToDataTable();//设置dataGridView1数据源
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            // 轉帳
            // 連接字串
            string db_filename = "ch17DB.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 連接字串

            //轉帳

            string table_name = "銀行帳戶";
            ReadMDF(cnstr, table_name);

            richTextBox1.Text += "------------------------------\n";  // 30個

            using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
            {
                string src_ID = "A003";
                string dst_ID = "A004";
                int money = 500;

                // 連接資料庫
                cn.ConnectionString = cnstr;
                cn.Open();  // 打開數據庫連線

                // 建立SqlCommand物件selectCmd1，用來查詢使用者帳號是否存在
                SqlCommand selectCmd1 = new SqlCommand("SELECT * FROM 銀行帳戶 WHERE 帳號='" + src_ID + "'", cn);

                // 建立SqlCommand物件selectCmd1，用來查詢轉入帳號是否存在
                SqlCommand selectCmd2 = new SqlCommand("SELECT * FROM 銀行帳戶 WHERE 帳號='" + dst_ID + "'", cn);

                // 宣告SqlDataReader物件dr1與dr2
                SqlDataReader dr1, dr2;
                // 傳回SqlDataReader物件dr1，用來查詢使用者帳號是否存在
                dr1 = selectCmd1.ExecuteReader();
                if (!dr1.Read())   // 使用者帳號不存在執行下列敘述
                {
                    richTextBox1.Text += "你的帳號" + src_ID + "錯誤\n";
                    return;
                }

                // 取得使用者的餘額並定給myMoney
                int myMoney = int.Parse(dr1["餘額"].ToString());
                dr1.Close();  // 關閉SqlDataRader物件dr1

                // 傳回SqlDataReader物件dr2，用來查詢轉入帳號是否存在
                dr2 = selectCmd2.ExecuteReader();
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
                    SqlCommand updateCmd1 = new SqlCommand("UPDATE 銀行帳戶 SET 餘額=餘額-" + money + " WHERE 帳號='" + src_ID + "'", cn, tran);

                    // 設定轉入帳號匯款的SQL語法
                    SqlCommand updateCmd2 = new SqlCommand("UPDATE 銀行帳戶 SET 餘額=餘額+" + money + " WHERE 帳號='" + dst_ID + "'", cn, tran);

                    updateCmd1.ExecuteNonQuery();  // 執行SQL命令

                    //throw new Exception("電腦當機");

                    updateCmd2.ExecuteNonQuery();  // 執行SQL命令

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
            using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

                string sqlstr = "SELECT * FROM 員工 ORDER BY 編號 DESC";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "員工");  // 將DataAdapter查詢之後的結果填充至DataSet

                dataGridView1.DataSource = ds.Tables["員工"];
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //員工資料表1    讀取 新增 修改 刪除

            // 連接字串
            string db_filename = "ch17DB.mdf";
            string cnstr1 = string.Format(db_cnstr, db_filename);  // 連接字串

            ShowData1(cnstr1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增

            string name = "david";
            string position = "engineering";
            string telephone = "0912345678";
            int salary = 55555;

            try  //使用try...catch...敘述來補捉異動資料可能發生的例外 
            {
                using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
                {
                    // 連接資料庫
                    cn.ConnectionString = cnstr1;
                    cn.Open();  // 打開數據庫連線

                    /* same
                    string sqlStr = "INSERT INTO 員工(姓名, 職稱, 電話, 薪資) VALUES('" + name + "','" + position + "','" + telephone + "'," + salary + ")";
                    SqlCommand Cmd = new SqlCommand(sqlStr, cn);
                    Cmd.ExecuteNonQuery();  // 執行SQL命令
                    */

                    string sqlStr = "INSERT INTO 員工(姓名, 職稱, 電話, 薪資)" + "VALUES(@name, @position, @tel, @salary)";
                    SqlCommand cmd = new SqlCommand(sqlStr, cn);
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
                using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
                {
                    // 連接資料庫
                    cn.ConnectionString = cnstr1;
                    cn.Open();  // 打開數據庫連線

                    /* same
                    string sqlStr = "UPDATE 員工 SET 職稱 = '" + position2 + "',電話 = '" + telephone2 + "', 薪資 = " + salary2 + " WHERE 姓名 = '" + name + "'";
                    SqlCommand Cmd = new SqlCommand(sqlStr, cn);
                    Cmd.ExecuteNonQuery();  // 執行SQL命令
                    */
                    string sqlStr = "UPDATE 員工 SET 職稱=@position," + "電話=@tel, 薪資=@salary WHERE 姓名=@name";
                    SqlCommand cmd = new SqlCommand(sqlStr, cn);
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

            using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
            {
                // 連接資料庫
                cn.ConnectionString = cnstr1;
                cn.Open();  // 打開數據庫連線

                /* same
                string sqlStr = "DELETE FROM 員工 WHERE 姓名 = '" + name + "'";
                SqlCommand Cmd = new SqlCommand(sqlStr, cn);
                Cmd.ExecuteNonQuery();  // 執行SQL命令
                */
                string sqlStr = "DELETE FROM 員工 WHERE 姓名 = @name";
                SqlCommand cmd = new SqlCommand(sqlStr, cn);
                cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                cmd.Parameters["@name"].Value = name;
                cmd.ExecuteNonQuery();  // 執行SQL命令
            }
            ShowData1(cnstr1);
        }
        // 員工資料表1 SP

        private void button7_Click(object sender, EventArgs e)
        {
            //RelationsDemo
            string db_filename = "Northwind.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 連接字串

            using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
            {
                cn.ConnectionString = cnstr;

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)

                string sqlstr1 = "SELECT * FROM 產品類別";  // 宣告查詢字串
                SqlDataAdapter da1 = new SqlDataAdapter(sqlstr1, cn);  // 建立資料庫適配器對象da
                da1.Fill(ds, "產品類別");

                string sqlstr2 = "SELECT * FROM 產品資料";  // 宣告查詢字串
                SqlDataAdapter da2 = new SqlDataAdapter(sqlstr2, cn);  // 建立資料庫適配器對象da
                da2.Fill(ds, "產品資料");

                ds.Relations.Add("FK_產品資料_產品類別", ds.Tables["產品類別"].Columns["類別編號"], ds.Tables["產品資料"].Columns["類別編號"]);

                dataGridView1.DataSource = ds;
                dataGridView1.DataMember = "產品類別";

                dataGridView2.DataSource = ds;
                dataGridView2.DataMember = "產品類別.FK_產品資料_產品類別";
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
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
//string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";


