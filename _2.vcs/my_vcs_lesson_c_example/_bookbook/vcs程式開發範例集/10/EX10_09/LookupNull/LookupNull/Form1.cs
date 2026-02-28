using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace LookupNull
{
    public partial class Form1 : Form
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\{0};Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);//連接數據庫
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM tb_08", cn);//透過SQL語句取得數據表中的訊息
            DataSet ds = new DataSet();//實例化DataSet類
            dap.Fill(ds);//更新行
            string[] arylist = new string[ds.Tables[0].Columns.Count];//用數據表的列數定義數組
            for (int i = 0; i < ds.Tables[0].Columns.Count; i++)
                arylist[i] = ds.Tables[0].Columns[i].ColumnName;//取得數據表中的字段名稱
            for (int j = 0; j < ds.Tables[0].Columns.Count; j++)//向ComboBox控制元件中新增字段名稱
                comboBox1.Items.Add(arylist[j]);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;//顯示數據表中的數據
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);//連接數據庫
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM tb_08 WHERE " + comboBox1.Text + " IS null OR " + comboBox1.Text + "=''", cn);//透過SQL語句查詢數據表中的空數據
            DataSet ds = new DataSet();//實例化DataSet類
            dap.Fill(ds);//更新行
            dataGridView1.DataSource = ds.Tables[0].DefaultView;//顯示查詢後的數據
        }
    }
}