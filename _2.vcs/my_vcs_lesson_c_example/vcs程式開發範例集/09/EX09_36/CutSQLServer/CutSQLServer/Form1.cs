using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace CutSQLServer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=master"))
            {
                try
                {
                    string strShutdown = "SHUTDOWN WITH NOWAIT";
                    SqlCommand cmd = new SqlCommand();
                    cmd.Connection = con;
                    cmd.Connection.Open();
                    cmd.CommandText = strShutdown;
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("已成功斷開服務");
                }
                catch(Exception euy)
                {
                    MessageBox.Show(euy.Message);
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}