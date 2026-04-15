using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace AppAlias
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

            SqlConnection cn = new SqlConnection(cnstr);
            cn.Open();
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM tb_02", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "tabel");
            string[] arylist = new string[ds.Tables[0].Columns.Count];
            for (int i = 0; i < ds.Tables[0].Columns.Count; i++)
            {
                arylist[i] = ds.Tables[0].Columns[i].ColumnName;
            }
            for (int j = 0; j < ds.Tables[0].Columns.Count; j++)
            {
                comboBox1.Items.Add(arylist[j]);
            }
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            if (comboBox1.Text == "" || textBox1.Text == "")
            {
                MessageBox.Show("列名和別名不能為空!");
                return;
            }
            SqlConnection cn = new SqlConnection(cnstr);
            cn.Open();
            string str = "SELECT " + comboBox1.Text + "," + comboBox1.Text + " AS " + textBox1.Text.Trim() + " FROM tb_02";
            SqlDataAdapter dap = new SqlDataAdapter(str, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
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
            // 資料庫檔案
            string db_filename = "db_10_Data.mdf";

            string sqlstr = "SELECT * FROM tb_02";
            sql_read_database(db_filename, sqlstr, dataGridView2);
        }
    }
}
