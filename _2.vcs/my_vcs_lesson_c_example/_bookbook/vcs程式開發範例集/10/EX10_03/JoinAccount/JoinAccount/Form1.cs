using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace JoinAccount
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
            SqlDataAdapter dap = new SqlDataAdapter("SELECT 產品編號,產品名稱,產品單價,產品數量,(產品數量*產品單價) AS 總金額 FROM tb_03", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds,"Table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}