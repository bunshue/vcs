using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace SnowfallFind
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);uid=sa;pwd=;Database=db_10");
            SqlDataAdapter dap = new SqlDataAdapter("select distinct 書號,書名,作者,出版社,現存數量 from tb_kcb order by 現存數量 desc ", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);uid=sa;pwd=;Database=db_10");
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_kcb", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}