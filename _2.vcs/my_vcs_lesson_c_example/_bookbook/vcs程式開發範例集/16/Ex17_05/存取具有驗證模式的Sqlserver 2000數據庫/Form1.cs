using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
namespace 存取具有驗證模式的Sqlserver_2000數據庫
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public SqlConnection con = null;//實義數據庫連接對像
        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == "")
            {
                MessageBox.Show(textBox1.Tag.ToString()+"不能為空","提示");
                textBox1.Focus();
                return;
            }
            if (textBox2.Text == "")
            {
                MessageBox.Show(textBox2.Tag.ToString() + "不能為空", "提示");
                textBox2.Focus();
                return;
            }
            if (textBox4.Text == "")
            {
                MessageBox.Show(textBox4.Tag.ToString() + "不能為空", "提示");
                textBox4.Focus();
                return;
            }
            try
            {
                string strcon = "server='" + textBox1.Text.Trim() + "';uid='" + textBox2.Text.Trim() + "';pwd='" + textBox3.Text + "';database='" + textBox4.Text.Trim() + "'";
                con = new SqlConnection(strcon);//實例SqlConnect對像
                con.Open();
                MessageBox.Show("登入成功");
            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message);
            }
        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (con.State == ConnectionState.Open)
            {
                con.Close();
                MessageBox.Show("連線已斷線");
            }
            else
            {
                MessageBox.Show("還沒有與資料庫連線");
            }
        }
    }
}