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

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection con = new SqlConnection(cnstr))
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
                catch (Exception euy)
                {
                    MessageBox.Show(euy.Message);
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
