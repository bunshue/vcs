using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace SQLServerDistill
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\_vcs200_db\db_20.mdf";
        //string filename = @"C:\______test_files\_vcs200_db\db_20_log.LDF";   another

        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton2.Checked == true)
            {
                textBox1.Enabled = true;
                textBox2.Enabled = true;
            }
            else
            {
                textBox1.Text = "";
                textBox2.Text = "";
                textBox1.Enabled = false;
                textBox2.Enabled = false;

            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            comboBox1.Text = "";
            comboBox2.Items.Clear();
            comboBox2.Enabled = false;
            comboBox3.Items.Clear();
            comboBox3.Enabled = false;
            radioButton1.Checked = false;
            radioButton2.Checked = false;
        }
        // 登录服务器
        private void button2_Click(object sender, EventArgs e)
        {
            if (comboBox1.Text == "")
            {
                MessageBox.Show("请选择服务器名称：");
                comboBox1.Focus();
                return;
            }// end if 
            else
            {

                if (radioButton1.Checked == false && radioButton2.Checked == false)
                {
                    MessageBox.Show("请选择登录方式");
                    return;
                }//
                //Windows身份验证
                if (radioButton1.Checked == true)
                {

                    SqlConnection con = getCon("master");
                    SqlCommand com = new SqlCommand("select name from sysdatabases", con);
                    SqlDataReader dr = com.ExecuteReader();
                    while (dr.Read())
                    {
                        comboBox2.Items.Add(dr[0].ToString());
                    }
                    dr.Close();
                    con.Close();
                    MessageBox.Show("登录成功");
                    comboBox2.Enabled = true;
                    comboBox3.Enabled = true;
                }// endi 
                //Server身份验证
                if (radioButton2.Checked == true)
                {
                    try
                    {
                        SqlConnection con = getCon("master");
                        SqlCommand com = new SqlCommand("select name from sysdatabases", con);
                        SqlDataReader dr = com.ExecuteReader();
                        while (dr.Read())
                        {
                            comboBox2.Items.Add(dr[0].ToString());
                        }
                        dr.Close();
                        con.Close();
                        MessageBox.Show("登录成功");
                        comboBox2.Enabled = true;
                        comboBox3.Enabled = true;

                    }
                    catch (Exception ee)
                    {
                        MessageBox.Show(ee.Message);
                    }
                }// end block if 
            }//
        }
        //提取表结构
        private void button3_Click(object sender, EventArgs e)
        {
            if (comboBox2.Text == "" && comboBox3.Text == "")
            {
                MessageBox.Show("请选择提取的表");
            }
            else
            {
                if (comboBox3.Text != "")//选择要提取的表
                {
                    SqlConnection con = getCon(comboBox2.Text);
                    SqlCommand com = new SqlCommand();
                    com.CommandText = "sp_mshelpcolumns";//存储过程名
                    com.CommandType = CommandType.StoredProcedure;
                    com.Connection = con;
                    com.Parameters.Add("@tablename", SqlDbType.NVarChar, 517);
                    com.Parameters["@tablename"].Value = comboBox3.Text;
                    SqlDataReader dr = com.ExecuteReader();
                    Form2 frm2 = new Form2(comboBox3.Text);
                    frm2.listView1.Items.Clear();
                    while (dr.Read())
                    {
                        ListViewItem lt = new ListViewItem(dr[0].ToString());
                        lt.SubItems.Add(dr[2].ToString());
                        lt.SubItems.Add(dr[3].ToString());
                        frm2.listView1.Items.Add(lt);
                    }
                    dr.Close();
                    con.Close();
                    frm2.Show();
                }

            }
        }//是以何种方式登录，是Windows集成方式，不是SQlserver方式。
        public SqlConnection getCon(string strDatabase)
        {
            SqlConnection con = null; ;
            if (radioButton1.Checked == true)
            {
                string strCOn = "Integrated Security=SSPI;Persist Security Info=False;Initial Catalog= '" + strDatabase + "';Data Source='" + comboBox1.Text + "'";
                con = new SqlConnection(strCOn);
                con.Open();
            }
            if (radioButton2.Checked == true)
            {
                string strcon = "server='" + comboBox1.Text + "';uid='" + textBox1.Text.Trim() + "';pwd='" + textBox2.Text + "';database='" + strDatabase + "'";
                con = new SqlConnection(strcon);
                con.Open();

            }
            return con;
        }//end block 
        public void getTables(string strDataBase, string U)
        {
            SqlConnection con = getCon(strDataBase);
            SqlCommand com = new SqlCommand("select name from sysobjects where Xtype='" + U + "'", con);
            SqlDataReader dr = com.ExecuteReader();
            comboBox3.Items.Clear();
            while (dr.Read())
            {
                comboBox3.Items.Add(dr[0].ToString());
            }//
            dr.Close();
            con.Close();
        }
        //填冲数据库中的表
        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox2.SelectedItem.ToString() != "")
            {
                getTables(comboBox2.SelectedItem.ToString(), "U");
            }
        }
    }
}
