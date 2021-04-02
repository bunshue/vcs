using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace COUNTMax
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);user id=sa;pwd=;Database=db_10");
            SqlDataAdapter dap = new SqlDataAdapter("select count(distinct 日期) as 商品數 from tb_sell where 銷價 >500", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            textBox1.Text = ds.Tables[0].Rows[0][0].ToString();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);user id=sa;pwd=;Database=db_10");
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_sell", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}