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
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showinf();
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
                    using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09"))
                    {
                        con.Open();
                        SqlCommand cmd = new SqlCommand("delete from 員工表 where 員工編號='" + str + "'", con);
                        cmd.Connection = con;
                        cmd.ExecuteNonQuery();
                        con.Close();
                        showinf();
                        MessageBox.Show("刪除成功");
                    }
                }
            }

        }

        private void showinf()
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09"))
            {
                DataTable dt = new DataTable();
                SqlDataAdapter da = new SqlDataAdapter("select * from 員工表", con);
                da.Fill(dt);
                this.dataGridView1.DataSource = dt.DefaultView;
            }
        }
    }
}