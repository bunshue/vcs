using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace SeparateSQLServer
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
            biandingiInfo();
        }

        private void biandingiInfo()
        {
            string db_filename = "db_09_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                DataTable dt = new DataTable();
                SqlDataAdapter da = new SqlDataAdapter("select name from sysdatabases", cn);
                da.Fill(dt);
                this.comboBox1.DataSource = dt.DefaultView;
                this.comboBox1.DisplayMember = "name";
                this.comboBox1.ValueMember = "name";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //分離資料庫

            string db_filename = "db_09_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                try
                {
                    SqlCommand cmd = new SqlCommand();
                    cn.Open();
                    cmd.Connection = cn;
                    cmd.CommandText = "sp_detach_db @dbname='" + this.comboBox1.Text + "'";
                    cmd.ExecuteNonQuery();
                    richTextBox1.Text += "分離成功\n";
                    //MessageBox.Show("分離成功");
                }
                catch (Exception ey)
                {
                    richTextBox1.Text += "分離失敗, 原因 : \n";
                    richTextBox1.Text += ey.Message + "\n";
                    //MessageBox.Show(ey.Message);
                }
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

        private void button7_Click(object sender, EventArgs e)
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
