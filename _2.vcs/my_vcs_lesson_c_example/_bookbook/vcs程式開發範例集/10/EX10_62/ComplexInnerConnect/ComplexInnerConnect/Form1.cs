using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace ComplexInnerConnect
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
            SqlDataAdapter dap = new SqlDataAdapter("SELECT 員工訊息表.員工編號, 員工訊息表.員工姓名, 員工工資表.基本工資, 加班訊息表.加班天數, 加班訊息表.加班費 FROM 員工訊息表 INNER JOIN 加班訊息表 ON 員工訊息表.員工編號 = 加班訊息表.員工編號 INNER JOIN 員工工資表 ON 加班訊息表.員工編號 = 員工工資表.員工編號", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}