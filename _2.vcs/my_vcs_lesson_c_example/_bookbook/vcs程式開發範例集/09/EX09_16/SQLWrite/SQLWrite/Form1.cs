using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace SQLWrite
{
    public partial class Form1 : Form
    {
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ControlInfo(false);
            showinfo();
        }

        private void showinfo()
        {
            using (SqlDataAdapter da = new SqlDataAdapter("select * from 員工表", con))
            {
                // DB => DA => DT => DV => DGV
                DataTable dt = new DataTable();
                da.Fill(dt);
                DataView dv = new DataView(dt);
                this.dataGridView1.DataSource = dv;
            }
        }

        private void tbADD_Click(object sender, EventArgs e)
        {
            ControlInfo(true);
            this.tbSave.Enabled = true;
            this.tbADD.Enabled = false;
        }

        private void ControlInfo(Boolean B)
        {
            foreach (Control ct in this.groupBox1.Controls)
            {
                if (ct is TextBox)
                {
                    ct.Text = "";
                    if (B)
                    {
                        ct.Enabled = true;
                    }
                    else
                    {
                        ct.Enabled = false;
                    }
                }
            }
        }

        private void tbSave_Click(object sender, EventArgs e)
        {
            StringBuilder strSQL = new StringBuilder();
            strSQL.Append("insert into 員工表(員工編號, 員工姓名,基本工資,工作評價)");
            strSQL.Append(" values('" + textBox1.Text.Trim().ToString() + "','" + textBox2.Text.Trim().ToString() + "',");
            strSQL.Append("'" + Convert.ToSingle(textBox4.Text.Trim().ToString()) + "','" + textBox5.Text.Trim().ToString() + "')");
            using (SqlCommand cmd = new SqlCommand(strSQL.ToString(), con))
            {
                con.Open();
                cmd.ExecuteNonQuery();
                MessageBox.Show("OK");
                ControlInfo(false);
                con.Close();
            }
            showinfo();
            strSQL.Remove(0, strSQL.Length);
            this.tbSave.Enabled = false;
            this.tbADD.Enabled = true;
        }
    }
}

