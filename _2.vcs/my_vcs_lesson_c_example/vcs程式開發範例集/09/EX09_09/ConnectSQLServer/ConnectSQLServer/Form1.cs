using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace ConnectSQLServer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            try
            {
                string ConStr = "server=(local);user id=sa;pwd=;database=db_09";
                SqlConnection con = new SqlConnection(ConStr);
                string SqlStr = "select * from 帳單";
                SqlDataAdapter ada = new SqlDataAdapter(SqlStr, con);
                DataSet ds = new DataSet();
                ada.Fill(ds);
                this.dataGridView1.DataSource = ds.Tables[0].DefaultView;  
            }
            catch
            {
                return;
            }
        }
    }
}