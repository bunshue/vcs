using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace FROMClause
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
            SqlDataAdapter dap = new SqlDataAdapter("select  distinct s.學生編號,s.學生姓名,s.性別,s.出生年月,s.年齡,s.所在學院,s.所學專業,m.高數 from tb_stu s ,tb_mark m where s.學生編號=m.學生編號 and m.高數 >85", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);user id=sa;pwd=;Database=db_10");
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_stu s ,tb_mark", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}