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
using System.Collections;  // for Hashtable
using System.Drawing.Drawing2D;  // for LinearGradientBrush
//using System.Drawing.Imaging;

//對資料庫操作 增茶改山

namespace vcs_SqlConnection4
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
            panel1.Size = new Size(420, 380);
            pictureBox1.Size = new Size(420, 380);

            lb_dgv1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd);
            lb_dgv2.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            dataGridView2.Location = new Point(x_st + dx * 3, y_st + dy * 6 + dd);
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
            panel1.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6);

            richTextBox1.Size = new Size(300, 820);
            richTextBox1.Location = new Point(x_st + dx * 7 + 110, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1920, 890);
            this.Text = "vcs_SqlConnection4";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            dataGridView1.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView2.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
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
                    //richTextBox1.Text += dr[0].ToString() + "\t" + Convert.ToDouble(dr[1].ToString()) + "\n";
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
            }
            else if (dgv == dataGridView2)
            {
                lb_dgv2.Text = "";
            }
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

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //插入多筆紀錄
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Student";
            sql_read_database(db_filename, sqlstr, dataGridView1);


            // 插入多条数据记录

            // 資料庫檔案
            db_filename = "db_TomeTwo.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            // 查詢字串
            sqlstr = string.Format(@"INSERT INTO tb_Student_Copy(学生姓名,学生年龄,性别,家庭住址) SELECT 学生姓名,年龄,性别,家庭住址 FROM tb_Student");

            //创建SQL连接对象
            SqlConnection cn = new SqlConnection(cnstr);
            cn.Open();//打开数据库连接
            //创建命令对象
            SqlCommand P_cmd = new SqlCommand(sqlstr, cn);
            if (P_cmd.ExecuteNonQuery() != 0)//写入数据并判断是否成功
            {
                richTextBox1.Text += "寫入數據 OK\n";
            }
            else
            {
                richTextBox1.Text += "寫入數據 NG\n";
            }
            cn.Close();//关闭数据库连接


            // 顯示出來

            // 資料庫檔案
            db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM tb_Student_Copy";
            sql_read_database(db_filename, sqlstr, dataGridView2);

        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {

        }
        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
            //分析產品銷售走勢

            // 資料庫檔案
            string db_filename = "db_13.mdf";

            // 查詢字串, 全部
            string sqlstr = "SELECT * FROM tb_merchandise";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "查詢字串, 全部";

            // 查詢字串, 相同項合併
            sqlstr = "SELECT distinct(t_name) FROM tb_merchandise";
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "查詢字串, 相同項合併";

            richTextBox1.Text += "------------------------------\n";  // 30個

            string str = "24K";
            richTextBox1.Text += "搜尋 : " + str + " 項目\n";

            // 資料庫檔案
            db_filename = "db_13.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection con = new SqlConnection(cnstr))
            {
                // 查詢字串, 找最大值
                sqlstr = "SELECT Max(t_price) FROM tb_merchandise WHERE t_name='" + str + "'";
                using (SqlCommand cmd = new SqlCommand(sqlstr, con))
                {
                    con.Open();
                    int MaxValue = Convert.ToInt16(cmd.ExecuteScalar());
                    richTextBox1.Text += "取得最大值 : " + MaxValue.ToString() + "\n";
                    con.Close();
                }

                // 查詢字串, 找最小值
                sqlstr = "SELECT Min(t_price) FROM tb_merchandise WHERE t_name='" + str + "'";
                using (SqlCommand cmd = new SqlCommand(sqlstr, con))
                {
                    con.Open();
                    int MinValue = Convert.ToInt16(cmd.ExecuteScalar());
                    richTextBox1.Text += "取得最小值 : " + MinValue.ToString() + "\n";
                    con.Close();
                }

                // 查詢字串
                sqlstr = "SELECT * FROM tb_merchandise WHERE t_name='" + str + "' order by t_date";
                using (SqlDataAdapter da = new SqlDataAdapter(sqlstr, con))
                {
                    DataSet ds = new DataSet();
                    da.Fill(ds);

                    richTextBox1.Text += "取得資料 : " + ds.Tables[0].Rows.Count.ToString() + " 筆\n";
                    for (int i = 0; i < ds.Tables[0].Rows.Count; i++)
                    {
                        richTextBox1.Text += ds.Tables[0].Rows[i][2].ToString() + "\t" + ds.Tables[0].Rows[i][3].ToString() + "\n";
                    }
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
            //數據分析

            //有資料的年份
            //1999, 2000, 2001, 2004, 2005, 2006, 2007
            int query_year = 1999;

            // 資料庫檔案
            string db_filename = "db_13.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_curve WHERE Years=" + query_year + "";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 資料庫檔案
            db_filename = "db_13.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                cn.Open();

                sqlstr = "SELECT * FROM tb_curve WHERE Years=" + query_year + "";
                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataAdapter da = new SqlDataAdapter();
                da.SelectCommand = cmd;
                DataSet ds = new DataSet();
                da.Fill(ds);
                for (int i = 0; i < 12; i++)
                {
                    richTextBox1.Text += ds.Tables[0].Rows[0][i + 1].ToString() + "\n";
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
            //網站人氣指數曲線分析

            // 資料庫檔案
            string db_filename = "db_13.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_reticulation";  // 網眼,網狀,網狀物
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 資料庫檔案
            db_filename = "db_13.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            SqlConnection cn = new SqlConnection(cnstr);
            sqlstr = "SELECT * FROM tb_reticulation";
            SqlCommand cmd = new SqlCommand(sqlstr, cn);
            SqlDataAdapter da = new SqlDataAdapter();
            da.SelectCommand = cmd;
            DataSet ds = new DataSet();
            da.Fill(ds);
            for (int j = 0; j < 12; j++)
            {
                richTextBox1.Text += ds.Tables[0].Rows[0][j + 2].ToString() + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
            //利用餅型圖分析產品市場佔有率

            // debug ST
            // 資料庫檔案
            string db_filename = "db_13.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_product";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            // debug SP

            // 資料庫檔案
            db_filename = "db_13.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            SqlConnection con = new SqlConnection(cnstr);
            con.Open();

            // 查詢字串
            sqlstr = "SELECT SUM(t_Num) FROM tb_product";
            using (SqlCommand cmd = new SqlCommand(sqlstr, con))
            {
                int SumNum = Convert.ToInt32(cmd.ExecuteScalar());
                richTextBox1.Text += "總和 : " + SumNum.ToString() + "\n\n";
            }

            // 查詢字串, 重複的Name要合併GROUP BY
            sqlstr = "SELECT t_Name, SUM(t_Num) AS Num FROM tb_product GROUP BY t_Name";
            sql_read_database(db_filename, sqlstr, dataGridView2);
        }

        //------------------------------------------------------------  # 60個

        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";

        private void button10_Click(object sender, EventArgs e)
        {
            //分析企業人力資源情況

            // debug ST
            // 資料庫檔案
            string db_filename = "db_13.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_manpower";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            // debug SP

            SqlConnection con = new SqlConnection(cnstr);

            int Sum = 100;
            using (SqlCommand cmd = new SqlCommand("SELECT SUM(t_Num) FROM tb_manpower ", con))
            {
                con.Open();
                Sum = Convert.ToInt32(cmd.ExecuteScalar());
                richTextBox1.Text += "Sum = " + Sum.ToString() + "\n";
                con.Close();
            }
            richTextBox1.Text += "Sum = " + Sum.ToString() + "\n";

            using (SqlCommand cmd = new SqlCommand("SELECT t_Point, SUM(t_Num) FROM tb_manpower GROUP BY t_Point ORDER BY SUM(t_Num) DESC", con))//降冪
            {
                cmd.Connection.Open();
                SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
                while (dr.Read())
                {
                    richTextBox1.Text += dr[0].ToString() + "\t" + Convert.ToDouble(dr[1].ToString()) + "\n";
                    float f = Convert.ToSingle(dr[1]) / Sum;
                    string str = dr[0].ToString();
                    richTextBox1.Text += "str : " + str + "\n";
                }
                dr.Close();
                con.Close();
            }
        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "db_10_Data.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM v10_01";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            // 更新資料
            //SqlCommand cmd = new SqlCommand("update v10_01 set 基本工資='" + textBox2.Text + "' WHERE 員工編號='" + textBox1.Text + "'", con);
        }

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 12\n";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 13 員工表\n";

            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工表";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 資料庫檔案
            db_filename = "db_09_Data.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            SqlConnection con = new SqlConnection(cnstr);

            con.Open();

            using (SqlCommand cmd = new SqlCommand("SELECT Max(員工編號) FROM 員工表", con))
            {
                //找到目前最大的員工編號 再加1，做為新增資料的員工編號
                if (Convert.ToString(cmd.ExecuteScalar()) != "")
                {
                    richTextBox1.Text += "aaaaaaaaaaaaaaaaa\n";
                    string strID = Convert.ToString(cmd.ExecuteScalar());
                    richTextBox1.Text += "取出員工表中最大的員工編號 : " + strID + "\n";
                }
                else
                {
                    richTextBox1.Text += "bbbbbbbbbbbbbbbbbb\n";
                }
            }
            con.Close();

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增

            string id = "P1007";  // 員工編號
            string name = "mary";  // 員工姓名
            string money = "12345";  // 基本工資
            string description = "well done";  // 工作評價

            // 資料庫檔案
            db_filename = "db_09_Data.mdf";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);

            con = new SqlConnection(cnstr);

            con.Open();

            // 查詢字串
            sqlstr = "INSERT INTO 員工表 " + "VALUES (@員工編號, @員工姓名,@基本工資,@工作評價)";

            using (SqlCommand command = new SqlCommand(sqlstr, con))
            {
                // Add the parameters for the InsertCommand.
                command.Parameters.Add("@員工編號", SqlDbType.VarChar, 50, "員工編號").Value = id;
                command.Parameters.Add("@員工姓名", SqlDbType.VarChar, 50, "員工姓名").Value = name;
                command.Parameters.Add("@基本工資", SqlDbType.Float, 8, "基本工資").Value = Convert.ToString(money);
                command.Parameters.Add("@工作評價", SqlDbType.VarChar, 50, "工作評價").Value = description;
                command.ExecuteNonQuery();
                richTextBox1.Text += "OK\n";
            }

            con.Close();

            // 查詢字串
            sqlstr = "SELECT * FROM 員工表";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增資料
            id = "P1008";  // 員工編號
            name = "mary";  // 員工姓名
            money = "12345";  // 基本工資
            description = "well done";  // 工作評價

            // 查詢字串
            sqlstr = "INSERT INTO 員工表(員工編號, 員工姓名,基本工資,工作評價) values('" + id + "','" + name + "','" + Convert.ToSingle(money) + "','" + description + "')";

            // 資料庫檔案
            db_filename = "db_09_Data.mdf";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);

            con = new SqlConnection(cnstr);

            using (SqlCommand cmd = new SqlCommand(sqlstr, con))
            {
                con.Open();
                cmd.ExecuteNonQuery();
                richTextBox1.Text += "OK\n";
                con.Close();
            }

            // 查詢字串
            sqlstr = "SELECT * FROM 員工表";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            string strid = "P1008";  // 員工編號
            richTextBox1.Text += "員工編號 : " + strid + "\n";
            //SqlCommand cmd = new SqlCommand("SELECT * FROM 員工表 WHERE 員工編號='" + strid + "'", con))

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            richTextBox1.Text += "測試 UPDATE 修改\n";
            richTextBox1.Text += "員工編號 : " + textBox1.Text + "\n";
            richTextBox1.Text += "員工姓名 : " + textBox2.Text + "\n";
            richTextBox1.Text += "基本工資 : " + textBox4.Text + "\n";
            richTextBox1.Text += "工作評價 : " + textBox5.Text + "\n";

            using (SqlCommand cmd = new SqlCommand())
            {
                try
                {
                    cmd.CommandText = "UPDATE 員工表 SET 員工姓名='" + this.textBox2.Text + "',基本工資='" + this.textBox4.Text + "',工作評價='" + this.textBox5.Text + "' WHERE 員工編號='" + this.textBox1.Text + "'";
                    con.Open();
                    cmd.Connection = con;
                    cmd.ExecuteNonQuery();
                    con.Close();
                }
                catch
                {

                }
            }
            */
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        SqlConnection con;
        SqlCommand cmd;

        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 15\n";

            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            /*
            textBox1.Text = "david";  // 員工姓名
            textBox2.Text = "12345";  // 基本工資
            textBox3.Text = "2000";  // 獎金
            textBox4.Text = "1000";  // 扣款
            textBox5.Text = "1500";  // 午餐
            textBox6.Text = "22222";  // 實際工資
            */
            //textBox1 員工姓名
            //textBox2 基本工資
            //textBox3 獎金
            //textBox4 扣款
            //textBox5 午餐
            //textBox6 實際工資

            //解析回資料庫
            using (SqlDataAdapter da = new SqlDataAdapter())
            {
                SqlCommand command = new SqlCommand("INSERT INTO 帳單 " + "VALUES (@員工姓名, @基本工資,@獎金,@扣款,@午餐,@實際工資)", con);
                // Add the parameters for the InsertCommand.
                command.Parameters.Add("@員工姓名", SqlDbType.VarChar, 10, "員工姓名");
                command.Parameters.Add("@基本工資", SqlDbType.VarChar, 10, "基本工資");
                command.Parameters.Add("@獎金", SqlDbType.VarChar, 10, "獎金");
                command.Parameters.Add("@扣款", SqlDbType.VarChar, 10, "扣款");
                command.Parameters.Add("@午餐", SqlDbType.VarChar, 10, "午餐");
                command.Parameters.Add("@實際工資", SqlDbType.VarChar, 10, "實際工資");
                da.InsertCommand = command;
                richTextBox1.Text += "已成功能將訊息解析回資料庫\n";
            }

            // 看一下結果

            // 資料庫檔案
            db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 帳單";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 16\n";

            //D:\db_09_Data.mdf

            //新增資料
            string pic_filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string file_no = "A123456";  // 檔案編號
            string work_no = "1234";  // 工號
            string name = "david";  // 姓名
            string birthday = "2006/03/11";  // 出生日期
            string city = "Taiwan";  // 籍貫
            string work_year = "5";  // 工齡
            string department = "研發部";  // 部門名稱
            string telephone = "0912345678";  // 電話
            string sex = "男";  // 性別
            string position = "員工";  // 技術職稱
            string marriage = "已婚";  // 婚姻狀態
            string health = "良好";  // 健康狀態

            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            SqlConnection con = new SqlConnection(cnstr);

            try
            {
                con.Open();

                // 查詢字串
                string sqlstr = "INSERT INTO 檔案訊息 values(@檔案編號,@工號,@姓名,@照片,@性別,@出生日期,@籍貫,@工齡,@電話,@部門名稱,@技術職稱,@婚姻狀態,@健康狀態)";

                SqlCommand cmd = new SqlCommand(sqlstr, con);
                cmd.Parameters.Add("@檔案編號", SqlDbType.Text).Value = file_no;
                cmd.Parameters.Add("@工號", SqlDbType.Text).Value = work_no;
                cmd.Parameters.Add("@姓名", SqlDbType.Text).Value = name;
                cmd.Parameters.Add("@照片", SqlDbType.Text).Value = pic_filename;
                cmd.Parameters.Add("@性別", SqlDbType.Text).Value = sex;
                cmd.Parameters.Add("@出生日期", SqlDbType.Text).Value = birthday;
                cmd.Parameters.Add("@籍貫", SqlDbType.Text).Value = city;
                cmd.Parameters.Add("@工齡", SqlDbType.Int).Value = Convert.ToInt16(work_year);
                cmd.Parameters.Add("@電話", SqlDbType.Text).Value = telephone;
                cmd.Parameters.Add("@部門名稱", SqlDbType.Text).Value = department;
                cmd.Parameters.Add("@技術職稱", SqlDbType.Text).Value = position;
                cmd.Parameters.Add("@婚姻狀態", SqlDbType.Text).Value = marriage;
                cmd.Parameters.Add("@健康狀態", SqlDbType.Text).Value = health;
                cmd.ExecuteNonQuery();
                con.Close();
                richTextBox1.Text += "新增成功\n";
            }
            catch (Exception ey)
            {
                richTextBox1.Text += "新增失敗\n";
                richTextBox1.Text += ey.Message.ToString() + "\n";
            }

            /*
            //讀取全部

            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 檔案訊息";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            */
        }

        private void button17_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 17\n";

            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_power";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //更新資料範例

            string name = "hywork";
            string strValue = "12345";

            // 查詢字串
            sqlstr = "UPDATE tb_Power SET power='" + strValue + "' WHERE name='" + name + "' ";
            sql_write_database(db_filename, sqlstr);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 資料庫檔案
            db_filename = "db_09_Data.mdf";
            // 查詢字串
            sqlstr = "SELECT * FROM tb_power";
            sql_read_database(db_filename, sqlstr, dataGridView2);


            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢範例

            // 資料庫檔案
            db_filename = "db_09_Data.mdf";
            // 連接字串
            cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection con = new SqlConnection(cnstr))//連接資料庫
            {
                SqlCommand cmd = new SqlCommand("SELECT power FROM tb_power WHERE name='" + name + "'", con);//連接SQL語句與數擾庫的連接
                cmd.Connection = con;
                cmd.Connection.Open();//打開資料庫的連接
                SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
                if (dr.HasRows)//如果有記錄
                {
                    dr.Read();//讀取下一行
                    string str = dr[0].ToString();//取得權限值
                    richTextBox1.Text += "取得權限值 = " + str + "\n";
                }
                dr.Close();//關閉
                con.Close();//關閉連接
                con.Dispose();
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 18\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 19\n";
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //更新資料
            string number = "P1003";
            string name = "david wang";
            string money = "12345";
            string description = "very good";

            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            SqlConnection con = new SqlConnection(cnstr);

            // 查詢字串
            string sqlstr = "update 員工表 set 員工姓名=@員工姓名,基本工資=@基本工資,工作評價=@工作評價 WHERE 員工編號=@員工編號";

            using (SqlCommand command = new SqlCommand(sqlstr, con))
            {
                con.Open();
                try
                {
                    command.Parameters.Add("@員工編號", SqlDbType.VarChar, 50, "員工編號").Value = number;
                    command.Parameters.Add("@員工姓名", SqlDbType.VarChar, 50, "員工姓名").Value = name;
                    command.Parameters.Add("@基本工資", SqlDbType.Float, 8, "基本工資").Value = Convert.ToString(money);
                    command.Parameters.Add("@工作評價", SqlDbType.VarChar, 50, "工作評價").Value = description;
                    command.ExecuteNonQuery();
                    con.Close();
                    richTextBox1.Text += "成功修改\n";
                }
                catch
                {
                    richTextBox1.Text += "成功失敗\n";
                }
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            SqlConnection con = new SqlConnection(cnstr);

            //查詢資料
            string strid = "P1005";  // 員工編號
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工表 WHERE 員工編號='" + strid + "'";

            using (SqlCommand cmd = new SqlCommand(sqlstr, con))
            {
                con.Open();
                SqlDataReader dr = cmd.ExecuteReader();
                if (dr.HasRows)
                {
                    dr.Read();
                    string new_id = dr[0].ToString();  // 員工編號
                    string new_name = dr[1].ToString();  // 員工姓名
                    string new_money = dr[2].ToString();  // 基本工資
                    string new_description = dr[3].ToString();  // 工作評價
                    //this.textBox1.Text = new_id;
                    //this.textBox2.Text = new_name;
                    //this.textBox4.Text = new_money;
                    //this.textBox5.Text = new_description;
                    richTextBox1.Text += "員工編號 : " + new_id + "\n";
                    richTextBox1.Text += "員工姓名 : " + new_name + "\n";
                    richTextBox1.Text += "基本工資 : " + new_money + "\n";
                    richTextBox1.Text += "工作評價 : " + new_description + "\n";
                }
                dr.Close();
                con.Close();
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            // some NG
            //更新資料
            string new_id = "P1005";  // 員工編號
            string new_name = "david";  // 員工姓名
            string new_money = "34567";  // 基本工資
            string new_description = "Very good3333";  // 工作評價

            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            SqlConnection con = new SqlConnection(cnstr);

            using (SqlCommand cmd = new SqlCommand())
            {
                con.Open();
                cmd.Connection = con;
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.CommandText = "proc_Update";
                SqlParameter[] par =
                    { 
                        new SqlParameter("@id", new_id),
                        new SqlParameter("@name", new_name),
                        new SqlParameter("@money", new_money),
                        new SqlParameter("@description", new_description)
                    };
                foreach (SqlParameter parms in par)
                {
                    cmd.Parameters.Add(parms);
                }
                cmd.ExecuteNonQuery();
                con.Close();
                richTextBox1.Text += "修改成功\n";
            }
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 24\n";
        }

        private void button25_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 25\n";
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
            //show db

            // 資料庫檔案
            string db_filename = string.Empty;
            // 查詢字串
            string sqlstr = "dddddddd";


            // 資料庫檔案
            db_filename = "db_13.mdf";

            // 查詢字串
            //sqlstr = "SELECT * FROM tb_lottery";
            sqlstr = "SELECT * FROM tb_curve";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            // 查詢字串
            sqlstr = "SELECT Years FROM tb_curve";
            sql_read_database(db_filename, sqlstr, dataGridView2);
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
//richTextBox1.Text += "---------------\n";  // 15個
//---------------  # 15個


/*  可搬出

 */

/*

//------------------------------------------------------------  # 60個

//查看表格結構
            // 查詢字串
            //"SELECT name FROM sysobjects WHERE type = 'U' AND name<>'dtproperties' "

            string strTableName = "table_name";
 // 查詢字串
            string sqlstr = "SELECT name 字段名, xusertype 類型編號, length 長度 into hy_Linshibiao FROM syscolumns WHERE id=object_id('" + strTableName + "') ";
            sqlstr += "SELECT name 類型, xusertype 類型編號 into angel_Linshibiao FROM systypes WHERE xusertype in (SELECT xusertype FROM syscolumns WHERE id=object_id('" + strTableName + "'))";

            SqlDataAdapter da = new SqlDataAdapter("SELECT 字段名, 類型, 長度 FROM hy_Linshibiao t,angel_Linshibiao b WHERE t.類型編號=b.類型編號", con);
            DataTable dt = new DataTable();
            da.Fill(dt);
            this.dataGridView1.DataSource = dt.DefaultView;

            SqlCommand cmdnew = new SqlCommand("drop table hy_Linshibiao,angel_Linshibiao", con);
            con.Open();
            cmdnew.ExecuteNonQuery();
            con.Close();

//------------------------------------------------------------  # 60個
//------------------------------------------------------------  # 60個

            // 斷開服務

             // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection con = new SqlConnection(cnstr))
            {
                try
                {
                    string strShutdown = "SHUTDOWN WITH NOWAIT";
                    SqlCommand cmd = new SqlCommand();
                    cmd.Connection = con;
                    cmd.Connection.Open();
                    cmd.CommandText = strShutdown;
                    cmd.ExecuteNonQuery();
                    richTextBox1.Text += "已成功斷開服務\n";
                }
                catch (Exception euy)
                {
                    richTextBox1.Text += euy.Message + "\n" ;
                }
            }

//------------------------------------------------------------  # 60個

            //枚举本地网络中的SQL Server所有可用实例
            SqlDataSourceEnumerator instance = SqlDataSourceEnumerator.Instance;
            DataTable table = instance.GetDataSources();//获取所有数据源，并存储到DataTable中
            richTextBox1.Text += table + "\n";
            foreach (DataRow row in table.Rows)//遍历获取到的数据源
            {
                richTextBox1.Text += row + "\n";
                richTextBox1.Text += row["ServerName"] + "\n";
            }

//------------------------------------------------------------  # 60個

            // 資料庫檔案
            string db_filename = "db_TomeTwo.MDF";
            // 查詢字串
            string sqlstr =
    @"SELECT 学生姓名,性别,家庭住址 FROM tb_Student
union
SELECT 学生姓名,convert(varchar,年龄),家庭住址 FROM tb_Student
union
SELECT 学生姓名,convert(varchar,出生年月),家庭住址 FROM tb_Student
union
SELECT 学生姓名,所在学院,家庭住址 FROM tb_Student";

            sql_read_database(db_filename, sqlstr, dataGridView1);

//------------------------------------------------------------  # 60個

*/

