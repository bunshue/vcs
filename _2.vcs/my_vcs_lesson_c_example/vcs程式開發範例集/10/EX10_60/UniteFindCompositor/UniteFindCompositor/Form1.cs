using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace UniteFindCompositor
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
            SqlDataAdapter dap = new SqlDataAdapter("SELECT cast(成績 AS varchar(20)) AS 成績 FROM 學生成績表 UNION SELECT DISTINCT 課程編號 FROM 學生訊息表 UNION SELECT 課程名稱 FROM 課程表 WHERE 課程名稱 = '計算機英語' UNION SELECT CONVERT(varchar(20), 出勤率) FROM 學生考勤表 WHERE 出勤率 > 0.8 ORDER BY 成績 DESC", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("SELECT cast(成績 AS varchar(20)) AS 成績 FROM 學生成績表 UNION SELECT DISTINCT 課程編號 FROM 學生訊息表 UNION SELECT 課程名稱 FROM 課程表 WHERE 課程名稱 = '計算機英語' UNION SELECT CONVERT(varchar(20), 出勤率) FROM 學生考勤表 WHERE 出勤率 > 0.8", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}