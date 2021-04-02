using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace ProcedureUpData
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
            con.Open();
            SqlCommand cmd = new SqlCommand("procUpdateEmployee", con);
            cmd.CommandType = CommandType.StoredProcedure;
            SqlParameter[] prams = {
			        new SqlParameter("@員工編號",  SqlDbType.VarChar, 50),
                	new SqlParameter("@員工姓名",  SqlDbType.VarChar, 50),
                	new SqlParameter("@身份證號",  SqlDbType.VarChar, 50),
                    new SqlParameter("@聯繫電話",  SqlDbType.VarChar, 50)
			};
            prams[0].Value = textBox1.Text;
            prams[1].Value = textBox2.Text;
            prams[2].Value = textBox3.Text;
            prams[3].Value = textBox4.Text;
            // 依次把參數傳入命令文字
            foreach (SqlParameter parameter in prams)
            {
                cmd.Parameters.Add(parameter);
            }
            cmd.ExecuteNonQuery();
            this.Form1_Load(sender, e);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("select * from 員工訊息表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}