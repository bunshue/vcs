using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace AddOnsSQLServer
{
    public partial class Form1 : Form
    {
        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (this.openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                this.textBox3.Text = this.openFileDialog1.FileName;
                this.button3.Enabled = true;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (this.openFileDialog2.ShowDialog() == DialogResult.OK)
            {
                this.textBox2.Text = this.openFileDialog2.FileName;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (this.textBox3.Text != "")
            {
                fujia();
            }
            else
            {
                MessageBox.Show("請輸入資料庫名");
            }
        }

        private void fujia()
        {
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection cn = new SqlConnection(cnstr))
            {
                try
                {
                    SqlCommand cmd = new SqlCommand();
                    cn.Open();
                    cmd.Connection = cn;
                    StringBuilder sb = new StringBuilder();
                    sb.Append("sp_attach_db @dbname='" + this.textBox1.Text + "',");
                    sb.Append("@filename1='" + this.textBox3.Text + "'");
                    if (this.textBox2.Text != "")
                    {
                        sb.Append(",@filename2='" + this.textBox2.Text + "'");
                    }
                    cmd.CommandText = sb.ToString();
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("附加成功");
                    this.button3.Enabled = false;
                }
                catch (Exception ety)
                {
                    MessageBox.Show(ety.Message);
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

        private void button4_Click(object sender, EventArgs e)
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
