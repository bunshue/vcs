using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace ProcedureAdd
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
            SqlConnection con = new SqlConnection(cnstr);
            SqlDataAdapter dap = new SqlDataAdapter("select * from 員工訊息表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            SqlCommand cmd = new SqlCommand("procInsertEmployee", con);
            cmd.CommandType = CommandType.StoredProcedure;
            SqlParameter[] prams = {
						new SqlParameter("@員工編號",  SqlDbType.VarChar, 50),
                		new SqlParameter("@員工姓名",  SqlDbType.VarChar, 50),
                		new SqlParameter("@身份證號",  SqlDbType.VarChar, 50),
                        new SqlParameter("@聯繫電話",  SqlDbType.VarChar, 50) 
			};
            prams[0].Value = textBox1.Text;
            prams[1].Value = textBox2.Text;
            prams[2].Value = textBox3.Text;
            prams[3].Value = textBox4.Text;

            // 新增參數
            foreach (SqlParameter parameter in prams)
            {
                cmd.Parameters.Add(parameter);
            }
            cmd.ExecuteNonQuery();
            con.Close();
            this.Form1_Load(sender, e);
        }
    }
}

