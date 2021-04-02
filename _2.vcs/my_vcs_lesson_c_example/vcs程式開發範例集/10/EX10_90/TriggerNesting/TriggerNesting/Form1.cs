using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace TriggerNesting
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
            SqlCommand cmd = new SqlCommand("update 部門工資統計表 set 基本工資=" + Convert.ToInt32(textBox2.Text) + "where 員工姓名 = '" + textBox1.Text + "'", con);
            con.Open();
            cmd.ExecuteNonQuery();
            con.Close();
            MessageBox.Show("修改成功！");
            this.Form1_Load(sender, e);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("select * from 部門工資統計表 select * from 明細工資表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
            dataGridView2.DataSource = ds.Tables[1].DefaultView;
        }
    }
}