
//richTextBox1.Text += "共有" + (dataGridView1.Rows.Count - 1) + "条记录\n";



                    //刪除表單
                    //SqlCommand cmdnew = new SqlCommand("drop table animals1_table", con);
                    //cmdnew.ExecuteNonQuery();





sqlstr : select  name 字段名, xusertype 類型編號, length 長度 into animals1_table222 from syscolumns where id=object_id('') 
sqlstr : select  name 字段名, xusertype 類型編號, length 長度 into animals1_table    from syscolumns where id=object_id('') 

            // 查詢字串, 一次搜尋多個
            string sqlstr = "SELECT * FROM cjd WHERE 姓名 IN('張三', '劉心')";


//6060



            // 取出某表單的 欄位名稱
            string db_filename = "db_10_Data.MDF";
            string table_name = "銷售表";
            string sqlstr = "select c.name from syscolumns c,sysobjects a where a.name='" + table_name + "' and a.id=c.id";
            sql_read_database(db_filename, sqlstr, dataGridView2);




利用運算符查詢指定條件的數據

            string sqlstr = "SELECT * FROM " + TableName;//組合運算符的SQL查詢語句

            //左右模糊查詢
            sqlstr = sqlstr + " where " + FieldName + " like '%" + FieldValue + "%'";//組合SQL查詢語句

            //左模糊查詢
            sqlstr = sqlstr + " where " + FieldName + " like '%" + FieldValue + "'";//組合SQL查詢語句
            //右模糊查詢
            sqlstr = sqlstr + " where " + FieldName + " like '" + FieldValue + "%'";//組合SQL查詢語句
            //如是不是模糊查詢
            sqlstr = sqlstr + " where " + FieldName + Condition + "'" + FieldValue + "'";//組合算數運算符查詢語句
            //查詢條件為空
            sqlstr = sqlstr + " where " + FieldName + " IS null or " + FieldName + "=''";




//6060



//查看資料庫內有那些表單
//SqlDataAdapter da = new SqlDataAdapter("select name from sysdatabases", con);


            //備份資料庫
            // 把資料庫檔案A的所有資料 備份到 資料庫檔案B

            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

            string backup_filename = "aaaaaaaa.bak";
            string db_filename = "db_09_Data.MDF";

            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            SqlConnection con = new SqlConnection();		//利用程式碼完成連接資料庫
            con.ConnectionString = cnstr;
            con.Open();
            SqlCommand com = new SqlCommand();
            com.CommandText = "BACKUP DATABASE " + "animals1_db" + " TO DISK = '" + backup_filename + "'";
            com.Connection = con;							//連接
            com.ExecuteNonQuery();						    //執行
            con.Close();
            con.Dispose();
            richTextBox1.Text += "數據備份成功\n";












//"Provider=Microsoft.Jet.OleDb.4.0;"是指數據提供者,這裡使用的是Microsoft Jet引擎,也就是Access中的數據引擎,asp.net就是靠這個和Access的數據庫連接的.
//"Data Source=XXXXX.mdb"是指明數據源的位置


/*
如果訪問的數據庫是SQL Server 7.0，只需要把上面源代碼中的一條語句：
private static string strConnect = "Provider = Microsoft.Jet.OLEDB.4.0 ; Data Source = " + Application.StartupPath + "\\MY.MDB" ;
改變成：
private static string strConnect = "Provider=SQLOLEDB.1 ; Persist Security Info=False ; User ID = sa ; Initial Catalog=數據庫名稱; Data Source = 服務器名稱 " ;
即可。
*/






一次執行多個SQL指令, 若有指令失敗, 可以回復指令
SqlTransaction
                // 建立SqlTransaction交易物件tran
                SqlTransaction tran = cn.BeginTransaction();
                try
                {
                    // 查詢字串
                    sqlstr = "UPDATE 銀行帳戶 SET 餘額=餘額-" + money + " WHERE 帳號='" + src_ID + "'";
                    SqlCommand cmd3 = new SqlCommand(sqlstr, cn, tran);

                    // 設定轉入帳號匯款的SQL語法
                    // 查詢字串
                    sqlstr = "UPDATE 銀行帳戶 SET 餘額=餘額+" + money + " WHERE 帳號='" + dst_ID + "'";
                    SqlCommand cmd4 = new SqlCommand(sqlstr, cn, tran);

                    cmd3.ExecuteNonQuery();  // 執行SQL命令

                    cmd4.ExecuteNonQuery();  // 執行SQL命令

                    tran.Commit();  // 認可交易
                    richTextBox1.Text += "轉帳成功, 交易成功\n";
                }
                catch (Exception ex)
                {
                    tran.Rollback();  // 回復交易
                    richTextBox1.Text += "轉帳失敗" + ex.Message + "交易失敗\n";
                }



//6060

using System.Management;
using Microsoft.Win32;


            richTextBox1.Text += "你的計算機名稱 : " + Environment.MachineName.ToString() + "\n";
            richTextBox1.Text += "你的網卡序號 : " + GetNetCardMacAddress() + "\n";


        //获得网卡信息函数
        public string GetNetCardMacAddress()
        {
            //创建ManagementClass对象
            ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
            ManagementObjectCollection moc = mc.GetInstances();//创建ManagementObjectCollection对象
            string str = "";//用于存储网卡序列号
            foreach (ManagementObject mo in moc)//遍历得到的集合
            {
                if ((bool)mo["IPEnabled"] == true)//判断IPEnabled属性是否为true
                    str = mo["MacAddress"].ToString();//获取网卡序列号
            }
            return str;//返回网卡序列号
        }


//---------------------------------------

            //設定regedit資料
            string strNumber = "IMS12345";
            richTextBox1.Text += "CreateSubKey : " + strNumber.TrimEnd() + "\n";
            Microsoft.Win32.RegistryKey retkey = Microsoft.Win32.Registry.CurrentUser.OpenSubKey("software", true).CreateSubKey("IMS1").CreateSubKey("IMS.INI").CreateSubKey(strNumber.TrimEnd());
            retkey.SetValue("Name", "群曜醫電");  // 設置註冊名
            retkey.SetValue("Serial", "0912345678");  //設置註冊序號

            richTextBox1.Text += "註冊成功\n";

//---------------------------------------

            //取得regedit資料
            Microsoft.Win32.RegistryKey retkey1 = Microsoft.Win32.Registry.CurrentUser.OpenSubKey("software", true).CreateSubKey("IMS1").CreateSubKey("IMS.INI");
            foreach (string strName in retkey1.GetSubKeyNames())//判断注册码是否过期
            {
                richTextBox1.Text += strName  + "\n";
            }


//---------------------------------------








            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_03_Data.mdf;Integrated Security=True;Connect Timeout=30";

            int MaxValue = 0;//表示表中的記錄

            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            SqlCommand com = new SqlCommand("select Count(*)from tb_01", con);
            MaxValue = (int)com.ExecuteScalar();
            richTextBox1.Text += "MaxValue = " + MaxValue.ToString() + "\n";
            con.Close();
            
-------------------------            

string selectString = "select au_id as 使用者編號,作者 as 使用者名,phone as 聯繫電話 from authors";

SqlCommand cmd = new SqlCommand("update 系統管理員表 set 使用者名稱='" + textBox1.Text + "',密碼='" + textBox2.Text + "'", con);

-------------------------

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

            SqlDataReader reader = cmd.ExecuteReader();            
            while (reader.Read())
            {
                Console.WriteLine(First Name: {0}, Last Name: {1}, reader.GetString(0), reader.GetString(1));
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




