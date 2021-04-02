using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace FindDate
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);database=db_10;Uid=sa;Pwd=");
            cn.Open();
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM tb_07 WHERE 出生日期='" + dateTimePicker1.Value.Date+ "'", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}