using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace DeoxidizeSQLServer
{
    public partial class Form1 : Form
    {
        // 資料庫連線參數, 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_03_Data.mdf;Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

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

        private void button2_Click(object sender, EventArgs e)
        {
            if (this.openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                this.textBox1.Text = this.openFileDialog1.FileName;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //還原SQL Server資料庫

            Restore();
        }

        private void Restore()
        {
            string path = this.textBox1.Text; //獲得備份路徑及資料庫名稱
            string dbname = this.comboBox1.Text;

            // 連接字串
            //string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";


            string SqlStr1 = "Server=(local);database='" + this.comboBox1.Text + "';Uid=sa;Pwd=";
            string SqlStr2 = "use master restore database " + dbname + " from disk='" + path + "'";
            using (SqlConnection con = new SqlConnection(SqlStr1))
            {
                con.Open();
                try
                {
                    SqlCommand cmd = new SqlCommand(SqlStr2, con);
                    cmd.Connection = con;
                    cmd.ExecuteNonQuery();
                    //MessageBox.Show("還原數據成功");
                    richTextBox1.Text += "還原數據成功\n";
                }
                catch (Exception error)
                {
                    richTextBox1.Text += "還原數據失敗，請確保還原項與庫對應, 原因 : \n";
                    richTextBox1.Text += error.Message + "\n";
                    //MessageBox.Show("還原失敗，請確保還原項與庫對應");
                }
                finally
                {
                    con.Close();
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

        private void button3_Click(object sender, EventArgs e)
        {
            //以下為debug
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工表";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }
    }
}
