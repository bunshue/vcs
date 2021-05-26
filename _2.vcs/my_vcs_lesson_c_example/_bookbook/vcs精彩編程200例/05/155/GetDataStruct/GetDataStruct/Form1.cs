using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.Data.Sql;

namespace GetDataStruct
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolStripTextBox1.Items.Clear();//清空列表
            //枚举本地网络中的SQL Server所有可用实例
            SqlDataSourceEnumerator instance = SqlDataSourceEnumerator.Instance;
            DataTable table = instance.GetDataSources();//获取所有数据源，并存储到DataTable中
            foreach (DataRow row in table.Rows)//遍历获取到的数据源
            {
                toolStripTextBox1.Items.Add(row["ServerName"]);//向列表中添加遍历到的服务器名
            }
            toolStripTextBox1.Text = "(local)";
            comboBox2.SelectedIndex = 0;
            toolStripTextBox3.TextBox.PasswordChar = '*';
        }

        private void toolStripTextBox2_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 13)
                toolStripTextBox3.Focus();
        }

        private void toolStripTextBox3_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 13)
                toolStripButton1_Click(sender, e);
        }

        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            try
            {
                string str = "Data Source=" + toolStripTextBox1.Text + ";database=master;Uid=" + toolStripTextBox2.Text + ";Pwd=" + toolStripTextBox3.Text + ";";
                comboBox1.DataSource = getTable(str, "select name from sysdatabases", "sysdatabases");
                comboBox1.DisplayMember = "name";
                comboBox1.ValueMember = "name";
                button1.Enabled = button2.Enabled = button3.Enabled = true;
            }
            catch { }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (comboBox1.Text != "")
            {
                listBox1.DataSource = null;
                listBox1.Items.Clear();
                string strCon = "Data Source=" + toolStripTextBox1.Text + ";DataBase=" + comboBox1.Text + ";uid=" + toolStripTextBox2.Text + ";pwd=" + toolStripTextBox3.Text;
                DataTable dt = null;
                if (comboBox2.Text == "数据表")
                {
                    dt = getTable(strCon, "SELECT name FROM sysobjects WHERE type = 'U' and name<>'dtproperties'", "sysobjects");
                }
                else if (comboBox2.Text == "视图")
                {
                    dt = getTable(strCon, "select name from sysobjects where xtype='v'", "sysobjects");
                }
                else if (comboBox2.Text == "存储过程")
                {
                    dt = getTable(strCon, "SELECT name FROM sysobjects WHERE xtype='p'", "sysobjects");
                }
                listBox1.DataSource = dt.DefaultView;
                listBox1.DisplayMember = "name";
            }
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            try
            {
                string strTableName = listBox1.SelectedValue.ToString();
                string strCon = "Data Source=" + toolStripTextBox1.Text + ";DataBase=" + comboBox1.Text + ";uid=" + toolStripTextBox2.Text + ";pwd=" + toolStripTextBox3.Text;
                using (SqlConnection con = new SqlConnection(strCon))
                {
                    string strSql = "select  name 字段名, xusertype 类型编号, length 长度 into hy_Linshibiao from  syscolumns  where id=object_id('" + listBox1.Text + "') ";
                    strSql += "select name 类型,xusertype 类型编号 into angel_Linshibiao from systypes where xusertype in (select xusertype from syscolumns where id=object_id('" + listBox1.Text + "'))";
                    con.Open();
                    SqlCommand cmd = new SqlCommand(strSql, con);
                    cmd.ExecuteNonQuery();
                    SqlDataAdapter da = new SqlDataAdapter("select 字段名,类型,长度 from hy_Linshibiao t,angel_Linshibiao b where t.类型编号=b.类型编号", con);
                    DataTable dt = new DataTable();
                    da.Fill(dt);
                    dataGridView1.DataSource = dt.DefaultView;
                    SqlCommand cmdnew = new SqlCommand("drop table hy_Linshibiao,angel_Linshibiao", con);
                    cmdnew.ExecuteNonQuery();
                    con.Close();
                }
            }
            catch { }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndices.Count > 0)
            {
                frmDataExport dataexport = new frmDataExport();
                dataexport.OutData = comboBox1.Text;
                dataexport.OutTable = listBox1.Text;
                dataexport.strserver = toolStripTextBox1.Text;
                dataexport.struser = toolStripTextBox2.Text;
                dataexport.strpwd = toolStripTextBox3.Text;
                dataexport.ShowDialog();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndices.Count > 0)
            {
                frmOutData outdata = new frmOutData();
                outdata.OutData = comboBox1.Text;
                outdata.OutTable = listBox1.Text;
                outdata.strserver = toolStripTextBox1.Text;
                outdata.struser = toolStripTextBox2.Text;
                outdata.strpwd = toolStripTextBox3.Text;
                outdata.ShowDialog();
            }
        }

        private void toolStripButton2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private DataTable getTable(string strCon, string strSql, string strTable)
        {
            try
            {
                SqlConnection sqlcon = new SqlConnection(strCon);
                SqlDataAdapter da = new SqlDataAdapter(strSql, sqlcon);
                DataTable dt = new DataTable(strTable);
                da.Fill(dt);
                return dt;
            }
            catch
            {
                return null;
            }
        }
    }
}
