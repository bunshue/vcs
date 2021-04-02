using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace SQLServerConfiguration
{
    public partial class Form1 : Form
    {
        string strDatabase = null;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.comboBox1.DataSource = Database();
            this.comboBox1.DisplayMember = "name";
            //this.comboBox1.ValueMember = "name";
        }

        private DataTable Database()
        {
            using (SqlConnection con = new SqlConnection("server=.;uid=sa;pwd=;database=master"))
            {
                SqlDataAdapter da = new SqlDataAdapter("select name from sysdatabases ", con);
                DataTable dt = new DataTable("sysdatabases");
                da.Fill(dt);
                return dt;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.dataGridView1.DataSource = null;
            strDatabase = this.comboBox1.Text.ToString();
            using (SqlConnection con = new SqlConnection("server=.;uid=sa;pwd=;database='" + strDatabase + "'"))
            {
                SqlDataAdapter da = new SqlDataAdapter("SELECT name FROM sysobjects WHERE type = 'U' and name<>'dtproperties' ", con);
                DataTable dt = new DataTable("sysobjects");
                da.Fill(dt);
                this.listBox1.DataSource = dt.DefaultView;
                this.listBox1.DisplayMember = "name";
                this.listBox1.ValueMember = "name";
            }
        }

        private void listBox1_Click(object sender, EventArgs e)
        {
            string strTableName = this.listBox1.SelectedValue.ToString();
            using (SqlConnection con = new SqlConnection("server=.;uid=sa;pwd=;database='" + strDatabase + "'"))
            {
                string strSql = "select  name 字段名, xusertype 類型編號, length 長度 into hy_Linshibiao from  syscolumns  where id=object_id('" + strTableName + "') ";
                strSql += "select name 類型,xusertype 類型編號 into angel_Linshibiao from systypes where xusertype in (select xusertype from syscolumns where id=object_id('" + strTableName + "'))";
                con.Open();
                SqlCommand cmd = new SqlCommand(strSql, con);
                cmd.ExecuteNonQuery();
                con.Close();

                SqlDataAdapter da = new SqlDataAdapter("select 字段名,類型,長度 from hy_Linshibiao t,angel_Linshibiao b where t.類型編號=b.類型編號", con);
                DataTable dt = new DataTable();
                da.Fill(dt);
                this.dataGridView1.DataSource = dt.DefaultView;

                SqlCommand cmdnew = new SqlCommand("drop table hy_Linshibiao,angel_Linshibiao", con);
                con.Open();
                cmdnew.ExecuteNonQuery();
                con.Close();

            }
        }
    }
}