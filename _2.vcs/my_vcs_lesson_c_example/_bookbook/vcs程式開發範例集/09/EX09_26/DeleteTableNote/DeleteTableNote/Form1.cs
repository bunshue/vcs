using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace DeleteTableNote
{
    public partial class Form1 : Form
    {
        public static string str = "";

        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09.mdf;Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showinfo();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void dataGridView1_Click(object sender, EventArgs e)
        {
            str = this.dataGridView1.SelectedCells[0].Value.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("您確定要刪除本條訊息嗎？", "提示", MessageBoxButtons.YesNo, MessageBoxIcon.Warning) == DialogResult.Yes)
            {
                if (str != "")
                {
                    using (SqlConnection con = new SqlConnection(cnstr))
                    {
                        con.Open();
                        SqlCommand cmd = new SqlCommand("delete from 員工表 where 員工編號='" + str + "'", con);
                        cmd.Connection = con;
                        cmd.ExecuteNonQuery();
                        con.Close();
                        showinfo();
                        MessageBox.Show("刪除成功");
                    }
                }
            }
        }

        private void showinfo()
        {
            using (SqlConnection con = new SqlConnection(cnstr))
            {
                DataTable dt = new DataTable();
                SqlDataAdapter da = new SqlDataAdapter("select * from 員工表", con);
                da.Fill(dt);
                this.dataGridView1.DataSource = dt.DefaultView;
            }
        }
    }
}
