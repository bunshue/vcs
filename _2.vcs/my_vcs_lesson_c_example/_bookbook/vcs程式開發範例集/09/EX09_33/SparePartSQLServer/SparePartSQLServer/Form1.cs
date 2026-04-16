using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.IO;
using System.Data.SqlClient;

namespace SparePartSQLServer
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
            string db_filename = "db_09_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            using (SqlConnection con = new SqlConnection(cnstr))
            {
                DataTable dt = new DataTable();
                SqlDataAdapter da = new SqlDataAdapter("select name from sysdatabases", con);
                da.Fill(dt);
                this.comboBox1.DataSource = dt.DefaultView;
                this.comboBox1.DisplayMember = "name";
                this.comboBox1.ValueMember = "name";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //備份

            string db_filename = "db_09_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            try
            {
                sd.InitialDirectory = Application.StartupPath + "\\";//預設路徑為D：//
                sd.FilterIndex = 1;								//預設值為第一個
                sd.RestoreDirectory = true;						//重新定位保存路徑
                sd.Filter = "備份文件 (*.bak)|*.bak|所有文件 (*.*)|*.*";//過濾器，定義文件類型
                if (sd.ShowDialog() == DialogResult.OK)
                {
                    if (!File.Exists(sd.FileName.ToString()))
                    {
                        SqlConnection con = new SqlConnection();		//利用程式碼完成連接資料庫

                        // 連接字串
                        //string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

                        con.ConnectionString = "server=.;uid=sa;pwd=;database='" + this.comboBox1.Text + "'";
                        con.Open();
                        SqlCommand com = new SqlCommand();
                        this.textBox1.Text = sd.FileName.ToString();
                        com.CommandText = "BACKUP DATABASE " + this.comboBox1.Text + " TO DISK = '" + sd.FileName.ToString() + "'";
                        com.Connection = con;							//連接
                        com.ExecuteNonQuery();						    //執行
                        con.Close();
                        con.Dispose();
                        richTextBox1.Text += "數據備份成功\n";
                    }
                    else
                    {
                        richTextBox1.Text += "請重新命名\n";
                    }
                }
            }
            catch (Exception k)
            {
                richTextBox1.Text += "數據備份失敗, 原因 : \n";
                richTextBox1.Text += k.Message + "\n";

                return;
            }
        }

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

        private void button2_Click(object sender, EventArgs e)
        {
            return;

            //以下為debug
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM ddddd";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }
    }
}
