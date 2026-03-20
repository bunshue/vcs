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
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from 員工工資表 select * from 規定工資表", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            dataGridView2.DataSource = ds.Tables[1].DefaultView;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            string SqlStr = "update 員工工資表 set 基本工資=(select 基本工資 from 規定工資表 where 工作時間='" + comboBox1.Text + "') where 員工姓名='" + textBox1.Text + "'";
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
