using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace TriggerSystemDate
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            con.Open();
            SqlCommand cmd = new SqlCommand("update 系統管理員表 set 使用者名稱='" + textBox1.Text + "',密碼='" + textBox2.Text + "'", con);
            cmd.ExecuteNonQuery();
            con.Close();
            MessageBox.Show("修改成功！");
        }
    }
}