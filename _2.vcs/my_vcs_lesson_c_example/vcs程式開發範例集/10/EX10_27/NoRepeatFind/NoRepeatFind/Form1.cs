using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace NoRepeatFind
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
            SqlDataAdapter dap = new SqlDataAdapter("select distinct 書號,條形碼,書名,作者,出版社 from tb_xsb", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "book");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;uid=sa;pwd=;");
            SqlDataAdapter dap = new SqlDataAdapter("select distinct 書號,條形碼,書名,作者,出版社 from tb_xsb", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "book");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}