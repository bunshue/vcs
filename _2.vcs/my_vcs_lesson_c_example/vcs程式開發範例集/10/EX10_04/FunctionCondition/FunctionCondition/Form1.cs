using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace FunctionCondition
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
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM tb_01", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds,"Table");
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
            if (textBox1.Text == ""||comboBox1.Text=="")
            {
                MessageBox.Show("文字框不能為空！");
                return;
            }
            SqlConnection cn = new SqlConnection("server=(local);database=db_10;Uid=sa;Pwd=");
            cn.Open();
            SqlDataAdapter dap = new SqlDataAdapter("SELECT 學生編號," + comboBox1.Text + " FROM tb_01 WHERE len(" + comboBox1.Text + ")=" + textBox1.Text, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "Table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}