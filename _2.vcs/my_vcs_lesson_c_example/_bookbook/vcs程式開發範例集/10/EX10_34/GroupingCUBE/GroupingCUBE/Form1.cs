using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace GroupingCUBE
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
            SqlDataAdapter dap= new SqlDataAdapter("select 所屬部門,性別,avg(工資)as 平均工資 from 工資表 group by 所屬部門,性別 with cube", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource=ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);user id=sa;pwd=;Database=db_10");
            SqlDataAdapter dap= new SqlDataAdapter("select * from 工資表", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource=ds.Tables[0].DefaultView;
        }
    }
}