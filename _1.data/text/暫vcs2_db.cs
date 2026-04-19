

SELECT name FROM sysdatabases


FROM sysdatabases

SELECT name, database_id, create_date
FROM sys.databases;
GO



SELECT name,
       user_access_desc,
       is_read_only,
       state_desc,
       recovery_model_desc
FROM sys.databases;


-- Execute from the master database.
SELECT a.name,
       a.state_desc,
       b.start_date,
       b.modify_date,
       b.percent_complete
FROM sys.databases AS a
     INNER JOIN sys.dm_database_copies AS b
         ON a.database_id = b.database_id
WHERE a.state = 7;





//------------------------------------------------------------  # 60個


            /*
            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            dataGridView1.Click += new EventHandler(dataGridView1_Click);
            */


        private void dataGridView1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "dataGridView1_Click, 取得資料 :\n";
            richTextBox1.Text += "第0欄 : " + this.dataGridView1.SelectedCells[0].Value.ToString() + "\n";
            richTextBox1.Text += "第1欄 : " + this.dataGridView1.SelectedCells[1].Value.ToString() + "\n";
            richTextBox1.Text += "第2欄 : " + this.dataGridView1.SelectedCells[2].Value.ToString() + "\n";
            richTextBox1.Text += "第3欄 : " + this.dataGridView1.SelectedCells[3].Value.ToString() + "\n";
        }


            dataGridView1.Columns[0].Width = 150;//設置欄位寬度
            dataGridView1.Columns[1].Width = 150;//設置欄位寬度
            dataGridView1.Columns[2].Width = 150;//設置欄位寬度



//------------------------------------------------------------  # 60個





//------------------------------------------------------------  # 60個






//------------------------------------------------------------  # 60個

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


//6060


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


using System.Diagnostics;
            //開啟 Sql Server 服務
            Process pro = new Process();
            pro.StartInfo.FileName = "cmd.exe";
            pro.StartInfo.UseShellExecute = false;
            pro.StartInfo.RedirectStandardInput = true;
            pro.StartInfo.RedirectStandardOutput = true;
            pro.StartInfo.RedirectStandardError = true;
            pro.StartInfo.CreateNoWindow = true;
            pro.Start();
            pro.StandardInput.WriteLine("net start mssqlserver");
            pro.StandardInput.WriteLine("exit");
            MessageBox.Show("已成功開啟服務");


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

        // 以下為debug ----------------------------------------------------------------------------------------------------  # 100個

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
        
// 以下為debug ----------------------------------------------------------------------------------------------------  # 100個

        private void button1_Click(object sender, EventArgs e)
        {
            return;
            // 以下為debug
            // 資料庫檔案
            string db_filename = "ddddddd.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM ddddddd";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }




// 簡易OK 資料庫檔案 + 查詢字串


            // 資料庫檔案
            db_filename = "db_10_Data.MDF";
            // 查詢字串, 查詢邏輯型數據, 查詢是否為國家統招學生
            string select_type = "是";  // "是/否"
            sqlstr = "SELECT * FROM tb_08 WHERE 統招否='" + select_type + "'";


// OK 查詢字串




