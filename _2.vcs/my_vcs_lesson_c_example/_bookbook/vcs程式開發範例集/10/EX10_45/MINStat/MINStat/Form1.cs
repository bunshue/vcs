using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace MINStat
{
    public partial class Form1 : Form
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\{0};Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_sell", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_sell where 銷價 in(select min(銷價) from tb_sell)", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_sell where 利潤 in(select min(利潤) from tb_sell)", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}
