using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace AddOnsSQLServer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (this.openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                this.textBox3.Text = this.openFileDialog1.FileName;
                this.button3.Enabled = true;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (this.openFileDialog2.ShowDialog() == DialogResult.OK)
            {
                this.textBox2.Text = this.openFileDialog2.FileName;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (this.textBox3.Text != "")
            {
                fujia();
            }
            else
            {
                MessageBox.Show("請輸入資料庫名");
            }
        }

        private void fujia()
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=master"))
            {
                try
                {
                    SqlCommand cmd = new SqlCommand();
                    con.Open();
                    cmd.Connection = con;
                    StringBuilder sb = new StringBuilder();
                    sb.Append("sp_attach_db @dbname='" + this.textBox1.Text + "',");
                    sb.Append("@filename1='" + this.textBox3.Text + "'");
                    if (this.textBox2.Text != "")
                    {
                        sb.Append(",@filename2='" + this.textBox2.Text + "'");
                    }
                    cmd.CommandText = sb.ToString();
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("附加成功");
                    this.button3.Enabled = false;
                }
                catch (Exception ety)
                {
                    MessageBox.Show(ety.Message);
                }

            }
        
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }


    }
}