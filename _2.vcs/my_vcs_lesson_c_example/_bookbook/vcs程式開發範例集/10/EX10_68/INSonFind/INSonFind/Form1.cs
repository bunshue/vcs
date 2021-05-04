using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace INSonFind
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == "" || textBox2.Text == "")
            {
                MessageBox.Show("查詢內容不能為空！");
                if (textBox1.Text == "")
                {
                    textBox1.Focus();
                    return; ;
                }
                if (textBox2.Text == "") textBox2.Focus();
                return;
            }
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM 明細工資表 WHERE (基本工資 IN (SELECT 基本工資 FROM 明細工資表 WHERE 基本工資 > " + textBox1.Text + " AND 基本工資 < " + textBox2.Text + "))", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource=ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM 明細工資表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource=ds.Tables[0].DefaultView;
        }
    }
}