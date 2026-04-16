
listView1參數
            this.listView1.AllowColumnReorder = true;
            this.listView1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.listView1.FullRowSelect = true;
            this.listView1.View = System.Windows.Forms.View.Details;
            this.listView1.GridLines = true;//網格線
            string str = this.listView1.SelectedItems[0].Text.ToString(); // 取出第0欄的資料, 員工編號
            richTextBox1.Text += str + "\n";



        private Boolean TextInfo()
        {
            foreach (Control c in groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    if (c.Text == "")
                    {
                        return false;
                    }
                    else
                    {
                        return true;
                    }
                }
            }
            return true;
        }



        private void clearText()
        {
            foreach (Control c in groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    c.Text = "";
                }
            }
            pictureBox1.Image = null;
        }




            string[] strCall = { "員工", "主幹人員", "部門經理", "經理" };
            this.comboBox2.DataSource = strCall;




//6060


            // 資料庫檔案
            string db_filename = "Northwind.mdb";

            // 查詢字串
            string sqlstr = "SELECT * FROM 員工";
            oledb_read_database(db_filename, sqlstr, dataGridView1);

            //3030

            db_filename = "Northwind.mdb";

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";





//撈出簡易的 資料庫檔案/連接字串 + 查詢字串


//------------------------------------------------------------  # 60個



 搜尋所有
"server=.;pwd=;uid=sa;database=db_13"


改 db_09.mdf 為 db_09_Data.MDF
	        db_09_Data

        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";


似乎 database接的是資料庫檔名 前檔名

        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");

            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09"))
            //using (SqlConnection con = new SqlConnection("server=.;uid=sa;pwd=;database=master"))


我使用Visual C# 做 SQL 程式，出現以下訊息，該如何解決呢?
An attempt to attach an auto-named database for file D:\db_TomeTwo3.mdf failed. A database with the same name exists, or specified file cannot be opened, or it is located on UNC share.


我使用Visual C# 做 SQL 程式，出現以下訊息，該如何解決呢?
Cannot open database "D:\DB_TOMETWO.MDF" requested by the login. The login failed. Login failed for user 'M-100028\070601'.


Cannot open database "D:\DB_TOMETWO.MDF" requested by the login. The login failed.
Login failed for user 'M-100028\070601'.



//------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //以下為debug
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工表";

            sql_read_database(db_filename, sqlstr, dataGridView1);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //新增

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection con = new SqlConnection(cnstr);

            con.Open();
            using (SqlCommand cmd = new SqlCommand("select Max(員工編號) from 員工表", con))
            {
                //找到目前最大的員工編號 再加1，做為新增資料的員工編號
                if (Convert.ToString(cmd.ExecuteScalar()) != "")
                {
                    richTextBox1.Text += "aaaaaaaaaaaaaaaaa\n";
                    string strID = Convert.ToString(cmd.ExecuteScalar());
                    richTextBox1.Text += "strID : " + strID + "\n";
                    this.textBox1.Text = strID.Substring(0, 1) + Convert.ToString(Convert.ToUInt32(strID.Substring(1)) + 1);
                }
                else
                {
                    richTextBox1.Text += "bbbbbbbbbbbbbbbbbb\n";
                    this.textBox1.Text = "P1001";
                }
            }
            con.Close();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //保存
            string id = "P1006";  // 員工編號
            string name = "mary";  // 員工姓名
            string money = "12345";  // 基本工資
           string description = "well done";  // 工作評價


            //保存按鈕

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection con = new SqlConnection(cnstr);

            con.Open();

            using (SqlCommand command = new SqlCommand("INSERT INTO 員工表 " +
               "VALUES (@員工編號, @員工姓名,@基本工資,@工作評價)", con))
            {
                // Add the parameters for the InsertCommand.
                command.Parameters.Add("@員工編號", SqlDbType.VarChar, 50, "員工編號").Value = id;
                command.Parameters.Add("@員工姓名", SqlDbType.VarChar, 50, "員工姓名").Value = name;
                command.Parameters.Add("@基本工資", SqlDbType.Float, 8, "基本工資").Value = Convert.ToString(money);
                command.Parameters.Add("@工作評價", SqlDbType.VarChar, 50, "工作評價").Value = description;
                command.ExecuteNonQuery();
                MessageBox.Show("OK");
            }

            con.Close();


        }

