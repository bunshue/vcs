using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace ProcedureUpData
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        DataTable dt = null;

        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        private void Form1_Load(object sender, EventArgs e)
        {
            showList();
        }

        private void listView1_Click(object sender, EventArgs e)
        {
            string str = this.listView1.SelectedItems[0].Text.ToString();
            showInfo(str);
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {
            if (TextClear())
            {
                using (SqlCommand cmd = new SqlCommand())
                {
                    con.Open();
                    cmd.Connection = con;
                    cmd.CommandType = CommandType.StoredProcedure;
                    cmd.CommandText = "proc_Update";
                    SqlParameter[] par ={ 
                    new SqlParameter("@id",this.textBox1.Text), 
                    new SqlParameter("@name",this.textBox2.Text),
                    new SqlParameter("@money",this.textBox4.Text),
                    new SqlParameter("@talk",this.textBox5.Text)
                };
                    foreach (SqlParameter parms in par)
                    {
                        cmd.Parameters.Add(parms);
                    }
                    cmd.ExecuteNonQuery();
                    con.Close();
                    MessageBox.Show("修改成功");
                    showList();

                }
            }
            else
            {
                MessageBox.Show("請選擇訊息");
            }
        }
        private Boolean TextClear()
        {
            foreach (Control c in this.groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    if (c.Text == "")
                    { return false; }
                    else
                    { return true; }
                }
            }
            return true;
        }


        private void showList()
        {
            listView1.View = View.Details;//圖示
            listView1.GridLines = true;//網格線
            using (SqlDataAdapter da = new SqlDataAdapter("select * from 員工表", con))
            {
                //產生結果集
                dt = new DataTable();
                da.Fill(dt);
                ColumnHeader ch;
                for (int i = 0; i < dt.Columns.Count; i++)//列
                {
                    ch = new ColumnHeader();
                    ch.Text = dt.Columns[i].ColumnName.ToString();
                    ch.Name = dt.Columns[i].ColumnName.ToString();
                    ch.Width = 72;

                    this.listView1.Columns.Add(ch);
                }
                //建立結構
                Method(dt);
            }
        }

        private void Method(DataTable dt)
        {
            listView1.Items.Clear();
            ListViewItem listItem = null;
            for (int j = 0; j < dt.Rows.Count; j++)
            {
                listItem = new ListViewItem(dt.Rows[j][0].ToString());
                for (int k = 1; k < dt.Columns.Count; k++)
                {
                    listItem.SubItems.Add(dt.Rows[j][k].ToString());
                }
                listView1.Items.Add(listItem);
            }
        }

        private void showInfo(string strid)
        {
            using (SqlCommand cmd = new SqlCommand("select * from 員工表 where 員工編號='" + strid + "'", con))
            {
                con.Open();
                SqlDataReader dr = cmd.ExecuteReader();
                if (dr.HasRows)
                {
                    dr.Read();
                    this.textBox1.Text = dr[0].ToString();
                    this.textBox2.Text = dr[1].ToString();
                    this.textBox4.Text = dr[2].ToString();
                    this.textBox5.Text = dr[3].ToString();
                }
                dr.Close();
                con.Close();

            }
        }

    }
}