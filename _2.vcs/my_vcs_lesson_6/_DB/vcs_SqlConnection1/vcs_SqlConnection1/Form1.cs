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

            dataGridView1.Size = new Size(620, 400);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            dataGridView2.Size = new Size(620, 400);
            dataGridView2.Location = new Point(x_st + dx * 3, y_st + dy * 6);

            richTextBox1.Size = new Size(400, 800);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1720, 910);
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
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

                string sqlstr = "SELECT * FROM 銀行帳戶";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);

                DataSet ds = new DataSet();  // 建立DataSet來儲存Table
                da.Fill(ds, "銀行帳戶");  // 將DataAdapter查詢之後的結果填充至DataSet

                dataGridView1.DataSource = ds.Tables["銀行帳戶"];
            }
        }

        // 指定查詢
        void ReadMDF(string cnstr, string table_name)
        {
            // DB => DS => dataGridView1
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

                string sqlstr = "SELECT * FROM " + table_name;  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);

                DataSet ds = new DataSet();  // 建立DataSet來儲存Table
                da.Fill(ds, table_name);  // 將DataAdapter查詢之後的結果填充至DataSet

                dataGridView1.DataSource = ds.Tables[table_name];
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            // 資料庫連線參數, 連接字串
            String cnStr0 = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\MyDB0.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnStr0))
            {
                string sqlstr = "SELECT * From 員工";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);

                DataSet ds = new DataSet();  // 建立DataSet來儲存Table
                da.Fill(ds);  // 將DataAdapter查詢之後的結果填充至DataSet

                dataGridView1.DataSource = ds.Tables[0];

                richTextBox1.Text += "DataSet內容\n";
                int len = ds.Tables.Count;
                richTextBox1.Text += "表格個數 : " + len.ToString() + "\n";
                for (int i = 0; i < len; i++)
                {
                    richTextBox1.Text += "表格名稱 : " + ds.Tables[i].TableName + "\n";
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增

            string id = "A008";
            string name = "david";
            string sex = "男";
            int money = 12345;

            try
            {
                using (SqlConnection cn = new SqlConnection(cnStr0))
                {
                    cn.Open();
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
                using (SqlConnection cn = new SqlConnection(cnStr0))
                {
                    cn.Open();
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
                using (SqlConnection cn = new SqlConnection(cnStr0))
                {
                    cn.Open();
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
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;
                cn.Open();

                string sqlstr = "SELECT * FROM 員工";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);

                DataSet ds = new DataSet();  // 建立DataSet來儲存Table
                da.Fill(ds, "員工");  // 將DataAdapter查詢之後的結果填充至DataSet

                dataGridView1.DataSource = ds.Tables["員工"];

                //3030

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
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // 成績單1
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True";

            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

                cn.Open();

                SqlCommand cmd = new SqlCommand("SELECT * FROM 成績單", cn);

                SqlDataReader dr = cmd.ExecuteReader();
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    richTextBox1.Text += dr.GetName(i) + "\t";
                }
                richTextBox1.Text += "\n";

                while (dr.Read())
                {
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        richTextBox1.Text += dr[i].ToString() + "\t";
                        //richTextBox1.Text += dr.GetValue(i).ToString() + "\t";    //另法
                    }
                    richTextBox1.Text += "\n";
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            // 成績單2
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True";

            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

                cn.Open();

                SqlCommand cmd = new SqlCommand("SELECT * FROM 成績單", cn);

                SqlDataReader dr = cmd.ExecuteReader();
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    richTextBox1.Text += dr.GetName(i) + "\t";
                }
                richTextBox1.Text += "\n";

                while (dr.Read())
                {
                    richTextBox1.Text += dr["學號"].ToString() + "\t";
                    richTextBox1.Text += dr["姓名"].ToString() + "\t";
                    richTextBox1.Text += dr["國文"].ToString() + "\t";
                    richTextBox1.Text += dr["英文"].ToString() + "\t";
                    richTextBox1.Text += dr["數學"].ToString() + "\t";
                    richTextBox1.Text += "\n";

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
        }

        // 員工資料表1 ST

        private void ShowData1(string cnstr)
        {
            // DB => DS => dataGridView1
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

                string sqlstr = "SELECT * FROM 員工 ORDER BY 編號 DESC";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);

                DataSet ds = new DataSet();  // 建立DataSet來儲存Table
                da.Fill(ds, "員工");  // 將DataAdapter查詢之後的結果填充至DataSet

                dataGridView1.DataSource = ds.Tables["員工"];
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //員工資料表1    讀取 新增 修改 刪除

            // 資料庫連線參數, 連接字串
            string cnstr1 = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

            ShowData1(cnstr1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增

            string name = "david";
            string position = "engineering";
            string telephone = "0912345678";
            int salary = 55555;

            try  //使用try...catch...敘述來補捉異動資料可能發生的例外 
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    // 連接資料庫
                    cn.ConnectionString = cnstr1;
                    cn.Open();

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
                using (SqlConnection cn = new SqlConnection())
                {
                    // 連接資料庫
                    cn.ConnectionString = cnstr1;
                    cn.Open();

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

            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr1;
                cn.Open();

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
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\Northwind.mdf;Integrated Security=True";

            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;

                DataSet ds = new DataSet();

                string sqlstr1 = "SELECT * FROM 產品類別";  // 宣告查詢字串
                SqlDataAdapter da1 = new SqlDataAdapter(sqlstr1, cn);
                da1.Fill(ds, "產品類別");

                string sqlstr2 = "SELECT * FROM 產品資料";  // 宣告查詢字串
                SqlDataAdapter da2 = new SqlDataAdapter(sqlstr2, cn);
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
            //成績單3
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

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
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //成績單4
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

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
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //成績單 搜尋1

            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

            string name = "david";

            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;
                cn.Open();

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
                    richTextBox1.Text += "數學：" + dr["數學"].ToString();
                }
                else   // 若沒有該筆記錄則執行else下面敘述
                {
                    richTextBox1.Text += "找不到這個學生的成績！\n";
                }
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //成績單 搜尋2

            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

            string name = "david";

            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;
                cn.Open();

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
                    richTextBox1.Text += "數學：" + dr["數學"].ToString();
                }
                else   // 若沒有該筆記錄則執行else下面敘述
                {
                    richTextBox1.Text += "找不到這個學生的成績！\n";
                }
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            // 資料庫連線參數, 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\Northwind.mdf;Integrated Security=True";

            //tt1
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

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

                //關閉資料庫
                cn.Close();
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\Northwind.mdf;Integrated Security=True";
            //tt2
            using (SqlConnection cn = new SqlConnection())
            {
                DataSet ds = new DataSet();  // 建立DataSet來儲存Table

                // 連接資料庫
                cn.ConnectionString = cnstr;

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

                // 員工
                dataGridView1.DataSource = ds.Tables["員工"];

                // 客戶
                dataGridView2.DataSource = ds.Tables["客戶"];

                // 產品類別
                //dataGridView1.DataSource = ds.Tables["產品類別"];
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            // 資料庫連線參數, 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

            //轉帳

            string table_name = "銀行帳戶";
            ReadMDF(cnstr, table_name);

            //3030

            using (SqlConnection cn = new SqlConnection())
            {
                string src_ID = "A003";
                string dst_ID = "A004";
                int money = 500;

                // 連接資料庫
                cn.ConnectionString = cnstr;
                cn.Open();

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

        private void button17_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "aaaaaaaaaaaaaaa\n";
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch18DB.mdf;Integrated Security=True";

            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;

                string sqlstr = "SELECT * FROM 員工 ORDER BY 編號 DESC";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();
                da.Fill(ds, "員工");

                // DataGridView控制項資料繫結
                dataGridView1.DataSource = ds;
                dataGridView1.DataMember = "員工";
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //成績單+搜尋條件

            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch18DB.mdf;Integrated Security=True";

            DataView dv;  // 宣告DataView物件dv

            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;

                string sqlstr = "SELECT * FROM 成績單 ORDER BY 國文 DESC";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();
                da.Fill(ds, "成績單");
                dv = ds.Tables["成績單"].DefaultView;
            }
            dataGridView1.DataSource = dv;

            string filter = "國文>80";  // 篩選條件, 用WHRER語法
            string sort = "英文 DESC";  // 排序方法, 科目, ASC:遞增, DESC:遞減

            richTextBox1.Text += "篩選條件 : " + filter + "\n";
            richTextBox1.Text += "排序方法 : " + sort + "\n";

            dv.RowFilter = filter;
            dv.Sort = sort;

            dataGridView1.DataSource = dv;
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //tmp1
            using (SqlConnection cn = new SqlConnection())
            {
                DataSet ds = new DataSet();

                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;" +
                    @"AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch19DB.mdf;" +
                    "Integrated Security=True";
                SqlDataAdapter da = new SqlDataAdapter("SELECT * FROM 產品", cn);
                da.Fill(ds, "產品");
                dataGridView1.DataSource = ds.Tables["產品"];


                // 將ds物件的所有產品資料寫入product.xml檔
                ds.WriteXml("tmp_product.xml");
                MessageBox.Show("產品資料成功寫入product.xml檔內");
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //tmp2
            DataSet ds = new DataSet();
            ds.ReadXml("../../../../person.xml");  //將person.xml讀入至ds
            //建立學號為學生DataTable的主鍵
            DataColumn dc = ds.Tables["學生"].Columns["學號"];
            ds.Tables["學生"].Constraints.Add("PK_學號", dc, true);
            //DataRowCollection的Find方法搜尋txtSearchId主鍵資料
            string student_id = "9096003";
            DataRow dr = ds.Tables["學生"].Rows.Find(student_id);
            //判斷dr是否為null
            if (dr == null)
            {
                // 找不到學生記錄執行此處
                richTextBox1.Text = "沒有學號 " + student_id + " 的學生";
                return;
            }
            else
            {
                // 找到學生記錄執行此處
                richTextBox1.Text += "學號：" + dr["學號"] + Environment.NewLine;
                richTextBox1.Text += "姓名：" + dr["姓名"] + Environment.NewLine;
                richTextBox1.Text += "電話：" + dr["電話"] + Environment.NewLine;
                richTextBox1.Text += "信箱：" + dr["信箱"];
            }

        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch20DB.mdf;Integrated Security=True";

            //LINQ 1
            //建立DataSet物件ds，ds建立於所有事件處理函式之外以便所有事件一起共用
            DataSet ds = new DataSet();

            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;

                string sqlstr = "SELECT * FROM 員工 ORDER BY 編號 DESC";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                da.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
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
                dataGridView1.DataSource = emp.ToList();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立資料庫, 目前只能新增表單, 需使用既有資料庫\n";

            //1 建立连接对象
            SqlConnection con = new SqlConnection();

            //2 连接字符串(这里连接的是本地数据库，sa用户登陆，无密码)
            //con.ConnectionString = "server=.;uid=sa;pwd=;";  // NG
            con.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\dddd.mdf;Integrated Security=True;Connect Timeout=30";

            //3 建立命令执行对象
            SqlCommand cmd = new SqlCommand();

            //4 给命令执行对象指定连接对象
            cmd.Connection = con;

            //5 SQL语句（指定要创建数据库的SQL句）
            //string sqlstr = "create database mydatabase2";
            string sqlstr = "create database mydatabase3";

            cmd.CommandText = sqlstr;

            //6 打开数据库连接
            con.Open();

            try  //使用try...catch...敘述來補捉異動資料可能發生的例外 
            {
                //7 执行命令对象里的SQL语句
                cmd.ExecuteNonQuery();  // 執行SQL命令
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + ", 新增資料發生錯誤\n";
            }

            //8 执行完后关闭数据库连接
            con.Close();
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

// 資料庫連線參數, 連接字串
//String cnStr0 = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\MyDB.mdf;Integrated Security=True;Connect Timeout=30";
//cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|\ch17DB.mdf;Integrated Security=True";
//string cnstr1 = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|ch17DB.mdf;Integrated Security=True";
//cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

/*
有v11.0的, 就不可以, 要改用MSSQLLocalDB
AttachDbFilename=|DataDirectory|ch17DB.mdf  是 mdf 在 |DataDirectory|之下
AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf 是 指定 mdf 的位置
固定的寫法 :
Integrated Security=True";
其他參數 :
Connect Timeout=30

cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;       AttachDbFilename=|DataDirectory|ch17DB.mdf;                                   ;
cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;       AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;      ;
cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf; ;
*/



        //宣告cnStr連線字串置於事件處理函式外，以提供給其他事件處理函式共用
        //String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\MyDB.mdf;Integrated Security=True;Connect Timeout=30";
        // 設定相關資料庫連線參數
//                    String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\VisualC#2015基礎必修課\2015範例程式\data\MyDB.mdf;Integrated Security=True;Connect Timeout=30";



