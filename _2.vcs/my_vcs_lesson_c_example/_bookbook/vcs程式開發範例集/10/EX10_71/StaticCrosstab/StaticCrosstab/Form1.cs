using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace StaticCrosstab
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
            SqlDataAdapter dap = new SqlDataAdapter("SELECT 所在部門, SUM(CASE 員工姓名 WHEN '李金明' THEN 銷售業績 ELSE NULL END)AS [李金明],SUM(CASE 員工姓名 WHEN '周可人' THEN 銷售業績 ELSE NULL END)as [周可人] ,SUM(CASE 員工姓名 WHEN '韓運' THEN 銷售業績 ELSE NULL END)AS [韓運],SUM(CASE 員工姓名 WHEN '司徒南' THEN 銷售業績 ELSE NULL END)AS [司徒南],SUM(CASE 員工姓名 WHEN '史佳金' THEN 銷售業績 ELSE NULL END)AS [史佳金]  FROM 銷售表 GROUP BY 所在部門", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("SELECT 員工姓名, SUM(CASE 所在部門 WHEN '食品部' THEN 銷售業績 ELSE NULL END) AS [食品部業績],SUM(CASE 所在部門 WHEN '家電部' THEN 銷售業績 ELSE NULL END) AS [家電部業績] FROM 銷售表 GROUP BY 員工姓名", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("SELECT * FROM 銷售表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}