-----------

            //新增資料

            string id = "P1006";  // 員工編號
            string name = "mary";  // 員工姓名
            string money = "12345";  // 基本工資
            string description = "well done";  // 工作評價

            StringBuilder strSQL = new StringBuilder();
            strSQL.Append("insert into 員工表(員工編號, 員工姓名,基本工資,工作評價)");
            strSQL.Append(" values('" + id + "','" + name + "',");
            strSQL.Append("'" + Convert.ToSingle(money) + "','" + description + "')");

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection con = new SqlConnection(cnstr);

            using (SqlCommand cmd = new SqlCommand(strSQL.ToString(), con))
            {
                con.Open();
                cmd.ExecuteNonQuery();
                MessageBox.Show("OK");
                con.Close();
            }
            strSQL.Remove(0, strSQL.Length);
            this.tbSave.Enabled = false;
            this.tbADD.Enabled = true;

-------------

        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";
        SqlConnection con = new SqlConnection(cnstr);

            //新增

            string get_new_id = ID();//自定義方法，自動產生編號

            //保存

            //利用預儲程序登入數據

            string id = "P1006";  // 員工編號1
            string name = "mary";  // 員工姓名2
            string money = "12345";  // 基本工資4
            string description = "well done";  // 工作評價5

            using (SqlCommand cmd = new SqlCommand())//實例化SqlCommand類
            {
                try
                {
                    cmd.Connection = con;//建立資料庫的連接
                    con.Open();//打開資料庫的連接
                    cmd.CommandType = CommandType.StoredProcedure;//設定類型為預儲程序
                    cmd.CommandText = "proc_insert";//預儲程序我
                    SqlParameter[] prams =
                        {
						        new SqlParameter("@id", SqlDbType.VarChar, 8),
                                new SqlParameter("@name", SqlDbType.VarChar, 50),
                                new SqlParameter("@money", SqlDbType.Float),
                                new SqlParameter("@talk", SqlDbType.VarChar, 50)
				        };//新增預儲程序的參數名
                    prams[0].Value = this.textBox1.Text;//設定參數值
                    prams[1].Value = this.textBox2.Text;
                    prams[2].Value = this.textBox4.Text;
                    prams[3].Value = this.textBox5.Text;
                    //新增參數
                    foreach (SqlParameter parameter in prams)
                        cmd.Parameters.Add(parameter);
                    SqlParameter sqlpar = cmd.Parameters.Add("@Return", SqlDbType.Int);
                    sqlpar.Direction = ParameterDirection.ReturnValue;//取得傳回值
                    cmd.ExecuteNonQuery();//執行SQL語句
                    con.Close();//關閉資料庫的連接
                }
                catch (Exception eu)
                {
                    MessageBox.Show("訊息有誤！！！");
                    con.Close();
                    return;
                }
                int i = Convert.ToInt16(cmd.Parameters["@Return"].Value.ToString());//傳回影響的行數
                if (i == 1)
                {
                    MessageBox.Show("新增過程成功");
                }
                else if (i == -1)
                {
                    MessageBox.Show("新增過程失敗");
                }

                //顯示新增後的結果
                //顯示數據
                using (SqlDataAdapter da = new SqlDataAdapter("select * from 員工表", con))//建立SQL語旬與數據庫的連接
                {
                    DataTable dt = new DataTable();//實例化DataTable類
                    da.Fill(dt);//新增SQL語句並執行
                    DataView dv = new DataView(dt);//實例化DataView
                    this.dataGridView1.DataSource = dv;//顯示數據
                }
            }

