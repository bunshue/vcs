using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace SQLDelete
{
    public partial class Form1 : Form
    {
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showinfo();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (SqlCommand cmd = new SqlCommand())
            {
                try
                {
                    con.Open();
                    cmd.Connection = con;
                    cmd.CommandText = this.textBox1.Text;
                    cmd.ExecuteNonQuery();
                    con.Close();
                    showinfo();
                    MessageBox.Show("刪除成功");
                    this.textBox1.Focus();
                    this.textBox1.SelectAll();
                }
                catch
                {
                    MessageBox.Show("SQL語句有誤");
                    this.textBox1.Focus();
                    this.textBox1.SelectAll();
                }
            }
        }

        private void showinfo()
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09"))
            {
                DataTable dt = new DataTable();
                SqlDataAdapter da = new SqlDataAdapter("select * from 員工表", con);
                da.Fill(dt);
                this.dataGridView1.DataSource = dt.DefaultView;
            }
        }
    }
}
