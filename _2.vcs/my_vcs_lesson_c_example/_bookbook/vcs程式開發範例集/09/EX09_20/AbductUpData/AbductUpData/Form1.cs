using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace AbductUpData
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        DataTable dt = null;

        private void Form1_Load(object sender, EventArgs e)
        {
            showList();
        }

        private void tbExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
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
                this.tbUpdate.Enabled = true;
            }
        }

        private void tbUpdate_Click(object sender, EventArgs e)
        {
            if (Updateinfo())
            {
                MessageBox.Show("修改成功");
                this.tbUpdate.Enabled = false;
                //showList();
            }
            else
            {
                MessageBox.Show("修改失敗");
                return;
            }
        }

        private bool Updateinfo()
        {
            using (SqlCommand cmd = new SqlCommand())
            {
                try
                {
                    cmd.CommandText = "update 員工表 set 員工姓名='" + this.textBox2.Text + "',基本工資='" + this.textBox4.Text + "',工作評價='" + this.textBox5.Text + "' where 員工編號='" + this.textBox1.Text + "'";
                    con.Open();
                    cmd.Connection = con;
                    cmd.ExecuteNonQuery();
                    con.Close();
                    return true;
                }
                catch
                {
                    return false;
                }
            }
        }

        private void listView1_Click(object sender, EventArgs e)
        {
            string str = this.listView1.SelectedItems[0].Text.ToString();
            showInfo(str);
        }
    }
}