----

        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";
        SqlConnection con = new SqlConnection(cnstr);


        //自定義方法
        private string ID()
        {
            try
            {
                SqlCommand cmd = new SqlCommand();//實例化SqlCommand類
                cmd.Connection = con;//設定資料庫的連接
                con.Open();//打開資料庫的連接
                cmd.CommandType = CommandType.StoredProcedure;//設定類型為預儲程序
                cmd.CommandText = "proc_Id";//預儲程序的名稱
                SqlParameter sqlOutput = new SqlParameter("@Id", SqlDbType.VarChar, 8);//取得最後一個記錄的編號
                sqlOutput.Direction = ParameterDirection.Output;//參數輸出
                cmd.Parameters.Add(sqlOutput);//新增編號
                cmd.ExecuteNonQuery();//執行SQL語句
                con.Close();//關閉連接
                richTextBox1.Text += "新增編號 : " + cmd.Parameters["@Id"].Value.ToString() + "\n";
                return cmd.Parameters["@Id"].Value.ToString();//傳回編號的值
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
                return null;
            }
        }



//------------------------------------------------------------  # 60個


            textBox1.Text="david";  // 員工姓名
            textBox2.Text="12345";  // 基本工資
            textBox3.Text="2000";  // 獎金
            textBox4.Text="1000";  // 扣款
            textBox5.Text="1500";  // 午餐
            textBox6.Text="22222";  // 實際工資

//textBox1 員工姓名
//textBox2 基本工資
//textBox3 獎金
//textBox4 扣款
//textBox5 午餐
//textBox6 實際工資

            //解析回資料庫
            using (SqlDataAdapter da = new SqlDataAdapter())
            {
                SqlCommand command = new SqlCommand("INSERT INTO 帳單 " +
                "VALUES (@員工姓名, @基本工資,@獎金,@扣款,@午餐,@實際工資)", con);
                // Add the parameters for the InsertCommand.
                command.Parameters.Add("@員工姓名", SqlDbType.VarChar, 10, "員工姓名");
                command.Parameters.Add("@基本工資", SqlDbType.VarChar, 10, "基本工資");
                command.Parameters.Add("@獎金", SqlDbType.VarChar, 10, "獎金");
                command.Parameters.Add("@扣款", SqlDbType.VarChar, 10, "扣款");
                command.Parameters.Add("@午餐", SqlDbType.VarChar, 10, "午餐");
                command.Parameters.Add("@實際工資", SqlDbType.VarChar, 10, "實際工資");
                da.InsertCommand = command;
                MessageBox.Show("以成功能將訊息解析回資料庫");
            }





            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "select * from 帳單";

            sql_read_database(db_filename, sqlstr, dataGridView1);



//------------------------------------------------------------  # 60個

            //以下為debug
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Employee";
            /*
            sql_read_database(db_filename, sqlstr, dataGridView1);
            */

            // 資料庫檔案
            db_filename = "db_09_Data.MDF";
            // 查詢字串
            sqlstr = "select name from sysdatabases ";  // 系統查詢資料庫名稱
            //sqlstr = "select filename from sysdatabases ";  // 系統查詢資料庫檔案

            sql_read_database(db_filename, sqlstr, dataGridView1);



查看表格結構
            // 查詢字串
            //"SELECT name FROM sysobjects WHERE type = 'U' and name<>'dtproperties' "

            string strTableName = "table_name";
            string strSql = "select  name 字段名, xusertype 類型編號, length 長度 into hy_Linshibiao from  syscolumns  where id=object_id('" + strTableName + "') ";
            strSql += "select name 類型,xusertype 類型編號 into angel_Linshibiao from systypes where xusertype in (select xusertype from syscolumns where id=object_id('" + strTableName + "'))";

            SqlDataAdapter da = new SqlDataAdapter("select 字段名,類型,長度 from hy_Linshibiao t,angel_Linshibiao b where t.類型編號=b.類型編號", con);
            DataTable dt = new DataTable();
            da.Fill(dt);
            this.dataGridView1.DataSource = dt.DefaultView;

            SqlCommand cmdnew = new SqlCommand("drop table hy_Linshibiao,angel_Linshibiao", con);
            con.Open();
            cmdnew.ExecuteNonQuery();
            con.Close();


