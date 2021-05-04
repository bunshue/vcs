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
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);database=db_10;Uid=sa;Pwd=");//連接數據庫
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
            SqlConnection cn = new SqlConnection("server=(local);database=db_10;Uid=sa;Pwd=");//連接數據庫
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM tb_08 WHERE " + comboBox1.Text + " IS null OR " + comboBox1.Text + "=''", cn);//透過SQL語句查詢數據表中的空數據
            DataSet ds = new DataSet();//實例化DataSet類
            dap.Fill(ds);//更新行
            dataGridView1.DataSource = ds.Tables[0].DefaultView;//顯示查詢後的數據
        }
    }
}