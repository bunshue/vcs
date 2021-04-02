using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace ORFind
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;uid=sa;pwd=;");
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_Score where Math_Score>95 or English_Score>95", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "book");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection("Server=(local);DataBase=db_10;uid=sa;pwd=;");
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_Score", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "book");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}