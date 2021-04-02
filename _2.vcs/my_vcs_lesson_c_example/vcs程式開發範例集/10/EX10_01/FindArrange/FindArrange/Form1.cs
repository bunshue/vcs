using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace FindArrange
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string cmdtxt = "SELECT 學生編號,學生姓名 FROM tb_01";
            SqlConnection cn = new SqlConnection("server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter(cmdtxt, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds,"table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}