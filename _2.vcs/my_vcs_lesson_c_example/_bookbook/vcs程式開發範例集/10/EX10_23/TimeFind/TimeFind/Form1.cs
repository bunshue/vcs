using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace TimeFind
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string sqlstr = "select 書號,書名,作者,單價,銷售數量,金額,日期 from tb_xsb where 日期 between'" + dateTimePicker1.Value.Date + "'and '" + dateTimePicker2.Value.Date + "' order by 日期";
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;Uid=sa;pwd=;");
            SqlDataAdapter dap = new SqlDataAdapter(sqlstr, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string sqlstr = "select * from tb_xsb";
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;Uid=sa;pwd=;");
            SqlDataAdapter dap = new SqlDataAdapter(sqlstr, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}