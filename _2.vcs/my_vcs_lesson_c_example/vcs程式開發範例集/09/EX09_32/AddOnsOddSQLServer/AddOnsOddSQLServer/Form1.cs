using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace AddOnsOddSQLServer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {

            if (this.openFileDialog1.ShowDialog() == DialogResult.OK)
            { 
                if(this.openFileDialog1.FileName!="")
                {
                    this.textBox1.Text = this.openFileDialog1.FileName;
                    
                  
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (this.textBox2.Text != "")
            {
                fujia();
            }
            else
            {
                MessageBox.Show("請寫入資料庫名稱");
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
                    sb.Append("sp_attach_single_file_db @dbname='" + this.textBox2.Text + "',");
                    sb.Append("@physname='" + this.textBox1.Text + "'");

                    cmd.CommandText = sb.ToString();
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("附加成功");
                   
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