//------------------------------------------------------------  # 60個


D:\db_09_Data.mdf

            richTextBox1.Text += "員工編號 : " + strid + "\n";
            using (SqlCommand cmd = new SqlCommand("SELECT * FROM 員工表 WHERE 員工編號='" + strid + "'", con))
            {
                con.Open();
                SqlDataReader dr = cmd.ExecuteReader();
                if (dr.HasRows)
                {
                    dr.Read();
                    this.textBox1.Text = dr[0].ToString();
                    this.textBox2.Text = dr[1].ToString();
                    this.textBox4.Text = dr[2].ToString();
                    this.textBox5.Text = dr[3].ToString();
                }
                dr.Close();
                con.Close();
                this.tbUpdate.Enabled = true;
            }


        private bool Updateinfo()
        {
            richTextBox1.Text += "測試 UPDATE\n";
            richTextBox1.Text += "員工編號 : " + textBox1.Text +"\n";
            richTextBox1.Text += "員工姓名 : " + textBox2.Text +"\n";
            richTextBox1.Text += "基本工資 : " + textBox4.Text +"\n";
            richTextBox1.Text += "工作評價 : " + textBox5.Text +"\n";

            using (SqlCommand cmd = new SqlCommand())
            {
                try
                {
                    cmd.CommandText = "update 員工表 set 員工姓名='" + this.textBox2.Text + "',基本工資='" + this.textBox4.Text + "',工作評價='" + this.textBox5.Text + "' where 員工編號='" + this.textBox1.Text + "'";
                    con.Open();
                    cmd.Connection = con;
                    cmd.ExecuteNonQuery();
                    con.Close();
                    return true;
                }
                catch
                {
                    return false;
                }
            }
        }




//------------------------------------------------------------  # 60個




//------------------------------------------------------------  # 60個



//------------------------------------------------------------  # 60個



//------------------------------------------------------------  # 60個



//------------------------------------------------------------  # 60個



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

/*
            // 資料庫檔案
            string db_filename = "db_TomeTwo.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工表";

            sqlstr =
    @"select 学生姓名,性别,家庭住址 from tb_Student
union
select 学生姓名,convert(varchar,年龄),家庭住址 from tb_Student
union
select 学生姓名,convert(varchar,出生年月),家庭住址 from tb_Student
union
select 学生姓名,所在学院,家庭住址 from tb_Student";

            sql_read_database(db_filename, sqlstr, dataGridView1);

*/



//------------------------------------------------------------  # 60個



//------------------------------------------------------------  # 60個



//------------------------------------------------------------  # 60個



//------------------------------------------------------------  # 60個

SQL Server 數據庫檔案 (.mdf)
Microsoft SQL Server 的主資料庫檔案（Master Database File），通常與 .ldf（日誌文件）成對出現。

開啟方式： Microsoft SQL Server 或 Visual Studio 的「伺服器總管」。 

//------------------------------------------------------------  # 60個


伺服器資料型別
BigInt
NChar(4)
NVarChar(50)
NVarChar(50)
NVarChar(60) NOT NULL
NVarChar(30) NOT NULL
NVarChar(15) NOT NULL
UniqueIdentifier NOT NULL
DateTime NOT NULL
Int NOT NULL
NVarChar(60)
Int NOT NULL IDENTITY


string (System.String)
long (System.Int64)


//------------------------------------------------------------  # 60個



開始前先確認有安裝 SQL Server LocalDB，找得到 SQLLocalDB.exe，
使用 SQLLocalDB.exe info 查詢 LocalDB 的預設個體名稱，一般會是 MSSQLLocalDB。
PS C:\Users\070601> sqllocaldb info
MSSQLLocalDB


