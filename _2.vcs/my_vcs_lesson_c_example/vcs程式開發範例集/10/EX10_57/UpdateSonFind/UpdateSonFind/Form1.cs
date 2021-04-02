using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace UpdateSonFind
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
            SqlDataAdapter dap = new SqlDataAdapter("select * from 員工工資表 select * from 規定工資表", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            dataGridView2.DataSource = ds.Tables[1].DefaultView;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("server=(local);user id=sa;pwd=;DataBase=db_10");
            con.Open();
            string SqlStr = "update 員工工資表 set 基本工資=(select 基本工資 from 規定工資表 where 工作時間='" + comboBox1.Text + "') where 員工姓名='" + textBox1.Text+ "'";
            SqlCommand cmd = new SqlCommand(SqlStr, con);
            cmd.ExecuteNonQuery();
            con.Close();
            //SqlDataAdapter dap = new SqlDataAdapter("select * from 員工工資表", con);
            //DataSet ds = new DataSet();
            //dap.Fill(ds);
            //dataGridView1.DataSource = ds.Tables[0].DefaultView;
            this.Form1_Load(sender, e);
        }
    }
}