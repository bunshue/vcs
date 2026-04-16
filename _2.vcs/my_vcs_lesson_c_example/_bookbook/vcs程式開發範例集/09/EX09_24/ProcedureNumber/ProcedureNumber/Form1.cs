using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Text.RegularExpressions;
using System.Data.SqlClient;

namespace ProcedureNumber
{
    public partial class Form1 : Form
    {
        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            AutoID();

            string id = "P1013";  // textbox1 員工編號
            string name = "david";  // textbox2 員工姓名
            string age = "18";  // textbox3 員工年齡
            string money = "34567";  // textbox5 基本工資
            string idcard = "P123456789";  // textbox4 身分證號

            //textBox1.Text = id;
            textBox2.Text = name;
            textBox3.Text = age;
            textBox5.Text = money;
            textBox4.Text = idcard;
        }

        private void textBox3_Validating(object sender, CancelEventArgs e)
        {
            try
            {
                int x = Int32.Parse(textBox3.Text);

                if (x < 60 && x > 20)
                {
                    errorage.SetError(this.textBox3, "");
                }
                else
                {
                    errorage.SetError(this.textBox3, "數值應在20-60之間");
                }
            }
            catch
            {
                errorage.SetError(this.textBox3, "應為整數");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (ifNull())
            {
                if (info())
                {
                    if (IDCard(this.textBox4.Text))
                    {
                        richTextBox1.Text += "做 InsertInfo()\n";
                        InsertInfo();
                    }
                    else
                    {
                        MessageBox.Show("身份證號格式不正確");
                    }
                }
            }
            else
            {
                MessageBox.Show("請將訊息新增完整");
            }
        }

        public bool IDCard(string ID)
        {
            richTextBox1.Text += "檢查身份證號格式\n";
            if (!Regex.IsMatch(ID, @"^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$"))  //15ID
            {
                if (Regex.IsMatch(ID,
                @"^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{4}$"))  //18ID
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }

        private bool info()
        {
            for (int i = 0; i < this.textBox5.Text.Length; i++)
            {
                if (!char.IsNumber(this.textBox5.Text[i]))
                {
                    if (this.textBox5.Text[i] != '.')
                    {
                        MessageBox.Show("工資訊息有誤");
                        return false;
                    }
                }
            }
            return true;
        }

        private bool ifNull()
        {
            foreach (Control Con in this.Controls)
            {
                if (Con is TextBox)
                {
                    if (Con.Text == "")
                    {
                        return false;
                    }
                }
            }
            return true;
        }

        private void NullValue()
        {
            foreach (Control Con in this.Controls)
            {
                if (Con is TextBox)
                {
                    Con.Text = "";
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void AutoID()
        {
            using (SqlConnection con = new SqlConnection(cnstr))
            {
                // 查詢字串
                string sqlstr = "SELECT Max(tb_ID) FROM 員工個人訊息";

                con.Open();
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = sqlstr;
                cmd.Connection = con;
                string str = cmd.ExecuteScalar().ToString();
                if (str == "")
                {
                    this.textBox1.Text = "P1001";
                }
                else
                {
                    this.textBox1.Text = "P" + Convert.ToString(Convert.ToInt32(str.Substring(1)) + 1);
                }
            }
        }

        private void InsertInfo()
        {
            string new_id = "P1018";  // 員工編號
            string new_name = "david";  // 員工姓名
            string new_age = "18";  // 員工年齡
            string new_money = "34567";  // 基本工資
            string new_idcard = "P123456789";  // 身分證號
            
            using (SqlConnection con = new SqlConnection(cnstr))
            {
                con.Open();
                SqlCommand cmd = new SqlCommand();
                string strSql = "insert into 員工個人訊息 values ('" + new_id + "','" + new_name + "','" + new_age + "','" + new_money + "','" + new_idcard + "')";
                cmd.CommandText = strSql;
                cmd.Connection = con;
                cmd.ExecuteNonQuery();
                con.Close();
                MessageBox.Show("成功新增訊息");
                NullValue();
            }
            AutoID();
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
            string sqlstr = "SELECT Max(tb_ID) FROM 員工個人訊息";
            sqlstr = "SELECT * FROM 員工個人訊息";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }
    }
}
