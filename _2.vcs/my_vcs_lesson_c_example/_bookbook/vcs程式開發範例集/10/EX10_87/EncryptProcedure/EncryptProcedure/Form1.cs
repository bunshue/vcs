using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace EncryptProcedure
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
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            SqlCommand cmd = new SqlCommand("ALTER  PROCEDURE [insert_加密學生訊息表](@姓名_2 [varchar](50),@性別_3	[varchar](50),@年齡_4 [int],@籍貫_5 [varchar](50),@課程編號_6 [varchar](50)) AS INSERT INTO [db_10].[dbo].[學生訊息表] ([姓名],[性別],[年齡], [籍貫],[課程編號]) VALUES (@姓名_2, @性別_3, @年齡_4, @籍貫_5, @課程編號_6)", con);
            cmd.CommandType = CommandType.Text;
            cmd.ExecuteNonQuery();
            con.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("exec sp_helptext insert_加密學生訊息表", con);
            dap.SelectCommand.CommandType = CommandType.Text;
            DataSet ds = new DataSet();
            dap.Fill(ds);
            try
            {
                textBox1.Text = ds.Tables[0].Rows[0][0].ToString();
            }
            catch
            {
                textBox1.Text = "該預儲程序已加密，無法檢視！";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            SqlCommand cmd = new SqlCommand("ALTER  PROCEDURE [insert_加密學生訊息表](@姓名_2 [varchar](50),@性別_3	[varchar](50),@年齡_4 [int],@籍貫_5 [varchar](50),@課程編號_6 [varchar](50)) with encryption AS INSERT INTO [db_10].[dbo].[學生訊息表] ([姓名],[性別],[年齡], [籍貫],[課程編號]) VALUES (@姓名_2, @性別_3, @年齡_4, @籍貫_5, @課程編號_6)", con);
            cmd.CommandType = CommandType.Text;
            cmd.ExecuteNonQuery();
            con.Close();
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

        private void button3_Click(object sender, EventArgs e)
        {
            //以下為debug
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM ddddd";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }
    }
}
