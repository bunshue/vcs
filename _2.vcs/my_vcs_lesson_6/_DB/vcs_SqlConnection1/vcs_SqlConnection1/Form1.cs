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
        //宣告cnStr連線字串置於事件處理函式外，以提供給其他事件處理函式共用
        //String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\MyDB.mdf;Integrated Security=True;Connect Timeout=30";

        // 設定相關資料庫連線參數
        String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\MyDB.mdf;Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
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

            dataGridView1.Size = new Size(560, 400);
            dataGridView1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            textBox1.Size = new Size(560, 400);
            textBox1.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            bt_clear2.Location = new Point(textBox1.Location.X + textBox1.Size.Width - bt_clear2.Size.Width, textBox1.Location.Y + textBox1.Size.Height - bt_clear2.Size.Height);

            richTextBox1.Size = new Size(560, 800);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1700, 910);
            this.Text = "vcs_SqlConnection1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection(cnStr);
            SqlDataAdapter da = new SqlDataAdapter("SELECT * From 員工", cn);
            DataSet ds = new DataSet();
            da.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0];
        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                //cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|\ch17DB.mdf;Integrated Security=True";
                //cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";
                cn.Open();
                SqlDataAdapter daEmployee = new SqlDataAdapter("SELECT * FROM 員工", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
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
            //test 2

            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

                cn.Open();
                if (cn.State == ConnectionState.Open)
                {
                    richTextBox1.Text += "資料庫已連接\n";
                }
                else
                {
                    richTextBox1.Text += "資料庫未連接\n";
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";
            using (SqlConnection cn = new SqlConnection(cnStr))
            {
                cn.Open();
                MessageBox.Show("連接資料庫：" + cn.Database, "Form1狀態");
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True";
                cn.Open();
                SqlCommand cmd = new SqlCommand("SELECT * FROM 成績單", cn);
                SqlDataReader dr = cmd.ExecuteReader();
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    textBox1.Text += dr.GetName(i) + "\t";
                }
                textBox1.Text += Environment.NewLine + Environment.NewLine;
                while (dr.Read())
                {
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        textBox1.Text += dr[i].ToString() + "\t";
                        //textBox1.Text += dr.GetValue(i).ToString() + "\t";    //另法
                    }
                    textBox1.Text += Environment.NewLine;
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True";
                cn.Open();
                SqlCommand cmd = new SqlCommand("SELECT * FROM 成績單", cn);
                SqlDataReader dr = cmd.ExecuteReader();
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    textBox1.Text += dr.GetName(i) + "\t";
                }
                textBox1.Text += Environment.NewLine + Environment.NewLine;
                while (dr.Read())
                {
                    textBox1.Text += dr["學號"].ToString() + "\t";
                    textBox1.Text += dr["姓名"].ToString() + "\t";
                    textBox1.Text += dr["國文"].ToString() + "\t";
                    textBox1.Text += dr["英文"].ToString() + "\t";
                    textBox1.Text += dr["數學"].ToString() + "\t";
                    textBox1.Text += Environment.NewLine;

                    /*
                    textBox1.Text += dr.GetString(0) + "\t";   //讀取學號
                    textBox1.Text += dr.GetString(1) + "\t";   //讀取姓名
                    textBox1.Text += dr.GetInt32(2).ToString() + "\t";   //讀取國文
                    textBox1.Text += dr.GetInt32(3).ToString() + "\t";   //讀取英文
                    textBox1.Text += dr.GetInt32(4).ToString() + "\t";   //讀取數學
                    textBox1.Text += Environment.NewLine;
                    */

                    /*
                    textBox1.Text += dr.GetSqlString(0).ToString() + "\t";//讀取學號
                    textBox1.Text += dr.GetSqlString(1).ToString() + "\t";//讀取姓名
                    textBox1.Text += dr.GetSqlInt32(2).ToString() + "\t";//讀取國文
                    textBox1.Text += dr.GetSqlInt32(3).ToString() + "\t";//讀取英文
                    textBox1.Text += dr.GetSqlInt32(4).ToString() + "\t";//讀取數學
                    textBox1.Text += Environment.NewLine;
                    */
                }
            }
        }

        // 員工資料表1 ST
        // 建立cnstr1連接字串用來連接ch17DB.mdf資料庫
        //string cnstr1 = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|ch17DB.mdf;Integrated Security=True";
        string cnstr1 = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

        // 定義ShowData1()方法將員工資料表所有記錄顯示於dataGridView1上
        void ShowData1()
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr1;
                SqlDataAdapter daEmployee = new SqlDataAdapter("SELECT * FROM 員工 ORDER BY 編號 DESC", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //員工資料表1
            //讀取 新增 修改 刪除
            ShowData1();


            //3030

            //新增

            string name = "david";
            string position = "engineering";
            string telephone = "0912345678";
            int salary = 55555;

            try  //使用try...catch...敘述來補捉異動資料可能發生的例外 
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    cn.ConnectionString = cnstr1;
                    cn.Open();
                    string sqlStr = "INSERT INTO 員工(姓名, 職稱, 電話, 薪資) VALUES('" + name + "','" + position + "','" + telephone + "'," + salary + ")";
                    SqlCommand Cmd = new SqlCommand(sqlStr, cn);
                    Cmd.ExecuteNonQuery();
                }
                ShowData1();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message + ", 新增資料發生錯誤");
            }

            //3030

            //修改

            string position2 = "manager";
            string telephone2 = "0987654321";
            int salary2 = 66666;

            try	//使用try...catch...敘述來補捉異動資料可能發生的例外
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    cn.ConnectionString = cnstr1;
                    cn.Open();
                    string sqlStr = "UPDATE 員工 SET 職稱 = '" + position2 + "',電話 = '" + telephone2 + "', 薪資 = " + salary2 + " WHERE 姓名 = '" + name + "'";
                    SqlCommand Cmd = new SqlCommand(sqlStr, cn);
                    Cmd.ExecuteNonQuery();
                }
                ShowData1();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message + ", 修改資料發生錯誤");
            }

            //3030

            //刪除

            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr1;
                cn.Open();
                string sqlStr = "DELETE FROM 員工 WHERE 姓名 = '" + name + "'";
                SqlCommand Cmd = new SqlCommand(sqlStr, cn);
                Cmd.ExecuteNonQuery();
            }
            ShowData1();
        }
        // 員工資料表1 SP


        // 員工資料表2 ST

        // 建立cnstr2連接字串用來連接ch17DB.mdf資料庫
        string cnstr2 = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

        // 定義ShowData2()方法將員工資料表所有記錄顯示於dataGridView1上
        void ShowData2()
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr2;
                SqlDataAdapter daEmployee = new SqlDataAdapter("SELECT * FROM 員工 ORDER BY 編號 DESC", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //員工資料表2
            //讀取 新增 修改 刪除

            ShowData2();

            //3030

            //新增

            string name = "david";
            string position = "engineering";
            string telephone = "0912345678";
            int salary = 55555;

            try	//使用try...catch...敘述來補捉異動資料可能發生的例外
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    cn.ConnectionString = cnstr2;
                    cn.Open();
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
                    cmd.ExecuteNonQuery();
                }
                ShowData2();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message + ", 新增資料發生錯誤");
            }


            //3030

            //修改

            string position2 = "manager";
            string telephone2 = "0987654321";
            int salary2 = 66666;

            try	//使用try...catch...敘述來補捉異動資料可能發生的例外
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    cn.ConnectionString = cnstr2;
                    cn.Open();
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
                    cmd.ExecuteNonQuery();
                }
                ShowData2();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message + ", 修改資料發生錯誤");
            }

            //3030

            //刪除

            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr2;
                cn.Open();
                string sqlStr = "DELETE FROM 員工 WHERE 姓名 = @name";
                SqlCommand cmd = new SqlCommand(sqlStr, cn);
                cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                cmd.Parameters["@name"].Value = name;
                cmd.ExecuteNonQuery();
            }
            ShowData2();
        }
        // 員工資料表2 SP

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //成績單1
            // 使用using敘述建立SqlConnection物件
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接ch16DB.mdf資料庫
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

                DataSet ds = new DataSet();  // 建立DataSet物件ds
                // 建立SqlDataAdapter物件daScore並取出成績單資料表
                SqlDataAdapter daScore = new SqlDataAdapter("SELECT * FROM 成績單", cn);
                // 將成績單資料表所有記錄填入ds物件
                daScore.Fill(ds, "成績單");
                // 宣告DataTable物件dt，該dt內存放ds中的成績單DataTable
                DataTable dt = ds.Tables["成績單"];
                // 在textBox1內顯示成績單的所有欄位名稱
                for (int i = 0; i < dt.Columns.Count; i++)
                {
                    textBox1.Text += dt.Columns[i].ColumnName + "\t";
                }
                textBox1.Text += Environment.NewLine + Environment.NewLine;
                // 在textBox1內顯示成績單的所有記錄
                for (int i = 0; i < dt.Rows.Count; i++)
                {
                    for (int j = 0; j < dt.Columns.Count; j++)
                    {
                        textBox1.Text += dt.Rows[i][j].ToString() + "\t";
                    }
                    textBox1.Text += Environment.NewLine;
                }
            }

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //成績單2

            // 使用using敘述建立SqlConnection物件
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接ch16DB.mdf資料庫
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

                DataSet ds = new DataSet();  // 建立DataSet物件ds
                // 建立SqlDataAdapter物件daScore並取出成績單資料表
                SqlDataAdapter daScore = new SqlDataAdapter("SELECT * FROM 成績單", cn);
                // 將成績單資料表所有記錄填入ds物件
                daScore.Fill(ds, "成績單");
                // 宣告DataTable物件dt，該dt內存放ds中的成績單DataTable
                DataTable dt = ds.Tables["成績單"];
                // 在textBox1內顯示成績單的所有欄位名稱
                for (int i = 0; i < dt.Columns.Count; i++)
                {
                    textBox1.Text += dt.Columns[i].ColumnName + "\t";
                }
                textBox1.Text += Environment.NewLine + Environment.NewLine;
                // 在textBox1內顯示成績單的所有記錄
                for (int i = 0; i < dt.Rows.Count - 1; i++)
                {
                    textBox1.Text += dt.Rows[i]["學號"].ToString() + "\t";
                    textBox1.Text += dt.Rows[i]["姓名"].ToString() + "\t";
                    textBox1.Text += dt.Rows[i]["國文"].ToString() + "\t";
                    textBox1.Text += dt.Rows[i]["英文"].ToString() + "\t";
                    textBox1.Text += dt.Rows[i]["數學"].ToString() + "\t";
                    textBox1.Text += Environment.NewLine;
                }
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //成績單 搜尋1
            string name = "david";
            // 使用using敘述建立SqlConnection物件cn
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接字串指定連接ch16DB.mdf資料庫
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

                cn.Open();  // 連接資料庫
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
                    richTextBox1.Text += "學號：" + dr["學號"].ToString() + Environment.NewLine;
                    richTextBox1.Text += "姓名：" + dr["姓名"].ToString() + Environment.NewLine;
                    richTextBox1.Text += "國文：" + dr["國文"].ToString() + Environment.NewLine;
                    richTextBox1.Text += "英文：" + dr["英文"].ToString() + Environment.NewLine;
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

            string name = "david";
            // 使用using敘述建立SqlConnection物件cn
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接字串指定連接ch16DB.mdf資料庫
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";
                cn.Open();  // 連接資料庫
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
                    richTextBox1.Text += "學號：" + dr["學號"].ToString() + Environment.NewLine;
                    richTextBox1.Text += "姓名：" + dr["姓名"].ToString() + Environment.NewLine;
                    richTextBox1.Text += "國文：" + dr["國文"].ToString() + Environment.NewLine;
                    richTextBox1.Text += "英文：" + dr["英文"].ToString() + Environment.NewLine;
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
