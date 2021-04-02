using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace UniteFind
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("select 考生編號,姓名,考生類別 From 高考學生訊息表 where 籍貫='中國北京' UNION select 考生編號,姓名,考生類別 from 高考成績表  where 總成績 > 500 AND 考生類別='文科考生'", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView3.DataSource = ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("select * From 高考學生訊息表 select * from 高考成績表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            dataGridView2.DataSource = ds.Tables[1].DefaultView;
        }
    }
}