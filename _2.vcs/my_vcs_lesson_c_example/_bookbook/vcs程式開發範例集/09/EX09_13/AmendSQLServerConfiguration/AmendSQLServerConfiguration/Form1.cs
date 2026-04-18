using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace AmendSQLServerConfiguration
{
    public partial class Form1 : Form
    {
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

        SqlConnection con = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30");
        DataTable dt;

        string tag = "null";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showTrack();

            types();

            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串, 預處理程序
            string sqlstr = "Poc_Linshi";
            sql_read_database(db_filename, sqlstr, dataGridView2);
        }

        private void showTrack()
        {
            con.Open();

            dt = new DataTable();
            SqlDataAdapter da = new SqlDataAdapter();
            SqlCommand cmd = new SqlCommand();
            cmd.CommandType = CommandType.StoredProcedure;
            cmd.CommandText = "Poc_Linshi";
            cmd.Connection = con;
            da.SelectCommand = cmd;
            da.Fill(dt);

            this.dataGridView1.DataSource = dt.DefaultView;

            con.Close();
        }

        private void types()
        {
            string[] strtype = { "varchar", "char" };
            this.comboBox1.DataSource = strtype;
        }

        private void dataGridView1_Click(object sender, EventArgs e)
        {
            this.textBox1.Text = this.dataGridView1.SelectedCells[0].Value.ToString();
            this.comboBox1.Text = this.dataGridView1.SelectedCells[1].Value.ToString();
            this.textBox2.Text = this.dataGridView1.SelectedCells[2].Value.ToString();
            this.textBox1.Enabled = false;

            richTextBox1.Text += "dataGridView1_Click, 取得資料 :\n";
            richTextBox1.Text += "第0項 : " + this.dataGridView1.SelectedCells[0].Value.ToString() + "\n";
            richTextBox1.Text += "第1項 : " + this.dataGridView1.SelectedCells[1].Value.ToString() + "\n";
            richTextBox1.Text += "第2項 : " + this.dataGridView1.SelectedCells[2].Value.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //新增
            this.button4.Enabled = true;
            this.textBox1.Enabled = true;
            this.textBox1.Text = "";
            this.textBox2.Text = "";
            tag = "add";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //修改
            this.button4.Enabled = true;
            tag = "update";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //刪除
            if (MessageBox.Show("是否刪除", "提示", MessageBoxButtons.OKCancel, MessageBoxIcon.Question) == DialogResult.OK)
            {
                con.Open();
                string sqlstr = "alter table tb_11 drop column " + this.textBox1.Text + "";
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = sqlstr;
                cmd.Connection = con;
                cmd.ExecuteNonQuery();
                con.Close();
                showTrack();
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //執行
            try
            {
                con.Open();
                string sqlstr = string.Empty;
                if (tag == "add")
                {
                    sqlstr += "alter table tb_11 add " + this.textBox1.Text + " ";
                    sqlstr += "" + this.comboBox1.Text + "(" + this.textBox2.Text + ")";
                }
                else if (tag == "update")
                {
                    sqlstr += "alter table tb_11 alter column " + this.textBox1.Text + " ";
                    sqlstr += "" + this.comboBox1.Text + "(" + this.textBox2.Text + ")";
                }
                richTextBox1.Text += "查詢字串 : " + sqlstr + "\n";
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = sqlstr;
                cmd.Connection = con;
                cmd.ExecuteNonQuery();
                con.Close();
                showTrack();
                this.button4.Enabled = false;
            }
            catch
            {
                con.Close();
                MessageBox.Show("請輸入有效訊息");
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

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

        private void button5_Click(object sender, EventArgs e)
        {
            //以下為debug
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_11";

            sql_read_database(db_filename, sqlstr, dataGridView1);

        }
    }
}
