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
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
      
        }

        private void biandingiInfo()
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=master"))
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
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=master"))
            {
                try
                {
                    SqlCommand cmd = new SqlCommand();
                    con.Open();
                    cmd.Connection = con;
                    cmd.CommandText = "sp_detach_db @dbname='" + this.comboBox1.Text+"'";
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("分離成功");
                }
                catch(Exception ey)
                {
                    MessageBox.Show(ey.Message);
                }
            }
        }
    }
}