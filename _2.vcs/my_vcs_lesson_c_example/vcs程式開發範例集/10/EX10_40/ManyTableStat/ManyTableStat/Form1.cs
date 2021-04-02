using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace ManyTableStat
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);uid=sa;pwd=;Database=db_10");
            SqlDataAdapter dap = new SqlDataAdapter("select * from xsb", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);uid=sa;pwd=;Database=db_10");
            SqlDataAdapter dap = new SqlDataAdapter("select k.書號,k.書名,x.作者, sum(k.現存數量)as 現存數量 ,sum(x.銷售數量)as 銷售數量 from xsb x ,kcb k where x.書號=k.書號  group by k.書號,k.書名,x.作者, k.現存數量 order by 1", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}