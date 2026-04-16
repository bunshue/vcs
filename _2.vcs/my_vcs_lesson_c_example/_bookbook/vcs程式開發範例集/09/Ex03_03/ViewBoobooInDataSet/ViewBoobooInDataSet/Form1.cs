using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace ViewBoobooInDataSet
{
    public partial class Form1 : Form
    {
        // 資料庫連線參數, 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_03_Data.mdf;Integrated Security=True;Connect Timeout=30";

        int MaxValue = 0;//表示表中的記錄
        int State = 1;//狀態記錄

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            SqlCommand com = new SqlCommand("select Count(*)from tb_01", con);
            MaxValue = (int)com.ExecuteScalar();
            richTextBox1.Text += "MaxValue = " + MaxValue.ToString() + "\n";
            con.Close();
        }

        public void Find(int first, int next)
        {
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            DataTable dt = new DataTable();
            SqlDataAdapter da = new SqlDataAdapter("select * from tb_01", con);
            da.Fill(first, next, dt);
            if (dt.Rows[0][1].ToString() == "")
            {
                textBox1.Text = "";
                errorProvider1.SetError(textBox1, "用戶名綁定有空項");
            }
            else
            {
                errorProvider1.SetError(textBox1, "");
                textBox1.Text = dt.Rows[0][1].ToString();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (MaxValue > 0)
            {
                Find(0, 1);
                State = 1;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (State < MaxValue)
            {
                Find(State, State + 1);
                State = State + 1;
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
            string sqlstr = "SELECT * FROM ddddd";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }
    }
}
