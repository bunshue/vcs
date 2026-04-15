using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace ProcedureUpData
{
    public partial class Form1 : Form
    {
        DataTable dt = null;

        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

        SqlConnection con;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            con = new SqlConnection(cnstr);

            showList();

            string id = "P1005";  // textbox1 員工編號
            string name = "david";  // textbox2 員工姓名
            string money = "34567";  // textbox4 基本工資
            string talk = "Very good";  // textbox5 工作評價
            textBox1.Text = id;
            textBox2.Text = name;
            textBox4.Text = money;
            textBox5.Text = talk;
        }

        private void listView1_Click(object sender, EventArgs e)
        {
            string str = this.listView1.SelectedItems[0].Text.ToString();
            richTextBox1.Text += "你選擇了 : " + str + "\n";
            showInfo(str);
        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {
            string id = "P1005";  // textbox1 員工編號
            string name = "david";  // textbox2 員工姓名
            string money = "34567";  // textbox4 基本工資
            string talk = "Very good";  // textbox5 工作評價

            if (TextClear())
            {
                using (SqlCommand cmd = new SqlCommand())
                {
                    con.Open();
                    cmd.Connection = con;
                    cmd.CommandType = CommandType.StoredProcedure;
                    cmd.CommandText = "proc_Update";
                    SqlParameter[] par =
                    { 
                        new SqlParameter("@id",this.textBox1.Text), 
                        new SqlParameter("@name",this.textBox2.Text),
                        new SqlParameter("@money",this.textBox4.Text),
                        new SqlParameter("@talk",this.textBox5.Text)
                    };
                    foreach (SqlParameter parms in par)
                    {
                        cmd.Parameters.Add(parms);
                    }
                    cmd.ExecuteNonQuery();
                    con.Close();
                    MessageBox.Show("修改成功");
                    showList();
                }
            }
            else
            {
                MessageBox.Show("請選擇訊息");
            }
        }

        private Boolean TextClear()
        {
            foreach (Control c in this.groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    if (c.Text == "")
                    {
                        return false;
                    }
                    else
                    {
                        return true;
                    }
                }
            }
            return true;
        }

        private void showList()
        {
            listView1.View = View.Details;//圖示
            listView1.GridLines = true;//網格線
            using (SqlDataAdapter da = new SqlDataAdapter("select * from 員工表", con))
            {
                //產生結果集
                dt = new DataTable();
                da.Fill(dt);
                ColumnHeader ch;
                for (int i = 0; i < dt.Columns.Count; i++)//列
                {
                    ch = new ColumnHeader();
                    ch.Text = dt.Columns[i].ColumnName.ToString();
                    ch.Name = dt.Columns[i].ColumnName.ToString();
                    ch.Width = 72;

                    this.listView1.Columns.Add(ch);
                }

                //建立結構
                listView1.Items.Clear();
                ListViewItem listItem = null;
                for (int j = 0; j < dt.Rows.Count; j++)
                {
                    listItem = new ListViewItem(dt.Rows[j][0].ToString());
                    for (int k = 1; k < dt.Columns.Count; k++)
                    {
                        listItem.SubItems.Add(dt.Rows[j][k].ToString());
                    }
                    listView1.Items.Add(listItem);
                }
            }
        }

        private void showInfo(string strid)
        {
            using (SqlCommand cmd = new SqlCommand("select * from 員工表 where 員工編號='" + strid + "'", con))
            {
                con.Open();
                SqlDataReader dr = cmd.ExecuteReader();
                if (dr.HasRows)
                {
                    dr.Read();
                    this.textBox1.Text = dr[0].ToString();
                    this.textBox2.Text = dr[1].ToString();
                    this.textBox4.Text = dr[2].ToString();
                    this.textBox5.Text = dr[3].ToString();
                }
                dr.Close();
                con.Close();
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
            string sqlstr = "SELECT * FROM 員工表";

            sql_read_database(db_filename, sqlstr, dataGridView1);

        }
    }
}
