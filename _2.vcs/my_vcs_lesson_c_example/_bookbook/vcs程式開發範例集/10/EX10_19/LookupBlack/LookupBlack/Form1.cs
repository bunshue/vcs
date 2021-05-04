using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace LookupBlack
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //設定統計查詢的SQL語句
            string sqlstr = "select top 10 書號,書名,sum(銷售數量)as 合計銷售數量 from tb_xsb group by 書號,書名,作者 order by 3 asc";
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;UID=SA;PWD=;");//連接數據庫
            SqlDataAdapter dap = new SqlDataAdapter(sqlstr, cn);//數據庫和SQL語句的連接
            DataSet ds = new DataSet();//實例化DataSet類
            dap.Fill(ds);//更新行
            dataGridView1.DataSource = ds.Tables[0].DefaultView;//顯示統計後的數據
         }

        private void Form1_Load(object sender, EventArgs e)
        {
            string sqlstr = "select * from tb_xsb";
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;UID=sa;PWD=;");
            SqlDataAdapter dap = new SqlDataAdapter(sqlstr, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}