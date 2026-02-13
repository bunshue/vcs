using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace SQLUpData
{
    public partial class Form1 : Form
    {
        DataTable dt = null;

        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showList();
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
                    showList();
                    MessageBox.Show("成功修改");
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
    }
}
