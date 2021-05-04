using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace RepeatFind
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;uid=sa;pwd=;");
            SqlDataAdapter dap = new SqlDataAdapter("select Count(書號)as 記錄條數, 書號,書名,作者 from tb_xsb group by 書號,書名,作者 Having Count(書號)>1", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "book");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;uid=sa;pwd=;");
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_xsb", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "book");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}