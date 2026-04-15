using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace SystemInitialization
{
    public partial class Form1 : Form
    {
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
                SqlDataAdapter da = new SqlDataAdapter("select name from tb_power", con);
                DataTable dt = new DataTable();
                da.Fill(dt);
                this.listBox1.DataSource = dt.DefaultView;
                this.listBox1.DisplayMember = "name";
                this.listBox1.ValueMember = "name";
            }
        }

        private void listBox1_Click(object sender, EventArgs e)
        {
            uncheck("false");//設定所有的CheckBox控制元件為不選取狀態

            string str = null;

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            richTextBox1.Text += "aaaaa : " + this.listBox1.Text + "\n";
            using (SqlConnection con = new SqlConnection(cnstr))//連接資料庫
            {
                SqlCommand cmd = new SqlCommand("select power from tb_power where name='" + this.listBox1.Text + "'", con);//連接SQL語句與數擾庫的連接
                cmd.Connection = con;
                cmd.Connection.Open();//打開資料庫的連接
                SqlDataReader dr = cmd.ExecuteReader();//執行SQL語句
                if (dr.HasRows)//如果有記錄
                {
                    dr.Read();//讀取下一行
                    str = dr[0].ToString();//取得權限值
                    richTextBox1.Text += "str = " + str + "\n";
                }
                dr.Close();//關閉
                con.Close();//關閉連接
                con.Dispose();
                string[] strpower = str.Split(',');//用逗號分隔字串
                for (int i = 0; i < strpower.Length; i++)//搜尋字串
                {
                    if (strpower[i] != "0")//如果使用者有權限
                    {
                        if (i + 1 == 1)//如果成立則表是有權限
                            checkBox1.Checked = true;//設為選擇狀態
                        else if (i + 1 == 2)
                            checkBox2.Checked = true;
                        else if (i + 1 == 3)
                            checkBox3.Checked = true;
                        else if (i + 1 == 4)
                            checkBox4.Checked = true;
                        else if (i + 1 == 5)
                            checkBox5.Checked = true;
                        else if (i + 1 == 6)
                            checkBox6.Checked = true;
                        else if (i + 1 == 7)
                            checkBox7.Checked = true;
                        else if (i + 1 == 8)
                            checkBox8.Checked = true;
                    }
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            uncheck("true");
        }

        private void uncheck(string str)
        {
            checkBox1.Checked = Convert.ToBoolean(str);
            checkBox2.Checked = Convert.ToBoolean(str);
            checkBox3.Checked = Convert.ToBoolean(str);
            checkBox4.Checked = Convert.ToBoolean(str);
            checkBox5.Checked = Convert.ToBoolean(str);
            checkBox6.Checked = Convert.ToBoolean(str);
            checkBox7.Checked = Convert.ToBoolean(str);
            checkBox8.Checked = Convert.ToBoolean(str);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            uncheck("false");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string strValue = null;
            if (checkBox1.Checked)
            {
                strValue += "1,";
            }
            else
            {
                strValue += "0,";
            }
            if (checkBox2.Checked)
            {
                strValue += "1,";
            }
            else
            {
                strValue += "0,";
            }
            if (checkBox3.Checked)
            {
                strValue += "1,";
            }
            else
            {
                strValue += "0,";
            }
            if (checkBox4.Checked)
            {
                strValue += "1,";
            }
            else
            {
                strValue += "0,";
            }
            if (checkBox5.Checked)
            {
                strValue += "1,";
            }
            else
            {
                strValue += "0,";
            }
            if (checkBox6.Checked)
            {
                strValue += "1,";
            }
            else
            {
                strValue += "0,";
            }
            if (checkBox7.Checked)
            {
                strValue += "1,";
            }
            else
            {
                strValue += "0,";
            }
            if (checkBox8.Checked)
            {
                strValue += "1";
            }
            else
            {
                strValue += "0";
            }

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection con = new SqlConnection(cnstr))
            {
                SqlCommand cmd = new SqlCommand("update tb_Power set power='" + strValue + "' where name='" + this.listBox1.Text + "' ", con);
                cmd.Connection = con;
                cmd.Connection.Open();
                cmd.ExecuteNonQuery();
                MessageBox.Show("授權成功！！！");
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
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";

            string sqlstr = "select name from tb_power";
            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

    }
}
