using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace ProcedureDelete
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("select * from 員工訊息表", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            con.Open();
            SqlCommand cmd = new SqlCommand("procDeleteEmployee", con);
            cmd.CommandType = CommandType.StoredProcedure;
            SqlParameter pares = new SqlParameter("@員工編號", SqlDbType.VarChar, 50);
            cmd.Parameters.Add(pares);
            cmd.Parameters["@員工編號"].Value = textBox1.Text;
            cmd.ExecuteNonQuery();
            con.Close();
            this.Form1_Load(sender, e);
        }
    }
}