using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace ComplexFind
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string sqlstr = "select * from tb_stu where 學生編號 like '"
            + textBox1.Text + "%' and (( 學生姓名 like '"
            + textBox2.Text + "_') or (年齡 like '[^"
            + textBox3.Text + "][0-9]'))";
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;UID=sa;pwd=;");
            SqlDataAdapter dap = new SqlDataAdapter(sqlstr, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;UID=sa;pwd=;");
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_stu", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}