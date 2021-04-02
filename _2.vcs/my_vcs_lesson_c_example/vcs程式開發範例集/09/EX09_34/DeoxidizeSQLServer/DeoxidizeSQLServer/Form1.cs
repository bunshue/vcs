using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;


namespace DeoxidizeSQLServer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
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

        private void button2_Click(object sender, EventArgs e)
        {
            if (this.openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                this.textBox1.Text = this.openFileDialog1.FileName;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Restore();
        }

        private void Restore()
        {
            string path = this.textBox1.Text; //獲得備份路徑及資料庫名稱
            string dbname = this.comboBox1.Text;
            string SqlStr1 = "Server=(local);database='" + this.comboBox1.Text + "';Uid=sa;Pwd=";
            string SqlStr2 = "use master restore database " + dbname + " from disk='" + path + "'";
            using (SqlConnection con = new SqlConnection(SqlStr1))
            {
                con.Open();
                try
                {
                    SqlCommand cmd = new SqlCommand(SqlStr2,con);
                    cmd.Connection = con;
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("還原數據成功");
                }
                catch (Exception error)
                {
                    MessageBox.Show("還原失敗，請確保還原項與庫對應");
                }
                finally
                {
                    con.Close();
                }
            }
        }
    }
}