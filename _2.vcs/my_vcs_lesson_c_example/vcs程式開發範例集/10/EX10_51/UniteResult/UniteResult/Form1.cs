using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace UniteResult
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);user id=sa;pwd=;Database=db_10");
            SqlDataAdapter dap = new SqlDataAdapter("select * from 顧客表, 僱員表", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);user id=sa;pwd=;Database=db_10");
            SqlDataAdapter dap = new SqlDataAdapter("select 顧客編號 as 編號,顧客姓名 as 姓名,所在城市,郵編 from 顧客表 union select 僱員編號,僱員名稱,家庭住址,郵編 from 僱員表", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}