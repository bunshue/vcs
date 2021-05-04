using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace HavingMuchTable
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM 部門工資統計表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("SELECT 部門工資統計表.所屬部門, MAX(部門工資統計表.基本工資) AS 部門最高工資,SUM(員工請假表.請假天數) AS 合計請假天數, AVG(員工請假表.扣除金額) AS 平均扣除金額 FROM 部門工資統計表 INNER JOIN 員工請假表 ON 部門工資統計表.員工編號 = 員工請假表.員工編號 GROUP BY 部門工資統計表.所屬部門 HAVING (SUM(員工請假表.請假天數) < 10)", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}