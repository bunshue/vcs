using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace ADO.NETWrite
{
    public partial class Form1 : Form
    {
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        public Form1()
        {
            InitializeComponent();
        }

        private void tbADD_Click(object sender, EventArgs e)
        {
            ControlInfo(true);
            this.textBox1.Enabled = false;
            con.Open();
            using (SqlCommand cmd = new SqlCommand("select Max(員工編號) from 員工表", con))
            {
                if (Convert.ToString(cmd.ExecuteScalar()) != "")
                {
                    string strID = Convert.ToString(cmd.ExecuteScalar());
                    this.textBox1.Text = strID.Substring(0, 1) + Convert.ToString(Convert.ToUInt32(strID.Substring(1)) + 1);
                }
                else
                {
                    this.textBox1.Text = "P1001";
                }
            }
            con.Close();

        }
        private void ControlInfo(Boolean B)
        {
            foreach (Control ct in this.groupBox1.Controls)
            {
                if (ct is TextBox)
                {
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

        private void Form1_Load(object sender, EventArgs e)
        {
            ControlInfo(false);
        }
        private void tbSave_Click(object sender, EventArgs e)
        {
            con.Open();
            using (SqlCommand command = new SqlCommand("INSERT INTO 員工表 " +
               "VALUES (@員工編號, @員工姓名,@基本工資,@工作評價)", con))
            {
                // Add the parameters for the InsertCommand.
                command.Parameters.Add("@員工編號", SqlDbType.VarChar, 50, "員工編號").Value = this.textBox1.Text;
                command.Parameters.Add("@員工姓名", SqlDbType.VarChar, 50, "員工姓名").Value = this.textBox2.Text;
                command.Parameters.Add("@基本工資", SqlDbType.Float, 8, "基本工資").Value = Convert.ToString(this.textBox4.Text);
                command.Parameters.Add("@工作評價", SqlDbType.VarChar, 50, "工作評價").Value = this.textBox5.Text;
                command.ExecuteNonQuery();
                MessageBox.Show("OK");
            }
            con.Close();
        }
    }
}