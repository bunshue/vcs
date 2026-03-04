using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace SeparateSQLServer
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
            biandingiInfo();
        }

        private void biandingiInfo()
        {
            string db_filename = "db_09_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            //using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=master"))
            using (SqlConnection con = new SqlConnection(cnstr))
            {
                DataTable dt = new DataTable();
                SqlDataAdapter da = new SqlDataAdapter("select name from sysdatabases", con);
                da.Fill(dt);
                this.comboBox1.DataSource = dt.DefaultView;
                this.comboBox1.DisplayMember = "name";
                this.comboBox1.ValueMember = "name";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //分離資料庫

            string db_filename = "db_09_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            //using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=master"))
            using (SqlConnection con = new SqlConnection(cnstr))
            {
                try
                {
                    SqlCommand cmd = new SqlCommand();
                    con.Open();
                    cmd.Connection = con;
                    cmd.CommandText = "sp_detach_db @dbname='" + this.comboBox1.Text + "'";
                    cmd.ExecuteNonQuery();
                    richTextBox1.Text += "分離成功\n";
                    //MessageBox.Show("分離成功");
                }
                catch (Exception ey)
                {
                    richTextBox1.Text += "分離失敗, 原因 : \n";
                    richTextBox1.Text += ey.Message + "\n";
                    //MessageBox.Show(ey.Message);
                }
            }
        }
    }
}
