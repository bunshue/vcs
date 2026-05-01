


準備搬進 簡易測試 的

//idx  /  資料庫檔案  /  查詢字串1  /  說明1 /  查詢字串2  /  說明2/  查詢字串3  /  說明3

-------------------------------------------------------------------



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




