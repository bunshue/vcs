using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace AppAlias
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("server=(local);database=db_10;Uid=sa;Pwd=");
            cn.Open();
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM tb_02", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "tabel");
            string[] arylist = new string[ds.Tables[0].Columns.Count];
            for (int i = 0; i < ds.Tables[0].Columns.Count; i++)
            {
                arylist[i] = ds.Tables[0].Columns[i].ColumnName;
            }
            for (int j = 0; j < ds.Tables[0].Columns.Count; j++)
            {
                comboBox1.Items.Add(arylist[j]);
            }
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (comboBox1.Text == "" || textBox1.Text=="")
            {
                MessageBox.Show("列名和別名不能為空!");
                return;
            }
            SqlConnection cn = new SqlConnection("server=(local);database=db_10;Uid=sa;Pwd=");
            cn.Open();
            string str = "SELECT " + comboBox1.Text + "," + comboBox1.Text + " AS " + textBox1.Text.Trim() + " FROM tb_02";
            SqlDataAdapter dap = new SqlDataAdapter(str, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}