Data Source=(local)\MSSQLLocalDB，執行以下指令即可建立空白資料庫及 mdf、ldf 檔案：

CREATE DATABASE <db_name>
ON PRIMARY ( 
    NAME=<db_name>_data, 
    FILENAME = '<path>\<db_name>_data.mdf'
) 
LOG ON (
    NAME=<db_name>_log, 
    FILENAME = '<paht>\<db_name>_log.ldf'
)




PS C:\Users\070601> sqllocaldb info
MSSQLLocalDB
PS C:\Users\070601> sqllocaldb info MSSQLLocalDB
Name:               MSSQLLocalDB
Version:            15.0.4153.1
Shared name:
Owner:              M-100028\070601
Auto-create:        Yes
State:              Stopped
Last start time:    2026/4/7 13:16:33
Instance pipe name:




richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

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


//欲刪除關鍵字
//SqlConnection con = new SqlConnection("Data Source=.;DataBase=master;integrated security=sspi");//初始化一個數據庫連接對像
//static string connectionString = "Data Source=.;DataBase=db_02;integrated security=sspi";
            //string cnstr = string.Format(@"server=MR-PC\YL;database=db_TomeTwo;uid=sa;pwd=");


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



OleDbDataAdapter
DataTable的用法 
                    OleDbDataAdapter OledbDat = new OleDbDataAdapter("select top 1 * from 帳單", strOledbCon);
                    DataTable dt = new DataTable();
                    OledbDat.Fill(dt);
                    this.textBox1.Text = dt.Rows[0][0].ToString().Trim();
                    this.textBox2.Text = dt.Rows[0][1].ToString().Trim();
                    this.textBox3.Text = dt.Rows[0][3].ToString().Trim();
                    this.textBox4.Text = dt.Rows[0][4].ToString().Trim();

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        SqlConnection conn = new SqlConnection(Data Source=localhost; Integrated Security=SSPI; Initial Catalog=pubs);

	SqlCommand cmd = new SqlCommand(SELECT * FROM employees, conn);
        try
        {        
            conn.Open();

            SqlDataReader reader = cmd.ExecuteReader();            
            while (reader.Read())
            {
                Console.WriteLine(First Name: {0}, Last Name: {1}, reader.GetString(0), reader.GetString(1));
            }
        
            reader.Close();
            conn.Close();
        }
        catch(Exception e)
        {
            Console.WriteLine(Exception Occured -->> {0},e);
        }        
    }
}

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


十、從SQL內讀數據到XML：
using System;
using System.Data;
using System.XML;
using System.Data.SqlClIEnt; 
using System.IO; 

public class TestWriteXML
{ 
    public static void Main()
    { 

        String strFileName=c:/temp/output.XML;

        SqlConnection conn = new SqlConnection(server=localhost;uid=sa;pwd=;database=db);

        String strSql = SELECT FirstName, LastName FROM employees; 

        SqlDataAdapter adapter = new SqlDataAdapter(); 

        adapter.SelectCommand = new SqlCommand(strSql, conn);

        // Build the DataSet
        DataSet ds = new DataSet();

        adapter.Fill(ds, employees);

        // Get a FileStream object
        FileStream fs = new FileStream(strFileName,FileMode.OpenOrCreate,FileAccess.Write);

        // Apply the WriteXml method to write an XML document
        ds.WriteXML(fs);

        fs.Close();

    }
}


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

----------------常用的程式片段 ST cccc----------------


string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
string filename = @"D:\_git\vcs\_1.data\______test_files1\__text\war_and_peace.txt";

//以下複製到每個檔案

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

        //以下為debug ----------------------------------------------------------------------------------------------------  # 100個

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
        }
        
//以下為debug ----------------------------------------------------------------------------------------------------  # 100個

        private void button1_Click(object sender, EventArgs e)
        {
            //以下為debug
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Employee";

            sql_read_database(db_filename, sqlstr, dataGridView1);

        }
