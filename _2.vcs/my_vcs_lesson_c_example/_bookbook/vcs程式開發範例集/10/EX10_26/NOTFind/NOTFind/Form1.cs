using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace NOTFind
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
            SqlDataAdapter dap = new SqlDataAdapter("select * from tb_kf", cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "hotal");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
        private void dataGridViewBind(string sqlStr)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection cn = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter(sqlStr, cn);
            DataSet ds = new DataSet();
            dap.Fill(ds, "hotal");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            this.dataGridViewBind("select * from tb_kf where 房態='空房 '");
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            this.dataGridViewBind("select * from tb_kf where 房態='入住'");
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            this.dataGridViewBind("select * from tb_kf where 房態='空房 ' and not(價格 between 80 and 150 )");
        }
    }
}
