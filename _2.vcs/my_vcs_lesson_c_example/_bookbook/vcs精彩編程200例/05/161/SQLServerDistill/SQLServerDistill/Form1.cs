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
        string filename = @"D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_20.mdf";
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_20_log.LDF";   another

        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton2.Checked == true)
            {
                textBox1.Enabled = true;
                textBox2.Enabled = true;
            }
            else
            {
                textBox1.Text = "";
                textBox2.Text = "";
                textBox1.Enabled = false;
                textBox2.Enabled = false;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            comboBox1.Text = "";
            comboBox2.Items.Clear();
            comboBox2.Enabled = false;
            comboBox3.Items.Clear();
            comboBox3.Enabled = false;
            radioButton1.Checked = false;
            radioButton2.Checked = false;
        }

        // 登录服务器
        private void button2_Click(object sender, EventArgs e)
        {
            if (comboBox1.Text == "")
            {
                MessageBox.Show("请选择服务器名称：");
                comboBox1.Focus();
                return;
            }// end if 
            else
            {

                if (radioButton1.Checked == false && radioButton2.Checked == false)
                {
                    MessageBox.Show("请选择登录方式");
                    return;
                }

                //Windows身份验证
                if (radioButton1.Checked == true)
                {

                    SqlConnection con = getCon("master");
                    SqlCommand com = new SqlCommand("select name from sysdatabases", con);
                    SqlDataReader dr = com.ExecuteReader();
                    while (dr.Read())
                    {
                        comboBox2.Items.Add(dr[0].ToString());
                    }
                    dr.Close();
                    con.Close();
                    MessageBox.Show("登录成功");
                    comboBox2.Enabled = true;
                    comboBox3.Enabled = true;
                }

                //Server身份验证
                if (radioButton2.Checked == true)
                {
                    try
                    {
                        SqlConnection con = getCon("master");
                        SqlCommand com = new SqlCommand("select name from sysdatabases", con);
                        SqlDataReader dr = com.ExecuteReader();
                        while (dr.Read())
                        {
                            comboBox2.Items.Add(dr[0].ToString());
                        }
                        dr.Close();
                        con.Close();
                        MessageBox.Show("登录成功");
                        comboBox2.Enabled = true;
                        comboBox3.Enabled = true;
                    }
                    catch (Exception ee)
                    {
                        MessageBox.Show(ee.Message);
                    }
                }
            }
        }

        //提取表结构
        private void button3_Click(object sender, EventArgs e)
        {
            if (comboBox2.Text == "" && comboBox3.Text == "")
            {
                MessageBox.Show("请选择提取的表");
            }
            else
            {
                if (comboBox3.Text != "")//选择要提取的表
                {
                    SqlConnection con = getCon(comboBox2.Text);
                    SqlCommand com = new SqlCommand();
                    com.CommandText = "sp_mshelpcolumns";//存储过程名
                    com.CommandType = CommandType.StoredProcedure;
                    com.Connection = con;
                    com.Parameters.Add("@tablename", SqlDbType.NVarChar, 517);
                    com.Parameters["@tablename"].Value = comboBox3.Text;
                    SqlDataReader dr = com.ExecuteReader();
                    Form2 frm2 = new Form2(comboBox3.Text);
                    frm2.listView1.Items.Clear();
                    while (dr.Read())
                    {
                        ListViewItem lt = new ListViewItem(dr[0].ToString());
                        lt.SubItems.Add(dr[2].ToString());
                        lt.SubItems.Add(dr[3].ToString());
                        frm2.listView1.Items.Add(lt);
                    }
                    dr.Close();
                    con.Close();
                    frm2.Show();
                }

            }
        }//是以何种方式登录，是Windows集成方式，不是SQlserver方式。

        public SqlConnection getCon(string strDatabase)
        {
            // 這種 cnstr Integrated Security=SSPI 應該都沒有用了
            SqlConnection con = null; ;
            if (radioButton1.Checked == true)
            {
                string cnstr = "Integrated Security=SSPI;Persist Security Info=False;Initial Catalog= '" + strDatabase + "';Data Source='" + comboBox1.Text + "'";
                con = new SqlConnection(cnstr);
                con.Open();
            }
            if (radioButton2.Checked == true)
            {
                string cnstr = "server='" + comboBox1.Text + "';uid='" + textBox1.Text.Trim() + "';pwd='" + textBox2.Text + "';database='" + strDatabase + "'";
                con = new SqlConnection(cnstr);
                con.Open();
            }
            return con;
        }//end block

        public void getTables(string strDataBase, string U)
        {
            SqlConnection con = getCon(strDataBase);
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


        //以下為debug ------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
            //以下為debug
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Employee";

            //sql_read_database(db_filename, sqlstr, dataGridView1);
        }

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



    }
}

/*
string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

string db_filename = "db_09_Data.MDF";
string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
*/

