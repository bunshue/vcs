using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace SonFindDerive
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);user id=sa;pwd=;Database=db_10");
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM tb_Stu", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);user id=sa;pwd=;Database=db_10");
            SqlDataAdapter dap = new SqlDataAdapter("SELECT 學生姓名, count(*) AS 相同數量 FROM (SELECT top 10 學生姓名 FROM tb_Stu order BY 學生編號 asc )as T GROUP BY 學生姓名", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}