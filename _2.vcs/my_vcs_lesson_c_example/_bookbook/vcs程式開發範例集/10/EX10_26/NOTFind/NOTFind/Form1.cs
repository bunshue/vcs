using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace NOTFind
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;uid=sa;pwd=;");
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_kf", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "hotal");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
        private void dataGridViewBind(string sqlStr)
        {
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;uid=sa;pwd=;");
            SqlDataAdapter dap = new SqlDataAdapter(sqlStr, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "hotal");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            this.dataGridViewBind("select * from tb_kf where 房態='空房 '");
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            this.dataGridViewBind("select * from tb_kf where 房態='入住'");
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            this.dataGridViewBind("select * from tb_kf where 房態='空房 ' and not(價格 between 80 and 150 )");
        }

    }
}