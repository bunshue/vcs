using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace SQLServerDistill
{
    public partial class Form1 : Form
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Enabled = true;
            textBox2.Enabled = true;
            textBox1.Text = "david";
            textBox2.Text = "12345";

            comboBox1.Text = "";
            comboBox2.Items.Clear();
            comboBox3.Items.Clear();
            radioButton1.Checked = true;
            radioButton2.Checked = true;
            comboBox2.Enabled = true;
            comboBox3.Enabled = true;

        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 登录服务器

            // 資料庫檔案
            string db_filename = "db_20.mdf";
            // 查詢字串
            string sqlstr = "select name from sysdatabases";


            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            using (SqlConnection con = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                con.Open();  // 打開資料庫連線
                SqlCommand com = new SqlCommand(sqlstr, con);
                SqlDataReader dr = com.ExecuteReader();
                while (dr.Read())
                {
                    comboBox2.Items.Add(dr[0].ToString());
                    richTextBox1.Text += dr[0].ToString() + "\n";
                }
                dr.Close();
                con.Close();
                MessageBox.Show("登录成功");
            }
        }

        //提取表结构
        private void button3_Click(object sender, EventArgs e)
        {
            Form2 frm2 = new Form2("ddddd");
            frm2.listView1.Items.Clear();

            // 資料庫檔案
            string db_filename = "animals1_db.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM animals1_table";

            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            //讀取資料庫
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串, 可有可無
                cn.Open();  // 打開資料庫連線

                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器

                while (dr.Read())  // 讀取一筆資料到dr
                {
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        richTextBox1.Text += dr[i].ToString();
                        //richTextBox1.Text += dr.GetValue(i).ToString();  // same
                        if (i == (dr.FieldCount - 1))
                        {
                            richTextBox1.Text += "\n";
                        }
                        else
                        {
                            richTextBox1.Text += "\t";
                        }
                    }


                    ListViewItem lt = new ListViewItem(dr[0].ToString());
                    lt.SubItems.Add(dr[2].ToString());
                    lt.SubItems.Add(dr[3].ToString());
                    frm2.listView1.Items.Add(lt);

                }
                dr.Close();
            }

            frm2.Show();
        }

        public void getTables(string cnstr, string U)
        {
            SqlConnection con = new SqlConnection(cnstr);
            SqlCommand com = new SqlCommand("select name from sysobjects where Xtype='" + U + "'", con);
            SqlDataReader dr = com.ExecuteReader();
            comboBox3.Items.Clear();
            while (dr.Read())
            {
                comboBox3.Items.Add(dr[0].ToString());
            }//
            dr.Close();
            con.Close();
        }

        //填充数据库中的表
        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox2.SelectedItem.ToString() != "")
            {
                getTables(comboBox2.SelectedItem.ToString(), "U");
            }
        }

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

        private void button4_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "db_20.mdf";

            // 查詢字串
            string sqlstr = "select name from sysdatabases";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }
    }
}
